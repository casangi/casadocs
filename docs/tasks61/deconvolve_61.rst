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



