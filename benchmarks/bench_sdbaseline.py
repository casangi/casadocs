import glob
import os
import shutil

from casatools import ctsys, table
from casatasks import sdbaseline
from casatasks.private.sdutil import table_manager

tb = table()
ctsys_resolve = ctsys.resolve

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (1, 2, 30.0) # between 1 and 2 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 3            # amount of instances a "repeat block" is run to collect samples
min_run_count = 5     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap for duration of a single test execution

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
        

class BaseSetup():
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
    

class Basic(BaseSetup):
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
    infile_overwrite = 'OrionS_rawACSmod_calave_overwrite.ms'
    infile_no_remove = 'OrionS_rawACSmod_calave_no_remove.ms'
    outroot = BaseSetup.taskname+'_basictest'
    blrefroot = os.path.join(BaseSetup.datapath,'refblparam')
    tid = None
    outfile_overwrite = outroot+'060'+'.ms'
    outfile_no_remove = outroot+'062'+'.ms'
    
    def setup_cache(self):
        if os.path.exists(self.infile_no_remove):
            shutil.rmtree(self.infile_no_remove)
        if os.path.exists(self.infile_no_remove):
            shutil.rmtree(self.infile_overwrite)
            
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile_overwrite)
        
        sdbaseline(infile=self.infile_overwrite, outfile=self.outfile_overwrite, overwrite=False, datacolumn='float_data')
        shutil.rmtree(self.outfile_overwrite)
        
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile_no_remove)
            
        sdbaseline(infile=self.infile_no_remove, outfile=self.outfile_no_remove, overwrite=False, datacolumn='float_data', blmode='fit', blformat=['text', 'table'])
        shutil.rmtree(self.outfile_no_remove)

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
        
    def no_remove_deco(func):
        def wrapper(self):
            tid = '062'
            infile = self.infile
            outfile = self.outroot+tid+'.ms'
            sdbaseline(infile=infile, outfile=outfile, overwrite=False, datacolumn='float_data', blmode='fit', blformat=['text', 'table'])
            shutil.rmtree(outfile)
            func()
        return wrapper
    

    def time_default(self):
        """sdbaseline: default values for all parameters - test000"""
        tid = '000'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'float_data'
        
        result = sdbaseline(infile=infile, datacolumn=datacolumn, outfile=outfile)
    time_default.version = "CAS-13981"

    def time_poly_blfunc_no_mask(self):
        """sdbaseline: simple successful case: blfunc = 'poly', maskmode = 'list' and masklist=[] (no mask) - test001"""
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
    time_poly_blfunc_no_mask.version = "CAS-13981"
    
    def time_chebyshev_blfunc_no_mask(self):
        """sdbaseline: simple successful case: blfunc = 'chebyshev', maskmode = 'list' and masklist=[] (no mask) - test002"""
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
    time_chebyshev_blfunc_no_mask.version = "CAS-13981"
    
    def time_cspline_blfunc_no_mask(self):
        """sdbaseline: simple successful case: blfunc = 'cspline', maskmode = 'list' and masklist=[] (no mask) - test003"""
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
    time_cspline_blfunc_no_mask.version = "CAS-13981"

    def time_blparam_overwrite(self):
        """sdbaseline: blparam file(s) should be overwritten when overwrite=True in fit mode - test060"""
        tid = '060'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'float_data'
        overwrite = True
        
        sdbaseline(infile=self.infile_overwrite, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn)
    time_blparam_overwrite.version = "CAS-13981"

    def time_blparam_apply_no_remove(self):
        """sdbaseline: blparam file(s) should not be removed in apply mode - test062"""
        tid = '062'
        infile = self.infile
        outfile = self.outroot+tid+'.ms'
        datacolumn = 'float_data'
        blformat = ['text', 'table']
        blmode = 'apply'
        bltable = self.infile_no_remove + '_blparam.bltable'
        overwrite = True
        
        sdbaseline(infile=self.infile_no_remove, outfile=outfile, overwrite=overwrite, datacolumn=datacolumn, blmode=blmode, bltable=bltable)
    time_blparam_apply_no_remove.version = "CAS-13981"


class Mask(BaseSetup):
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
    outroot = BaseSetup.taskname+'_masktest'
    blrefroot = os.path.join(BaseSetup.datapath,'refblparam_mask')
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

    def time_cspline_blfunc_masked_range_spectrum_edge(self):
        """sdbaseline: with masked ranges at the edges of spectrum. blfunc must be cspline. - test100"""
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
     time_cspline_blfunc_masked_range_spectrum_edge.version = "CAS-13981"

    def time_masked_ranges_no_edge_spectrum(self):
        """sdbaaseline: with masked ranges not touching spectrum edge - test101"""
        self.tid='101'
        infile = self.infile
        outfile = self.outroot+self.tid+'.ms'
        datacolumn='float_data'
        mode = 'list'
        spw = '2:%s'%(';'.join(map(self._get_range_in_string,self.blchan2)))
        pol = 'RR'

        result = sdbaseline(infile=infile,datacolumn=datacolumn,maskmode=mode,
                            outfile=outfile,spw=spw,pol=pol)
    time_masked_ranges_no_edge_spectrum.version = "CAS-13981"

    def _get_range_in_string(self, valrange):
        if isinstance(valrange, list) or isinstance(valrange, tuple):
            return str(valrange[0])+'~'+str(valrange[1])
        else:
            return False
            

