blcal -- Calculate a baseline-based calibration solution (gain or bandpass) -- calibration task
=======================================

Description
---------------------------------------






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
     - :code:`'scan'`
     - 
   * - freqdep
     - :code:`False`
     - 
   * - calmode
     - :code:`'ap'`
     - 
   * - solnorm
     - :code:`False`
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

Solution interval


combine
---------------------------------------

:code:`'scan'`

Data axes which to combine for solve (obs, scan, spw, and/or field)


freqdep
---------------------------------------

:code:`False`

Solve for frequency dependent solutions


calmode
---------------------------------------

:code:`'ap'`

Type of solution" (\'ap\', \'p\', \'a\')


solnorm
---------------------------------------

:code:`False`

Normalize average solution amplitudes to 1.0


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

Interpolation mode (in time) to use for each gaintable


spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintables(s)


parang
---------------------------------------

:code:`False`

Apply parallactic angle correction




