#
# stub function definition file for docstring parsing
#

def fringefit(vis, caltable='', field='', spw='', intent='', selectdata=True, timerange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='', refant='', minsnr=3.0, zerorates=False, globalsolve=True, niter=100, delaywindow=[''], ratewindow=[''], append=False, corrdepflags=False, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[''], paramactive=[''], parang=False):
    r"""
Fringe fit delay and rates

Parameters
   - **vis** (string) - Name of input visibility file [1]_
   - **caltable** (string='') - Name of output gain calibration table [2]_
   - **field** (string='') - Select field using field id(s) or field name(s) [3]_
   - **spw** (string='') - Select spectral window/channels [4]_
   - **intent** (string='') - Select observing intent [5]_
   - **selectdata** (bool=True) - Other data selection parameters [6]_

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - **timerange** (string='') - Select data based on time range [7]_
      - **antenna** (string='') - Select data based on antenna/baseline [8]_
      - **scan** (string='') - Scan number range [9]_
      - **observation** ({string, int}='') - Select by observation ID(s) [10]_
      - **msselect** (string='') - Optional complex data selection (ignore for now) [11]_

      .. raw:: html

         </details>
   - **solint** (variant='inf') - Solution interval: egs. \'inf\', \'60s\' (see help) [12]_
   - **combine** (string='') - Data axes which to combine for solve (obs, scan, spw, and/or field) [13]_
   - **refant** (string='') - Reference antenna name(s) [14]_
   - **minsnr** (double=3.0) - Reject solutions below this signal-to-noise ratio (at the FFT stage) [15]_
   - **zerorates** (bool=False) - Zero delay-rates in solution table [16]_
   - **globalsolve** (bool=True) - Refine estimates of delay and rate with global least-squares solver [17]_
   - **niter** (int=100) - Maximum number of iterations for least-squares solver [18]_
   - **delaywindow** (doubleArray=['']) - Constrain FFT delay search to a window [19]_
   - **ratewindow** (doubleArray=['']) - Constrain FFT rate search to a window [20]_
   - **append** (bool=False) - Append solutions to the (existing) table [21]_
   - **corrdepflags** (bool=False) - Respect correlation-dependent flags [22]_
   - **docallib** (bool=False) - Use callib or traditional cal apply parameters [23]_

      .. raw:: html

         <details><summary><i> docallib = False </i></summary>

      - **gaintable** (stringArray=['']) - Gain calibration table(s) to apply on the fly [25]_
      - **gainfield** (stringArray=['']) - Select a subset of calibrators from gaintable(s) [26]_
      - **interp** (stringArray=['']) - Temporal interpolation for each gaintable (''=linear) [27]_
      - **spwmap** (intArray=['']) - Spectral window mappings to form for gaintable(s) [28]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> docallib = True </i></summary>

      - **callib** (string='') - Cal Library filename [24]_

      .. raw:: html

         </details>
   - **paramactive** (boolArray=['']) - Control which parameters are solved for [29]_
   - **parang** (bool=False) - Apply parallactic angle correction on the fly [30]_


Description
   .. warning:: **WARNING: fringefit**is currently an experimental task. Use
      with care and report issues back to the CASA team via the`NRAO
      helpdesk <http://help.nrao.edu/>`__. Notethat calibration
      tables made with fringefit in CASA 5.5 will not work in CASA
      5.6 and later.

   | The **fringefit** task determines phase, delay, delay-rate and
     (optionally) dispersive delay solutions as a function of time
     and spectral window, thus enabling correction of visibility
     phases for errors introduced by the atmosphere, the signal paths
     of the instrument, or other pre-calibration steps. It can
     correct a single scan on a bright source for delay offsets
     between spectral windows, which can result from instrumental
     signal paths (single-band delays), and it can correct multiple
     scans on a source to correct for errors that are variable in
     time (multi-band delay and delay rate). The task uses the model
     data column when present in the MeasurementSet. Fringe fitting
     is primarily useful for VLBI.
   | 

   .. rubric:: Introduction
      

   | In Very Long Baseline Interferometry (VLBI), fringe-fitting is
     an essential step which is not typically used for connected
     element arrays such as JVLA and ALMA. The very long baselines
     make observations particularly sensitive to small errors in the
     correlator model (station positions), signal chain, and the
     temporally- and spatially-variable atmosphere. The errors
     manifest themselves as residual delays (which introduce a slope
     when plotting phase against frequency) and delay-rates (which
     cause the phase offset at, say, the center of the band to drift
     as a function of time). Additionally at low frequencies and
     large fractional bandwidths a dispersive delay can be observed
     proportional (in time) to the inverse of the square of frequency
     and therefore proportional to the reciprocal of the frequency in
     phase. These errors can be corrected by observations of a bright
     calibrator source and a phase reference source which is close to
     the target source in projection on the sky.
   | Prior to running **fringefit** it is recommended to calibrate
     the amplitudes, as the weights are used by **fringefit** to
     determine the reliability of the fringe detection. A tunable
     SNR-cutoff is implemented to allow weak fringes and
     non-detections to be discarded. Bandpass correction can be done
     either before or after fringe fitting using
     **bandpass**. **** Since the CASA **bandpass** is a simple
     complex gain correction, it will be more efficient after fringe
     fitting when VLBI-style geometrical errors are important.
   | The algorithm used in **fringefit**, based on the Schwab-Cotton
     algorithm (originally implemented in the AIPS task FRING), has
     two stages. The first step is to look for fringes on each
     baseline to a reference station separately and estimate the SNR
     value for each of these baselines using a Fast Fourier
     Transform. The fringes that pass the SNR requirement are passed
     through to the second step, a global least-squares solver that
     attempts to optimize the solutions and transform them into
     antenna-based solutions for phase, delay, rate and dispersive
     delay. All of the parameters except phase can be included or
     excluded in the solution at this phase using the *paramactive*
     keyword described below; the default is that phase, delay and
     rate are solved but dispersive delay is not, since this matches
     the historical default and the usage we expect to be most common
     in VLBI.

   .. note:: **NOTE**: For the multi-band delay, the solutions for the full
      combined spectral window are written for a notional spectral
      window 0. To account for this spectral windowin the
      **applycal** step, use the *spwmap* parameter to ensure that
      the solutions are correctly applied to all spectral windows
      (see the Examples tab for details).

   .. rubric:: Common calibration solve parameters
      

   See `Solving for
   Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__for
   more information on the task parameters **fringefit** shares with
   all solving tasks, including data selection, general solving
   properties and arranging prior calibration (i.e.,specifying other
   caltables to pre-apply before solving).Also see
   the**rerefant**task documentation for the behavior of reference
   antenna application. Below we describe parameters unique to
   **fringefit**and those common parameters with unique properties.

   .. note:: **NOTE**: Like **gaincal**, fringefit supports passing a list
      of antennas through the *refant* parameter. However
      **fringefit** does not implement the *refantmode* parameter and
      effectively always operates in 'flex' mode, using the next
      antenna from the list as the reference antenna if an antenna is
      not available.

   .. rubric:: Parameter descriptions
      

   .. rubric:: Solution interval: *solint*
      

   The solution interval specified in *solint* (in seconds) is used
   to group data. It is important to make sure that for intervals
   shorter than the scan length, the scan is divided into roughly
   equal sized solution intervals. Avoid selecting a solution
   interval that will lead to intervals containing a single
   integration time, as this will cause an error.

   .. rubric:: Combining data for solutions: *combine*
      

   As in other calibration solve tasks, data can be combined over
   different axes. To derive multi-band delay corrections, set
   *combine='spw'.*

   .. rubric:: SNR control: *minsnr*
      

   The *minsnr* parameter sets the threshold of the SNR value
   required for the baseline based fringe (FFT stage) to be included
   in the global least-squares minimization.

   .. rubric:: Rate-zeroing: *zerorates*
      

   When correcting instrumental delays by solving for each spectral
   window separately, it is usual to apply the corrections derived to
   the entire dataset. Extrapolating the rates in time is
   undesirable, so use of *zerorates=True* will cause no
   time-dependent rate correction to be applied. Note that with this
   option the rates are still solved, and zeroed only when written to
   the table; *paramactive* can be used to turn off solution of rates
   altogether but this is currently not recommended; *zerorates*(and
   its equivalent in other software) has been the standard practice
   in VLBI for a long time, and is likely to remain so.

   .. rubric:: Prior correction for parallactic angle: *parang*
      

   Although optional, it is is generally recomended that
   *parang=True* be used for VLBI observations, since parallactic
   angle causes differential phase rates among widely-separated
   antennas that usually should not be included within the
   **fringefit** solution.

   .. rubric:: Disabling the global least-squares solver:
      *globalsolve*
      

   By default, fringe-fit solutions are refined by a global
   least-squares optimization algorithm after the FFT stage. For some
   purposes, it is desirable to use the estimates from the FFT stage
   directly; this can be done by setting *globalsolve* =False. (The
   default is True)

   .. rubric:: Setting a maximum number of iterations: *niter*
      

   A maximum number of iterations for the global least squares solver
   can be set with the *niter* parameter. The default is 100; in
   cases with high signal-to-noise this limit is not reached.

   .. rubric:: Constrain the search window for delay:*delaywindow*
      

   Sometimes a priori information is available to constrain the
   delays relative to the reference station at the FFT search step.
   The upper and lower bounds (in nanoseconds) can be provided as a
   two element list through the keyword *delaywindow*. The value None
   can be used to leave either the upper or lower limit unconstrained
   (setting both to None constrains neither; this is the default).
   Note that the same constraint is applied to all baselines in the
   FFT search step.

   .. rubric:: Constrain the search window for rate:*ratewindow*
      

   Similarly to *delaywindow*, sometimes a priori information is
   available to constrain the delay rates relative to the reference
   station at the FFT search step. The upper and lower bounds (in
   units of seconds/second) can be provided as a two element list
   through the keyword *ratewindow*. The value None can be used to
   leave either the upper or lower limit unconstrained (setting both
   to None constrains neither; this is the default). Note that the
   same constraint is applied to all baselines in the FFT search
   step.

   .. rubric:: Select a weighting strategy for the least squares
      solver: *weightfactor*
      

   It is common in VLBI practice for the user to choose how weights
   of visiblities should be used in the global stage of
   fringe-fitting. In any array such as the EVN with a very sensitive
   antenna (in the EVN's case Effelsberg), the use of measurement set
   weights can mean that baselines to the sensitive antenna dominate
   and other baselines have neglibible impact. Choosing the square
   root of those weights gives, many users feel, a more balanced
   interpretation of the data.

   The *weightfactor* parameter allows the user to chose between
   strategies:

   -  0 => use a weight of 1 (i.e., ignore measurement set weights);
   -  1 => use the square-root of measurement set weights;
   -  2 => use the measurement set weights as they are (the default)

   .. rubric:: Select active parameters for least square solver:
      *paramactive*
      

   As part of the inclusion of a dispersive component of delay we
   have added a parameter to control which model parameters are used
   in the least-squares part of the solver (the FFT stage is
   unaffected). The *paramactive* parameter takes a Python list of
   boolean arguments for the delay, rate and dispersive components,
   with a default value of [True, True, False] to match the historic
   default, which is also expected to be the most common future
   use-case. Note that we do not offer users an opportunity not to
   solve for phase offset (also known as "secular phase").




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file
.. [2] 
   **caltable** (string='')
      | Name of output gain calibration table
.. [3] 
   **field** (string='')
      | Select field using field id(s) or field name(s)
.. [4] 
   **spw** (string='')
      | Select spectral window/channels
.. [5] 
   **intent** (string='')
      | Select observing intent
.. [6] 
   **selectdata** (bool=True)
      | Other data selection parameters
.. [7] 
   **timerange** (string='')
      | Select data based on time range
.. [8] 
   **antenna** (string='')
      | Select data based on antenna/baseline
.. [9] 
   **scan** (string='')
      | Scan number range
.. [10] 
   **observation** ({string, int}='')
      | Select by observation ID(s)
.. [11] 
   **msselect** (string='')
      | Optional complex data selection (ignore for now)
.. [12] 
   **solint** (variant='inf')
      | Solution interval: egs. \'inf\', \'60s\' (see help)
.. [13] 
   **combine** (string='')
      | Data axes which to combine for solve (obs, scan, spw, and/or field)
.. [14] 
   **refant** (string='')
      | Reference antenna name(s)
.. [15] 
   **minsnr** (double=3.0)
      | Reject solutions below this signal-to-noise ratio (at the FFT stage)
.. [16] 
   **zerorates** (bool=False)
      | Zero delay-rates in solution table
      | 
      |         Write a solution table with delay-rates zeroed, for the case of
      |     "manual phase calibration", so that the calibration table can be
      |     applied to the full dataset without the extrapolation of a non-zero delay-rate term
      |     affecting the data
.. [17] 
   **globalsolve** (bool=True)
      | Refine estimates of delay and rate with global least-squares solver
.. [18] 
   **niter** (int=100)
      | Maximum number of iterations for least-squares solver
.. [19] 
   **delaywindow** (doubleArray=[''])
      | Constrain FFT delay search to a window specified as a two-element list with units of nanoseconds
      |     Default: [None, None]
      |     Examples: [-10, 10]
.. [20] 
   **ratewindow** (doubleArray=[''])
      | Constrain FFT rate search to a window specified as a two-element list with units of seconds per second
      |       Default: [None, None]
      |       Examples: [-1e-13, 1e-13]
.. [21] 
   **append** (bool=False)
      | Append solutions to the (existing) table
      |     Default: False (overwrite existing table or make
      |     new table)
      | 
      |     Appended solutions must be derived from the same
      |     MS as the existing caltable, and solution spws
      |     must have the same meta-info (according to spw
      |     selection and solint) or be non-overlapping.
.. [22] 
   **corrdepflags** (bool=False)
      | If False (default), if any correlation is flagged, treat all correlations in
      |         the visibility vector as flagged when solving (per channel, per baseline).
      |         If True, use unflagged correlations in a visibility vector, even if one or more
      |         other correlations are flagged.
      |               
      |         Default: False (treat correlation vectors with one or more correlations flagged as entirely flagged)
      |   
      |         Traditionally, CASA has observed a strict interpretation of 
      |         correlation-dependent flags: if one or more correlations 
      |         (for any baseline and channel) is flagged, then all available 
      |         correlations for the same baseline and channel are 
      |         treated as flagged.  However, it is desirable in some 
      |         circumstances to relax this stricture, e.g., to preserve use
      |         of data from antennas with only one good polarization (e.g., one polarization
      |         is bad or entirely absent).  Solutions for the bad or missing polarization 
      |         will be rendered as flagged.
.. [23] 
   **docallib** (bool=False)
      | Control means of specifying the caltables
      |                      Default: False (Use gaintable, gainfield, interp,
      |                      spwmap, calwt)
      |                      Options: False|True
      | 
      |                      If True, specify a file containing cal library in
      |                      callib
.. [24] 
   **callib** (string='')
      | Specify a file containing cal library directives
      |     Subparameter of docallib=True
.. [25] 
   **gaintable** (stringArray=[''])
      | Gain calibration table(s) to apply on the fly
      |     Default: '' (none)
      |     Subparameter of docallib=False
      |     Examples: 
      |     gaintable='ngc5921.gcal'
      |     gaintable=['ngc5921.ampcal','ngc5921.phcal']
.. [26] 
   **gainfield** (stringArray=[''])
      | Select a subset of calibrators from gaintable(s)
      |     Default: '' (all sources on the sky)
      | 
      |     'nearest' ==> nearest (on sky) available field in
      |     table otherwise, same syntax as field
      | 
      |     Examples: 
      |     gainfield='0~2,5' means use fields 0,1,2,5
      |     from gaintable
      |     gainfield=['0~3','4~6'] means use field 0
      |     through 3
.. [27] 
   **interp** (stringArray=[''])
      | Interpolation parameters (in time[,freq]) for each gaintable, as a list of strings.
      |     Default: '' --> 'linear,linear' for all gaintable(s)
      |     Options: Time: 'nearest', 'linear'
      |     Freq: 'nearest', 'linear', 'cubic',
      |     'spline'
      |     Specify a list of strings, aligned with the list of caltable specified
      |     in gaintable, that contain the required interpolation parameters
      |     for each caltable.
      |     * When frequency interpolation is relevant (B, Df,
      |     Xf), separate time-dependent and freq-dependent
      |     interp types with a comma (freq_after_ the
      |     comma). 
      |     * Specifications for frequency are ignored when the
      |     calibration table has no channel-dependence. 
      |     * Time-dependent interp options ending in 'PD'
      |     enable a "phase delay" correction per spw for
      |     non-channel-dependent calibration types.
      |     * For multi-obsId datasets, 'perobs' can be
      |     appended to the time-dependent interpolation
      |     specification to enforce obsId boundaries when
      |     interpolating in time. 
      |     * Freq-dependent interp options can have 'flag' appended
      |     to enforce channel-dependent flagging, and/or 'rel' 
      |     appended to invoke relative frequency interpolation
      | 
      |     Examples: 
      |     interp='nearest' (in time, freq-dep will be
      |     linear, if relevant)
      |     interp='linear,cubic'  (linear in time, cubic
      |     in freq)
      |     interp='linearperobs,splineflag' (linear in
      |     time per obsId, spline in freq with
      |     channelized flagging)
      |     interp='nearest,linearflagrel' (nearest in
      |     time, linear in freq with with channelized 
      |     flagging and relative-frequency interpolation)
      |     interp=',spline'  (spline in freq; linear in
      |     time by default)
      |     interp=['nearest,spline','linear']  (for
      |     multiple gaintables)
.. [28] 
   **spwmap** (intArray=[''])
      | Spectral window mappings to form for gaintable(s)
      |                      Only used if callib=False
      |                      default: [] (apply solutions from each calibration spw to
      |                      the same MS spw only)
      |                      Any available calibration spw can be mechanically mapped to any 
      |                       MS spw. 
      |                      Examples:
      |                         spwmap=[0,0,1,1] means apply calibration 
      |                           from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
      |                         spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
      |                           gaintables)
.. [29] 
   **paramactive** (boolArray=[''])
      | Control which parameters are solved for; a vector of (exactly) three booleans for delay, delay-rate and dispersive delay (in that order)
.. [30] 
   **parang** (bool=False)
      | Apply parallactic angle correction on the fly.

    """
    pass
