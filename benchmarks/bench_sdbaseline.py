
import contextlib
import filecmp
import glob
import numpy as np
import os
import shutil
import unittest

from casatools import ctsys, table
from casatasks import sdbaseline
from casatasks.private.sdutil import table_manager
from casatasks.private.task_sdbaseline import check_fftthresh, is_empty, parse_wavenumber_param
from casatestutils import selection_syntax


tb = table()
ctsys_resolve = ctsys.resolve

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (1, 2, 30.0) # between 1 and 2 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 3            # amount of instances a "repeat block" is run to collect samples
min_run_count = 5     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap for duration of a single test execution

### Utilities for reading blparam file
class FileReader(object):
    def __init__(self, filename):
        self.__filename = filename
        self.__data = None
        self.__nline = None

    def read(self):
        if self.__data is None:
            f = open(self.__filename, 'r')
            self.__data = f.readlines()
            f.close()
            self.__nline = len(self.__data)
        return

    def nline(self):
        self.read()
        return self.__nline

    def index(self, txt, start):
        return self.__data[start:].index(txt) + 1 + start

    def getline(self, idx):
        return self.__data[idx]


class BlparamFileParser(FileReader):
    def __init__(self, blfile):
        FileReader.__init__(self, blfile)
        #self.__nrow = None
        #self.__coeff = None
        #self.__rms = None
        self.__ctxt = 'Baseline parameters\n'
        self.__rtxt = 'Results of baseline fit\n'

def remove_single_file_dir(filename):
    """
    Remove a single file or a single directory.
    For filename, '.' and those end with '..' (namely, '..', '../..' etc.)
    are not allowed.
    """
    if filename == '.' or filename[-2:] == '..':
        raise Exception("Caution! Attempting to remove '" + filename + "'!!")
    
    if os.path.exists(filename):
        if os.path.isdir(filename):
            shutil.rmtree(filename)
        else: # file or symlink
            os.remove(filename)


def remove_files_dirs(filename):
    """
    Remove files/directories/symlinks 'filename*'.
    For filename, '', '.' and those end with '..' (namely, '..', '../..' etc.)
    are not allowed.
    """
    if filename == '.' or filename[-2:] == '..':
        raise Exception("Caution! Attempting to remove '" + filename + "*'!!")
    elif filename == '':
        raise Exception("The parameter 'filename' must not be a null string.")
    
    filenames = glob.glob('{}*'.format(filename.rstrip('/')))

    for filename in filenames:
        remove_single_file_dir(filename)

def _get_num_files_by_keyword(cmpresult, keyword):
    return len(sum([eval(s[s.index(':')+1:]) for s in cmpresult if s.startswith(keyword)], []))


