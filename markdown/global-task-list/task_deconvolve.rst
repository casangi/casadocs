Description
      **deconvolve** performs minor cycle deconvolution directly on a
      dirty image. No MS is required. 

      .. note:: **ALERT:** **deconvolve** is currently defunct. We plan to
         replace the task with **tclean** code. For the moment use
         **tclean** (although **tclean** requires an MS at this stage),
         or please use **deconvolve** in an older version of CASA
         (v4.7.2 or earlier).

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *imagename*
         :name: imagename

      The input dirty image that will be deconvolved.

      .. rubric:: m *odel*
         :name: model

      The output cleaned image containing a deconvolved point model.

      .. rubric:: *psf*
         :name: psf

      Can be either be an image (e.g., a psf that **tclean** has
      calculated), or a list of values that define a Gaussian,
      e.g., *psf=['3arcsec', '2.5arcsec', '10deg']* defines a Gaussian
      with '3arcsec' as the major axis, '2.5arcsec' as the minor axis,
      and a position angle of 10 degrees. 

      .. rubric:: *alg*
         :name: alg

      The clean algorithm to use by **deconvolve**. Several algorithms
      are available to deconvolve an image with a known psf (dirty
      beam), or a Gaussian beam. The algorithms are 'clark' (default)
      and 'hogbom' clean, 'multiscale' clean and a Maximum Entropy 'mem'
      clean. Details on the algorithms are given in the `Synthesis
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging>`__
      chapter in the page describing `Deconvolution
      Algorithms. <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__

      .. rubric:: *alg='multiscale'* expandable parameters
         :name: algmultiscale-expandable-parameters

      .. rubric:: *scales*
         :name: scales

      A list of scales in units of pixels (see the **deconvolve**
      examples tab).

      .. rubric:: *alg='mem'* expandable parameters
         :name: algmem-expandable-parameters

      .. rubric:: *sigma*
         :name: sigma

      This parameter allows the user to input an expected noise value,
      which will allow for a faster convergence.

      .. rubric:: *targetflux*
         :name: targetflux

      The estimated total flux in the image.

      .. rubric:: *prior*
         :name: prior

      A starting model to be used by **deconvolve**. If no *prior* is
      provided, a flat image will be used.

       

      .. rubric:: *niter*
         :name: niter

      The number of iterations to perform on the image. Default: 10

      .. rubric:: *gain*
         :name: gain

      Sets the CLEAN gain parameter. Default: 0.1

      .. rubric:: *threshold*
         :name: threshold

      Sets the lower level below which sources will not be deconvolved.

      .. rubric:: *mask*
         :name: mask

      The image mask to limit the region of deconvolution.
