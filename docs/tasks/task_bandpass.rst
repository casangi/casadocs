

.. _Description:

Description
   Determines the amplitude and phase as a function of frequency for
   each spectral window containing more than one channel. Strong
   sources (or many observations of moderately strong sources) are
   needed to obtain accurate bandpass functions. The two solution
   choices are: individual antenna/based channel solutions 'B'; and a
   polynomial fit over the channels 'BPOLY'. The 'B' solutions can be
   determined at any specified time interval, and is recommended in
   most applications.

   .. rubric:: Introduction

   For channelized data, it is usually desirable to solve for the
   gain variations in frequency as well as in time. Variation in
   frequency arises as a result of non-uniform filter passbands or
   other frequency-dependent effects in signal transmission. It is
   usually the case that these frequency-dependent effects vary on
   timescales much longer than the time-dependent effects handled by
   **gaincal**. Thus, it makes sense to solve for them as a separate
   term, using the **bandpass** task.
   
   It is usually best to solve for the bandpass in channelized data
   before solving for the gain as a function of time. However, if the
   gains during the bandpass calibrator observations are fluctuating
   over the timerange of those observations, then it can be helpful
   to first solve for those time-dependent gains of that source with
   **gaincal**, and input these to **bandpass** via *gaintable*. See
   the examples section for more on how to do this.
   
   .. rubric:: Common calibration solve parameters

   See `"Solving for
   Calibration" <../../notebooks/synthesis_calibration.ipynb#Solve-for-Calibration>`__
   for more information on the task parameters **bandpass** shares
   with all solving tasks, including data selection, general solving
   properties and arrange prior calibration. Below we describe
   parameters unique to **bandpass**, and those common parameters
   with unique properties.
   
   .. warning:: **WARNING:** the channelization of the bandpass solution spws
      is set by the nominal channelization of the input data, not the
      selected portion. Edge-channels should be flagged if they are
      not to be taken into account in the further data processing. If
      edge channels are excluded by the spw selection but not
      flagged, then solutions for those channels will be
      extrapolated.
   
   .. rubric:: Bandpass types: *bandtype*
   
   The *bandtype* parameter selects the type of solution used for the
   **bandpass**. The choices are 'B' and 'BPOLY'.
   
   .. rubric:: *bandtype='B'*

   Use of *bandtype='B'* in **bandpass** differs from *gaintype='G'*
   in **gaincal** only in that it is determined for each channel in
   each spectral window. It is possible to solve for it as a function
   of time, but it is most efficient to keep the B solving timescale
   as long as possible, and use **gaincal** for frequency-independent
   rapid time-scale variations.
   
   Do not use *combine='spw'* with *bandtype='B'*, as this will
   generate a solution for all spws overlaid in *channel*
   coordinates, and for which it is not yet possible to apply to all
   spws in *frequency* coordinates.
   
   The B solutions are limited by the signal-to-noise ratio available
   per channel, which may be limited. It is therefore important that
   the data be optimally coherent over the time-range of the B
   solutions. As a result, B solutions are almost always preceded by
   an initial, provisional **gaincal** solution. In turn, if the B
   solution improves the frequency domain coherence significantly,
   subsequent **gaincal** solutions using it will be better than the
   original. The SNR per bandpass channel can also be boosted by
   using a non-trivial frequency solint to partially average the MS
   visibility frequency channels for the solution. However, for
   accuracy, it is important to use a frequency *solint* that doesn't
   obscure actual systematic bandpass structure. If adequate SNR is
   unachievable by these means with the available data, use of
   *bandtype='BPOLY'* can be considered.
   
   .. rubric:: *bandtype='BPOLY'*

   For some observations, it may be the case that the SNR per channel
   is insufficient to obtain a usable per-channel B solution. In this
   case it is desirable to solve instead for a best-fit functional
   form for each antenna using the BPOLY solver. The BPOLY solver
   fits (Chebychev) polynomials to the amplitude and phase of the
   calibrator visibilities as a function of frequency. Use of
   *combine='spw'* will cause a single common BPOLY solution to be
   determined in frequency space for all selected spectral windows in
   aggregate (plots of such solutions with plotcal will only show the
   evaluated polynomial for the first spw used in the solve). It is
   usually most meaningful to do per-spw solutions, unless groups of
   adjacent spectral windows are known *a priori* to share a single
   continuous bandpass response over their combined frequency
   range.
   
   The BPOLY solver requires a number of unique sub-parameters
   (default values are given below):
   
   ::
   
      bandtype        =    'BPOLY'   #   Type of bandpass solution (B or BPOLY)
           degamp     =          3   #   Polynomial degree for BPOLY amplitude solution
           degphase   =          3   #   Polynomial degree for BPOLY phase solution
           visnorm    =      False   #   Normalize data prior to BPOLY solution
           maskcenter =          0   #   Number of channels in BPOLY to avoid in center of band
           maskedge   =          0   #   Percent of channels in BPOLY to avoid at each band edge
   
   The *degamp* and *degphase* parameters indicate the polynomial
   degree desired for the amplitude and phase solutions. The
   *maskcenter* parameter is used to indicate the number of
   channels in the center of the band to avoid passing to the
   solution (e.g., to avoid Gibbs ringing in central channels for
   PdBI data). The *maskedge* parameter drops beginning and end
   channels. The *visnorm* parameter turns on normalization of the
   visibilities before the solution is obtained (rather than after
   as for *solnorm*).

   The *combine* parameter can be used to combine data across
   spectral windows, scans, and fields.

   Note that **bandpass** will allow you to use multiple fields,
   and can determine a single solution for all specified fields
   using *combine='field'.* If you want to use more than one field
   in the solution, it is prudent to use an initial **gaincal**
   using proper flux densities for all sources (not just 1 Jy) and
   use this table as an input to **bandpass** because in general
   the phase towards two (widely separated) sources will not be
   sufficiently similar to combine them, and you want the same
   amplitude scale. If you do not include amplitude in the initial
   **gaincal**, you probably want to set *visnorm=True* also to
   take out the amplitude normalization change. Note also in the
   case of multiple fields, that the BPOLY solution will be labeled
   with the field ID of the first field used in the BPOLY solution.

   .. rubric:: Bandpass calibration considerations

   **Bandpass normalization (*solnorm*)**
   
   The *solnorm* parameter requires more explanation in the context
   of the bandpass. Most users are used to seeing a normalized
   bandpass, where the mean amplitude is unity and fiducial phase is
   zero. Use of *solnorm=True* allows this. However, the parts of the
   bandpass solution normalized away will be still left in any data
   to which it is applied, and thus you should not use *solnorm=True*
   if the bandpass calibration is the end of your calibration
   sequence (e.g. you have already done all the gain calibration you
   want to).
   
   .. note:: **NOTE**: Setting *solnorm=True* will NOT rescale any previous
      calibration tables that the user may have supplied in
      gaintable.
   
   You can safely use *solnorm=True* if you do the **bandpass** first
   (perhaps using a throw-away initial **gaincal** calibration) as we
   suggest above, as later **gaincal** calibration stages will deal
   with this remaining calibration term. This does have the benefit
   of isolating the overall (channel independent) gains to the
   following **gaincal** stage. It is also recommended for the case
   where you have multiple scans on possibly different bandpass
   calibrators. It may also be preferred when applying the bandpass
   before doing **gaincal** and then **fluxscale**, as significant
   variation of bandpass among antennas could otherwise enter the
   gain solution and make (probably subtle) adjustments to the flux
   scale.
   
   We finally note that *solnorm=False* at the bandpass step in the
   calibration chain will still in the end produce the correct
   results. It only means that there will be a part of what we
   usually think of the gain calibration inside the bandpass
   solution, particularly if **bandpass** is run as the first step.
   
   .. rubric:: What if the bandpass calibrator has a significant
      spectral variation?
   
   The bandpass calibrator may have a spectral slope that will change
   the spectral properties of the solutions if a flat-spectrum model
   is used. If the slope is significant, the best remedy is to
   estimate the spectral shape and store that model in the bandpass
   calibrator MS. To do so, go through the normal steps of
   **bandpass** and the **gaincal** runs on the bandpass and flux
   calibrators, followed by **setjy** of the flux calibrator. The
   next step would be to use **fluxscale** on the bandpass calibrator
   to derive its spectral index. **fluxscale** can store this
   information in a python dictionary which is subsequently fed into
   a second **setjy** run, this time using the bandpass calibrator as
   the source and the derived spectrum (the python dictionary) as
   input. This step will create a source model with the correct
   overall spectral slope for the bandpass calibrator. Finally, rerun
   **bandpass** and all other calibration steps again, making use of
   the newly created internal bandpass model.
   
   .. rubric:: Combining spectral windows for bandpass calibration

   It may sometimes be desirable to combine spectral windows in
   **bandpass** solving, using *combine='spw'*.   This is useful,
   e.g., for calibrating the bandpass for HI observations (e.g.,
   at the VLA) when even the bandpass calibrator has its own HI
   lines or is absorbed by galactic HI.
   
   When using *combine='spw'* in **bandpass**, all selected spws
   (which must all have the same number of selected channels, have
   the same net sideband, and should probably all have the same
   net bandwidth, etc.) will effectively be averaged together to
   derive a single **bandpass** solution.  The channel frequencies
   assigned to the solution will be a channel-by-channel average
   over spws of the input channel frequencies (these may or may
   not coincide with the frequencies of the intended spectral
   window to which this solution is to be appied, depending on the
   symmetry of the observing setup).  The solution will be
   assigned the lowest spectral window id from the input spectral
   windows.   This solution can be applied to any other spectral
   window by using *spwmap* and adding *'rel'* to the frequency
   interpolation string for the **bandpass** table in the *interp*
   parameter.  See the section on "Prior calibration" at `Solve
   for
   Calibration <../../notebooks/synthesis_calibration.ipynb#Solve-for-Calibration>`__
   for more information about the mechanics of applying bandpass
   solutions of this sort.
   

