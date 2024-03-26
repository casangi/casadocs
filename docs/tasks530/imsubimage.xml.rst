imsubimage -- Create a (sub)image from a region of the image -- analysis task
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
   * - outfile
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
   * - dropdeg
     - :code:`False`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - verbose
     - :code:`True`
     - 
   * - stretch
     - :code:`False`
     - 
   * - keepaxes
     - :code:`numpy.array( [  ] )`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Input image name.  Default is unset.


outfile
---------------------------------------

:code:`''`

Output image name.  Default is unset.


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. Default is to use the entire direction plane.


region
---------------------------------------

:code:`''`

Region selection. Default is to use the full image.


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


dropdeg
---------------------------------------

:code:`False`

Drop degenerate axes


overwrite
---------------------------------------

:code:`False`

Overwrite (unprompted) pre-existing output file?


verbose
---------------------------------------

:code:`True`

Post additional informative messages to the logger


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 


keepaxes
---------------------------------------

:code:`numpy.array( [  ] )`

If dropdeg=True, these are the degenerate axes to keep. Nondegenerate axes are implicitly always kept.




