import contextlib
import os
import re
import shutil
import unittest
import numpy
from casatools import ctsys, table
from casatasks import sdcal, initweights
from casatasks.private.sdutil import table_manager, table_selector

# ASV iteration control (https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-attributes)
number = 1            # i.e., always run the setup and teardown methods
repeat = (1, 2, 30.0) # between 1 and 2 iterations per round w/ soft cutoff (start no new repeats) past 1m
rounds = 3            # amount of instances a "repeat block" is run to collect samples
min_run_count = 5     # enforce the min_repeat * rounds setting is met
timeout = 3600        # conservative 1hr hard cap for duration of a single test execution

# Data path of input
datapath = ctsys.resolve('unittest/sdcal/')

class Apply():
    """
    Runtime benchmark tests for task sdcal
    """
    # Input and output data
    infile = 'uid___A002_X6218fb_X264.ms.sel'
    tsystable = 'tsystable'

    def setup(self):
        shutil.copytree(os.path.join(datapath, self.infile), self.infile)
        # Create TSYS table
        sdcal(infile=self.infile, calmode='tsys', outfile=self.tsystable)
        # Run initweights on input MS
        initweights(vis=self.infile, wtmode='nyq', dowtsp=True)

    def teardown(self):
        shutil.rmtree(self.infile, ignore_errors=True)
        shutil.rmtree(self.tsystable, ignore_errors=True)

    def time_spwmap_dict(self):
        """Test01: weight = 1/(SIGMA**2) X 1/(FPARAM_ave**2) dictionary version."""
        # Not sure what name is given to outfile in this run. Check!!
        spwmap_dict = {1: [1], 3: [3], 5: [5], 7: [7]}
        sdcal(infile=self.infile, calmode='apply', spwmap=spwmap_dict,
              applytable=self.tsystable, outfile='')

    def time_spwmap_list(self):
        """Test02: weight = 1/(SIGMA**2) X 1/(FPARAM_ave**2) list version."""
        # focus on antenna1=0, data_disk_id=1
        spwmap_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        sdcal(infile=self.infile, calmode='apply', spwmap=spwmap_list,
              applytable=self.tsystable, outfile='')

    def time_spwmap_dict_correct_data(self):
        """Test03: Validation of CORRECTED_DATA = DATA X FPARAM (spwmap={1:[1], 3:[3], 5:[5], 7:[7]})."""
        spwmap = {1: [1], 3: [3], 5: [5], 7: [7]}
        sdcal(infile=self.infile, calmode='apply', spwmap=spwmap, applytable=self.tsystable)

    def time_test05(self):
        """Test05: Validation of CORRECTED_DATA = DATA X FPARAM.
        (spwmap={1:[9], 3:[11], 5:[13], 7:[15]})
        antanna1=0, DATA_DISC_ID=9, FPARAM_average
        """
        spwmap = {1: [9], 3: [11], 5: [13], 7: [15]}
        sdcal(infile=self.infile, calmode='apply', spwmap=spwmap, applytable=self.tsystable)

    def time_spwmap_dict_weight_spectrum(self):
        """Test06: weight_spectrum = 1/(SIGMA**2) X 1/(FPARAMx**2) dictionary version."""
        spwmap_dict = {1: [1], 3: [3], 5: [5], 7: [7]}
        sdcal(infile=self.infile, calmode='apply', spwmap=spwmap_dict,
              applytable=self.tsystable, interp='nearest', outfile='')


class PositionSwitch():
    """
    Runtime benchmark tests for task sdcal (position switch sky calibration).
    """
    # Input and output data
    infile = 'uid___A002_X6218fb_X264.ms.sel'
    applytable = infile + '.sky'

    def setup(self):
        shutil.copytree(os.path.join(datapath, self.infile), self.infile)

    def teardown(self):
        if (os.path.exists(self.infile)):
            shutil.rmtree(self.infile)
        if os.path.exists(self.applytable):
            shutil.rmtree(self.applytable)

    def time_ps_basic(self):
        """test_ps05 --- position switch calibration ('ps')."""
        sdcal(infile=self.infile, calmode='ps', outfile=self.applytable)

    def time_ps_selection(self):
        """test_ps06 --- position switch calibration ('ps') with data selection."""
        sdcal(infile=self.infile, calmode='ps', spw='9', outfile=self.applytable)


