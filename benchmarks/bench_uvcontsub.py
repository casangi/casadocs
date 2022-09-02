import os, shutil
import numpy
from casatools import ctsys
from casatasks import uvcontsub

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (1, 5, 60.0) # between 1 and 5 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 3            # amount of instances a "repeat block" is run to collect samples
min_run_count = 3     # enforce the min_repeat * rounds setting is met
timeout = 1800        # conservative 0.5hr hard cap for duration of a single test execution

# Input data sets
datapath = ctsys.resolve("unittest/uvcontsub/")
ms_simple = 'known0.ms'
datapath_simple = ctsys.resolve(os.path.join(datapath, ms_simple))

# SPW 1 of this dataset has 1 channel
ms_alma = 'uid___X02_X3d737_X1_01_small.ms'
datapath_alma = ctsys.resolve(os.path.join(datapath, ms_alma))

# MS for tests that use CORRECTED_DATA
# Beware: this is all flagged!
ms_corr = 'uid___A002_X71a45c_X1d24.ms.split'
datapath_corr = ctsys.resolve(os.path.join(datapath, ms_corr))

# Another MS for tests that use CORRECTED_DATA
ms_papersky = 'papersky_standard.ms'
datapath_papersky = ctsys.resolve(os.path.join(datapath, ms_papersky))

# Mixed polarizations, from CAS-12283. This MS has ~60 SPWs with very mixed pols
ms_mixed_pols = 'split_ddid_mixedpol_CAS-12283.ms'
datapath_mixed_pols = ctsys.resolve(os.path.join(datapath, ms_mixed_pols))

class BaseClassSetup():
    # Cannot cleanup files copied by this method
    def setup_cache(self):
        shutil.copytree(datapath_simple, ms_simple)
        shutil.copytree(datapath_alma, ms_alma)
        shutil.copytree(datapath_corr, ms_corr)
        shutil.copytree(datapath_papersky, ms_papersky)
        shutil.copytree(datapath_mixed_pols, ms_mixed_pols)

class Uvcontsub_Basic():
    """
    Runtime benchmark tests for uvcontsub basic functionality
    """
    def setup_cache(self):
        shutil.copytree(datapath_simple, ms_simple)
        shutil.copytree(datapath_alma, ms_alma)
        shutil.copytree(datapath_corr, ms_corr)
        shutil.copytree(datapath_papersky, ms_papersky)
        shutil.copytree(datapath_mixed_pols, ms_mixed_pols)

    def setup(self):
        # Input MS is always strictly read-only, one copy in setup_cache is enough
        # Default output name for simple tests
        self.output = 'test_uvcs_output.ms'

    def teardown(self):
        if os.path.exists(self.output):
            shutil.rmtree(self.output)

    def time_makes_output_ms_data(self):
        uvcontsub(vis=ms_simple, outputvis=self.output)

    def time_select_field(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, field='2')

    def time_select_spw(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, spw='1')

    def time_select_spw_mismatching_fitspec(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, spw='1', fitspec='0')

    def time_select_scan(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, scan='2')

    def time_select_intent(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, intent='*AMPLI*')

    def time_select_array(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, array='0')

    def time_select_observation(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, observation='0')

    def time_datacolumn(self):
        uvcontsub(vis=ms_corr, outputvis=self.output, datacolumn='CORRECTED')

    def time_fitspec_empty(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitspec='')

    def time_fitspec_spws(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitspec='0')

    def time_fitspec_spw_one_chan(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, field='0', fitspec='1')

    def time_fitspec_dict_fitspec_one_chan(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, field='0',
                        fitspec={'0':
                                 {'1': {'chan': '',
                                        'fitorder': 0}}
                        })

    def time_fitspec_dict_fitspec_one_chan_order1(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, field='0',
                        fitspec={'0':
                                 {'1': {'chan': '',
                                        'fitorder': 1}}
                        })

    def time_fitspec_dict_select_spw_mismatching(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, field='0', spw='1',
                        fitspec={'0':
                                 {'0': {'chan': '2~127',
                                        'fitorder': 0}},
                                 '1':
                                 {'0': {'chan': '0~40',
                                        'fitorder': 1}},
                                 '3':
                                 {'0': {'chan': '1~33;56~119',
                                        'fitorder': 1}}
                        })

    def time_fitspec_channels(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitspec='0:5~19')

    def time_fitspec_multifield(self):
        uvcontsub(vis=ms_alma, outputvis=self.output,
                        fitspec={
                            '0': {'0': {'chan': '100~500;600~910;1215~1678;1810~1903',
                                        'fitorder': 0}},
                            '1': 'NONE',
                            '2': {'0': {'chan': '100~1903',
                                        'fitorder': 0}}
                        })

    def time_fitspec_multifield_blocks(self):
        uvcontsub(vis=ms_alma, outputvis=self.output,
                        fitspec={
                            '0, 1': {'0': {'chan': '100~500;600~900;1200~1900',
                                           'fitorder': 0}},
                            '2': {'0': {'chan': '100~1903',
                                        'fitorder': 0}}
                        })

    def time_fitspec_multifield_multispw_diff_fitorder(self):
        uvcontsub(vis=ms_alma, outputvis=self.output,
                        fitspec={'0': {'0': {'chan':
                                             '100~500;600~910;1215~1678;1810~1903',
                                             'fitorder': 1},
                                       '1': {'chan': '0',
                                             'fitorder': 2}},
                                 '1': 'NONE',
                                 '2': {'0': {'chan': '100~1903',
                                             'fitorder': 2}}
                        })

    def time_fitspec_multifield_fields_sel(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, field='1,2',
                        fitspec={'1': {'0': {'chan': '100~500;600~900',
                                             'fitorder': 0}},
                                 '2': {'0': {'chan': '100~1903',
                                             'fitorder': 0}}
                        })

    def time_fitspec_separate_fields(self):
        uvcontsub(vis=ms_alma, outputvis=self.output, field='1',
                           fitspec='0:100~500;600~910;1215~1678;1810~1903')

    def time_fitspec_spws_sel(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, spw='0', fitspec='0')

    def time_fitmethod_gsl(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitmethod='gsl')

    def time_fitmethod_casacore(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitmethod='casacore')

    def time_fitorder1(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitorder=1,
                        fitspec='0:2~20')

    def time_fitorder2(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitorder=2,
                        fitspec='0:2~20')

    def time_fitspec_dict_fitorder1(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitorder=1,
                        fitspec={'0': {'0': {'chan': '2~20',
                                             'fitorder': 1}}
                        })

    def time_fitspec_dict_fitorder2(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, fitorder=2,
                        fitspec={'0': {'0': {'chan': '2~20',
                                             'fitorder': 2}}
                        })

    def time_fitspec3_spws_fitorder0(self):
        uvcontsub(vis=ms_mixed_pols, outputvis=self.output, fitorder=0,
                                fitspec='3')

    def time_fitspec_spwschans_fitorder3(self):
        uvcontsub(vis=ms_mixed_pols, outputvis=self.output, fitorder=3,
                                fitspec='4:50~503;600~850;900~1002')

    def time_writemodel(self):
        uvcontsub(vis=ms_simple, outputvis=self.output, writemodel=True)

    def time_writemodel_from_corrected(self):
        uvcontsub(vis=ms_papersky, outputvis=self.output, datacolumn='CORRECTED',
                        writemodel=True)

    def time_writemodel_from_corrected_all_flagged(self):
        uvcontsub(vis=ms_corr, outputvis=self.output, datacolumn='CORRECTED',
                        writemodel=True)

    def time_mixed_pols(self):
        uvcontsub(vis=ms_mixed_pols, outputvis=self.output)


