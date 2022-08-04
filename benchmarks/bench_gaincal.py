import os, shutil
from casatools import ctsys
from casatasks import gaincal

# ASV attributes
timeout = 10000
number = 2


class DataSetUp():

    datapath = ctsys.resolve('unittest/applycal/')

    def setup_basic(self):
        self.vis = 'gaincaltest2copy.ms'
        self.compCal = 'gaincaltest2.ms.G0'
        self.tCal = 'gaincaltest2.ms.T0'
        self.cal = 'testoucal.cal'

        if os.path.exists(self.vis):
            shutil.rmtree(self.vis)

        if os.path.exists(self.vis):
            shutil.rmtree(self.vis)
        if os.path.exists(self.compCal):
            shutil.rmtree(self.compCal)
        if os.path.exists(self.tCal):
            shutil.rmtree(self.tCal)
        if (os.path.exists(self.cal)):
            shutil.rmtree(self.cal)

        shutil.copytree(os.path.join(self.datapath, 'gaincaltest2.ms'), self.vis)
        shutil.copytree(os.path.join(self.datapath, 'gaincaltest2.ms.G0'), self.compCal)
        shutil.copytree(os.path.join(self.datapath, 'gaincaltest2.ms.T0'), self.tCal)

    def teardown_basic(self):
        if os.path.exists(self.cal):
            shutil.rmtree(self.cal)


class FullGainCal(DataSetUp):
    """
    Benchmark runtime of a standard gaincal call with multiple selections
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_fullcal(self):
        gaincal(vis=self.vis, caltable=self.cal, combine='scan', solint='inf', field='0', refant='0',
                smodel=[1, 0, 0, 0], scan='0~9')


class MinSNRFlag(DataSetUp):
    """
    Benchmark Runtime when setting min SNR threshold
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_minsnr(self):
        gaincal(vis=self.vis, caltable=self.cal, solint='30s', field='0', refant='0',
                smodel=[1, 0, 0, 0], minsnr=1000)


class GaincalSelections(DataSetUp):
    """
    Benchmark runtime with basic selection parameters
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_fieldSelect(self):
        gaincal(vis=self.vis, caltable=self.cal, combine='scan', solint='inf', field='0',
                smodel=[1, 0, 0, 0])

    def time_gaincal_refantSelect(self):
        gaincal(vis=self.vis, caltable=self.cal, combine='scan', solint='inf', refant='0',
                smodel=[1, 0, 0, 0])

    def time_gaincal_scanSelect(self):
        gaincal(vis=self.vis, caltable=self.cal, solint='inf',
                smodel=[1, 0, 0, 0], scan='2')

    def time_gaincal_spwSelect(self):
        gaincal(vis=self.vis, caltable=self.cal, solint='inf',
                smodel=[1, 0, 0, 0], spw='2')

    def time_gaincal_uvRangeSelect(self):
        gaincal(vis=self.vis, caltable=self.cal, spw='2', refant='0', uvrange='<1160', minblperant=1)

    def time_gaincal_antennaSelect(self):
        gaincal(vis=self.vis, caltable=self.cal, refant='0', field='0', solint='inf', combine='scan', antenna='0~5&',
                smodel=[1, 0, 0, 0], gaintype='G')


class RefantSelection(DataSetUp):
    """
    Benchmark runtime when setting new refant
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_refant(self):
        gaincal(vis=self.vis, caltable=self.cal, solint='inf', field='0', combine='scan', refant='1',
                smodel=[1, 0, 0, 0])


class PreApplyTables(DataSetUp):
    """
    Benchmark runtime when pre-applying cal tables
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_apply_tables(self):
        gaincal(vis=self.vis, caltable=self.cal, refant='0', solint='inf', smodel=[1, 0, 0, 0], gaintype='G', field='0',
                gaintable=[self.tCal, self.compCal], gainfield=['0', '0'], interp=[''])


class MinBlPerAnt(DataSetUp):
    """
    Benchmark runtime when setting min baseline threshold
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_minbl(self):
        gaincal(vis=self.vis, caltable=self.cal, refant='0', solint='int', smodel=[1, 0, 0, 0], gaintype='G',
                combine='scan', antenna='0~5&', minblperant=6)


class CalModes(DataSetUp):
    """
    Benchmark runtime with the different cal modes
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_calmode_P(self):
        gaincal(vis=self.vis, caltable=self.cal, field='0', smodel=[1, 0, 0, 0], solint='inf', combine='scan',
                calmode='p')

    def time_gaincal_calmode_A(self):
        gaincal(vis=self.vis, caltable=self.cal, field='0', smodel=[1, 0, 0, 0], solint='inf', combine='scan',
                calmode='a')



class GainTypes(DataSetUp):
    """
    Benchmark runtime with different gain types
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_gain_type_K(self):
        gaincal(vis=self.vis, caltable=self.cal, field='0', smodel=[1, 0, 0, 0], solint='inf', combine='scan',
                gaintype='KCROSS', refant='0')

    def time_gaincal_gain_type_spline(self):
        gaincal(vis=self.vis, caltable=self.cal, field='0', smodel=[1, 0, 0, 0], solint='inf', combine='scan',
                gaintype='GSPLINE', refant='0')


class UseSpwMap(DataSetUp):
    """
    Benchmark runtime using spwmap
    """

    def setup(self):
        self.setup_basic()

    def teardown(self):
        self.teardown_basic()

    def time_gaincal_use_spw_map(self):
        gaincal(vis=self.vis, caltable=self.cal, field='0', smodel=[1, 0, 0, 0], solint='inf', combine='scan',
                refant='0', spwmap=[0, 0, 1, 1])