class OTFRaster():
    """Runtime benchmark tests for task sdcal (OTF raster sky calibration).
    """
    # Input and output data
    infile = 'uid___A002_X6218fb_X264.ms.sel.otfraster'
    outfile = 'uid___A002_X6218fb_X264.ms.sel.sky'

    def setup(self):
        shutil.copytree(os.path.join(datapath, self.infile), self.infile)

    def teardown(self):
        shutil.rmtree(self.infile, ignore_errors=True)
        shutil.rmtree(self.outfile, ignore_errors=True)

    def time_default(self):
        """test_otfraster07 --- OTF raster calibration ('otfraster') with default setting."""
        sdcal(infile=self.infile, outfile=self.outfile, calmode='otfraster')

    def time_fraction_string_numeric(self):
        """test_otfraster08 --- OTF raster calibration ('otfraster') with string fraction (numeric value)."""
        sdcal(infile=self.infile, outfile=self.outfile, calmode='otfraster', fraction='0.3')

    def time_fraction_string_percentage(self):
        """test_otfraster09 --- OTF raster calibration ('otfraster') with string fraction (percentage)."""
        sdcal(infile=self.infile, outfile=self.outfile, calmode='otfraster', fraction='30%')

    def time_fraction_numeric(self):
        """test_otfraster10 --- OTF raster calibration ('otfraster') with numeric fraction."""
        sdcal(infile=self.infile, outfile=self.outfile, calmode='otfraster', fraction=0.3)

    def time_autodetection(self):
        """test_otfraster11 --- OTF raster calibration ('otfraster') with auto detection."""
        sdcal(infile=self.infile, outfile=self.outfile,
                            calmode='otfraster', fraction=0, noff=0)

    def time_noff_custom(self):
        """test_otfraster12 --- OTF raster calibration ('otfraster') with custom noff."""
        sdcal(infile=self.infile, outfile=self.outfile, calmode='otfraster', noff=3)

    def time_noff_priority_over_fraction(self):
        """test_otfraster13 --- check if noff takes priority over fraction."""
        sdcal(infile=self.infile, outfile=self.outfile, calmode='otfraster', fraction='90%', noff=3)


