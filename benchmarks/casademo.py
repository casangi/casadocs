from collections import OrderedDict
import re, os, shutil
from casatools import casalog
from casatools import ctsys
from casatasks import flagdata
from casatasks import gaincal
from casatasks import applycal
from casatasks import tclean
from casatasks import bandpass


class tclean_memory_suite:
    """
    An example benchmark that adapts test_perf_tclean_mem_setweighting.py to asv
    """

    timeout = 10000

    dataroot = ctsys.resolve(
        os.path.join(
            os.environ.get("ASV_CONF_DIR"),
            "casatestdata/performance/tclean_mem_setweighting/",
        )
    )
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
        unit = "file descriptors"

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

        with open(templogfile) as mylog:
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
        os.remove(os.path.join(os.getcwd(), self.templogfile))
        shutil.rmtree(self.input_ms, ignore_errors=True)


class flagdata_suite:
    """
    An example benchmark that adapts CAS-13490 to asv
    """

    dataroot = ctsys.resolve(
        os.path.join(
            os.environ.get("ASV_CONF_DIR"), "casatestdata/performance/flagdata_runtime/"
        )
    )
    input_ms = "uid___A002_Xe1f219_X6d0b_data_autocorr_WRAY_scan7.ms/"
    flags_cmd = "uid___A002_Xe1f219_X6d0b.flagcmds.txt"

    timeout = 10000

    def setup_cache(self):
        # only run once for repeated tests
        pass

    def setup(self):
        # run for each repeated test

        # iterations per sample
        self.number = 2

        # assign our test dataset
        self.datapath = os.path.join(self.dataroot, self.input_ms)

        ## fresh copy of the test MS to the tmp directory where tests are run ?
        # if not os.path.exists(self.input_ms):
        #    shutil.copytree(os.path.join(self.dataroot, self.input_ms),
        #                    os.path.join(os.getcwd(), self.input_ms))

        # Copy the flagcmd text file into temporary test directory
        if not os.path.exists(self.flags_cmd):
            shutil.copyfile(
                os.path.join(self.dataroot, self.flags_cmd),
                os.path.join(os.getcwd(), self.flags_cmd),
            )

    def time_flagdata_summary(self):
        """hifa_importdata"""
        summary_dict = flagdata(vis=self.datapath, flagbackup=False, mode="summary")

    def time_flagdata_list(self):
        """hifa_flagdata"""
        flagdata(
            vis=self.datapath,
            mode="list",
            inpfile=self.flags_cmd,
            tbuff=[0.048, 0.0],
            action="apply",
            flagbackup=False,
            savepars=False,
        )

    def time_flagdata_list_summary(self):
        """hifa_rawflagchans"""
        summary_dict = flagdata(
            vis=self.datapath,
            mode="list",
            inpfile=["mode='summary' name='before'"],
            reason="any",
            action="apply",
            flagbackup=False,
            savepars=False,
        )

    def time_flagdata_bandpassflag(self):
        """hifa_bandpassflag"""
        flagdata(
            vis=self.datapath,
            mode="list",
            inpfile=[
                "intent='CALIBRATE_BANDPASS#ON_SOURCE' spw='16' antenna='CM05' \
                 timerange='20:09:50~20:09:52' field='J1924-2914' reason='bad antenna timestamp'",
                "intent='CALIBRATE_BANDPASS#ON_SOURCE' spw='20' antenna='CM05' \
                          timerange='20:09:20~20:09:22' field='J1924-2914' reason='bad antenna timestamp'",
                "intent='CALIBRATE_BANDPASS#ON_SOURCE' spw='20' antenna='CM05' \
                          timerange='20:10:21~20:10:22' field='J1924-2914' reason='bad antenna timestamp'",
                "intent='CALIBRATE_BANDPASS#ON_SOURCE' spw='22' antenna='CM05' \
                          timerange='20:09:30~20:09:32' field='J1924-2914' reason='bad antenna timestamp'",
            ],
            reason="any",
            action="apply",
            flagbackup=False,
            savepars=False,
        )

    def teardown(self):
        # remove the data products generated by the task
        os.remove(self.flags_cmd)
        shutil.rmtree(self.input_ms, ignore_errors=True)


