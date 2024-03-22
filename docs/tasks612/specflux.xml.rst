specflux -- Report spectral profile and calculate spectral flux over a user specified region -- analysis task
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
     - Name of the input image
   * - region
     - :code:`''`
     - Region selection. Default is to use the full image.
   * - box
     - :code:`''`
     - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   * - chans
     - :code:`''`
     - Channels to use. Default is to use all channels.
   * - stokes
     - :code:`''`
     - Stokes planes to use. Default is to use all Stokes planes.
   * - mask
     - :code:`''`
     - Mask to use. Default is none.
   * - stretch
     - :code:`False`
     - Stretch the mask if necessary and possible?
   * - function
     - :code:`'flux density'`
     - Aggregate function to use for computing per channel values. Supported values are "flux density", "mean", "median", "sum". Minimal match supported.
   * - unit
     - :code:`'km/s'`
     - Unit to use for the spectral flux calculation. Must be conformant with a typical spectral axis unit.
   * - major
     - :code:`''`
     - Major axis of overriding restoring beam. If specified, must be a valid quantity.
   * - minor
     - :code:`''`
     - Minor axis of overriding restoring beam. If specified, must be a valid quantity
   * - logfile
     - :code:`''`
     - File which to write details. Default is to not write to a file.
   * - overwrite
     - :code:`False`
     - Overwrite exisitng ouput file if it exists?


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


region
---------------------------------------

:code:`''`

Region selection. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. Default is to use all Stokes planes.


mask
---------------------------------------

:code:`''`

Mask to use. Default is none.


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 


function
---------------------------------------

:code:`'flux density'`

Aggregate function to use for computing per channel values. Supported values are "flux density", "mean", "median", "sum". Minimal match supported.


unit
---------------------------------------

:code:`'km/s'`

Unit to use for the spectral flux calculation. Must be conformant with a typical spectral axis unit.


major
---------------------------------------

:code:`''`

Major axis of overriding restoring beam. If specified, must be a valid quantity.


minor
---------------------------------------

:code:`''`

Minor axis of overriding restoring beam. If specified, must be a valid quantity


logfile
---------------------------------------

:code:`''`

File which to write details. Default is to not write to a file.


overwrite
---------------------------------------

:code:`False`

Overwrite exisitng ouput file if it exists?




