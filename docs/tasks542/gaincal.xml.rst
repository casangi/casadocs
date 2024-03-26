gaincal -- Determine temporal gains from calibrator observations -- calibration task
=======================================

Description
---------------------------------------

The complex gains for each antenna/spwid are determined from the
data column (raw data), divided by the model column, for the
specified fields.  The gains can be obtained for a
specified solution interval for each spectral window, or by a spline 
fit to all spectral windows simultaneously.

Previous calibrations (egs. bandpass) should be applied on the fly.




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
     - 
   * - caltable
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - selectdata
     - :code:`True`
     - 
   * - timerange
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - msselect
     - :code:`''`
     - 
   * - solint
     - :code:`'inf'`
     - 
   * - combine
     - :code:`''`
     - 
   * - preavg
     - :code:`float(-1.0)`
     - 
   * - refant
     - :code:`''`
     - 
   * - refantmode
     - :code:`'flex'`
     - 
   * - minblperant
     - :code:`int(4)`
     - 
   * - minsnr
     - :code:`float(3.0)`
     - 
   * - solnorm
     - :code:`False`
     - 
   * - normtype
     - :code:`'mean'`
     - 
   * - gaintype
     - :code:`'G'`
     - 
   * - smodel
     - :code:`numpy.array( [  ] )`
     - 
   * - calmode
     - :code:`'ap'`
     - 
   * - append
     - :code:`False`
     - 
   * - splinetime
     - :code:`float(3600.0)`
     - 
   * - npointaver
     - :code:`int(3)`
     - 
   * - phasewrap
     - :code:`float(180.0)`
     - 
   * - docallib
     - :code:`False`
     - 
   * - callib
     - :code:`''`
     - 
   * - gaintable
     - :code:`numpy.array( [  ] )`
     - 
   * - gainfield
     - :code:`numpy.array( [  ] )`
     - 
   * - interp
     - :code:`numpy.array( [  ] )`
     - 
   * - spwmap
     - :code:`numpy.array( [  ] )`
     - 
   * - parang
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


caltable
---------------------------------------

:code:`''`

Name of output gain calibration table


field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


intent
---------------------------------------

:code:`''`

Select observing intent


selectdata
---------------------------------------

:code:`True`

Other data selection parameters


timerange
---------------------------------------

:code:`''`

Select data based on time range


uvrange
---------------------------------------

:code:`''`

Select data within uvrange (default units meters)


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


scan
---------------------------------------

:code:`''`

Scan number range


observation
---------------------------------------

:code:`''`

Select by observation ID(s)


msselect
---------------------------------------

:code:`''`

Optional complex data selection (ignore for now)


solint
---------------------------------------

:code:`'inf'`

Solution interval: egs. \'inf\', \'60s\' (see help)


combine
---------------------------------------

:code:`''`

Data axes which to combine for solve (obs, scan, spw, and/or field)


preavg
---------------------------------------

:code:`float(-1.0)`

Pre-averaging interval (sec) (rarely needed)


refant
---------------------------------------

:code:`''`

Reference antenna name(s)


refantmode
---------------------------------------

:code:`'flex'`

Reference antenna mode


minblperant
---------------------------------------

:code:`int(4)`

Minimum baselines _per antenna_ required for solve


minsnr
---------------------------------------

:code:`float(3.0)`

Reject solutions below this SNR


solnorm
---------------------------------------

:code:`False`

Normalize (squared) solution amplitudes (G, T only)


normtype
---------------------------------------

:code:`'mean'`

Solution normalization calculation type: mean or median


gaintype
---------------------------------------

:code:`'G'`

Type of gain solution (G,T,GSPLINE,K,KCROSS)


smodel
---------------------------------------

:code:`numpy.array( [  ] )`

Point source Stokes parameters for source model.


calmode
---------------------------------------

:code:`'ap'`

Type of solution: (\'ap\', \'p\', \'a\')


append
---------------------------------------

:code:`False`

Append solutions to the (existing) table


splinetime
---------------------------------------

:code:`float(3600.0)`

Spline timescale(sec); All spw\'s are first averaged.


npointaver
---------------------------------------

:code:`int(3)`

The phase-unwrapping algorithm


phasewrap
---------------------------------------

:code:`float(180.0)`

Wrap the phase for jumps greater than this value (degrees)


docallib
---------------------------------------

:code:`False`

Use callib or traditional cal apply parameters


callib
---------------------------------------

:code:`''`

Cal Library filename


gaintable
---------------------------------------

:code:`numpy.array( [  ] )`

Gain calibration table(s) to apply on the fly


gainfield
---------------------------------------

:code:`numpy.array( [  ] )`

Select a subset of calibrators from gaintable(s)


interp
---------------------------------------

:code:`numpy.array( [  ] )`

Temporal interpolation for each gaintable (''=linear)


spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintables(s)


parang
---------------------------------------

:code:`False`

Apply parallactic angle correction on the fly




