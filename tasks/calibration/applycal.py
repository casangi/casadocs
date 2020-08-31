#
# stub function definition file for docstring parsing
#

def applycal(vis, field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[''], calwt=[True], parang=False, applymode='', flagbackup=True):
    r"""
Apply calibrations solutions(s) to data

Parameters
   - **vis** (string) - Name of input visibility file
   - **field** (string) - Select field using field id(s) or field name(s)
   - **spw** (string) - Select spectral window/channels
   - **intent** (string) - Select observing intent
   - **selectdata** (bool) - Other data selection parameters
   - **docallib** (bool) - Use callib or traditional cal apply parameters
   - **parang** (bool) - Apply parallactic angle correction
   - **applymode** (string) - Calibration mode: ""="calflag","calflagstrict","trial","flagonly","flagonlystrict", or "calonly"
   - **flagbackup** (bool) - Automatically back up the state of flags before the run?

Subparameters
   .. raw:: html

      <details><summary><i> selectdata = True </i></summary>

   - **timerange** (string='') - Select data based on time range
   - **uvrange** (variant='') - Select data within uvrange (default units meters)
   - **antenna** (string='') - Select data based on antenna/baseline
   - **scan** (string='') - Scan number range
   - **observation** (string='', int) - Select by observation ID(s)
   - **msselect** (string='') - Optional complex data selection (ignore for now)

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> docallib = False </i></summary>

   - **gaintable** (stringArray='') - Gain calibration table(s) to apply on the fly
   - **gainfield** (stringArray='') - Select a subset of calibrators from gaintable(s)
   - **interp** (stringArray='') - Interpolation parameters for each gaintable, as a list
   - **spwmap** (intArray='') - Spectral windows combinations to form for gaintables(s)
   - **calwt** (boolArray=True) - Calibrate data weights per gaintable.

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> docallib = True </i></summary>

   - **callib** (string='') - Cal Library filename

   .. raw:: html

      </details>


Description
      .. rubric:: Summary
         :name: summary

      The **applycal** task reads the specified gain calibration tables,
      applies them to the (raw) MS *DATA* column (with the specified
      selection), and writes the calibrated data into the
      *CORRECTED_DATA* column, where imaging or other analysis can find
      it for further processing. All supplied calibration is applied in
      one step, according to the `Measurement
      Equation <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-measurement-equation-calibration>`__.
      The existing contents of the *CORRECTED_DATA* (for the specified
      selection) will be overwritten.  

      The **applycal** task shares the input dataset ('vis'), data
      selection and (prior) calibration parameters with the solving
      tasks; detailed information about setting these parameters can be
      found the section on `"Solving for
      Calibration" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__.
      Several parameters unique to **applycal** are described below.

      In the traditional interface (*docallib=False*), all calibration
      tables (both temporal, frequency, polarization calibrations) are
      specified in the gaintable parameter. The calibration values
      associated with a restricted list of fields can also be selected
      for each table in gainfield. As of CASA v4.2, *docallib=True*
      provides specification of an ensemble of calibration tables and
      directives via a cal library file.

      After running **applycal**, the corrected data may be selected,
      partially (and optionally) averaged, and copied to a new MS using
      **mstransform** (formerly **split**). This may be desirable to
      reduce the size of the dataset for further processing, if
      circumstances (e.g., field-of-view) permit. Alternatively, the
      corrected data may be imaged directly from the original MS.

      Calibrated data may be examined in **plotms** and **visstat**.

       

      .. rubric:: Weight calibration: *calwt*
         :name: weight-calibration-calwt

      Unlike the solving tasks, calibration of the weights is optional
      in **applycal**, and is controlled using the *calwt* parameter. If
      *calwt=True*, the weights will be calibrated by all specified
      caltables that change the data's scale (phase-like caltables have
      no effect on the weights). The *calwt* parameter may also be
      specified as a list of Booleans, enabling control of which
      caltables calibrate the weights. In general, it is advisable to
      calibrate the weights, as this should ensure achieving the full
      natural sensitivity of the observation. Information about weight
      calibration conventions can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__.

      .. rubric:: Calibration application modes: *applymode*
         :name: calibration-application-modes-applymode

      The **applycal** task supports different modes of application via
      the *applymode* parameter:

      -  'calflag' will apply all flags from a calibration table to the
         MS and apply the calibration itself to the remaining
         visibilities (and weights, as per calwt). This is the default.
      -  'trial' will only report on the calibration table flags but not
         manipulate the data or weights.
      -  'flagonly' applies the flags but not the calibration itself,
         leaving the data and weights untouched.
      -  'calonly' will apply the calibration to data and weights, but
         leave the flags untouched.

      For the flag-aware options, if 'strict' is appended (e.g.,
      'calflagstrict' or 'flagonlystrict'), **applycal** will flag all
      selected data for spws that have no solutions available in any one
      of the caltables, instead of allowing the to pass uncorrected and
      unflagged. 

      .. rubric:: Flag control: *flagbackup*
         :name: flag-control-flagbackup

      Since the MS stores only one copy of the flags (in the *FLAG*
      column), saving flags prior to **applycal** is often desirable.
      Use *flagbackup=True* for this. The pre-applycal flags will be
      stored in a separate CASA table named for the MS, with a
      '.flagversions' suffix. See the **flagmanager** task to recover
      old flag versions and otherwise manage the flag information.

    """
    pass
