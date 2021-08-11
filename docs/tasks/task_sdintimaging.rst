

.. _Description:

Description
   The sdintimaging task allows joint reconstruction of wideband single dish
   and interferometer data.

   .. warning::

      Joint reconstruction of wideband single dish and interferometer data in
      CASA is experimental. Please use at own discretion.
   
      A description of tested usage modes can
      be found on the CASA Docs chapter page on  `Joint Single Dish
      and Interferometer Image Reconstruction <../../notebooks/image_combination.ipynb#Joint-Single-Dish-and-Interferometer-Image-Reconstruction>`_

   Interferometer data are gridded into an image cube (and
   corresponding PSF). The single dish image and PSF cubes are
   combined with the interferometer cubes in a feathering step. The
   joint image and PSF cubes then form inputs to any deconvolution
   algorithm (in either cube or mfs/mtmfs modes). Model images from
   the deconvolution algorithm are translated back to model image
   cubes prior to subtraction from both the single dish image cube as
   well as the interferometer data to form a new pair of residual
   image cubes to be feathered in the next iteration. In the case of
   mosaic imaging, primary beam corrections are performed per channel
   of the image cube, followed by a multiplication by a common
   primary beam, prior to deconvolution. Therefore, for mosaic
   imaging, this task always implements conjbeams=True and
   normtype=’flatnoise’.

   |image1|

   A more detailed description of the underlying algorithm, as well
   as results from its testing, can be found on the CASA Docs chapter
   page on `Joint Single Dish and Interferometer Image
   Reconstruction <../../notebooks/image_combination.ipynb#Joint-Single-Dish-and-Interferometer-Image-Reconstruction>`_.
   Note that the above diagram shows only the 'mtmfs' variant. Cube
   deconvolution proceeds directly with the cubes in the green box
   above, without the extra conversion back and forth to the
   multi-term basis. Primary beam handling is also not shown in this
   diagram, but full details (via pseudocode) are available in
   the `reference
   publication. <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7>`_

   
   .. rubric:: Task Specification : sdintimaging
   
   The sdintimaging task shares a significant number of parameters
   with the tclean task. In the description below, parameters that
   are specific to sdintimaging are listed with full details, but all
   others will reference the existing tclean parameter documentation.

   
   .. rubric:: Data Selection
   
   -  All data selection options allowed for interferometer data.
      This set of parameters is identical to those in task
      **tclean**.

   
   .. rubric:: Image Definition
   
   -  Spatial dimensions are defined via the parameters : *imsize,
      cell, phasecenter, projection*
   
   -  Spectral dimensions for the major cycle are defined for cubes
      : *nchan,start, width, outframe, veltype, restfreq, interpolation*
   
   -  Spectral dimensions for the minor cycle are chosen based on
      specmode.  For *specmode='cube'* the minor cycle follows the
      same channelization as the major cycle. For *specmode='mfs'*,
      the choice of deconvolver and the setting of *'reffreq'* will
      decide the spectral coordinate system of the wideband image
      that is created after collapsing the cube images from the major
      cycle. For *deconvolver='mtmfs'* the appropriate cube-to-taylor
      (and reverse) conversions are applied.
   
   .. rubric:: Specifying Both Cube and MFS settings (for *specmode='mfs'*) :
   
   In **sdintimaging**, with MFS deconvolution, one *needs to specify
   both cube and mfs settings for frequency coordinates because in
   this usage mode the major cycle is done with cubes and the minor
   cycle with mfs*. This detail is different from the tclean task.  A
   few general rules to follow for a MFS (or MTMFS) minor cycle are
   
   -  The reffreq must lie between the ends of the cube frequency
      range (default based on data selection, or explicitly specified
      using *start, width, nchan*).  If this is not the case, an
      error message will appear.  If left at its default value of
      *reffreq=''*, it will be automatically computed to be the mean
      of the first and last channel frequencies and a log message is
      printed with the new value.
   
   -  For a wideband imaging run with nterms, at least nterms
      channels must be present in the input cubes. Ideally, in order
      to fully capture spectral variations and also guard against
      missing data, it is recommended that the cube be defined with
      between 5 and 20 channels. More may of course be used,
      especially in order to avoid bandwidth smearing within
      channels, but a larger number of channels will cause the
      feathering step to take longer.  Warnings are printed if the
      nchan of the cube is small (less than 5) or too large (more
      than 50), and the task will exit with an error if nchan <
      nterms.
   
   -  The sdintimaging task will perform the above checks on the
      input parameters and report problems/warnings as appropriate.  
      The internal automation of some of these settings is on our
      'Future Work' list.
   
   .. rubric:: Single Dish data input
   
   -  Image cubes that represent the observed SD image per channel
      and the corresponding SD beam :  *sdimage, sdpsf*
   
   -  Both the sdimage and sdpsf image cubes must contain per plane
      restoringbeams that represent the effective SD beam.  Per-plane
      restoring beams may be added to an existing image cube using
      ia.open(), a loop over channels with ia.setrestoringbeam(..),
      and ia.close()
   
   -  Ideally, the imsize, cellsize, and phasecenter of the SD cube
      should match that of the INT cubes specified by imsize,
      cellsize, phasecenter.   However in case of a detected
      mismatch, the *ia.regrid()* method is called internally to
      convert it to the target csys prior to continuing. It is
      expected that such a regrid is possible and in case of error,
      the user should see a warning and suggestion to experiment with
      the imregrid task to reformat their input SD cube.
   
   -  The frequency axis of the SD cubes must exactly match the INT
      cube spectral axis defined by nchan, start, width.  Note that
      in the internal imregrid call, the frequency axis is not
      regridded. *This means that nchan, start and width specified in
      the task interface must match the frequency coordinates of the
      input SD image.*
   
      -  Use a helper method (shown in the ALMA M100
         example below)
         to extract nchan/start/width parameters from the SD Image
         cube, and supply these as inputs to sdintimaging to exactly
         match the frequency coordinates of the SD and INT cubes.
   
   -  The order of the direction, stokes, and spectral axes must
      match the INT cubes, typically RA,DEC,Stokes,Channel
   
   -  Blank channels (sum of pixel amplitudes=0) are internally
      flagged and left out of the joint reconstruction.   So, one way
      to tell the algorithm to ignore some channels in the input SD
      cube is to force all pixel values to zero.
   
   -  A convenience option has been provided within sdintimaging to
      auto-generate simple SD PSF cubes. If sdpsf='', a PSF cube is
      calculated by evaluating Gaussians based on the restoringbeam
      information per channel read from the input SD Image cube. 
      This option is useful if only an SD Image cube is available as
      the output of the single dish imaging step.
   
   Please see the ALMA M100 example below
   for sample code and task calls that illustrates the simplest way
   of setting up these inputs.
   
   To use SD PSFs that represent actual SD beam patterns, please read
   the following details.
   
   -  The SD PSF must contain a model of the single dish beam at the
      same world-coordinate location as the imaging phasecenter that
      is specified (or assumed via the supplied MS, when
      *phasecenter=’’*), it must be normalized to peak 1, and the PSF
      cube must contain corresponding restoring beams per channel.
   
   -  It is also expected that the single dish PSF peak is at the
      image center after regridding (same as the interferometer PSF).
      An internal check will look for position shifts (subpixel
      shifts too) and if offsets are 0.001 of a degree or more, it
      will not proceed.  A way around this is to manually re-evaluate
      the SD PSF directly onto the coordinate system of one of the
      intermediate INT images such that the middle pixel contains the
      peak of the PSF. An alternative is to use the *sdpsf=''*
      option, with which one can approximate the SD PSF.
   
   -  Other ideas to create an SD PSF : Use the SD image cube for
      header information and cube dimensions. Create an empty CASA
      image, fill it with evaluated Gaussians that match the SD beam
      size per channel. A sample script is provided
      `here <https://github.com/urvashirau/WidebandSDINT/blob/master/ScriptForRealData/make_gauss_beam_cube.txt>`__.
   
   -  The SD PSFs (in this case for the simulated examples/tests) are
      typically generated by calculating disk-shaped aperture
      functions of the appropriate dish diameter, taking a Fourier
      transform and squaring and normalizing the result.

   
   .. rubric:: Data Combination options
   
   The sdintimaging task may be run in three data combination modes
   via the *usedata* parameter. 
   
   -  **'sdint' :**  Use the interferometer and single dish data in a
      joint reconstruction.  Specification of the ‘sdgain’ and
      ‘ dishdia’ are the same as for the feather task. The method in
      the feather task is called internally to combine image cubes
      and PSF cubes prior to deconvolution.
   
      -  For *specmode='mfs'*, each channel is pb-corrected to flat
         sky and then a common primary beam (and mask) is applied
         prior to deconvolution. The common PB is computed as a
         weighted average of PBs, using the .sumwt per channel. 
      -  When the INT or the SD cubes contain flagged (i.e. empty)
         channels, they are left out of the joint reconstruction.
         Therefore, only those channels that have both INT and SD
         images, are used.
   
   -  '**sd**' : Use only the single-dish data and enable
      deconvolution of the single dish image cubes. Both cube and
      wideband multi-term deconvolution of single dish data are
      possible. Note that this mode (currently) still requires an
      interferometer MS to be supplied in order to construct image
      templates. This option is experimental and has passed only the
      tests reported in the publication and the examples shown in
      CASAdocs.
   
   -  **'int'** : Uses only interferometer data. For
      gridder= *'mosaic'* and *'awproject'*, it implements a
      wideband mosaic scheme similar to those offered via task
      tclean, but with the concept of conjugate-pb correction
      implemented in the image domain. It does so by taking a
      flat-sky normalization per channel, followed by a flat-noise
      rescaling to apply a common primary beam to all channels, and
      subsequently collapsing into taylor images for deconvolution.
      This option is experimental and has passed only the most basic
      tests and comparisons with equivalent modes in tclean.
      Therefore, please use only with caution.

   
   .. rubric:: Tuning the sdgain parameter
   
   The *sdgain* parameter acts as an image weighting option by being
   applied both to the data as well as the PSFs during combination.
   Setting values away from 1.0 adjusts the relative weight of the SD
   information to be higher than INT cube, separately for each
   channel. Initial demonstrations have shown promise, but the
   robustness of this algorithm control will become clearer with more
   practical use.

   -  A high sdgain value ( > 1.0 ) has been demonstrated to
      emphasize extended emission without changing the high
      resolution structure (see the ALMA M100 example in the `Joint
      Single Dish and Interferometer Image
      Reconstruction <../../notebooks/image_combination.ipynb#Joint-Single-Dish-and-Interferometer-Image-Reconstruction>`__
      page).   However, when using a high sdgain, please remember to
      monitor the shape of the joint PSF to look for signs of angular
      resolution loss due to weighting the SD data much too high. 
   
   -  A low sdgain value ( < 1.0 ) has also been shown to be useful
      in reducing the effect of the usually high SD noise in the
      joint reconstruction while still preserving flux correctness
      (see the `algorithm publication <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta>`_).
      This mode could be useful when the SD image signal-to-noise
      ratio is high enough to match that of the interferometer
      images, even if the rms noise of the SD data is higher than the
      INT image rms (which can happen when the flux of the SD data is
      higher than that of the INT data).

   .. rubric:: Imaging and Deconvolution Options
   
   Parameters that control interferometer-gridding/imaging and
   deconvolution options are *specmode, gridder, deconvolver* (and
   associated sub-parameters similar to **tclean**).
   
   -  **Specmode** : Supported modes include  *specmode='cube' * with
      any single-term deconvolver, and  *specmode='mfs'* with any
      deconvolver (including multi-term). These options represent
      different conversion routines between the feathered cubes and
      the inputs/outputs for deconvolution.
   
      -  *‘cube’*: the cubes are sent as is to the deconvolver and
         the output model cube is directly passed to the major cycle.
      -  *‘mfs’*: the cubes are averaged to form a continuum image
         and continuum PSF prior to deconvolution and the model image
         is expanded out to an image model cube prior to the next
         major cycle.
      -  *‘mtmfs’*: the cubes are converted to Taylor-weighted
         averages in accordance with the MTMFS algorithm and the
         model Taylor coefficient image output from the deconvolver
         are evaluated back onto a model image cube prior to the
         major cycle. This image reshaping follows the diagram at the
         top of this page.
   
   All frequency averages in the Cube to Taylor conversions and in
   the calculation of a common Primary Beam use the interferometer
   sum-or-weight spectrum as frequency-dependent weights, multiplied
   by a 1-0 flag to identify channels with valid images in both the
   SD and INT cubes
   
   -  **Deconvolvers** : Algorithms supported are *‘multiscale',
      'hogbom’* and *'clark'* for *cube* and *mfs(nterms=1)* imaging
      and *‘mtmfs’* for multi-term mfs imaging. However, for use
      cases where single dish data are required along with
      interferometer data, multiscale deconvolution is most
      appropriate to get accurate reconstructions at multiple spatial
      scales. The *‘multiscale’* deconvolver applies to
      *specmode=’cube’* and *'mfs(nterms=1)’* and the *‘mtmfs’*
      deconvolver applies to the *specmode=’mfs(nterms>1)’*. In all
      cases, the *‘scales’* parameter is also relevant as it sets the
      list of scale sizes to use during deconvolution.The *‘hogbom’*
      deconvolver is relevant only when used with *usedata=’sdonly’*
      to deconvolve unresolved sources.
   
   -  **Gridders** :  All gridders supported by task tclean may be
      used with **sdintimaging**. Two options that represent
      different normalization schemes are *'standard'* and *'mosaic'*
      (or *'awproject'*). Similar to tclean, the  *‘standard’*
      gridder does not consider primary beams and represents one mode
      of operation that is valid only in the central region of the
      interferometer primary beam. The *‘mosaic’* and *'awproject'*
      gridders account for primary beams and are appropriate for
      full-beam or joint mosaic images.  For these two A-Projection
      gridders, the normtype is always *'flatnoise'* and conjbeams is
      implemented via an image-domain scheme not offered by task
      tclean.  **Note** also that the *‘awproject’* gridder is currently 
      unavailable with the sdintimaging task. This usage mode will be
      commissioned in a future release when it is enabled for cube 
      imaging in tclean as well. 

   
   .. rubric:: Iteration Control and Automasking
   
   Iteration contol and automasking parameters are identical to those
   used in task tclean, with the same rules and conventions applied
   to stopping criteria.

   
   .. rubric:: Output Images
   
   The initial version of the sdintimaging task produces many
   intermediate images which persist after the end of the task.  The
   naming convention of the images is more complex than the tclean
   task.
   
   +-----------------------------------+-----------------------------------+
   | <imagename>.sd.cube.{image,psf}   | Image cubes onto which the input  |
   |                                   | Single Dish image and psf cubes   |
   | <im                               | are regridded.                    |
   | agename>.sd.cube.{model,residual} |                                   |
   |                                   | Intermediate products containing  |
   |                                   | the model image cube that is      |
   |                                   | subtracted from the SD image to   |
   |                                   | make the SD residual              |
   +-----------------------------------+-----------------------------------+
   | <imagename>.int.cube.{residual,   | Image cubes made from only the    |
   | psf, sumwt,weight,pb)             | interferometer data               |
   |                                   |                                   |
   | <imagename>.int.cube.{model}      | Intermediate product. Cube model  |
   |                                   | image used for model prediction   |
   |                                   | and residual calculation.         |
   +-----------------------------------+-----------------------------------+
   | <imagename>.joint.cube.{residual, | Feathered cubes for the residual  |
   | psf}                              | and psf.   For cube minor cycles, |
   |                                   | these are also the inputs to the  |
   | <imagename>.joint.multite         | deconvolver.                      |
   | rm.{residual,psf}.{tt0,tt1[,tt2]} |                                   |
   |                                   | Multi-term residual images and    |
   |                                   | spectral PSFs constructed from    |
   |                                   | the above feathered cubes. These  |
   |                                   | are inputs to the minor cycle for |
   |                                   | multi-term deconvolution          |
   +-----------------------------------+-----------------------------------+
   | <imagename>.joint.cube.{image,    | For cube minor cycles, all        |
   | sumwt, weight, pb,model,          | standard data products            |
   | mask,pbcor}                       |                                   |
   +-----------------------------------+-----------------------------------+
   | <i                                | For multi-term minor cycles, all  |
   | magename>.joint.multiterm.{image, | standard data products            |
   | sumwt, weight, pb, model, mask,   |                                   |
   | alpha,pbcor}  with  {.tt0, .tt1,  |                                   |
   | .tt2 } extensions as appropriate. |                                   |
   +-----------------------------------+-----------------------------------+
   
   This long list of output and intermediate images is likely to be
   pruned in a future release.
   
   .. rubric:: Model Prediction
   
   For usedata=‘int’ , one may wish to save a sky model to the MeasurementSet for later use such as self-calibration.  The tclean task can be used 
   in such instances after executing sdintimaging. As described in the tclean section, model prediction can be done by running tclean by niter=0 and 
   specifying savemodel=‘modelcolumn’ or ’ virtual’. For example,
   
   ::
   
       sdintimaging(usedata=‘int’, vis=‘xxx.ms’, imagename=‘tst-intonly’, ... niter=1000, ...)
       tclean(vis=‘xxx.ms’, imagename=‘tst-intonly', ... niter=0, savemodel=‘modelcolumn’, calcpsf=False, calcres=False, restoration=False)

   
   For more information and examples on the functionality of the
   sdintimaging task, see the CASA Docs chapter page on `Joint
   Single Dish and Interferometer Image
   Reconstruction <../../notebooks/image_combination.ipynb#Joint-Single-Dish-and-Interferometer-Image-Reconstruction>`__
   
   .. |image1| image:: _apimedia/c914c39a74a69699c2ae1d84231e2133af6d7081.png
   

.. _Examples:

Examples
   To run sdintimaging with automatic SD-PSF generation, n-sigma
   stopping thresholds, a pb-based mask at the 0.3 gain level, and no
   other deconvolution masks (interactive=False).  Use the helper
   function shown below to extract frequency information from the sd
   cube to supply as input to sdintimaging.  Note that the sdimage
   cube must contain per-plane restoring beams.
   
   ::
   
      from sdint_helper import \*
      sdintlib = SDINT_helper()
      sdintlib.setup_cube_params(sdcube='M100_TP')
         Output : Shape of SD cube : [90 90  1 70]
         Coordinate ordering : ['Direction', 'Direction', 'Stokes',
         'Spectral']
         nchan = 70
         start = 114732899312.0Hz
         width = -1922516.74324Hz
         Found 70 per-plane restoring beams#
         (For specmode='mfs' in sdintimaging, please remember to set
         'reffreq' to a value within the freq range of the cube)
         Returned Dict : {'nchan': 70, 'start': '114732899312.0Hz',
         'width': '-1922516.74324Hz'}
   
      sdintimaging(usedata="sdint", sdimage="../M100_TP",
                   sdpsf="",sdgain=3.0, dishdia=12.0, vis="../M100_12m_7m",
                   imagename="try_sdint_niter5k", imsize=1000, cell="0.5arcsec",
                   phasecenter="J2000 12h22m54.936s +15d48m51.848s", stokes="I",
                   specmode="cube", reffreq="", nchan=70,
                   start="114732899312.0Hz", width="-1922516.74324Hz",
                   outframe="LSRK", veltype="radio", restfreq="115.271201800GHz",
                   interpolation="linear", perchanweightdensity=True, 
                   gridder="mosaic", mosweight=True,
                   pblimit=0.2, deconvolver="multiscale", scales=[0, 5, 10, 15, 20],
                   smallscalebias=0.0, pbcor=False, weighting="briggs",
                   robust=0.5, niter=5000, gain=0.1, threshold=0.0, nsigma=3.0,
                   interactive=False, usemask="user", mask="", pbmask=0.3)
   
   For test-results using these parameters, and for additional
   test-results, see the CASA Docs chapter page on `Joint Single Dish
   and Interferometeric Image
   Reconstruction <../../notebooks/image_combination.ipynb#Joint-Single-Dish-and-Interferometer-Image-Reconstruction>`__.
   

.. _Development:

Development
   This page gives an overview of the code design and future
   development work that needs to be done. Detailed information on
   the algorithm can be found on the chapter page on `Joint Single
   Dish and Interferometer Image
   Reconstruction <../../notebooks/image_combination.ipynb#Joint-Single-Dish-and-Interferometer-Image-Reconstruction>`__,
   while a description of the **sdintimaging** task and associated
   parameters can be found on the
   `sdintimaging <../../api/casatasks.rst>`__
   task pages.
   

   .. rubric:: Code Design

   The sdintimaging task is implemented using the PySynthesisImager
   module in CASA.
   
   **Core algorithm implementation**: sdint_imager.py and
   sdint_helper.py
   
   sdint_imager contains main setup fuctions using PySnthesisImager:
   setup_imager, setup_deconvolver, setup_sdimaging as well as main
   joint imaging alogrithm (do_reconstruct). The sdint_helper
   provides helper functions such as feathering of sd + int, single
   dish residual calculation, primary beam manipulation, checks for
   consistency between SD and INT cube coordinate systems, etc.
   
   As shown in the diagram at the top of this page, a feathering step
   is inserted in between major and minor cycles to combine SD
   residual and interferometer residual images as well as PSFs before
   deconvolution. Apart from this, standard major/minor cycle
   iterations are performed and most imaging modes of task tclean are
   preserved.  However, only the above documented subset of modes
   have been tested. 
   

   .. rubric:: Future work
   
   The following is a list of features that are either not available
   yet or currently untested with the sdintimaging task (or known
   bugs):

   -  Single Plane Imaging. The internal code assumes cubes, and the ability to work with single channel images needs more testing and debugging. 
   
   -  Use of task_deconvolve for sd only.
	
   -  Fully test and characterize ‘int-only’ as a wideband mosaic option
	
   -  Add the ability to specify only the SD image cube and have the interferometer cube coordinate system be generated to match it. 
	
   -  Improve how task feather works on cubes with per-plane restoring beams
	
   -  Understand why the feather step results in NaNs if the pblimit is set to a negative value for joint mosaic imaging of the INT data.
	
   -  Understand why feather produces ‘imageregrid’ warnings for every single run, even if the SD cell size and beam are compatible.
	
   -  Add tools to check the relative flux densities of single-dish and interferometer visibility data to verify the results of joint deconvolution and other combination techniques.
	
   -  Check if restoration can happen with niter=0.
	
   -  Use sdint_helper:: setup_cube_params() to autogenerate nchan/start/width and then remove some parameters from the sdintimaging task interface, and check for validity of the input Single Dish image and PSF cubes
	
   -  For cases where the SD PSF is not available, allow the user to specify a dish diameter and ask the task to generate an Airy Disk SD PSF cube that may be used along with the supplied SD image cube.
	
   -  If it is not possible to run ‘imregrid’, provide guidance to users on what to do.
	
   -  Connect to tsdimaging internally for ALMA data.
   
   
   



