uvmodelfit -- Fit a single component source model to the uv data -- modeling, calibration task
=======================================

Description
---------------------------------------

	Fit a single component source model to the uv data



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
   * - msselect
     - :code:`''`
     - 
   * - niter
     - :code:`int(5)`
     - 
   * - comptype
     - :code:`'P'`
     - 
   * - sourcepar
     - :code:`numpy.array( [ float(1.0),float(0.0),float(0.0) ] )`
     - 
   * - varypar
     - :code:`numpy.array( [  ] )`
     - 
   * - outfile
     - :code:`''`
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


msselect
---------------------------------------

:code:`''`

Optional complex data selection (ignore for now)


niter
---------------------------------------

:code:`int(5)`

Number of fitting iterations to execute


comptype
---------------------------------------

:code:`'P'`

component model type: P(oint), G(aussian), or D(isk)


sourcepar
---------------------------------------

:code:`numpy.array( [ float(1.0),float(0.0),float(0.0) ] )`

Starting guess for component parameters (3 values for type P, 5 for G and D)


varypar
---------------------------------------

:code:`numpy.array( [  ] )`

Control which parameters to let vary in the fit


outfile
---------------------------------------

:code:`''`

Optional output component list table




