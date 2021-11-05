

.. _Description:

Description
   **feather** can be used as one method of combining single-dish and
   interferometric images after they have been separately made.
   The algorithm converts each image to the gridded visibility plane,
   combines them, and reconverts them into a combined image. Each
   image must include a well-defined beam shape (clean beam) in order
   for feathering to work well; these could be a 'clean beam' for
   interferometric images, and a 'primary-beam' for a single-dish
   image. Images with multiple (per-plane) beams are supported. The
   two images must have the same flux density
   normalization scale.
   
   Currently, the following constraints are imposed on the two input
   images:

   * The images must have identical shapes and number of dimensions
   * The images must have 2, 3, or 4 dimensions
   * The image coordinate systems must have identical axis names in
     the same order
   * The image coordinate systems must have identical coordinate
     types in the same order
   * image coordinate systems must have coincident world and pixel
     coordinates at all pixels.

   In general, it is the responsibility of the user to regrid the
   low resolution image to coincide with the coordinate system of
   the high resolution image and to ensure that the resulting
   regridded image is of reasonable quality to use in feather.
   This can be achieved via the imregrd task for the image.regrid()
   tool method.
   
   Mathematically, the feathered image, :math:`I_{feather}`, is produced via

   .. math::

        I_{feather} = \frac{\mathcal{F}^{-1}[\mathcal{F}(I_{highres}) + B*\mathcal{F}(S*I_{lowres})]}{1 + B}

   where  :math:`I_{highres}` and :math:`I_{lowres}` are the high resolution
   (interferometer) and low resolution (single dish) images, respectively,
   :math: `S` is the user-specified factor by which to scale the low resolution image
   brightness scale, :math:`B` is the ratio of the high resolution beam area to the low
   resolution beam area, :math:`\mathcal{F}` denotes the Fast Fourier Transform,
   and :math: `\mathcal{F}^{-1}` denotes the Inverse Fast Fourier Transform. In the case
   where the high resolution and low resolution images have a single beam each,
   :math:`B` is a scalar. In the case one of them has multiple (per-plane) beams,
   :math:`B` is a matrix with each element corresponding to the beam ratios for
   each frequency channel/polarization pair, and the multiplication and division
   of terms with :math:`B` are done element-wise, so that the above equation is
   valid for every frequency channel/polarization pair :math: `(f, p)`:


   .. math::

        I_{{feather}_{(f, p)}} = \frac{\mathcal{F}^{-1}[\mathcal{F}(I_{{highres}_{(f, p)}}) + B_{(f, p)}*\mathcal{F}(S*I_{{lowres}_{(f, p)}})]}{1 + B_{(f, p)}}

   The output image will have an identical resolution to the high resolution image.

    


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
   
   **I am not certain how to factor this into the math/algorithm**
   New effective SingleDish diameter to use in meters [m]. One can
   only reduce the dish effective dish diameter in feathering.
   Default is -1.0 which means leave as is.
   
   *lowpassfiltersd*
   
   **I am not certain how to factor this into the math/algorithm**
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

   
