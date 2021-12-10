import os, shutil
from casatools import ctsys
from casatasks import gaincal
from casatasks import applycal
from casatasks import bandpass


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