class calibration_suite:
    """
    An example benchmark that adapts PLWG benchmark tests of 7m ALMA project 2019.1.01056.S (MOUS uid://A001/X1465/X1b3c) to asv
    """

    dataroot = ctsys.resolve(
        os.path.join(
            os.environ.get("ASV_CONF_DIR"),
            "casatestdata/performance/calibration_runtime/",
        )
    )
    input_ms = "uid___A002_Xe1f219_X6d0b.ms"
    applycal_library = "uid___A002_Xe1f219_X6d0b.ms.s12.4.callibrary"
    library_subtables = [
        "uid___A002_Xe1f219_X6d0b.ms.h_tsyscal.s6_1.tsyscal.tbl",
        "uid___A002_Xe1f219_X6d0b.ms.hifa_bandpassflag.s12_1.spw16_18_20_22.channel.solintinf.bcal.tbl",
        "uid___A002_Xe1f219_X6d0b.ms.hifa_bandpassflag.s12_3.spw16_18_20_22.solintinf.gacal.tbl",
        "uid___A002_Xe1f219_X6d0b.ms.hifa_bandpassflag.s12_4.spw16_18_20_22.solintint.gpcal.tbl",
    ]
    tsyscal_table = library_subtables[0]
    bandpass_table = library_subtables[1]
    gaincal_table = library_subtables[3]

    timeout = 10000

    def setup_cache(self):
        # only run once for repeated tests
        pass

    def setup(self):
        # run for each repeated test

        # iterations per sample
        self.number = 2

        # fresh copy of the test MS to the tmp directory where tests are run
        shutil.copytree(
            os.path.join(self.dataroot, self.input_ms),
            os.path.join(os.getcwd(), self.input_ms),
        )

        # Copy the callibrary (and associated tables) into temporary test directory
        shutil.copyfile(
            os.path.join(self.dataroot, self.applycal_library),
            os.path.join(os.getcwd(), self.applycal_library),
        )

        for st in self.library_subtables:
            if not os.path.exists(st):
                shutil.copytree(
                    os.path.join(self.dataroot, st), os.path.join(os.getcwd(), st)
                )
        # Redundant to copy gaincal_table explicitly unless it changes

    def time_applycal_callib(self):
        """Taken from the hifa_bandpassflag step of ALMA pipeline run 2019.1.01056.S_2021_07_20T07_45_18.149/

        Note that this is from on-the-fly application of preliminary phase-up, bandpass, and amplitude caltables, not the later stage hifa_applycal
        Expected to take ~48s, could be sped up by splitting out SPWs (especially the square law detector windows) or applying to only one of them.
        """
        applycal(
            vis=self.input_ms,
            field="J1924-2914",
            spw="16,18,20,22",
            intent="CALIBRATE_BANDPASS#ON_SOURCE",
            selectdata=True,
            timerange="",
            uvrange="",
            antenna="*&*",
            scan="",
            observation="",
            msselect="",
            docallib=True,
            callib=self.applycal_library,
            gaintable=[],
            gainfield=[],
            interp=[],
            spwmap=[],
            calwt=[True],
            parang=False,
            applymode="calflagstrict",
            flagbackup=False,
        )

    def time_gaincal(self):
        """Taken from the hifa_bandpassflag step of ALMA pipeline run 2019.1.01056.S_2021_07_20T07_45_18.149/

        Expected to take ~7s
        """
        gaincal(
            vis=self.input_ms,
            caltable=self.gaincal_table,
            field="J1924-2914",
            spw="16,18,20,22",
            intent="CALIBRATE_BANDPASS#ON_SOURCE",
            selectdata=True,
            timerange="",
            uvrange="",
            antenna="0~9",
            scan="",
            observation="",
            msselect="",
            solint="int",
            combine="",
            preavg=-1.0,
            refant="CM03,CM10,CM02,CM12,CM06,CM05,CM11,CM04,CM07,CM01",
            refantmode="flex",
            minblperant=4,
            minsnr=3.0,
            solnorm=False,
            normtype="mean",
            gaintype="G",
            smodel=[],
            calmode="p",
            solmode="",
            rmsthresh=[],
            corrdepflags=False,
            append=False,
            splinetime=3600.0,
            npointaver=3,
            phasewrap=180.0,
            docallib=False,
            callib="",
            gaintable=[self.gaincal_table],
            gainfield=["J1924-2914"],
            interp=["linear,linear"],
            spwmap=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 18, 20, 22, 16, 16, 18, 18, 20, 20, 22,],
            parang=False,
        )

    def time_bandpass(self):
        """Taken from the hifa_bandpassflag step of ALMA pipeline run 2019.1.01056.S_2021_07_20T07_45_18.149/"""
        bandpass(
            vis=self.input_ms,
            caltable=self.bandpass_table,
            field="J1924-2914",
            spw="22",
            intent="CALIBRATE_BANDPASS#ON_SOURCE",
            selectdata=True,
            antenna="0~9",
            solint="inf,15.625000MHz",
            combine="scan",
            refant="CM03,CM10,CM02,CM12,CM06,CM05,CM11,CM04,CM07,CM01",
            minblperant=4,
            minsnr=3.0,
            solnorm=True,
            bandtype="B",
            append=True,
            gaintable=[self.tsyscal_table, self.gaincal_table],
            gainfield=["J1924-2914", "nearest"],
            interp=["linear,linear", "linear,linear"],
            spwmap=[
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 18, 20, 22, 16, 16, 18, 18, 20, 20, 22,],
                [],
            ],
        )

    def teardown(self):
        # remove the data products generated by the setup methods and the task
        os.remove(self.applycal_library)
        shutil.rmtree(self.gaincal_table, ignore_errors=True)
        shutil.rmtree(self.input_ms, ignore_errors=True)
