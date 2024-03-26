imrebin -- Rebin an image by the specified integer factors -- analysis task
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
   * - outfile
     - :code:`''`
     - Output image name.
   * - factor
     - :code:`numpy.ndarray(0)`
     - Binning factors for each axis. Use imhead or ia.summary to determine axis ordering.
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
     - Stokes planes to use. Default is to use all Stokes planes. Stokes planes cannot be rebinned.
   * - mask
     - :code:`''`
     - Mask to use. Default is none.
   * - dropdeg
     - :code:`False`
     - Drop degenerate axes?
   * - overwrite
     - :code:`False`
     - Overwrite the output if it exists? Default False
   * - stretch
     - :code:`False`
     - Stretch the mask if necessary and possible?
   * - crop
     - :code:`True`
     - Remove pixels from the end of an axis to be rebinned if there are not enough to form an integral bin?


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


outfile
---------------------------------------

:code:`''`

Output image name.


factor
---------------------------------------

:code:`numpy.ndarray(0)`

Binning factors for each axis. Use imhead or ia.summary to determine axis ordering.


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

Stokes planes to use. Default is to use all Stokes planes. Stokes planes cannot be rebinned.


mask
---------------------------------------

:code:`''`

Mask to use. Default is none.


dropdeg
---------------------------------------

:code:`False`

Drop degenerate axes?


overwrite
---------------------------------------

:code:`False`

Overwrite the output if it exists? Default False


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 


crop
---------------------------------------

:code:`True`

Remove pixels from the end of an axis to be rebinned if there are not enough to form an integral bin?




