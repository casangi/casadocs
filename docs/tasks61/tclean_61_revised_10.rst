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
     - First channel (e.g. start=3,start='1.1GHz',start='15343km/s')
   * - width
     - :code:`''`
     - Channel width (e.g. width=2,width='0.1MHz',width='10km/s')
   * - outframe
     - :code:`'LSRK'`
     - Spectral reference frame in which to interpret 'start' and 'width'
   * - veltype
     - :code:`'radio'`
     - Velocity type (radio, z, ratio, beta, gamma, optical)
   * - restfreq
     - :code:`numpy.array( [  ] )`
     - List of rest frequencies
   * - interpolation
     - :code:`'linear'`
     - Spectral interpolation (nearest,linear,cubic)

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




start
---------------------------------------

First channel (e.g. start=3,start='1.1GHz',start='15343km/s')
                       of output cube images specified by data channel number (integer),
                       velocity (string with a unit),  or frequency (string with a unit).
                       Default:''; The first channel is automatically determined based on
                       the 'spw' channel selection and 'width'.
                       When the channel number is used along with the channel selection
                        in 'spw' (e.g. spw='0:6~100'),
                       'start' channel number is RELATIVE (zero-based) to the selected
                       channels in 'spw'. So for the above example,
                       start=1 means that the first image channel is the second selected
                       data channel, which is channel 7.
                       For specmode='cube', when velocity or frequency is used it is
                       interpreted with the frame defined in outframe. [The parameters of
                       the desired output cube can be estimated by using the 'transform'
                       functionality of 'plotms']
                       examples: start='5.0km/s'; 1st channel, 5.0km/s in outframe
                                 start='22.3GHz'; 1st channel, 22.3GHz in outframe



width
---------------------------------------

Channel width (e.g. width=2,width='0.1MHz',width='10km/s') of output cube images
                      specified by data channel number (integer), velocity (string with a unit), or
                      or frequency (string with a unit).
                      Default:''; data channel width
                      The sign of width defines the direction of the channels to be incremented.
                      For width specified in velocity or frequency with '-' in front  gives image channels in
                      decreasing velocity or frequency, respectively.
                      For specmode='cube', when velocity or frequency is used it is interpreted with
                      the reference frame defined in outframe.
                      examples: width='2.0km/s'; results in channels with increasing velocity
                                width='-2.0km/s';  results in channels with decreasing velocity
                                width='40kHz'; results in channels with increasing frequency
                                width=-2; results in channels averaged of 2 data channels incremented from
                                          high to low channel numbers




outframe
---------------------------------------

Spectral reference frame in which to interpret 'start' and 'width'
                      Options: '','LSRK','LSRD','BARY','GEO','TOPO','GALACTO','LGROUP','CMB'
                      example: outframe='bary' for Barycentric frame

                      REST -- Rest frequency
                      LSRD -- Local Standard of Rest (J2000)
                               -- as the dynamical definition (IAU, [9,12,7] km/s in galactic coordinates)
                      LSRK -- LSR as a kinematical (radio) definition
                               -- 20.0 km/s in direction ra,dec = [270,+30] deg (B1900.0)
                      BARY -- Barycentric (J2000)
                      GEO --- Geocentric
                      TOPO -- Topocentric
                      GALACTO -- Galacto centric (with rotation of 220 km/s in direction l,b = [90,0] deg.
                      LGROUP -- Local group velocity -- 308km/s towards l,b = [105,-7] deg (F. Ghigo)
                     CMB -- CMB velocity -- 369.5km/s towards l,b = [264.4, 48.4] deg (F. Ghigo)
                     DEFAULT = LSRK




veltype
---------------------------------------

Velocity type (radio, z, ratio, beta, gamma, optical)
                      For start and/or width specified in velocity, specifies the velocity definition
                      Options: 'radio','optical','z','beta','gamma','optical'
                      NOTE: the viewer always defaults to displaying the 'radio' frame,
                        but that can be changed in the position tracking pull down.

                       The different types (with F = f/f0, the frequency ratio), are:

                       Z = (-1 + 1/F)
                      RATIO = (F) *
                      RADIO = (1 - F)
                      OPTICAL == Z
                      BETA = ((1 - F2)/(1 + F2))
                      GAMMA = ((1 + F2)/2F) *
                      RELATIVISTIC == BETA (== v/c)
                      DEFAULT == RADIO
                      Note that the ones with an '*' have no real interpretation
                      (although the calculation will proceed) if given as a velocity.




restfreq
---------------------------------------

List of rest frequencies or a rest frequency in a string.
                      Specify rest frequency to use for output image.
                      *Currently it uses the first rest frequency in the list for translation of
                      velocities. The list will be stored in the output images.
                      Default: []; look for the rest frequency stored in the MS, if not available,
                      use center frequency of the selected channels
                      examples: restfreq=['1.42GHz']
                                restfreq='1.42GHz'




interpolation
---------------------------------------

Spectral interpolation (nearest,linear,cubic)

                       Interpolation rules to use when binning data channels onto image channels
                       and evaluating visibility values at the centers of image channels.

                      Note : 'linear' and 'cubic' interpolation requires data points on both sides of
                        each image frequency. Errors  are therefore possible at edge  channels, or near
                        flagged data channels. When image channel width is much larger than the data
                        channel width there is nothing much to be gained using linear or cubic thus
                        not worth the extra computation involved.