.. _Examples:

Examples
   To solve for a B-bandpass using a single short scan on the
   calibrator (with no prior gain calibration available):
   
   ::
   
      bandpass(vis = 'n5921.ms',
               caltable='n5921.bcal',
               gaintable='',                   # No gain tables yet
               gainfield='',
               interp='',
               field='0',                      # Calibrator 1331+305 = 3C286 (FIELD_ID 0)
               spw='',                         # all channels
               selectdata=False,               # No other selection
               bandtype='B',                   # standard time-binned B (rather than BPOLY)
               solint='inf',                   # set solution interval arbitrarily long
               refant='15')                    # ref antenna 15 (=VLA:N2) (ID 14)
   
   On the other hand, we might have a number of scans on the bandpass
   calibrator spread over time, but we want a single bandpass
   solution. In this case, we could solve for and then pre-apply an
   initial gain calibration, and let the bandpass solution cross
   scans:
   
   ::
   
      bandpass(vis='n5921.ms',
               caltable='n5921.bcal',
               field='0',                      # Calibrator 1331+305 = 3C286 (FIELD_ID 0)
               spw='',                         # all channels
               selectdata=False,               # No other selection
               bandtype='B',                   # standard time-binned B (rather than BPOLY)
               solint='inf',                   # set solution interval arbitrarily long
               combine='scan',                 # Solution crosses scans(ID 14)
               refant='15',                    # ref antenna 15 (=VLA:N2)
               gaintable='n5921.init.gcal',    # Our previously determined G table
               gainfield='0',
               interp='linear')                # Do linear interpolation
   
   To solve for a single bandpass from two spectral windows (0 and 1)
   that is intended for a third (2), we add 'spw' to combine (also
   using a prior gain solution):
   
   ::
   
      bandpass(vis='n5921.ms',
               caltable='n5921.bcal2',
               field='0',                      # Calibrator 1331+305 = 3C286 (FIELD_ID 0)
               spw='0,1',                      # all channels in spws 0 and 1
               selectdata=False,               # No other selection
               bandtype='B',                   # standard time-binned B (rather than BPOLY)
               solint='inf',                   # set solution interval arbitrarily long
               combine='scan,spw',             # Combine scans and spws into a single solution
               refant='15',                    # ref antenna 15 (=VLA:N2)
               gaintable='n5921.init.gcal',    # Our previously determined G table
               gainfield='0',
               interp='linear')                # Do linear interpolation on gaintable
   
   The resulting bandpass table will have average channels labeled
   with the average frequencies of the input spectral windows
   channels.  Applying this solution will require use of relative
   frequency interpolation.   See
   `here <../../notebooks/synthesis_calibration.ipynb#Solve-for-Calibration>`__,
   for more information.
   
   To solve for a BPOLY (5th order in amplitude, 7th order in phase),
   using data from field 2, with prior **gaincal** corrections
   pre-applied:
   
   ::
   
      bandpass(vis='data.ms',          # input data set
               caltable='cal.BPOLY',   #
               spw='0:2~56',           # Use channels 3-57 (avoid end channels)
               field='0',              # Select bandpass calibrator (field 0)
               bandtype='BPOLY',       # Select bandpass polynomials
               degamp=5,               #   5th order amp
               degphase=7,             #   7th order phase
               gaintable='cal.G',      # Pre-apply gain solutions derived previously
               refant='14')            #

.. _Development:

Development
   No additional development details

