import re, os, shutil
from casatools import ctsys
from casatasks import casalog, delmod, tclean
from casatestutils.imagerhelpers import TestHelpers

th = TestHelpers()

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (3, 6, 60.0) # 3-6 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 3            # amount of instances a "repeat block" is run to collect samples
min_run_count = 3     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap for duration of a single test execution

# Test datasets; root directory is read from config.py
datapath = ctsys.resolve("unittest/tclean/")

class BaseTcleanSetup():
    epsilon = 0.05
    cfcache = 'cfcach'
    msfile = ""
    img = "tst"
    imsize = 100
    # To use subdir in the output image names in some tests (CAS-10937)
    img_subdir = 'refimager_tst_subdir'
    parallel = False
    nnode = 0

    # Copy and cleanup datasets
    def prepData(self, msname=""):
        if msname != "":
            self.msfile = msname
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)
        shutil.copytree(os.path.join(datapath, self.msfile), self.msfile)

    # Cache data for awproject tests
    def prepCfcache(self,cfcache=""):
        if (os.path.exists(self.cfcache)):
            os.system('rm -rf ' + self.cfcache)
        if cfcache !="":
            self.cfcache=cfcache
        if (os.path.exists(self.cfcache)):
            os.system('rm -rf ' + self.cfcache)
        shutil.copytree(os.path.join(datapath,self.cfcache), self.cfcache)

class TcleanSingleField(BaseTcleanSetup):
    """Runtime benchmarking tests for tclean on single fields"""
    def setup(self):
        self.prepData('refim_twochan.ms')

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def time_mfs_standard_clark(self):
        """tclean: mfs with clark minor cycle - test_onefield_clark"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec', niter=10,
                     deconvolver='clark', parallel=False)
    time_mfs_standard_clark.version = "CAS-13924"

    def time_mfs_standard_hogbom(self):
        """tclean: mfs with hogbom minor cycle - test_onefield_hogbom"""
        tricky_imagename = self.img + '_uid___A001_X1234a_X56cb.s19_0.J2253+1608_bp.more-dash.virtspw19.mfs.I.iter0.hoghbom'
        ret = tclean(vis=self.msfile, imagename=tricky_imagename, imsize=100, cell='8.0arcsec', niter=10,
                     deconvolver='hogbom', parallel=False)
    time_mfs_standard_hogbom.version = "CAS-13924"

    def time_mfs_standard_mtmfs(self):
        """tclean: mt-mfs with minor cycle iterations - test_onefield_mtmfs"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec', niter=10,
                     deconvolver='mtmfs', parallel=False)
    time_mfs_standard_mtmfs.version = "CAS-13924"

    def test_mfs_standard_hogbom_mask_file(self):
        """tclean: Input mask as file and string using mode mfs - test_mask_1"""
        mstr = 'circle[[50pix,80pix],10pix]'
        th.write_file(self.img + '.mask.txt', '#CRTFv0 CASA Region Text Format version 0\n' + mstr + '\n')
        ret = tclean(vis=self.msfile,imagename=self.img+'1',imsize=100,cell='8.0arcsec',niter=10,
                     deconvolver='hogbom', usemask='user',
                     mask=self.img+'.mask.txt',parallel=False)
    test_mfs_standard_hogbom_mask_file.version = "CAS-13924"

    def time_mfs_standard_hogbom_automask(self):
        """tclean: multi-threshold Autobox (minbeamfrac=0.3) - test_mask_autobox_multithresh_with_prune"""
        ret = tclean(vis=self.msfile,imagename=self.img,imsize=1000,cell='8.0arcsec',niter=10,
                     deconvolver='hogbom', usemask='auto-multithresh',
                     minbeamfrac=0.3,parallel=False)
    time_mfs_standard_hogbom_automask.version = "CAS-13924"

    def time_cube_standard_pcwdT(self):
        """tclean: cube with perchanweightdensity True and briggs weighting - test_onefield_pcwdT_and_pcwdF"""
        ret = tclean(self.msfile, imagename=self.img + '1', imsize=20, cell='8.0arcsec', niter=0, nchan=1,
                     spw='0:1', gridder='standard', perchanweightdensity=True, specmode='cube',
                     weighting='briggs', robust=0.5)
    time_cube_standard_pcwdT.version = "CAS-13924"

