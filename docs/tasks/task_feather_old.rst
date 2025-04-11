

.. _Description:

Description
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
   Combination <../../notebooks/image_combination.ipynb#Feather-&-CASAfeather>`__
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

   .. figure:: _apimedia/featherimage.png
   
      The results of feathering ALMA 12+7m and Total Power data for
      M100 using three different sdfactors: 0.5 (right) 0.7 (middle)
      1.3 (left). The higher sdfactor (1.3) recovers more of the faint
      extended emission, as it is boosting the TP signal.
   
   .. note:: **NOTE**: The **tclean** task allows another method of
      combining single-dish and interferometric data. The single-dish
      image can be used as a starting model for the interferometric
      image-reconstruction. If there is some overlap between the
      spatial-frequencies contained in the single-dish image and the
      interferometer sampling function, then such a starting model
      will help constrain the solutions on the short-baselines of the
      interferometric data.


   .. rubric:: Parameter descriptions

   *imagename*

   Name of output feathered image. Default is none; example:
   *imagename='orion_combined.im'*.
   
   *highres*

   Name of high resolution (interferometer) image. Default is none;
   example: *highres='orion_vla.im'*. This image is often a clean
   image obtained from synthesis observations.
   
   *lowres*
   
   Name of low resolution (single dish) image. Default is none;
   example: *lowres='orion_gbt.im'*. This image is often a image from
   a single-dish observations or a clean image obtained from lower
   resolution synthesis observations.
   
   *sdfactor*
   
   Value by which to scale the Single Dish image. Default is 1.0.
   Basically modifying the flux scale of the SD image.
   
   *effdishdiam*
   
   New effective SingleDish diameter to use in meters [m]. One can
   only reduce the dish effective dish diameter in feathering.
   Default is -1.0 which means leave as is.
   
   *lowpassfiltersd*
   
   If True the high spatial frequency in the SD image is rejected.
   Any data outside the maximum uv distance that the SD has
   illuminated is filtered out.
   

.. _Examples:

Examples
   Creating a image called 'M100_Feather_CO.image' from an ALMA
   interferometric cube, 'M100_combine_CO_cube.image.subim', and a
   single dish ALMA total power image,
   'M100_TP_CO_cube.regrid.subim.depb'. The inputs have been
   appropriately cleaned, regridded, and cropped beforehand.
   
   ::

      feather(imagename='M100_Feather_CO.image',highres='M100_combine_CO_cube.image.subim',
              lowres='M100_TP_CO_cube.regrid.subim.depb')
   
   Creating an image called 'feather.im' by combining the cleaned,
   synthesis image, 'synth.im' and the SD image, 'single_dish.im'
   while increasing the flux scale of the SD image by setting
   sdfactor = 1.2.
   
   ::

      feather(imagename ='feather.im', highres ='synth.im', lowres ='single_dish.im'sdfactor = 1.2)


.. _Development:

Development
   No additional development details

   