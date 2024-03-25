importmiriad -- Convert a Miriad visibility file into a CASA MeasurementSet -- import/export task
=======================================

Description
---------------------------------------

        Convert a Miriad visibility file into a CASA MeasurementSet with 
	optional selection of spectral windows and weighting scheme
	


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - mirfile
     - :code:`''`
     - 
   * - vis
     - :code:`''`
     - 
   * - tsys
     - :code:`False`
     - 
   * - spw
     - :code:`numpy.array( [  ] )`
     - 
   * - vel
     - :code:`''`
     - 
   * - linecal
     - :code:`False`
     - 
   * - wide
     - :code:`numpy.array( [  ] )`
     - 
   * - debug
     - :code:`int(0)`
     - 


Parameter Explanations
=======================================



mirfile
---------------------------------------

:code:`''`

Name of input Miriad visibility file


vis
---------------------------------------

:code:`''`

Name of output MeasurementSet


tsys
---------------------------------------

:code:`False`

Use the Tsys to set the visibility weights


spw
---------------------------------------

:code:`numpy.array( [  ] )`

Select spectral windows, default is all


vel
---------------------------------------

:code:`''`

Select velocity reference (TOPO,LSRK,LSRD)


linecal
---------------------------------------

:code:`False`

(CARMA) Apply line calibration


wide
---------------------------------------

:code:`numpy.array( [  ] )`

(CARMA) Select wide window averages


debug
---------------------------------------

:code:`int(0)`

Display increasingly verbose debug messages




