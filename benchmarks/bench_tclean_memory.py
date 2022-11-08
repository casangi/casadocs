from collections import OrderedDict
import re, os, shutil
from casatools import ctsys
from casatasks import casalog
from casatasks import tclean
from casatestutils.imagerhelpers import TestHelpers
th = TestHelpers()

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (1, 5, 60.0) # between 1 and 5 iterations per round w/ soft cutoff (start no new repeats) past 1m
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

class MemoryMultiField(BaseTcleanSetup):
    """Peak memory benchmarking tests for tclean on multiple fields"""
    def setup(self):
        self.prepData("refim_twopoints_twochan.ms")

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def peakmem_multifield_mfs_hogbom(self):
        """tclean : Two fields, both mfs - test_multifield_both_mfs"""
        th.write_file(self.img + '.out.txt',
                           'imagename=' + self.img + '1\nnchan=1\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:40.895 +40.55.58.543\nusemask=user\nmask=circle[[40pix,40pix],10pix]')

        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50", outlierfile=self.img + '.out.txt', niter=10,
                     deconvolver='hogbom', interactive=0, parallel=False)

    def peakmem_multifield_mfs_mtmfs(self):
        """ tclean: Two fields, both mt-mfs - test_multifield_both_mtmfs"""
        th.write_file(self.img + '.out.txt',
                           'imagename=' + self.img + '1\n\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:40.895 +40.55.58.543\nusemask=user\nmask=circle[[40pix,40pix],10pix]')

        ret = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50", outlierfile=self.img + '.out.txt', niter=10,
                     deconvolver='mtmfs', interactive=0, parallel=False)

    def peakmem_multifield_cube_hogbom(self):
        """tclean: Two fields, both cube - test_multifield_both_cube"""
        th.write_file(self.img + '.out.txt',
                           'imagename=' + self.img + '1\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:40.895 +40.55.58.543\nimagename=' + self.img + '2\nimsize=[80,80]\ncell=[8.0arcsec,8.0arcsec]\nphasecenter=J2000 19:58:48.895 +40.55.58.543\n')

        retpar = tclean(vis=self.msfile, imagename=self.img, imsize=100, cell='8.0arcsec',
                        phasecenter="J2000 19:59:28.500 +40.44.01.50", outlierfile=self.img + '.out.txt', niter=10,
                        deconvolver='hogbom', interactive=0, specmode='cube', nchan=2, interpolation='nearest',
                        parallel=False)

class MemoryWideField(BaseTcleanSetup):
    """Peak memory benchmarking tests of tclean on widefield using mosaic gridder with cube mode"""
    def setup(self):
        self.prepData('refim_oneshiftpoint.mosaic.ms')

    def peakmem_cube_mosaic_cbFalse_mwFalse_twofield(self):
        """tclean: - cube mosaic using conjbeams=False - test_cube_mosaic_cbFalse_mwFalse_twofield"""
        tclean(vis=self.msfile, imagename=self.img,niter=10,specmode='cube',spw='*',imsize=1024, phasecenter='J2000 19h59m28.5 +40d40m01.5',cell='10.0arcsec',gridder='mosaic',field='0,1', conjbeams=False, wbawp=True, psterm=False,pblimit=0.1,reffreq='1.5GHz',pbcor=True,mosweight=False,parallel=False)

    def peakmem_cube_mosaic_cbFalse_mwTrue_twofield(self):
        """tclean: - cube mosaic using conjbeams=False - test_cube_mosaic_cbFalse_mwTrue_twofield"""
        tclean(vis=self.msfile, imagename=self.img,niter=10,specmode='cube',spw='*',imsize=1024, phasecenter='J2000 19h59m28.5 +40d40m01.5',cell='10.0arcsec',gridder='mosaic',field='0,1', conjbeams=False, wbawp=True, psterm=False,pblimit=0.1,reffreq='1.5GHz',pbcor=True,mosweight=True,parallel=False)

    def peakmem_cube_mosaic_cbFalse_mwFalse_twofield_upTrue(self):
        """tclean: Cube mosaic with conjbeams=F, mosaicweight=F, usepointing=T, of two fields -  test_cube_mosaic_cbFalse_mwFalse_twofield_upTrue"""
        tclean(vis=self.msfile, imagename=self.img,niter=10,specmode='cube',spw='*',imsize=1024, phasecenter='J2000 19h59m28.5 +40d40m01.5',cell='10.0arcsec',gridder='mosaic',field='0,1',  usepointing = True, conjbeams=False, wbawp=True, psterm=False,pblimit=0.1,reffreq='1.5GHz',pbcor=True,mosweight=False,parallel=False)

