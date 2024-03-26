immoments -- Compute moments from an image -- analysis task
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
   * - moments
     - :code:`numpy.array( [  ] )`
     - 
   * - axis
     - :code:`'spectral'`
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
   * - mask
     - :code:`''`
     - 
   * - includepix
     - :code:`int(-1)`
     - 
   * - excludepix
     - :code:`int(-1)`
     - 
   * - outfile
     - :code:`''`
     - 
   * - stretch
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


moments
---------------------------------------

:code:`numpy.array( [  ] )`

List of moments you would like to compute


axis
---------------------------------------

:code:`'spectral'`

The momement axis: ra, dec, lat, long, spectral, or stokes


region
---------------------------------------

:code:`''`

Region selection. See "help par.region" for details. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region(s) to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


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


includepix
---------------------------------------

:code:`int(-1)`

Range of pixel values to include


excludepix
---------------------------------------

:code:`int(-1)`

Range of pixel values to exclude


outfile
---------------------------------------

:code:`''`

Output image file name (or root for multiple moments) 


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 




