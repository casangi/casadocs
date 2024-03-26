fringefit -- Fringe fit delay and rates -- calibration task
=======================================

Description
---------------------------------------

Phase offsets, groups delays and delay rates are calculated with
respect to a specified referance antenna by a two-dimensional FFT and
subsequent least-squares optimisation.

Previous calibrations should be applied on the fly.




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
   * - refant
     - :code:`''`
     - 
   * - minsnr
     - :code:`float(3.0)`
     - 
   * - zerorates
     - :code:`False`
     - 
   * - globalsolve
     - :code:`True`
     - 
   * - delaywindow
     - :code:`numpy.array( [  ] )`
     - 
   * - ratewindow
     - :code:`numpy.array( [  ] )`
     - 
   * - append
     - :code:`False`
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


refant
---------------------------------------

:code:`''`

Reference antenna name(s)


minsnr
---------------------------------------

:code:`float(3.0)`

Reject solutions below this signal-to-noise ratio (at the FFT stage)


zerorates
---------------------------------------

:code:`False`

Zero delay-rates in solution table


globalsolve
---------------------------------------

:code:`True`

Refine estimates of delay and rate with global least-squares solver


delaywindow
---------------------------------------

:code:`numpy.array( [  ] )`

Constrain FFT delay search to a window; a two-element list, units of nanoseconds


ratewindow
---------------------------------------

:code:`numpy.array( [  ] )`

Constrain FFT rate search to a window; a two-element list, units of seconds per second


append
---------------------------------------

:code:`False`

Append solutions to the (existing) table


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




