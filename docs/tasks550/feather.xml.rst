feather -- Combine two images using their Fourier transforms -- imaging task
=======================================

Description
---------------------------------------

This task can be used as one method of combining single-dish and
interferometric images after they have been separately made.

The algorithm converts each image to the gridded visibility plane,
combines them, and reconverts them into an combined image.  Each image
must include a well-defined beam shape (clean beam) in order for
feathering to work well.  The two images must have the same flux
density normalization scale.



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
     - Name of output feathered image
   * - highres
     - :code:`''`
     - Name of high resolution (interferometer) image
   * - lowres
     - :code:`''`
     - Name of low resolution (single dish) image
   * - sdfactor
     - :code:`float(1.0)`
     - Scale factor to apply to Single Dish image
   * - effdishdiam
     - :code:`float(-1.0)`
     - New effective SingleDish diameter to use in m
   * - lowpassfiltersd
     - :code:`False`
     - Filter out the high spatial frequencies of the SD image


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of output feathered image
                          Default: none

                             Example: imagename='orion_combined.im'



highres
---------------------------------------

:code:`''`

Name of high resolution (interferometer) image
                          Default: none

                             Example: imagename='orion_vla.im'



lowres
---------------------------------------

:code:`''`

Name of low resolution (single dish) image
                          Default: none

                             Example: imagename='orion_gbt.im'



sdfactor
---------------------------------------

:code:`float(1.0)`

Value by which to scale the Single Dish image.
                          Default: 1.0

                          Basically modifying the flux scale of the SD image



effdishdiam
---------------------------------------

:code:`float(-1.0)`

New effective SingleDish diameter to use in m 
                          Default: -1.0 (leave as is)

                          Obviously one can only reduce the dish
			  effective dish diameter in feathering.



lowpassfiltersd
---------------------------------------

:code:`False`

Filter out the high spatial frequencies of the SD image
                          Default: False

                          If True the high spatial frequency in the SD
			  image is rejected.

                          Any data outside the maximum uv distance
			  that the SD has illuminated  is filtered
			  out.