class sdbaseline_unittest_base(unittest.TestCase):
    """
    Base class for sdbaseline unit test
    """
    # Data path of input/output
    datapath = ctsys_resolve('unittest/sdbaseline/')
    taskname = "sdbaseline"
    verboselog = False

    #complist = ['max','min','rms','median','stddev']

    blparam_order = ['row', 'pol', 'mask', 'nclip', 'cthre',
                     'uself', 'lthre', 'ledge', 'redge', 'chavg',
                     'btype', 'order', 'npiec', 'nwave']
    blparam_dic = {}
    blparam_dic['row']   = [0, 0, 1, 1, 2, 2, 3, 3]
    blparam_dic['pol']   = [0, 1, 0, 1, 0, 1, 0, 1]
    #blparam_dic['mask']  = ['0~4000;6000~8000']*3 + ['']*5
    blparam_dic['mask']  = ['500~2500;5000~7500']*8
    blparam_dic['nclip'] = [0]*8
    blparam_dic['cthre'] = ['3.']*8
    blparam_dic['uself'] = ['false']*4 + ['true'] + ['false']*3
    blparam_dic['lthre'] = ['0.']*4 + ['3.', '', '', '0.']
    blparam_dic['ledge'] = [0]*4 + [10, 50, '', 0]
    blparam_dic['redge'] = [0]*4 + [10, 50, '', 0]
    blparam_dic['chavg'] = [0]*4 + [4, '', '', 0]
    blparam_dic['btype'] = ['poly'] + ['chebyshev']*2 + ['poly', 'chebyshev', 'poly'] + ['cspline']*2
    blparam_dic['order'] = [0, 0, 1, 1, 2, 2, '', '']
    blparam_dic['npiec'] = [0]*6 + [1]*2
    blparam_dic['nwave'] = [[]]*3 + ['']*2 + [[]]*3

    ### helper functions for tests ###
    def _createBlparamFile(self, file, param_order, val, option=''):
        nspec = 8
        f = open(file, 'w')
        assert(len(param_order) == len(val.keys()))
        for key in val.keys():
            assert(len(val[key]) == nspec)
        for i in range(nspec):
            do_write = True
            s = ''
            for key in param_order:
                v = val[key][i]
                if key == 'nwave':
                    if v != '':
                        s += ','
                        s += str(v)
                else:
                    s += str(v)
                    if key != 'npiec': s += ','
            s += '\n'
            if (option == 'r2p1less') and (val['row'][i] == 2) and (val['pol'][i] == 1):
                do_write = False
            if (option == 'r2p1cout') and (val['row'][i] == 2) and (val['pol'][i] == 1):
                s = '#' + s
            if do_write:
                f.write(s)
        f.close()

    def _remove(self, names):
        """
        Remove a list of files and directories from disk
        """
        for name in names:
            remove_single_file_dir(name)

    def _copy(self, names, from_dir=None, dest_dir=None):
        """
        Copy a list of files and directories from a directory (from_dir) to
        another (dest_dir) in the same name.
        
        names : a list of files and directories to copy
        from_dir : a path to directory from which search and copy files
                   and directories (the default is the current path)
        to_dir   : a path to directory to which copy files and directories
                   (the default is the current path)
        NOTE: it is not allowed to specify
        """
        # Check for paths
        if from_dir==None and dest_dir==None:
            raise ValueError("Can not copy files to exactly the same path.")
        from_path = os.path.abspath("." if from_dir==None else from_dir.rstrip("/"))
        to_path = os.path.abspath("." if dest_dir==None else dest_dir.rstrip("/"))
        if from_path == to_path:
            raise ValueError("Can not copy files to exactly the same path.")
        # Copy a list of files and directories
        for name in names:
            from_name = from_path + "/" + name
            to_name = to_path + "/" + name
            if os.path.exists(from_name):
                if os.path.isdir(from_name):
                    shutil.copytree(from_name, to_name)
                else:
                    shutil.copyfile(from_name, to_name)
                if self.verboselog:
                    casalog.post("Copying '%s' FROM %s TO %s" % (name, from_path, to_path))
            else:
                casalog.post("Could not find '%s'...skipping copy" % from_name, 'WARN')
    

