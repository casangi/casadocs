import os, shutil
import numpy
from casatools import ctsys
from casatasks import flagdata

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (1, 5, 60.0) # between 1 and 5 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 3            # amount of instances a "repeat block" is run to collect samples
min_run_count = 3     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap for duration of a single test execution

# Helper functions for tests
def create_input(str_text, filename):
    """Save the string in a text file"""
    inp = filename
    cmd = str_text
    # remove file first
    if os.path.exists(inp):
        os.system('rm -f ' + inp)
    # save to a file
    with open(inp, 'w') as f:
        f.write(cmd)
    f.close()
    return

class BaseFlagSetup():
    # Test datasets; root directory is read from config.py
    datapath = ctsys.resolve("unittest/flagdata/")

    def setUp_data4tfcrop(self):
        """EVLA MS, 4 ants, scan=30,31 spw=0~15, 64 chans, RR,RL,LR,LL"""
        self.vis = "Four_ants_3C286.ms"
        if os.path.exists(self.vis):
            os.system('rm -rf ' + self.vis + '*')
        shutil.copytree(os.path.join(self.datapath,self.vis),self.vis)

    def setUp_ngc5921(self):
        """VLA data set, scan=1~7, spw=0 63 chans, RR,LL"""
        self.vis = "ngc5921.ms"
        if os.path.exists(self.vis):
            os.system('rm -rf ' + self.vis + '*')
        shutil.copytree(os.path.join(self.datapath,self.vis),self.vis)

    def setUp_WRay_perf(self):
        self.vis = "uid___A002_Xe1f219_X6d0b_data_autocorr_WRAY_scan7.ms/"
        if os.path.exists(self.vis):
            os.system('rm -rf ' + self.vis + '*')
        shutil.copytree(os.path.join(self.datapath,self.vis),
                        os.path.join(os.getcwd(), self.vis))

    def setUp_alma_ms(self):
        """ALMA MS, scan=1,8,10 spw=0~3 4,128,128,1 chans, I,XX,YY"""
        self.vis = "uid___A002_X30a93d_X43e_small.ms"
        if os.path.exists(self.vis):
            os.system('rm -rf ' + self.vis + '*')
        shutil.copytree(os.path.join(self.datapath, self.vis), self.vis)

    def setUp_tsys(self):
        self.vis = "X7ef.tsys"
        if os.path.exists(self.vis):
            os.system('rm -rf ' + self.vis + '*')
        shutil.copytree(os.path.join(self.datapath, self.vis), self.vis)

    def setUp_bpass(self):
        self.vis = "cal.fewscans.bpass"
        if os.path.exists(self.vis):
            os.system('rm -rf ' + self.vis + '*')
        shutil.copytree(os.path.join(self.datapath, self.vis), self.vis)

    def setUp_shadowdata(self):
        """ALMA ACA observation with one field in APP ref frame"""
        self.vis = "shadowAPP.ms"
        if os.path.exists(self.vis):
            os.system('rm -rf ' + self.vis + '*')
        shutil.copytree(os.path.join(self.datapath, self.vis), self.vis)

class AntintMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata in antint mode
    """
    def setup(self):
        self.setUp_data4tfcrop()

    def time_antint_low_threshold_spw(self):
        """flagdata: mode antint, with low threshold; (original test_antint_spw3_low_threshold)"""
        flagdata(vis=self.vis, mode='antint', spw='3', antint_ref_antenna='ea01', minchanfrac=-.1)

class CalibrationBandpass(BaseFlagSetup):
    """
    Benchmark runtime of flagdata on bandpass calibration tables
    """
    def setup(self):
        self.setUp_bpass()

    def time_bandpass_clip_timerange(self):
        """Flagdata: clip a timerange from field 3C286_A; (original test_cal_time1)"""
        flagdata(vis=self.vis, mode='clip', timerange='<14:12:52',clipzeros=True,
                 clipminmax=[0.,0.35], datacolumn='CPARAM',flagbackup=False)

class CalibrationTsys(BaseFlagSetup):
    """
    Benchmark runtime of flagdata on Tsys calibration tables
    """
    def setup(self):
        self.setUp_tsys()

    def time_tsys_clip_fparam(self):
        """Flagdata: flag default data column FPARAM; (original test_default_fparam)"""
        flagdata(vis=self.vis, mode='clip', clipminmax=[0,500], flagbackup=False,
                 datacolumn='FPARAM')

class ClipMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata clip mode
    """
    def setup(self):
        self.setUp_data4tfcrop()

    def time_clip_corrected_data(self):
        """flagdata: clip CORRECTED data column; (original test_datacol_corrected)"""
        flagdata(vis=self.vis, flagbackup=False, mode='clip', datacolumn='CORRECTED',
                 clipminmax=[0.,10.])

    def time_clip_with_timeavg(self):
        """flagdata: clip with time averaging in spw 9; (original test_timeavg_spw9_2scans)"""
        flagdata(vis=self.vis, flagbackup=False, mode='clip', datacolumn='DATA', spw='9',
                 timeavg=True, timebin='2s', clipminmax=[0.0, 0.08])


class ElevationMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata in elevation mode
    """
    def setup(self):
        self.setUp_ngc5921()

    def time_elevation_interval(self):
        """Flagdata: flag an interval between upper and lower elevations; (original test_interval)"""
        flagdata(vis = self.vis,mode = 'elevation',lowerlimit = 55,upperlimit = 60,
                  savepars=False,flagbackup=False)

class ListMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata list mode used in the pipeline
    """
    flags_cmd = "uid___A002_Xe1f219_X6d0b.flagcmds.txt"

    def setup_cache(self):
        if not os.path.exists(self.flags_cmd):
            shutil.copyfile(
                os.path.join(self.datapath, self.flags_cmd), 
                os.path.join(os.getcwd(), self.flags_cmd)
            )

    def setup(self):
        self.setUp_WRay_perf()

    def time_list_tbuff(self):
        """Flagdata list mode from pipeline hifa_flagdata"""
        flagdata(
            vis=self.vis,
            mode="list",
            inpfile=self.flags_cmd,
            tbuff=[0.048, 0.0],
            action="apply",
            flagbackup=False,
            savepars=False,
        )

    def time_list_bandpassflag(self):
        """Flagdata list mode from pipeline hifa_bandpassflag"""
        flagdata(
            vis=self.vis,
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

    def time_list_summary(self):
        """Flagdata list mode from pipeline hifa_rawflagchans"""
        summary_dict = flagdata(
            vis=self.vis,
            mode="list",
            inpfile=["mode='summary' name='before'"],
            reason="any",
            action="apply",
            flagbackup=False,
            savepars=False,
        )

    def teardown(self):
        # remove the data products generated by the task
        #os.remove(self.flags_cmd)
        shutil.rmtree(self.vis, ignore_errors=True)

class ListFileMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata list mode with input files
    """
    inpfile1 = 'listcmd1.txt'
    inpfile2 = 'listcmd2.txt'
    inpfile3 = 'listcmd3.txt'

    def setup_cache(self):
        # Create 3 flagcmd files and save to disk
        myinput = "scan='1'\n" \
                  "scan='2'\n" \
                  "# a comment line\n" \
                  "scan='3'"
        create_input(myinput, self.inpfile1)

        myinput = "scan='5'\n" \
                  " \n" \
                  "scan='6'\n" \
                  "scan='7'"
        create_input(myinput, self.inpfile2)

        myinput = "scan='4' mode='clip' clipminmax=[0,4]"
        
        create_input(myinput, self.inpfile3)

    def setup(self):
        self.setUp_ngc5921()

    def time_list_from_3files(self):
        """Flagdata list mode reading commands from three files; (original test_file_CAS4819)"""
        flagdata(vis=self.vis, mode='list', inpfile=[self.inpfile1, self.inpfile2, self.inpfile3],
                 flagbackup=False)

class RflagMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata rflag mode
    """
    def setup(self):
        self.setUp_data4tfcrop()
        self.t1 = [numpy.int32(1), 10, numpy.float32(0.1)]
        self.t2 = [1, numpy.int16(11), numpy.float64(0.07)]

    def time_rflag_numpy_types(self):
        """flagdata: rflag, thresholds using numpy types; (original test_rflag_partial_thresholds)"""
        flagdata(vis=self.vis, mode='rflag', spw='9,10', timedev=[self.t1, self.t2], freqdev=0.5,
                 flagbackup=False, extendflags=False)

class Selections(BaseFlagSetup):
    """
    Benchmark runtime of flagdata using different selections
    """
    def setup(self):
        self.setUp_alma_ms()

    def time_sel_abs_wvr(self):
        """flagdata: clip ABS_WVR; (original test_abs_wvr)"""
        flagdata(vis=self.vis, mode='clip',clipminmax=[0,50], correlation='ABS_WVR', savepars=False,
                 flagbackup=False)

    def time_sel_autocorr_wvr(self):
        """flagdata: CAS-5286, do not flag auto-correlations in WVR data; (original test_autocorr_wvr)"""
        flagdata(vis=self.vis, autocorr=True, flagbackup=False)

class ShadowMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata using different selections
    """
    antfile = 'antfile.txt'
    inpfile = 'listcmd.txt'

    def setup(self):
        self.setUp_shadowdata()

        # Create antennafile in disk
        myinput = "name=VLA01\n" \
                  "diameter=25.0\n" \
                  "position=[-1601144.96146691, -5041998.01971858, 3554864.76811967]\n" \
                  "name=VLA02\n" \
                  "diameter=25.0\n" \
                  "position=[-1601105.7664601889, -5042022.3917835914, 3554847.245159178]\n" \
                  "name=VLA09\n" \
                  "diameter=25.0\n" \
                  "position=[-1601197.2182404203, -5041974.3604805721, 3554875.1995636248]\n" \
                  "name=VLA10\n" \
                  "diameter=25.0\n" \
                  "position=[-1601227.3367843349,-5041975.7011900628,3554859.1642644769]\n"

        create_input(myinput, self.antfile)

        # Create flagcmd file
        myinput = "mode='shadow' tolerance=0.0 addantenna='antfile.txt'"
        create_input(myinput, self.inpfile)

    def teardown(self):
        if os.path.exists(self.inpfile):
            os.system("rm -rf listcmd*.txt antfile*.txt withdict.txt")

    def time_shadow_addantenna(self):
        """flagdata: use antenna file in list mode; (original test_addantenna)"""
        flagdata(vis=self.vis, mode='list', inpfile=self.inpfile, savepars=True, outfile='withdict.txt',
                 flagbackup=False)

    def time_shadow_absent_antennas(self):
        """flagdata: shadow by antennas not present in MS; (original test_CAS2399)"""
        flagdata(vis=self.vis, mode='shadow', tolerance=0.0, addantenna=self.inpfile, flagbackup=False)

class TfcropMode(BaseFlagSetup):
    """
    Benchmark runtime of flagdata tfcrop mode
    """
    def setup(self):
        self.setUp_data4tfcrop()

    def time_tfcrop_abs_rr(self):
        """flagdata:: flag with tfcrop mode an ABS_RR correlation; (original test_tfcrop1)"""
        flagdata(vis=self.vis, mode='tfcrop', correlation='ABS_RR',ntime=51.0,spw='9',
                 savepars=False, extendflags=False)

    def time_tfcrop_extendflags(self):
        """flagdata: flag with tfcrop mode and extend flags automatically"""
        flagdata(vis=self.vis, mode='tfcrop', spw='0', extendflags=True, flagbackup=False)

