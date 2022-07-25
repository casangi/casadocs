from collections import OrderedDict
import re, os, shutil
from casatools import ctsys
from casatasks import casalog
from casatasks import tclean


class tclean_memory_suite:
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

    def track_tclean_file_descriptors_cubemode_mosaic_briggs(self):
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