class sdbaseline_basicTest(sdbaseline_unittest_base):
    """
    Basic unit tests for task sdbaseline. No interactive testing.

    List of tests:
    test000 --- default values for all parameters
    test001 --- polynominal baselining with no mask (maskmode = 'list'). spw and pol specified.
    test002 --- Chebyshev polynominal baselining with no mask (maskmode = 'list'). spw and pol specified.
    test003 --- cubic spline baselining with no mask (maskmode = 'list'). spw and pol specified.
    test050 --- existing file as outfile with overwrite=False (raises an exception)
    test051 --- no data after selection (raises an exception)
    test060 --- blparam files should be overwritten when overwrite=True in fit mode
    test061 --- blparam files should not exist when overwrite=False in fit mode
    test062 --- blparam files should not be removed in apply mode
    test070 --- no output MS when dosubtract=False
    test071 --- dosubtract=False and blformat is empty (raises an exception)
    test080 --- existent outfile is not overwritten if dosubtract=False

    Note: The input data 'OrionS_rawACSmod_calave.ms' is generated
          from a single dish regression data 'OrionS_rawACSmod' as follows:
          
          sdcal(infile='OrionS_rawACSmod',scanlist=[20,21,22,23],
                calmode='ps',tau=0.09,outfile='temp.asap')
          sdcal(infile='temp.asap',timeaverage=True,
                tweight='tintsys',outfile='temp2.asap')
          sdsave(infile='temp2.asap',outformat='MS2',
                 outfile='OrionS_rawACSmod_calave.ms')
    """
    # Input and output names
    
    infile = 'OrionS_rawACSmod_calave.ms'
    outroot = sdbaseline_unittest_base.taskname+'_basictest'
    blrefroot = os.path.join(sdbaseline_unittest_base.datapath,'refblparam')
    tid = None

    def setUp(self):
        if os.path.exists(self.infile):
            shutil.rmtree(self.infile)
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile)

        if os.path.exists(self.infile+'_blparam.txt'):
            os.remove(self.infile+ '_blparam.txt')
        if os.path.exists(self.infile+'_blparam.csv'):
            os.remove(self.infile+ '_blparam.csv')
        if os.path.exists(self.infile+'_blparam.btable'):
            shutil.rmtree(self.infile+ '_blparam.btable')

    def tearDown(self):
        remove_files_dirs(self.infile)
        remove_files_dirs(self.outroot)
    

    def time_test000(self):
        """Basic Test 000: default values for all parameters"""
        tid = '000'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'float_data'
        
        result = sdbaseline(infile=infile, datacolumn=datacolumn, outfile=outfile)

    def time_test001(self):
        """Basic Test 001: simple successful case: blfunc = 'poly', maskmode = 'list' and masklist=[] (no mask)"""
        tid = '001'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'float_data'
        maskmode = 'list'
        blfunc = 'poly'
        spw = '3'
        pol = 'LL'
        overwrite = True
        result = sdbaseline(infile=infile, datacolumn=datacolumn,
                             maskmode=maskmode, blfunc=blfunc,
                             spw=spw, pol=pol, outfile=outfile,
                             overwrite=overwrite)

    def time_test001_uppercase_params(self):
        """Basic Test 001: simple successful case: blfunc = 'poly', maskmode = 'list' and masklist=[] (no mask)"""
        tid = '001'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'FLOAT_DATA'
        maskmode = 'LIST'
        blfunc = 'POLY'
        spw = '3'
        pol = 'LL'
        overwrite = True
        result = sdbaseline(infile=infile, datacolumn=datacolumn,
                             maskmode=maskmode, blfunc=blfunc,
                             spw=spw, pol=pol, outfile=outfile,
                             overwrite=overwrite)
    
    def time_test002(self):
        """Basic Test 002: simple successful case: blfunc = 'chebyshev', maskmode = 'list' and masklist=[] (no mask)"""
        tid = '002'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'float_data'
        maskmode = 'list'
        blfunc = 'chebyshev'
        spw = '3'
        pol = 'LL'
        overwrite = True
        result = sdbaseline(infile=infile, datacolumn=datacolumn,
                             maskmode=maskmode, blfunc=blfunc,
                             spw=spw, pol=pol, outfile=outfile,
                             overwrite=overwrite)
    
    
    def time_test003(self):
        """Basic Test 003: simple successful case: blfunc = 'cspline', maskmode = 'list' and masklist=[] (no mask)"""
        print("")

        tid = '003'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'float_data'
        maskmode = 'list'
        blfunc = 'cspline'
        overwrite = True
        npiece = 3
        spw='3'
        pol='LL'
        result = sdbaseline(infile=infile, datacolumn=datacolumn,
                             maskmode=maskmode, blfunc=blfunc,
                             npiece=npiece,spw=spw,
                             pol=pol,
                             outfile=outfile,overwrite=overwrite)

    def time_test050(self):
        """Basic Test 050: failure case: existing file as outfile with overwrite=False"""
        infile = self.infile
        outfile = 'Dummy_Empty.ms'
        mode = 'list'
        os.mkdir(outfile)
        try:
            result = sdbaseline(infile=infile, outfile=outfile, overwrite=False, maskmode=mode)
        except Exception as e:
            pos = str(e).find("outfile='" + outfile + "' exists, and cannot overwrite it.")
        finally:
            shutil.rmtree(outfile)

    def time_test051(self):
        """Basic Test 051: failure case: no data after selection"""
        tid = '051'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        spw = '10' # non-existent IF value
        mode = 'list'
        #sdbaseline(infile=infile, outfile=outfile, spw=spw, maskmode=mode)
        
        try:
            sdbaseline(infile=infile, outfile=outfile, spw=spw, maskmode=mode)
        except Exception as e:
            print('error')
            #self.assertIn('Spw Expression: No match found for 10,', str(e))

    def time_test060(self):
        """Basic Test 060: blparam file(s) should be overwritten when overwrite=True in fit mode"""
        tid = '060'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        overwrite = False
        datacolumn = 'float_data'

        # First run
        sdbaseline(infile=infile, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn)

        shutil.rmtree(outfile)

        overwrite = True
        sdbaseline(infile=infile, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn)

    def time_test061(self):
        """Basic Test 061: blparam file(s) should not exist when overwrite=False in fit mode """
        tid = '061'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        overwrite = False
        datacolumn = 'float_data'

        # First run
        sdbaseline(infile=infile, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn)

        # Keep blparam.txt, and remove outfile only
        shutil.rmtree(outfile)

        # Second run (in fit mode, overwrite=False), which must emit ValueError
        with self.assertRaises(ValueError, msg='{}_blparam.txt exists.'.format(infile)):
            sdbaseline(infile=infile, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn)

    def time_test062(self):
        """Basic Test 062: blparam file(s) should not be removed in apply mode"""
        tid = '062'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        overwrite = False
        datacolumn = 'float_data'
        blmode = 'fit'
        blformat = ['text', 'table']

        # First run
        sdbaseline(infile=infile, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn, blmode=blmode, blformat=blformat)

        # Keep blparam files, and remove outfile only
        shutil.rmtree(outfile)

        # Second run (in apply mode), which must be successful
        blmode = 'apply'
        bltable = infile + '_blparam.bltable'
        overwrite = True
        sdbaseline(infile=infile, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn, blmode=blmode, bltable=bltable)

    def time_test070(self):
        """Basic Test 070: no output MS when dosubtract=False"""
        tid = '070'
        infile = self.infile
        outfile = self.outroot + tid + '.ms'
        datacolumn = 'float_data'
        dosubtract = False
        blformats = ['text', 'csv', 'table', ['text', 'table'], ['text', ''], ['text', 'csv', 'table']]

        for blformat in blformats:
            remove_files_dirs(infile+'_blparam.')
            remove_single_file_dir(outfile)
            sdbaseline(infile=infile, datacolumn=datacolumn, outfile=outfile, dosubtract=dosubtract, blformat=blformat)

    def time_test071(self):
        """Basic Test 071: dosubtract=False and blformat is empty (raises an exception)"""
        tid = '071'
        infile = self.infile
        outfile = self.outroot + tid + '.ms'
        datacolumn = 'float_data'
        dosubtract = False
        blformats = ['', [], ['', '', '']]

        for blformat in blformats:
            with self.assertRaises(ValueError, msg="blformat must be specified when dosubtract is False"):
                sdbaseline(infile=infile, datacolumn=datacolumn, outfile=outfile, dosubtract=dosubtract, blformat=blformat)

    def time_test080(self):
        """Basic Test 080: existent outfile is not overwritten if dosubtract=False"""
        tid = '080'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        dosubtract = False
        overwrite = False
        datacolumn = 'float_data'

        shutil.copytree(infile, outfile)

        # Run sdbaseline with dosubtract=False
        sdbaseline(infile=infile, outfile=outfile, dosubtract=dosubtract, overwrite=overwrite, datacolumn=datacolumn)

