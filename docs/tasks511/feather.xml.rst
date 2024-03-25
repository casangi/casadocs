feather -- Combine two images using their Fourier transforms -- imaging task
=======================================

Description
---------------------------------------

The algorithm converts each image to the gridded visibility plane, combines
them, and reconverts them into an combined image.  Each image must include a
well-defined beam shape (clean beam) in order for feathering to work well.  The
two images must have the same flux density normalization scale.

	


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
   * - highres
     - :code:`''`
     - 
   * - lowres
     - :code:`''`
     - 
   * - sdfactor
     - :code:`float(1.0)`
     - 
   * - effdishdiam
     - :code:`float(-1.0)`
     - 
   * - lowpassfiltersd
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of output feathered image


highres
---------------------------------------

:code:`''`

Name of high resolution (interferometer) image


lowres
---------------------------------------

:code:`''`

Name of low resolution (single dish) image


sdfactor
---------------------------------------

:code:`float(1.0)`

Scale factor to apply to Single Dish image


effdishdiam
---------------------------------------

:code:`float(-1.0)`

New effective SingleDish diameter to use in m 


lowpassfiltersd
---------------------------------------

:code:`False`

Filter out the high spatial frequencies of the SD image




