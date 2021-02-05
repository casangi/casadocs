

.. _Description:

Description
   The **tclean** task forms images from visibilities and
   reconstructs a sky model.
   
   tclean handles continuum images and spectral line cubes, full
   Stokes polarization imaging, supports outlier fields, contains
   point-source CLEAN
   based `algorithms <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__ as
   well as options for multi-scale and `wideband image
   reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__ ,
   widefield imaging correcting for the w-term, full primary-beam
   imaging and joint mosaic imaging (with heterogeneous array support
   for ALMA). Parallelization of the major cycle is also available.
   
   The tclean task as based on the `CLEAN
   algorithm <https://www.cv.nrao.edu/~abridle/deconvol/node7.html>`__ ,
   which is the most popular and widely-studied method for
   reconstructing a model image based on interferometer data. It
   iteratively removes at each step a fraction of the flux in the
   brightest pixel in a defined region of the current “dirty” image,
   and places this in the model image.
   
   Image reconstruction in CASA typically comprises an outer loop of
   *major cycles* and an inner loop of *minor cycles*. The major
   cycle implements transforms between the data and image domains and
   the minor cycle operates purely in the image domain. Together,
   they implement an iterative weighted :math:`\chi^2` minimization
   that `solves the measurement
   equation <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/imaging-overview>`__.
   Minor cycle algorithms can have their own (different) optimization
   schemes and the imaging framework and task interface allow for
   considerable freedom in choosing options separately for each step
   of the process.
   
   |image1|

   .. rubric:: Operating Modes

   The tclean task can be configured to perform either full iterative
   image reconstructions
   (see `synthesis-imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging>`__ )
   or to run each step separately. Parameters for data selection,
   image definition, gridding and deconvolution algorithms,
   restoration and primary beam setup are shared between all
   operational modes.
   
   The main usage modes of tclean are:
   
   -  .. rubric:: Imaging and Deconvolution Iterations:
         
   
   Construct the PSF and Dirty image and apply a deconvolution
   algorithm to reconstruct a Sky model. A series of major and minor
   cycle iterations are usually performed. The output sky model is
   then restored and optionally PB-corrected. The Sky model can
   optionally be saved in the MS during the last major cycle.
   
   -  .. rubric:: Make PSF and PB:
         
   
   Make only the Point Spread Function and the Primary Beam, along
   with auxiliary weight images (a single pixel image containing
   sum-of-weight per plane, and (for mosaic and aprojection) a weight
   image containing the weighted sum of PB square).
   
   -  .. rubric:: Make a Residual/Dirty Image:
         
   
   Make a dirty image, or a new residual image using an existing or
   specified model image. This step requires the presence of the
   sum-of-weight and weight images (for normalization) constructed
   during the PSF and PB generation step.
   
   -  .. rubric:: Model Prediction:
         
   
   Save a sky model in the MeasurementSet for later use in
   calibration (virtual model or by actual prediction into a model
   column).
   
   .. warning:: **WARNING** *:* While tclean is generally safe to kill at
      almost any time (ctrl-c), the possible exceptions are the brief
      instances in which the data-writes back to the MS are in
      progress. Therefore, when setting the parameter
      *savemodel='modelcolumn’*, ensure that you do not interrupt the
      tclean process (ctrl-c) while the model is being written to the
      MS, as this will likely corrupt the MS.  
   
   -  .. rubric:: PB-Correction:
         
   
   Divide out the Primary Beam from the restored Sky image.
   
   .. rubric:: pblimit
      
   
   | The pblimit is a parameter used to define the value of the
     antenna primary beam gain, below which wide-field gridding
     algorithms such as *'mosaic'* and *'awproject'* will not apply
     normalization (and will therefore set to zero).  For
     *gridder='standard'*, there is no pb-based normalization during
     gridding and so the value of this parameter is ignored.
   | The sign of the pblimit parameter is used for a different
     purpose. If positive, it defines a T/F pixel mask that is
     attached to the output residual and restored images.  If
     negative, this T/F pixel mask is not included.  Please note that
     this pixel mask is different from the deconvolution mask used to
     control the region where CLEAN based algorithms will search for
     source peaks.  In order to set a deconvolution mask based on pb
     level, please use the *'pbmask'* parameter.
   
   .. warning:: **WARNING** *:* Certain values of pblimit should be avoided!
      These values are 1, -1, and 0. Details can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/data-weighting>`__. *
      *
   
   .. rubric:: widebandpbcor
      
   
   `Widebandpbcor <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_widebandpbcor>`__
   is a separate task, and will eventually be implemented as a
   parameter in **tclean**. It allows correction of the primary beam
   as part of `wideband
   imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__.
   It computes a set of PBs at the specified frequencies, calculates
   Taylor-coefficient images that represent the PB spectrum, performs
   a polynomial division to PB-correct the output Taylor-coefficient
   images from **tclean** (with *nterms>1* and
   *deconvolver='mtmfs'*), and recomputes the spectral index (and
   curvature) using the PB-corrected Taylor-coefficient images.
   
   -  .. rubric:: Pointing Corrections:
         
   
   Heterogeneous Pointing Corrections can optionally be applied with
   the *usepointing* and *pointingoffsetsigdev* parameters. These
   parameters apply corrections based on the pointing errors that are
   present in the POINTING sub-table. This can improve imaging
   performance for observations with high wide-band sensitivity, such
   as is typically observed with the VLA and ALMA telescopes. An
   overview of pointing corrections is given in the CASA Docs page on
   `Widefield
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam>`__.
   
   -  .. rubric:: Restoration:
         
   
   Specify a restoring beam and re-restore the model image.
   
   -  .. rubric:: Auto-masking:
         
   
   Automatically mask emission during clean; see `Masks for
   Deconvolution <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__
   for more information.
   
    
   
   .. rubric:: Output Images
      
   
   Depending on the operation being run, a subset of the following
   output images will be written to disk.
   
   imagename = 'try'
   
   +-----------------------------------+-----------------------------------+
   | try.psf                           | Point Spread Function             |
   +-----------------------------------+-----------------------------------+
   | try.pb                            | Primary Beam                      |
   +-----------------------------------+-----------------------------------+
   | try.residual                      | Residual Image (or initial Dirty  |
   |                                   | Image)                            |
   +-----------------------------------+-----------------------------------+
   | try.model                         | Model Image after deconvolution   |
   +-----------------------------------+-----------------------------------+
   | try.image                         | Restored output image             |
   +-----------------------------------+-----------------------------------+
   | try.image.pbcor                   | Primary Beam corrected image      |
   +-----------------------------------+-----------------------------------+
   | try.mask                          | Deconvolution mask                |
   +-----------------------------------+-----------------------------------+
   | try.sumwt                         | A single pixel image containing   |
   |                                   | sum of weights per plane          |
   +-----------------------------------+-----------------------------------+
   | try.weight                        | Image of un-normalized sum of     |
   |                                   | PB-square (for mosaics and        |
   |                                   | A-Projection)                     |
   +-----------------------------------+-----------------------------------+
   | try.psf.tt0, try.psf.tt1,         | Multi-term images representing    |
   | try.psf.tt2, try.model.tt0,       | Taylor coefficients (of           |
   | try.model.tt1, try.residual.tt0,  | polynomials that model the sky    |
   | try.residual.tt1, try.image.tt0,  | spectrum)                         |
   | try.image.tt1, etc...             |                                   |
   +-----------------------------------+-----------------------------------+
   | try.workdirectory                 | Scratch images written within a   |
   |                                   | 'work directory' for parallel     |
   | ( try.n1.psf, try.n2.psf,         | imaging runs for cube imaging.    |
   | try.n3.psf, try.n1.residual,      | The reference images are          |
   | try.n2.residual, try.n3.residual, | reference-concatenated at the end |
   | try.n1.weight, try.n2.weight,     | to produce single output cubes.   |
   | try.n3.weight, try.n1.gridwt,     | As of CASA 5.7, continuum imaging |
   | try.n2.gridwt, etc... )           | no longer produces a              |
   |                                   | try.workdirectory.                |
   |                                   |                                   |
   |                                   |                                   |
   +-----------------------------------+-----------------------------------+
   
    
   
   .. warning:: WARNING: If an image with that name already exists, it will in
      general be overwritten. Beware using names of existing images
      however. If the tclean is run using an imagename where
      <imagename>.residual and <imagename>.model already exist, then
      tclean will continue starting from these (effectively
      restarting from the end of the previous tclean). Thus, if
      multiple runs of tclean are run consecutively with the same
      imagename, then the cleaning is incremental.
   
   .. rubric:: Stokes polarization products
      
   
   It is possible to make polarization images of various Stokes
   parameters, based on the R/L circular (e.g., VLA) or the X/Y
   linear (e.g., ALMA) polarization products. When specifying
   multiple values in the 'stokes' parameter, the output image will
   have planes (along the "polarization" axis) corresponding to the
   chosen Stokes parameters.
   
   The Stokes parameter is specified as a string of up to four
   letters, and can indicate stokes parameters themselves, Right/Left
   hand polarization products, or linear polarization products (X/Y).
   Examples include:
   
   ::
   
      | stokes = 'I' # Intensity only (default)
      | stokes = 'IQU' # Intensity and linear polarization
      | stokes = 'IV' # Intensity and circular polarization
      | stokes = 'IQUV' # All Stokes imaging
      | stokes = 'RR' # Right hand polarization only
      | stokes = 'XXYY' # Both linear polarizations
      | stokes = 'pseudoI' # Intensity only, but including data with
        one of the parallel polarizations flagged
   
   For imaging the total intensity, the stokes='I' option is stricter
   than the stokes='pseudoI' option in the sense that it excludes all
   correlations for which any correlation is flagged, even though the
   remaining correlations are valid. On the other hand,
   the'pseudoI'option allows Stokes I images to include data for
   which either of the parallel hand data are unflagged. For example,
   if you have RR and LL dual polarization data and you flagged parts
   of RR but not LL, stokes='I' will ignore both polarizations in the
   time-stamps where RR are flagged, while stokes='pseudoI' will
   include all unflagged data in the total intensity image. See the
   CASA Docs pages on `Types of
   Images <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/image-definition>`__ and `Single
   Dish Imaging
   (tsdimaging) <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tsdimaging>`__ for
   more information. It is also possible to split out a polarization
   product with split and image separately, but you will not be able
   to combine these part-flagged data in the uv-domain. 
   
    
   
   .. rubric:: Functional Parameter Blocks
      
   
   The **tclean** parameters are arrangedin the functional blocks
   described below. More details on the individual parameters and
   sub-parameters can be found under the Parameters tab at the top of
   this page.
   
   As a general rule, sub-parameters will appear (and be used) only
   when a parent parameter has a specific value. This means that for
   a given set of choices (e.g. deconvolution or gridding algorithm)
   only parameters that are relevant to that choice will be visible
   to the user when " inp() " is invoked. It is advised that this
   task interface be used even when constructing tclean scripts that
   call the task as a python call " tclean(....) " to understand
   which parameters are relevant to the run and which are not.
   
    
   
   .. rubric:: Data Selection (selectdata)
      
   
   Selection parameters allow the definition of a subset of the
   supplied MS (or list of MSs) on which the imaging is to operate.
   Details can be found on the `CASA Docs pages of Image
   Selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__.
   
    
   
   .. rubric:: Image Definition (specmode)
      
   
   The image coordinate system(s) and shape(s) can be set up to form
   single images (from a single field or from multiple fields forming
   a mosaic),or multiple fields. The different modes for imaging
   include:
   
   -  'mfs': multi-frequency synthesis, i.e., continuum imaging with
      only one output image channel.
   -  'cube': Spectral line imaging with one or more channels. The
      fixed spectral frame, LSRK, will be used for automatic internal
      software Doppler tracking so that a spectral line observed over
      an extended time range will line up appropriately.
   -  'cubedata': Spectral line imaging with one or more channels
      There is no internal software Doppler tracking so a spectral
      line observed over an extended time range may be smeared out in
      frequency.
   -  'cubesource': Spectral line imaging while tracking moving
      source (near field or solar system `ephemeris
      objects <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/ephemeris-data>`__ ).
      The velocity of the source is accounted and the frequency
      reported is in the source frame.
   
   Combined use of the parameters 'specmode' and 'gridder' (see
   below) allows to specify smaller outlier fields, facetted images,
   single plane wideband images (with 1 or more Taylor terms to model
   spectra), 3D spectral cubes with multiple channels, 3D images with
   multiple Stokes planes, 4D images with frequency channels and
   Stokes planes. Various combinations of all these options are also
   supported.
   
   The  `CASA Docs pages on Image
   Types <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/image-definition>`__  provide
   more details.
   
    
   
   .. rubric:: Gridding Options (gridder)
      
   
   Options for convolutional resampling include standard gridding
   using a prolate spheroidal function, the use of FTs of Fresnel
   kernels for W-Projection, the use of baseline aperture
   illumination functions for A-Projection and Mosaicing. These
   include:
   
   -  'standard': standard gridding using a prolate spheroidal
      function
   -  'wproject': use of FTs of Fresnel kernels to correct for the
      widefield non-coplanar baseline effect (Cornwell et.al 2008)
   -  'widefield': Facetted imaging with or without W-Projection per
      facet.
   -  'mosaic': A-Projection that uses baseline, frequency and time
      dependent primary beams, without sidelobes, beam rotation or
      squint correction.
   -  'awproject': A-Projection from aperture illumination models
      with azimuthally asymmetric beams, including beam rotation,
      squint correction, conjugate frequency beams and W-projection
      (Bhatnagar et.al, 2008).
   
   Combinations of these options are also available. See the `CASA
   Docs pages on Widefield
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam>`__ for
   more information.
   
   For mosaicing and AW-projection, the frequency dependence of the
   primary beam within the data being imaged is included in the
   calculations and can optionally also be corrected for during
   gridding. See the CASA Docs page on `Wideband
   Imaging <https://casa.nrao.edu/casadocs-devel/imaging/synthesis-imaging/wide-band-imaging>`__ for
   details.
   
    
   
   .. rubric:: Deconvolution Options (deconvolver)
      
   
   All our algorithms follow the Cotton-Schwab CLEAN style of major
   and minor cycles with the details of the deconvolution algorithm
   usually contained within the minor cycle and operating in the
   image domain. Options include:
   
   -  'hogbom': An adapted version of Hogbom Clean (Hogbom, 1974)
   -  'clark': An adapted version of Clark Clean (Clark, 1980)
   -  'clarkstokes': Clark Clean operating separately per Stokes
      plane
   -  'multiscale': MultiScale Clean (Cornwell, 2008).
      Scale-sensitive deconvolution algorithm designed for images
      with complicated spatial structure. It parameterizes the image
      into a collection of inverted tapered paraboloids.
   -  'mtmfs': Multi-term (Multi Scale) Multi-Frequency Synthesis
      (Rau and Cornwell, 2011). Models the wide-band sky brightness
      distribution through the use of multi-term Taylor polynomial
      and wideband primary beam corrections (to be used with
      nterms>1).
   -  'mem': Maximum Entropy Method (Cornwell and Evans, 1985). Note:
      The MEM implementation in CASA is not very robust, improvements
      will be made in the future.
   
   If as input to tclean the stokes parameter includes polarization
   planes other than I, then choosing deconvolver='hogbom' or
   'clarkstokes' will clean (search for components) each plane
   sequentially, while deconvolver ='clark' will deconvolve jointly.
   
   For more details, see the `CASA Docs pages on Deconvolution
   Algorithms <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__.
   
   Several options for `making masks, including
   automasking <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__,
   are also provided.
   
    
   
   .. rubric:: Data Weighting (weighting)
      
   
   Data weighting during imaging allows for the improvement of the
   dynamic range and the ability to adjust the synthesized beam
   associated with the produced image. The weight given to each
   visibility sample can be adjusted to fit the desired output. There
   are several reasons to adjust the weighting, including improving
   sensitivity to extended sources or accounting for noise variation
   between samples. The user can adjust the weighting by changing the
   *weighting* parameter with six options: 'natural', 'uniform',
   'briggs',  'superuniform', 'briggsabs', and 'radial'. Optionally,
   a UV taper can be applied, and various parameters can be set to
   further adjust the weight calculations.
   
   The most used options for data weighting are 'natural', 'unform'
   and 'briggs'.
   
   -  'Natural' weighting gives equal weight to all samples,
      resulting in the lowest noise level and largest (poorest)
      resolution, with relatively high sidelobe levels.
   -  'Uniform' weighting gives a weight inversely proportional to
      the sampling density function, which minimizes sidelobe levels
      and provides higher resolution, but at the expense of higher
      noise levels.
   -  'Briggs' weighting provides a compromise between natural and
      uniform weighting, and often optimizes between angular
      resolution, noise, and sidelobe levels. The key parameter for
      briggs weighting is the robust sub-parameter, which takes
      value between -2.0 (close to uniform weighting) to 2.0 (close
      to natural). The scaling of Ris such that robust=0 gives a good
      trade-off between resolution and sensitivity.
   
   In addition to the weighting scheme specified via the 'weighting'
   parameter, additional weights can be applied:
   
   -  The 'uvtaper' parameter applies a Gaussian taper on the weights
      of the UV data, in addition to the weighting scheme specified
      via the 'weighting' parameter. It is equivalent to smoothing
      the PSF obtained by other weighting schemes and can be
      specified either as a Gaussian in uv-space (eg. units of lambda
      or klambda) or as a Gaussian in the image domain (eg. angular
      units like arcsec). The effect of uvtaper this is that the
      clean beam becomes larger, and surface brightness sensitivity
      increases for extended emission.
   -  The 'perchanweightdensity' parameter (for briggs and uniform
      weighting of cubes) determines whether to calculate the
      weight density for each channel independently (True) or a
      common weight density for all of the selected data (False). In
      general, perchanweightdensity=True (default since CASA 5.5)
      provides more uniform sensitivity per channel for cubes, but
      with generally larger PSFs, while perchanweightdensity=False
      results in smaller psfs for the same robustness value, but the
      rms noise as a function of channel varies and increases toward
      the edge channels.
   -  The 'mosweight' sub-parameter of the mosaic gridder determines
      whether to weight each field in a mosaic independently
      (mosweight = True), or to calculate the weight density from the
      average uv distribution of all the fields combined (mosweight =
      False). For ALMA it has been shown that mosweight = True
      (default since CASA 5.4) may give better results in the
      presence of poor uv-coverage or non-uniform sensitivity across
      the mosaic, but the downside is that the major and minor axis
      of the synthesized beam may be ~10% larger than with
      mosweight=False, and it may potentially cause memory issues for
      large VLA mosaics.
   
   More details on data weighting can be found on the `Image
   Algorithm <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/data-weighting>`__ pages
   of CASA Docs
   
    
   
   .. rubric:: Iteration Control (niter)
      
   
   Iterations are controlled by user parameters (gain, niter, etc..)
   as well as stopping criteria that decide when to exit minor cycle
   iterations and trigger the next major cycle, and also when to
   terminate the major-minor loop. These stopping criteria include
   reaching iteration limits, convergence thresholds, and signs of
   divergence with appropriate messages displayed in the log. For
   more details, see the `CASA Docs pages on Iteration
   Control <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/user-interaction>`__ .
   
    
   
    
   
   .. rubric:: Other Options
      
   
   .. rubric:: Handling Large Data and Image Sizes
      
   
   Parallelization of the major cycle is available for continuum
   imaging and of both major and minor cycles for cube imaging. In
   order to run tclean in parallel mode it is necessary to launch
   CASA with mpicasa, and set the tclean parameter parallel=True. The
   parallelization of tclean works in the same way if the input is a
   normal MS or a Multi-MS (MMS), and thus differs from the parallel
   approach used by other tasks in that it does not require a
   partitioned MMS file. Details can be found in the `CASA Docs
   chapter on Parallel
   Processing <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__ .
   
   For large image cubes, the gridders can run into memory limits as
   they loop over all available image planes for each row of data
   accessed. To prevent this problem, we can grid subsets of channels
   in sequence with the chanchunks parameter, so that at any given
   time only part of the image cube needs to be loaded into memory.
   The chanchunks parameter controls the number of chunks to split
   the cube into.
   
   .. rubric:: User Interaction
      
   
   Options for user interaction include `interactive
   masking <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__
   and editing of iteration control parameters. The `output log
   files <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-logger>`__ can
   also be used to diagnose some problems.
   
   Several convenience features are also available, such as operating
   on the MS in read-only mode (which does not require write
   permissions), the ability to restart and continue imaging runs
   without incuring the unnecessary cost of an inital major cycle or
   PSF construction and the optional return of a python dictionary
   that contains the convergence history of the run.
   
   .. rubric:: Scripting Controls
      
   
   Finer control can be achieved using the PySynthesisImager tools to
   run (for example) only image domain deconvolution or to insert
   methods for automatic mask generation (for example) in between the
   existing major/minor cycle loops or to connect external methods or
   algorithms for either the minor or major cycles.
   
   .. rubric:: Tracking moving sources or sources with ephemeris
      tables
      
   
   If the phasecenter is a known major solar system object
   ('MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS',
   'NEPTUNE', 'PLUTO', 'SUN', 'MOON') or is an ephemerides table,
   then that source is tracked and the background sources get smeared
   (which is useful especially for long observations or multi epoch
   data). There is a special case, when phasecenter='TRACKFIELD',
   which will use the ephemerides or polynomial phasecenter in the
   FIELD table of the MeasurementSets as the source center to track.
   When in tracking mode,  the image center will be the direction of
   the source at the first time in the user selected data. At all
   other times, the source will be shifted by the amount it has moved
   in the frame of the image to that initial time. Examples of usage
   are presented in the **tclean** examples tab.
   
   .. note:: **NOTE**: When displaying ephemeris images, it is good practice
      to use relative coordinates to determine the average offset of
      emission from the ephemeris path over the observation, i.e.,
      axis label properties: world coordinate, relative position. The
      use of the absolute grid (default) can be misleading since the
      chosen coordinate frame is associated with the ephemeris path
      location at an unspecified time, although usually near the
      beginning of the experimient.
   
   More information can be found in the `CASA Docs chapter on
   Ephemeris
   Data <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/ephemeris-data>`__.
   
   .. |image1| image:: _apimedia/26ad14d4f63ff633dbd5d9e92d40a5059ab46a67.png

   .. rubric:: History

   At the end of a successful tclean run, the history of the output
   images is updated. For every tclean command a series of entries is
   recorded, including the task name (tclean), the CASA version used,
   and every parameter-value pair of the task. The history is written
   to all the images found with the name given in the 'imagename'
   parameter of tclean and any extension.

   The image history entries added by tclean can be inspected using
   the task imhistory (`see API <../casatasks.rst>`_), similarly as
   with the history entries added by other image analysis tasks.

   As a lower level interface, the image history can be also inspected
   and manipulated using CASA tools such as the image analysis tool
   and the table tool (`see API <../casatools.rst>`_. The history
   entries are written into the 'logtable' subtable of the images.
   

.. _Examples:

Examples
   task examples
   
   The following examples, to be expanded, highlight modes and
   options that the tclean task supports.
   The examples below are written as scripts that may be copied
   and pasted to get started with the basic parameters needed for
   a particular operation. When writing scripts, it is advised
   that the interactive task interface be used to view lists of
   sub-parameters that are relevant only to the operations being
   performed. For example, setting specmode='cube' and running
   inp() will list parameters that are relevant to spectral
   coordinate definition, or setting niter to a number greater
   than zero (niter=100) followed by inp() will list iteration
   control parameters.
   Note that all runs of tclean need the following parameters:
   vis, imagename, imsize, and cell.
   By default, tclean will run with niter=0, making the PSF, a
   primary beam, the initial dirty (or residual) image and a
   restored version of the image.
   
    
   
   For examples running tclean on ALMA data, see also the CASA
   Guide `"Tclean and
   ALMA" <https://casaguides.nrao.edu/index.php?title=TCLEAN_and_ALMA>`__.
   
   .. rubric:: 
      Imaging and Deconvolution Iterations
      
   
   .. rubric:: Using Hogbom CLEAN on a single MFS image
      
   
   ::
   
      | tclean(vis='test.ms', imagename='try1', imsize=100,
        cell='10.0arcsec', specmode='mfs',
      |        deconvolver='hogbom', gridder='standard',
        weighting='natural', niter=100 )
   
   .. rubric:: Using Multi-scale CLEAN on a Cube Mosaic image
   
   ::

      tclean(vis='test.ms', imagename='try1', imsize=100,
             cell='10.0arcsec',specmode='cube', nchan=10,
             start='1.0GHz', width='10MHz', deconvolver='multiscale',
             scales=[0,3,10,30], gridder='mosaic', pblimit=0.1,
             weighting='natural', niter=100 )
   
   .. rubric:: Using W-Projection with Multi-Term MFS wideband imaging

   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100,
             cell='10.0arcsec', deconvolver='mtmfs', reffreq='1.5GHz',
             nterms=2, gridder='wproject', wprojplanes=64,
             weighting='natural', niter=100 )
   
   .. rubric:: Using automasking with any type of image

   ::
   
      tclean(vis='test.ms', imagename='try1', niter=100, ....,
             usemask='auto-multithresh')
    
   
   .. rubric:: Scripting using PySynthesisImager

   PySynthesisImager (LINK) is a python application built on top
   of the synthesis tools (LINK). The operations of the tclean
   task can be replicated using the following python script.
   Subsets of the script can thus be chosen, and extra external
   methods can be inserted in between as desired.  After each
   stage, images are saved on disk. Therefore, any modifications
   done to the images in between steps will be honored. 
   

   ::
   
      ## (1) Import the python application layer
      from imagerhelpers.imager_base import PySynthesisImager
      from imagerhelpers.input_parameters import ImagerParameters

      ## (2) Set up Input Parameters
      ## - List all parameters that you need here
      ## - Defaults will be assumed for unspecified parameters
      ## - Nearly all parameters are identical to that in the task.
      ## Please look at the list of parameters under __init__
      ## using "help ImagerParameters"
      paramList = ImagerParameters(msname ='DataTest/point.ms',
                                   field='',
                                   spw='',
                                   imagename='try2',
                                   imsize=100,
                                   cell='10.0arcsec',
                                   specmode='mfs',
                                   gridder='standard',
                                   weighting='briggs',
                                   niter=100,
                                   deconvolver='hogbom')

      ## (3) Construct the PySynthesisImager object, with all input parameters
      imager = PySynthesisImager(params=paramList)

      ## (4) Initialize various modules.
      ## - Pick only the modules you will need later on. For
      example, to only make
      ## the PSF, there is no need for the deconvolver or iteration control modules.
      ## Initialize modules major cycle modules
      imager.initializeImagers()
      imager.initializeNormalizers()
      imager.setWeighting()
      ## Init minor cycle modules
      imager.initializeDeconvolvers()
      imager.initializeIterationControl()

      ## (5) Make the initial images
      imager.makePSF()
      imager.makePB()
      imager.runMajorCycle() # Make initial dirty / residual image

      ## (6) Make the initial clean mask
      imager.hasConverged()
      imager.updateMask()

      ## (7) Run the iteration loops
      while ( not imager.hasConverged() ):
          imager.runMinorCycle()
          imager.runMajorCycle()
          imager.updateMask()

      ## (8) Finish up
      retrec=imager.getSummary();
      imager.restoreImages()
      imager.pbcorImages()

      ## (9) Close tools.
      imager.deleteTools()
   
    
   For model prediction (i.e. to only save an input model in
   preparation for self-calibration, for example), use the
   following in step (5). The name of the input model is either
   assumed to be <imagename>.model (or its multi-term equivalent)
   or should be specified via the startmodel parameter in step
   (2).
    
   
   ::
   
      imager.predictModel()      # Step (5)
   
   For major cycle parallelization for continuum imaging
   (specmode='mfs'), replace steps (1) and (3) with the following
   
    
   
   ::
   
      # Step (1)
      from imagerhelpers.imager_parallel_continuum import PyParallelContSynthesisImager

      # Step (3)
      imager = PyParallelContSynthesisImager(params=paramList)

   
   For parallelization of both the major and minor cycles for Cube
   imaging, replace steps (1) and (3) with the following, and
   include a virtual concanenation call at the end. (However, note
   that for parallel Cube imaging, if you would like to replace
   the minor cycle with your own code (for example), you would
   have to go one layer deeper. For this, please contact our team
   for assistance.)
   
    
   
   ::
   
      from imagerhelpers.imager_parallel_cube import PyParallelCubeSynthesisImager   # Step (1)
      imager = PyParallelCubeSynthesisImager(params=paramList) # Step (3)
      imager.concatImages(type='virtualcopy') # Step (8)
   
    
   
   .. rubric:: Using tclean with ephemerides tables in CASA format

   When you have an ephermeris table that covers the whole
   observation:
   
   ::
   
      tclean(vis=['MS1.ms', 'MS2.ms', 'MS3.ms', 'MS4.ms', 'MS5.ms'],
             selectdata=True, field="DES_DEEDEE",
             spw=['17,19,21,23','17,19,21,23','17,19,21,23','17,19,21,23','17,19,21,23'],
             intent="OBSERVE_TARGET#ON_SOURCE", datacolumn="data",
             imagename="test_track", imsize=[2000, 2000], cell=['0.037arcsec'],
             phasecenter="des_deedee_ephem.tab", stokes="I")
   
   You can check whether the ephermeris table is of the format
   that CASA accepts by using the measures tool me.framecomet
   function:

   ::
   
      me.framecomet('des_deedee.tab')
   
   If this tool accepts the input without complaint, then the same
   should work in tclean.
   If the source you are tracking is one of the ten sources for
   which the CASA measures tool has the ephemerides from the JPL
   DE200 or DE405, then you can use their names directly:

   ::
   
      tclean(vis=['uid___A002_Xbc74ea_X175c.ms',
                  'uid___A002_Xbc74ea_X1af4.ms',
                  'uid___A002_Xbc74ea_X1e19.ms',
                  'uid___A002_Xbc74ea_X20b7.ms'],
             selectdata=True, field="Jupiter",
             spw=['17,19,21,23','17,19,21,23','17,19,21,23','17,19,21,23'],
             intent="OBSERVE_TARGET#ON_SOURCE", datacolumn="corrected",
             imagename="alltogether", imsize=[700, 700], cell=['0.16arcsec'],
             phasecenter="JUPITER", stokes="I")
   
   For ALMA data mainly the correlator may have the ephemerides of
   a moving source already attached to the FIELD tables of the
   MeasurementSets (as it was used to phase track the source). In
   such special cases, you can use the keyword "TRACKFIELD" in the
   phasecenter parameter, and then the internal ephemerides will
   be used to track the source.
   
    
   
   ::
   
      tclean(vis=['MS1.ms', 'MS2.ms', 'MS3.ms', 'MS4.ms', 'MS5.ms'],
             selectdata=True, field="DES_DEEDEE",
             spw=['17,19,21,23','17,19,21,23','17,19,21,23','17,19,21,23','17,19,21,23'],
             intent="OBSERVE_TARGET#ON_SOURCE", datacolumn="data",
             imagename="test_track", imsize=[2000, 2000],
             cell=['0.037arcsec'], phasecenter="TRACKFIELD", stokes="I")

