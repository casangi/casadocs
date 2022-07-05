import re, os, shutil
from casatools import ctsys
from casatasks import casalog, delmod, tclean
from casatestutils.imagerhelpers import TestHelpers

th = TestHelpers()

# ASV attributes
timeout = 10000
number = 2

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
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if msname != "":
            self.msfile = msname
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)
        shutil.copytree(os.path.join(datapath, self.msfile), self.msfile)

# class TcleanSingleField, TcleanMultiField
#       def time_SF_specmode_gridder
#       def time_MF_specmode_gridder
# Main specmodes: mfs, cube, cubesource, cubedata(?)
# Main gridders: standard, mosaic, mosaicft, wproject, awproject
# Deconvolvers: hogbom, clark, multiscale, mtmfs, asp....
# Weighting: natural, briggs,, briggsbwtaper

class TcleanSingleField(BaseTcleanSetup):

    def setup(self):
        self.prepData('refim_twochan.ms')

    def time_mfs_standard_clark (self):
        """tclean: mfs with clark minor cycle - test_onefield_clark"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec', niter=10,
                     deconvolver='clark', interactive=0, parallel=False)

    def time_mfs_standard_hogbom(self):
        """tclean: mfs with hogbom minor cycle - test_onefield_hogbom"""
        tricky_imagename = self.img + '_uid___A001_X1234a_X56cb.s19_0.J2253+1608_bp.more-dash.virtspw19.mfs.I.iter0.hoghbom'
        ret = tclean(vis=self.msfile, imagename=tricky_imagename, imsize=100, cell='8.0arcsec', niter=10,
                     deconvolver='hogbom', interactive=0,parallel=False)

    def time_msf_standard_mtmfs(self):
        """tclean: mt-mfs with minor cycle iterations - test_onefield_mtmfs"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec', niter=10,
                     deconvolver='mtmfs',interactive=0, parallel=False)

     def test_standard_mfs_mask_file(self):
          """tclean: Input mask as file and string using mode mfs - test_mask_1"""
          mstr = 'circle[[50pix,80pix],10pix]'
          self.th.write_file(self.img + '.mask.txt', '#CRTFv0 CASA Region Text Format version 0\n' + mstr + '\n')
          ret = tclean(vis=self.msfile,imagename=self.img+'1',imsize=100,cell='8.0arcsec',niter=10,
                        deconvolver='hogbom',interactive=0,usemask='user',
                        mask=self.img+'.mask.txt',parallel=False)

     def test_standard_mfs_mask_string(self):
          """tclean: Input mask as file and string using mode mfs - test_mask_1"""
          mstr = 'circle[[50pix,80pix],10pix]'
          ret = tclean(vis=self.msfile,imagename=self.img+'2',imsize=100,cell='8.0arcsec',niter=10,
                        deconvolver='hogbom',interactive=0,usemask='user',mask=mstr,parallel=False)

    def time_standard_cube_pcwdT(self):
        """tclean: cube with perchanweightdensity True and briggs weighting - test_onefield_pcwdT_and_pcwdF"""
        ret = tclean(self.msfile, imagename=self.img + '1', imsize=20, cell='8.0arcsec', niter=0, nchan=1,
                     spw='0:1', interactive=0, gridder='standard', perchanweightdensity=True, specmode='cube',
                     weighting='briggs', robust=0.5)


