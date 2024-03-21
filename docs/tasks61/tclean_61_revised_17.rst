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

Parameter Explanations
=======================================



vis
---------------------------------------

Name(s) of input visibility file(s)
               default: none;
               example: vis='ngc5921.ms'
                        vis=['ngc5921a.ms','ngc5921b.ms']; multiple MSes



selectdata
---------------------------------------

Enable data selection parameters.



field
---------------------------------------

 Select fields to image or mosaic.  Use field id(s) or name(s).
                  ['go listobs' to obtain the list id's or names]
               default: ''= all fields
                 If field string is a non-negative integer, it is assumed to
                 be a field index otherwise, it is assumed to be a
                 field name
                 field='0~2'; field ids 0,1,2
                 field='0,4,5~7'; field ids 0,4,5,6,7
                 field='3C286,3C295'; field named 3C286 and 3C295
                 field = '3,4C*'; field id 3, all names starting with 4C
                 For multiple MS input, a list of field strings can be used:
                 field = ['0~2','0~4']; field ids 0-2 for the first MS and 0-4
                         for the second
                 field = '0~2'; field ids 0-2 for all input MSes




spw
---------------------------------------

 Select spectral window/channels
               NOTE: channels de-selected here will contain all zeros if
                         selected by the parameter mode subparameters.
               default: ''=all spectral windows and channels
                 spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                 spw='0:5~61'; spw 0, channels 5 to 61
                 spw=' 2';   spectral windows less than 2 (i.e. 0,1)
                 spw='0,10,3:3~45'; spw 0,10 all channels, spw 3,
                                    channels 3 to 45.
                 spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                 For multiple MS input, a list of spw strings can be used:
                 spw=['0','0~3']; spw ids 0 for the first MS and 0-3 for the second
                 spw='0~3' spw ids 0-3 for all input MS
                 spw='3:10~20;50~60' for multiple channel ranges within spw id 3
                 spw='3:10~20;50~60,4:0~30' for different channel ranges for spw ids 3 and 4
                 spw='0:0~10,1:20~30,2:1;2;3'; spw 0, channels 0-10,
                      spw 1, channels 20-30, and spw 2, channels, 1,2 and 3
                 spw='1~4;6:15~48' for channels 15 through 48 for spw ids 1,2,3,4 and 6




timerange
---------------------------------------

Range of time to select from data

                   default: '' (all); examples,
                   timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                   Note: if YYYY/MM/DD is missing date defaults to first
                         day in data set
                   timerange='09:14:0~09:54:0' picks 40 min on first day
                   timerange='25:00:00~27:30:00' picks 1 hr to 3 hr
                             30min on NEXT day
                   timerange='09:44:00' pick data within one integration
                             of time
                   timerange='  10:24:00' data after this time
                   For multiple MS input, a list of timerange strings can be
                   used:
                   timerange=['09:14:0~09:54:0','  10:24:00']
                   timerange='09:14:0~09:54:0''; apply the same timerange for
                                                 all input MSes




uvrange
---------------------------------------

Select data within uvrange (default unit is meters)
                   default: '' (all); example:
                   uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                   uvrange='  4klambda';uvranges greater than 4 kilo lambda
                   For multiple MS input, a list of uvrange strings can be
                   used:
                   uvrange=['0~1000klambda','100~1000klamda']
                   uvrange='0~1000klambda'; apply 0-1000 kilo-lambda for all
                                            input MSes
 


antenna
---------------------------------------

Select data based on antenna/baseline

                   default: '' (all)
                   If antenna string is a non-negative integer, it is
                   assumed to be an antenna index, otherwise, it is
                   considered an antenna name.
                   antenna='5 6'; baseline between antenna index 5 and
                                 index 6.
                   antenna='VA05 VA06'; baseline between VLA antenna 5
                                       and 6.
                   antenna='5 6;7 8'; baselines 5-6 and 7-8
                   antenna='5'; all baselines with antenna index 5
                   antenna='05'; all baselines with antenna number 05
                                (VLA old name)
                   antenna='5,6,9'; all baselines with antennas 5,6,9
                                   index number
                   For multiple MS input, a list of antenna strings can be
                   used:
                   antenna=['5','5 6'];
                   antenna='5'; antenna index 5 for all input MSes
                   antenna='!DV14'; use all antennas except DV14




scan
---------------------------------------

Scan number range

                   default: '' (all)
                   example: scan='1~5'
                   For multiple MS input, a list of scan strings can be used:
                   scan=['0~100','10~200']
                   scan='0~100; scan ids 0-100 for all input MSes




observation
---------------------------------------

Observation ID range
                   default: '' (all)
                   example: observation='1~5'



intent
---------------------------------------

Scan Intent(s)

                   default: '' (all)
                   example: intent='TARGET_SOURCE'
                   example: intent='TARGET_SOURCE1,TARGET_SOURCE2'
                   example: intent='TARGET_POINTING*'



datacolumn
---------------------------------------

Data column to image (data or observed, corrected)
                     default:'corrected'
                     ( If 'corrected' does not exist, it will use 'data' instead )




imagename
---------------------------------------

Pre-name of output images

                       example : imagename='try'

                       Output images will be (a subset of) :

                       try.psf              - Point spread function
                       try.residual      - Residual image
                       try.image         - Restored image
                       try.model         - Model image (contains only flux components)
                       try.sumwt        - Single pixel image containing sum-of-weights.
                                                 (for natural weighting, sensitivity=1/sqrt(sumwt))
                       try.pb              - Primary beam model (values depend on the gridder used)

                       Widefield projection algorithms (gridder=mosaic,awproject) will
                       compute the following images too.
                       try.weight        - FT of gridded weights or the
                                                 un-normalized sum of PB-square (for all pointings)
                                                 Here, PB = sqrt(weight) normalized to a maximum of 1.0

                       For multi-term wideband imaging, all relevant images above will
                       have additional .tt0,.tt1, etc suffixes to indicate Taylor terms,
                       plus the following extra output images.
                       try.alpha            - spectral index
                       try.alpha.error   - estimate of error on spectral index
                       try.beta              - spectral curvature (if nterms \  2)

                       Tip : Include a directory name in 'imagename' for all
                               output images to be sent there instead of the
                               current working directory : imagename='mydir/try'

                       Tip : Restarting an imaging run without changing 'imagename'
                               implies continuation from the existing model image on disk.
                                - If 'startmodel' was initially specified it needs to be set to 
                                  for the restart run (or tclean will exit with an error message).
                                - By default, the residual image and psf will be recomputed
                                  but if no changes were made to relevant parameters between
                                  the runs, set calcres=False, calcpsf=False to resume directly from
                                  the minor cycle without the (unnecessary) first major cycle.
                                To automatically change 'imagename' with a numerical
                                increment, set restart=False (see tclean docs for 'restart').

                        Note : All imaging runs will by default produce restored images.
                                  For a niter=0 run, this will be redundant and can optionally
                                  be turned off via the 'restoration=T/F' parameter.




imsize
---------------------------------------

Number of pixels
         example :  imsize = [350,250]
                           imsize = 500 is equivalent to [500,500]
         To take proper advantage of internal optimized FFT routines, the
         number of pixels must be even and factorizable by 2,3,5,7 only.



cell
---------------------------------------

Cell size
               example: cell=['0.5arcsec,'0.5arcsec'] or
               cell=['1arcmin', '1arcmin']
               cell = '1arcsec' is equivalent to ['1arcsec','1arcsec']



phasecenter
---------------------------------------

Phase center of the image (string or field id); if the phasecenter is the name known major solar system object ('MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO', 'SUN', 'MOON') or is an ephemerides table then that source is tracked and the background sources get smeared. There is a special case, when phasecenter='TRACKFIELD', which will use the ephemerides or polynomial phasecenter in the FIELD table of the MS's as the source center to track.
               example: phasecenter=6
                        phasecenter='J2000 19h30m00 -40d00m00'
                        phasecenter='J2000 292.5deg  -40.0deg'
                        phasecenter='J2000 5.105rad  -0.698rad'
                        phasecenter='ICRS 13:05:27.2780 -049.28.04.458'
                        phasecenter='myComet_ephem.tab'
                        phasecenter='MOON'
                        phasecenter='TRACKFIELD'



stokes
---------------------------------------

Stokes Planes to make
               default='I'; example: stokes='IQUV';
                 Options: 'I','Q','U','V','IV','QU','IQ','UV','IQUV','RR','LL','XX','YY','RRLL','XXYY','pseudoI'

                             Note : Due to current internal code constraints, if any correlation pair
                                        is flagged, by default, no data for that row in the MS will be used.
                                        So, in an MS with XX,YY, if only YY is flagged, neither a
                                        Stokes I image nor an XX image can be made from those data points.
                                        In such a situation, please split out only the unflagged correlation into
                                        a separate MS.

                             Note : The 'pseudoI' option is a partial solution, allowing Stokes I imaging
                                    when either of the parallel-hand correlations are unflagged.

                             The remaining constraints shall be removed (where logical) in a future release.




projection
---------------------------------------

Coordinate projection
                     Examples : SIN,   NCP
                     A list of supported (but untested) projections can be found here :
                     http://casa.nrao.edu/active/docs/doxygen/html/classcasa_1_1Projection.html#a3d5f9ec787e4eabdce57ab5edaf7c0cd






startmodel
---------------------------------------

Name of starting model image

                      The contents of the supplied starting model image will be
                      copied to the imagename.model before the run begins.

                      example : startmodel = 'singledish.im'

                      For deconvolver='mtmfs', one image per Taylor term must be provided.
                      example : startmodel = ['try.model.tt0', 'try.model.tt1']
                                      startmodel = ['try.model.tt0']  will use a starting model only
                                                           for the zeroth order term.
                                      startmodel = ['','try.model.tt1']  will use a starting model only
                                                           for the first order term.

                       This starting model can be of a different image shape and size from
                       what is currently being imaged. If so, an image regrid is first triggered
                       to resample the input image onto the target coordinate system.

                       A common usage is to set this parameter equal to a single dish image

                       Negative components in the model image will be included as is.

                      [ Note : If an error occurs during image resampling/regridding,
                                   please try using task imregrid to resample the starting model
                                   image onto a CASA image with the target shape and
                                   coordinate system before supplying it via startmodel ]

 


specmode
---------------------------------------

Spectral definition mode (mfs,cube,cubedata, cubesource)

                       mode='mfs' : Continuum imaging with only one output image channel.
                                             (mode='cont' can also be used here)

                       mode='cube' : Spectral line imaging with one or more channels
                                               Parameters start, width,and nchan define the spectral
                                               coordinate system and can be specified either in terms
                                               of channel numbers, frequency or velocity in whatever
                                               spectral frame is specified in 'outframe'.
                                               All internal and output images are made with outframe as the
                                               base spectral frame. However imaging code internally uses the fixed
                                               spectral frame, LSRK for automatic internal software
                                               Doppler tracking so that a spectral line observed over an
                                               extended time range will line up appropriately.
                                               Therefore the output images have additional spectral frame conversion
                                               layer in LSRK on the top the base frame.


                                               (Note : Even if the input parameters are specified in a frame
                                                           other than LSRK, the viewer still displays spectral
                                                           axis in LSRK by default because of the conversion frame
                                                           layer mentioned above. The viewer can be used to relabel
                                                           the spectral axis in any desired frame - via the spectral
                                                           reference option under axis label properties in the
                                                           data display options window.)


                                               

                        mode='cubedata' : Spectral line imaging with one or more channels
                                                        There is no internal software Doppler tracking so
                                                        a spectral line observed over an extended time range
                                                        may be smeared out in frequency. There is strictly
                                                        no valid spectral frame with which to label the output
                                                        images, but they will list the frame defined in the MS.

                                                        mode='cubesource': Spectral line imaging while
                                                        tracking moving source (near field or solar system
                                                        objects). The velocity of the source is accounted
                                                        and the frequency reported is in the source frame.
                                                        As there is not SOURCE frame defined,
                                                        the frame reported will be REST (as it may not be
                                                        in the rest frame emission region may be
                                                        moving w.r.t the systemic velocity frame)





reffreq
---------------------------------------

Reference frequency of the output image coordinate system

                       Example :  reffreq='1.5GHz'    as a string with units.

                       By default, it is calculated as the middle of the selected frequency range.

                       For deconvolver='mtmfs' the Taylor expansion is also done about
                       this specified reference frequency.




nchan
---------------------------------------

Number of channels in the output image
                       For default (=-1), the number of channels will be automatically determined
                       based on data selected by 'spw' with 'start' and 'width'.
                       It is often easiest to leave nchan at the default value.
                       example: nchan=100




niter
---------------------------------------

Maximum number of iterations

                       A stopping criterion based on total iteration count.
                       Currently the parameter type is defined as an integer therefore the integer value 
                       larger than 2147483647 will not be set properly as it causes an overflow.

                       Iterations are typically defined as the selecting one flux component
                       and partially subtracting it out from the residual image.

                       niter=0 : Do only the initial major cycle (make dirty image, psf, pb, etc)

                       niter larger than zero : Run major and minor cycles.

                       Note : Global stopping criteria vs major-cycle triggers

                                  In addition to global stopping criteria, the following rules are
                                  used to determine when to terminate a set of minor cycle iterations
                                  and trigger major cycles [derived from Cotton-Schwab Clean, 1984]

                                  'cycleniter' : controls the maximum number of iterations per image
                                                      plane before triggering a major cycle.
                                  'cyclethreshold' : Automatically computed threshold related to the
                                                              max sidelobe level of the PSF and peak residual.
                                   Divergence, detected as an increase of 10 percent in peak residual from the
                                   minimum so far (during minor cycle iterations)

                                   The first criterion to be satisfied takes precedence.

                       Note :  Iteration counts for cubes or multi-field images :
                                   For images with multiple planes (or image fields) on which the
                                   deconvolver operates in sequence, iterations are counted across
                                   all planes (or image fields). The iteration count is compared with
                                   'niter' only after all channels/planes/fields have completed their
                                   minor cycles and exited either due to 'cycleniter' or 'cyclethreshold'.
                                   Therefore, the actual number of iterations reported in the logger
                                   can sometimes be larger than the user specified value in 'niter'.
                                   For example, with niter=100, cycleniter=20,nchan=10,threshold=0,
                                   a total of 200 iterations will be done in the first set of minor cycles
                                   before the total is compared with niter=100 and it exits.

                        Note : Additional global stopping criteria include
                                  - no change in peak residual across two major cycles
                                  - a 50 percent or more increase in peak residual across one major cycle





gain
---------------------------------------

Loop gain

                       Fraction of the source flux to subtract out of the residual image
                       for the CLEAN algorithm and its variants.

                       A low value (0.2 or less) is recommended when the sky brightness
                       distribution is not well represented by the basis functions used by
                       the chosen deconvolution algorithm. A higher value can be tried when
                       there is a good match between the true sky brightness structure and
                       the basis function shapes.  For example, for extended emission,
                       multiscale clean with an appropriate set of scale sizes will tolerate
                       a higher loop gain than Clark clean (for example).

                       




threshold
---------------------------------------

Stopping threshold (number in units of Jy, or string)

                      A global stopping threshold that the peak residual (within clean mask)
                      across all image planes is compared to.

                      threshold = 0.005  : 5mJy
                      threshold = '5.0mJy'

                      Note : A 'cyclethreshold' is internally computed and used as a major cycle
                                 trigger. It is related what fraction of the PSF can be reliably
                                 used during minor cycle updates of the residual image. By default
                                 the minor cycle iterations terminate once the peak residual reaches
                                 the first sidelobe level of the brightest source.

                                 'cyclethreshold' is computed as follows using the settings in
                                  parameters 'cyclefactor','minpsffraction','maxpsffraction','threshold' :

                                psf_fraction = max_psf_sidelobe_level * 'cyclefactor'
                                psf_fraction = max(psf_fraction, 'minpsffraction');
                                psf_fraction = min(psf_fraction, 'maxpsffraction');
                                cyclethreshold = peak_residual * psf_fraction
                                cyclethreshold = max( cyclethreshold, 'threshold' )

                                If nsigma is set ( 0.0), the N-sigma threshold is calculated (see
                                the description under nsigma), then cyclethreshold is further modified as,

                                cyclethreshold = max( cyclethreshold, nsgima_threshold )


                                'cyclethreshold' is made visible and editable only in the
                                interactive GUI when tclean is run with interactive=True.



nsigma
---------------------------------------

Multiplicative factor for rms-based threshold stopping

                       N-sigma threshold is calculated as nsigma * rms value per image plane determined
                       from a robust statistics. For nsigma   0.0, in a minor cycle, a maximum of the two values,
                       the N-sigma threshold and cyclethreshold, is used to trigger a major cycle
                       (see also the descreption under 'threshold').
                       Set nsigma=0.0 to preserve the previous tclean behavior without this feature.
                       The top level parameter, fastnoise is relevant for the rms noise calculation which is used 
                       to determine the threshold. 




cycleniter
---------------------------------------

Maximum number of minor-cycle iterations (per plane) before triggering
                       a major cycle

                       For example, for a single plane image, if niter=100 and cycleniter=20,
                       there will be 5 major cycles after the initial one (assuming there is no
                       threshold based stopping criterion). At each major cycle boundary, if
                       the number of iterations left over (to reach niter) is less than cycleniter,
                       it is set to the difference.

                       Note : cycleniter applies per image plane, even if cycleniter x nplanes
                                  gives a total number of iterations greater than 'niter'. This is to
                                  preserve consistency across image planes within one set of minor
                                  cycle iterations.




cyclefactor
---------------------------------------

Scaling on PSF sidelobe level to compute the minor-cycle stopping threshold.

                       Please refer to the Note under the documentation for 'threshold' that
                       discussed the calculation of 'cyclethreshold'

                       cyclefactor=1.0 results in a cyclethreshold at the first sidelobe level of
                       the brightest source in the residual image before the minor cycle starts.

                       cyclefactor=0.5 allows the minor cycle to go deeper.
                       cyclefactor=2.0 triggers a major cycle sooner.




minpsffraction
---------------------------------------

PSF fraction that marks the max depth of cleaning in the minor cycle

                       Please refer to the Note under the documentation for 'threshold' that
                       discussed the calculation of 'cyclethreshold'

                       For example, minpsffraction=0.5 will stop cleaning at half the height of
                       the peak residual and trigger a major cycle earlier.




maxpsffraction
---------------------------------------

PSF fraction that marks the minimum depth of cleaning in the minor cycle

                       Please refer to the Note under the documentation for 'threshold' that
                       discussed the calculation of 'cyclethreshold'

                       For example, maxpsffraction=0.8 will ensure that at least the top 20
                       percent of the source will be subtracted out in the minor cycle even if
                       the first PSF sidelobe is at the 0.9 level (an extreme example), or if the
                       cyclefactor is set too high for anything to get cleaned.




interactive
---------------------------------------

Modify masks and parameters at runtime

                       interactive=True will trigger an interactive GUI at every major cycle
                       boundary (after the major cycle and before the minor cycle).

                       The interactive mode is currently not available for parallel cube imaging (please also
                       refer to the Note under the documentation for 'parallel' below).

                       Options for runtime parameter modification are :

                       Interactive clean mask : Draw a 1/0 mask (appears as a contour) by hand.
                                                              If a mask is supplied at the task interface or if
                                                              automasking is invoked, the current mask is
                                                              displayed in the GUI and is available for manual
                                                              editing.

                                                              Note : If a mask contour is not visible, please
                                                                         check the cursor display at the bottom of
                                                                         GUI to see which parts of the mask image
                                                                         have ones and zeros. If the entire mask=1
                                                                         no contours will be visible.


                       Operation buttons :  -- Stop execution now (restore current model and exit)
                                                        -- Continue on until global stopping criteria are reached
                                                           without stopping for any more interaction
                                                        -- Continue with minor cycles and return for interaction
                                                            after the next major cycle.

                       Iteration control : -- max cycleniter :  Trigger for the next major cycle

                                                                                   The display begins with
                                                                                   [ min( cycleniter, niter - itercount ) ]
                                                                                   and can be edited by hand.

                                                    -- iterations left :  The display begins with [niter-itercount ]
                                                                                and can be edited to increase or
                                                                                decrease the total allowed niter.

                                                    -- threshold : Edit global stopping threshold

                                                    -- cyclethreshold : The display begins with the
                                                                                  automatically computed value
                                                                                  (see Note in help for 'threshold'),
                                                                                  and can be edited by hand.

                                                    All edits will be reflected in the log messages that appear
                                                    once minor cycles begin.


                       [ For scripting purposes, replacing True/False with 1/0 will get tclean to
                         return an imaging summary dictionary to python ]




usemask
---------------------------------------

Type of mask(s) to be used for deconvolution

                       user: (default) mask image(s) or user specified region file(s) or string CRTF expression(s)
                         subparameters: mask, pbmask
                       pb: primary beam mask
                         subparameter: pbmask

                           Example: usemask=pb, pbmask=0.2
                                             Construct a mask at the 0.2 pb gain level.
                                             (Currently, this option will work only with
                                             gridders that produce .pb (i.e. mosaic and awproject)
                                             or if an externally produced .pb image exists on disk)

                       auto-multithresh : auto-masking by multiple thresholds for deconvolution
                          subparameters : sidelobethreshold, noisethreshold, lownoisethreshold, negativethrehsold,  smoothfactor,
                                          minbeamfrac, cutthreshold, pbmask, growiterations, dogrowprune, minpercentchange, verbose
                          Additional top level parameter relevant to auto-multithresh: fastnoise

                          if pbmask is  0.0, the region outside the specified pb gain level is excluded from
                          image statistics in determination of the threshold.

                      
                       

                       Note: By default the intermediate mask generated by automask at each deconvolution cycle
                             is over-written in the next cycle but one can save them by setting
                             the environment variable, SAVE_ALL_AUTOMASKS=true.
                             (e.g. in the CASA prompt, os.environ['SAVE_ALL_AUTOMASKS']=true )
                             The saved CASA mask image name will be imagename.mask.autothresh#, where
                             # is the iteration cycle number.




mask
---------------------------------------

Mask (a list of image name(s) or region file(s) or region string(s)

    
                       The name of a CASA image or region file or region string that specifies
                       a 1/0 mask to be used for deconvolution. Only locations with value 1 will
                       be considered for the centers of flux components in the minor cycle.
                       If regions specified fall completely outside of the image, tclean will throw an error.

                       Manual mask options/examples :

                       mask='xxx.mask'  : Use this CASA image named xxx.mask and containing
                                                       ones and zeros as the mask. 
                                                       If the mask is only different in spatial coordinates from what is being made 
                                                       it will be resampled to the target coordinate system before being used.
                                                       The mask has to have the same shape in velocity and Stokes planes
                                                       as the output image. Exceptions are single velocity and/or single
                                                       Stokes plane masks. They will be expanded to cover all velocity and/or
                                                       Stokes planes of the output cube.

                                                       [ Note : If an error occurs during image resampling or
                                                                   if the expected mask does not appear, please try
                                                                   using tasks 'imregrid' or 'makemask' to resample
                                                                   the mask image onto a CASA image with the target
                                                                   shape and coordinates and supply it via the 'mask'
                                                                   parameter. ]


                       mask='xxx.crtf' : A text file with region strings and the following on the first line
                                                  ( #CRTFv0 CASA Region Text Format version 0 )
                                                  This is the format of a file created via the viewer's region
                                                  tool when saved in CASA region file format.

                       mask='circle[[40pix,40pix],10pix]'  : A CASA region string.

                       mask=['xxx.mask','xxx.crtf', 'circle[[40pix,40pix],10pix]']  : a list of masks


              


                       Note : Mask images for deconvolution must contain 1 or 0 in each pixel.
                                  Such a mask is different from an internal T/F mask that can be
                                  held within each CASA image. These two types of masks are not
                                  automatically interchangeable, so please use the makemask task
                                  to copy between them if you need to construct a 1/0 based mask
                                  from a T/F one.

                       Note : Work is in progress to generate more flexible masking options and
                                  enable more controls.




pbmask
---------------------------------------

Sub-parameter for usemask='auto-multithresh': primary beam mask

                       Examples : pbmask=0.0 (default, no pb mask)
                                  pbmask=0.2 (construct a mask at the 0.2 pb gain level)




sidelobethreshold
---------------------------------------

Sub-parameter for auto-multithresh:  mask threshold based on sidelobe levels:  sidelobethreshold * max_sidelobe_level * peak residual




noisethreshold
---------------------------------------

Sub-parameter for auto-multithresh:  mask threshold based on the noise level: noisethreshold * rms + location (=median)

              The rms is calculated from MAD with rms = 1.4826*MAD.



lownoisethreshold
---------------------------------------

Sub-parameter for auto-multithresh:  mask threshold to grow previously masked regions via binary dilation:   lownoisethreshold * rms in residual image + location (=median)

              The rms is calculated from MAD with rms = 1.4826*MAD.



negativethreshold
---------------------------------------

Sub-parameter for auto-multithresh: mask threshold  for negative features: -1.0* negativethreshold * rms + location(=median)

              The rms is calculated from MAD with rms = 1.4826*MAD.



smoothfactor
---------------------------------------

Sub-parameter for auto-multithresh:  smoothing factor in a unit of the beam



minbeamfrac
---------------------------------------

Sub-parameter for auto-multithresh:  minimum beam fraction in size to prune masks smaller than mimbeamfrac * beam
                        =0.0 : No pruning



cutthreshold
---------------------------------------

Sub-parameter for auto-multithresh: threshold to cut the smoothed mask to create a final mask: cutthreshold * peak of the smoothed mask



growiterations
---------------------------------------

Sub-parameter for auto-multithresh: Maximum number of iterations to perform using binary dilation for growing the mask



dogrowprune
---------------------------------------

Experimental sub-parameter for auto-multithresh: Do pruning on the grow mask



minpercentchange
---------------------------------------

If the change in the mask size in a particular channel is less than minpercentchange, stop masking that channel in subsequent cycles. This check is only applied when noise based threshold is used and when the previous clean major cycle had a cyclethreshold value equal to the clean threshold. Values equal to -1.0 (or any value less than 0.0) will turn off this check (the default). Automask will still stop masking if the current channel mask is an empty mask and the noise threshold was used to determine the mask.



verbose
---------------------------------------

 If it is set to True, the summary of automasking at the end of each automasking process
                        is printed in the logger.  Following information per channel will be listed in the summary.

                        chan: channel number
                        masking?: F - stop updating automask for the subsequent iteration cycles
                        RMS: robust rms noise
                        peak: peak in residual image
                        thresh_type: type of threshold used (noise or sidelobe)
                        thresh_value: the value of threshold used
                        N_reg: number of the automask regions
                        N_pruned: number of the automask regions removed by pruning
                        N_grow: number of the grow mask regions
                        N_grow_pruned: number of the grow mask regions removed by pruning
                        N_neg_pix: number of pixels for negative mask regions

                        Note that for a large cube, extra logging may slow down the process.



fastnoise
---------------------------------------

 Only relevant when automask (user='multi-autothresh') and/or n-sigma stopping threshold (nsigma 0.0) are/is used. If it is set to True,  a simpler but faster noise calucation is used. 
                        In this case, the threshold values are determined based on classic statistics (using all
                        unmasked pixels for the calculations).
                          
                        If it is set to False,  the new noise calculation
                        method is used based on pre-existing mask.   
 
                        Case 1: no exiting mask
                        Calculate image statistics using Chauvenet algorithm 
                        
                        Case 2: there is an existing mask
                        Calculate image statistics by classical method on the region
                        outside the mask and inside the primary beam mask.

                        In all cases above RMS noise is calculated from MAD. 



restart
---------------------------------------

 Restart using existing images (and start from an existing model image)
                        or automatically increment the image name and make a new image set.

                        True : Re-use existing images. If imagename.model exists the subsequent
                                  run will start from this model (i.e. predicting it using current gridder
                                  settings and starting from the residual image).  Care must be taken
                                  when combining this option with startmodel. Currently, only one or
                                  the other can be used.

                                  startmodel='', imagename.model exists :
                                            - Start from imagename.model
                                  startmodel='xxx', imagename.model does not exist :
                                            - Start from startmodel
                                  startmodel='xxx', imagename.model exists :
                                            - Exit with an error message requesting the user to pick
                                              only one model.  This situation can arise when doing one
                                              run with startmodel='xxx' to produce an output
                                              imagename.model that includes the content of startmodel,
                                              and wanting to restart a second run to continue deconvolution.
                                              Startmodel should be set to '' before continuing.

                                   If any change in the shape or coordinate system of the image is
                                   desired during the restart, please change the image name and
                                   use the startmodel (and mask) parameter(s) so that the old model
                                   (and mask) can be regridded to the new coordinate system before starting.

                         False : A convenience feature to increment imagename with '_1', '_2',
                                    etc as suffixes so that all runs of tclean are fresh starts (without
                                    having to change the imagename parameter or delete images).

                                    This mode will search the current directory for all existing
                                    imagename extensions, pick the maximum, and adds 1.
                                    For imagename='try' it will make try.psf, try_2.psf, try_3.psf, etc.

                                    This also works if you specify a directory name in the path :
                                    imagename='outdir/try'.  If './outdir' does not exist, it will create it.
                                    Then it will search for existing filenames inside that directory.

                                    If outlier fields are specified, the incrementing happens for each
                                    of them (since each has its own 'imagename').  The counters are
                                    synchronized across imagefields, to make it easier to match up sets
                                    of output images.  It adds 1 to the 'max id' from all outlier names
                                    on disk.  So, if you do two runs with only the main field
                                   (imagename='try'), and in the third run you add an outlier with
                                   imagename='outtry', you will get the following image names
                                   for the third run :  'try_3' and 'outtry_3' even though
                                   'outry' and 'outtry_2' have not been used.





savemodel
---------------------------------------

Options to save model visibilities (none, virtual, modelcolumn)

                       Often, model visibilities must be created and saved in the MS
                       to be later used for self-calibration (or to just plot and view them).

                          none : Do not save any model visibilities in the MS. The MS is opened
                                     in readonly mode.

                                     Model visibilities can be predicted in a separate step by
                                     restarting tclean with niter=0,savemodel=virtual or modelcolumn
                                     and not changing any image names so that it finds the .model on
                                     disk (or by changing imagename and setting startmodel to the
                                     original imagename).

                          virtual : In the last major cycle, save the image model and state of the
                                       gridder used during imaging within the SOURCE subtable of the
                                       MS. Images required for de-gridding will also be stored internally.
                                       All future references to model visibilities will activate the
                                       (de)gridder to compute them on-the-fly.  This mode is useful
                                       when the dataset is large enough that an additional model data
                                       column on disk may be too much extra disk I/O, when the
                                       gridder is simple enough that on-the-fly recomputing of the
                                       model visibilities is quicker than disk I/O.
                                       For e.g. that gridder='awproject' does not support virtual model. 

                          modelcolumn : In the last major cycle, save predicted model visibilities
                                      in the MODEL_DATA column of the MS. This mode is useful when
                                      the de-gridding cost to produce the model visibilities is higher
                                      than the I/O required to read the model visibilities from disk.
                                      This mode is currently required for gridder='awproject'.
                                      This mode is also required for the ability to later pull out
                                      model visibilities from the MS into a python array for custom
                                      processing.

                        Note 1 : The imagename.model  image on disk will always be constructed
                                      if the minor cycle runs. This savemodel parameter applies only to
                                      model visibilities created by de-gridding the model image.

                        Note 2 :  It is possible for an MS to have both a virtual model
                                      as well as a model_data column, but under normal operation,
                                      the last used mode will get triggered.  Use the delmod task to
                                      clear out existing models from an MS if confusion arises.
                       Note 3:    when parallel=True, use savemodel='none'; Other options are not yet ready 
                                  for use in parallel. If model visibilities need to be saved (virtual or modelcolumn):
                                  please run tclean in serial mode with niter=0; after the parallel run




calcres
---------------------------------------

Calculate initial residual image

                      This parameter controls what the first major cycle does.

                      calcres=False with niter greater than 0 will assume that
                      a .residual image already exists  and that the minor cycle can
                      begin without recomputing it.

                      calcres=False with niter=0 implies that only the PSF will be made
                      and no data will be gridded.

                      calcres=True requires that calcpsf=True or that the .psf and .sumwt
                      images already exist on disk (for normalization purposes).

                      Usage example : For large runs (or a pipeline scripts) it may be
                                                  useful to first run tclean with niter=0 to create
                                                  an initial .residual to look at and perhaps make
                                                  a custom mask for. Imaging can be resumed
                                                  without recomputing it.




calcpsf
---------------------------------------

Calculate PSF

                        This parameter controls what the first major cycle does.

                        calcpsf=False will assume that a .psf image already exists
                        and that the minor cycle can begin without recomputing it.
      


parallel
---------------------------------------

Run major cycles in parallel (this feature is experimental)

                       Parallel tclean will run only if casa has already been started using mpirun.
                       Please refer to HPC documentation for details on how to start this on your system.

                       Example :  mpirun -n 3 -xterm 0 `which casa`

                       Continuum Imaging :
                          -  Data are partitioned (in time) into NProc pieces
                          -  Gridding/iFT is done separately per partition
                          -  Images (and weights) are gathered and then normalized
                          - One non-parallel minor cycle is run
                          - Model image is scattered to all processes
                          - Major cycle is done in parallel per partition

                      Cube Imaging :
                          - Data and Image coordinates are partitioned (in freq) into NProc pieces
                          - Each partition is processed independently (major and minor cycles)
                          - All processes are synchronized at major cycle boundaries for convergence checks
                          - At the end, cubes from all partitions are concatenated along the spectral axis

                      Note 1 :  Iteration control for cube imaging is independent per partition.
                                    - There is currently no communication between them to synchronize
                                       information such as peak residual and cyclethreshold. Therefore,
                                       different chunks may trigger major cycles at different levels.
                                    - For cube imaging in parallel, there is currently no interactive masking.
                                   (Proper synchronization of iteration control is work in progress.)




