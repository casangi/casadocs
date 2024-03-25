gencal -- Specify Calibration Values of Various Types -- calibration task
=======================================

Description
---------------------------------------


        Specify calibration externally.

	


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
   * - caltype
     - :code:`''`
     - 
   * - infile
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - parameter
     - :code:`numpy.array( [  ] )`
     - 
   * - uniform
     - :code:`True`
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

The new/existing calibration table


caltype
---------------------------------------

:code:`''`

The calibration type: \'amp\',\'ph\',\'sbd\',\'mbd\',\'antpos\',\'antposvla\',\'tsys\',\'evlagain\',\'opac\',\'gc\',\'gceff\',\'eff\',\'tecim\'


infile
---------------------------------------

:code:`''`

Input ancilliary file


spw
---------------------------------------

:code:`''`

Calibration spw(s) selection


antenna
---------------------------------------

:code:`''`

Calibration antenna(s) selection


pol
---------------------------------------

:code:`''`

Calibration polarizations(s) selection


parameter
---------------------------------------

:code:`numpy.array( [  ] )`

The calibration values


uniform
---------------------------------------

:code:`True`

Assume uniform calibration values across the array