class UVContsub_Numerical():
    """
    Benchmar Tests of numerical behavior based on simulated datasets
    """
    def setup_cache(self):
        self.ms_cont_nonoise_order_0 = 'sim_alma_cont_poly_order_0_nonoise.ms'
        self.ms_cont_noise_order_0 = 'sim_alma_cont_poly_order_0_noise.ms'
        self.ms_cont_nonoise_order_1 = 'sim_alma_cont_poly_order_1_nonoise.ms'
        self.ms_cont_noise_order_1 = 'sim_alma_cont_poly_order_1_noise.ms'
        self.sim_mss = [self.ms_cont_nonoise_order_0, self.ms_cont_noise_order_0,
                       self.ms_cont_nonoise_order_1, self.ms_cont_noise_order_1]

        for sim in self.sim_mss:
            datapath_sim = ctsys.resolve(os.path.join(datapath, sim))
            shutil.copytree(datapath_sim, sim)

    def setup(self):
        # Input MS is always strictly read-only, one copy in setUpClass is enough
        # Default output name for simple tests
        self.output = 'test_numerical_uvcs_output.ms'
        self.fitspec = '0:0~59;86~127'

    def teardown(self):
        if os.path.exists(self.output):
            shutil.rmtree(self.output)

    def time_sim_specline_nonoise_pol_0(self):
        """ Check fitting of continuum as polynomial order 0"""
        uvcontsub(vis=self.ms_cont_nonoise_order_0, outputvis=self.output,
                        fitorder=0, fitspec=self.fitspec)

    def time_sim_specline_noise_pol_0(self):
        """ Check fitting of continuum as polynomial order 0"""
        uvcontsub(vis=self.ms_cont_noise_order_0, outputvis=self.output,
                        fitorder=0, fitspec=self.fitspec)

    def time_sim_specline_nonoise_pol_1(self):
        """ Check fitting of continuum as polynomial order 1"""
        uvcontsub(vis=self.ms_cont_nonoise_order_1, outputvis=self.output,
                        fitorder=1, fitspec=self.fitspec)

    def time_sim_specline_noise_pol_1(self):
        """ Check fitting of continuum as polynomial order 1. Gaussian noise included"""
        uvcontsub(vis=self.ms_cont_noise_order_1, outputvis=self.output,
                        fitorder=1, fitspec=self.fitspec)
