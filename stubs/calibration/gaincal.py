#
# stub function definition file for docstring parsing
#

def gaincal(vis, caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='', preavg=-1.0, refant='', refantmode='flex', minblperant=4, minsnr=3.0, solnorm=False, normtype='mean', gaintype='G', smodel=[''], calmode='ap', solmode='', rmsthresh=[''], corrdepflags=False, append=False, splinetime=3600.0, npointaver=3, phasewrap=180.0, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[''], parang=False):
    r"""
Determine temporal gains from calibrator observations

Parameters
   - vis_ (string) - Name of input visibility file
   - caltable_ (string='') - Name of output gain calibration table
   - field_ (string='') - Select field using field id(s) or field name(s)
   - spw_ (string='') - Select spectral window/channels
   - intent_ (string='') - Select observing intent
   - selectdata_ (bool=True) - Other data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - timerange_ (string='') - Select data based on time range
      - uvrange_ (variant='') - Select data by baseline length.
      - antenna_ (string='') - Select data based on antenna/baseline
      - scan_ (string='') - Scan number range
      - observation_ ({string, int}='') - Select by observation ID(s)
      - msselect_ (string='') - Optional complex data selection (ignore for now)

      .. raw:: html

         </details>
   - solint_ (variant='inf') - Solution interval
   - combine_ (string='') - Data axes which to combine for solve (obs, scan, spw, and/or field)
   - preavg_ (double=-1.0) - Pre-averaging interval (sec) (rarely needed)
   - refant_ (string='') - Reference antenna name(s)
   - refantmode_ (string='flex') - Reference antenna mode
   - minblperant_ (int=4) - Minimum baselines _per antenna_ required for solve
   - minsnr_ (double=3.0) - Reject solutions below this SNR
   - solnorm_ (bool=False) - Normalize (squared) solution amplitudes (G, T only)

      .. raw:: html

         <details><summary><i> solnorm = True </i></summary>

      - normtype_ (string='mean') - Solution normalization calculation type: mean or median

      .. raw:: html

         </details>
   - gaintype_ (string='G') - Type of gain solution (G,T,GSPLINE,K,KCROSS)

      .. raw:: html

         <details><summary><i> gaintype = GSPLINE </i></summary>

      - splinetime_ (double=3600.0) - Spline timescale(sec); All spw\'s are first averaged.
      - npointaver_ (int=3) - The phase-unwrapping algorithm
      - phasewrap_ (double=180.0) - Wrap the phase for jumps greater than this value (degrees)

      .. raw:: html

         </details>
   - smodel_ (doubleArray=['']) - Point source Stokes parameters for source model.
   - calmode_ (string='ap') - Type of solution" (\'ap\', \'p\', \'a\')
   - solmode_ (string='') - Robust solving mode: (\'\', \'L1\', \'R\',\'L1R\')
   - rmsthresh_ (doubleArray=['']) - RMS Threshold sequence (for solmode=\'R\' or \'L1R\'; see help)
   - corrdepflags_ (bool=False) - Respect correlation-dependent flags
   - append_ (bool=False) - Append solutions to the (existing) table
   - docallib_ (bool=False) - Use callib or traditional cal apply parameters

      .. raw:: html

         <details><summary><i> docallib = False </i></summary>

      - gaintable_ (stringArray=['']) - Gain calibration table(s) to apply on the fly
      - gainfield_ (stringArray=['']) - Select a subset of calibrators from gaintable(s)
      - interp_ (stringArray=['']) - Interpolation parameters for each gaintable, as a list
      - spwmap_ (intArray=['']) - Spectral window mappings to form for gaintable(s)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> docallib = True </i></summary>

      - callib_ (string='') - Cal Library filename

      .. raw:: html

         </details>
   - parang_ (bool=False) - Apply parallactic angle correction


Description
   .. rubric:: Summary
      

   The complex time-dependent gains for each antenna/spwid are
   determined from the ratio of the data column (raw data), divided
   by the model column, for the specified data selection. The gains
   can be obtained for a specified solution interval for each
   spectral window, or by a spline fit to all spectral windows
   simultaneously. Any specified prior calibrations (e.g., bandpass)
   will be applied on the fly.

   .. rubric:: Introduction
      

   The fundamental calibration to be done on your interferometer data
   is to calibrate the antenna-based gains as a function of time,
   using **gaincal**. Systematic time-dependent complex gain errors
   are almost always the dominant calibration effect, and a solution
   for them is almost always necessary before proceeding with any
   other calibration solve. Traditionally, this calibration type has
   been a catch-all for a variety of similar effects, including: the
   relative amplitude and phase gain for each antenna/polarization,
   phase and amplitude drifts in the electronics of each antenna,
   amplitude response as a function of elevation (gain curve), and
   tropospheric amplitude and phase effects. In CASA, it is possible
   to handle many of these specific effects separately, as available
   information, circumstances, and required accuracy warrant, but if
   accuracy is not paramount it is still possible to solve for the
   net effect using a quick-and-dirty **gaincal**. In fact,
   **gaincal** is often used for an initial exploration of a dataset,
   to find data problems, etc. Also, a provisional gaincal solution
   can be used as prior calibration to optimize bandpass
   calibration. Such gaincal solutions are typically discarded.

   It is best to have determined a (constant or slowly-varying)
   bandpass from the frequency channels by solving for the
   **bandpass**, and to include any other ancillary calibration that
   may be available via **gencal** (e.g., gaincurve, antenna position
   corrections, opacity, etc.).

   .. rubric:: Common calibration solve parameters
      

   See `Solving for
   Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__for
   more information on the task parameters **gaincal** shares with
   all solving tasks, including data selection, general solving
   properties and arranging prior calibration. Also see the
   **rerefant** task documentation for the behavior of reference
   antenna application. Below we describe parameters unique to
   **gaincal**, and those common parameters with unique properties.

   .. rubric:: Gain calibration types: *gaintype*
      

   The *gaintype* parameter selects the type of gain solution to
   compute. For complex gain calibration, the choices are *'T'*,
   *'G'*, and *'GSPLINE'*. The **gaincal** task also supports
   rudimetary delay solutions using *'K'* and *'KCROSS'*.

   .. rubric:: Polarization-dependent sampled gain (*gaintype='G'*)
      

   Generally speaking, *gaintype='G'* can represent any
   multiplicative polarization- and time-dependent complex gain
   effect downstream of the polarizers. (Polarization- and
   time-independent effects upstream of the polarizers may also be
   treated implicitly with G.) Multi-channel data (per spectral
   window) will be averaged in frequency before solving (use
   calibration type B to solve for frequency-dependent effects within
   each spectral window).

   .. rubric:: Polarization-independent sampled gain (*gaintype='T'*)
      

   At high radio frequencies (>10 GHz), it is often the case that the
   most rapid time-dependent gain errors are introduced by the
   troposphere, and are polarization-*independent*. It is therefore
   unnecessary to solve for separate time-dependent solutions for
   both polarizations, as is the case for *gaintype='G'*. Thus
   *gaintype='T'* is available to calibrate such tropospheric
   effects, differing from G only in that a single common solution
   for both polarizations is determined. In cases where only one
   polarization is observed, *gaintype='T'* is adequate to describe
   the time-dependent complex multiplicative gain calibration
   entirely. For the dual-polarization case, it is necessary to
   ensure that the two polarizations are, in fact, coherent by using
   a prior G or (unnormalized) bandpass calibration.

   .. rubric:: Spline gains (*gaintype='GSPLINE'*)
      

   At high radio frequencies, where tropospheric phase fluctuates
   rapidly, it is often the case that there is insufficient
   signal-to-noise to obtain robust G or T solutions on timescales
   short enough to track the variation. In this case it is desirable
   to solve for a best-fit functional form for each antenna using the
   GSPLINE solver. This fits a time-series of cubic B-splines to the
   phase and/or amplitude of the calibrator visibilities.

   The *combine* parameter can be used to combine data across
   spectral windows, scans, and fields. Note that if you want to use
   *combine='field'*, then all fields used to obtain a GSPLINE
   amplitude solution must have models with accurate relative flux
   densities. Use of incorrect relative flux densities will introduce
   spurious variations in the GSPLINE amplitude solution.

   The GSPLINE solver requires a number of unique additional
   parameters, compared to ordinary G and T solving. The
   sub-parameters are:

   ::

      | gaintype = 'GSPLINE' # Type of solution (G, T,
        or GSPLINE)
      |  splinetime = 3600.0 # Spline (smooth) timescale
        (sec), default=1 hours
      |  npointaver = 3 # Points to average for
        phase wrap
      |  phasewrap = 180 # Wrap phase when greater
        than this

   The duration of each spline segment is controlled by *splinetime*.
   The *splinetime* will be adjusted automatically such that an
   integral number of equal-length spline segments will fit within
   the overall range of data.

   Phase splines require that cycle ambiguities be resolved prior to
   the fit; this operation is controlled by *npointaver* and
   *phasewrap*. The *npointaver* parameter controls how many
   contiguous points in the time-series are used to predict the cycle
   ambiguity of the next point in the time-series, and *phasewrap*
   sets the threshold phase jump (in degrees) that would indicate a
   cycle slip. Large values of *npointaver* improve the SNR of the
   cycle estimate, but tend to frustrate ambiguity detection if the
   phase rates are large. The *phasewrap* parameter may be adjusted
   to influence when cycles are detected. Generally speaking, large
   values (>180 degrees) are useful when SNR is high and phase rates
   are low. Smaller values for *phasewrap* can force cycle slip
   detection when low SNR conspires to obscure the jump, but the
   algorithm becomes significantly less robust. More robust
   algorithms for phase-tracking are under development (including
   traditional fringe-fitting).

   .. warning:: GSPLINE solutions cannot be used in fluxscale. You should do at
      least some long-timescale G amplitude solutions to establish
      the flux scale, then do GSPLINE in phase before or after to fix
      up the short timescale variations. Note also that the phase
      tracking algorithm in GSPLINE needs some improvement.

   .. rubric:: Single- and multi-band delay (*gaintype='K'*)
      

   With *gaintype='K'* **gaincal** solves for simple antenna-based
   delays via Fourier transforms of the spectra on baselines to
   (only) the reference antenna. This is not a global fringe fit but
   will be useful for deriving delays from data of reasonable SNR. If
   *combine* includes *'spw'*, multi-band delays solved jointly from
   all selected spectral windows will be determined, and will be
   identified with the first spectral window id in the output
   *caltable*. When applying a multi-band delay table, a non-trivial
   *spwmap* is required to distribute the solutions to all spectral
   windows (fan-out is not automatic). As of CASA 5.6, multi-band
   delays can be solved using heterogeneous spws (e.g., with
   differing bandwidths, channelizations, etc.).

   After solving for delays, a subsequent **bandpass** is recommended
   to describe higher-order channel-dependent variation in the phase
   and amplitude.

   .. rubric:: Cross-hand delays (*gaintype='KCROSS'*)
      

   With *gaintype='KCROSS',* **gaincal** solves for a global
   cross-hand delay. This is used only when doing polarimetry. Use
   *parang=T* to apply prior gain and bandpass solutions. This mode
   assumes that all cross-hand data (per spw) share the same
   cross-hand delay residual, which should be the case for a proper
   gain/bandpass calibration. See sections on polarimetry for more
   information on use of this mode. Multi-band cross-hand delays are
   only supported for homogeneous spws (same bandwidths,
   channelizations, etc.).

   

   .. rubric:: Solution normalization: *solnorm, normtype*
      

   Nominally, gain solution amplitudes are implicitly scaled in
   amplitude to satisfy the the effective amplitude ratio between the
   visiibility data and model (as pre-corrected or pre-corrupted,
   respectively, by specified prior calibrations). If *solnorm=True*,
   the solution amplitudes will be normalized so as to achieve an
   effective time- and antenna-relative gain calibration that will
   minimally adjust the global amplitude scale of the visibility
   amplitudes when applied. This is desirable when the model against
   which the calibration is solved is in some way incomplete w.r.t.
   the net amplitude scale, but a antenna- and time-relative
   calibration is desired, e.g., amplitude-sensitive self-calibration
   when not all of the total flux density has been recovered in the
   visibility model. The normalization factor is calculated from the
   power gains (squared solution amplitudes) for all antennas and
   times (per spw) according to the the setting of *normtype*. If
   *normtype='mean'*, (the default), the square root of the mean
   power gain is used to normalize the amplitude gains. If
   *normtype='median'*, the median is used instead, which can be
   useful to avoid biasing of the normalization by outlier
   amplitudes. The default for *solnorm* is *solnorm=False*, which
   means no normalization.

   

   .. rubric:: Robust solving: *solmode, rmsthresh*
      

   .. warning:: Robust solving modes in gaincal are considered experimental in
      CASA 5.5. With more experience and testing in the coming
      development cycles, we will provide more refined advice for use
      of these options.

   | Nominally (*solmode=''*), gaincal performs an iterative,
     steepest-descent chi-squared minimization for its antenna-based
     gain solution, i.e., minimizaiton of the L2 norm. Visibility
     outliers (i.e., data not strictly consistent with the assumption
     of antenna-based gains and the supplied visibility model within
     the available SNR) can significantly distort the chi-squared
     gradient calculation, and thereby bias the resulting solution.
     For an outlier on a single baseline, the solutions for the
     antennas in that baseline will tend to be biased in the
     direction of the outlier, and all other antenna solutions in the
     other direction (by a lesser amount consistent with the fraction
     of normal, non-outlying baselines to them). It is thus
     desirable to dampen the influence of such outliers, and
     solmode/rmshresh provide a mechanism for achieving this. These
     options apply only to *gaintype='G'* and *'T'*, and will be
     ignored for other options.
   | Use of *solmode='L1'* invokes an approximate form of
     minimization of the aggregate absolute deviation of visibilities
     with respect to the model, i.e., the L1 norm. This is achieved
     by accumulating the nominal chi-squared and its gradient using
     weights divided by (at each iteration of the steepest descent
     process) the current per-baseline absolute residual (i.e., the
     square-root of each baseline's chi-square contribution). (NB:
     It is not possible to analytically accumulate the gradient of L1
     since the absolute value is not differentiable.) To avoid an
     over-reliance on baselines with atypically small residuals at
     each interation, the weight adjustments are clamped to a minimum
     (divided) value, and the steepest descent convergence is
     repeated three times with increasingly modest clamping. The net
     effect is to gently but effectively render the weight of
     relative outliers to appropriately damped influence in the
     solution.
   | Using *solmode='R'* invokes the normal L2 solution, but attempts
     to identify outliers (relative to apparent aggregate rms) upon
     steepest descent convergence, flag them, and repeat the steepest
     descent. Since outliers will tend to bias the rms calculation
     initially (and thus possibly render spuriously large rms
     residuals for otherwise good data), outlier detection and
     re-covergence is repeated with increasingly aggressive rms
     thresholds, a sequence specifiable in *rmsthresh*. By default
     *(rmsthresh=[])* invokes a sequence of 10 thresholds borrowed
     from a traditional implementation found in AIPS:
     [7.0,5.0,4.0,3.5,3.0,2.8,2.6,2.4,2.2,2.5]. Note that the lower
     threshold values are likely to cull visibilites not formally
     outliers, but merely with modestly large residuals still
     consistent with gaussian statistitics, and thereby unnecessarily
     decrease net effective sensitivity in the gain solution (cf
     normal L2), especially for larger arrays where the number of
     baselines likely implies a larger number of visibility residuals
     falling in the modest wings of the distribution. Thus, it may
     be desirable to set *rmsthresh* manually to a more modest
     sequence of thresholds. Optimization of *rmsthresh* for modern
     arrays and conditions is an area of ongoing study.
   | Use of *solmode='L1R'* combines both the L1 and R modes
     described above, with the iterative clamped L1 loop occuring
     inside the R outliner excision threshold sequence loop.

   | 
   |




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _caltable:

   .. rubric:: caltable

   | Name of output gain calibration table
   |                      Default: none
   | 
   |                         Example: caltable='ngc5921.gcal'

.. _field:

   .. rubric:: field

   | Select field using field id(s) or field name(s)
   |                      Default: '' (all fields)
   |                      
   |                      Use 'go listobs' to obtain the list id's or
   |                      names. If field string is a non-negative integer,
   |                      it is assumed a field index,  otherwise, it is
   |                      assumed a field name.
   | 
   |                         Examples:
   |                         field='0~2'; field ids 0,1,2
   |                         field='0,4,5~7'; field ids 0,4,5,6,7
   |                         field='3C286,3C295'; field named 3C286 and
   |                         3C295
   |                         field = '3,4C*'; field id 3, all names
   |                         starting with 4C

.. _spw:

   .. rubric:: spw

   | Select spectral window/channels
   |                      Default: '' (all spectral windows and channels)
   | 
   |                         Examples:
   |                         spw='0~2,4'; spectral windows 0,1,2,4 (all
   |                         channels)
   |                         spw='<2';  spectral windows less than 2
   |                         (i.e. 0,1)
   |                         spw='0:5~61'; spw 0, channels 5 to 61,
   |                         INCLUSIVE
   |                         spw='*:5~61'; all spw with channels 5 to 61
   |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
   |                         3, channels 3 to 45.
   |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
   |                         through 6 in each.
   |                         spw='0:0~10;15~60'; spectral window 0 with
   |                         channels 0-10,15-60. (NOTE ';' to separate
   |                         channel selections)
   |                         spw='0:0~10^2,1:20~30^5'; spw 0, channels
   |                         0,2,4,6,8,10, spw 1, channels 20,25,30

.. _intent:

   .. rubric:: intent

   | Select observing intent
   |                      Default: '' (no selection by intent)
   | 
   |                         Example: intent='*BANDPASS*'  (selects data
   |                         labelled with BANDPASS intent)

.. _selectdata:

   .. rubric:: selectdata

   | Other data selection parameters
   |                      Default: True
   |                      Options: True|False

.. _timerange:

   .. rubric:: timerange

   | Select data based on time range
   |                      Subparameter of selectdata=True
   |                      Default = '' (all)
   | 
   |                         Examples:
   |                         timerange =
   |                         'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   |                         (Note: if YYYY/MM/DD is missing date defaults
   |                         to first day in data set.)
   |                         timerange='09:14:0~09:54:0' picks 40 min on
   |                         first day 
   |                         timerange= '25:00:00~27:30:00' picks 1 hr to 3
   |                         hr 30min on NEXT day
   |                         timerange='09:44:00' pick data within one
   |                         integration of time
   |                         timerange='>10:24:00' data after this time

.. _uvrange:

   .. rubric:: uvrange

   | Select data by baseline length.
   |                      Default = '' (all)
   | 
   |                         Examples:
   |                         uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
   |                         uvrange='>4klambda';uvranges greater than 4 kilo-lambda
   |                         uvrange='0~1000km'; uvrange in kilometers

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline
   |                      Subparameter of selectdata=True
   |                      Default: '' (all)
   | 
   |                      If antenna string is a non-negative integer, it
   |                      is assumed an antenna index, otherwise, it is
   |                      assumed as an antenna name
   |   
   |                          Examples: 
   |                          antenna='5&6'; baseline between antenna
   |                          index 5 and index 6.
   |                          antenna='VA05&VA06'; baseline between VLA
   |                          antenna 5 and 6.
   |                          antenna='5&6;7&8'; baselines with
   |                          indices 5-6 and 7-8
   |                          antenna='5'; all baselines with antenna index
   |                          5
   |                          antenna='05'; all baselines with antenna
   |                          number 05 (VLA old name)
   |                          antenna='5,6,10'; all baselines with antennas
   |                          5,6,10 index numbers

.. _scan:

   .. rubric:: scan

   | Scan number range
   |                      Subparameter of selectdata=True
   |                      Default: '' = all
   | 
   |                      Check 'go listobs' to insure the scan numbers are
   |                      in order.

.. _observation:

   .. rubric:: observation

   | Select by observation ID(s)
   |                      Subparameter of selectdata=True
   |                      Default: '' = all
   | 
   |                          Example: observation='0~2,4'

.. _msselect:

   .. rubric:: msselect

   | Optional complex data selection (ignore for now)

.. _solint:

   .. rubric:: solint

   | Solution interval
   |                      Default: 'inf' (infinite, up to boundaries
   |                      controlled by combine); 
   |                      Options: 'inf' (~infinite), 'int' (per
   |                      integration), any float or integer value with or
   |                      without units
   | 
   |                         Examples: 
   |                         solint='1min'; solint='60s', solint=60 (i.e.,
   |                         1 minute); solint='0s'; solint=0; solint='int'
   |                         (i.e., per integration); solint-'-1s';
   |                         solint='inf' (i.e., ~infinite, up to
   |                         boundaries enforced by combine)

.. _combine:

   .. rubric:: combine

   | Data axes which to combine for solve
   |                      Default: 'scan' (solutions will break at obs,
   |                      field, and spw boundaries)
   |                      Options: '','obs','scan','spw',field', or any
   |                      comma-separated combination in a single string
   | 
   |                         Example: combine='scan,spw' - Extend solutions
   |                         over scan boundaries (up to the solint), and
   |                         combine spws for solving

.. _preavg:

   .. rubric:: preavg

   | Pre-averaging interval (sec)
   |                      Default: -1.0 (none)
   | 
   |                      Rarely needed.  Will average data over periods
   |                      shorter than the solution interval first.

.. _refant:

   .. rubric:: refant

   | Reference antenna name(s); a prioritized list may be
   | specified
   |                      Default: '' (No refant applied)
   | 
   |                         Examples: 
   |                         refant='4' (antenna with index 4)
   |                         refant='VA04' (VLA antenna #4)
   |                         refant='EA02,EA23,EA13' (EVLA antenna EA02,
   |                         use EA23 and EA13 as alternates if/when EA02
   |                         drops out)
   | 
   |                      Use taskname=listobs for antenna listing

.. _refantmode:

   .. rubric:: refantmode

   | Reference antenna mode

.. _minblperant:

   .. rubric:: minblperant

   | Minimum number of baselines required per antenna for each
   | solve
   |                      Default: 4
   | 
   |                      Antennas with fewer baselines are excluded from
   |                      solutions.
   | 
   |                         Example: minblperant=10 --> Antennas
   |                         participating on 10 or more baselines are
   |                         included in the solve
   | 
   |                      minblperant = 1 will solve for all baseline
   |                      pairs, even if only one is present in the data
   |                      set.  Unless closure errors are expected, use
   |                      taskname=gaincal rather than taskname=blcal to
   |                      obtain more options in data analysis.

.. _minsnr:

   .. rubric:: minsnr

   | Reject solutions below this SNR
   |                      Default: 3.0

.. _solnorm:

   .. rubric:: solnorm

   | Normalize (squared) solution amplitudes (G, T only)
   |                      Default: False (no normalization)

.. _normtype:

   .. rubric:: normtype

   | Solution normalization calculation type: mean or median
   |                      Default: 'mean'

.. _gaintype:

   .. rubric:: gaintype

   | Type of gain solution (G,T,GSPLINE,K,KCROSS)
   |                      Default: 'G'
   | 
   |                         Example: gaintype='GSPLINE'
   | 
   |                    * 'G' means determine gains for each polarization and sp_wid
   |                    * 'T' obtains one solution for both polarizations;
   |                      Hence. their phase offset must be first removed
   |                      using a prior G.
   |                    * 'GSPLINE' makes a spline fit to the calibrator
   |                      data. It is useful for noisy data and fits a
   |                      smooth curve through the calibrated amplitude and
   |                      phase. However, at present GSPLINE is somewhat
   |                      experimental. Use with caution and check
   |                      solutions.
   |                    * 'K' solves for simple antenna-based delays via
   |                      FFTs of the spectra on baselines to the reference
   |                      antenna.  (This is not global fringe-fitting.)
   |                      If combine includes 'spw', multi-band delays are
   |                      determined; otherwise, per-spw single-band delays
   |                      will be determined.
   |                    * 'KCROSS' solves for a global cross-hand delay.
   |                      Use parang=T and apply prior gain and bandpass
   |                      solutions.  Multi-band delay solves
   |                      (combine='spw') not yet supported for KCROSS.

.. _smodel:

   .. rubric:: smodel

   | Point source Stokes parameters for source model
   | (experimental).
   |                      Default: [] (use MODEL_DATA column)
   | 
   |                         Example: [1,0,0,0] (I=1, unpolarized)

.. _calmode:

   .. rubric:: calmode

   | Type of solution" ('ap', 'p', 'a')
   |                      Default: 'ap' (amp and phase)
   |                      Options: 'p' (phase) ,'a' (amplitude), 'ap'
   |                      (amplitude and phase)
   | 
   |                         Example: calmode='p'

.. _solmode:

   .. rubric:: solmode

   | Robust solving mode: 
   |                      Options: '', 'L1', 'R', 'L1R'

.. _rmsthresh:

   .. rubric:: rmsthresh

   | RMS Threshold sequence
   |                      Subparameter of solmode='R' or 'L1R'
   | 
   |                      See CASA Docs for more information
   |                      (https://casa.nrao.edu/casadocs/)

.. _corrdepflags:

   .. rubric:: corrdepflags

   | If False (default), if any correlation is flagged, treat all correlations in
   |               the visibility vector as flagged when solving (per channel, per baseline).
   |               If True, use unflagged correlations in a visibility vector, even if one or more
   |               other correlations are flagged.
   |               
   |                      Default: False (treat correlation vectors with one or more correlations flagged as entirely flagged)
   |   
   |                      Traditionally, CASA has observed a strict interpretation of 
   |                      correlation-dependent flags: if one or more correlations 
   |                      (for any baseline and channel) is flagged, then all available 
   |                      correlations for the same baseline and channel are 
   |                      treated as flagged.  However, it is desirable in some 
   |                      circumstances to relax this stricture, e.g., to preserve use
   |                      of data from antennas with only one good polarization (e.g., one polarization
   |                      is bad or entirely absent).  Solutions for the bad or missing polarization 
   |                      will be rendered as flagged.

.. _append:

   .. rubric:: append

   | Append solutions to the (existing) table
   |                      Default: False (overwrite existing table or make
   |                      new table)
   | 
   |                      Appended solutions must be derived from the same
   |                      MS as the existing caltable, and solution spws
   |                      must have the same meta-info (according to spw
   |                      selection and solint) or be non-overlapping.

.. _splinetime:

   .. rubric:: splinetime

   | Spline timescale(sec); All spw\'s are first averaged.
   |                      Subparameter of gaintype='GSPLINE'
   |                      Default: 3600 (1 hour)
   | 
   |                         Example: splinetime=1000
   | 
   |                      Typical splinetime should cover about 3 to 5
   |                      calibrator scans.

.. _npointaver:

   .. rubric:: npointaver

   | Tune phase-unwrapping algorithm
   |                      Subparameter of gaintype='GSPLINE'
   |                      Default: 3; Keep at this value

.. _phasewrap:

   .. rubric:: phasewrap

   | Wrap the phase for jumps greater than this value
   | (degrees)
   |                      Subparameter of gaintype='GSPLINE'
   |                      Default: 180; Keep at this value

.. _docallib:

   .. rubric:: docallib

   | Control means of specifying the caltables
   |                      Default: False (Use gaintable, gainfield, interp,
   |                      spwmap, calwt)
   |                      Options: False|True
   | 
   |                      If True, specify a file containing cal library in
   |                      callib

.. _callib:

   .. rubric:: callib

   | Specify a file containing cal library directives
   |                      Subparameter of docallib=True

.. _gaintable:

   .. rubric:: gaintable

   | Gain calibration table(s) to apply on the fly
   |                      Default: '' (none)
   |                      Subparameter of docallib=False
   |                         Examples: 
   |                         gaintable='ngc5921.gcal'
   |                         gaintable=['ngc5921.ampcal','ngc5921.phcal']

.. _gainfield:

   .. rubric:: gainfield

   | Select a subset of calibrators from gaintable(s)
   |                      Default: '' (all sources on the sky)
   | 
   |                      'nearest' ==> nearest (on sky) available field in
   |                      table otherwise, same syntax as field
   | 
   |                         Examples: 
   |                         gainfield='0~2,5' means use fields 0,1,2,5
   |                         from gaintable
   |                         gainfield=['0~3','4~6'] means use field 0
   |                         through 3

.. _interp:

   .. rubric:: interp

   | Interpolation parmameters (in time[,freq]) for each gaintable, as a list of strings.
   |                      Default: '' --> 'linear,linear' for all gaintable(s)
   |                      Options: Time: 'nearest', 'linear'
   |                               Freq: 'nearest', 'linear', 'cubic',
   |                               'spline'
   |                    Specify a list of strings, aligned with the list of caltable specified
   |                    in gaintable, that contain the required interpolation parameters
   |                    for each caltable.
   |                    * When frequency interpolation is relevant (B, Df,
   |                      Xf), separate time-dependent and freq-dependent
   |                      interp types with a comma (freq_after_ the
   |                      comma). 
   |                    * Specifications for frequency are ignored when the
   |                      calibration table has no channel-dependence. 
   |                    * Time-dependent interp options ending in 'PD'
   |                      enable a "phase delay" correction per spw for
   |                      non-channel-dependent calibration types.
   |                    * For multi-obsId datasets, 'perobs' can be
   |                      appended to the time-dependent interpolation
   |                      specification to enforce obsId boundaries when
   |                      interpolating in time. 
   |                    * Freq-dependent interp options can have 'flag' appended
   |                      to enforce channel-dependent flagging, and/or 'rel' 
   |                      appended to invoke relative frequency interpolation
   | 
   |                         Examples: 
   |                         interp='nearest' (in time, freq-dep will be
   |                         linear, if relevant)
   |                         interp='linear,cubic'  (linear in time, cubic
   |                         in freq)
   |                         interp='linearperobs,splineflag' (linear in
   |                         time per obsId, spline in freq with
   |                         channelized flagging)
   |                         interp='nearest,linearflagrel' (nearest in
   |                         time, linear in freq with with channelized 
   |                         flagging and relative-frequency interpolation)
   |                         interp=',spline'  (spline in freq; linear in
   |                         time by default)
   |                         interp=['nearest,spline','linear']  (for
   |                         multiple gaintables)

.. _spwmap:

   .. rubric:: spwmap

   | Spectral window mappings to form for gaintable(s)
   |                      Only used if callib=False
   |                      default: [] (apply solutions from each calibration spw to
   |                       the same MS spw only)
   |                      Any available calibration spw can be mechanically mapped to any 
   |                       MS spw. 
   |                      Examples:
   |                         spwmap=[0,0,1,1] means apply calibration 
   |                           from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
   |                         spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
   |                           gaintables)

.. _parang:

   .. rubric:: parang

   | Apply parallactic angle correction
   |                      Default: False
   | 
   |                      If True, apply the parallactic angle correction
   |                      (required for polarization calibration)


    """
    pass