# Multifield test classes with different gridders and specmodes
class TcleanWideFieldMosaic(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean widefield mosaic"""
    def time_mosaic_cube_hogbom(self):
    def time_mosaic_cube_clark(self):
    def time_mosaic_cube_multiscale(self):
    def time_mosaic_cube_mtmfs(self):

    def time_mosaic_mfs_hogbom(self):
    def time_mosaic_mfs_clark(self):
    def time_mosaic_mfs_multiscale(self):
    def time_mosaic_mfs_mtmfs(self):

class TcleanWideFieldMosaicFT(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean widefield mosaicft"""
    def setup(self):
        self.prepData("refim_mawproject.ms")

    def time_mosaicft_mfs_hogbom(self):
        """tclean: MFS with mosaicft  stokes I - test_widefield_mosaicft_mfs"""
        ret = tclean(vis=self.msfile, spw='1', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=30, gridder='mosaicft',
                     deconvolver='hogbom', pblimit=0.3, parallel=False)

    def time_mosaicft_mfs_mtmfs(self):
        """tclean: MT-MFS with mosaicft  stokes I, alpha - test_widefield_mosaicft_mtmfs"""
        ret = tclean(vis=self.msfile, spw='*', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=60, gridder='mosaicft',
                     deconvolver='mtmfs', conjbeams=False, parallel=False)

    def time_mosaicft_cube_hogbom(self):
          """tclean: MFS with mosaicft  stokes I - test_widefield_mosaicft_cube"""
          ret = tclean(vis=self.msfile,spw='*',field='0',imagename=self.img,imsize=512,cell='10.0arcsec',
                       phasecenter="J2000 19:59:28.500 +40.44.01.50",specmode='cube',niter=10,gridder='mosaicft',
                       deconvolver='hogbom',gain=0.1,stokes='I',parallel=False)


class TcleanWideFieldAWP(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean widefield awproject"""
    def setup(self):
        self.prepData("refim_mawproject.ms")

    def time_awproject_mfs_hogbom(self):
        """tclean: MFS with narrowband AWProjection - test_widefield_aproj_mfs"""
        ret = tclean(vis=self.msfile, spw='1', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=30, gridder='awproject', cfcache='',
                     wbawp=False, conjbeams=True, psterm=False,computepastep=360.0,rotatepastep=360.0,
                     deconvolver='hogbom', savemodel='modelcolumn', parallel=False)

    def time_awproject_mfs_mtmfs(self):
        """tclean: MFS with AWProjection and nt=2 stokes I - test_widefield_aproj_mtmfs  """
        ret = tclean(vis=self.msfile, spw='*', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=0, gridder='awproject',
                     cfcache=self.img + '.cfcache', wbawp=True, conjbeams=False, psterm=False,
                     computepastep=360.0,rotatepastep=360.0, deconvolver='mtmfs', parallel=False)

   def time_awproject_cube_hogbom(self):
        """tclean: Cube with AW-Projection  and rotation off - test_widefield_aproj_cube"""
        ret = tclean(vis=self.msfile, field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",specmode='cube', niter=1, gain=1.0,
                     gridder='awproject', cfcache=self.img + '.cfcache',wbawp=True,conjbeams=False,
                     psterm=False, computepastep=360.0, rotatepastep=360.0, deconvolver='hogbom',
                     parallel=False)


class TcleanWideFieldWP(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean widefield wproject"""

    def time_wproject_cube_...(self):
    def time_wproject_mfs_...(self):


class TcleanEphemeris(BaseTcleanSetup):
    """Runtime benchmarking tests of tclean ephemeris object imaging"""
    def setup(self):
        self.prepData('venus_ephem_test.ms')

    def time_eph_singlefield_standard_mfs(self):
        """single field (standard gridder), mfs mode - test_onefield_mfs_eph"""
        ret = tclean(vis=self.msfile, field='0', imagename=self.img, imsize=[288, 288], cell=['0.14arcsec'],
                     phasecenter='TRACKFIELD', specmode='mfs', gridder='standard', niter=0, interactive=0,
                     parallel=False)

    def time_eph_singlefield_standard_cubesource(self):
        """tclean: single field (standard gridder), cubesource mode - test_onefield_cube_eph"""
        ret = tclean(vis=self.msfile, field='0', imagename=self.img, imsize=[288, 288], cell=['0.14arcsec'],
                   phasecenter='TRACKFIELD', specmode='cubesource', gridder='standard', niter=0,
                   interactive=0, parallel=False)

    def time_eph_multifield_mosaic_mfs(self):
        """tclean: multifield (mosaic gridder), mfs mode - test_multifield_mfs_eph"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=[480, 420], cell=['0.14arcsec'],
                     phasecenter='TRACKFIELD', specmode='mfs', gridder='mosaic', niter=0, interactive=0,
                     parallel=False)

    def time_eph_multifield_mosaic_cubesource(self):
        """tclean: multifield (mosaic gridder), cubesource mode - test_multifield_cube_eph"""
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=[480, 420], cell=['0.14arcsec'],
                     phasecenter='TRACKFIELD', specmode='cubesource', gridder='mosaic', niter=0, interactive=0,
                     parallel=False)

class TcleanMoldelVis(BaseTcleanSetup):
    """
    Benchmark runtime of task_tclean with model column
    """
    def setup(self):
        self.prepData("refim_twochan.ms")
        delmod(self.msfile)
        th.delmodels(self.msfile, modcol='delete')

     def test_modelvis_2(self):
        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec', niter=10,
                     savemodel='modelcolumn',parallel=self.parallel)

     def test_modelvis_3(self):
          """ [modelpredict] Test_modelvis_3 : mfs with save virtual model """
          ret = tclean(vis=self.msfile,imagename=self.img,imsize=100,cell='8.0arcsec',niter=10,
                       savemodel='virtual',parallel=self.parallel)
    def test_modelvis_12(self):
          """ [modelpredict] Test_modelvis_12 : (CAS-12618) mfs with automask and save model column (single tclean call, internally a separate predit model step)"""
          ret = tclean(vis=self.msfile,imagename=self.img,imsize=100,cell='8.0arcsec',niter=10,
                       savemodel='modelcolumn',usemask='auto-multithresh', parallel=self.parallel)