class sdbaseline_maskTest(sdbaseline_unittest_base):
    """
    Tests for various mask selections. No interactive testing.

    List of tests:
    test100 --- with masked ranges at the edges of spectrum. blfunc is cspline.
    test101 --- with masked ranges not touching spectrum edge

    Note: input data is generated from a single dish regression data,
    'OrionS_rawACSmod', as follows:
      sdcal(infile='OrionS_rawACSmod',scanlist=[20,21,22,23],
                calmode='ps',tau=0.09,outfile='temp.asap')
      sdcal(infile='temp.asap',timeaverage=True,
                tweight='tintsys',outfile='temp2.asap')
      sdsave(infile='temp2.asap',outformat='MS2',
                outfile='OrionS_rawACSmod_calave.ms')
    """
    # Input and output names
    infile = 'OrionS_rawACSmod_calave.ms'
    outroot = sdbaseline_unittest_base.taskname+'_masktest'
    blrefroot = os.path.join(sdbaseline_unittest_base.datapath,'refblparam_mask')
    tid = None

    # Channel range excluding bad edge
    search = [[200,7599]]
    # Baseline channels. should be identical to one selected by 'auto' mode
    blchan2 = [[200,2959],[3120,7599]]
     
    def setUp(self):
        if os.path.exists(self.infile):
            shutil.rmtree(self.infile)
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile)

        if os.path.exists(self.infile+'_blparam.txt'):
            os.remove(self.infile+ '_blparam.txt')
        if os.path.exists(self.infile+'_blparam.csv'):
            os.remove(self.infile+ '_blparam.csv')
        if os.path.exists(self.infile+'_blparam.btable'):
            shutil.rmtree(self.infile+ '_blparam.btable')




    def tearDown(self):
        remove_files_dirs(self.infile)
        remove_files_dirs(self.outroot)

    def time_test100(self):
        """Mask Test 100: with masked ranges at the edges of spectrum. blfunc must be cspline."""
        self.tid='100'
        infile = self.infile
        outfile = self.outroot+self.tid+'.ms'
        datacolumn='float_data'
        mode = 'list'
        spw = '2:%s'%(';'.join(map(self._get_range_in_string,self.search)))
        pol = 'RR'
        blfunc = 'cspline'
        npiece = 4

        result = sdbaseline(infile=infile,datacolumn=datacolumn,maskmode=mode,
                             spw=spw,pol=pol,blfunc=blfunc,npiece=npiece,
                             outfile=outfile)

    def time_test101(self):
        """Mask Test 101: with masked ranges not touching spectrum edge"""
        self.tid='101'
        infile = self.infile
        outfile = self.outroot+self.tid+'.ms'
        datacolumn='float_data'
        mode = 'list'
        spw = '2:%s'%(';'.join(map(self._get_range_in_string,self.blchan2)))
        pol = 'RR'

        result = sdbaseline(infile=infile,datacolumn=datacolumn,maskmode=mode,
                            outfile=outfile,spw=spw,pol=pol)


    def _get_range_in_string(self, valrange):
        if isinstance(valrange, list) or isinstance(valrange, tuple):
            return str(valrange[0])+'~'+str(valrange[1])
        else:
            return False

