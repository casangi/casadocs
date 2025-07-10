

.. _Description:

Description
   **feather** can be used to combine single-dish and
   interferometric images after they have been separately made.
   The algorithm converts each image to the gridded visibility plane,
   combines them, and reconverts them into a combined image. Each
   image must include a beam shape in its metadata in order for
   feathering to work well. 
   These could be a 'clean beam' for interferometric images, and a
   'primary-beam' for a single-dish image. The two images must have
   the same flux density normalization scale.
 

   In detail, the feathered image, :math:`I^{feather}`, is given by (cf. Rao,
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

   As justification for the form of the first equation, one can consider that
   if the two images are the result of simply splitting an interferometer
   dataset into two pieces, then B=1 and w=1 for all uv-cells (since there is
   no relative *uv*-coverage difference for which to account), and so the
   expression in square brackets simplifies to 
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
                \left(\frac{x\sin\phi - y\cos\phi}{\alpha}\right)^2
                + \left(\frac{x\cos\phi + y\sin\phi}{\beta}\right)^2
            \right]
        \right\}


   and so if :math:`x, y, \alpha`, and :math:`\beta` are measured in radians,
   then, if *u* and *v* are measured in wavelengths

   .. math::

        w \equiv
            \frac{\mathcal{F}(I^{lowres, psf})}{max|\mathcal{F}(I^{lowres, psf})|}
            = exp\left\{
                -\frac{\pi^2}{4ln(2)}\left[
                    \alpha^2\left(u\sin\phi - v\cos\phi\right)^2
                    + \beta^2\left(u\cos\phi + v\sin\phi\right)^2
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

        S = (RMS^{highres}_{Jy/beam}/RMS^{lowres}_{Jy/beam} \times \Omega^{lowres}_{beam}/\Omega^{highres}_{beam})^2

   where the RMSes are in units of Jy/beam and :math:`\Omega_{beam}` denotes the beam area
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

   More information about **feather** can be found in the `Image
   Combination <../../notebooks/image_combination.ipynb#Feather-&-CASAfeather>`__
   section of the CASAdocs.

 Currently, the following constraints are imposed on the two input images:

  * The images must have identical shapes and number of dimensions.
  * The direction coordinates of the two images must be identical.
  * The brightness units of both images should be Jy/beam. If an image has
    another brightness unit (eg K), it is the user's responsibility to convert
    pixel values to Jy/beam and to set the brightness unit to Jy/beam in the
    image metadata. Image pixel values can be manipulated using task immath.
    The brightness unit can be set via task **imhead** or the
    **setbrightnessunit()** method of the image tool.
  * Each image must have a global beam or per-plane beams defined in its
    metadata. Both images may have global beams, per-plane beams, or one image
    may havee a global beam and the other can have per-plane beams. Note that
    the user can add or modify beam information by using **imhead** or the
    **setrestoringbeam()** method of the image tool.
  * Image masks will be ignored and all image pixel values will be used. It
    is suggested that the **replacemaskedpixels()** method of the image tool
    be run on the input images if they have masks prior to running feather,
    setting all masked pixel values to 0.


   In general, it is the responsibility of the user to regrid the
   low resolution image to coincide with the coordinate system of
   the high resolution image and to ensure that the resulting
   regridded image is of reasonable quality to use in **feather**.
   This can be achieved via the **imregrid** task or the
   **regrid()** method of the image tool.
   
   Should absolute scaling be necessary for the flux densities of the two images to
   be equal, this should be addressed prior to running **feather**. One can use task
   **immath** or tool method **image.imagecalc()** to scale the pixel values in an
   image.

  
   There are two feathering implementations from which users can choose. The CASA
   implementation is the default implementation used. It was implemented many years
   ago. The newer method is implmeneted in the astroviper python package. It supports
   multithreading via the dask package and is normally faster than the CASA
   implementation, in some cases at least 
   (the details of CASA to astroviper performance comparisons are not yet well
   determined eg, using various image sizes, various hardware configurations, etc).
   While qualitative agreement between output images from the two implementations
   can be expected, the two implementations are not identical, and so quantitative
   results will likely differ.
   Which implementation is used is determined by the *method* parameter. If set to
   "casa" (the default), the CASA implementation is used. If set to "astroviper",
   the astroviper implementation is used.

   The astroviper package is not included as part of the standard CASA distribution,
   so users must install it and its dependencies separately if they wish to run
   this version of feather. Running

   ``pip install astroviper``

   should suffice. This package and its dependencies require version 3.11, 3.12,
   3.13, or 3.14 of
   python. Additional information on astroviper can be found at 
   https://github.com/casangi/astroviper. In order for astroviper to be used, the
   package and its requirments must be included, implicitly or explicitly, in the
   user environment's python path. This can be done by setting the
   *PYTHONPATH* environment explicitly before starting the python shell, or by using
   a virtual python environment, either via venv or conda. If the environment variable
   route is chosen, the most
   common process is to set this variable on the command line that starts the python
   shell. For example, if the astroviper package is installed in the directory
   /home/user/astroviper, then the following command can be used to start the python
   shell:

   ``PYTHONPATH=/home/user/astroviper python``

   Additional directories in PYTHONPATH can be separated by a colon (:), so that, in
   addition, if CASA is installed in /home/user/casa, then the following command
   can be used to start the python shell:

   ``PYTHONPATH=/home/user/astroviper:/home/user/casa python``

   Note that because of an unresolved issue, which may result from the collision
   beteween CASA and astroviper libraries, feather will launch a subprocess in
   which to run feather. In general this shouldn't be noticed by most users.
   However, this constaint means that, if the user launches a dask client prior
   to calling feather (e.g. via toolviper.dask.local_client()), this client
   will not be used by the subprocess that launches astroviper feather because
   a dask client is tied to the process in which it was started. The launched
   subprocess in which astroviper feather is run will always create its own
   client, configured via the ncores and maxmem feather input parameters.


   Some other input parameters, such
   as *imagename* (the output image name), *highres* (the high
   resolution/interferometer image name), *lowres* (the low resolution/single dish
   image name), and *sdfactor* (the factor by which to scale the single dish image
   flux density) are required and ueed by both implementations. The *effdishdiam*
   (the effective single dish diameter) and *lowpassfiltersd* (indicating it the high
   spatial frequencies of the SD image should be filtered out) input parameters are
   only used by the CASA implementation. The *outformat* (the output image format),
   *cores* (number of cores to use for parallel processing), and *maxmem* (the
   maximum amount of memory to use per core) input parameters are only used by the
   astroviper implementation. 

   Here are examples of how different values of sdfactor may affect the ouput image.

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


   
