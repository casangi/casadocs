specflux -- Report details of an image spectrum. -- analysis task
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
     - 
   * - box
     - :code:`''`
     - 
   * - region
     - :code:`''`
     - 
   * - chans
     - :code:`''`
     - 
   * - stokes
     - :code:`''`
     - 
   * - mask
     - :code:`''`
     - 
   * - stretch
     - :code:`False`
     - 
   * - unit
     - :code:`'km/s'`
     - 
   * - major
     - :code:`''`
     - 
   * - minor
     - :code:`''`
     - 
   * - logfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


region
---------------------------------------

:code:`''`

Region selection. See "help par.region" for details. Default is to use the full image.


chans
---------------------------------------

:code:`''`

Channels to use. See "help par.chans" for details. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. See "help par.stokes" for details. Default is to use all Stokes planes.


mask
---------------------------------------

:code:`''`

Mask to use. See help par.mask. Default is none.


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? See help par.stretch 


unit
---------------------------------------

:code:`'km/s'`

Unit to use for the abscissa. Must be conformant with a typical spectral axis unit.


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




