applycal -- Apply calibrations solutions(s) to data -- calibration task
=======================================

Description
---------------------------------------

Applycal reads the specified gain calibration tables, applies
them to the (raw) data column (with the specified selection),
and writes the calibrated results into the corrected column.
This is done in one step, so all available calibration must
be specified.  Applycal will overwrite existing corrected data.

Standard data selection is supported.  See help par.selectdata
for more information.

One or more calibration tables (both temporal, frequency, polarization
calibrations) can be specified in the gaintable parameter.  The
calibration values associated with a restricted list of fields
can also be selected for each table.

See task accum for instructions on forming calibration
incrementally.  See task split for saving corrected data in
another visibility file.




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
   * - calwt
     - :code:`numpy.array( [  ] )`
     - 
   * - parang
     - :code:`False`
     - 
   * - applymode
     - :code:`''`
     - 
   * - flagbackup
     - :code:`True`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


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

Interp type in time[,freq], per gaintable. default==linear,linear


spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintables(s)


calwt
---------------------------------------

:code:`numpy.array( [  ] )`

Calibrate data weights per gaintable.


parang
---------------------------------------

:code:`False`

Apply parallactic angle correction


applymode
---------------------------------------

:code:`''`

Calibration mode: ""="calflag","calflagstrict","trial","flagonly","flagonlystrict", or "calonly"


flagbackup
---------------------------------------

:code:`True`

Automatically back up the state of flags before the run?




