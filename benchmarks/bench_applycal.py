import os, shutil
from casatools import ctsys
from casatasks import applycal

# ASV attributes (https://asv.readthedocs.io/en/stable/benchmarks.html?highlight=number#benchmark-attributes)
number=1
repeat = (1, 3, 60.0)
rounds=1
min_run_count=1
timeout = 600

class DataSetUp():

    datapath = ctsys.resolve('unittest/applycal/')

    def setup_basic(self):
        self.vis = 'applycalcopy.ms'
        self.gCal = 'tempgcal.G0'
        self.tCal = 'temptcal.T0'
        self.callibfile = 'refcallib.txt'

        if os.path.exists(self.vis):
            shutil.rmtree(self.vis)

        if os.path.exists(self.vis):
            shutil.rmtree(self.vis)
        if os.path.exists(self.gCal):
            shutil.rmtree(self.gCal)
        if os.path.exists(self.tCal):
            shutil.rmtree(self.tCal)
        if (os.path.exists(self.callibfile)):
            os.remove(self.callibfile)

        shutil.copytree(os.path.join(self.datapath, 'gaincaltest2.ms'), self.vis)
        shutil.copytree(os.path.join(self.datapath, 'gaincaltest2.ms.G0'), self.gCal)
        shutil.copytree(os.path.join(self.datapath, 'gaincaltest2.ms.T0'), self.tCal)
        self.callibfile = os.path.join(self.datapath, self.callibfile)

class StandardGainTable(DataSetUp):
    """
    Benchmark runtime of applycal with basic gaintables
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_basic_gaintable(self):
        applycal(vis=self.vis, gaintable=[self.gCal, self.tCal])

class SelectionTypes(DataSetUp):
    """
    Benchmark runtime of the selection parameters
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_select_field(self):
        applycal(vis=self.vis, gaintable=[self.gCal], field='1')

    def time_applycal_select_spw(self):
        applycal(vis=self.vis, gaintable=[self.gCal], spw='1')

    def time_applycal_select_intent(self):
        applycal(vis=self.vis, gaintable=[self.gCal], intent='*AMPLI*')

    def time_applycal_select_timerange(self):
        applycal(vis=self.vis, gaintable=[self.gCal], timerange='04:33:23~04:38:23')

    def time_applycal_select_uvrange(self):
        applycal(vis=self.vis, gaintable=[self.gCal], uvrange='>100klambda')

    def time_applycal_select_antenna(self):
        applycal(vis=self.vis, gaintable=[self.gCal], antenna='0~5&')

    def time_applycal_select_scan(self):
        applycal(vis=self.vis, gaintable=[self.gCal], scan='10')

class CalLibrary(DataSetUp):
    """
    Benchmark runtime using a callibrary
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_callibrary(self):
        applycal(vis=self.vis, docallib=True, callib=self.callibfile)

# Requires the use of another task
#class CalLibraryField():
#    """  """

class GainField(DataSetUp):
    """
    Benchmark runtime when selecting the gainfield
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_gainfield(self):
        applycal(vis=self.vis, gaintable=[self.tCal], gainfield='1')

class Interp(DataSetUp):
    """
    Benchmark runtime with different interpolation mode
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_interp(self):
        applycal(vis=self.vis, gaintable=[self.tCal], interp='cubicflag')

class SpwMap(DataSetUp):
    """
    Benchmark runtime when using spwmaps
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_spwmap(self):
        applycal(vis=self.vis, gaintable=[self.gCal], spwmap=[0, 0, 1, 1])

class CalWeight(DataSetUp):
    """
    Benchmark runtime when calwt is False
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_calweight(self):
        applycal(vis=self.vis, gaintable=[self.gCal], calwt=[False])

class Parang(DataSetUp):
    """
    Benchmark runtime when using parang
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_parang(self):
        applycal(vis=self.vis, gaintable=[self.gCal], parang=True)

class CalFlag(DataSetUp):
    """
    Benchmark runtime when in applymode calflag
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_calflag(self):
        applycal(vis=self.vis, gaintable=[self.gCal], applymode='calflag')

class TrialMode(DataSetUp):
    """
    Benchmark runtime when in applymode trial
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_trial(self):
        applycal(vis=self.vis, gaintable=[self.gCal], applymode='trial')

class ApplyModes(DataSetUp):
    """
    Benchmark runtime for different apply modes
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_strict_mode(self):
        applycal(vis=self.vis, gaintable=[self.gCal], applymode='calflagstrict')

    def time_applycal_flag_only_mode(self):
        applycal(vis=self.vis, gaintable=[self.gCal], applymode='flagonly')

    def time_applycal_cal_only_mode(self):
        applycal(vis=self.vis, gaintable=[self.gCal], applymode='calonly')

    def time_applycal_flag_only_strict_mode(self):
        applycal(vis=self.vis, gaintable=[self.gCal], applymode='flagonlystrict')

class FlagBackup(DataSetUp):
    """
    Benchmark runtime when using flagbackup
    """

    def setup(self):
        self.setup_basic()

    def time_applycal_flag_backup(self):
        applycal(vis=self.vis, gaintable=[self.gCal], flagbackup=True)

