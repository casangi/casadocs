rmfit -- Calculate rotation measure. -- analysis task
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
   * - imagename
     - :code:`''`
     - Name(s) of the input image(s). Must be specified.
   * - rm
     - :code:`''`
     - Output rotation measure image name. If not specified, no image is written.
   * - rmerr
     - :code:`''`
     - Output rotation measure error image name. If not specified, no image is written.
   * - pa0
     - :code:`''`
     - Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.
   * - pa0err
     - :code:`''`
     - Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.
   * - nturns
     - :code:`''`
     - Output number of turns image name. If not specified, no image is written.
   * - chisq
     - :code:`''`
     - Output reduced chi squared image name. If not specified, no image is written.
   * - sigma
     - :code:`float(-1)`
     - Estimate of the thermal noise.  A value less than 0 means auto estimate.
   * - rmfg
     - :code:`float(0.0)`
     - Foreground rotation measure in rad/m/m to subtract.
   * - rmmax
     - :code:`float(0.0)`
     - Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.
   * - maxpaerr
     - :code:`float(1e30)`
     - Maximum input position angle error in degrees to allow in solution determination.


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name(s) of the input image(s). Must be specified.


rm
---------------------------------------

:code:`''`

Output rotation measure image name. If not specified, no image is written.


rmerr
---------------------------------------

:code:`''`

Output rotation measure error image name. If not specified, no image is written.


pa0
---------------------------------------

:code:`''`

Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.


pa0err
---------------------------------------

:code:`''`

Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.


nturns
---------------------------------------

:code:`''`

Output number of turns image name. If not specified, no image is written.


chisq
---------------------------------------

:code:`''`

Output reduced chi squared image name. If not specified, no image is written.


sigma
---------------------------------------

:code:`float(-1)`

Estimate of the thermal noise.  A value less than 0 means auto estimate.


rmfg
---------------------------------------

:code:`float(0.0)`

Foreground rotation measure in rad/m/m to subtract.


rmmax
---------------------------------------

:code:`float(0.0)`

Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.


maxpaerr
---------------------------------------

:code:`float(1e30)`

Maximum input position angle error in degrees to allow in solution determination.




