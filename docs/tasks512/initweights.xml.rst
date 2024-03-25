initweights -- Initializes weight information in the MS -- calibration task
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
   * - wtmode
     - :code:`'nyq'`
     - 
   * - tsystable
     - :code:`''`
     - 
   * - gainfield
     - :code:`''`
     - 
   * - interp
     - :code:`''`
     - 
   * - spwmap
     - :code:`numpy.array( [  ] )`
     - 
   * - dowtsp
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


wtmode
---------------------------------------

:code:`'nyq'`

Initialization mode


tsystable
---------------------------------------

:code:`''`

Tsys calibration table to apply on the fly


gainfield
---------------------------------------

:code:`''`

Select a subset of calibrators from Tsys table


interp
---------------------------------------

:code:`''`

Interpolation type in time[,freq]. default==linear,linear


spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintables(s)


dowtsp
---------------------------------------

:code:`False`

Initialize the WEIGHT_SPECTRUM column.