class TcleanMultiField(BaseTcleanSetup):
    """Runtime benchmarking tests for tclean on multiple fields"""
    def setup(self):
        self.prepData("refim_twopoints_twochan.ms")

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def time_multifield_mfs_hogbom(self):
        """tclean : Two fields, both mfs - test_multifield_both_mfs"""
        th.write_file(self.img + '.out.txt',
                           'imagename=' + self.img + '1\nnchan=1\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:40.895 +40.55.58.543\nusemask=user\nmask=circle[[40pix,40pix],10pix]')

        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50", outlierfile=self.img + '.out.txt', niter=10,
                     deconvolver='hogbom', parallel=False)
    time_multifield_mfs_hogbom.version = "CAS-13924"

    def time_multifield_mfs_mtmfs(self):
        """ tclean: Two fields, both mt-mfs - test_multifield_both_mtmfs"""
        th.write_file(self.img + '.out.txt',
                           'imagename=' + self.img + '1\n\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:40.895 +40.55.58.543\nusemask=user\nmask=circle[[40pix,40pix],10pix]')

        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50", outlierfile=self.img + '.out.txt', niter=10,
                     deconvolver='mtmfs', parallel=False)
    time_multifield_mfs_mtmfs.version = "CAS-13924"

    def time_multifield_cube_hogbom(self):
        """tclean: Two fields, both cube - test_multifield_both_cube"""
        th.write_file(self.img + '.out.txt',
                           'imagename=' + self.img + '1\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:40.895 +40.55.58.543\nimagename=' + self.img + '2\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:48.895 +40.55.58.543\n')

        retpar = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec',
                        phasecenter="J2000 19:59:28.500 +40.44.01.50", outlierfile=self.img + '.out.txt', niter=10,
                        deconvolver='hogbom', specmode='cube', nchan=2, interpolation='nearest', parallel=False)
    time_multifield_cube_hogbom.version = "CAS-13924"