class OutBlTable(BaseSetup):
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
    infile_variable_a = 'OrionS_rawACSmod_calave_a.ms'
    infile_variable_b = 'OrionS_rawACSmod_calave_b.ms'
    infile_variable_c = 'OrionS_rawACSmod_calave_c.ms'
    outroot = BaseSetup.taskname+'_bltabletest'
    tid = None
    ftype = {'poly': 0, 'chebyshev': 1, 'cspline': 2, 'sinusoid': 3}
    
    def setup_cache(self):
        if os.path.exists(self.infile_variable_a):
            shutil.rmtree(self.infile_variable_a)
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile_variable_a)
        if os.path.exists(self.infile_variable_b):
            shutil.rmtree(self.infile_variable_b)
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile_variable_b)
        if os.path.exists(self.infile_variable_c):
            shutil.rmtree(self.infile_variable_c)
        shutil.copytree(os.path.join(self.datapath,self.infile), self.infile_variable_c)
        
        self.modify_table(self.infile_variable_a, [0,1])
        self.modify_table(self.infile_variable_b, [0])
        self.modify_table(self.infile_variable_c, [1])

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
            
        blparam = self.outroot+'.blparam'
        
        self._createBlparamFile(blparam, self.blparam_order, self.blparam_dic, '')

    def tearDown(self):
        remove_single_file_dir(self.infile)
        remove_files_dirs(self.outroot)
        if (os.path.exists(self.infile)):
            shutil.rmtree(self.infile)
            
        os.system('rm -rf ' + self.outroot + '*')
        
    def modify_table(self, file, ind):
        tb.open(tablename=file, nomodify=False)
        r2msk = tb.getcell('FLAG', 2)
        for ipol in ind:
            for ichan in range(len(r2msk[0])):
                r2msk[ipol][ichan] = True
        tb.putcell('FLAG', 2, r2msk)
        tb.close()

    def time_fit_variable_r2p1less(self):
        """sdbaseline: per-spectrum baselining, output bltable - test302"""
        self.tid='302a'
        infile = self.infile
        datacolumn='float_data'
        blmode='fit'
        blformat='table'
        blfunc='variable'
        dosubtract=True

        bloutput= self.outroot+self.tid+'r2p1less'+'.bltable'
        outfile = self.outroot+self.tid+'r2p1less'+'.ms'
        blparam = self.outroot+self.tid+'r2p1less'+'.blparam'
        self._createBlparamFile(blparam, self.blparam_order, self.blparam_dic, 'r2p1less')
        result = sdbaseline(infile=infile,datacolumn=datacolumn,
                             blmode=blmode,blformat=blformat,bloutput=bloutput,
                             blfunc=blfunc,blparam=blparam,
                             dosubtract=dosubtract,outfile=outfile)
    time_fit_variable_r2p1less.version = "CAS-13981"
                                 
    def time_fit_variable_r2p1cout(self):
        """sdbaseline: per-spectrum baselining, output bltable - test302"""
        self.tid='302b'
        infile = self.infile
        datacolumn='float_data'
        blmode='fit'
        blformat='table'
        blfunc='variable'
        dosubtract=True

        bloutput= self.outroot+self.tid+'r2p1cout'+'.bltable'
        outfile = self.outroot+self.tid+'r2p1cout'+'.ms'
        blparam = self.outroot+self.tid+'r2p1cout'+'.blparam'
        self._createBlparamFile(blparam, self.blparam_order, self.blparam_dic, 'r2p1cout')
        result = sdbaseline(infile=infile,datacolumn=datacolumn,
                             blmode=blmode,blformat=blformat,bloutput=bloutput,
                             blfunc=blfunc,blparam=blparam,
                             dosubtract=dosubtract,outfile=outfile)
    time_fit_variable_r2p1cout.version = "CAS-13981"
    
    def time_fit_variable_masked_masked(self):
        """sdbaseline: testing shortening baseline table for blfunc=variable - test304"""
        self.tid = '304a'
        infile = self.infile_variable_a
        datacolumn='float_data'
        spw=''
        blmode='fit'
        blformat='table'
        blfunc='variable'
        dosubtract=True
        blparam = self.outroot+'.blparam'
        pol = ''

        outfile = self.outroot+self.tid+blfunc+'.ms'
        bloutput= self.outroot+self.tid+blfunc+'.bltable'
        sdbaseline(infile=self.infile,datacolumn=datacolumn,
                            blmode=blmode,blformat=blformat,bloutput=bloutput,
                            spw=spw,pol=pol,blfunc=blfunc,blparam=blparam,
                            dosubtract=dosubtract,outfile=outfile)
    time_fit_variable_masked_masked.version = "CAS-13981"
                                 
    def time_fit_variable_masked_unselect(self):
        """sdbaseline: testing shortening baseline table for blfunc=variable - test304"""
        self.tid = '304b'
        infile = self.infile_variable_b
        datacolumn='float_data'
        spw=''
        blmode='fit'
        blformat='table'
        blfunc='variable'
        dosubtract=True
        blparam = self.outroot+'.blparam'
        pol = 'RR'

        outfile = self.outroot+self.tid+blfunc+'.ms'
        bloutput= self.outroot+self.tid+blfunc+'.bltable'
        sdbaseline(infile=infile,datacolumn=datacolumn,
                            blmode=blmode,blformat=blformat,bloutput=bloutput,
                            spw=spw,pol=pol,blfunc=blfunc,blparam=blparam,
                            dosubtract=dosubtract,outfile=outfile)
    time_fit_variable_masked_unselect.version = "CAS-13981"
        
    def time_fit_variable_unselect_masked(self):
        """sdbaseline: testing shortening baseline table for blfunc=variable - test304"""
        self.tid = '304c'
        infile = self.infile_variable_c
        datacolumn='float_data'
        spw=''
        blmode='fit'
        blformat='table'
        blfunc='variable'
        dosubtract=True
        blparam = self.outroot+'.blparam'
        pol = 'LL'

        outfile = self.outroot+self.tid+blfunc+'.ms'
        bloutput= self.outroot+self.tid+blfunc+'.bltable'
        sdbaseline(infile=infile,datacolumn=datacolumn,
                            blmode=blmode,blformat=blformat,bloutput=bloutput,
                            spw=spw,pol=pol,blfunc=blfunc,blparam=blparam,
                            dosubtract=dosubtract,outfile=outfile)
     time_fit_variable_unselect_masked.version = "CAS-13981"


