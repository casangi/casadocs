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
