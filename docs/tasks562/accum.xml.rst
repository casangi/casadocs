accum -- Accumulate incremental calibration solutions into a calibration table -- calibration task
=======================================

Description
---------------------------------------

Accum will interpolate and extrapolate a calibration table onto a new
table that has a regularly-space time grid.

The first run of accum defines the time grid and fills this table with
the results from the input table.

Subsequent use of accum will combine additional calibration tables
onto the same grid of the initial accum table to obtain an output
accum table.  See below for concrete examples.

Accum tables are similar to CL tables in AIPS. Incremental tables are
similar to SN tables in AIPS.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input visibility file
   * - tablein
     - :code:`''`
     - Input cumulative calibration table; use \'\' on first run
   * - incrtable
     - :code:`''`
     - Input incremental calibration table to add
   * - caltable
     - :code:`''`
     - Output (cumulative) calibration table
   * - field
     - :code:`numpy.array( [  ] )`
     - 
   * - calfield
     - :code:`numpy.array( [  ] )`
     - List of field names to use from incrtable.
   * - interp
     - :code:`'linear'`
     - Interpolation mode to use for resampling incrtable solutions
   * - accumtime
     - :code:`float(1.0)`
     - Time-interval when create cumulative table
   * - spwmap
     - :code:`numpy.array( [  ] )`
     - Spectral window combinations to apply


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



tablein
---------------------------------------

:code:`''`

Input cumulative calibration table
                     Default: '' (none)

                     On first execution of accum, tablein='' and
                     accumtime is used to generate tablein with the
                     specified time gridding.



incrtable
---------------------------------------

:code:`''`

The calibration data to be interpolated onto the tablein
file.
                     Default: '' (must be specified)



caltable
---------------------------------------

:code:`''`

The output cumulative calibration table
                     Default: '' (use tablein as the output file)



field
---------------------------------------

:code:`numpy.array( [  ] )`

Select field using field id(s) or field name(s)
                     Default: '' --> all fields
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative
                     integer, it is assumed a field index,
                     otherwise, it is assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C



calfield
---------------------------------------

:code:`numpy.array( [  ] )`

Select field(s) from incrtable to process.
                     Default: '' (all fields)



interp
---------------------------------------

:code:`'linear'`

Interpolation type (in time[,freq]) to use for each
gaintable.
                     Default: '' ('linear,linear' for all gaintable(s))
                     Options: Time: 'nearest', 'linear'
                              Freq: 'nearest', 'linear', 'cubic',
                              'spline'

                   * When frequency interpolation is relevant (B, Df,
                     Xf), separate time-dependent and freq-dependent
                     interp types with a comma (freq _after_ the
                     comma). 
                   * Specifications for frequency are ignored when the
                     calibration table has no channel-dependence.
                   * Time-dependent interp options ending in 'PD'
                     enable a "phase delay" correction per spw for
                     non-channel-dependent calibration types.
                   * For multi-obsId datasets, 'perobs' can be
                     appended to the time-dependent interpolation
                     specification to enforce obsId boundaries when
                     interpolating in time.

                        Examples: 
                        interp='nearest' (in time, freq-dep will be
                        linear, if relevant)
                        interp='linear,cubic' (linear in time, cubic
                        in freq)
                        interp='linearperobs,spline' (linear in time
                        per obsId, spline in freq)
                        interp=',spline' (spline in freq; linear in
                        time by default)
                        interp=['nearest,spline','linear'] (for
                        multiple gaintables)



accumtime
---------------------------------------

:code:`float(1.0)`

The time separation when making tablein.
                     Subparameter of tablein
                     Default: 1.0  (1 second)

                     Note: This time should not be less than the
                     visibility sampling time, but should be less than
                     about 30% of a typical scan length.



spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintable(s)
                     Default: [] (apply solutions from each spw to
                                  that spw only)

                        Examples: 
                        spwmap=[0,0,1,1] means apply the caltable
                        solutions from spw = 0 to the spw 0,1 
                        and spw 1 to spw 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]] (for multiple
                        gaintables)





