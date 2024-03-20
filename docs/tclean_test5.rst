tclean -- Radio Interferometric Image Reconstruction -- imaging task
=======================================

Description
---------------------------------------
Form images from visibilities and reconstruct a sky model.
                         This task handles continuum images and spectral line cubes,
                         supports outlier fields, contains standard clean based algorithms
                         along with algorithms for multi-scale and wideband image
                         reconstruction, widefield imaging correcting for the w-term,
                         full primary-beam imaging and joint mosaic imaging (with
                         heterogeneous array support for ALMA).




Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input visibility file(s)
   * - selectdata
     - :code:`True`
     - Enable data selection parameters
   * - field
     - :code:`''`
     - field(s) to select
   * - spw
     - :code:`''`
     - spw(s)/channels to select
   * - timerange
     - :code:`''`
     - Range of time to select from data
   * - uvrange
     - :code:`''`
     - Select data within uvrange
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - scan
     - :code:`''`
     - Scan number range
   * - observation
     - :code:`''`
     - Observation ID range
   * - intent
     - :code:`''`
     - Scan Intent(s)
   * - datacolumn
     - :code:`'corrected'`
     - Data column to image(data,corrected)
   * - imagename
     - :code:`''`
     - Pre-name of output images
   * - imsize
     - :code:`numpy.array( [  ] )`
     - Number of pixels
   * - cell
     - :code:`numpy.array( [  ] )`
     - Cell size
   * - phasecenter
     - :code:`''`
     - Phase center of the image
   * - stokes
     - :code:`'I'`
     - Stokes Planes to make
   * - projection
     - :code:`'SIN'`
     - Coordinate projection
   * - startmodel
     - :code:`''`
     - Name of starting model image
   * - specmode
     - :code:`'mfs'`
     - Spectral definition mode (mfs,cube,cubedata, cubesource)
   * - reffreq
     - :code:`''`
     - Reference frequency
   * - nchan
     - :code:`int(-1)`
     - Number of channels in the output image
   * - start
     - :code:`''`
     - First channel (e.g. start=3,start=\'1.1GHz\',start=\'15343km/s\')
   * - width
     - :code:`''`
     - Channel width (e.g. width=2,width=\'0.1MHz\',width=\'10km/s\')
   * - outframe
     - :code:`'LSRK'`
     - Spectral reference frame in which to interpret \'start\' and \'width\'
   * - veltype
     - :code:`'radio'`
     - Velocity type (radio, z, ratio, beta, gamma, optical)
   * - restfreq
     - :code:`numpy.array( [  ] )`
     - List of rest frequencies
   * - interpolation
     - :code:`'linear'`
     - Spectral interpolation (nearest,linear,cubic)
   * - perchanweightdensity
     - :code:`True`
     - whether to calculate weight density per channel in Briggs style weighting or not
   * - gridder
     - :code:`'standard'`
     - Gridding options (standard, wproject, widefield, mosaic, awproject)
   * - facets
     - :code:`int(1)`
     - Number of facets on a side
   * - psfphasecenter
     - :code:`''`
     - optional direction to calculate psf for mosaic (default is image phasecenter)
   * - chanchunks
     - :code:`int(1)`
     - Number of channel chunks
   * - wprojplanes
     - :code:`int(1)`
     - Number of distinct w-values for convolution functions
   * - vptable
     - :code:`''`
     - Name of Voltage Pattern table
   * - mosweight
     - :code:`True`
     - Indepently weight each field in a mosaic
   * - aterm
     - :code:`True`
     - Use aperture illumination functions during gridding
   * - psterm
     - :code:`False`
     - Use prolate spheroidal during gridding
   * - wbawp
     - :code:`True`
     - Use wideband A-terms
   * - conjbeams
     - :code:`False`
     - Use conjugate frequency for wideband A-terms
   * - cfcache
     - :code:`''`
     - Convolution function cache directory name
   * - usepointing
     - :code:`False`
     - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.
   * - computepastep
     - :code:`float(360.0)`
     - Parallactic angle interval after the AIFs are recomputed (deg)
   * - rotatepastep
     - :code:`float(360.0)`
     - Parallactic angle interval after which the nearest AIF is rotated (deg)
   * - pointingoffsetsigdev
     - :code:`numpy.array( [  ] )`
     - Pointing offset threshold to determine heterogeneity of pointing corrections for the AWProject gridder
   * - pblimit
     - :code:`float(0.2)`
     - PB gain level at which to cut off normalizations
   * - normtype
     - :code:`'flatnoise'`
     - Normalization type (flatnoise, flatsky,pbsquare)
   * - deconvolver
     - :code:`'hogbom'`
     - Minor cycle algorithm (hogbom,clark,multiscale,mtmfs,mem,clarkstokes)
   * - scales
     - :code:`numpy.array( [  ] )`
     - List of scale sizes (in pixels) for multi-scale algorithms
   * - nterms
     - :code:`int(2)`
     - Number of Taylor coefficients in the spectral model
   * - smallscalebias
     - :code:`float(0.0)`
     - Biases the scale selection when using multi-scale or mtmfs deconvolvers
   * - restoration
     - :code:`True`
     - Do restoration steps (or not)
   * - restoringbeam
     - :code:`numpy.array( [  ] )`
     - Restoring beam shape to use. Default is the PSF main lobe
   * - pbcor
     - :code:`False`
     - Apply PB correction on the output restored image
   * - outlierfile
     - :code:`''`
     - Name of outlier-field image definitions
   * - weighting
     - :code:`'natural'`
     - Weighting scheme (natural,uniform,briggs, briggsabs[experimental])
   * - robust
     - :code:`float(0.5)`
     - Robustness parameter
   * - noise
     - :code:`'1.0Jy'`
     - noise parameter for briggs abs mode weighting
   * - npixels
     - :code:`int(0)`
     - Number of pixels to determine uv-cell size
   * - uvtaper
     - :code:`numpy.array( [ '' ] )`
     - uv-taper on outer baselines in uv-plane
   * - niter
     - :code:`int(0)`
     - Maximum number of iterations
   * - gain
     - :code:`float(0.1)`
     - Loop gain
   * - threshold
     - :code:`float(0.0)`
     - Stopping threshold
   * - nsigma
     - :code:`float(0.0)`
     - Multiplicative factor for rms-based threshold stopping
   * - cycleniter
     - :code:`int(-1)`
     - Maximum number of minor-cycle iterations
   * - cyclefactor
     - :code:`float(1.0)`
     - Scaling on PSF sidelobe level to compute the minor-cycle stopping threshold.
   * - minpsffraction
     - :code:`float(0.05)`
     - PSF fraction that marks the max depth of cleaning in the minor cycle
   * - maxpsffraction
     - :code:`float(0.8)`
     - PSF fraction that marks the minimum depth of cleaning in the minor cycle
   * - interactive
     - :code:`False`
     - Modify masks and parameters at runtime
   * - usemask
     - :code:`'user'`
     - Type of mask(s) for deconvolution:  user, pb, or auto-multithresh
   * - mask
     - :code:`''`
     - Mask (a list of image name(s) or region file(s) or region string(s) )
   * - pbmask
     - :code:`float(0.0)`
     - primary beam mask
   * - sidelobethreshold
     - :code:`float(3.0)`
     - sidelobethreshold *  the max sidelobe level * peak residual
   * - noisethreshold
     - :code:`float(5.0)`
     - noisethreshold * rms in residual image + location(median)
   * - lownoisethreshold
     - :code:`float(1.5)`
     - lownoisethreshold * rms in residual image + location(median)
   * - negativethreshold
     - :code:`float(0.0)`
     - negativethreshold * rms in residual image + location(median)
   * - smoothfactor
     - :code:`float(1.0)`
     - smoothing factor in a unit of the beam
   * - minbeamfrac
     - :code:`float(0.3)`
     - minimum beam fraction for pruning
   * - cutthreshold
     - :code:`float(0.01)`
     - threshold to cut the smoothed mask to create a final mask
   * - growiterations
     - :code:`int(75)`
     - number of binary dilation iterations for growing the mask
   * - dogrowprune
     - :code:`True`
     - Do pruning on the grow mask
   * - minpercentchange
     - :code:`float(-1.0)`
     - minimum percentage change in mask size (per channel plane) to trigger updating of mask by automask
   * - verbose
     - :code:`False`
     - True: print more automasking information in the logger
   * - fastnoise
     - :code:`True`
     - True: use the faster (old) noise calculation. False: use the new improved noise calculations
   * - restart
     - :code:`True`
     - True : Re-use existing images. False : Increment imagename
   * - savemodel
     - :code:`'none'`
     - Options to save model visibilities (none, virtual, modelcolumn)
   * - calcres
     - :code:`True`
     - Calculate initial residual image
   * - calcpsf
     - :code:`True`
     - Calculate PSF
   * - parallel
     - :code:`False`
     - Run major cycles in parallel

