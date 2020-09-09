#
# stub function definition file for docstring parsing
#

def applycal(vis, field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[''], calwt=[True], parang=False, applymode='', flagbackup=True):
    r"""
Apply calibrations solutions(s) to data

Parameters
   - vis_ (string) - Name of input visibility file
   - field_ (string='') - Select field using field id(s) or field name(s)
   - spw_ (string='') - Select spectral window/channels
   - intent_ (string='') - Select observing intent
   - selectdata_ (bool=True) - Other data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - timerange_ (string='') - Select data based on time range
      - uvrange_ (variant='') - Select data within uvrange (default units meters)
      - antenna_ (string='') - Select data based on antenna/baseline
      - scan_ (string='') - Scan number range
      - observation_ ({string, int}='') - Select by observation ID(s)
      - msselect_ (string='') - Optional complex data selection (ignore for now)

      .. raw:: html

         </details>
   - docallib_ (bool=False) - Use callib or traditional cal apply parameters

      .. raw:: html

         <details><summary><i> docallib = False </i></summary>

      - gaintable_ (stringArray=['']) - Gain calibration table(s) to apply on the fly
      - gainfield_ (stringArray=['']) - Select a subset of calibrators from gaintable(s)
      - interp_ (stringArray=['']) - Interpolation parameters for each gaintable, as a list
      - spwmap_ (intArray=['']) - Spectral windows combinations to form for gaintables(s)
      - calwt_ (boolArray=[True]) - Calibrate data weights per gaintable.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> docallib = True </i></summary>

      - callib_ (string='') - Cal Library filename

      .. raw:: html

         </details>
   - parang_ (bool=False) - Apply parallactic angle correction
   - applymode_ (string='') - Calibration mode: ""="calflag","calflagstrict","trial","flagonly","flagonlystrict", or "calonly"
   - flagbackup_ (bool=True) - Automatically back up the state of flags before the run?


Description
   .. rubric:: Summary
      

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


.. _vis:

vis (string)
   | Name of input visibility file
   |                      default: non
   | 
   |                         Example: vis='ngc5921.ms'

.. _field:

field (string='')
   | Select field using field id(s) or field name(s)
   |                      default: '' --> all fields
   |                      
   |                      Use 'go listobs' to obtain the list id's or
   |                      names. If field string is a non-negative integer,
   |                      it is assumed a field index,  otherwise, it is
   |                      assumed a field name.
   | 
   |                         Examples:
   |                         field='0~2'; field ids 0,1,2
   |                         field='0,4,5~7'; field ids 0,4,5,6,7
   |                         field='3C286,3C295'; field named 3C286 and
   |                         3C295
   |                         field = '3,4C*'; field id 3, all names
   |                         starting with 4C

.. _spw:

spw (string='')
   | Select spectral window/channels
   | 
   |                         Examples:
   |                         spw='0~2,4'; spectral windows 0,1,2,4 (all
   |                         channels)
   |                         spw='<2';  spectral windows less than 2
   |                         (i.e. 0,1)
   |                         spw='0:5~61'; spw 0, channels 5 to 61,
   |                         INCLUSIVE
   |                         spw='*:5~61'; all spw with channels 5 to 61
   |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
   |                         3, channels 3 to 45.
   |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
   |                         through 6 in each.
   |                         spw='0:0~10;15~60'; spectral window 0 with
   |                         channels 0-10,15-60. (NOTE ';' to separate
   |                         channel selections)
   |                         spw='0:0~10^2,1:20~30^5'; spw 0, channels
   |                         0,2,4,6,8,10, spw 1, channels 20,25,30 
   |                         type 'help par.selection' for more examples.

.. _intent:

intent (string='')
   | Select observing intent
   |                      default: '' (no selection by intent)
   | 
   |                         Example: intent='*BANDPASS*'  (selects data
   |                         labelled with BANDPASS intent)

.. _selectdata:

selectdata (bool=True)
   | Other data selection parameters
   |                      default: True

.. _timerange:

timerange (string='')
   | Select data based on time range
   |                      Subparameter of selectdata=True
   |                      default = '' (all)
   | 
   |                         Examples:
   |                         timerange =
   |                         'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   |                         (Note: if YYYY/MM/DD is missing date defaults
   |                         to first day in data set.)
   |                         timerange='09:14:0~09:54:0' picks 40 min on
   |                         first day 
   |                         timerange= '25:00:00~27:30:00' picks 1 hr to 3
   |                         hr 30min on NEXT day
   |                         timerange='09:44:00' pick data within one
   |                         integration of time
   |                         timerange='>10:24:00' data after this time

.. _uvrange:

uvrange (variant='')
   | Select data within uvrange (default units meters)
   |                      Subparameter of selectdata=True
   |                      default: '' (all)
   | 
   |                         Examples:
   |                         uvrange='0~1000klambda'; uvrange from 0-1000
   |                         kilo-lambda
   |                         uvrange='>4klambda';uvranges greater than 4
   |                         kilolambda

.. _antenna:

antenna (string='')
   | Select data based on antenna/baseline
   |                      Subparameter of selectdata=True
   |                      default: '' (all)
   | 
   |                      If antenna string is a non-negative integer, it
   |                      is assumed an antenna index, otherwise, it is
   |                      assumed as an antenna name
   |   
   |                          Examples: 
   |                          antenna='5&6'; baseline between antenna
   |                          index 5 and index 6.
   |                          antenna='VA05&VA06'; baseline between VLA
   |                          antenna 5 and 6.
   |                          antenna='5&6;7&8'; baselines with
   |                          indices 5-6 and 7-8
   |                          antenna='5'; all baselines with antenna index
   |                          5
   |                          antenna='05'; all baselines with antenna
   |                          number 05 (VLA old name)
   |                          antenna='5,6,10'; all baselines with antennas
   |                          5,6,10 index numbers

.. _scan:

scan (string='')
   | Scan number range
   |                      Subparameter of selectdata=True
   |                      default: '' = all

.. _observation:

observation ({string, int}='')
   | Select by observation ID(s)
   |                      Subparameter of selectdata=True
   |                      default: '' = all
   | 
   |                          Example: observation='0~2,4'

.. _msselect:

msselect (string='')
   | Optional complex data selection (ignore for now)

.. _docallib:

docallib (bool=False)
   | Control means of specifying the caltables
   |                      default: False --> Use gaintable, gainfield,
   |                      interp, spwmap, calwt. 
   | 
   |                      If True, specify a file containing cal library in
   |                      callib

.. _callib:

callib (string='')
   | Cal Library filename
   |                      Subparameter of callib=True
   | 
   |                      If docallib=True, specify a file containing cal
   |                      library directives

.. _gaintable:

gaintable (stringArray=[''])
   | Gain calibration table(s) to apply on the fly
   |                      Subparameter of callib=False
   |                      default: '' (none)
   | 
   |                      All gain table types: 'G', GSPLINE, 'T', 'B',
   |                      'BPOLY', 'D's' can be applied.
   | 
   |                         Examples: gaintable='ngc5921.gcal'
   |                         gaintable=['ngc5921.ampcal','ngc5921.phcal']

.. _gainfield:

gainfield (stringArray=[''])
   | Select a subset of calibrators from gaintable(s)
   |                      Subparameter of callib=False
   |                      default:'' --> all sources in table
   |                      
   |                      gaintable='nearest' --> nearest (on sky)
   |                      available field in table. Otherwise, same syntax
   |                      as field
   | 
   |                         Examples: 
   |                         gainfield='0~2,5' means use fields 0,1,2,5
   |                         from gaintable
   |                         gainfield=['0~3','4~6'] (for multiple
   |                         gaintables)

.. _interp:

interp (stringArray=[''])
   | Interpolation parmameters (in time[,freq]) for each gaintable, as a list of strings.
   |                      Default: '' --> 'linear,linear' for all gaintable(s)
   |                      Options: Time: 'nearest', 'linear'
   |                               Freq: 'nearest', 'linear', 'cubic',
   |                               'spline'
   |                    Specify a list of strings, aligned with the list of caltable specified
   |                    in gaintable, that contain the required interpolation parameters
   |                    for each caltable.
   |                    * When frequency interpolation is relevant (B, Df,
   |                      Xf), separate time-dependent and freq-dependent
   |                      interp types with a comma (freq_after_ the
   |                      comma). 
   |                    * Specifications for frequency are ignored when the
   |                      calibration table has no channel-dependence. 
   |                    * Time-dependent interp options ending in 'PD'
   |                      enable a "phase delay" correction per spw for
   |                      non-channel-dependent calibration types.
   |                    * For multi-obsId datasets, 'perobs' can be
   |                      appended to the time-dependent interpolation
   |                      specification to enforce obsId boundaries when
   |                      interpolating in time. 
   |                    * Freq-dependent interp options can have 'flag' appended
   |                      to enforce channel-dependent flagging, and/or 'rel' 
   |                      appended to invoke relative frequency interpolation
   | 
   |                         Examples: 
   |                         interp='nearest' (in time, freq-dep will be
   |                         linear, if relevant)
   |                         interp='linear,cubic'  (linear in time, cubic
   |                         in freq)
   |                         interp='linearperobs,splineflag' (linear in
   |                         time per obsId, spline in freq with
   |                         channelized flagging)
   |                         interp='nearest,linearflagrel' (nearest in
   |                         time, linear in freq with with channelized 
   |                         flagging and relative-frequency interpolation)
   |                         interp=',spline'  (spline in freq; linear in
   |                         time by default)
   |                         interp=['nearest,spline','linear']  (for
   |                         multiple gaintables)

.. _spwmap:

spwmap (intArray=[''])
   | Spectral windows combinations to form for gaintables(s)
   |                      Subparameter of callib=False
   |                      default: [] (apply solutions from each spw to
   |                      that spw only)
   | 
   |                         Examples:
   |                         spwmap=[0,0,1,1] means apply the caltable
   |                         solutions from spw = 0 to the spw 0,1 and spw
   |                         1 to spw 2,3.
   |                         spwmap=[[0,0,1,1],[0,1,0,1]] (for multiple
   |                         gaintables)

.. _calwt:

calwt (boolArray=[True])
   | Calibrate data weights per gaintable.
   |                      default: True (for all specified gaintables)
   |  
   |                         Examples:
   |                         calwt=False (for all specified gaintables)
   |                         calwt=[True,False,True] (specified per
   |                         gaintable)

.. _parang:

parang (bool=False)
   | Apply parallactic angle correction
   |                      default: False
   | 
   |                      If True, apply the parallactic angle
   |                      correction. FOR ANY POLARIZATION CALIBRATION AND
   |                      IMAGING, parang = True

.. _applymode:

applymode (string='')
   | Calibration apply mode
   |                      default: 'calflag' 
   |                      Options: "calflag", "calflagstrict", "trial",
   |                      "flagonly", "flagonlystrict", "calonly"
   | 
   |                      -- applymode='calflag': calibrate data and apply
   |                      flags from solutions
   |                      -- applymode='trial': report on flags from
   |                      solutions, dataset entirely unchanged
   |                      -- applymode='flagonly': apply flags from
   |                      solutions only, data not calibrated
   |                      -- applymode='calonly' calibrate data only, flags
   |                      from solutions NOT applied (use with extreme
   |                      caution!)
   |                      -- applymode='calflagstrict' or 'flagonlystrict'
   |                      same as above except flag spws for which
   |                      calibration is unavailable in one or more tables
   |                      (instead of allowing them to pass uncalibrated
   |                      and unflagged)

.. _flagbackup:

flagbackup (bool=True)
   | Automatically back up the state of flags before the run?
   |                      default: True


    """
    pass
