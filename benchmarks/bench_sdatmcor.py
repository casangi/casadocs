import os
import shutil

from casatasks import sdatmcor
from casatasks.private.sdutil import table_manager
from casatools import ctsys
from casatools import ms as mstool

ctsys_resolve = ctsys.resolve

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (1, 2, 30.0) # between 1 and 2 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 3            # amount of instances a "repeat block" is run to collect samples
min_run_count = 5     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap for duration of a single test execution

def smart_remove(name):
    if os.path.exists(name):
        if os.path.isdir(name):
            shutil.rmtree(name)
        elif os.path.isfile(name):
            os.remove(name)
        else:
            # could be a symlink
            os.remove(name)

def apply_gainfactor(name, spw, factor):
    ms = mstool()
    idx = ms.msseltoindex(name, spw=[int(spw)])
    ddid = idx['dd'][0]
    with table_manager(name, nomodify=False) as tb:
        colnames = tb.colnames()
        tsel = tb.query('DATA_DESC_ID=={}'.format(ddid))
        try:
            for colname in ['DATA', 'FLOAT_DATA', 'CORRECTED_DATA']:
                if colname in colnames:
                    data = tsel.getcol(colname)
                    tsel.putcol(colname, data * factor)
        finally:
            tsel.close()

class test_sdatmcor():
    datapath = ctsys_resolve('unittest/sdatmcor')
    infile = 'X320b_sel2.ms'
    infile2 = 'X320b_sel2_gainfactor.ms'
    outfile = infile + '.atmcor'
    caltable = infile + '.k2jycal'

    local_unit_test = False

    def setUp(self):

        smart_remove(self.infile)
        smart_remove(self.infile2)
        smart_remove(self.outfile)
        smart_remove(self.caltable)
        shutil.copytree(os.path.join(self.datapath, self.infile), self.infile)
        shutil.copytree(os.path.join(self.datapath, self.infile), self.infile2)
        # Gainfactor test set up
        gainfactor = {'19': 10.0, '23': 45.0}
        apply_gainfactor(self.infile2, 19, gainfactor['19'])
        apply_gainfactor(self.infile2, 23, gainfactor['23'])

    def tearDown(self):
        smart_remove(self.infile)
        smart_remove(self.infile2)
        smart_remove(self.outfile)
        smart_remove(self.caltable)

    def time_sdatmcor_normal(self):
        """Test normal usage of sdatmcor."""
        sdatmcor(infile=self.infile, outfile=self.outfile, datacolumn='data')
    time_sdatmcor_normal.version = "CAS-13982"

    def time_sdatmcor_explicit_atmtype(self):
        """Test specifying atmtype explicitly."""
        sdatmcor(infile=self.infile, outfile=self.outfile, datacolumn='data', atmtype=2)
    time_sdatmcor_explicit_atmtype.version = "CAS-13982"

    def time_sdatmcor_gainfactor_dict(self):
        """Test gainfactor: dict input."""
        gainfactor = {'19': 10.0, '23': 45.0}
        sdatmcor(infile=self.infile2, outfile=self.outfile, datacolumn='data', gainfactor=gainfactor)
    time_sdatmcor_gainfactor_dict.version = "CAS-13982"

    def time_custom_atm_params(self):
        """Test customized ATM parameters."""
        sdatmcor(
            infile=self.infile, outfile=self.outfile, datacolumn='data',
            dtem_dh='-5.7K/km', h0='2010m',
            atmdetail=True,
            altitude='5.1km', temperature='290K', pressure='700hPa',
            humidity=30, pwv='0.1cm', dp='10hPa', dpm=1.2,
            layerboundaries='800m,1.5km', layertemperature='250K,200K'
        )
    time_custom_atm_params.version = "CAS-13982"
