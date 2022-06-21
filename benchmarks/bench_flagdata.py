import os, shutil
import numpy
from casatools import ctsys
from casatasks import flagdata

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

# ASV attributes
timeout = 10000
number = 2

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
        pass


class TaskModeSomething(BaseFlagSetup):
    """
    Benchmark runtime of taskname mode something
    """
    def setup(self):
        self.setUp_data4tfcrop()

    def time_taskmode_someinfo(self):
        """taskname: mode taskmode, .... (original test case name for reference)"""
        taskname(vis=self.vis, ......)

class TaskModeOther(BaseFlagSetup):
    """
    Benchmark runtime of taskname mode other
    """
    def setup(self):
        self.setUp_data4tfcrop()

    def time_taskmodeother_something(self):
        """taskname: ..... (original test case name)"""
         taskname(vis=self.vis, ......)

class TaskModeUsingSetupCache(BaseFlagSetup):
    """
    Benchmark runtime of flagdata using different selections
    """
    def setup_cache(self):
        # Create antennafile in disk
        myinput = 'name=VLA01\n' + \
                  'diameter=25.0\n' + \
                  'position=[-1601144.96146691, -5041998.01971858, 3554864.76811967]\n' + \
                  'name=VLA02\n' + \
                  'diameter=25.0\n' + \
                  'position=[-1601105.7664601889, -5042022.3917835914, 3554847.245159178]\n' + \
                  'name=VLA09\n' + \
                  'diameter=25.0\n' + \
                  'position=[-1601197.2182404203, -5041974.3604805721, 3554875.1995636248]\n' + \
                  'name=VLA10\n' + \
                  'diameter=25.0\n' + \
                  'position=[-1601227.3367843349,-5041975.7011900628,3554859.1642644769]\n'

        self.antfile = 'antfile.txt'
        create_input(myinput, self.antfile)

        # Create flagcmd file
        myinput = "mode='shadow' tolerance=0.0 addantenna='antfile.txt'"
        self.inpfile = 'listcmd.txt'
        create_input(myinput, self.inpfile)

    def setup(self):
        self.setUp_data4tfcrop()

    def teardown(self):
        if os.path.exists(self.inpfile):
            os.system("rm -rf listcmd*.txt antfile*.txt withdict.txt")

    def time_someothermode_info(self):
        """taskname: ....; (original test case)"""
        taskname(vis=self.vis, mode='list', inpfile=self.inpfile, savepars=True, outfile='withdict.txt',
                 flagbackup=False)

