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
     - Name of the input image
   * - moments
     - :code:`numpy.array( [  ] )`
     - List of moments you would like to compute
   * - axis
     - :code:`'spectral'`
     - The momement axis: ra, dec, lat, long, spectral, or stokes
   * - region
     - :code:`''`
     - Region selection. Default is to use the full image.
   * - box
     - :code:`''`
     - Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
   * - chans
     - :code:`''`
     - Channels to use. Default is to use all channels.
   * - stokes
     - :code:`''`
     - Stokes planes to use. Default is to use all Stokes planes.
   * - mask
     - :code:`''`
     - Mask to use. Default is none.
   * - includepix
     - :code:`int(-1)`
     - Range of pixel values to include
   * - excludepix
     - :code:`int(-1)`
     - Range of pixel values to exclude
   * - outfile
     - :code:`''`
     - Output image file name (or root for multiple moments)
   * - stretch
     - :code:`False`
     - Stretch the mask if necessary and possible?


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

Region selection. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.


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