class BlFuncVariable(BaseSetup):
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

    def tearDown(self):
        remove_files_dirs(os.path.splitext(self.infile)[0])
        remove_single_file_dir(self.outfile)

    def _refetch_files(self, files, from_dir=None):
        if type(files)==str:
            files = [files]
        self._remove(files)
        self._copy(files, from_dir)
    
    def time_variable_orders(self):
        """sdbaseline: Test blfunc='variable' with variable baseline functions and orders - testVariable00"""
        print('why is this failing?')
        infile = 'analytic_variable.ms'
        self.paramfile = 'analytic_variable_blparam.txt'
        self._refetch_files([infile, self.paramfile], self.datapath)
        sdbaseline(infile=infile, blfunc='variable', outfile=self.outfile, blparam=self.paramfile, datacolumn=self.column)
    time_variable_orders.version = "CAS-13981"


class UpdateWeight(BaseSetup):
    """
    Tests for updateweight=True
    to confirm if WEIGHT_SPECTRUM column is removed
    test052 --- blmode='apply', spw to flag channels 4500-6499
    """

    datapath = ctsys_resolve('unittest/sdbaseline/')
    infile = 'uid___A002_X6218fb_X264.ms'
    infile2 = 'analytic_order3_withoffset.ms'
    outroot = BaseSetup.taskname+'_updateweighttest'
    outfile = outroot + '.ms'
    spw = '*:0~4499;6500~8191'

    def setUp(self):
        remove_files_dirs(self.infile)
        shutil.copytree(os.path.join(self.datapath, self.infile), self.infile)
        remove_files_dirs(self.infile2)
        shutil.copytree(os.path.join(self.datapath, self.infile2), self.infile2)

    def tearDown(self):
        remove_files_dirs(self.infile)
        remove_files_dirs(self.infile2)
        remove_files_dirs(self.outroot)

    def time_remove_weight_col(self):
        sdbaseline(infile=self.infile, outfile=self.outfile, intent='OBSERVE_TARGET#ON_SOURCE', spw='9', datacolumn='data', updateweight=True)
    time_remove_weight_col.version = "CAS-13981"
    
    def time_blmode_apply_spw_to_flag(self):
        sdbaseline(infile=self.infile2, outfile=self.outfile, intent='OBSERVE_TARGET#ON_SOURCE', datacolumn='float_data', spw=self.spw)
    time_blmode_apply_spw_to_flag.version = "CAS-13981"
