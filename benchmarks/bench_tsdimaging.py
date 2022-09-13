import os, shutil, glob
from casatools import ctsys
from casatasks import tsdimaging as sdimaging

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (3, 6, 60.0) # between 3 and 6 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 1            # amount of instances a "repeat block" is run to collect samples
min_run_count = 3     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap should never be met for these test cases

class DataSetUp():

    datapath = ctsys.resolve("unittest/tsdimaging/")

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

    def setup_ephemeris(self):
        self.vis = 'ephemtest.spw18_copy.ms'
        self.ephtab = self.vis + '/FIELD/EPHEM0_Sol_58327.6.tab'
        self.out = 'sdimagingTest_eph.im'

        if os.path.exists(self.vis):
            shutil.rmtree(self.vis, ignore_errors=True)

        existing_images = [ff for ff in glob.glob(self.out+"*")]
        for fname in existing_images:
            os.system(f"rm -rf {fname}")

        # working with a copy of the input MS in all cases to avoid column writes
        shutil.copytree(os.path.join(self.datapath, 'ephemtest.spw18.ms'), self.vis)

class Basic(DataSetUp):
    """
    Benchmark runtime of tsdimaging with basic input and mostly default parameter settings
    Adapted from test_task_tsdimaging.py; test100 - test405
    (most of the tests with meaningful output that use sdimaging.ms)
    """
    def setup(self):
        self.setup_basic()

    def time_gridfunction_PB(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_PB_width_1024(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=1, width=1024, gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_PB_nchan_1024(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=1024, width=1, gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_PB_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, outframe='', gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_BOX_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='BOX', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_SF_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='SF', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_PB_start_400_stokes_XXYY(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, outframe='', gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', stokes="XXYY", minweight=0.0 )

    def time_gridfunction_GAUSS_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='GAUSS', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_GJINC_start_400(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='GJINC', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_BOX_start_400_phasecenter_null(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='BOX', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='', minweight=0.0 )

    def time_gridfunction_GJINC_start_400_minweight_70(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', nchan=40, start=400, width=10, gridfunction='GJINC', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=70.0 )

    def time_gridfunction_PB_mode_frequency(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="frequency", nchan=100, start="1420.200000MHz", width="0.010000MHz", gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_PB_mode_velocity_nchan_1(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="velocity", nchan=1, start="-50256.681248364m/s", width="527652.833436753m/s", gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', restfreq="1420405800.0Hz", minweight=0.0 )

    def time_gridfunction_PB_mode_velocity_nchan_100(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="velocity", nchan=100, start="-200.000000km/s", width="2.000000km/s", gridfunction='PB', imsize=[75, 75], cell=['3.0arcmin', '3.0arcmin'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_BOX_imsize_40x35(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="channel", nchan=1, width=1024, gridfunction='BOX', imsize=[40, 35], cell=['320arcsec', '320arcsec'], phasecenter='J2000 17:18:29 +59.31.23', minweight=0.0 )

    def time_gridfunction_BOX_imsize_detect_cell_default_phasecenter_detect(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="channel", nchan=1, width=1024, gridfunction='BOX', imsize=[], minweight=0.0 )

    def time_gridfunction_BOX_imsize_40x35_phasecenter_detect(self):
        sdimaging( infiles=[self.vis], outfile=self.out, intent='', mode="channel", nchan=1, width=1024, gridfunction='BOX', imsize=[40, 35], cell=['320arcsec', '320arcsec'], phasecenter="", minweight=0.0 )

class Ephemeris(DataSetUp):
    """Benchmark runtime of tsdimaging on tracking moving objects (ephemeris data)
    Adapted from test_task_tsdimaging.py; test_ephemeris_notset, test_ephemeris_sun,
    test_ephemeris_trackf, test_ephemeris_table
    """
    def setup(self):
        self.setup_ephemeris()

    def time_ephemeris_notset(self):
        sdimaging(infiles=[self.vis], outfile=self.out, overwrite=False, field='Sol',
                   spw='18', mode='channel', nchan=1, start=0, width=1,
                   veltype='radio', specmode='cube', outframe='', gridfunction='BOX', convsupport=-1, truncate=-1,
                   gwidth=-1, jwidth=-1, imsize=[1000], cell='4arcsec', phasecenter='', projection='SIN',
                   pointingcolumn='direction', restfreq='', stokes='I', minweight=0.1, brightnessunit='',
                   clipminmax=False)

    def time_ephemeris_sun(self):
        sdimaging(infiles=[self.vis], outfile=self.out, overwrite=False, field='Sol',
                   spw='18', mode='channel', nchan=1, start=0, width=1,
                   veltype='radio', specmode='cube', outframe='', gridfunction='BOX', convsupport=-1, truncate=-1,
                   gwidth=-1, jwidth=-1, imsize=[1000], cell='4arcsec', phasecenter='SUN', projection='SIN',
                   pointingcolumn='direction', restfreq='', stokes='I', minweight=0.1, brightnessunit='',
                   clipminmax=False)

    def time_ephemeris_trackf(self):
        sdimaging(infiles=[self.vis], outfile=self.out, overwrite=False, field='Sol',
                  spw='18', mode='channel', nchan=1, start=0, width=1,
                  veltype='radio', specmode='cube', outframe='', gridfunction='BOX', convsupport=-1, truncate=-1,
                  gwidth=-1, jwidth=-1, imsize=[1000], cell='4arcsec', phasecenter='TRACKFIELD', projection='SIN',
                  pointingcolumn='direction', restfreq='', stokes='I', minweight=0.1, brightnessunit='',
                  clipminmax=False)

    def time_ephemeris_table(self):
        sdimaging(infiles=[self.vis], outfile=self.out, overwrite=False, field='Sol',
                  spw='18', mode='channel', nchan=1, start=0, width=1,veltype='radio', specmode='cube',
                  outframe='', gridfunction='BOX', convsupport=-1, truncate=-1,gwidth=-1, jwidth=-1,
                  imsize=[1000], cell='4arcsec',phasecenter=self.ephtab,
                  projection='SIN',pointingcolumn='direction', restfreq='', stokes='I', minweight=0.1,
                  brightnessunit='',clipminmax=False)

    def time_ephemeris_cubesource(self):
        sdimaging(infiles=[self.vis], outfile=self.out, overwrite=False, field='Sol',
                  spw='18', mode='channel', nchan=1, start=0, width=1,veltype='radio', specmode='cubesource', outframe='',
                  gridfunction='BOX', convsupport=-1, truncate=-1,gwidth=-1, jwidth=-1, imsize=[1000], cell='4arcsec',
                   phasecenter='TRACKFIELD', projection='SIN',pointingcolumn='direction', restfreq='', stokes='I',
                   minweight=0.1, brightnessunit='',clipminmax=False)