class sdbaseline_outbltableTest(sdbaseline_unittest_base):
    """
    Tests for outputting baseline table

    List of tests
    test302 --- blmode='fit', bloutput!='', dosubtract=True, blfunc='variable'
                (variable fit in MS, bltable is written)
                testing 3 cases:
                    (1) blparam contains values for all spectra
                    (2) no values for a spectrum (row=2,pol=1), which is to be skipped
                    (3) values commented out for a spectrum (row=2,pol=1), which is to be skipped
    test304 --- same as test303, but for blfunc='variable'

    Note: input data is generated from a single dish regression data,
    'OrionS_rawACSmod', as follows:
      sdcal(infile='OrionS_rawACSmod',scanlist=[20,21,22,23],
                calmode='ps',tau=0.09,outfile='temp.asap')
      sdcal(infile='temp.asap',timeaverage=True,
                tweight='tintsys',outfile='temp2.asap')
      sdsave(infile='temp2.asap',outformat='MS2',
                outfile='OrionS_rawACSmod_calave.ms')
    """
    # Input and output names
    infile = 'OrionS_rawACSmod_calave.ms'
    outroot = sdbaseline_unittest_base.taskname+'_bltabletest'
    tid = None
    ftype = {'poly': 0, 'chebyshev': 1, 'cspline': 2, 'sinusoid': 3}

    def setUp(self):
        if os.path.exists(self.infile):
            shutil.rmtree(self.infile)
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile)

        if os.path.exists(self.infile+'_blparam.txt'):
            os.remove(self.infile+ '_blparam.txt')
        if os.path.exists(self.infile+'_blparam.csv'):
            os.remove(self.infile+ '_blparam.csv')
        if os.path.exists(self.infile+'_blparam.btable'):
            shutil.rmtree(self.infile+ '_blparam.btable')


    def tearDown(self):
        remove_single_file_dir(self.infile)
        remove_files_dirs(self.outroot)

    def time_test302(self):
        """test302: per-spectrum baselining, output bltable"""
        self.tid='302'
        infile = self.infile
        datacolumn='float_data'
        blmode='fit'
        blformat='table'
        blfunc='variable'
        dosubtract=True

        for option in ['', 'r2p1less', 'r2p1cout']:
            bloutput= self.outroot+self.tid+option+'.bltable'
            outfile = self.outroot+self.tid+option+'.ms'
            blparam = self.outroot+self.tid+option+'.blparam'
            self._createBlparamFile(blparam, self.blparam_order, self.blparam_dic, option)
            result = sdbaseline(infile=infile,datacolumn=datacolumn,
                                 blmode=blmode,blformat=blformat,bloutput=bloutput,
                                 blfunc=blfunc,blparam=blparam,
                                 dosubtract=dosubtract,outfile=outfile)

    
    def time_test304(self):
        """test304: testing shortening baseline table for blfunc=variable"""
        self.tid = '304'
        infile = self.infile
        datacolumn='float_data'
        spw=''
        blmode='fit'
        blformat='table'
        blfunc='variable'
        dosubtract=True
        with table_manager(infile) as tb:
            nrow_data = tb.nrows()
            
        testmode = ['masked_masked', 'masked_unselect', 'unselect_masked']
        prange = [[0,1], [0], [1]]
        polval = ['', 'RR', 'LL']
        for j in range(len(testmode)):
            print('testing blfunc='+blfunc+', testmode='+testmode[j]+'...')
            # prepare input data
            if os.path.exists(self.infile):
                shutil.rmtree(self.infile)
            shutil.copytree(os.path.join(self.datapath,self.infile), self.infile)

            blparam = self.outroot+'.blparam'
            self._createBlparamFile(blparam, self.blparam_order, self.blparam_dic, '')

            tb.open(tablename=infile, nomodify=False)
            r2msk = tb.getcell('FLAG', 2)
            for ipol in prange[j]:
                for ichan in range(len(r2msk[0])):
                    r2msk[ipol][ichan] = True
            tb.putcell('FLAG', 2, r2msk)
            tb.close()
            pol = polval[j]

            outfile = self.outroot+self.tid+blfunc+'.ms'
            bloutput= self.outroot+self.tid+blfunc+'.bltable'
            sdbaseline(infile=infile,datacolumn=datacolumn,
                                blmode=blmode,blformat=blformat,bloutput=bloutput,
                                spw=spw,pol=pol,blfunc=blfunc,blparam=blparam,
                                dosubtract=dosubtract,outfile=outfile)
            if (os.path.exists(self.infile)):
                shutil.rmtree(self.infile)
            os.system('rm -rf ' + self.outroot + '*')
                                 

