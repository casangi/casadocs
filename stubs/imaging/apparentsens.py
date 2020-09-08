#
# stub function definition file for docstring parsing
#

def apparentsens(vis, field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', imsize=100, cell='"1arcsec"', stokes='I', specmode='mfs', weighting='natural', robust=0.5, npixels=0, uvtaper=['']):
    r"""
Imaging sensitivity estimataion

Parameters
   - vis_ ({string, stringArray}) - Name of input visibility file(s)
   - selectdata_ (bool=True) - Enable data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - field_ ({string, stringArray}='') - field(s) to select
      - spw_ ({string, stringArray}='') - spw(s)/channels to select
      - timerange_ ({string, stringArray}='') - Range of time to select from data
      - uvrange_ ({string, stringArray}='') - Select data within uvrange
      - antenna_ ({string, stringArray}='') - Select data based on antenna/baseline
      - scan_ ({string, stringArray}='') - Scan number range
      - observation_ ({string, int}='') - Observation ID range
      - intent_ ({string, stringArray}='') - Scan Intent(s)

      .. raw:: html

         </details>
   - imsize_ ({int, intArray}=100) - Number of pixels
   - cell_ ({int, double, intArray, doubleArray, string, stringArray}='"1arcsec"') - Cell size
   - stokes_ (string='I') - Stokes Planes to make (I only, for now)
   - specmode_ (string='mfs') - Spectral definition mode (mfs only, for now)
   - weighting_ (string='natural') - Weighting scheme (natural,uniform,briggs)

      .. raw:: html

         <details><summary><i> weighting = natural </i></summary>

      - uvtaper_ (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> weighting = briggs </i></summary>

      - robust_ (double=0.5) - Robustness parameter
      - npixels_ (int=0) - Number of pixels to determine uv-cell size (0 : -/+ 3 pixels)
      - uvtaper_ (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>


Description
   The **apparentsens** task calculates the point source sensitivity
   for the specified selected data, and according to the desired
   imaging geometry and uv grid weighting. The calculation is
   performed solely using the weight information stored in the MS
   WEIGHT column (or WEIGHT_SPECTRUM, if present), and as adjusted by
   the net imaging weighting function (natural, uniform, robust,
   taper, etc.). Therefore, it is assumed that the MS WEIGHTs have
   been properly initialized and calibrated along with the visibility
   data. As long as the WEIGHTs are in the inverse square units of
   the visibilities (i.e., inverse variance weights), the calculation
   should yield a reasonably accurate theoretical imaging sensitivity
   for data at any stage of the calibration (though data at early and
   intermediate stages of calibration may not be sufficiently
   coherent for imaging at high–or even modest–fidelity).

   Two values are returned in a dictionary and reported in the
   logger. First, the apparent sensitivity (in the units implied by
   the WEIGHTs’ units), for the specified imaging geometry and
   weighting scheme (dictionary key: 'effSens'). Second, a unitless
   factor describing the ratio of the apparent sensitivity to that
   obtained with pure ’natural’ weighting (the nominal maximum
   possible sensitivity; dictionary key: 'relToNat'). When ’natural’
   weighting is selected, this ratio factor will be precisely 1.0;
   all other weighting choices will yield an apparent sensitivity
   ratio greater than 1.0. I.e., all non-natural weighting schemes
   are *less* sensitive (higher rms) than natural.

   Currently, **apparentsens** reports only the continuum sensitivity
   for the selected data, and in particular, for the aggregate
   bandwidth indicated by the spectral window selection. The
   calculation further assumes that the visibility samples are each
   entirely independent, i.e., that there are no redundant samples
   such as would occur for overlapping spectral windows. If the
   per-channel visibility weights reflect their own isolated
   sensitivity, the reported *continuum* sensitivity will be
   over-estimated if the data have been smoothed (i.e., Hanning
   smoothed channels individually have sensitivity a factor 8/3 times
   their apparent bandwidth, and this factor is not yet accounted for
   when forming the continuum sensitivity estimate). 

   A future version of **apparentsens** will support reporting a
   sensitivity spectrum for the spectral line case. For now, spectral
   line sensitivity may be reasonably estimated by dividing the
   reported continuum sensitivity by the square root of the
   fractional bandwidth of a single image channel, or by selecting a
   bandwidth matching the width of a single image channel.  In
   either case, sufficient care should be applied with respect to the
   additional per-channel sensitivity introduced by having smoothed
   (e.g., Hanning) the visilbility, as described above.

   

   .. rubric:: Parameter descriptions
      

   The **apparentsens** task use the same data selection as the
   **tclean** task, as well as a subset of the image geometry and
   weighting parameters. All operate in essentially the same way
   (with exceptions noted below), and the **tclean** documentation
   should be consulted for details on how to set them.

   .. rubric:: *specmode*
      

   For now, it is only meaningful to use specmode='mfs'. Use of
   specmode='cube' will be supported in future (and a apparent
   sensitivity spectrum will be returned and reported).

   .. rubric:: *stokes*
      

   Currently, **apparentsens** will report the sensitivity for
   stokes='I' only. Support for polarization-dependent sensitivity
   estimates will be added in future.

   

   .. rubric:: **
      

   .. rubric:: **




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name(s) of input visibility file(s)
   |                default: none;
   |                example: vis='ngc5921.ms'
   |                         vis=['ngc5921a.ms','ngc5921b.ms']; multiple MSes

.. _field:

   .. rubric:: field

   | Select fields to image or mosaic.  Use field id(s) or name(s).
   |                   ['go listobs' to obtain the list id's or names]
   |                default: ''= all fields
   |                  If field string is a non-negative integer, it is assumed to
   |                  be a field index otherwise, it is assumed to be a
   |                  field name
   |                  field='0~2'; field ids 0,1,2
   |                  field='0,4,5~7'; field ids 0,4,5,6,7
   |                  field='3C286,3C295'; field named 3C286 and 3C295
   |                  field = '3,4C*'; field id 3, all names starting with 4C
   |                  For multiple MS input, a list of field strings can be used:
   |                  field = ['0~2','0~4']; field ids 0-2 for the first MS and 0-4
   |                          for the second
   |                  field = '0~2'; field ids 0-2 for all input MSes

.. _spw:

   .. rubric:: spw

   | Select spectral window/channels
   |                NOTE: channels de-selected here will contain all zeros if
   |                          selected by the parameter mode subparameters.
   |                default: ''=all spectral windows and channels
   |                  spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
   |                  spw='0:5~61'; spw 0, channels 5 to 61
   |                  spw='<2';   spectral windows less than 2 (i.e. 0,1)
   |                  spw='0,10,3:3~45'; spw 0,10 all channels, spw 3,
   |                                     channels 3 to 45.
   |                  spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
   |                  For multiple MS input, a list of spw strings can be used:
   |                  spw=['0','0~3']; spw ids 0 for the first MS and 0-3 for the second
   |                  spw='0~3' spw ids 0-3 for all input MS
   |                  spw='3:10~20;50~60' for multiple channel ranges within spw id 3
   |                  spw='3:10~20;50~60,4:0~30' for different channel ranges for spw ids 3 and 4
   |                  spw='0:0~10,1:20~30,2:1;2;3'; spw 0, channels 0-10,
   |                       spw 1, channels 20-30, and spw 2, channels, 1,2 and 3
   |                  spw='1~4;6:15~48' for channels 15 through 48 for spw ids 1,2,3,4 and 6

.. _intent:

   .. rubric:: intent

   | Scan Intent(s)
   | 
   |                    default: '' (all)
   |                    example: intent='TARGET_SOURCE'
   |                    example: intent='TARGET_SOURCE1,TARGET_SOURCE2'
   |                    example: intent='TARGET_POINTING*'

.. _selectdata:

   .. rubric:: selectdata

   | Enable data selection parameters.

.. _timerange:

   .. rubric:: timerange

   | Range of time to select from data
   | 
   |                    default: '' (all); examples,
   |                    timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   |                    Note: if YYYY/MM/DD is missing date defaults to first
   |                          day in data set
   |                    timerange='09:14:0~09:54:0' picks 40 min on first day
   |                    timerange='25:00:00~27:30:00' picks 1 hr to 3 hr
   |                              30min on NEXT day
   |                    timerange='09:44:00' pick data within one integration
   |                              of time
   |                    timerange='> 10:24:00' data after this time
   |                    For multiple MS input, a list of timerange strings can be
   |                    used:
   |                    timerange=['09:14:0~09:54:0','> 10:24:00']
   |                    timerange='09:14:0~09:54:0''; apply the same timerange for
   |                                                  all input MSes

.. _uvrange:

   .. rubric:: uvrange

   | Select data within uvrange (default unit is meters)
   |                    default: '' (all); example:
   |                    uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
   |                    uvrange='> 4klambda';uvranges greater than 4 kilo lambda
   |                    For multiple MS input, a list of uvrange strings can be
   |                    used:
   |                    uvrange=['0~1000klambda','100~1000klamda']
   |                    uvrange='0~1000klambda'; apply 0-1000 kilo-lambda for all
   |                                             input MSes

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline
   | 
   |                    default: '' (all)
   |                    If antenna string is a non-negative integer, it is
   |                    assumed to be an antenna index, otherwise, it is
   |                    considered an antenna name.
   |                    antenna='5\&6'; baseline between antenna index 5 and
   |                                  index 6.
   |                    antenna='VA05\&VA06'; baseline between VLA antenna 5
   |                                        and 6.
   |                    antenna='5\&6;7\&8'; baselines 5-6 and 7-8
   |                    antenna='5'; all baselines with antenna index 5
   |                    antenna='05'; all baselines with antenna number 05
   |                                 (VLA old name)
   |                    antenna='5,6,9'; all baselines with antennas 5,6,9
   |                                    index number
   |                    For multiple MS input, a list of antenna strings can be
   |                    used:
   |                    antenna=['5','5\&6'];
   |                    antenna='5'; antenna index 5 for all input MSes
   |                    antenna='!DV14'; use all antennas except DV14

.. _scan:

   .. rubric:: scan

   | Scan number range
   | 
   |                    default: '' (all)
   |                    example: scan='1~5'
   |                    For multiple MS input, a list of scan strings can be used:
   |                    scan=['0~100','10~200']
   |                    scan='0~100; scan ids 0-100 for all input MSes

.. _observation:

   .. rubric:: observation

   | Observation ID range
   |                    default: '' (all)
   |                    example: observation='1~5'

.. _imsize:

   .. rubric:: imsize

   | Number of pixels
   |          example :  imsize = [350,250]
   |                            imsize = 500 is equivalent to [500,500]
   |          To take proper advantage of internal optimized FFT routines, the
   |          number of pixels must be even and factorizable by 2,3,5,7 only.

.. _cell:

   .. rubric:: cell

   | Cell size
   |                example: cell=['0.5arcsec,'0.5arcsec'] or
   |                cell=['1arcmin', '1arcmin']
   |                cell = '1arcsec' is equivalent to ['1arcsec','1arcsec']

.. _stokes:

   .. rubric:: stokes

   | Stokes Planes to make (I only, for now)
   |                default='I'; example: stokes='IQUV';
   |                  Options: 'I','Q','U','V','IV','QU','IQ','UV','IQUV','RR','LL','XX','YY','RRLL','XXYY','pseudoI'
   | 
   |                              Note : Due to current internal code constraints, if any correlation pair
   |                                         is flagged, by default, no data for that row in the MS will be used.
   |                                         So, in an MS with XX,YY, if only YY is flagged, neither a
   |                                         Stokes I image nor an XX image can be made from those data points.
   |                                         In such a situation, please split out only the unflagged correlation into
   |                                         a separate MS.
   | 
   |                              Note : The 'pseudoI' option is a partial solution, allowing Stokes I imaging
   |                                     when either of the parallel-hand correlations are unflagged.
   | 
   |                              The remaining constraints shall be removed (where logical) in a future release.

.. _specmode:

   .. rubric:: specmode

   | Spectral definition mode (mfs only, for now)
   | 
   |                        mode='mfs' : Continuum imaging with only one output image channel.
   |                                              (mode='cont' can also be used here)
   | 
   |                        mode='cube' : Spectral line imaging with one or more channels
   |                                                Parameters start, width,and nchan define the spectral
   |                                                coordinate system and can be specified either in terms
   |                                                of channel numbers, frequency or velocity in whatever
   |                                                spectral frame is specified in 'outframe'.
   |                                                All internal and output images are made with outframe as the
   |                                                base spectral frame. However imaging code internally uses the fixed
   |                                                spectral frame, LSRK for automatic internal software
   |                                                Doppler tracking so that a spectral line observed over an
   |                                                extended time range will line up appropriately.
   |                                                Therefore the output images have additional spectral frame conversion
   |                                                layer in LSRK on the top the base frame.
   | 
   | 
   |                                                (Note : Even if the input parameters are specified in a frame
   |                                                            other than LSRK, the viewer still displays spectral
   |                                                            axis in LSRK by default because of the conversion frame
   |                                                            layer mentioned above. The viewer can be used to relabel
   |                                                            the spectral axis in any desired frame - via the spectral
   |                                                            reference option under axis label properties in the
   |                                                            data display options window.)
   | 
   | 
   |                                                
   | 
   |                         mode='cubedata' : Spectral line imaging with one or more channels
   |                                                         There is no internal software Doppler tracking so
   |                                                         a spectral line observed over an extended time range
   |                                                         may be smeared out in frequency. There is strictly
   |                                                         no valid spectral frame with which to label the output
   |                                                         images, but they will list the frame defined in the MS.

.. _weighting:

   .. rubric:: weighting

   | Weighting scheme (natural,uniform,briggs,superuniform,radial)
   | 
   |                        During gridding of the dirty or residual image, each visibility value is
   |                        multiplied by a weight before it is accumulated on the uv-grid.
   |                        The PSF's uv-grid is generated by gridding only the weights (weightgrid).
   | 
   |                        weighting='natural' : Gridding weights are identical to the data weights
   |                                                          from the MS. For visibilities with similar data weights,
   |                                                          the weightgrid will follow the sample density
   |                                                          pattern on the uv-plane. This weighting scheme
   |                                                          provides the maximum imaging sensitivity at the
   |                                                          expense of a possibly fat PSF with high sidelobes.
   |                                                          It is most appropriate for detection experiments
   |                                                          where sensitivity is most important.
   | 
   |                        weighting='uniform' : Gridding weights per visibility data point are the
   |                                                           original data weights divided by the total weight of
   |                                                           all data points that map to the same uv grid cell :
   |                                                           ' data_weight / total_wt_per_cell '.
   | 
   |                                                           The weightgrid is as close to flat as possible resulting
   |                                                           in a PSF with a narrow main lobe and suppressed
   |                                                           sidelobes. However, since heavily sampled areas of
   |                                                           the uv-plane get down-weighted, the imaging
   |                                                           sensitivity is not as high as with natural weighting.
   |                                                           It is most appropriate for imaging experiments where
   |                                                           a well behaved PSF can help the reconstruction.
   | 
   |                        weighting='briggs' :  Gridding weights per visibility data point are given by
   |                                                          'data_weight / ( A / total_wt_per_cell + B ) ' where
   |                                                          A and B vary according to the 'robust' parameter.
   | 
   |                                                          robust = -2.0 maps to A=1,B=0 or uniform weighting.
   |                                                          robust = +2.0 maps to natural weighting.
   |                                                          (robust=0.5 is equivalent to robust=0.0 in AIPS IMAGR.)
   | 
   |                                                          Robust/Briggs weighting generates a PSF that can
   |                                                          vary smoothly between 'natural' and 'uniform' and
   |                                                          allow customized trade-offs between PSF shape and
   |                                                          imaging sensitivity.
   | 
   |                        weighting='superuniform' : This is similar to uniform weighting except that
   |                                                                     the total_wt_per_cell is replaced by the
   |                                                                     total_wt_within_NxN_cells around the uv cell of
   |                                                                     interest.  ( N = subparameter 'npixels' )
   | 
   |                                                                    This method tends to give a PSF with inner
   |                                                                    sidelobes that are suppressed as in uniform
   |                                                                    weighting but with far-out sidelobes closer to
   |                                                                    natural weighting. The peak sensitivity is also
   |                                                                    closer to natural weighting.
   | 
   |                        weighting='radial' : Gridding weights are given by ' data_weight * uvdistance '
   | 
   |                                                       This method approximately minimizes rms sidelobes
   |                                                       for an east-west synthesis array.
   | 
   |                For more details on weighting please see Chapter3
   |                of Dan Briggs' thesis (http://www.aoc.nrao.edu/dissertations/dbriggs)

.. _robust:

   .. rubric:: robust

   | Robustness parameter for Briggs weighting.
   | 
   |                             robust = -2.0 maps to uniform weighting.
   |                             robust = +2.0 maps to natural weighting.
   |                             (robust=0.5 is equivalent to robust=0.0 in AIPS IMAGR.)

.. _npixels:

   .. rubric:: npixels

   | Number of pixels to determine uv-cell size for super-uniform weighting
   |                       (0 defaults to -/+ 3 pixels)
   | 
   |                      npixels -- uv-box used for weight calculation
   |                                     a box going from -npixel/2 to +npixel/2 on each side
   |                                    around a point is used to calculate weight density.
   | 
   |                      npixels=2 goes from -1 to +1 and covers 3 pixels on a side.
   | 
   |                      npixels=0 implies a single pixel, which does not make sense for
   |                                      superuniform weighting. Therefore, if npixels=0 it will
   |                                      be forced to 6 (or a box of -3pixels to +3pixels) to cover
   |                                      7 pixels on a side.

.. _uvtaper:

   .. rubric:: uvtaper

   | uv-taper on outer baselines in uv-plane
   | 
   |                    Apply a Gaussian taper in addition to the weighting scheme specified
   |                    via the 'weighting' parameter. Higher spatial frequencies are weighted
   |                    down relative to lower spatial frequencies to suppress artifacts
   |                    arising from poorly sampled areas of the uv-plane. It is equivalent to
   |                    smoothing the PSF obtained by other weighting schemes and can be
   |                    specified either as a Gaussian in uv-space (eg. units of lambda)
   |                    or as a Gaussian in the image domain (eg. angular units like arcsec).
   | 
   |                    uvtaper = [bmaj, bmin, bpa]
   | 
   |                    NOTE: the on-sky FWHM in arcsec is roughly  the uv taper/200 (klambda).
   |                    default: uvtaper=[]; no Gaussian taper applied
   |                    example: uvtaper=['5klambda']  circular taper
   |                                 FWHM=5 kilo-lambda
   |                             uvtaper=['5klambda','3klambda','45.0deg']
   |                             uvtaper=['10arcsec'] on-sky FWHM 10 arcseconds
   |                             uvtaper=['300.0'] default units are lambda
   |                                 in aperture plane


    """
    pass
