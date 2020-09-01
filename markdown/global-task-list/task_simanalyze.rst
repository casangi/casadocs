Description
      .. rubric:: Summary
         :name: summary

      This task is for imaging and analyzing MeasurementSets (MSs)
      simulated with **simobserve** or **simalma**.

      **simanalyze** analyzes one or more MeasurementSets -
      interferometric and/or single dish, using CASA's
      `tclean <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean>`__
      task. It can also calculate and display the difference between the
      simulated observation and the original model data, and generate a
      "fidelity image". Fidelity is defined as:

      .. math:: \begin{equation} \frac{I}{|I-T|} \end{equation}

      where I is the observed image intensity and T is the true image
      intensity, given in this case by the sky model (see `ALMA memo
      398 <http://library.nrao.edu/public/memos/alma/memo398.pdf>`__ for
      description of fidelity). The input parameters are therefore
      grouped by the two main pieces of functionality:

      #. Image - Image the visibility data with CASA's
         `tclean <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean>`__
         task. Most of the parameters are passed to the wrapper method
         **simutil.imtclean**, which in turn calls **tclean**.
      #. Analyze - Calculate and display the difference between output
         and input, and the fidelity image. Different diagnostic images
         can be chosen to plot on a multi-panel figure, with the
         different show parameters. That figure can be saved as a .png
         file if *graphics='both'* or *graphics='file'*.

      The output is a synthesized image, a difference image between the
      synthesized image and your sky model convolved with the output
      synthesized beam, and a fidelity image. 

      .. note:: **NOTE**: If you prefer to run **tclean** manually (e.g., to
         interactively clean with a mask), you can do that, and then use
         **simanalyze** to convolve the sky model and create difference
         and fidelity images by setting *image=False*.

      .. rubric:: Task output
         :name: task-output

      Below is a list of the products produced by the **simanalyze**
      task. Not all of these will necessarily be produced, depending on
      the input parameters selected.

      .. note:: **NOTE**: To support various runs using differing arrays, the
         file names have the configuration name from the antenna list
         appended.

      -  [project].[cfg].skymodel.flat.regrid.conv = input sky regridded
         to match the output image, and convolved with the output clean
         beam
      -  [project].[cfg].image = synthesized image
      -  [project].[cfg].pb.pbcoverage = primary beam correction for
         mosaic image
      -  [project].[cfg].residual = residual image after cleaning
      -  [project].[cfg].tclean.last = parameter file of what parameters
         were used in the **tclean** task
      -  [project].[cfg].psf = synthesized (dirty) beam calculated from
         weighted uv distribution
      -  [project].[cfg].image.png = diagnostic figure of clean image
         and residual
      -  [project].[cfg].fidelity = fidelity image
      -  [project].[cfg].analysis.png = diagnostic figure of difference
         and fidelity
      -  [project].[cfg].simanalyze.last = saved input parameters for
         **simanalyze** task, available in CASAshell

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *project*
         :name: project

      This parameter should be set to the same name as used when running
      **simobserve** or **simalma** for the directory of results
      generated. In particular, [project]/[project].skymodel will be
      required in order to compare output and input images.

      .. note:: **NOTE**: **simanalyze** was designed to be used after one or
         more runs of **simobserve**, and as such it assumes it will be
         able to find a sky model image called
         [project]/[project].skymodel, .newmodel, or .compskymodel in
         the [project]/ subdirectory. If the simulated MS has been
         created by means other than simply calling **simobserve**, the
         user may have to copy their sky model image into the project
         subdirectory and call it [project].skymodel.

      .. rubric:: *image*
         :name: image

      This parameter determines if **simanalyze** produces images or
      not.

      .. note:: **WARNING**: As is the case for real images, cleaning images
         produced by **simobserve** can lead to a spurious decrease in
         object fluxes and noise on the image (an effect known as "clean
         bias"). This is particularly true for observations with poor
         coverage of the uv-plane, i.e., using telescopes with small
         numbers of antennas, such as the ALMA Early Science
         configurations, and/or in short "snapshot" observations. Users
         should always clean images with care, using a small number of
         iterations and/or a conservative (3-5sigma) threshold and
         boxing bright sources.

      .. rubric:: *image=True* expandable parameters
         :name: imagetrue-expandable-parameters

      .. rubric:: *vis*
         :name: vis

      Single or list of input MeasurementSets, which can include a total
      power MS. **simanalyze** will grid any total power MS, **tclean**
      (invert and deconvolve) any interferometric MSes, and **feather**
      the results. Examples: single MS: *vis="[project].alma.out03.ms"*;
      multiple MSes: *vis="[project].alma.out03.ms,
      [project].aca.tp.ms"*.

      The user can use *project* and let the task automatically replace
      it with the project name, e.g.,
      *vis="[project].noisy.ms,project.noisy.sd.ms"*. However, note that
      if you created MeasurementSet(s) using **simobserve**, the MS
      names will include the configuration, e.g.,
      [project].alma_out20.noisy.ms. Setting *vis='default'* will find
      and attempt to image all MeasurementSets (interferometric and
      single dish) in the [project]/ directory.

      .. rubric:: *modelimage*
         :name: modelimage

      It is often preferable to use a low resolution (single dish or
      synthesis) image as a prior model during clean deconvolution of a
      higher resolution interferometric MS. That is accomplished by
      putting the low-resolution image in *modelimage* and the MS to be
      deconvolved in *vis*.

      .. note:: **NOTE**: This is not the original skymodel that was used in
         simobserve or simalma. It is recommended to leave this blank
         unless the user is familiar with using a prior in clean
         deconvolution.

      .. note:: **NOTE 2**: *modelimage* will not be used if the MS to be
         imaged is total power.

      .. rubric:: *imsize*
         :name: imsize

      The output image size in pixels (x,y), or set to 0 to match model
      (default). Examples: *imsize=[500,500]* or *imsize=500* result in
      the same image size.

      .. rubric:: *imdirection*
         :name: imdirection

      Sets the output image direction. If left unset (default), the
      model center will be used. Examples: *imdirection='J2000
      10h00m00.0s -30d00m00.0s'*

      .. rubric:: *cell*
         :name: cell

      Sets the cell size of the image with units. If left unset
      (default), the model cell size will be used. Examples:
      *cell='10arcsec'*

      .. rubric:: *interactive*
         :name: interactive

      Turns interactive cleaning off or on. The default setting for this
      parameter is *interactive=False* (no interactive cleaning). If
      True, make sure to set *niter>0*.

      .. rubric:: *niter*
         :name: niter

      The maximum number of iterations to perform. This value can be
      changed for interactive cleaning (*interactive=True*) in the
      viewer GUI. Examples: *niter=5000*

      .. rubric:: *threshold*
         :name: threshold

      This parameter sets the upper threshold for cleaning (**clean**
      will stop if this level is reached). The default is 0.1 mJy.
      Examples: *threshold='0.5mJy'*

      .. rubric:: *weighting*
         :name: weighting

      This parameter sets the weighting that is to be applied to the
      visibility data. Options: 'natural' (+2.0 robust, default),
      'uniform' (-2.0 robust), or 'briggs'. If 'briggs' weighting is
      selected, the default robust factor of **tclean** will be used
      (0.5) and changing this parameter value is not supported by
      **simanalyze**. If a robust weighting is needed that is not
      available, it is suggested to set *image* to False and to clean
      manually with **clean**/**tclean**.

      .. rubric:: *mask*
         :name: mask

      Specification of cleanbox(es), mask image(s), primary beam
      coverage level, and/or region(s) to be used for cleaning.
      **clean** tends to perform better and is less likely to diverge if
      the clean component placement is limited by a mask to where real
      emission is expected to be. Examples: pixel ranges
      *mask=[110,110,150,145];* filename of mask image
      *mask='myimage.mask'*; or a file with mask regions
      *mask='mymask.txt'*.

      .. rubric:: *outertaper*
         :name: outertaper

      *outertaper* sets an outer threshold on baselines in the uv-plane,
      usually to achieve a lower angular resolution and to recover more
      extended emission that may be resolved out. Examples:
      *outertaper=[ ]* no outer taper applied; *outertaper=[’5klambda’]*
      circular uv taper FWHM at 5 kilo-lambda;
      *outertaper=[’5klambda’,’3klambda’,’45.0deg’*] elliptical
      Gaussian; *outertaper=[’10arcsec’]* on-sky FWHM of 10 arcsecs;
      *outertaper=[’300.0’]* 300m in aperture plane

      .. rubric:: *pbcor*
         :name: pbcor

      The *pbcor* parameter determines whether or not **simanalyze**
      corrects the flux based on the primary beam. If *pbcor=True*, a
      .pbcor image will be produced with the primary beam correction
      applied. This is set to True by default.

      .. rubric:: *stokes*
         :name: stokes

      The *stokes* parameter specifies the Stokes parameters for the
      resulting images. Note that forming Stokes Q and U images requires
      the presence of cross-hand polarizations (e.g. RL and LR for
      circularly polarized systems such as the VLA) in the data. Stokes
      V requires both parallel hands (RR and LL) for
      circularly-polarized systems or the cross-hands (XY and YX) for
      linearly polarized systems such as ALMA and ATCA. Examples:
      *stokes = ’I’* intensity only (default); *stokes = ’IQU’*
      intensity and linear polarization; *stokes = ’IV’* intensity and
      circular polarization; *stokes = ’IQUV’* all Stokes imaging;
      *stokes = ’RR’* right hand polarization only; *stokes = ’XXYY’*
      both linear polarizations

      .. rubric:: *featherimage*
         :name: featherimage

      Sometimes it is preferable to grid the single dish MS using the
      **sdimaging** task for more control. In that case, the user can
      input the resulting single dish imaging under *featherimage*, only
      put interferometric MSs in *vis*, and **simanalyze** will clean
      the interferometric and feather with the *featherimage*.

       

      .. rubric:: *image=False* expandable parameters
         :name: imagefalse-expandable-parameters

      .. rubric:: *imagename*
         :name: imagename

      If the user already has a synthesized image they wish to use, it
      can be input using the parameter *imagename*.

      .. rubric:: *skymodel*
         :name: skymodel

      **simanalyze** will attempt to find an appropriate skymodel image
      - this is the \*.skymodel image created by **simobserve** or
      **simalma**, the (optionally rescaled) original sky model which
      was used to create the MeasurementSet. If a *skymodel* is not
      explicitedly assigned, **simanalyze** will look in the project
      directory.

       

      .. rubric:: *analyze*
         :name: analyze

      This parameter is used to turn on or off the creation of
      analytical images pertaining to the simulation.

      .. rubric:: analyze=True expandable parameters
         :name: analyzetrue-expandable-parameters

      When the *analyze* parameter is set to True, **simanalyze** will
      display the first 6 of the following analysis images, based on
      whether the sub-parameters are set to True or False. An image will
      also be created of the difference between the input skymodel and
      the simulated output image (whether that output image is being
      generated in the same call to **simanalyze**, with *image=True*,
      or has already been generated, and **simanalyze** is being called
      with *image=False*).

      .. rubric:: *showuv*
         :name: showuv

      Displays a plot of the uv coverage for the simulation.

      .. rubric:: *showpsf*
         :name: showpsf

      Displays a synthesized (dirty) beam (ignored in single dish
      simulation).

      .. rubric:: *showmodel*
         :name: showmodel

      Displays the sky model at its original resolution.

      .. rubric:: *showconvolved*
         :name: showconvolved

      Displays the sky model convolved with an output beam.

      .. rubric:: *showclean*
         :name: showclean

      Displays the synthesized image.

      .. rubric:: *showresidual*
         :name: showresidual

      Displays the clean residual image (ignored in single dish
      simulation).

      .. rubric:: *showdifference*
         :name: showdifference

      Displays the difference between output cleaned image and input
      model sky image convolved with an output clean beam.

      .. rubric:: *showfidelity*
         :name: showfidelity

      Displays the fidelity image. The fidelity image is defined by the
      following equation:

      :math:`fidelity = \frac{| input |}{max[| input-output |  0.7*rms(output)]}`

      .. note:: **NOTE**: The RMS is calculated in the lower quarter of the
         image which is likely not the best choice. It is encouraged to
         measure RMS manually in an off-source region using the
         **viewer**.

       

      .. rubric:: *graphics*
         :name: graphics

      Displays graphics based on the manner in which the parameter is
      set. Options: 'screen', 'file', 'both', 'none'

      .. rubric:: *verbose*
         :name: verbose

      Turns on or off the reporting of task activity in the log.
      Examples: *verbose=False* (default)

      .. rubric:: *overwrite*
         :name: overwrite

      If the user would like **simanalyze** to replace the previously
      created files starting with the *project* name, set this parameter
      to True (default).

      .. rubric:: *dryrun*
         :name: dryrun

      *dryrun=True* is an advanced technical mode only useful for
      interferometric (not single dish) data.

      .. rubric:: *logfile*
         :name: logfile

      Allows for a user-defined log file naming convention if
      *verbose=True*.
