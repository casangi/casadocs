Description
      .. rubric:: The 'clean' task will be deprecated in the near future
         - please use tclean instead!
         :name: the-clean-task-will-be-deprecated-in-the-near-future---please-use-tclean-instead

      All major functionality from clean is present in tclean via a
      modified interface along with additional algorithmic options.

       

      .. rubric:: Basics of **clean**
         :name: basics-of-clean

      The CLEAN algorithm (more details available
      `here <https://www.cv.nrao.edu/~abridle/deconvol/node7.html>`__)
      is the most popular and widely-studied method for reconstructing a
      model image based on interferometer data. It iteratively removes
      at each step a fraction of the flux in the brightest pixel in a
      defined region of the current “dirty” image, and places this in
      the model image. The **clean** task implements the CLEAN algorithm
      for single-field data. The user can choose from a number of
      options for the particular flavor of CLEAN to use. Often, the
      first step in imaging is to make a simple gridded Fourier
      inversion of the calibrated data to make a “dirty” image. This can
      then be examined to look for the presence of noticeable emission
      above the noise, and to assess the quality of the calibration by
      searching for artifacts in the image. This is done using **clean**
      with *niter=0*.

      .. note:: **ALERT**: For large fractional bandwidths, the psf in
         **clean** may vary considerably with frequency in data cubes.
         To accommodate this fact we have introduced a per-plane psf
         (dirty beam) when the change is larger than half the size of a
         pixel. Analysis tasks in CASA can deal with such beam
         variation. If a single beam size is requested, **imsmooth** can
         be invoked on the clean products to smooth to a common, uniform
         beam for all channels.

      The **clean** task has many options:

      -  Make 'dirty' image and 'dirty' beam (PSF)
      -  Multi-frequency-continuum images or spectral channel imaging
      -  Full Stokes imaging
      -  Mosaicking of several pointings
      -  Multi-scale cleaning
      -  Widefield cleaning
      -  Interactive clean boxing
      -  Use starting model (e.g. from single-dish)

       

      .. rubric:: *imagermode* parameter
         :name: imagermode-parameter

      CASA supports several methods for data deconvolution and imaging.
      These methods can be set using the parameter *imagermode*, which
      chooses the mode of operation of **clean**, either as single-field
      deconvolution using image-plane major and minor cycles only
      (*imagermode=''*), single-field deconvolution using Cotton-Schwab
      (CS) residual visibilities for major cycles
      (*imagermode='csclean'*), or multi-field mosaics using CS major
      cycles (*imagermode='mosaic'*).

      The default *imagermode='csclean'* choice specifies the
      Cotton-Schwab algorithm (more details available
      `here <https://www.cv.nrao.edu/~abridle/deconvol/node10.html>`__).
      This opens up the following sub-parameters:

      .. note:: | imagermode          =  'csclean'   #  Options: 'csclean' or
           'mosaic'; '', uses psfmode
         |      cyclefactor    =        1.5   #  Controls how often
           major cycles are done. (e.g. 5 for frequently)
         |      cyclespeedup   =         -1   #  Cycle threshold doubles
           in this number of iterations

      In the CS mode, cleaning is split into minor and major cycles. For
      each field, a minor cycle is performed using the PSF algorithm
      specified by the *psfmode* parameter. At major-cycle breakpoints,
      the points thus found are subtracted from the original
      visibilities. A fast variant does a convolution using a FFT (Fast
      Fourier transform). This will be faster for large numbers of
      visibilities. If you want to be extra careful, double the image
      size from that used for the Clark **clean** and set a mask to
      clean only the inner quarter or less (this is not done by
      default). This is probably the best choice for high-fidelity
      deconvolution of images without lots of large-scale structure.

      .. note:: **NOTE**: When using the Cotton-Schwab algorithm with a
         threshold, there may be strange behavior when you hit the
         threshold with a major cycle. In particular, it may be above
         threshold again at the start of the next major cycle. This is
         particularly noticeable when cleaning a cube, where different
         channels will hit the threshold at different times.

      In the empty mode (*imagermode=''*), the major and minor clean
      cycles work off of the gridded FFT dirty image, with residuals
      updated using the PSF calculation algorithm set by the *psfmode*
      parameter. This method is not recommended for high dynamic range
      or high fidelity imaging applications, but can be significantly
      faster than CS clean (the default).

      .. note:: **NOTE**: For this option only, if *mask=''* (no mask or box
         set) then it will clean the inner quarter of the image by
         default.

      .. note:: **ALERT**: You will see a warning message in the logger,
         similar to this:

         .. note:: Zero Pixels selected with a Flux limit of 0.000551377 and a
            maximum Residual of 0.00751239

         whenever it finds 0 pixels above the threshold. This is normal,
         and not a problem if you’ve specified a non-zero threshold. On
         the other hand, if you get this warning with the threshold set
         to the default of '0Jy', then you should look carefully at your
         inputs or your data, since this usually means that the masking
         is bad.

      The option *imagermode='mosaic'* is for multi-field mosaics. This
      choice opens up the following sub-parameters:

      .. note:: | imagermode          =   'mosaic'   #  Use csclean or mosaic. 
           If ’’, use psfmode
         |      mosweight      =      False   #  Individually weight the
           fields of the mosaic
         |      ftmachine      =   'mosaic'   #  Gridding method for the
           image
         |      scaletype      =    'SAULT'   #  Controls scaling of
           pixels in the image plane.
         |      cyclefactor    =        1.5   #  change depth in between
           of  csclean cycle
         |      cyclespeedup   =         -1   #  Cycle threshold doubles
           in this number of iterations

      .. rubric:: *psfmode* parameter
         :name: psfmode-parameter

      The *psfmode* parameter chooses the “algorithm” that will be used
      to calculate the synthesized beam for use during the minor cycles
      in the image plane. There are 3 choices: '*clark*' (default),
      '*hogbom*', and '*clarkstokes*'.

      In the 'clark' algorithm, the cleaning is split into minor and
      major cycles. In the minor cycles only the brightest points are
      cleaned, using a subset of the point spread function. In the major
      cycle, the points thus found are subtracted correctly by using an
      FFT-based convolution. This algorithm is reasonably fast. Also,
      for polarization imaging, Clark searches for the peak in

      :math:`I^2 + Q^2 + U^2 + V^2`.

      The '*hogbom*' algorithm is the “Classic” image-plane CLEAN, where
      model pixels are found iteratively by searching for the peak. Each
      point is subtracted from the full residual image using the shifted
      and scaled point spread function. In general, this is not a good
      choice for most imaging problems (*clark* or *csclean* are
      preferred) as it does not calculate the residuals accurately. But
      in some cases, with poor uv-coverage and/or a PSF with bad
      sidelobes, the Hogbom algorithm will do better as it uses a
      smaller beam patch. For polarization cleaning, Hogbom searches for
      clean peak in I, Q, U, and V independently.

      In the '*clarkstokes*' algorithm, the Clark psf is used, but for
      polarization imaging the Stokes planes are cleaned sequentially
      for components instead of jointly as in '*clark*'. This means that
      this is the same as 'clark' for Stokes I imaging only. This option
      can also be combined with *imagermode='csclean'*.

       

      .. rubric:: Data weighting
         :name: data-weighting

      Data weighting during imaging allows for the improvement of the
      dynamic range and the ability to adjust the synthesized beam
      associated with the produced image. The weight given to each
      visibility sample can be adjusted to fit the desired output. There
      are several reasons to adjust the weighting, including improving
      sensitivity to extended sources or accounting for noise variation
      between samples.The user can adjust the weighting using **clean**
      and changing the *weighting* parameter with six options:
      'natural', 'uniform', 'briggs',  'superuniform', 'briggsabs', and
      'radial'.

      .. rubric:: Natural weighting
         :name: natural-weighting

      For *weighting='natural'*, visibilities are weighted only by the
      data weights, which are calculated during filling and calibration
      and should be equal to the inverse noise variance on that
      visibility. Imaging weight :math:`w_i` of
      sample :math:`\dot\imath` is given by:

      :math:`w_i = \omega_i = \frac{1}{{\sigma_i}^2}`

      where the data weight :math:`\omega_i` is determined from
      :math:`\sigma_i`, the rms noise on visibility :math:`\dot\imath`.
      When data is gridded into the same uv-cell for imaging, the
      weights are summed, and thus a higher uv density results in higher
      imaging weights. No sub-parameters are linked to this mode choice.
      It is the default imaging weight mode, and it should produce
      “optimum” image with with the lowest noise (highest
      signal-to-noise ratio).

      .. note:: **NOTE**: This generally produces images with the poorest
         angular resolution, since the density of visibilities falls
         radially in the uv-plane.

      .. rubric:: Uniform weighting
         :name: uniform-weighting
         :class: nopar

      For *weighting='uniform'*, the data weights are calculated as in
      'natural'weighting. The data is then gridded to a number of cells
      in the uv-plane, and after all data is gridded the uv-cells are
      re-weighted to have “uniform” imaging weights. This pumps up the
      influence on the image of data with low weights (they are
      multiplied up to be the same as for the highest weighted data),
      which sharpens resolution and reduces the sidelobe level in the
      field-of-view, but increases the rms image noise. No
      sub-parameters are linked to this mode choice.

      For uniform weighting, we first grid the inverse variance
      :math:`\omega_i` for all selected data onto a grid with uv
      cell-size given by 2 ∕ FOV,where FOVis the specified field of view
      (defaults to the image field of view). This forms the gridded
      weights :math:`W_k`. The weight of the :math:`\dot\imath`-th
      sample is then:

      :math:`w_i = \frac{w_i}{W_k}`

      .. rubric:: Briggs weighting
         :name: briggs-weighting
         :class: noindent

      The *weighting='briggs'* mode is an implementation of the
      flexible weighting scheme developed by Dan Briggs in his PhD
      thesis, which can be viewed
      `here <http://www.aoc.nrao.edu/dissertations/dbriggs/>`__.

      This choice brings up the sub-parameters:

      .. note:: | weighting      =   'briggs'  
           #   Weighting to apply to visibilities  
         |      robust    =        0.0   #   Briggs robustness parameter
            
         |      npixels   =          0   #   number of pixels to determine uv-cell size 0=> field of view

      The actual weighting scheme used is:

      :math:`w_i = \frac{\omega_i}{1 + W_k f^2}`

       where :math:`W_k` is defined as in 'uniform'and
      'superuniform'weighting, and

      :math:`f^2 = \frac{(5 \times 10^{-\text{R}})^2}{\frac{\Sigma_k W_k^2}{\Sigma_i \omega_i}}`

      and Ris the *robust* sub-parameter.

      The key parameter is the *robust sub-* parameter, which sets Rin
      the Briggs equations. The scaling of Ris such that *robust=0*
      gives a good trade-off between resolution and sensitivity. The
      robustRtakes value between -2.0 (close to uniform weighting) to
      2.0 (close to natural).

      Superuniform weighting can be combined with Briggs weighting using
      the *npixels* sub-parameter. This works as in
      ’superuniform’weighting.

      .. rubric:: Superuniform weighting
         :name: superuniform-weighting
         :class: noindent

      The *weighting='superuniform'* mode is similar to the
      'uniform'weighting mode but there is now an additional
      *npixels* sub-parameter that specifies a change to the number of
      cells on a side (with respect to uniform weighting) to define a
      uv-plane patch for the weighting renormalization. If
      *npixels=0* , you get uniform weighting.

      .. rubric:: Briggsabs weighting
         :name: briggsabs-weighting

      For *weighting='briggsabs'*, a slightly different Briggs weighting
      is used, with:

      :math:`w_i = \frac{\omega_i}{W_k \text{R}^2 + 2\sigma_\text{R}^2}`

      where Ris the *robust* parameter and :math:`\sigma_\text{R}` is
      the *noise* parameter.

      This choice brings up the sub-parameters:

      .. note:: | weighting      = 'briggsabs' 
           #   Weighting to apply to visibilities  
         |      robust    =      0.0     #   Briggs robustness parameter
            
         |      noise     =  '0.0Jy'    
           #   noise parameter for briggs weighting when rmode='abs' 
         |      npixels   =        0     #   number of pixels to determine uv-cell size 0=> field of view

      Otherwise, this works as *weighting='briggs'* above.

      .. rubric:: Radial weighting
         :name: radial-weighting

      The *weighting='radial'* mode is a seldom-used option that
      increases the weight by the radius in the uv-plane, i.e.:

      :math:`w_i = \omega_i \times \sqrt{u_i^2 + v_i^2}`

      Technically, this would be called an inverse uv-taper, since it
      depends on uv-coordinates and not on the data per-se. Its effect
      is to reduce the rms sidelobes for an east-west synthesis array.
      This option has limited utility.

       

      .. rubric:: Output images with parameter *imagename*
         :name: output-images-with-parameter-imagename

      The value of the *imagename* parameter is used as the root name of
      the output image. Depending on the particular task and the options
      chosen, one or more images with names built from that root will be
      created. For example, the **clean** task run with
      *imagename='ngc5921'* a series of output images will be created
      with the names ngc5921.clean, ngc5921.residual, ngc5921.model,
      etc. If an image with that name already exists, it will in general
      be overwritten. Beware using names of existing images however. If
      the **clean** is run using an *imagename* where
      <imagename>.residual and <imagename>.model already exist  then
      **clean** will continue starting from these (effectively
      restarting from the end of the previous **clean**). Thus, if
      multiple runs of **clean** are run consecutively with the same
      *imagename*, then the cleaning is incremental (as in the
      `difmap <https://www.cv.nrao.edu/adass/adassVI/shepherdm.html>`__
      package).

      The output image may also have a different beam per plane. For
      datasets with very large fractional bandwidth, **clean** will use
      a different PSF for each channel when the PSF changes by more than
      half a pixel as a function of frequency. To smooth to a common
      resolution, one can either use the parameter *resmooth* to smooth
      to the smallest common possible beam, *restoringbeam* for an
      arbitrary, larger beam, or the task **imsmooth** after cleaning.
      Data analysis tasks such as **immoments** in CASA support changing
      beams per plane.

      There is some differences between the output images based on the
      algorithm used during a **clean**. The following is a list of
      differences between MS-MFS (*nterms>1*) and standard imaging, in
      the current CASA release:

      #. Iterations always proceed as cs-clean major/minor cycles, and
         uses the full psf during minor cycle iterations. There are
         currently no user-controls on the *cyclespeedup*, and the
         flux-limit per major cycle is chosen as 10% of the peak
         residual. In future releases, this will be made more
         adaptive/controllable.
      #. Currently, the following options are not supported for
         *nterms>1*: *psfmode*, *pbcorr*, *minpb*,
         *imagermode='mosaic'*, *gridmode='aprojection'*,
         *cyclespeedup*, and allowed are one of Stokes I, Q, U, V, RR,
         LL, XX, YY at a time. More options and combinations are
         currently under development and testing. Under 'Using
         CASA'→'Other Documentation'→'Imaging Algorithms in CASA' you
         can find the latest implementations.

       

      .. rubric:: Mosaic imaging
         :name: mosaic-imaging

      The **clean** task contains the capability to image multiple
      pointing centers together into a single “mosaic” image. This
      ability is controlled by setting *imagermode='mosaic'*. The key
      parameter that controls how clean produces the mosaic is the
      *ftmachine* sub-parameter. For *ftmachine='ft'*, clean will
      perform a weighted combination of the images produced by
      transforming each mosaic pointing separately. This can be slow, as
      the individual sub-images must be recombined in the image plane.

      .. note:: **NOTE**: This option is preferred for data taken with
         sub-optimal mosaic sampling (e.g. fields too far apart, on a
         sparse irregular pattern, etc.)

      If *ftmachine='mosaic'*, then the data are gridded onto a single
      uv-plane which is then transformed to produce the single output
      image. This is accomplished by using a gridding kernel that
      approximates the  transform of the primary beam pattern. Note that
      for this mode the <imagename>.flux image includes this convolution
      kernel in its effective weighted response pattern (needed to
      “primary-beam correct” the output image). For this mode only, an
      additional image <imagename>.flux.pbcoverage is produced that is
      the primary-beam coverage only used to compute the *minpb* cutoff.

      The *flatnoise* parameter determines whether the minor cycle
      performs on the the residual with or without a primary beam
      correction. Whereas the former has the correct fluxes, the latter
      has a uniform noise, which allows for a simpler deconvolution in
      particular at the the edges of the mosaic where the primary beam
      correction is largest.

      .. note:: **ALERT**: In order to avoid aliasing artifacts for
         *ftmachine='mosaic'* in the mosaic image, due to the discrete
         sampling of the mosaic pattern on the sky, you should make an
         image in which the desired unmasked part of the image (above
         minpb) lies within the inner quarter. In other words, make an
         image twice as big as necessary to encompass the mosaic.

      It is also important to choose an appropriate *phasecenter* for
      your output mosaic image. The phase center should not be at the
      edge of an image with pointings around it. In that case, FFT
      aliasing may creep into the image.

      .. rubric:: Mosaic *threshold* parameter
         :name: mosaic-threshold-parameter

      For mosaics, the specification of the threshold is not
      straightforward, as it is in the single field case. This is
      because the different fields can be observed to different depths,
      and get different weights in the mosaic. We now provide internal
      rescaling (based on scaletype) so **clean** does its component
      search on a properly weighted and scaled version of the sky. For
      *ftmachine='ft'*, the minor cycles of the deconvolution are
      performed on an image that has been weighted to have constant
      noise, as in 'SAULT' weighting. This is equivalent to making a
      dirty mosaic by coadding dirty images made from the individual
      pointings with a sum of the mosaic contributions to a given pixel
      weighted by so as to give constant noise across the image. This
      means that the flux scale can vary across the mosaic depending on
      the effective noise (higher weighted regions have lower noise, and
      thus will have higher “fluxes” in the 'SAULT' map). Effectively,
      the flux scale that threshold applies to is that at the center of
      the highest-weighted mosaic field, with higher-noise regions
      down-scaled accordingly. Compared to the true sky, this image has
      a factor of the PB, plus a scaling map (returned in the .flux
      image). You will preferentially find components in the low-noise
      regions near mosaic centers. When *ftmachine='mosaic'* and
      *scaletype='SAULT'*, the deconvolution is also performed on a
      “constant noise image”, as detailed above for 'ft'.

      .. note:: **ALERT**: The intrinsic image made using *ftmachine='mosaic'*
         is equivalent to a dirty mosaic that is formed by coadding
         dirty images made from the individual fields after apodizing
         each by the PB function. Thus compared to the true sky, this
         has a factor of the PB 2 in it. You would thus preferentially
         find components in the centers of the mosaic fields (even more
         so than in the 'ft' mosaics). We now rescale this image
         internally at major-cycle (and interactive) boundaries based on
         scaletype, and do not have a way to clean on the raw unscaled
         dirty image (as was done in previous released versions).

       

      .. rubric:: Multi-scale cleaning
         :name: multi-scale-cleaning

      The CASA multi-scale algorithm uses “Multi-scale CLEAN” to
      deconvolve using delta-functions and circular Gaussians as the
      basis functions for the model, instead of just delta-functions or
      pixels as in the other **clean** algorithms. This algorithm is
      still in the experimental stage, mostly because we are working on
      better algorithms for setting the scales for the Gaussians. The
      sizes of the Gaussians are set using the *scales* sub-parameter.

      Multi-scale cleaning is also not as sensitive to the loop gain as
      regular cleaning algorithms. A loop gain of 0.3 may still work
      fine and will considerably speed up the processing time.
      Increasing the cyclefactor by a few may provide better stability
      in the solution, in particular when the data exhibit a severely
      non-Gaussian dirty beam.

      .. note:: **Inside the Toolkit**: The **im.setscales** method sets the
         multi-scale Gaussian widths. In addition to choosing a list of
         sizes in pixels, you can just pick a number of scales and get a
         geometric series of sizes.

      To activate multi-scale mode, specify a non-blank list of scales
      in the *multiscale* parameter. A good rule of thumb for starters
      is [ 0, 2xbeam, 5xbeam ], and maybe adding larger scales up to the
      maximum scale the interferometer can image. E.g. for a 2 arcsecond
      beam:

      .. note:: multiscale = [0,6,10,30] # Four scales including point sources

      These are given in numbers of pixels, and specify FWHM of the
      Gaussians used to compute the filtered images. Setting the
      *multiscale* parameter to a non-empty list opens up the
      sub-parameter:

      .. note:: | multiscale = [0, 6, 10, 30]  # set deconvolution scales
           (pixels)    
         |      negcomponent = -1       # Stop cleaning if the
         |                              # largest scale finds this
           number of neg
         |                              # components
         |      smallscalebias = 0.6    # a bias to give more weight
         |                              # toward smaller scales

      The *negcomponent* sub-parameter is here to set the point at which
      the **clean** terminates because of negative components. For
      *negcomponent > 0*, component search will cease when this number
      of negative  components are found at the largest scale. If
      *negcomponent = -1,* then component search will continue even if
      the largest component is negative. Increasing *smallscalebias*
      gives more weight to small scales. A value of 1.0 weighs the
      largest scale to zero and a value < 0.2 weighs all scales nearly
      equally. The default of 0.6 is usually a good number as it
      corresponds to a weighting that approximates the normalization of
      each component by its area. Depending on the image, however, it
      may be necessary to tweak the *smallscalebias* for a better
      convergence of the algorithm.

      .. note:: **NOTE**: Currently *smallscalebias* is ignored by the MS-MFS
         algorithm. It will be available in a future release.

      .. rubric:: MS-MFS Algorithm
         :name: ms-mfs-algorithm

      The MS-MFS (multiscale-multifrequency synthesis) algorithm
      combines the concepts of multi-scale and multi-frequency synthesis
      cleaning for wideband synthesis imaging. Setting the *mode='mfs'*
      sub-parameter *nterms>1* runs the MS-MFS algorithm, and the choice
      of *nterms* should depend on the expected shape and SNR of the
      spectral structure, across the chosen bandwidth. The MS-MFS
      algorithm requires the *multiscale* parameter to be set. For
      point-source deconvolution, set *multiscale=[0]* (also the
      default). Output images represent Taylor-coefficients of the sky
      spectrum (images with file-name extensions of tt0,tt1,etc). A
      spectral index map is also computed as the ratio of the first two
      terms, following this convention:

      :math:`I(\nu) = I(ref_\nu) \times  (\nu/\nu_0)^\alpha`

      .. note:: **NOTE**: Unlike standard multi-scale cleaning (*multiscale=
         [0,6,10,....]* with *nterms=1*), with higher nterms the largest
         specified scale size must lie within the sampled range of the
         interferometer. If not, there can be an ambiguity in the
         spectral reconstruction at very large spatial scales.

      Additionally, a spectral-index error image is made by treating
      Taylor-coefficient residuals as errors, and propagating them
      through the division used to compute spectral-index. It is meant
      to be a guide to which parts of the spectral-index image to trust,
      and the values may not always represent a statistically-correct
      error. For more details about this algorithm, please refer to the
      paper titled "A multi-scale multi-frequency deconvolution
      algorithm for synthesis imaging in radio interferometry"
      `[1] <#cit1>`__ .

      .. note:: **NOTE**: The software implementation of the MS-MFS algorithm
         for *nterms>1* currently does not allow combination with
         mosaics and pbcor.

       

      .. rubric:: Polarization Imaging
         :name: polarization-imaging

      The *stokes* parameter specifies the Stokes parameters for the
      resulting images, with standard imaging only using the
      *stokes='I'* for the total intensity measurement.

      .. note:: **NOTE**: Forming Stokes Q and U images requires the presence
         of cross-hand polarizations (e.g. RL and LR for circularly
         polarized systems such as the VLA) in the data. Stokes V
         requires both parallel hands (RR and :LL) for circularly
         polarized systems or the cross-hands (XY and YX) for linearly
         polarized systems such as ALMA and ATCA.

      This parameter is specified as a string of up to four letters and
      can indicate stokes parameters themselves, Right/Left hand
      polarization products, or linear polarization products (X/Y). For
      example,

      .. note:: | stokes = 'I' # Intensity only
         | stokes = 'IQU' # Intensity and linear polarization
         | stokes = 'IV' # Intensity and circular polarization
         | stokes = 'IQUV' # All Stokes imaging
         | stokes = 'RR' # Right hand polarization only
         | stokes = 'XXYY' # Both linear polarizations

      are common choices (see the inline help of **clean** for a full
      range of possible options). The output image will have planes
      (along the “polarization axis”) corresponding to the chosen Stokes
      parameters. If as input to deconvolution tasks such as **clean**,
      the *stokes* parameter includes polarization planes other than I,
      then choosing *psfmode='hogbom'* or *psfmode='clarkstokes'* will
      **clean** (search for components) each plane sequentially, while
      *psfmode='clark'* will deconvolve jointly.

      .. note:: **ALERT**: As of Release 3.2, **clean** expects that all input
         polarizations are present. E.g. if you have RR and LL dual
         polarization data and you flagged parts of RR but not LL,
         **clean** will ignore both polarizations in slice. It is
         possible to split out a polarization product with **split** and
         image separately. But you will not be able to combine these
         part-flagged data in the uv-domain. We will remove that
         restriction in a future CASA release.

       

      .. rubric:: Hints on **clean** with flanking fields
         :name: hints-on-clean-with-flanking-fields

      | There are two ways of specifying multi-field images for clean:
        (a) the task parameters are used to define the first (main)
        field and a text file containing definitions of all additional
        fields is supplied to the outlierfile task parameter, or (b) all
        fields are specified as lists for each task parameter.
      | For the first example, the outlier file must contain the
        following parameters per field: *imagename*, *imsize*, and
        *phasecenter*. Optional parameters include *mask* and
        *modelimage*. The parameter set for each field must begin with
        *imagename*. Parameters can be listed in a single line or span
        multiple lines. The task inputs are:

      .. note:: | imagename = 'M1_0'
         | outlierfile='outlier.txt'
         | imsize = [1024,1024]
         | phasecenter = 'J2000 13h27m20.98 43d26m28.0'

       The contents of outlier file 'outlier.txt' are:

      ::

         imagename = 'M1_1'
         imsize = [128,128]
         phasecenter = 'J2000 13h30m52.159 43d23m08.02'
         mask = ['out1.mask', 'circle[[40pix,40pix],5pix]' ]
         modelimage = 'out1.model'
         imagename = 'M1_2'
         imsize = [128,128]
         phasecenter = 'J2000 13h24m08.16 43d09m48.0'

      | In this example, the first field 'M1_0' is defined using main
        task parameters. The next two 'M1_1' and 'M1_2' are listed in
        the file 'outlier.txt'.  A *mask* and *modelimage* has been
        supplied only for the second field (M1_1). Fields with
        unspecified masks will use the full field for cleaning.
      | For the second example, the inputs are instead included in the
        main parameters, using brackets to signify multiple inputs.
        Parameters that support lists for multi-field specification are
        *imagename*, *imsize*, *phasecenter*, *mask*, and *modelimage*.
        The task inputs are:

      .. note:: | imagename = ['M1_0','M1_1','M1_2]
         | imsize = [[1024,1024],[128,128],[128,128]]
         | phasecenter = ['J2000 13h27m20.98 43d26m28.0',
         |                        'J2000 13h30m52.159 43d23m08.02',
         |                        'J2000 13h24m08.16 43d09m48.0']
         | mask=[[''], ['out1.mask','circle[[40pix,40pix],5pix]'],['']]
         | modelimage=[[''],['out1.model'],['']]

      .. note:: **NOTE**: All lists must have the same length.

      In both examples, the following images will be made:

      -  M1_0.image, M1_1.image, M1_2.image (cleaned images)
      -  M1.0.model, M1_1.model, M1_2.model (model images)
      -  M1.0.residual, M1_1.residual, M1_2.residual (residual images)

      .. note:: **NOTE**: The old AIPS-style outlier-file and boxfile formats
         have been deprecated. However, due to user-requests, they will
         continue be supported in CASA 3.4. Note that the old outlier
         file format does not support the specification of modelimage
         and mask for each field. The new format is more complete, and
         less ambiguous, so please consider updating your scripts.

       

      .. rubric:: Parameters
         :name: parameters

      .. rubric:: *vis*
         :name: vis

      Name(s) of input visibility file(s). default: none; example:
      *vis='ngc5921.ms'*; *vis=['ngc5921a.ms','ngc5921b.ms']*; multiple
      MSes

      .. rubric:: *imagename*
         :name: imagename

      Pre-name of output images.

          default: none; example: *imagename='m2'*

          Output images are:

      -  m2.image; cleaned and restored image with or without primary
         beam correction
      -  m2.psf; point-spread function (dirty beam)
      -  m2.flux;  relative sky sensitivity over field
      -  m2.flux.pbcoverage;  relative pb coverage over field (gets
         created only for *ft='mosaic'*)
      -  m2.model; image of clean components
      -  m2.residual; image of residuals
      -  m2.interactive.mask; image containing clean regions  

           To include outlier fields:
      imagename=['n5921','outlier1','outlier2']

      .. rubric:: *outlierfile*
         :name: outlierfile

      Text file name which contains image names, sizes, field centers
      (See 'HINTS ON CLEAN WITH FLANKING FIELDS' above for the format of
      this outlier file.)

      .. rubric:: *field*
         :name: field

      Select fields to image or mosaic.  Use field ID(s) or name(s).
      ['go listobs' to obtain the list id's or names]

      |     default: '' all fields; If field string is a non-negative
        integer, it is assumed to be a field index otherwise, it is
        assumed to be a field name
      |     examples: *field='0~2'*; field IDs 0,1,2
      |                        *field='0,4,5~7'*; field IDs 0,4,5,6,7
      |                        *field='3C286,3C295'*; field named 3C286
        and 3C295
      |                        *field = '3,4C*'*; field id 3, all names
        starting with 4C
      |     For multiple MS input, a list of field strings can be used:
      |                        *field = ['0~2','0~4']*; field IDs 0-2
        for the first MS and 0-4 for the second
      |                        *field = '0~2'*; field IDs 0-2 for all
        input MSes

      .. rubric:: *spw*
         :name: spw

      Select spectral window/channels

      .. note:: **NOTE**:  Channels de-selected here will contain all zeros if
         selected by the parameter *mode* subparameters.

      |     default: '' all spectral windows and channels
      |     examples: *spw='0~2,4'*; spws 0,1,2,4 (all channels)
      |                        *spw='0:5~61'*; spw 0, channels 5 to 61
      |                        *spw='<2'*;   spws less than 2 (i.e. 0,1)
      |                        *spw='0,10,3:3~45'*; spw 0,10 all
        channels, spw 3, channels 3 to 45.
      |                        *spw='0~2:2~6'*; spw 0,1,2 with channels
        2 through 6 in each.
      |     For multiple MS input, a list of spw strings can be used:
      |                        *spw=['0','0~3']*; spw ids 0 for the
        first MS and 0-3 for the second
      |                        *spw='0~3'* spw ids 0-3 for all input MS
      |                        *spw='3:10~20;50~60'* for multiple
        channel ranges within spw id 3
      |                        *spw='3:10~20;50~60,4:0~30'* for
        different channel ranges for spw ids 3 and 4
      |                        *spw='0:0~10,1:20~30,2:1;2;3'*; spw 0,
        channels 0-10, spw 1, channels 20-30, and spw 2, channels, 1,2
        and 3
      |                        *spw='1~4;6:15~48'* for channels 15
        through 48 for spw ids 1,2,3,4 and 6

      .. rubric:: *selectdata*
         :name: selectdata

      | Other data selection parameters
      |     default: True

      .. rubric::     selectdata=True expandable parameters (See help
         par.selectdata for more on these)
         :name: selectdatatrue-expandable-parameters-see-help-par.selectdata-for-more-on-these

      .. rubric::     *timerange*
         :name: timerange

      |     Select data based on time range:
      |         default: '' (all)
      |         examples: *timerange =
        'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'*

      .. note:: **NOTE**: If YYYY/MM/DD is missing, date defaults to first day
         in data set.

      |                           *timerange='09:14:0~09:54:0'* picks 40
        min on first day
      |                           *timerange='25:00:00~27:30:00'* picks
        1 hr to 3 hr 30min on NEXT day
      |                           *timerange='09:44:00'* pick data
        within one integration of time
      |                           *timerange='>10:24:00'* data after
        this time
      |         For multiple MS input, a list of timerange strings can
        be used:
      |                          
        *timerange=['09:14:0~09:54:0','>10:24:00']*
      |                           *timerange='09:14:0~09:54:0'*; apply
        the same timerange for all input MSes
      |                   

      .. rubric::     *uvrange*
         :name: uvrange

      |     Select data within uvrange (default units meters)
      |         default: '' (all)
      |         example: *uvrange='0~1000klambda'*; uvrange from 0-1000
        kilo-lambda
      |                          *uvrange='>4klambda'*;uvranges greater
        than 4 kilo lambda
      |         For multiple MS input, a list of uvrange strings can be
        used:
      |                         
        *uvrange=['0~1000klambda','100~1000klamda']*
      |                          *uvrange='0~1000klambda'*; apply 0-1000
        kilo-lambda for all input MSes

      .. rubric:: 
             *antenna*
         :name: antenna

      |     Select data based on antenna/baseline
      |         default: '' (all)
      |         If antenna string is a non-negative integer, it is
        assumed to be an antenna index, otherwise, it is considered an
        antenna name.
      |                        *antenna='5&amp;6'*; baseline between
        antenna index 5 and index 6.
      |                        *antenna='VA05&amp;VA06'*; baseline
        between VLA antenna 5 and 6.
      |                        *antenna='5&amp;6;7&amp;8'*; baselines
        5-6 and 7-8
      |                        *antenna='5'*; all baselines with antenna
        index 5
      |                        *antenna='05'*; all baselines with
        antenna number 05 (VLA old name)
      |                        *antenna='5,6,9'*; all baselines with
        antennas 5,6,9 index number
      |         For multiple MS input, a list of antenna strings can be
        used:
      |                        *antenna=['5','5&amp;6']*;
      |                        *antenna='5'*; antenna index 5 for all
        input MSes

      .. rubric:: 
             *scan*
         :name: scan

      |     Scan number range. [Check 'go listobs' to insure the scan
        numbers are in order.]
      |         default: '' (all)
      |         examples: *scan='1~5'*
      |         For multiple MS input, a list of scan strings can be
        used:
      |                            *scan=['0~100','10~200']*
      |                            *scan='0~100*; scan ids 0-100 for all
        input MSes
      |                       

      .. rubric::     *observation*
         :name: observation

      |     Observation ID range.
      |         default: '' (all); example: *observation='1~5'*

      .. rubric:: 
             *intent*
         :name: intent

      |     Scan intent (case sensitive)
      |         default: '' (all); examples: *intent='TARGET_SOURCE',
        intent='TARGET_SOURCE1,TARGET_SOURCE2',
        intent='TARGET_POINTING*'*

      .. rubric:: *mode:* Frequency Specification
         :name: mode-frequency-specification

      .. note:: **NOTE**: Channels deselected with spw parameter will contain
         all zeros.

          default: 'mfs'; examples: *mode = 'mfs'* means produce one
      image from all specified data, *mode = 'channel'* use with nchan,
      start, width to specify output image cube, *mode = 'velocity'*
      channels are specified in velocity, *mode = 'frequency'*, channels
      are specified in frequency.

      .. rubric::     mode='mfs' expandable parameters
         :name: modemfs-expandable-parameters

      |     Make a continuum image from the selected frequency
        channels/range using Multi-frequency synthesis algorithm for
        wide-band narrow field imaging.  
      |     examples: *spw = '0,1'*; *mode = 'mfs'* will produce one
        image made from all channels in spw 0 and 1
      |                        *spw='0:5~28^2'*; *mode = 'mfs'* will
        produce one image made with channels (5,7,9,...,25,27)

      .. rubric::     *nterms*
         :name: nterms

          Number of Taylor terms to be used to model the frequency
      dependence of the sky emission. nterms=1 is equivalent to assuming
      no frequency dependence. nterms>1 runs the MS-MFS algorithm, and
      the choice of nterms should depend on the expected shape and SNR
      of the spectral structure, across the chosen bandwidth. Output
      images represent taylor-coefficients of the sky spectrum (images
      with file-name extensions of tt0,tt1,etc). A spectral index map is
      also computed as the ratio of the first two terms (following the
      convention of :math:`I(nu) = I(ref_nu) x (nu/nu_0)^\alpha`).
      Additionally, a spectral-index error image is made by treating
      taylor-coefficient residuals as errors, and propagating them
      through the division used to compute spectral-index. It is meant
      to be a guide to which parts of the spectral-index image to trust,
      and the values may not always represent a statistically-correct
      error.

      .. note:: **NOTE**: The software implementation of the MS-MFS algorithm
         for *nterms>1* currently does not allow combination with
         mosaics, and *pbcor*.

      .. rubric::     *reffreq*
         :name: reffreq

      |     The reference frequency (for nterms>1) about which the
        Taylor expansion if done.
      |                    *reffreq=''* defaults to the middle frequency
        of the selected range.
      |    

      .. rubric::     mode='channel', 'velocity', and 'frequency'
         expandable parameters
         :name: modechannel-velocity-and-frequency-expandable-parameters

      .. rubric::     *nchan*
         :name: nchan

      |     Total number of channels in the output image.
      |         default: -1; Automatically selects enough channels to
        cover data selected by 'spw' consistent with 'start' and
        'width'. It is often easiest to leave nchan at the default
        value. example: *nchan=100*.

      .. rubric::     *start*
         :name: start

      |     First channel, velocity, or frequency.
      |          For *mode='channel'*; This selects the channel index
        number from the MS (0 based) that you want to correspond to the
        first channel of the output cube. The output cube will be in
        frequency space with the first channel having the frequency of
        the MS channel selected by *start*.  *start=0* refers to the
        first channel in the first selected spw, even if that channel is
        de-selected in the *spw* parameter. Channels de-selected by the
        *spw* parameter will be filled with zeros if included by the
        *start* parameter. For example, *spw=3~8:3~100* and *start=2*
        will produce a cube that starts on the third channel (recall 0
        based) of spw index 3, and the first channel will be blank.
        example: *start=5*
      |          For *mode='velocity'* or *'frequency'*: default='';
        starts at first input channel of first input spw; examples:
        *start='5.0km/s'* or *start='22.3GHz'*

      .. rubric::     *width*
         :name: width

      |     Output channel width
      |          For *mode='channel'*, default=1; >1 indicates channel
        averaging; example: *width=4*
      |          For *mode= 'velocity'* or *'frequency'*, default='';
        width of first input channel, or more precisely, the difference
        in frequencies between the first two selected channels. For
        example, if channels 1 and 3 are selected with *spw*, then the
        default width will be the difference between their frequencies,
        and not the width of channel 1. Similarly, if the selected data
        has uneven channel-spacing, the default width will be picked
        from the first two selected channels. In this case, please
        specify the desired width. When specifying the width, one must
        give units. examples: *width='1.0km/s'*, or *width='24.2kHz'*.
        Setting *width>0* gives channels of increasing frequency for
        *mode='frequency'*, and increasing velocity for
        *mode='velocity'*.

      .. rubric::     *interpolation*
         :name: interpolation

      |     Interpolation type for spectral gridding onto the uv-plane.
        Options: 'nearest', 'linear', or 'cubic'.
      |         default = 'linear'

      .. note:: **NOTE**: 'linear' and 'cubic' interpolation requires data
         points on both sides of each image frequency. Errors are
         therefore possible at edge channels, or near flagged data
         channels. When image channel width is much larger than the data
         channel width there is nothing much to be gained using linear
         or cubic thus not worth the extra computation involved.

      .. rubric::     *resmooth*
         :name: resmooth

      |     If the cube has a different restoring beam/channel. Restore
        image to a common beam or leave as is; (default) options: True
        or False
      |         default = False

      .. rubric::     *chaniter*
         :name: chaniter

      |     Specify how spectral CLEAN is performed,
      |         default: *chaniter=False*; example: *chaniter=True*;
        step through channels

      .. rubric::     *outframe*
         :name: outframe

      |     For *mode='velocity'*, 'frequency', or 'channel': default
        spectral reference frame of output image; Options:
        '','LSRK','LSRD','BARY','GEO','TOPO','GALACTO', ''LGROUP','CMB'
      |         default: ''; same as input data; example: *frame='bary'*
        for Barycentric frame

      .. rubric::     *veltype*
         :name: veltype

      |     For *mode='velocity'* gives the velocity definition; 
        Options: 'radio','optical'
      |         default: 'radio'

      .. note:: **NOTE**: The viewer always defaults to displaying the 'radio'
         frame, but that can be changed in the position tracking pull
         down.

      |     *mode='channel'* examples:
      |         *spw = '0'*; *mode = 'channel'*: *nchan=3*; *start=5*;
        *width=4* will produce an image with 3 output planes: plane 1
        contains data from channels (5+6+7+8), plane 2 contains data
        from channels (9+10+11+12), plane 3 contains data from channels
        (13+14+15+16)
      |         *spw = '0:0~63^3'*; *mode='channel'*; *nchan=21*; *start
        = 0*; *width = 1* will produce an image with 20 output planes:
        plane 1 contains data from channel 0, plane 2 contains date from
        channel 2, plane 21 contains data from channel 61
      |         *spw = '0:0~40^2'*; *mode = 'channel'*; *nchan = 3*;
        *start = 5*; *width = 4* will produce an image with three output
        planes: plane 1 contains channels (5,7), plane 2 contains
        channels (13,15), plane 3 contains channels (21,23)

       

      .. rubric:: *psfmode*
         :name: psfmode

      | method of PSF calculation to use during minor cycles:
      |     default: 'clark': Options: 'clark','clarkstokes', 'hogbom'
      |          'clark'  use smaller beam (faster, usually good
        enough); for stokes images clean components peaks are searched
        in the I^2+Q^2+U^2+V^2 domain
      |          'clarkstokes' locate clean components independently in
        each stokes image
      |          'hogbom' full-width of image (slower, better for poor
        uv-coverage)

      .. note:: **NOTE**:  *psfmode* will also be used to clean if *imagermode
         = ''*.

      .. rubric:: *imagermode*
         :name: imagermode

      | Advanced imaging e.g. mosaic or Cotton-Schwab clean
      |     default: *imagermode='csclean'*: Options: '', 'csclean',
        'mosaic'
      |          ''  => psfmode cleaning algorithm used

      .. note:: **NOTE**: *imagermode* 'mosaic' (and/or) any *gridmode* not
         blank (and/or) *nterms>1* : will always use CS style clean.

      .. rubric:: *    imagermode='mosaic'* expandable parameter(s)
         :name: imagermodemosaic-expandable-parameters

          Make a mosaic of the different pointings (uses csclean style
      too)

      .. rubric::     *mosweight*
         :name: mosweight

          Individually weight the fields of the mosaic. Default:
      *mosweight = False*; Example: *mosweight = True*, this performs
      the weight density calculation for each field indepedently when
      using Briggs (including uniform) weighting. This can be useful if
      some of your fields are more sensitive than others (i.e. due to
      time spent on-source) or if you have relatively poor uv-coverage
      (e.g., snap-shot). If *False*, the weight density is calculated
      from the average uv distribution of all the fields.

      .. rubric::     *ftmachine*
         :name: ftmachine

          Gridding method for the mosaic; Options: 'mosaic' , 'ft' or
      'wproject'. default: 'mosaic'; 'ft' or 'wproject' implies standard
      interferometric 2D or widefield gridding. The residual
      visibilities are imaged for each pointing and combined in the
      image plane with the appropriate PB to make the mosaic. 'mosaic'
      (grid using the Fourier transform of PB as convolution function
      and mosaic combination is done in visibilities). ONLY if
      *imagermode='mosaic'* is chosen and *ftmachine='mosaic'*, is
      heterogeneous imaging (CARMA, ALMA) or wideband beam accounting
      possible using the right convolution derived from primary beams
      for each baseline and for different frequencies

      .. note:: **NOTE**: *ftmachine='mosaic'* uses Fourier transforms of the
         primary beams/pointing for mosaicing. Making an image which is
         too small for the pointing coverages will cause aliasing due to
         standard Fourier transform wrap around.

      .. rubric::     *scaletype*
         :name: scaletype

          Controls scaling of pixels in the image plane. (controls what
      is seen if *interactive=True*) It does \*not\* affect the scaling
      of the \*final\* image that is done by *pbcor*. default='SAULT';
      example: *scaletype='PBCOR'*; Options: 'PBCOR','SAULT'. 'SAULT'
      when *interactive=True* shows the residual with constant noise
      across the mosaic. Can also be achieved by setting *pbcor=False*.
      'PBCOR' uses the SAULT scaling scheme for deconvolution, but if
      *interactive=True* shows the primary beam corrected image during
      interactive.

      .. rubric::     *cyclefactor*
         :name: cyclefactor

          Controls the threshhold at which the deconvolution cycle will
      pause to degrid and subtract the model from the visibilities. With
      poor PSFs, reconcile often (*cyclefactor=4* or *5*) for
      reliability. With good PSFs, use *cyclefactor = 1.5* to *2.0* for
      speed.               

      .. note:: **NOTE**: *threshold* = *cyclefactor* \* max sidelobe \* max
         residual

              default: 1.5; example: *cyclefactor=4*

      .. rubric::     *cyclespeedup*
         :name: cyclespeedup

      |     The major cycle threshold doubles in this number of
        iterations.
      |         default: -1 (no doubling); example: *cyclespeedup=3*;
        Try *cyclespeedup = 50* to speed up cleaning.

      .. rubric::     flatnoise
         :name: flatnoise

          Controls whether searching for clean components is done in a
      constant noise residual image (True) or in an optimal
      signal-to-noise residual image (False) when *ftmosaic='mosaic'* is
      chosen. default=True

      .. rubric::    imagermode='csclean' expandable parameter(s)
         :name: imagermodecsclean-expandable-parameters

          Image using the Cotton-Schwab algorithm in between major
      cycles.

      .. rubric::     *cyclefactor*
         :name: cyclefactor-1

          See above, under *imagermode='mosaic'*.

      .. rubric::     *cyclespeedup*
         :name: cyclespeedup-1

          See above, under *imagermode='mosaic'*.

       

      .. rubric:: *gridmode*
         :name: gridmode

      This parameter is now provided to access more advanced
      deconvolution capabilities.

      .. rubric::     gridmode='' expandable parameters
         :name: gridmode-expandable-parameters

          The default value of '' has no effect.

      .. rubric::     gridmode='widefield' expandable parameters
         :name: gridmodewidefield-expandable-parameters

          Apply corrections for non-coplanar effects during imaging
      using the W-Projection algorithm `[2] <#cit2>`__ or faceting or a
      combination of the two.

      .. rubric::     *wprojplanes*
         :name: wprojplanes

          The number of pre-computed w-planes used for the W-Projection
      algorithm. *wprojplanes=1* disables correction for non-coplanar
      effects. default value *wprojpanes=-1* means **clean** will
      determine the number to use.

      .. rubric::     *facets*
         :name: facets

          The number of facets on each side of the image (i.e. the total
      number of facets is 'facets x facets'). If wprojplanes>1,
      W-Projection is done for each facet. Usually when many wprojection
      convolution functions sizes are  above ~400 pixels, it might be
      faster to use a few facets with wprojection.

      .. rubric::     gridmode='aprojection' expandable parameters
         :name: gridmodeaprojection-expandable-parameters

          Corrects for the (E)VLA time-varying PB effects including
      polarization squint using the A-Projection algorithm
      `[3] <#cit3>`__. This can optinally include w-projection also.

      .. rubric::     *wprojplanes*
         :name: wprojplanes-1

          The number of pre-computed w-planes used for W-Projection
      algorithm. *wprojplanes=1* disables correction for non-coplanar
      effects.

      .. rubric::     *cfcache*
         :name: cfcache

          The name of the directory to store the convolution functions
      and weighted sensitivty pattern function. These functions can be
      reused again if the image parameters are unchanged. If the image
      parameters change, a new cache must be created (or the existing
      one removed).

      .. rubric::     *rotpainc*
         :name: rotpainc

          The Parallactic Angle increment (in degrees) used for OTF
      rotation of the convolution function.

      .. rubric::     *painc*
         :name: painc

      | *   * The Parallactic Angle increment (in degrees) used to
        compute the convolution functions *.*
      |  

      .. rubric:: *multiscale*
         :name: multiscale

      set of scales to use in deconvolution. If set, cleans with several
      resolutions using Hogbom clean. The scale sizes are in units of
      cellsize. So if *cell='2arcsec'*, a multiscale *scale=10* =>
      20arcsec. The first scale is recommended to  be 0 (point), we
      suggest the second be on the order of synthesized beam, the third
      3-5 times the synthesized beam, etc.. Avoid making the largest
      scale too large relative to the image width or the scale of the
      lowest measured spatial frequency.  For example, if the
      synthesized beam is 10" FWHM and *cell='2',* try *multiscale =
      [0,5,15]*. default: *multiscale=[]* (standard **clean** with
      psfmode algorithm, no multi-scale). Example: *multiscale =
      [0,5,15]*

      .. rubric::     multiscale expandable parameter(s)
         :name: multiscale-expandable-parameters

      .. rubric::     *negcomponent*
         :name: negcomponent

          Stop component search when the largest scale has found this
      number of negative components; -1 means continue component search
      even if the largest component is negative. default: -1; example:
      *negcomponent=50*

      .. rubric::     *smallscalebias*
         :name: smallscalebias

          A bias toward smaller scales. The peak flux found at each
      scale is weighted by a factor = 1 -
      smallscalebias*scale/max_scale, so that Fw = F*factor. Typically
      the values range from 0.2 to 1.0. default: 0.6

       

      .. rubric:: *imsize*
         :name: imsize

      Image size in pixels (x, y). DOES NOT HAVE TO BE A POWER OF 2 (but
      has to be even and factorizable to 2,3,5,7 only). default =
      [256,256]; examples: *imsize=[350,350]*, *imsize = 500* is
      equivalent to [500,500]. If include outlier fields, e.g.,
      [[400,400],[100,100]] or use *outlierfile*. Avoid odd-numbered
      imsize.

      .. rubric:: *cell*
         :name: cell

      Cell size (x,y). default= '1.0arcsec'; examples:
      *cell=['0.5arcsec,'0.5arcsec']*, *cell=['1arcmin', '1arcmin']*,
      *cell = '1arcsec'* is equivalent to ['1arcsec','1arcsec'], *cell =
      2.0* is equivalent to ['2arcsec', '2arcsec']

      .. rubric:: *phasecenter*
         :name: phasecenter

      Direction measure or fieldid for the mosaic center. default: '' =
      first field selected; examples: *phasecenter=6, phasecenter='J2000
      19h30m00 -40d00m00', phasecenter='J2000 292.5deg  -40.0deg',
      phasecenter='J2000 5.105rad  -0.698rad'*. If include outlier
      fields, e.g. ['J2000 19h30m00 -40d00m00',J2000 19h25m00
      -38d40m00'] or use *outlierfile*.

      .. rubric:: *restfreq*
         :name: restfreq

      Specify rest frequency to use for output image. default=''
      Occasionally it is necessary to set this (for example some VLA
      spectral line data). For example, for NH_3 (1,1) put
      *restfreq='23.694496GHz'*

      .. rubric:: *stokes*
         :name: stokes

      Stokes parameters to image. default='I'; example: *stokes='IQUV'*;
      Options:
      'I','Q','U','V','IV','QU','IQ','UV','IQU','IUV','IQUV','RR','LL','XX','YY','RRLL','XXYY'

      .. rubric:: *niter*
         :name: niter

      Maximum number iterations. If *niter=0*, then no cleaning is done
      ("invert" only). (*niter=0* can be used instead of the 'ft' task
      to predict/save a model) For cube or multi field images, *niter*
      is the maximum number of iteration **clean** will use for each
      image plane. The number of iterations used may be less that
      *niter* if *threshold* value is reached. default: 500; example:
      *niter=5000*

      .. rubric:: *gain*
         :name: gain

      Loop gain for CLEANing. default: 0.1; example: *gain=0.5*

      .. rubric:: *threshold*
         :name: threshold

      Flux level at which to stop CLEANing. default: '0.0mJy'; examples:
      *threshold='2.3mJy'*  (always include units), *threshold =
      '0.0023Jy', threshold = '0.0023Jy/beam'* (okay also)

      .. rubric:: *interactive*
         :name: interactive

      | Use interactive **clean** (with GUI viewer). Interactive
        **clean** allows the user to build the cleaning mask
        interactively using the viewer. The viewer will appear every
        *npercycle* interation, but modify as needed. The final
        interactive mask is saved in the file
        imagename_interactive.mask. The initial masks use the union of
        mask and cleanbox (see below). default: *interactive=False*;
        example: *interactive=True*
      |    

      .. rubric::     interactive=True expandable parameters
         :name: interactivetrue-expandable-parameters

      .. rubric::     *npercycle*
         :name: npercycle

          This is the number of iterations between each interactive
      update of the mask. It is important to modify this number
      interactively during the cleaning, starting with a low number like
      20, but then increasing as more extended emission is encountered.

      .. rubric::     *mask*
         :name: mask

          Specification of cleanbox(es), mask image(s), primary beam
      coverage level, and/or region(s) to be used for cleaning.
      **clean** tends to perform better, and is less likely to diverge,
      if the **clean** component placement is limited by a mask to where
      real emission is expected to be. As long as the image has the same
      shape (size), mask images (e.g. from a previous interactive
      session) can be used for a new execution. 

      .. note:: **NOTE**: The initial clean mask actually used is the union of
         what is specified in mask and <imagename>.mask.

      |         default: [] or '' : no masking; Possible specification
        types:
      |             (a) Cleanboxes, specified using the CASA region
        format
        (http://casaguides.nrao.edu/index.php?title=CASA_Region_Format)
      |             examples: *mask='box [ [ 100pix , 130pix] , [120pix,
        150pix ] ]'*, *mask='circle [ [ 120pix , 40pix] ,6pix ]'*,
        *mask='circle[[19h58m52.7s,+40d42m06.04s ], 30.0arcsec]'*
      |             If used with a spectral cube, it will apply to all
        channels.
      |             Multiple regions may be specified as a list of pixel
        ranges.
      |             examples: *mask= ['circle [ [ 120pix , 40pix] ,6pix
        ]', 'box [ [ 100pix , 130pix] , [120pix, 150pix ] ]' ]*
      |             (b) Filename with cleanbox shapes defined using the
        CASA region format.
      |             example: *mask='mycleanbox.txt';* The file
        'mycleanbox.txt' contains:

      ::

         box [ [ 100pix , 130pix ] , [ 120pix, 150pix ] ]
         circle [ [ 150pix , 150pix] ,10pix ]
         rotbox [ [ 60pix , 50pix ] , [ 30pix , 30pix ] , 30deg ]

      |              (c) Filename for image mask. example:
        *mask='myimage.mask'*
      |              Multiple mask files may be specified.
      |              example: *mask=[ 'mask1.mask', 'mask2.mask' ]*
      |              (d) Filename for region specification (e.g. from
        **viewer**).
      |              example: *mask='myregion.rgn'*
      |              (e) Combinations of the above options.
      |              example: *mask=['mycleanbox.txt', 'myimage.mask',
        'myregion.rgn','circle [ [ 120pix , 40pix] ,6pix ]']*
      |              (f) Threshold on primary-beam.
      |              A number between 0 and 1, used as a threshhold of
        primary beam coverage. The primary beam coverage map (imagename
        + '.flux(.pbcoverage)') will be made and the clean component
        placement will be limited to where it is > the number.
      |              (g) True or False.
      |              True: like (f), but use *minpb* as the number.
      |              False: go maskless (and expect trouble).
      |              (For masks for multiple fields, please see 'HINTS
        ON CLEAN WITH FLANKING FIELDS')

       

      .. rubric:: *uvtaper*
         :name: uvtaper

      .. rubric:: Apply additional uv tapering of the visibilities.
         default: *uvtaper=False*; example: *uvtaper=True*
             uvtaper=True expandable parameters
         :name: apply-additional-uv-tapering-of-the-visibilities.-default-uvtaperfalse-example-uvtapertrue-uvtapertrue-expandable-parameters

      .. rubric::     *outertaper*
         :name: outertaper

          uv-taper on outer baselines in uv-plane, [bmaj, bmin, bpa]
      taper Gaussian scale in uv or angular units.

      .. note:: **NOTE**: The on-sky FWHM in arcsec is roughly the *uvtaper* /
         200 (klambda).

           default: *outertaper=[]*; no outer taper applied; examples:
      *outertaper=['5klambda']* circular taper FWHM=5 kilo-lambda,
      *outertaper=['5klambda','3klambda','45.0deg']*,
      *outertaper=['10arcsec']* on-sky FWHM 10 arcseconds,
      *outertaper=['300.0']* default units are lambda in aperture plane

       

      .. rubric:: *modelimage*
         :name: modelimage

      Name of model image(s) to initialize cleaning. If multiple images,
      then these will be added together to form initial staring model.

      .. note:: **NOTE**: these are in addition to any initial model in the
         <imagename>.model image file.

          default: '' (none); examples: *modelimage='orion.model'*,
      *modelimage=['orion.model','sdorion.image']*

      .. note:: **NOTE**: If the units in the image are Jy/beam as in a
         single-dish image, then it will be converted to Jy/pixel as in
         a model image, using the restoring beam in the image header and
         zeroing negatives. If the image is in Jy/pixel then it is taken
         as is.

          When *nterms>1*, a one-to-one mapping is done between images
      in this list and Taylor-coefficients. If more than *nterms* images
      are specified, only the first *nterms* are used. It is valid to
      supply fewer than *nterms* model images. Example: Supply an
      estimate of the continuum flux from a previous imaging run.

      .. rubric:: *weighting*
         :name: weighting

      Weighting to apply to visibilities. default='natural'; example:
      *weighting='uniform'*; Options: 'natural','uniform','briggs',
      'superuniform','briggsabs','radial'

      .. rubric::     weighting expandable parameters
         :name: weighting-expandable-parameters

          For details on weighting please see Chapter3 of late Dr.
      Brigg's thesis (http://www.aoc.nrao.edu/dissertations/dbriggs)

          For *weighting='briggs'* and *'briggsabs'*:

      .. rubric::         *robust*
         :name: robust

              Brigg's robustness parameter. default=0.0; example:
      robust=0.5; Options: -2.0 to 2.0; -2 (uniform)/+2 (natural)

      .. rubric:: *        npixels*
         :name: npixels

              uv-box used for weight calculation a box going from
      -npixel/2 to +npixel/2 on each side around a point is used to
      calculate weight density. 0 means box is pixel size. default = 0;
      example: *npixels=2*

      .. note:: **EXEMPTION**: When choosing superuniform, it does not make
         sense to use npixels=0 as it is uniform thus if npixels is 0,
         it will be forced to 6 or a box from -3pixels to 3pixels.

          For *weighting='briggsabs'*

      .. rubric::         *noise*
         :name: noise

              noise parameter to use for Briggs "abs" weighting.
      example: *noise='1.0mJy'*      *
      *

       

      .. rubric:: *restoringbeam*
         :name: restoringbeam

      Output Gaussian restoring beam for clean image, [bmaj, bmin, bpa]
      elliptical Gaussian restoring beam. Default units are in
      arc-seconds for bmaj,bmin, degrees for bpa. default:
      *restoringbeam=[]*; Use PSF calculated from dirty beam. examples:
      *restoringbeam=['10arcsec']* circular Gaussian FWHM 10 arcseconds,
      *restoringbeam=['10.0','5.0','45.0deg']* 10"x5" at 45 degrees

      .. rubric:: *pbcor*
         :name: pbcor

      Output primary beam-corrected image. If *pbcor=False*, the final
      output image is NOT corrected for the PB pattern (particularly
      important for mosaics), and therefore is not "flux correct".
      Correction can also be done after the fact using immath to divide
      <imagename>.image by the <imagename>.flux image. default:
      *pbcor=False*, output un-corrected image; example: *pbcor=True*,
      output pb-corrected image (masked outside *minpb*)

      .. rubric:: *minpb*
         :name: minpb

      | Minimum PB level to use for pb-correction and pb-based masking.
        default=0.2; example: *minpb=0.01*
      |     When *imagermode* is \*not\* 'mosaic': *minpb* is applied to
        the flux image (sensitivity-weighted pb). *minpb* is used to
        create a mask, only when *pbcor=True*
      |     When *imagermode='mosaic'*: *minpb* is applied to the
        flux.pbcoverage image (mosaic pb with equal weight per
        pointing). *minpb* is always used to create a mask (regardless
        of *pbcor=True/False*).

      .. rubric:: *usescratch*
         :name: usescratch

      If True will create scratch columns if they are not there. And
      after **clean** completes the predicted model visibility is from
      the clean components are written to the MS. This increases the MS
      size by the data volume. if False then the model is saved in the
      MS header and the calculation of the visibilities is done on the
      fly when using calibration or **plotms**. Use True if you want to
      access the model visibilities in python, say.

      .. rubric:: *allowchunk*
         :name: allowchunk

      | Partition the image cube by channel-chunks. default=False;  
      |     False: Major cycle grids all channels. Minor cycle steps
        through all channels before the next major cycle.
      |     True: Major and minor cycles are performed one chunk at a
        time, and output images cubes are concatenated.

      .. rubric:: *async*
         :name: async

      Run asynchronously. default = False; do not run asychronously


   Bibliography
         :sup:`1. Rau and Cornwell, AA, Volume 532, 2011
         (` `ADS <http://adsabs.harvard.edu/abs/2011A%26A...532A..71R>`__ :sup:`)` `<#ref-cit1>`__

         :sup:`2. Cornwell et al. IEEE JSTSP, 2008
         (` `IEEE <http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4703511>`__ :sup:`)` `<#ref-cit2>`__

         :sup:`3. Bhatnagar et al., AandA, 487, 419, 2008
         (` `A&A <http://www.aanda.org/articles/aa/full/2008/31/aa9284-07/aa9284-07.html>`__ :sup:`)` `<#ref-cit3>`__
