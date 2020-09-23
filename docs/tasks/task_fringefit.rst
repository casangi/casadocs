

.. _Description:

Description
   calculates a fringe-fitting (phase/delay/rate) solution
   
   .. warning:: **WARNING: fringefit** is currently an experimental task. Use
      with care and report issues back to the CASA team via the `NRAO
      helpdesk <http://help.nrao.edu/>`__. Note that calibration
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
     **bandpass**. ** ** Since the CASA **bandpass** is a simple
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
      window 0. To account for this spectral window in the
      **applycal** step, use the *spwmap* parameter to ensure that
      the solutions are correctly applied to all spectral windows
      (see the Examples tab for details).
   
   .. rubric:: Common calibration solve parameters
      
   
   See `Solving for
   Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__ for
   more information on the task parameters **fringefit** shares with
   all solving tasks, including data selection, general solving
   properties and arranging prior calibration (i.e., specifying other
   caltables to pre-apply before solving). Also see
   the **rerefant** task documentation for the behavior of reference
   antenna application. Below we describe parameters unique to
   **fringefit** and those common parameters with unique properties. 
   
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
   altogether but this is currently not recommended; *zerorates* (and
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
   
   .. rubric:: Constrain the search window for delay: *delaywindow*
      
   
   Sometimes a priori information is available to constrain the
   delays relative to the reference station at the FFT search step.
   The upper and lower bounds (in nanoseconds) can be provided as a
   two element list through the keyword *delaywindow*. The value None
   can be used to leave either the upper or lower limit unconstrained
   (setting both to None constrains neither; this is the default).
   Note that the same constraint is applied to all baselines in the
   FFT search step.
   
   .. rubric:: Constrain the search window for rate: *ratewindow*
      
   
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
   

.. _Examples:

Examples
   task fringefit examples
   
   Single-band delay: calibration of delay only for a single scan on
   a bright calibrator:
   
   ::
   
      | fringefit(vis='data.ms',
      |           caltable='data.sbd',                  # write
        solutions to this table on disk
      |           scan='30',                            # use only
        scan 30
      |           solint='inf',                         # use all
        timestamps in the scan
      |           refant='EF',                          # a big
        antenna does well as reference antenna
      |           minsnr=50,                            # empirically
        proven to be a good value is anything over 25
      |           zerorates=True,                       # for
        instrumental delay rates should not be used
      |           gaintable=['data.tsys','data.gc'],    # apply the
        amplitude calibration on the fly
      |           parang=True)                          # always True
        for VLBI
   
   Multi-band delay: calibration of time-dependent delay and
   delay-rate for a phase reference source, relative to single-band
   delay solution from above:
   
   ::
   
      | fringefit(vis='data.ms',
      |           caltable='data.mbd',                  # write
        solutions to this table disk
      |           solint='60',                          # anything
        shorter than the scan length will give more than 1 solution
      |           combine='spw',                        # combine
        spectral windows for this step, gives only a solution for
        spw0
      |           field='1',                            # select the
        field that is your phase reference calibrator
      |           refant='EF',                          # pick a big
        antenna or one close to the geometric center of the array
      |           minsnr=50,                            # this seems
        to be a sensible value
      |           gaintable=['data.tys', 'data.gc', 'data.sbd'],   #
        apply amplitude calibration and single band delay on the fly
      |           parang=True)                          # always set
        to True for VLBI
   
   The calibration table data.mbd will contain phase, delay, and rate
   solutions per antenna, per polarization and per solution interval.
   For data with multiple spectral windows the solutions will be
   assigned to spectral window 0 in the output cal table. In the
   **applycal** step, the parameter *spwmap* needs to be set to apply
   the solutions to all spectral windows. For example, in a dataset
   with 8 spectral windows: *spwmap=[8*[0]]*. Since the **applycal**
   step will include multiple calibration tables, this setting needs
   to correspond to the data.mbd table in the *gaintable* parameter:
   
   ::
   
      | applycal(vis='data.ms',
      |          field='0,1',                           # now select
        the phase calibrator AND the target source
      |          gaintable=['data.tsys', 'data.gc','data.sbd',
        'data.mbd'],    # include all the calibration tables
      |          interp=[],spwmap=[[], [], [],
        8*[0]],                         # map the spectral windows
        accordingly
      |          parang=True)                           # for VLBI
        this should always be True
   
   In cases where it is necessary to constrain the search for group
   delay and fringe rates at the FFT stage, the parameters
   *delaywindow* and *ratewindow* can be used:
   
   ::
   
      | fringefit(vis='data.ms',
      |           caltable='data.mbd',            # write solutions
        to this table disk
      |           solint='60',                    # anything shorter
        than the scan length will give more than 1 solution
      |           combine='spw',                  # combine spectral
        windows for this step, gives only a solution for spw0
      |           field='1',                      # select the field
        that is your phase reference calibrator
      |           refant='EF',                    # pick a big
        antenna or one close to the geometric center of the array
      |           minsnr=5,                       # we're looking for
        weak detections, but we have a good a priori idea of where
        they are to steer the FFT search
      |           delaywindow = [0,10],           # FFT delay search
        range of 0 to 10 nanoseconds
      |           ratewindow = [-5e-9,5e-9],      # FFT rate search
        range of -5 to 5 nanoseconds per second
      |           gaintable=['data.tys', 'data.gc', 'data.sbd'],   #
        apply amplitude calibration and single band delay on the fly
      |           parang=True)                    # always set to
        True for VLBI
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   