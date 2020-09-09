#
# stub function definition file for docstring parsing
#

def accum(vis, tablein='', incrtable='', caltable='', field=[''], calfield=[''], interp='linear', accumtime=1.0, spwmap=[-1]):
    r"""
Accumulate incremental calibration solutions into a calibration table (NB: ACCUM WILL BE REMOVED IN CASA 5.8/6.2)

Parameters
   - vis_ (string) - Name of input visibility file
   - tablein_ (string='') - Input cumulative calibration table; use \'\' on first run

      .. raw:: html

         <details><summary><i> tablein = '' </i></summary>

      - accumtime_ ({double, int}=1.0) - Time-interval when create cumulative table

      .. raw:: html

         </details>
   - incrtable_ (string='') - Input incremental calibration table to add
   - caltable_ (string='') - Output (cumulative) calibration table
   - field_ (stringArray=[''])
   - calfield_ (stringArray=['']) - List of field names to use from incrtable.
   - interp_ (string='linear') - Interpolation mode to use for resampling incrtable solutions
   - spwmap_ (intArray=[-1]) - Spectral window combinations to apply


Description
   .. rubric:: Summary
      

   .. warning:: Please note: The **accum** task has been designated for
      deprecation, and will be removed in CASA 5.8/6.2.

   

   **accum** will interpolate and extrapolate a temporal calibration
   table onto a new table that has a regularly-space time grid. The
   first run of **accum** defines the time grid and fills this table
   with the results from the input table. Subsequent use of **accum**
   will combine additional calibration tables onto the same grid of
   the initial **accum** table to obtain an output **accum** table.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input MeasurementSet. No default.

   .. rubric:: *tablein*
      

   Input cumulative calibration table. Default: ''** means none. On
   first execution of **accum**, *tablein=''* and *accumtime* is
   used to generate *tablein* withthe specified time gridding.

   .. rubric:: *tablein* expandable parameters
      

   .. rubric:: *accumtime*
      

   The time separation when making *tablein*. Default: 1.0 ** (1
   second).This time should not beless than the visibiility
   sampling time, but shouldbe less than about 30% of a typical scan
   length.

   

   .. rubric:: *incrtable*
      

   The calibration data to be interpolated onto the*tablein* file.
   Default: ''. Must be specified.

   .. rubric:: *caltable*
      

   The output cumulative calibration file. Default: '' means use
   *tablein* as the output file.

   .. rubric:: *field*
      

   Standard field ID or name selection for *tablein* to process.
   Default: '' = all fields. (See `Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__for
   more details.)

   .. rubric:: *calfield*
      

   Select field(s) from *incrtable* to process. Default: '' = all
   fields. (See`Data Selection in a
   MeasurementSet <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__for
   more details.)

   .. rubric:: *interp*
      

   Interpolation type (in time,freq) to use for each gaintable.When
   frequency interpolation is relevant (B, Df, Xf),separate
   time-dependent and freq-dependent *interp*types with a comma
   (freq*interp*type should be afterthe comma). Specifications for
   frequency are ignored when thecalibration table has no
   channel-dependence.Time-dependent interp options ending in 'PD'
   enable a"phase delay" correction per spw for
   non-channel-dependentcalibration types.For multi-obsId datasets,
   'perobs' can be appended to the time-dependent interpolation
   specification toenforce obs ID boundaries when interpolating in
   time. Options: Time - 'nearest'*,* 'linear'*;* Freq - 'nearest'*,*
   'linear'*,* 'cubic'*,* 'spline'*. D* efault: 'linear,linear' for
   all gaintable(s). See also: `Solving for
   Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__.

   .. rubric:: *spwmap*
      

   Spectral windows combinations to form gaintable(s). Default: [ ]
   (apply solutions from each spw to that spw only). See
   also:`Solving for
   Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__.


.. _vis:

vis (string)
   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _tablein:

tablein (string='')
   | Input cumulative calibration table
   |                      Default: '' (none)
   | 
   |                      On first execution of accum, tablein='' and
   |                      accumtime is used to generate tablein with the
   |                      specified time gridding.

.. _incrtable:

incrtable (string='')
   | The calibration data to be interpolated onto the tablein
   | file.
   |                      Default: '' (must be specified)

.. _caltable:

caltable (string='')
   | The output cumulative calibration table
   |                      Default: '' (use tablein as the output file)

.. _field:

field (stringArray=[''])
   | Select field using field id(s) or field name(s)
   |                      Default: '' --> all fields
   |                      
   |                      Use 'go listobs' to obtain the list id's or
   |                      names. If field string is a non-negative
   |                      integer, it is assumed a field index,
   |                      otherwise, it is assumed a field name.
   | 
   |                         Examples:
   |                         field='0~2'; field ids 0,1,2
   |                         field='0,4,5~7'; field ids 0,4,5,6,7
   |                         field='3C286,3C295'; field named 3C286 and
   |                         3C295
   |                         field = '3,4C*'; field id 3, all names
   |                         starting with 4C

.. _calfield:

calfield (stringArray=[''])
   | Select field(s) from incrtable to process.
   |                      Default: '' (all fields)

.. _interp:

interp (string='linear')
   | Interpolation type (in time[,freq]) to use for each
   | gaintable.
   |                      Default: '' ('linear,linear' for all gaintable(s))
   |                      Options: Time: 'nearest', 'linear'
   |                               Freq: 'nearest', 'linear', 'cubic',
   |                               'spline'
   | 
   |                    * When frequency interpolation is relevant (B, Df,
   |                      Xf), separate time-dependent and freq-dependent
   |                      interp types with a comma (freq _after_ the
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
   | 
   |                         Examples: 
   |                         interp='nearest' (in time, freq-dep will be
   |                         linear, if relevant)
   |                         interp='linear,cubic' (linear in time, cubic
   |                         in freq)
   |                         interp='linearperobs,spline' (linear in time
   |                         per obsId, spline in freq)
   |                         interp=',spline' (spline in freq; linear in
   |                         time by default)
   |                         interp=['nearest,spline','linear'] (for
   |                         multiple gaintables)

.. _accumtime:

accumtime ({double, int}=1.0)
   | The time separation when making tablein.
   |                      Subparameter of tablein
   |                      Default: 1.0  (1 second)
   | 
   |                      Note: This time should not be less than the
   |                      visibility sampling time, but should be less than
   |                      about 30% of a typical scan length.

.. _spwmap:

spwmap (intArray=[-1])
   | Spectral windows combinations to form for gaintable(s)
   |                      Default: [] (apply solutions from each spw to
   |                                   that spw only)
   | 
   |                         Examples: 
   |                         spwmap=[0,0,1,1] means apply the caltable
   |                         solutions from spw = 0 to the spw 0,1 
   |                         and spw 1 to spw 2,3.
   |                         spwmap=[[0,0,1,1],[0,1,0,1]] (for multiple
   |                         gaintables)


    """
    pass
