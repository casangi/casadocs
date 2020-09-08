#
# stub function definition file for docstring parsing
#

def deconvolve(imagename, model='', psf=[''], alg='clark', niter=10, gain=0.1, threshold=0.0, mask='', scales=[0, 3, 10], sigma=0.0, targetflux=1.0, prior=''):
    r"""
Image based deconvolver

Parameters
   - imagename_ (string) - 
   - model_ (string='') - 
   - psf_ (stringArray=['']) - 
   - alg_ (string='clark') - 

      .. raw:: html

         <details><summary><i> alg = multiscale </i></summary>

      - scales_ (intArray=[0, 3, 10]) - 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> alg = mem </i></summary>

      - sigma_ (double=0.0) - 
      - targetflux_ (double=1.0) - 
      - prior_ (string='') - 

      .. raw:: html

         </details>
   - niter_ (int=10) - 
   - gain_ (double=0.1) - 
   - threshold_ (double=0.0) - 
   - mask_ (string='') - 


Description
   **deconvolve** performs minor cycle deconvolution directly on a
   dirty image. No MS is required.

   .. warning:: **ALERT:** **deconvolve** is currently defunct. We plan to
      replace the task with **tclean**code. For the moment use
      **tclean** (although **tclean** requires an MS at this stage),
      or please use**deconvolve** in an older version of CASA
      (v4.7.2 or earlier).

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *imagename*
      

   The input dirty image that will be deconvolved.

   .. rubric:: m *odel*
      

   The output cleaned image containing a deconvolved point model.

   .. rubric:: *psf*
      

   Can be either be an image (e.g., a psf that **tclean** has
   calculated), or a list of values that define a Gaussian,
   e.g.,*psf=['3arcsec', '2.5arcsec', '10deg']* defines a Gaussian
   with '3arcsec' as the major axis, '2.5arcsec' as the minor axis,
   and a position angle of 10 degrees.

   .. rubric:: *alg*
      

   The clean algorithm to use by **deconvolve**. Several algorithms
   are available to deconvolve an image with a known psf (dirty
   beam), or a Gaussian beam. The algorithms are 'clark' (default)
   and 'hogbom' clean, 'multiscale' clean and a Maximum Entropy 'mem'
   clean. Details on the algorithms are given in the `Synthesis
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging>`__
   chapter in the page describing`Deconvolution
   Algorithms. <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__

   .. rubric:: *alg='multiscale'* expandable parameters
      

   .. rubric:: *scales*
      

   A list of scales in units of pixels (see the **deconvolve**
   examples tab).

   .. rubric:: *alg='mem'* expandable parameters
      

   .. rubric:: *sigma*
      

   This parameter allows the user to input an expected noise value,
   which will allow for a faster convergence.

   .. rubric:: *targetflux*
      

   The estimated total flux in the image.

   .. rubric:: *prior*
      

   A starting model to be used by **deconvolve**. If no*prior* is
   provided, a flat image will be used.

   

   .. rubric:: *niter*
      

   The number of iterations to perform on the image. Default: 10

   .. rubric:: *gain*
      

   Sets the CLEAN gain parameter. Default: 0.1

   .. rubric:: *threshold*
      

   Sets the lower level below which sources will not be deconvolved.

   .. rubric:: *mask*
      

   The image mask to limit the region of deconvolution.




Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Input image to deconvolve

.. _model:

   .. rubric:: model

   | Output image containing deconvolved point model

.. _psf:

   .. rubric:: psf

   | Point spread function (dirty beam)

.. _alg:

   .. rubric:: alg

   | Algorithm to use (clark, hogbom, multiscale, mem)

.. _niter:

   .. rubric:: niter

   | number of iteration in deconvolution process

.. _gain:

   .. rubric:: gain

   | CLEAN gain parameter

.. _threshold:

   .. rubric:: threshold

   | level below which sources will not be deconvolved

.. _mask:

   .. rubric:: mask

   | image mask to limit region of deconvolution

.. _scales:

   .. rubric:: scales

   | scale sizes (pixels) to deconvolve

.. _sigma:

   .. rubric:: sigma

   | mem parameter: Expected noise in image

.. _targetflux:

   .. rubric:: targetflux

   | mem parameter: Estimated total flux in image

.. _prior:

   .. rubric:: prior

   | mem parameter: prior image for mem search


    """
    pass
