import os, shutil, glob
from casatools import ctsys
from casatasks import sdimaging

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (3, 6, 60.0) # between 3 and 6 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 1            # amount of instances a "repeat block" is run to collect samples
min_run_count = 3     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap should never be met for these test cases

class DataSetUp():

    datapath = ctsys.resolve("unittest/sdimaging/")

    def setup_basic(self):
        self.vis = "sdimaging_copy.ms"
        self.out = "sdimagingTest.im"

        if os.path.exists(self.vis):
            shutil.rmtree(self.vis, ignore_errors=True)

        existing_images = [ff for ff in glob.glob(self.out+"*")]
        for fname in existing_images:
            os.system(f"rm -rf {fname}")

        # working with a copy of the input MS in all cases to avoid column writes
        shutil.copytree(os.path.join(self.datapath, 'sdimaging.ms'), self.vis)

class Basic(DataSetUp):
    """
    Benchmark runtime of sdimaging with basic input and mostly default parameter settings
    Adapted from test_task_sdimaging.py; test100 - test405
    (most of the tests with meaningful output that use sdimaging.ms)
    """
    def setup(self):
        self.setup_basic()

    def time_sdimaging_gridfunction_PB(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_PB_width_1024(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=1, width=1024, gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_PB_nchan_1024(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=1024, width=1, gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_PB_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, outframe='', gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_BOX_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='BOX', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_SF_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='SF', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_PB_start_400_stokes_XXYY(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, outframe='', gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', stokes="XXYY", minweight=0.0 )

    def time_sdimaging_gridfunction_GAUSS_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='GAUSS', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_GJINC_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='GJINC', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_BOX_start_400_phasecenter_null(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='BOX', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='', minweight=0.0 )

    def time_sdimaging_gridfunction_GJINC_start_400_minweight_70(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='GJINC', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=70.0 )

    def time_sdimaging_gridfunction_PB_mode_frequency(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="frequency", nchan=100, start="1420.200000MHz", width="0.010000MHz", gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_PB_mode_velocity_nchan_1(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="velocity", nchan=1, start="-50256.681248364m/s", width="527652.833436753m/s", gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', restfreq="1420405800.0Hz", minweight=0.0 )

    def time_sdimaging_gridfunction_PB_mode_velocity_nchan_100(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="velocity", nchan=100, start="-200.000000km/s", width="2.000000km/s", gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_BOX_imsize_40x35(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="channel", nchan=1, width=1024, gridfunction='BOX', imsize=[40, 35], cell=['320arcsec', '320arcsec'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_sdimaging_gridfunction_BOX_imsize_detect_cell_default_phasecenter_detect(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="channel", nchan=1, width=1024, gridfunction='BOX', imsize=[], minweight=0.0 )

    def time_sdimaging_gridfunction_BOX_imsize_40x35_phasecenter_detect(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="channel", nchan=1, width=1024, gridfunction='BOX', imsize=[40, 35], cell=['320arcsec', '320arcsec'], phasecenter="", minweight=0.0 )

class SelectionTypes(DataSetUp):
    """
    Benchmark runtime of sdimaging to exercise data selection parameter input
    Adapted from test_task_sdimaging.py; test_scan*, test_intent*, 
    
    Most of the tests with meaningful output that use:
      selection_misc.ms
      selection_intent.ms
      selection_spw_unifreq.ms
      selection_spw.ms
    """

    def setup(self):
        self.setup_selection()