class OTF():
    """Runtime benchmark tests for task sdcal sky calibration mode = 'otf' : On-The-Fly (OTF) *non-raster*
    """
    # Input data
    infile_squares = 'squares.dec60_cs.ms'
    infile_lissajous = 'lissajous.ms'
    infiles = [infile_squares, infile_lissajous]
    ref_datapath = os.path.join(datapath, 'otf_reference_data')
    applytable = 'lissajous.edges_new_fraction_0.1.ms_caltable'

    # Output data
    outfile = 'test_otf.caltable'

    def setup(self):
        for infile in self.infiles:
            shutil.copytree(os.path.join(datapath, infile), infile)
        shutil.copytree(os.path.join(self.ref_datapath, self.applytable), self.applytable)

    def teardown(self):
        for infile in self.infiles:
            shutil.rmtree(infile, ignore_errors=True)
        shutil.rmtree(self.outfile, ignore_errors=True)
        shutil.rmtree(self.applytable, ignore_errors=True)

    def time_otf01(self):
        """test_otf01 --- Compute calibration table. calmode='otf' ms=squares.dec60_cs.ms."""
        sdcal(infile=self.infile_squares, calmode='otf', fraction='10%', noff=-1, width=0.5, elongated=False,
              applytable='', interp='', spwmap={}, outfile=self.outfile, overwrite=False, field='', spw='')

    def time_otf02(self):
        """test_otf02 --- Compute calibration table. calmode='otf' ms=squares.dec60_cs.ms edges_fraction=20%."""
        sdcal(infile=self.infile_squares, calmode='otf', fraction=0.2, noff=-1, width=0.5, elongated=False,
              applytable='', interp='', spwmap={}, outfile=self.outfile, overwrite=False, field='', spw='')

    def time_otf03(self):
        """test_otf03 --- Compute calibration table. calmode='otf' ms=lissajous.ms."""
        sdcal(infile=self.infile_lissajous, calmode='otf', fraction='10%', noff=-1, width=0.5,
              elongated=False, applytable='',interp='', spwmap={}, outfile=self.outfile, overwrite=False)

    def time_otf04(self):
        """test_otf04 --- Compute calibration table. calmode='otf' ms=lissajous.ms edges_fraction=20%."""
        sdcal(infile=self.infile_lissajous, calmode='otf', fraction='20%', noff=-1, width=0.5, elongated=False,
              applytable='',interp='', spwmap={}, outfile=self.outfile, overwrite=False, field='')

    # To be checked
    def time_otf05(self):
        """test_otf05 --- Sky calibration. calmode='otf,apply' ms=squares.dec60_cs.ms."""
        # In the original test it runs sdcal() twice, first with calmode=apply and then with otf,apply
        sdcal(infile=self.infile_squares, calmode='otf,apply', fraction='10%', noff=-1, width=0.5,
              elongated=False, applytable='', interp='', spwmap={}, outfile='', overwrite=False)

    def time_otf06(self):
        """test_otf06 --- Sky calibration reusing caltable pre-computed with calmode='otf'. calmode='apply' ms=lissajous.ms."""
        sdcal(infile=self.infile_lissajous, calmode='apply', fraction='10%', noff=-1, width=0.5,
              elongated=False, applytable=self.applytable, interp='', spwmap={}, outfile='', overwrite=False)

    def time_otf07(self):
        """test_otf07 --- Sky calibration + Tsys conversion, composite calmode='otf,tsys,apply'. ms=lissajous.ms."""
        sdcal(infile=self.infile_lissajous, calmode='otf,tsys,apply', fraction='10%', noff=-1, width=0.5, elongated=False,
              applytable='', interp='', spwmap={}, outfile='', overwrite=False, field='', spw='', scan='', intent='')


class OTF_Ephemeris():
    """Runtime benchmark tests for task sdcal, sky calibration mode = 'otf' : On-The-Fly (OTF) *non-raster*
        test cases for ephemeris objects
    """
    # Input data
    infile = 'otf_ephem.ms'

    # Output data
    outfile = infile + '.otfcal'

    def setup(self):
        shutil.copytree(os.path.join(datapath, self.infile), self.infile)

    def teardown(self):
        shutil.rmtree(self.infile, ignore_errors=True)
        shutil.rmtree(self.outfile, ignore_errors=True)

    def time_otf_ephem(self):
        """test_otfephem01: Sky calibration of 'otf' mode for ephemeris object."""
        sdcal(infile=self.infile, outfile=self.outfile, calmode='otf')

    def test_otf_apply_ephem(self):
        """test_otfephem02: On-the-fly application of 'otf' calibration mode for ephemeris object."""
        sdcal(infile=self.infile, calmode='otf,apply')

