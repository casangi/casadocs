#
# stub function definition file for docstring parsing
#

def feather(highres, lowres, imagename='', sdfactor=1.0, effdishdiam=-1.0, lowpassfiltersd=False):
    r"""
Combine two images using their Fourier transforms

Parameters
   - **imagename** (string='') - Name of output feathered image
   - **highres** (string) - Name of high resolution (interferometer) image
   - **lowres** (string) - Name of low resolution (single dish) image
   - **sdfactor** (double=1.0) - Scale factor to apply to Single Dish image
   - **effdishdiam** (double=-1.0) - New effective SingleDish diameter to use in m
   - **lowpassfiltersd** (bool=False) - Filter out the high spatial frequencies of the SD image


Description
      .. rubric:: Summary
         :name: summary

      **feather** can be used as one method of combining single-dish and
      interferometric images after they have been separately made.
      The algorithm converts each image to the gridded visibility plane,
      combines them, and reconverts them into a combined image. Each
      image must include a well-defined beam shape (clean beam) in order
      for feathering to work well; these could be a 'clean beam' for
      interferometric images, and a 'primary-beam' for a single-dish
      image. The two images must have the same flux density
      normalization scale.

      More information about **feather** can be found in the `Image
      Combination <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/feather>`__
      section of the CASAdocs. 

      Feathering is a simple method for combining two images with
      different spatial resolution. The processing steps are:

      #. Regrid the low-resolution image to a temporary copy matching
         the resolution of the high-resolution image.
      #. Transform each image to the spatial-frequency plane (gridded).
      #. Scale the low-resolution image (uv-grid) by the ratio of the
         volumes of the two 'clean beams' (high-res/low-res).
      #. Add to this, the uv-grid of the high-resolution image, scaled
         by (1-:math:`\omega` t) where ':math:`\omega` t' is the
         Fourier transform of the 'clean beam' defined in the
         low-resolution image.
      #. Transform back to the image plane.

      One commonly used option for feather is sdfactor, which can be
      used to adjust the flux scale of the SD image in the case that the
      fluxes don't match where there is overlap between the
      spatial-frequencies in the SD image and the interferometer image.

       

      |The results of feathering ALMA 12+7m and Total Power data for
      M100 using three different sdfactors: 0.5 (right) 0.7 (middle) 1.3
      (left). The higher sdfactor (1.3) recovers more of the faint
      extended emission, as it is boosting the TP signal. |

      | *The results of feathering ALMA 12+7m and Total Power data for
        M100 using three different sdfactors: 0.5 (right) 0.7 (middle)
        1.3 (left). The higher sdfactor (1.3) recovers more of the faint
        extended emission, as it is boosting the TP signal.*
      |  

      .. note:: **NOTE**: The **tclean** task allows another method of
         combining single-dish and interferometric data. The single-dish
         image can be used as a starting model for the interferometric
         image-reconstruction. If there is some overlap between the
         spatial-frequencies contained in the single-dish image and the
         interferometer sampling function, then such a starting model
         will help constrain the solutions on the short-baselines of the
         interferometric data.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *imagename*
         :name: imagename

      Name of output feathered image. Default is none; example:
      *imagename='orion_combined.im'*.

      .. rubric:: *highres*
         :name: highres

      Name of high resolution (interferometer) image. Default is none;
      example: *highres='orion_vla.im'*. This image is often a clean
      image obtained from synthesis observations.

      .. rubric:: *lowres*
         :name: lowres

      Name of low resolution (single dish) image. Default is none;
      example: *lowres='orion_gbt.im'*. This image is often a image from
      a single-dish observations or a clean image obtained from lower
      resolution synthesis observations.

      .. rubric:: *sdfactor*
         :name: sdfactor

      Value by which to scale the Single Dish image. Default is 1.0.
      Basically modifying the flux scale of the SD image.

      .. rubric:: *effdishdiam*
         :name: effdishdiam

      New effective SingleDish diameter to use in meters [m]. One can
      only reduce the dish effective dish diameter in feathering.
      Default is -1.0 which means leave as is.

      .. rubric:: *lowpassfiltersd*
         :name: lowpassfiltersd

      If True the high spatial frequency in the SD image is rejected.
      Any data outside the maximum uv distance that the SD has
      illuminated is filtered out.

.. |The results of feathering ALMA 12+7m and Total Power data for M100 using three different sdfactors: 0.5 (right) 0.7 (middle) 1.3 (left). The higher sdfactor (1.3) recovers more of the faint extended emission, as it is boosting the TP signal. | image:: ../media/c54b9bc64427577246358518c70157487bed008a.png
   :class: image-inline

    """
    pass
