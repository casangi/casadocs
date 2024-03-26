imcontsub -- Estimates and subtracts continuum emission from an image cube -- analysis, imaging task
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
   * - linefile
     - :code:`''`
     - 
   * - contfile
     - :code:`''`
     - 
   * - fitorder
     - :code:`int(0)`
     - 
   * - region
     - :code:`''`
     - 
   * - box
     - :code:`''`
     - 
   * - chans
     - :code:`''`
     - 
   * - stokes
     - :code:`''`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input spectral line image


linefile
---------------------------------------

:code:`''`

Output continuum-subtracted image file name


contfile
---------------------------------------

:code:`''`

Output continuum image file name


fitorder
---------------------------------------

:code:`int(0)`

Polynomial order for the continuum estimation


region
---------------------------------------

:code:`''`

Region selection. See "help par.region" for details. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use for fitting. See "help par.chans" for details. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. See "help par.stokes" for details. Default is to use all Stokes planes.