class TestWideField(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean on widefield using mosaic gridder with cube mode"""
    def setup(self):
        self.prepData('refim_oneshiftpoint.mosaic.ms')

    def time_cube_mosaic_cbFalse_mwFalse_twofield(self):
        """tclean: - cube mosaic using conjbeams=False - test_cube_mosaic_cbFalse_mwFalse_twofield"""
        tclean(vis=self.msfile, imagename=self.img,niter=10,specmode='cube',spw='*',imsize=1024, 
               phasecenter='J2000 19h59m28.5 +40d40m01.5',cell='10.0arcsec',gridder='mosaic',field='0,1', 
               conjbeams=False, wbawp=True, psterm=False,pblimit=0.1,reffreq='1.5GHz', 
               pbcor=True, mosweight=False, parallel=False)
    time_cube_mosaic_cbFalse_mwFalse_twofield.version = "CAS-13924"

    def time_cube_mosaic_cbFalse_mwTrue_twofield(self):
        """tclean: - cube mosaic using conjbeams=False - test_cube_mosaic_cbFalse_mwTrue_twofield"""
        tclean(vis=self.msfile, imagename=self.img,niter=10,specmode='cube',spw='*',imsize=1024,
               phasecenter='J2000 19h59m28.5 +40d40m01.5',cell='10.0arcsec',gridder='mosaic',field='0,1',
               conjbeams=False, wbawp=True, psterm=False,pblimit=0.1,reffreq='1.5GHz',
               pbcor=True, mosweight=True, parallel=False)
    time_cube_mosaic_cbFalse_mwFalse_twofield.version = "CAS-13924"

    def time_cube_mosaic_cbFalse_mwFalse_twofield_upTrue(self):
        """tclean: Cube mosaic with conjbeams=F, mosaicweight=F, usepointing=T, of two fields -  test_cube_mosaic_cbFalse_mwFalse_twofield_upTrue"""
        tclean(vis=self.msfile, imagename=self.img,niter=10,specmode='cube',spw='*',imsize=1024, 
               phasecenter='J2000 19h59m28.5 +40d40m01.5',cell='10.0arcsec',gridder='mosaic',field='0,1', 
               usepointing = True, conjbeams=False, wbawp=True, psterm=False,pblimit=0.1,reffreq='1.5GHz', 
               pbcor=True, mosweight=False, parallel=False)
    time_cube_mosaic_cbFalse_mwFalse_twofield.version = "CAS-13924"

class TcleanWideFieldAWP(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean on widefield using awproject"""
    def setup(self):
        self.prepData("refim_mawproject.ms")

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def time_mfs_awproject_hogbom(self):
        """tclean: MFS with narrowband AWProjection - test_widefield_aproj_mfs"""
        ret = tclean(vis=self.msfile, spw='1', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=30, gridder='awproject', cfcache='',
                     wbawp=False, conjbeams=True, psterm=False,computepastep=360.0,rotatepastep=360.0,
                     deconvolver='hogbom', savemodel='modelcolumn', parallel=False)

    def time_mfs_awproject_mtmfs(self):
        """tclean: MFS with AWProjection and nt=2 stokes I - test_widefield_aproj_mtmfs  """
        ret = tclean(vis=self.msfile, spw='*', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=0, gridder='awproject',
                     cfcache=self.img + '.cfcache', wbawp=True, conjbeams=False, psterm=False,
                     computepastep=360.0,rotatepastep=360.0, deconvolver='mtmfs', parallel=False)

    def time_cube_awproject_hogbom(self):
        """tclean: Cube with AW-Projection  and rotation off - test_widefield_aproj_cube"""
        ret = tclean(vis=self.msfile, field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",specmode='cube', niter=1, gain=1.0,
                     gridder='awproject', cfcache=self.img + '.cfcache',wbawp=True,conjbeams=False,
                     psterm=False, computepastep=360.0, rotatepastep=360.0, deconvolver='hogbom',
                     parallel=False)

class TcleanCube(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean cube"""
    def setup(self):
        self.prepData('refim_point.ms')

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def time_cube_standard_hogbom(self):
        """tclean: mosaic cube with Hogbom deconvolver -  test_cube_0"""
        ret = tclean(vis=self.msfile, field='0', imsize=100, cell='8.0arcsec', niter=10,
                     specmode='cube', nchan=10, restfreq=['1.25GHz'],
                     phasecenter="J2000 19:59:28.500 +40.44.01.50", deconvolver='hogbom',
                     spw='0', imagename=self.img + 'Cubetest_chandefstdefwidth',
                     start=0, width=1, veltype='radio', outframe='LSRK', interpolation='linear', parallel=False)

    def time_cube_standard_channel_gap(self):
        """tclean" mosaic cube with gap in channel selection - test_cube_21"""
        ret = tclean(vis=self.msfile, field='0', imsize=100, cell='8.0arcsec', niter=10,
                     specmode='cube', nchan=10, restfreq=['1.25GHz'],
                     phasecenter="J2000 19:59:28.500 +40.44.01.50", deconvolver='hogbom',
                     spw='0:4~9;12~14', imagename=self.img + 'Cubetest_st4gap', start=4,
                     width='', veltype='radio', outframe='LSRK', interpolation='nearest', parallel=False)

    def time_cube_standard_fullsummary(self):
        """tclean: single field cube with fullsummary parameter - test_iterbot_cube_fullsummary_true"""
        retpar = tclean(vis=self.msfile, imagename=self.img + "Cubetest_fullsummary", imsize=100, cell='8.0arcsec',
                        specmode='cube', deconvolver='clark', niter=10, threshold='0.75Jy', fullsummary=True, parallel=False)
    time_cube_standard_fullsummary.version = "CAS-13924"

class TcleanEphemeris(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean ephemeris object imaging"""
    def setup(self):
        self.prepData('venus_ephem_test.ms')

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def time_eph_singlefield_standard_mfs(self):
        """single field (standard gridder), mfs mode - test_onefield_mfs_eph"""
        ret = tclean(vis=self.msfile, field='0', imagename=self.img, imsize=[288, 288], cell=['0.14arcsec'],
                     phasecenter='TRACKFIELD', specmode='mfs', gridder='standard', niter=0, parallel=False)
    time_eph_singlefield_standard_mfs.version = "CAS-13924"

    def time_eph_singlefield_standard_cubesource(self):
        """tclean: single field (standard gridder), cubesource mode - test_onefield_cube_eph"""
        ret = tclean(vis=self.msfile, field='0', imagename=self.img, imsize=[288, 288], cell=['0.14arcsec'],
                   phasecenter='TRACKFIELD', specmode='cubesource', gridder='standard', niter=0, parallel=False)
    time_eph_singlefield_standard_cubesource.version = "CAS-13924"

    def time_eph_multifield_mosaic_mfs(self):
        """tclean: multifield (mosaic gridder), mfs mode - test_multifield_mfs_eph"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=[480, 420], cell=['0.14arcsec'],
                     phasecenter='TRACKFIELD', specmode='mfs', gridder='mosaic', niter=0, parallel=False)
    time_eph_multifield_mosaic_mfs.version = "CAS-13924"

    def time_eph_multifield_mosaic_cubesource(self):
        """tclean: multifield (mosaic gridder), cubesource mode - test_multifield_cube_eph"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=[480, 420], cell=['0.14arcsec'],
                     phasecenter='TRACKFIELD', specmode='cubesource', gridder='mosaic', niter=0, parallel=False)
    time_eph_multifield_mosaic_cubesource.version = "CAS-13924"

class TcleanMoldelVis(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean with saving model column"""
    def setup(self):
        self.prepData("refim_twochan.ms")
        delmod(self.msfile)
        th.delmodels(self.msfile, modcol='delete')

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def time_mfs_modelcolumn(self):
        """tclean: mfs mode saving a model column - test_modelvis_2"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec', niter=10,
                     savemodel='modelcolumn',parallel=False)

    def time_mfs_virtual_modelcolumn(self):
        """tclean: mfs saving a virtual model column - test_modelvis_3"""
        ret = tclean(vis=self.msfile,imagename=self.img,imsize=100,cell='8.0arcsec',niter=10,
                     savemodel='virtual',parallel=False)

    def time_mfs_automask_modelcolumn(self):
        """tclean: mfs with automask and save model column, internally a separate predit model step - test_modelvis_12"""
        ret = tclean(vis=self.msfile,imagename=self.img,imsize=100,cell='8.0arcsec',niter=10,
                     savemodel='modelcolumn',usemask='auto-multithresh', parallel=False)

class TcleanStokes(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean with Stokes imaging"""
    def setup(self):
        self.prepData('refim_point_linRL.ms')

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def time_mfs_stokes_IV(self):
      """tclean: mfs with stokes IV - test_stokes_mfs_IV"""
      tclean(vis=self.msfile,imagename=self.img,imsize=100,cell='8.0arcsec',niter=10, stokes='IV',
             parallel=False)

    def time_mtmfs_stokes_IQUV(self):
        """tclean: mtmfs with stokes IQUV - test_stokes_mtmfs_IQUV"""
        tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec', niter=10, stokes='IQUV',
               deconvolver='mtmfs', nterms=2, parallel=False)

    def time_cube_stokes_IV(self):
      """tclean: cube with stokes V - test_stokes_cube_IV"""
      ret = tclean(vis=self.msfile,imagename=self.img,imsize=100,cell='8.0arcsec',niter=10,
                   stokes='IV', specmode='cube', interpolation='nearest', parallel=False)
    time_cube_stokes_IV.version = "CAS-13924"
