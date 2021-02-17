

.. _Description:

Description
   **deconvolve** performs minor cycle deconvolution directly on a
   dirty image. No MS is required. 
   
   .. warning:: **ALERT:** **deconvolve** is currently defunct. We plan to
      replace the task with **tclean** code. For the moment use
      **tclean** (although **tclean** requires an MS at this stage),
      or please use **deconvolve** in an older version of CASA
      (v4.7.2 or earlier).
   
   .. rubric:: Parameter descriptions

   *imagename*
   
   The input dirty image that will be deconvolved.
   
   *model*
   
   The output cleaned image containing a deconvolved point model.
   
   *psf*
   
   Can be either be an image (e.g., a psf that **tclean** has
   calculated), or a list of values that define a Gaussian,
   e.g., *psf=['3arcsec', '2.5arcsec', '10deg']* defines a Gaussian
   with '3arcsec' as the major axis, '2.5arcsec' as the minor axis,
   and a position angle of 10 degrees. 
   
   *alg*
   
   The clean algorithm to use by **deconvolve**. Several algorithms
   are available to deconvolve an image with a known psf (dirty
   beam), or a Gaussian beam. The algorithms are 'clark' (default)
   and 'hogbom' clean, 'multiscale' clean and a Maximum Entropy 'mem'
   clean. Details on the algorithms are given in the `Synthesis
   Imaging <../../notebooks/synthesis_imaging.ipynb>`__
   chapter in the page describing `Deconvolution
   Algorithms. <../../notebooks/synthesis_imaging.ipynb#Deconvolution-Algorithms>`__
   
   .. rubric:: *alg='multiscale'* expandable parameters

   *scales*

   A list of scales in units of pixels (see the **deconvolve**
   examples tab).
   
   .. rubric:: *alg='mem'* expandable parameters
   
   *sigma*
   
   This parameter allows the user to input an expected noise value,
   which will allow for a faster convergence.
   
   *targetflux*
   
   The estimated total flux in the image.
   
   *prior*
   
   A starting model to be used by **deconvolve**. If no *prior* is
   provided, a flat image will be used.
   
   *niter*
   
   The number of iterations to perform on the image. Default: 10
   
   *gain*
   
   Sets the CLEAN gain parameter. Default: 0.1
   
   *threshold*
   
   Sets the lower level below which sources will not be deconvolved.
   
   *mask*
   
   The image mask to limit the region of deconvolution.


.. _Examples:

Examples
   Deconvolve the dirty image 'mydirtyimage.image' with a dirty beam
   (psf) 'mydirtyimage.psf'. No MS is required as only minor cycles
   are performed. We are using the 'multiscale' clean algorithm with
   scales of 0, 3, and 10 pixels. The stopping criteria are either
   10000 iterations, or an RMS threshold of 10mJy: 
   
   ::
   
      deconvolve(imagename='mydirtyimage.image',
      model='mycleanimage.image', psf='mydirtyimage.psf',
      alg='multiscale', scales=[0,3,10], niter=10000, gain=0.1,
      threshold='10mJy')
   

.. _Development:

Development
   No additional development details