.. _Development:

Development
   task_tclean.py  contains only calls to various steps and the
   controls for different Operating Modes (LINK).  No other logic is
   present in the top level task script.    task_tclean.py uses
   classes defined in refimagerhelper.py ( PySynthesisImager and its
   parallel derivatives ).

   Script writers aiming to replicate tclean in an external script
   and be able to insert their own methods or connect their own
   modules, will be able to simply copy and paste the task tclean
   code (the lines containing  " imager.xxxx " )
   
    
   
   The tclean task interface is meant to show (and use) subparameters
   only when their parent options are turned on. This way, at any
   given time, the only parameters a user should see via inp() are
   those that are relevant to the current set of algorithm and
   operational choices. 
   
    
   
   Additional examples to be added to the Examples tab (from testing
   suite at
   https://svn.cv.nrao.edu/svn/casa/branches/release-4_7/gcwrap/python/scripts/tests/test_refimager.py):
   
   Examples are meant to have a consistent set of values for vis,
   imagename, imsize,cell, with a limited number of parameters per
   line, to ensure readability. Note that each multiline command has
   to be edited outside of plone and copied in here, such that the
   spacing is preserved and the reader can copy/paste at the casa
   prompt. 
   
   
   
   .. rubric:: Make PSF and PB
      
   
   Make only the PSF, Weight images, and the PB.
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec, niter=0)


   .. rubric:: Make a residual/dirty image
      
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: Model Prediction

   
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: PB-correction
      
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   

   .. rubric:: Restoration

   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: Restarts

   ( deconv only,  autonaming, etc )
   
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   

   .. rubric:: Data Selection
      
   
   one MS, a list of MSs.
   
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: Single-Field Image Shapes

   Single Field (mfs, cube (basics), phasecenter, stokes planes ? )
   
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: Defining Spectral Coordinate Systems
      
   
   LINK to Synthesis Imaging / Spectral Line Imaging
   
   (examples of all the complicated ways you can do this)
   
   example ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')


   .. rubric:: Examples of Multi-Field Imaging
      
   
   ( 2 single, multiterm, mfs and cube, etc )
   
   example ::

      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')

   
   .. rubric:: Examples of Iteration Control
      
   
   niter=0,  using cycleniter,  cyclefactor...
   
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')

   
   .. rubric:: Using a Starting model

   single term, multi-term, with restarts, a single-dish model
   (units, etc).
   
   example
   
   ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: Saving model visibilities in preparation for self-calibration
      
   
   use savemodel of various types.
   
   example ::

      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: Making masks for deconvolution
      
   
   LINK to Synthesis Imaging / Masks For Deconvolution
   
   making masks....
   
   example ::

      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')

   
   .. rubric:: Primary Beam correction
      
   
   LINK to Synthesis Imaging / Primary Beams
   
   single term, wideband (connect to wb)
   
   example ::

      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   

   .. rubric:: Returned dictionary
      
   
   example of what is in it...
   
   example ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   

   .. rubric:: Examples of Wide-Band Imaging

   LINK to Synthesis Imaging / Wide Band Imaging
   
   Choose nterms, ref-freq.  Re-restore outputs. Apply widebandpbcor
   
   example::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   

   .. rubric:: Examples of Mosaicking
      
   
   LINK to Synthesis Imaging / Mosaicking
   
   Setting up mosaic imaging, setup vpmanager to supply external PB.
   
   example ::

      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   

   .. rubric:: Examples of Wide-field and Full-Beam Imaging
      
   
   facets, wprojection (and wprojplanes),  A-Projection
   
   example ::
   
      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
    
   
   .. rubric:: Parallelization for Continuum/MFS and Cube

   example ::

      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec'
   

   .. rubric:: Channel chunking for very large Spectral Cubes

   example ::

      tclean(vis='test.ms', imagename='try1', imsize=100, cell='10.0arcsec')
   
   
   
   .. rubric:: Changes to tclean

   10/19/2019:
   
   In the MTMFS deconvolver, the expression used to compute D-Chisq
   can be algebraically reduced. This means that the runtime of the
   minor cycle has been improved ror deconvolver=‘MTMFS’,
   particularly for large imsize, niter, and number of scales for
   multi-scale deconvolution. This `technical memo <https://drive.google.com/file/d/1U1zRrmBJ4vYfsi-7IE5orOYHIIRmiFSL/view?usp=sharing>`_
   briefly describes the algorithmic changes and provides examples of
   the speed-up in runtime.