class sdbaseline_variableTest(sdbaseline_unittest_base):
    """
    Tests for blfunc='variable'
    List of tests necessary
    00: test baseline subtraction with variable baseline functions and orders
    """
    outfile='variable_bl.ms'
    column='float_data'
    nspec = 4
    infile = 'analytic_variable.ms'
    
    def setUp(self):
        pass
        #if hasattr(self, 'infile'):
            #self.__refetch_files(self.infile)

    def tearDown(self):
        remove_files_dirs(os.path.splitext(self.infile)[0])
        remove_single_file_dir(self.outfile)

    def _refetch_files(self, files, from_dir=None):
        if type(files)==str:
            files = [files]
        self._remove(files)
        self._copy(files, from_dir)
    
    def time_testVariable00(self):
        """Test blfunc='variable' with variable baseline functions and orders"""
        print('why is this failing?')
        infile = 'analytic_variable.ms'
        self.paramfile = 'analytic_variable_blparam.txt'
        self._refetch_files([infile, self.paramfile], self.datapath)
        sdbaseline(infile=infile, blfunc='variable', outfile=self.outfile, blparam=self.paramfile, datacolumn=self.column)


class sdbaseline_updateweightTest(sdbaseline_unittest_base):
    """
    Tests for updateweight=True
    to confirm if WEIGHT_SPECTRUM column is removed
    """

    datapath = ctsys_resolve('unittest/sdbaseline/')
    infile = 'uid___A002_X6218fb_X264.ms'
    outroot = sdbaseline_unittest_base.taskname+'_updateweighttest'
    outfile = outroot + '.ms'

    def setUp(self):
        remove_files_dirs(self.infile)
        shutil.copytree(os.path.join(self.datapath, self.infile), self.infile)

    def tearDown(self):
        remove_files_dirs(self.infile)
        remove_files_dirs(self.outroot)

    def time_test000(self):
        sdbaseline(infile=self.infile, outfile=self.outfile, intent='OBSERVE_TARGET#ON_SOURCE', spw='9', datacolumn='data', updateweight=True)


class sdbaseline_updateweightTest2(sdbaseline_unittest_base):
    """
    Tests for updateweight=True cases
    test052 --- blmode='apply', spw to flag channels 4500-6499
    """

    datapath = ctsys_resolve('unittest/sdbaseline/')
    infile = 'analytic_order3_withoffset.ms'
    outroot = sdbaseline_unittest_base.taskname + '_updateweighttest'
    outfile = outroot + '.ms'
    spw = '*:0~4499;6500~8191'

    def setUp(self):
        remove_files_dirs(self.infile)
        shutil.copytree(os.path.join(self.datapath, self.infile), self.infile)

    def tearDown(self):
        remove_files_dirs(self.infile)
        remove_files_dirs(self.outroot)

    def time_test052(self):
        sdbaseline(infile=self.infile, outfile=self.outfile, intent='OBSERVE_TARGET#ON_SOURCE', datacolumn='float_data', spw=self.spw)

if __name__ == '__main__':
    unittest.main()