class Apply_Interp():
    """
    Unit test for task sdcal (apply tables).

    The list of tests:
    test_apply_sky00 --- empty applytable
    test_apply_sky01 --- empty applytable (list ver.)
    test_apply_sky02 --- empty applytable list
    test_apply_sky03 --- unexisting applytable
    test_apply_sky04 --- unexisting applytable (list ver.)
    test_apply_sky05 --- invalid selection (empty selection result)
    test_apply_sky06 --- invalid interp value
    test_apply_sky07 --- invalid applytable (not caltable)
    test_apply_sky08 --- apply data (linear)
    test_apply_sky09 --- apply selected data
    test_apply_sky10 --- apply data (nearest)
    test_apply_sky11 --- apply data (linearflag for frequency interpolation)
    test_apply_sky12 --- apply data (nearestflag for frequency interpolation)
    test_apply_sky13 --- apply data (string applytable input)
    test_apply_sky14 --- apply data (interp='')
    test_apply_sky15 --- check if WEIGHT_SPECTRUM is updated properly when it exists
    test_apply_sky16 --- apply both sky table and Tsys table simultaneously
    test_apply_composite00 --- on-the-fly application of sky table ('ps,apply')
    test_apply_composite01 --- on-the-fly application of sky table with existing Tsys table
    test_apply_composite02 --- on-the-fly application of sky and tsys tables ('ps,tsys,apply')
    test_apply_composite03 --- on-the-fly application of sky table ('otfraster,apply')
    """
    # Input
    infile = 'uid___A002_X6218fb_X264.ms.sel'
    applytable = infile + '.sky'

    def setup(self):
        shutil.copytree(os.path.join(datapath, self.infile), self.infile)
        shutil.copytree(os.path.join(datapath, self.applytable), self.applytable)

    def teardown(self):
        shutil.rmtree(self.infile, ignore_errors=True)
        shutil.rmtree(self.applytable, ignore_errors=True)

    def time_linear(self):
        """test_apply_sky08 --- apply data (linear)."""
        sdcal(infile=self.infile, calmode='apply',applytable=[self.applytable], interp='linear')

    def time_linear_spw_selection(self):
        """test_apply_sky09 --- apply selected data."""
        self.result = sdcal(infile=self.infile, calmode='apply', applytable=[
                            self.applytable], spw='9', interp='linear')

    def time_nearest(self):
        """test_apply_sky10 --- apply data (nearest)."""
        self.result = sdcal(infile=self.infile, calmode='apply',
                            applytable=[self.applytable], interp='nearest')

    def time_linear_linearflag(self):
        """test_apply_sky11 --- apply data (linearflag for frequency interpolation)."""
        sdcal(infile=self.infile, calmode='apply', applytable=[
                            self.applytable], interp='linear,linearflag')

    def time_linear_nearestflag(self):
        """test_apply_sky12 --- apply data (nearestflag for frequency interpolation)."""
        sdcal(infile=self.infile, calmode='apply', applytable=[
                            self.applytable], interp='linear,nearestflag')

    def time_interp_empty(self):
        """test_apply_sky14 --- apply data (interp='')."""
        self.result = sdcal(infile=self.infile, calmode='apply',
                            applytable=self.applytable, interp='')

    def fill_weightspectrum(func):
        import functools

        @functools.wraps(func)
        def wrapper(self):
            with table_manager(self.infile, nomodify=False) as tb:
                self.assertTrue('WEIGHT_SPECTRUM' in tb.colnames(), msg='Internal Error')
                nrow = tb.nrows()
                for irow in range(nrow):
                    w = tb.getcell('WEIGHT', irow)
                    wsp = numpy.ones(tb.getcell('DATA', irow).shape, dtype=float)
                    for ipol in range(len(w)):
                        wsp[ipol, :] = w[ipol]
                    tb.putcell('WEIGHT_SPECTRUM', irow, wsp)
                    self.assertTrue(tb.iscelldefined('WEIGHT_SPECTRUM', irow), msg='Internal Error')
            func(self)
        return wrapper


