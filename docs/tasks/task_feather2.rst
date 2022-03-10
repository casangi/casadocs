

.. _Description:

Description
   **feather2** can be used as one method of combining single-dish and
   interferometric images after they have been separately made.
   The algorithm converts each image to the gridded visibility plane,
   combines them, and reconverts them into a combined image. Each
   image must include a beam shape in its metadata in order for;
   these could be a 'clean beam' for interferometric images, and a
   'primary-beam' for a single-dish image. Images (both single dish
   and interferometer) with multiple (per-plane) beams are supported.
   The two images must have the same flux density normalization scale.
   
   Currently, the following constraints are imposed on the two input
   images:

   * The images must have identical shapes and number of dimensions
   * The images must have 2, 3, or 4 dimensions
   * The image coordinate systems must have identical axis names in
     the same order
   * The image coordinate systems must have identical coordinate
     types in the same order
   * image coordinate systems must have coincident world and pixel
     coordinates at all pixels,
   * the brightness units of both images should be Jy/beam. If
     an image has another brightness unit (eg K), it is the user's
     responsibility to convert pixel values to Jy/beam and to set
     the brightness unit to Jy/beam in the image metadata. Image
     pixel values can be manipulated using task immath. The
     brightness unit can be set using task imhead or via the
     setbrightnessunit() method of the image tool.
   * each image must have a global beam of per-plane beams defined
     in its metadata. Both images may have global beams, per-plane 
     beams, or one image may havee a global beam and the other
     can have per-plane beams. Note that the user can add or 
     modify beam information by using imhead or the
     setrestoringbeam() method of the image tool.

   In general, it is the responsibility of the user to regrid the
   low resolution image to coincide with the coordinate system of
   the high resolution image and to ensure that the resulting
   regridded image is of reasonable quality to use in **feather2**.
   This can be achieved via the **imregrid** task or the
   **image.regrid()** tool method.
   
   The feathered image, :math:`I^{feather}`, is given by (cf. Rao,
   Naik, & Braun 2019 AJ, 158, 3)

   .. math::

        I^{feather} = \mathcal{F}^{-1}\left[
            \frac
                {(1-w)\mathcal{F}(I^{highres}) + SB\mathcal{F}(I^{lowres})}
                {(1-w) + Sw}
        \right]

   where  :math:`I^{highres}` and :math:`I^{lowres}` are the high resolution
   (interferometer) and low resolution (single dish) images, respectively,
   :math:`S` is the user-specified weight to give the Fourier Transform of
   low resolution image relative to the Fourier Transform of the high
   resolution image, :math:`B` is the ratio of the high resolution beam
   area to the low resolution beam area, :math:`\mathcal{F}` denotes the Fourier
   Transform, :math:`\mathcal{F}^{-1}` denotes the Inverse Fourier Transform,
   and :math:`w` is the Fourier Transform of the single dish psf scaled to a
   maximum of unity

   .. math::
  
        w \equiv \mathcal{F}(I^{lowres, psf})/max[|\mathcal{F}(I^{lowres, psf})|]

   As justification the form of the first equation, one can consider that if the
   two images are the result of simply splitting an interferometer dataset into
   two pieces, then B=1 and w=1 for all uv-cells (since there is no relative
   *uv*-coverage difference for which to account), and so the expression in
   square brackets simplifies to 
   :math:`[\mathcal{F}(im_1)+S\mathcal{F}(im_2)]/(1+S)`. For natural
   weighting, S can be interpreted simply as the ratio of the number of data
   points that were used to create the two images, and so this expression is just
   the weighted average, as expected. 
   
   For the present application, :math:`I^{lowres, psf}` is taken to be the
   elliptical Gaussian beam defined in the low resolution image metadata, with
   major and minor FWHM (:math:`\alpha` and :math:`\beta`) and position angle
   (:math:`\phi`, measured from north to east). In this case,

   .. math::

        I^{lowres, psf} = exp\left\{
            -4ln(2)\left[
                \left(\frac{x\sin(\phi)}{\alpha}\right)^2
                + \left(\frac{y\cos(\phi)}{\beta}\right)^2
            \right]
        \right\}

   and so if :math:`x, y, \alpha`, and :math:`\beta` are measured in radians,
   then, if *u* and *v* are measured in wavelengths

   .. math::

        w \equiv
            \frac{\mathcal{F}(I^{lowres, psf})}{max|\mathcal{F}(I^{lowres, psf})|}
            = exp\left\{
                -\pi\left[
                    \left(u\alpha\cos(\phi)\right)^2
                    + \left(v\beta\sin(\phi)\right)^2
                \right]
            \right\}

   The effect of the :math:`(1-w)` term is to provide uniform weighting to
   :math:`\mathcal{F}(I^{highres})`, which has the benefit of
   down-weighting shorter spacing data which are not well sampled by the
   interferometer.

   A reasonable starting value for *S* is given by

   .. math::

        S = (RMS^{highres}/RMS^{lowres})^2

   where :math:`RMS^{highres}` and :math:`RMS^{lowres}` are the root mean
   square noise measured in the high resolution and low resolution images,
   respectively. This relationship can be derived by considering that the
   canonical combination of the flux measurements from the two images is
   just the weighted mean of the two images, where the weight for each
   image is equal to the reciprocal of the square of the rms of each
   image. Note that the image RMSes should be computed using a common
   solid angle unit, such as in Jy/sr or :math:`Jy/arcsec^2`, not
   Jy/beam or K because the beam areas will, in general, be different for
   the two images. To obtain the desired quantity without explicity
   converting to eg, Jy/sr, one can just use the ratio of the beam areas
   in the above equation:

   .. math::

        S = (RMS^{highres}_{Jy/beam}/RMS^{lowres}_{Jy/beam} * b^{lowres}/b^{highres})^2

   where the RMSes are in units of Jy/beam and :math:`b` denotes the beam area
   for the specified image. The two beam areas should have the same units
   (eg sr or :math:`arcsec^2`).

   In the case where the single dish image has multiple beams, *w* must be
   computed for each frequency/polarization (:math:`\nu`, p) pair. In the case
   where the high resolution and low resolution images have a single beam each,
   :math:`B` is a scalar. In the case in which at least one of them has multiple
   (per-plane) beams, :math:`B` is a matrix with each element corresponding to
   the beam area ratios for each (:math:`\nu`, p) pair, and the multiplication
   of the term with :math:`B` is done (:math:`\nu`, p) pair-wise. So, in 
   the general case where at least one image has multiple beams

   .. math::

        I^{feather}_{\nu, p} = \mathcal{F}^{-1}\left[
            \frac
                {
                    (1-w_{\nu, p})\mathcal{F}(I^{highres}_{\nu, p})
                    + SB_{\nu, p}\mathcal{F}(I^{lowres}_{\nu, p})
                }
                {(1-w_{\nu, p}) + Sw_{\nu, p}}
        \right]

   The output image will have an identical resolution to the high resolution image.

   The application requires that beam information be present in the image
   metadata. Should the beam information be known but absent from the metadata,
   it can be added via task **imhead** using mode='put' or via tool method
   **image.setrestoringbeam()**.

   Should absolute scaling be necessary for the flux densities of the two images to
   be equal, this should be addressed prior to running **feather2**. One can use task
   **immath** or tool method **image.imagecalc()** to scale the pixel values in an
   image.

   ..
        If *lowpassfiltersd* is set to True, then spatial frequencies not sampled by
        the single dish will be omitted. In this case, the Fourier Transform of the
        single dish image, :math:`\mathcal{F}(I^{lowres})`, will have all pixels with
        *uv* distances greater than :math:`d/\lambda` wavelengths from the origin
        masked before combination with :math:`\mathcal{F}(I^{highres})`, so that
        :math:`\mathcal{F}(I^{lowres}) \equiv 0` for these *u-v* distances. Here,
        :math:`d` and :math:`\lambda` are the single dish diameter and observing
        wavelength respectively, and :math:`d` is computed from the provided beam of
        the single dish image via :math:`d = \lambda/\sqrt{\alpha\beta}`. 

        **[NOTE: This is a bit of a fuzzy way of determining the dish diameter, so
        perhaps this is where another input parameter, say dishdiam, should be used
        and required, since then there is no ambiguity of what dish diameter and
        what resolution(s) are being used for the computations, because both would
        be required inputs. There doesn't seem to be data in casa-data which maps
        telescope name to dish diameter, so I'm not sure the dish diameter can
        be easily determined if not specified, short of implementing a long
        conditional block]**

..
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
   
        *sdweight*
   
        Weight to give the Fourier Transform of the single dish image relative to
        the Fourier Transform of the interferometer image. Default is 1.0.
   
   ..
        *effdishdiam*
   
        <Holding off on this for now, since it should in general be implemented by
        convolving the sd image prior to the FT and by not just modifying B. Not
        sure if the convolution is a step that should be hidden from the user.>

        *lowpassfiltersd*
   
        If true, remove high spatial frequencies not sampled from the
        SD FT image by masking pixels that lie beyond (dish diameter)/lambda
        wavelengths from the origin before combining the SD FT image with the
        interferometer FT image. if false, no such masking is performed.

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
        while increasing the intensity scale of the SD image by setting
        sdfactor = 1.2.
   
        ::

            feather(imagename ='feather.im', highres ='synth.im', lowres ='single_dish.im'sdfactor = 1.2)

.. _Development:

Development
   No additional development details


   
