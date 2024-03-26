polcal -- Determine instrumental polarization calibrations -- calibration task
=======================================

Description
---------------------------------------

The complex instrumental polarization factors (D-terms) for each antenna/spwid 
are determined from the data for the specified calibrator sources. Previous 
calibrations can be applied on the fly.



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
   * - caltable
     - :code:`''`
     - Name of output gain calibration table
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - intent
     - :code:`''`
     - Select observing intent
   * - selectdata
     - :code:`True`
     - Other data selection parameters
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - uvrange
     - :code:`''`
     - Select data within uvrange (default units meters)
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - scan
     - :code:`''`
     - Scan number range
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - msselect
     - :code:`''`
     - Optional complex data selection (ignore for now)
   * - solint
     - :code:`'inf'`
     - Solution interval
   * - combine
     - :code:`'obs,scan'`
     - Data axes which to combine for solve (obs, scan, spw, and/or field)
   * - preavg
     - :code:`float(300.0)`
     - Pre-averaging interval (sec)
   * - refant
     - :code:`''`
     - Reference antenna name(s)
   * - minblperant
     - :code:`int(4)`
     - Minimum baselines _per antenna_ required for solve
   * - minsnr
     - :code:`float(3.0)`
     - Reject solutions below this SNR
   * - poltype
     - :code:`'D+QU'`
     - Type of instrumental polarization solution (see help)
   * - smodel
     - :code:`numpy.array( [  ] )`
     - Point source Stokes parameters for source model.
   * - append
     - :code:`False`
     - Append solutions to the (existing) table
   * - docallib
     - :code:`False`
     - Use callib or traditional cal apply parameters
   * - callib
     - :code:`''`
     - Cal Library filename
   * - gaintable
     - :code:`numpy.array( [  ] )`
     - Gain calibration table(s) to apply
   * - gainfield
     - :code:`numpy.array( [  ] )`
     - Select a subset of calibrators from gaintable(s)
   * - interp
     - :code:`numpy.array( [  ] )`
     - Interpolation mode (in time) to use for each gaintable
   * - spwmap
     - :code:`[ ]`
     - Spectral window mappings to form for gaintable(s)


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

:code:`'obs,scan'`

Data axes which to combine for solve (obs, scan, spw, and/or field)


preavg
---------------------------------------

:code:`float(300.0)`

Pre-averaging interval (sec)


refant
---------------------------------------

:code:`''`

Reference antenna name(s)


minblperant
---------------------------------------

:code:`int(4)`

Minimum baselines _per antenna_ required for solve


minsnr
---------------------------------------

:code:`float(3.0)`

Reject solutions below this SNR


poltype
---------------------------------------

:code:`'D+QU'`

Type of instrumental polarization solution (see help)


smodel
---------------------------------------

:code:`numpy.array( [  ] )`

Point source Stokes parameters for source model.


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

Gain calibration table(s) to apply


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

:code:`[ ]`

Spectral window mappings to form for gaintable(s)
                     Only used if callib=False
                     default: [] (apply solutions from each calibration spw to
                     the same MS spw only)
                     Any available calibration spw can be mechanically mapped to any 
                      MS spw. 
                     Examples:
                        spwmap=[0,0,1,1] means apply calibration 
                          from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
                          gaintables)
	  