class MemoryWideFieldAWP(BaseTcleanSetup):
    """Peak memory benchmarking tests of tclean on widefield using awproject"""
    def setup(self):
        self.prepData("refim_mawproject.ms")

    def teardown(self):
        os.system('rm -rf ' + self.img_subdir)
        os.system('rm -rf ' + self.img + '*')
        if (os.path.exists(self.msfile)):
            os.system('rm -rf ' + self.msfile)

    def peakmem_mfs_awproject_hogbom(self):
        """tclean: MFS with narrowband AWProjection - test_widefield_aproj_mfs"""
        ret = tclean(vis=self.msfile, spw='1', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=30, gridder='awproject', cfcache='',
                     wbawp=False, conjbeams=True, psterm=False,computepastep=360.0,rotatepastep=360.0,
                     deconvolver='hogbom', savemodel='modelcolumn', parallel=False)

    def peakmem_mfs_awproject_mtmfs(self):
        """tclean: MFS with AWProjection and nt=2 stokes I - test_widefield_aproj_mtmfs  """
        ret = tclean(vis=self.msfile, spw='*', field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",niter=0, gridder='awproject',
                     cfcache=self.img + '.cfcache', wbawp=True, conjbeams=False, psterm=False,
                     computepastep=360.0,rotatepastep=360.0, deconvolver='mtmfs', parallel=False)

    def peakmem_cube_awproject_hogbom(self):
        """tclean: Cube with AW-Projection  and rotation off - test_widefield_aproj_cube"""
        ret = tclean(vis=self.msfile, field='*', imagename=self.img, imsize=512, cell='10.0arcsec',
                     phasecenter="J2000 19:59:28.500 +40.44.01.50",specmode='cube', niter=1, gain=1.0,
                     gridder='awproject', cfcache=self.img + '.cfcache',wbawp=True,conjbeams=False,
                     psterm=False, computepastep=360.0, rotatepastep=360.0, deconvolver='hogbom',
                     parallel=False)