# New class for special cases from class Apply_Interp
class Apply_Modified_Tsys():
    """
    Runtime benchmark tests for sdcal ....
    """
    # Input
    infile = 'uid___A002_X6218fb_X264.ms.sel'
    applytable = infile + '.sky'
    tsystable = 'tsystable'

    def setup(self):
        shutil.copytree(os.path.join(datapath, self.infile), self.infile)
        shutil.copytree(os.path.join(datapath, self.applytable), self.applytable)
        # generate Tsys table
        self.tsystable = self.infile.rstrip('/') + '.tsys'
        try:
            # generate Tsys table
            sdcal(infile=self.infile, calmode='tsys', outfile=self.tsystable)
        except:
            print("Error generating tsys table")
            

    def teardown(self):
        shutil.rmtree(self.infile, ignore_errors=True)
        shutil.rmtree(self.applytable, ignore_errors=True)
        if os.path.exists(self.tsystable):
            shutil.rmtree(self.tsystable, ignore_errors=True)

    def _modify_tsys(self, mytsys=100.0):
        with table_manager(self.infile, nomodify=False) as tb:
            tsel = tb.query('SPECTRAL_WINDOW_ID IN [1,3]',
                            sortlist='ANTENNA_ID,SPECTRAL_WINDOW_ID,TIME')
            try:
                nrow = tsel.nrows()
                tsys = mytsys
                for irow in range(nrow):
                    tsys_spectrum = tsel.getcell('TSYS_SPECTRUM', irow)
                    tsys_spectrum[:] = tsys
                    tsel.putcell('TSYS_SPECTRUM', irow, tsys_spectrum)
                    # tsys += 100.0
            finally:
                tsel.close()


    # TBD
    # @fill_weightspectrum
    # @normal_case(interp='linear')
    # def test_apply_sky15(self):
    #     """test_apply_sky15 --- check if WEIGHT_SPECTRUM is updated properly when it exists."""
    #     self.result = sdcal(infile=self.infile, calmode='apply',
    #                         applytable=self.applytable, interp='linear')

    def modify_tsys(func):
        import functools

        @functools.wraps(func)
        def wrapper(self):
            with table_manager(os.path.join(self.infile, 'SYSCAL'), nomodify=False) as tb:
                tsel = tb.query('SPECTRAL_WINDOW_ID IN [1,3]',
                                sortlist='ANTENNA_ID,SPECTRAL_WINDOW_ID,TIME')
                try:
                    nrow = tsel.nrows()
                    tsys = 100.0
                    for irow in range(nrow):
                        tsys_spectrum = tsel.getcell('TSYS_SPECTRUM', irow)
                        tsys_spectrum[:] = tsys
                        tsel.putcell('TSYS_SPECTRUM', irow, tsys_spectrum)
                        # tsys += 100.0
                finally:
                    tsel.close()
            func(self)
        return wrapper

    #@normal_case()
    def time_apply_sky_normal(self):
        """test_apply_composite00 --- on-the-fly application of sky table ('ps,apply')."""
        sdcal(infile=self.infile, calmode='ps,apply')

    @modify_tsys
    #@normal_case(tsys=100.0)
    def time_preapply_tsys(self):
        """test_apply_composite01 --- on-the-fly application of sky table with existing Tsys table."""
        sdcal(infile=self.infile, calmode='ps,apply', applytable=self.tsystable,
              spwmap={1: [9], 3: [11]})

    @modify_tsys
    #@normal_case(tsys=100.0)
    def time_apply_sky_tsys(self):
        """test_apply_composite02 --- on-the-fly application of sky and tsys tables ('ps,tsys,apply')."""
        sdcal(infile=self.infile, calmode='ps,tsys,apply',
              spwmap={1: [9], 3: [11]})

    @modify_tsys
    #@normal_case(tsys=100.0)
    def time_apply_sky(self):
        """test_apply_composite03 --- on-the-fly application of sky table ('otfraster,apply')."""
        sdcal(infile=self.infile, calmode='tsys,apply', applytable=self.applytable,
              spwmap={1: [9], 3: [11]})


class sdcal_test_single_polarization():
    """Unit test for task sdcal (calibration/application of single-polarization data).

    The list of tests:
    test_single_pol_ps --- generate caltable for single-polarization data
    test_single_pol_apply --- apply caltable to single-polarization data
    test_single_pol_apply_composite --- on-the-fly calibration/application
                                        on single-polarization data
    """

    datapath = ctsys.resolve('unittest/sdcal/')
    # Input
    infile = 'analytic_spectra.ms'
    outfile = 'sdcalout.cal'

    def setUp(self):
        shutil.copytree(os.path.join(datapath, self.infile), self.infile)

    def tearDown(self):
        shutil.rmtree(self.infile, ignore_errors=True)
        shutil.rmtree(self.outfile, ignore_errors=True)

    def time_single_pol_ps(self):
        """test_single_pol_ps --- generate caltable for single-polarization data."""
        sdcal(infile=self.infile, calmode='ps', outfile=self.outfile)

    def time_single_pol_apply(self):
        """test_single_pol_apply --- apply caltable to single-polarization data."""
        # Generate ouput file for apply case
        sdcal(infile=self.infile, calmode='ps', outfile=self.outfile)
        sdcal(infile=self.infile, calmode='apply', applytable=self.outfile)

    def time_single_pol_apply_composite(self):
        """test_single_pol_apply_composite --- on-the-fly calibration/application on single-polarization data."""
        sdcal(infile=self.infile, calmode='ps,apply')
