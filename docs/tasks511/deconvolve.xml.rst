deconvolve -- Image based deconvolver -- imaging task
=======================================

Description
---------------------------------------

Several algorithms are available to deconvolve an image with a
known psf (dirty beam), or a Gaussian beam.  The algorithms
available are clark and hogbom clean, a multiscale clean and a
mem clean.

NOTE: Recommend using taskname=clean if psf is a dirty beam


  


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
   * - model
     - :code:`''`
     - 
   * - psf
     - :code:`numpy.array( [  ] )`
     - 
   * - alg
     - :code:`'clark'`
     - 
   * - niter
     - :code:`int(10)`
     - 
   * - gain
     - :code:`float(0.1)`
     - 
   * - threshold
     - :code:`{'value': float(0.0), 'unit': 'mJy'}`
     - 
   * - mask
     - :code:`''`
     - 
   * - scales
     - :code:`numpy.array( [ int(0),int(3),int(10) ] )`
     - 
   * - sigma
     - :code:`{'value': float(0.0), 'unit': 'mJy'}`
     - 
   * - targetflux
     - :code:`{'value': float(1.0), 'unit': 'Jy'}`
     - 
   * - prior
     - :code:`''`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Input image to deconvolve


model
---------------------------------------

:code:`''`

Output image containing deconvolved point model


psf
---------------------------------------

:code:`numpy.array( [  ] )`

Point spread function (dirty beam)


alg
---------------------------------------

:code:`'clark'`

Algorithm to use (clark, hogbom, multiscale, mem) 


niter
---------------------------------------

:code:`int(10)`

number of iteration in deconvolution process


gain
---------------------------------------

:code:`float(0.1)`

CLEAN gain parameter


threshold
---------------------------------------

:code:`{'value': float(0.0), 'unit': 'mJy'}`

level below which sources will not be deconvolved


mask
---------------------------------------

:code:`''`

image mask to limit region of deconvolution


scales
---------------------------------------

:code:`numpy.array( [ int(0),int(3),int(10) ] )`

scale sizes (pixels) to deconvolve


sigma
---------------------------------------

:code:`{'value': float(0.0), 'unit': 'mJy'}`

mem parameter: Expected noise in image


targetflux
---------------------------------------

:code:`{'value': float(1.0), 'unit': 'Jy'}`

mem parameter: Estimated total flux in image


prior
---------------------------------------

:code:`''`

mem parameter: prior image for mem search