class MemorySetWeighting:
    """
    An example benchmark that adapts test_perf_tclean_mem_setweighting.py to asv
    """

    timeout = 10000

    dataroot = ctsys.resolve("performance/tclean_mem_setweighting/")
    input_ms = "uid___A002_Xb9dfa4_X4724_target_spw16.ms"

    # assign our test dataset
    datapath = os.path.join(dataroot, input_ms)

    templogfile = "tclean_memprofile.log"

    imsize = [1344, 1512]
    nchan = 10  # original is nchan=2046
    phasecenter = "ICRS 10:43:50.2473 -059.56.48.583"
    imagename = f"memtest_{imsize[0]}x{imsize[1]}_uid___A001_X87a_X13d.s28_0.Pillar_3_sci.spw16.mfs.I.findcont"

    def setup_cache(self):
        # only run once for repeated tests
        pass
        # TODO: consider paramterizing here instead of setup/test methods for more accurate measurement

    def setup(self):
        ## fresh copy of the test MS to the tmp directory where tests are run ?
        # shutil.copytree(os.path.join(self.dataroot, self.input_ms),os.path.join(os.getcwd(), self.input_ms))
        pass
        # note: creating objects in setup method confounds memory benchmarks
        # (https://asv.readthedocs.io/en/stable/writing_benchmarks.html#memory)

    def peakmem_tclean_setweighting(self):
        """Adapted from CAS-13026"""
        tclean(
            vis=self.datapath,
            imagename=self.imagename,
            phasecenter=self.phasecenter,
            scan=["17,11,13"],
            restoration=False,
            datacolumn="data",
            pbcor=False,
            spw="0",
            weighting="briggs",
            intent="OBSERVE_TARGET#ON_SOURCE",
            threshold="0mJy",
            robust=0.5,
            savemodel="none",
            imsize=self.imsize,
            stokes="I",
            nchan=self.nchan,
            deconvolver="hogbom",
            field="Pillar_3",
            npixels=0,
            niter=0,
            pblimit=0.2,
            restoringbeam=[],
            cell=["0.94arcsec"],
            start="230.490186515GHz",
            outframe="LSRK",
            specmode="cube",
            width="0.0610478663509MHz",
            gridder="mosaic",
            interactive=False,
            parallel=False,
        )

    def track_file_descriptors_cubemode_mosaic_briggs(self):
        """Adapted from CAS-8755
        https://open-bitbucket.nrao.edu/projects/CASA/repos/casa6/browse/casatests/performance/test_perf_tclean_mem_setweighting.py?at=refs%2Fheads%2FCAS-13026#166-225

        Requires user configuration ~/.casa/rc to contain `synthesis.imager.memprofile.enable: 1`
        Expected output is casa.synthesis.imager.memprofile.PID.HOSTNAME.DATE_TIME_when_test_started.txt
        """
        # attribute for tracking metric
        self.unit = "file descriptors"

        casalog.setlogfile(self.templogfile)
        tclean(
            vis=self.datapath,
            imagename=self.imagename,
            phasecenter=self.phasecenter,
            scan=["17,11,13"],
            restoration=False,
            datacolumn="data",
            pbcor=False,
            spw="0",
            weighting="briggs",
            intent="OBSERVE_TARGET#ON_SOURCE",
            threshold="0mJy",
            robust=0.5,
            savemodel="none",
            imsize=self.imsize,
            stokes="I",
            nchan=self.nchan,
            deconvolver="hogbom",
            field="Pillar_3",
            npixels=0,
            niter=0,
            pblimit=0.2,
            restoringbeam=[],
            cell=["0.94arcsec"],
            start="230.490186515GHz",
            outframe="LSRK",
            specmode="cube",
            width="0.0610478663509MHz",
            gridder="mosaic",
            interactive=False,
            parallel=False,
        )

        with open(self.templogfile) as mylog:
            for line in mylog:
                a_match = re.search("casa.synthesis.imager.memprofile", line)
                if a_match:
                    str_match = a_match.string
                    break

        # Get name of memprofile created by tclean
        (start, middle, end) = str_match.partition("casa.synthesis.imager.memprofile")
        mem_profile = middle + end.rstrip()

        # Get the memory values of the second column named MemRSS_(VmRSS)_MB, for each row
        with open(mem_profile, "r") as mfile:
            memdict = OrderedDict()
            maxFDSize = 0
            for myrow in mfile:
                linelist = []
                print(myrow.rstrip())
                if myrow.startswith("#"):
                    continue

                linelist = myrow.split(",")
                tclean_step = str(linelist[-1].rstrip())
                memdict[tclean_step.strip("[]")] = int(linelist[1])
                maxFDSize = max(maxFDSize, int(linelist[7]))

        return maxFDSize

    def teardown(self):
        # remove the data products generated by the task
        os.system("rm -rf memtest_*")
        shutil.rmtree(self.input_ms, ignore_errors=True)
        try:
            os.remove(os.path.join(os.getcwd(), self.templogfile))
        except FileNotFoundError:
            pass
