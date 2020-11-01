

.. _Description:

Description
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
      
   
   Since the MS stores only one copy of the flags (in the *FLAG*
   column), saving flags prior to **applycal** is often desirable.
   Use *flagbackup=True* for this. The pre-applycal flags will be
   stored in a separate CASA table named for the MS, with a
   '.flagversions' suffix. See the **flagmanager** task to recover
   old flag versions and otherwise manage the flag information.
   

.. _Examples:

Examples
   Often, it is desirable to calibrate calibrators and science
   targets in separate runs of **applycal**, perhaps with different
   interpolation parameters. First we calibrate the calibrators
   (fields 0 and 1) using gainfield='nearest' for the gain caltable
   to ensure that each calibrator will be calibrated by solutions
   obtained from itself. (The bandpass calibration is typically
   solved from one field but applied to all fields.):
   
   ::
   
      applycal(vis='n5921.ms',
               field='0,1',                             # calibrators
               spw='',                                  # all channels
               gaintable=['n5921.gcal','n5921.bcal']    # gain and bandpass tables
               gainfield=['nearest',''],                # nearest on sky for gcal
               interp=['nearest','nearest,linear'],     # nearest in time for gcal
               calwt=True)                              # calibrate the weights
   
   Next, calibrate the science target with explicit gainfield
   selection for the gain caltable, and linear interpolation in time:
   
   ::
   
      applycal(vis='n5921.ms',
               field='2',                               # science field
               spw='',                                  # all channels
               gaintable=['n5921.gcal','n5921.bcal']    # gain and bandpass tables
               gainfield=['1',''],                      # field 1 calibrates field 2 for gcal table
               interp=['linear','nearest,linear'],      # linear in time for gcal
               calwt=True)                              # calibrate the weights


.. _Development:

Development
   None
