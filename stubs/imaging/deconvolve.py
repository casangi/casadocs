#
# stub function definition file for docstring parsing
#

def deconvolve(imagename, model='', psf=[''], alg='clark', niter=10, gain=0.1, threshold=0.0, mask='', scales=[0, 3, 10], sigma=0.0, targetflux=1.0, prior=''):
    r"""
Image based deconvolver

Parameters
   - imagename_ (string)
   - model_ (string='')
   - psf_ (stringArray=[''])
   - alg_ (string='clark')

      .. raw:: html

         <details><summary><i> alg = multiscale </i></summary>

      - scales_ (intArray=[0, 3, 10])

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> alg = mem </i></summary>

      - sigma_ (double=0.0)
      - targetflux_ (double=1.0)
      - prior_ (string='')

      .. raw:: html

         </details>
   - niter_ (int=10)
   - gain_ (double=0.1)
   - threshold_ (double=0.0)
   - mask_ (string='')


Description
   **deconvolve** performs minor cycle deconvolution directly on a
   dirty image. No MS is required.

   .. warning:: **ALERT:** **deconvolve** is currently defunct. We plan to
      replace the task with **tclean**code. For the moment use
      **tclean** (although **tclean** requires an MS at this stage),
      or please use**deconvolve** in an older version of CASA
      (v4.7.2 or earlier).


.. _imagename:

imagename (string)
   | Input image to deconvolve

.. _model:

model (string='')
   | Output image containing deconvolved point model

.. _psf:

psf (stringArray=[''])
   | Point spread function (dirty beam)

.. _alg:

alg (string='clark')
   | Algorithm to use (clark, hogbom, multiscale, mem)

.. _niter:

niter (int=10)
   | number of iteration in deconvolution process

.. _gain:

gain (double=0.1)
   | CLEAN gain parameter

.. _threshold:

threshold (double=0.0)
   | level below which sources will not be deconvolved

.. _mask:

mask (string='')
   | image mask to limit region of deconvolution

.. _scales:

scales (intArray=[0, 3, 10])
   | scale sizes (pixels) to deconvolve

.. _sigma:

sigma (double=0.0)
   | mem parameter: Expected noise in image

.. _targetflux:

targetflux (double=1.0)
   | mem parameter: Estimated total flux in image

.. _prior:

prior (string='')
   | mem parameter: prior image for mem search


    """
    pass
