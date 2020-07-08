.. container::
   :name: viewlet-above-content-title

Preparing for Calibration
=========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   A description of the range of prior information necessary to solve
   for calibration

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      There is a range of *a priori* information that may need to be
      initialized or estimated before calibration solving is carried
      out.  This includes establishing prior information about the data
      within the MS:

      -  **weight initialization** --- if desired, initialization of
         spectral weights, using **initweight** (by default,
         unchannelized weight accounting is used, and no special action
         is required)
      -  **flux density models** --- establish the flux density scale
         using "standard" calibrator sources, with models for resolved
         calibrators, using **setjy** as well as deriving various prior
         calibration quanitities using various modes of **gencal**
      -  **gain curves** --- the antenna gain-elevation dependence
      -  **atmospheric optical depth** --- attenuation of the signal by
         the atmosphere, including correcting for its elevation
         dependence
      -  **antenna position errors** --- offsets in the positions of
         antennas assumed during correlation
      -  **ionosphere** --- dispersive delay and Faraday effects arising
         from signal transmission through the magnetized plasma of the
         ionosphere
      -  **switched power** (EVLA) --- electronic gains monitored by the
         EVLA online system
      -  **system temperature** (ALMA) --- turn correlation coefficient
         into correlated flux density (necessary for some telescopes)
      -  **generic cal factors** --- antenna-based amp, phase, delay

      These are all pre-determined effects and should be applied (if
      known) as priors when solving for other calibration terms, and
      included in the final application of all calibration.  If unknown,
      then they will be solved for or subsumed in other calibration such
      as bandpass or gains.

      Each of these will now be described in turn.

      .. rubric:: Weight Initialization
         :name: weight-initialization

      See the section on
      `data <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__
      weights\ `  <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__\ for
      a more complete description of weight accounting in CASA.

      CASA 4.3 introduced initial experimental support for spectral
      weights.  At this time, this is mainly relevant to ALMA processing
      for which *spectral* Tsys\ :math:`T_{sys}` corrections, which
      faithfully reflect spectral sensitivity, are available.  In most
      other cases, sensitivity is, to a very good approximation,
      channel-independent after bandpass calibration (and often also
      before), except perhaps at the very edges of spectral windows (and
      for which analytic expressions of the sensitivity loss are
      generally unavailable).  Averaging of data with channel-dependent
      flagging which varies on sufficiently short timescales will also
      generate channel-dependent net weights (see **split** or
      **mstransform** for more details).

      By default, CASA's weight accounting scheme maintains
      unchannelized weight information that is appropriately updated
      when calibration is applied.  In the case of spectral calibrations
      (Tsys\ :math:`T_{sys}` and bandpass), an appropriate spectral
      average is used for the weight update.  This spectral average is
      formally correct for weight update by bandpass.  For
      Tsys\ :math:`T_{sys}`, traditional treatments used a single
      measurement per spectral window; ALMA has implemented spectral
      Tsys\ :math:`T_{sys}` to better track sensitivity as a function of
      channel, and so should benefit from *spectral* weight accounting
      as described here, especially where atmospheric emmission lines
      occur.  If spectral weight accounting is desired, users must
      re-initialize the spectral weights using the **initweights** task:

       

      .. container:: casa-input-box

         initweights(vis='mydata.ms', wtmode='nyq', dowtsp=True)

      In this task, the *wtmode* parameter controls the weight
      initialization convention.  Usually, when initializing the weight
      information for a raw dataset, one should choose *wtmode='nyq'* so
      that the channel bandwidth and integration time information are
      used to initialize the weight information (as
      described `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__). 
      The *dowtsp* parameter controls whether or not (*True* or *False*)
      the spectral weights (the *WEIGHT_SPECTRUM* column) are
      initialized.  The default is *dowtsp=False*, wherein only the
      non-spectral weights (the *WEIGHT* column) will be initialized. 
      If the spectral weights have been initialized, then downstream
      processing that supports spectral weights will use and update
      them.  In CASA 4.3 and later, this includes **applycal**,
      **clean**, and **split**/**mstransform**; use of spectral weights
      in calibration solving (e.g., **gaincal** and other solve tasks)
      is scheduled for the CASA 5.0 release.

      Note that **importasdm** currently initializes the *non-spectral*
      weights using channel bandwidth and integration time information
      (equivalent to using *dospwt=False* in the above example.  In
      general, it only makes sense to run **initweights** on a raw
      dataset which has not yet been calibrated, and it should only be
      necessary if the filled weights are inappropriate, or if spectral
      weight accounting is desired in subsequent processing. It is
      usually *not* necessary to re-initialize the weight information
      when redoing calibration from scratch (the raw weight information
      is preserved in the *SIGMA*/*SIGMA_SPECTRUM* columns). 
      (Re-)initializing the weight information for data that has already
      been calibrated (with *calwt=True*, presumably) is formally
      incorrect and is not recommended.

      When combining datasets from different epochs, it is generally
      preferable to have used the same version of CASA (most recent is
      best), and with the same weight information conventions and
      *calwt* settings in calibration tasks.  Doing so will minimize the
      likelihood of arbitrary weight imbalances that might lead to net
      loss of sensitivity, and maximize the likelihood that *real*
      differences in per-epoch sensitivity (e.g., due to different
      weather conditions and instrumental setups) will be properly
      accounted for.  Modern instruments support more variety in
      bandwidth and integration time settings, and so use of these
      parameters in weight initialization is preferred (c.f. use of
      simple unit weight initialization, which has often been the
      traditional practice).

      .. container:: alert-box

         **Alert:** Full and proper weight accounting for the EVLA
         formally depends on the veracity of the switched power
         calibration scheme.  As of mid-2015, use of the EVLA switched
         power is not yet recommended for general use, and otherwise
         uniform weights are carried through the calibration process. 
         As such, spectral weight accounting is not yet meaningful. 
         Facilities for post-calibration estimation of spectral weights
         are rudimentarily supported in **statwt**.

      .. rubric:: Flux Density Models
         :name: flux-density-models

      It is necessary to be sure calibrators have appropriate models set
      for them before solving for calibration.  Please see the task
      documentation for **setjy** and **ft** for more information on
      setting non-trivial model information in the MS.   Also,
      information about setting models for flux density calibrators can
      be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-density-calibrator-models-conventions-data-formats>`__.  
      Fields in the MS for which no model has been explicitly set will
      be rendered as unpolarized unit flux density (1 Jy) point sources
      in calibration solving.

       

      .. rubric:: Antenna Gain-Elevation Curve Calibration
         :name: antenna-gain-elevation-curve-calibration

      Large antennas (such as the 25-meter antennas used in the VLA and
      VLBA) have a forward gain and efficiency that changes with
      elevation. Gain curve calibration involves compensating for the
      effects of elevation on the amplitude of the received signals at
      each antenna.  Antennas are not absolutely rigid, and so their
      effective collecting area and net surface accuracy vary with
      elevation as gravity deforms the surface.  This calibration is
      especially important at higher frequencies where the deformations
      represent a greater fraction of the observing wavelength.  By
      design, this effect is usually minimized (i.e., gain maximized)
      for elevations between 45 and 60 degrees, with the gain decreasing
      at higher and lower elevations.  Gain curves are most often
      described as 2nd- or 3rd-order polynomials in zenith angle.

      Gain curve calibration has been implemented in CASA for the modern
      VLA and old VLA (only), with gain curve polynomial coefficients
      available directly from the CASA data repository.  To make gain
      curve and antenna efficiency corrections for VLA data, use
      **gencal**:

      .. container:: casa-input-box

         gencal(vis='mydata.ms', caltable='gaincurve.cal',
         caltype='gceff')

      Use of *caltype='gceff'* generates a caltable that corrects for
      both the elevation dependence and an antenna-based efficiency unit
      conversion that will render the data in units of *approximate* Jy
      (NB: this is generally not a good substitute for proper flux
      density calibration, using **fluxscale**!).  Use of *caltype='gc'*
      or *caltype='eff'* can be used to introduce these corrections
      separately.

      The resulting calibration table should then be used in all
      subsequent processing the requires the specification of prior
      calibration.

      .. container:: alert-box

         **Alert:** If you are not using VLA data, do not use gaincurve
         corrections.  A general mechanism for incorporating gaincurve
         information for other arrays will be made available in future
         releases.  The gain-curve information available for the VLA is
         time-dependent (on timescales of months to years, at least for
         the higher frequencies), and CASA will automatically select the
         date-appropriate gain curve information.  Note, however, that
         the time-dependence was poorly sampled prior to 2001, and so
         gain curve corrections prior to this time should be considered
         with caution.

      .. rubric:: Atmospheric Optical Depth Correction
         :name: atmospheric-optical-depth-correction

      The troposphere is not completely transparent.  At high radio
      frequencies (>\ :math:`>`\ 15 GHz), water vapor and molecular
      oxygen begin to have a substantial effect on radio observations.
      According to the physics of radiative transmission, the effect is
      threefold.  First, radio waves from astronomical sources are
      absorbed (and therefore attenuated) before reaching the antenna. 
      Second, since a good absorber is also a good emitter, significant
      noise-like power will be added to the overall system noise, and
      thus further decreasing the *fraction* of correlated signal from
      astrophysical sources.  Finally, the optical path length through
      the troposphere introduces a time-dependent phase error.  In all
      cases, the effects become worse at lower elevations due to the
      increased air mass through which the antenna is looking.  In CASA,
      the opacity correction described here compensates only for the
      first of these effects, tropospheric attenuation, using a
      plane-parallel approximation for the troposphere to estimate the
      elevation dependence.  (Gain solutions solved for later will
      account for the other two effects.)

      To make opacity corrections in CASA, an estimate of the zenith
      opacity is required (see observatory-specific chapters for how to
      measure zenith opacity).  This is then supplied to the
      *caltype='opac'* parameter in **gencal** which creates a
      calibration table that will introduce the elevation-dependent
      correction when applied in later operaions. E.g. for data with two
      spectral windows:

      .. container:: casa-input-box

         | gencal(vis='mydatas.ms',
         |        caltable='opacity.cal',
         |        caltype='opac',
         |        spw='0,1',
         |        parameter=[0.0399,0.037])

      If you do not have an externally supplied value for *opacity*, for
      example from a VLA tip procedure, then you should either use an
      average value for the telescope, or omit this cal table and let
      your gain calibration compensate as best it can (e.g. that your
      calibrator is at the same elevation as your target at
      approximately the same time). As noted above, there are no
      facilities yet to estimate this from the data (e.g. by plotting
      Tsys\ :math:`T_{sys}` vs. elevation).

      The resulting calibration table should then be used in all
      subsequent processing the requires the specification of prior
      calibration.

      Below, we give instructions for determining opacity values for
      Jansky VLA data from weather statistics and VLA observations where
      tip-curve data is available.  It is beyond the scope of this
      description to provide information for other telescopes.

      .. rubric:: Determining opacity corrections for *modern* VLA data
         :name: determining-opacity-corrections-for-modern-vla-data

      For the VLA site, weather statistics and/or seasonal models that
      average over many years of weather statistics prove to be
      reasonable good ways to estimate the opacity at the time of the
      observations. The task **plotweather** calculates the opacity as a
      mix of both actual weather data and seasonal model. It can be run
      as follows:

      .. container:: casa-input-box

         myTau=plotweather(vis='mydata.ms',doPlot=True)

      The task plots the weather statistics if *doPlot=T*, generating a
      plot shown in the figure below. The bottom panel displays the
      calculated opacities for the run as well as a seasonal model. An
      additional parameter, *seasonal_weight* can be adjusted to
      calculate the opacities as a function of the weather data alone
      (*seasonal_weight=0*), only the seasonal model
      (*seasonal_weight=1*), or a mix of the two (values between 0 and
      1). Calculated opacities are shown in the logger output, one for
      each spectral window.  Note that **plotweather** returns a python
      list of opacity values with length equal to the number of spectral
      windows in the MS, appropriate for use in **gencal**:

      .. container:: casa-input-box

         gencal(vis='mydata.ms', caltype='opac', spw='0,1',
         parameter=myTau)  

      Note that the *spw* parameter is used non-trivially and explicitly
      here to indicate that the list of opacity values corresponds to
      the specified spectral windows.

      The resulting calibration table should then be used in all
      subsequent processing the requires the specification of prior
      calibration.

      |image1|

      +---------+-----------------------------------------------------------+
      | Type    | Figure                                                    |
      +---------+-----------------------------------------------------------+
      | ID      | plotwx                                                    |
      +---------+-----------------------------------------------------------+
      | Caption | The weather information for a MS as plotted by the task   |
      |         | {\tt plotweather}.}                                       |
      +---------+-----------------------------------------------------------+

       

      .. rubric:: Determining opacity corrections for historical VLA
         data
         :name: determining-opacity-corrections-for-historical-vla-data

      For VLA data, zenith opacity can be measured at the frequency and
      during the time observations are made using a VLA tipping scan in
      the observe file.  Historical tipping data are available
      `here. <http://www.vla.nrao.edu/astro/calib/tipper>`__  Choose a
      year, and click *Go* to get a list of all tipping scans that have
      been made for that year.

      If a tipping scan was made for your observation, then select the
      appropriate file.  Go to the bottom of the page and click on the
      button that says *Press here to continue*.  The results of the
      tipping scan will be displayed.  Go to the section called 'Overall
      Fit Summary' to find the fit quality and the fitted zenith opacity
      in percent.  If the zenith opacity is reported as 6%, then the
      actual zenith optical depth value is 0.060.  Use this value in
      **gencal** as described above.

      If there were no tipping scans made for your observation, then
      look for others made in the same band around the same time and
      weather conditions.  If nothing is available here, then at K and Q
      bands you might consider using an average value (e.g. 6% in
      reasonable weather).  See the VLA memo
      `here <http://www.vla.nrao.edu/memos/test/232/232.pdf>`__ for more
      on the atmospheric optical depth correction at the VLA, including
      plots of the seasonal variations.

       

      .. rubric:: Antenna-position corrections
         :name: antenna-position-corrections

      When antennas are moved, residual errors in the geographical
      coordinates of the antenna will cause time-dependent delay errors
      in the correlated data.  Normally, the observatory will solve for
      these offsets soon after the move and correct the correlator
      model, but sometimes science data is taken before the offsets are
      available, and thus the correction must be handled in
      post-processing. If the 3D position offsets for affected antennas
      are known, use **gencal** as follows:

      .. container:: casa-input-box

         gencal(vis='mydata.ms', caltable='antpos.cal',
         caltype='antpos', antenna='ea01',parameter=[0.01,0.02,0.005])

      In this execution, the position offset for antenna ea01 is
      [1cm,2cm,0.5cm] in an Earth-centered right-handed coordinate
      system with the first axis on the prime meridian and third axis
      coincident with the Earth's axis.  Corrections for multiple
      antennas can be specified by listing all affected antennas and
      extending the *parameter* list with as many offset triples as
      needed. 

      In general, it is difficut to know what position offsets to use,
      of course.  For the VLA, **gencal** will look up the required
      offests automatically, simply by omitting the *antenna *\ and
      *parameter* arguments:

      .. container:: casa-input-box

         gencal(vis='mydata.ms', caltable='antpos.cal',
         caltype='antpos')

      For the historical VLA, the antenna position coordinate system was
      a local one translated from the Earth's center and rotated to the
      VLA's longitude.  Use *caltype='antposvla'* to force this
      coordiate system when processing old VLA data.

      The resulting calibration table should then be used in all
      subsequent processing the requires the specification of prior
      calibration.

       

      .. rubric:: Ionospheric corrections
         :name: ionospheric-corrections

      CASA 4.3 introduced initial support for on-axis ionospheric
      corrections, using time- and direction-dependent total electron
      content (TEC) information obtained from the internet.  The
      correction includes the dispersive delay
      (∝ν−1\ :math:`\propto \nu^{-1}`) delay and Faraday rotation
      (∝ν−2\ :math:`\propto \nu^{-2}`) terms.  These corrections are
      most relevant at observing frequencies less than
      ∼\ :math:`\sim`\ 5 GHz.  When relevant, the ionosphere correction
      table should be generated at the beginning of a reduction along
      with other calibration priors (antenna position errors, gain
      curve, opacity, etc.), and carried through all subsequent
      calibration steps.  Formally, the idea is that the ionospheric
      effects (as a function of time and on-axis direction) will be
      nominally accounted for by this calibration table, and thus not
      spuriously leak into gain and bandpass solves, etc.  In practice,
      the quality of the ionospheric correction is limited by the
      relatively sparse sampling (in time and direction) of the
      available TEC information.  Especially active ionospheric
      conditions may not be corrected very well.  Also,
      direction-dependent (*within the instantaneous field-of-view*)
      ionosphere corrections are not yet supported.  Various
      improvements are under study for future releases.

      To generate the ionosphere correction table, first import a helper
      function from the casapy recipes repository:

      .. container:: casa-input-box

         from recipes import tec_maps

      Then, generate a TEC surface image:

      .. container:: casa-input-box

         tec_maps.create(vis='mydata.ms',doplot=T,imname='iono')

      This function obtains TEC information for the observing date and
      location from `NASA's CDDIS Archive of Space Geodesy
      Data <https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/atmospheric_products.html>`__,
      and generates a time-dependent CASA image containing this
      information.  The string specified for *imname* is used as a
      prefix for two output images, with suffixes *.IGS_TEC.im* (the
      actual TEC image) and *.IGS_RMS_TEC.im* (a TEC error image).  If
      *imname* is unspecified, the MS name (from *vis*) will be used as
      the prefix.

      The quality of the retrieved TEC information for a specific date
      improves with time after the observing date as CDDIS's ionospheric
      modelling improves, becoming optimal 1-2 weeks later.  Both images
      can be viewed as a movie in the CASA image **viewer**.  If
      *doplot=T*, the above function will also produce a plot of the TEC
      as a function of time in a vertical direction over the
      observatory.

      Finally, to generate the ionosphere correction caltable, pass the
      *.IGS\_TEC.im* image into **gencal**, using *caltype='tecim'*:

      .. container:: casa-input-box

         gencal(vis='mydata.ms',caltable='tec.cal',caltype='tecim',infile='iono.IGS_TEC.im')

      This iterates through the dataset and samples the zenith
      angle-dependent projected line-of-sight TEC for all times in the
      observation, storing the result in a standard CASA caltable. 
      Plotting this caltable will show how the TEC varies between
      observing directions for different fields and times, in particular
      how it changes as zenith angle changes, and including the nominal
      difference between science targets and calibrators.

      This caltable should then be used as a prior in all subsequent
      calibration solves, and included in the final **applycal**.

      A few warnings:

      -  The TEC information obtained from the web is relatively poorly
         sampled in time and direction, and so will not always describe
         the details of the ionospheric corruption, especially during
         active periods.
      -  For instrumental polarization calibration, it is recommended
         that an *unpolarized* calibrator be used; polarized calibrators
         may not yield as accurate a solution since the ionospheric
         corrections are not yet used properly in the source
         polarization portion of the **polcal** solve.

      Special thanks are due to Jason Kooi (UIowa) for his contributions
      to ionospheric corrections in CASA.

       

      .. rubric:: Switched-power (EVLA)
         :name: switched-power-evla

      The EVLA is equipped with noise diodes that synchronously inject a
      nominally constant and known power contribution appropriate for
      tracking electronic gain changes with time resolution as short as
      1 second.  The total power in both the ON and OFF states of the
      noise diodes is continuously recorded, enabling a gain calibration
      derived from their difference (as a fraction of the mean total
      power), and scaled by a the approximately known contributed power
      (nominally in K).  Including this calibration will render the data
      in units of (nominal) K, and also calibrate the data weights to
      units of inverse K\ :sup:`2`.  To generate a switched-power
      calibration table for use in subsequent processing, run **gencal**
      as follows:

      .. container:: casa-input-box

         gencal(vis='myVLAdata.ms',caltable='VLAswitchedpower.cal',caltype='evlagain')                      
          

      The resulting calibration table should then be used in all
      subsequent processing the requires the specification of prior
      calibration.

      To ensure that the weight calibration by this table works
      correctly, it is important that the raw data weights are
      proprotional to integration time and channel bandwidth.  This can
      be guaranteed by use of **initweights** as described above.

       

      .. rubric:: System Temperature (ALMA)
         :name: system-temperature-alma

      ALMA routinely measures Tsys\ :math:`T_{sys}` while observing, and
      these measurements are used to reverse the online normalization of
      the correlation coefficients and render the data in units of
      nominal K.  To generate a Tsys\ :math:`T_{sys}` calibration table,
      run **gencal** as follows:

      .. container:: casa-input-box

         gencal(vis='myALMAdata.ms',caltable='ALMAtsys.cal',caltype='tsys')                                  
          

      The resulting calibration table should then be used in all
      subsequent processing the requires the specification of prior
      calibration.

       

      .. rubric:: Miscellaneous ad hoc corrections
         :name: miscellaneous-ad-hoc-corrections

      The **gencal** task supports generating ad hoc amp, phase, and
      delay corrections via appropriate settings of the *caltype*
      parameter.  Currently, such factors must be constant in time
      (**gencal** has no mechanism for specifying multiple timestamps
      for parameters), but sometimes such corrections can be useful. 
      See the general **gencal** task documenation for more information
      on this type of correction.

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/plotwx-1.png/@@images/ecedf759-9ae0-4ac9-b7e8-e108ac9ec369.png
   :class: image-inline
