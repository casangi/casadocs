

.. _Description:

Description
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
   calibration.  Such gaincal solutions are typically discarded.
   
   It is best to have determined a (constant or slowly-varying)
   bandpass from the frequency channels by solving for the
   **bandpass**, and to include any other ancillary calibration that
   may be available via **gencal** (e.g., gaincurve, antenna position
   corrections, opacity, etc.).
   
   .. rubric:: Common calibration solve parameters
   
   See `Solving for
   Calibration <../../notebooks/synthesis_calibration.ipynb#Solve-for-Calibration>`__ for
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
   
      gaintype         =  'GSPLINE'   #   Type of solution (G, T, or GSPLINE)
           splinetime  =     3600.0   #   Spline (smooth) timescale (sec), default=1 hours
           npointaver  =          3   #   Points to average for phase wrap
           phasewrap   =        180   #   Wrap phase when greater than this
   
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
   windows (fan-out is not automatic).  As of CASA 5.6, multi-band
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
   information on use of this mode.  Multi-band cross-hand delays are
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
   amplitudes when applied.  This is desirable when the model against
   which the calibration is solved is in some way incomplete w.r.t.
   the net amplitude scale, but a antenna- and time-relative
   calibration is desired, e.g., amplitude-sensitive self-calibration
   when not all of the total flux density has been recovered in the
   visibility model.  The normalization factor is calculated from the
   power gains (squared solution amplitudes) for all antennas and
   times (per spw) according to the the setting of *normtype*.  If
   *normtype='mean'*, (the default), the square root of the mean
   power gain is used to normalize the amplitude gains.  If
   *normtype='median'*, the median is used instead, which can be
   useful to avoid biasing of the normalization by outlier
   amplitudes.  The default for *solnorm* is *solnorm=False*, which
   means no normalization.

   
   .. rubric:: Robust solving:  *solmode, rmsthresh*
   
   .. warning:: Robust solving modes in gaincal are considered experimental in
      CASA 5.5.  With more experience and testing in the coming
      development cycles, we will provide more refined advice for use
      of these options.
   
   Nominally (*solmode=''*), gaincal performs an iterative,
   steepest-descent chi-squared minimization for its antenna-based
   gain solution, i.e., minimizaiton of the L2 norm.  Visibility
   outliers (i.e., data not strictly consistent with the assumption
   of antenna-based gains and the supplied visibility model within
   the available SNR) can significantly distort the chi-squared
   gradient calculation, and thereby bias the resulting solution.
   For an outlier on a single baseline, the solutions for the
   antennas in that baseline will tend to be biased in the
   direction of the outlier, and all other antenna solutions in the
   other direction (by a lesser amount consistent with the fraction
   of normal, non-outlying baselines to them).  It is thus
   desirable to dampen the influence of such outliers, and
   solmode/rmshresh provide a mechanism for achieving this.  These
   options apply only to *gaintype='G'* and *'T'*, and will be
   ignored for other options.

   Use of *solmode='L1'* invokes an approximate form of
   minimization of the aggregate absolute deviation of visibilities
   with respect to the model, i.e., the L1 norm.  This is achieved
   by accumulating the nominal chi-squared and its gradient using
   weights divided by (at each iteration of the steepest descent
   process) the current per-baseline absolute residual (i.e., the
   square-root of each baseline's chi-square contribution).  (NB:
   It is not possible to analytically accumulate the gradient of L1
   since the absolute value is not differentiable.)   To avoid an
   over-reliance on baselines with atypically small residuals at
   each interation, the weight adjustments are clamped to a minimum
   (divided) value, and the steepest descent convergence is
   repeated three times with increasingly modest clamping. The net
   effect is to gently but effectively render the weight of
   relative outliers to appropriately damped influence in the
   solution.

   Using *solmode='R'* invokes the normal L2 solution, but attempts
   to identify outliers (relative to apparent aggregate rms) upon
   steepest descent convergence, flag them, and repeat the steepest
   descent.  Since outliers will tend to bias the rms calculation
   initially (and thus possibly render spuriously large rms
   residuals for otherwise good data), outlier detection and
   re-covergence is repeated with increasingly aggressive rms
   thresholds, a sequence specifiable in *rmsthresh*.  By default
   *(rmsthresh=[])* invokes a sequence of 10 thresholds borrowed
   from a traditional implementation found in AIPS:
   [7.0,5.0,4.0,3.5,3.0,2.8,2.6,2.4,2.2,2.5].  Note that the lower
   threshold values are likely to cull visibilites not formally
   outliers, but merely with modestly large residuals still
   consistent with gaussian statistitics, and thereby unnecessarily
   decrease net effective sensitivity in the gain solution (cf
   normal L2), especially for larger arrays where the number of
   baselines likely implies a larger number of visibility residuals
   falling in the modest wings of the distribution.  Thus, it may
   be desirable to set *rmsthresh* manually to a more modest
   sequence of thresholds.  Optimization of *rmsthresh* for modern
   arrays and conditions is an area of ongoing study.

   Use of *solmode='L1R'* combines both the L1 and R modes
   described above, with the iterative clamped L1 loop occuring
   inside the R outliner excision threshold sequence loop.
   

.. _Examples:

Examples
   To solve for G on, say, fields 1 & 2, on a 90s timescale, and do
   so relative to gaincurve and bandpass corrections:
   
   ::
   
      gaincal('data.ms',
              caltable='cal.G90s',          # Write solutions to disk file 'cal.G'
              field='0,1',                  # Restrict field selection
              solint='90s',                 # Solve for phase and amp on a 90s timescale
              gaintable=['cal.B','cal.gc'], # prior bandpass and gaincurve tables
              refant='3')                   # reference antenna
   
   To solve for more rapid tropopheric gains (3s timescale) using the
   above G solution, use *gaintype='T'*:
   
   ::
   
      gaincal(vis='data.ms',
              caltable='cal.T',             # Output table name
              gaintype='T',                 # Solve for T (polarization-independent)
              field='0,1',                  # Restrict data selection to calibrators
              solint='3s',                  # Obtain solutions on a 3s timescale
              gaintable=['cal.B','cal.gc','cal.G90s'],   # all prior cal
              refant='3')                   # reference antenna
   
   To solve for GSPLINE phase and amplitudes, with splines of
   duration 600 seconds:
   
   ::
   
      gaincal('data.ms',
              caltable='cal.spline.ap',
              gaintype='GSPLINE'       #   Solve for GSPLINE
              calmode='ap'             #   Solve for amp & phase
              field='0,1',             #   Restrict data selection to calibrators
              splinetime=600.)         #   Set spline timescale to 10min


.. _Development:

Development
   No additional development details

