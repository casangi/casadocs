#
# stub function definition file for docstring parsing
#

def bandpass(vis, caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='scan', refant='', minblperant=4, minsnr=3.0, solnorm=False, bandtype='B', smodel=[''], corrdepflags=False, append=False, fillgaps=0, degamp=3, degphase=3, visnorm=False, maskcenter=0, maskedge=5, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[''], parang=False):
    r"""
Calculates a bandpass calibration solution

Parameters
   - vis_ (string) - Name of input visibility file
   - caltable_ (string='') - Name of output bandpass calibration table
   - field_ (string='') - Select field using field id(s) or field name(s)
   - spw_ (string='') - Select spectral window/channels
   - intent_ (string='') - Select observing intent
   - selectdata_ (bool=True) - Other data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - timerange_ (string='') - Select data based on time range
      - uvrange_ (variant='') - Select data within uvrange (default units meters)
      - antenna_ (string='') - Select data based on antenna/baseline
      - scan_ (string='') - Scan number range
      - observation_ ({string, int}='') - Select by observation ID(s)
      - msselect_ (string='') - Optional complex data selection (ignore for now)

      .. raw:: html

         </details>
   - solint_ (variant='inf') - Solution interval in time[,freq]
   - combine_ (string='scan') - Data axes which to combine for solve (obs, scan, spw, and/or field)
   - refant_ (string='') - Reference antenna name(s)
   - minblperant_ (int=4) - Minimum baselines _per antenna_ required for solve
   - minsnr_ (double=3.0) - Reject solutions below this SNR (only applies for bandtype = B)
   - solnorm_ (bool=False) - Normalize average solution amplitudes to 1.0 
   - bandtype_ (string='B') - Type of bandpass solution (B or BPOLY)

      .. raw:: html

         <details><summary><i> bandtype = B </i></summary>

      - fillgaps_ (int=0) - Fill flagged solution channels by interpolation

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> bandtype = BPOLY </i></summary>

      - degamp_ (int=3) - Polynomial degree for BPOLY amplitude solution
      - degphase_ (int=3) - Polynomial degree for BPOLY phase solution
      - visnorm_ (bool=False) - Normalize data prior to BPOLY solution
      - maskcenter_ (int=0) - Number of channels to avoid in center of each band
      - maskedge_ (int=5) - Fraction of channels to avoid at each band edge (in %)

      .. raw:: html

         </details>
   - smodel_ (doubleArray=['']) - Point source Stokes parameters for source model.
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
   Calibration" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__
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
      extrapolated. **
      **

   

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
   range. *
   *

   The BPOLY solver requires a number of unique sub-parameters
   (default values are given below):

   ::

      | bandtype = 'BPOLY' # Type of bandpass solution
        (B or BPOLY)
      |  degamp = 3 # Polynomial degree for
        BPOLY amplitude solution
      |  degphase = 3 # Polynomial degree for
        BPOLY phase solution
      |  visnorm = False # Normalize data prior to
        BPOLY solution
      |  maskcenter = 0 # Number of channels in
        BPOLY to avoid in center of band
      |  maskedge = 0 # Percent of channels in
        BPOLY to avoid at each band edge

   | The *degamp* and *degphase* parameters indicate the polynomial
     degree desired for the amplitude and phase solutions. The
     *maskcenter* parameter is used to indicate the number of
     channels in the center of the band to avoid passing to the
     solution (e.g., to avoid Gibbs ringing in central channels for
     PdBI data). The *maskedge* parameter drops beginning and end
     channels. The *visnorm* parameter turns on normalization of the
     visibilities before the solution is obtained (rather than after
     as for *solnorm*).
   | The *combine* parameter can be used to combine data across
     spectral windows, scans, and fields.
   | Note that **bandpass** will allow you to use multiple fields,
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
      

   .. rubric:: Bandpass normalization (*solnorm*)
      

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
      **bandpass** solving, using *combine='spw'*. This is useful,
      e.g., for calibrating the bandpass for HI observations (e.g.,
      at the VLA) when even the bandpass calibrator has its own HI
      lines or is absorbed by galactic HI.

      When using *combine='spw'* in **bandpass**, all selected spws
      (which must all have the same number of selected channels, have
      the same net sideband, and should probably all have the same
      net bandwidth, etc.) will effectively be averaged together to
      derive a single **bandpass** solution. The channel frequencies
      assigned to the solution will be a channel-by-channel average
      over spws of the input channel frequencies (these may or may
      not coincide with the frequencies of the intended spectral
      window to which this solution is to be appied, depending on the
      symmetry of the observing setup). The solution will be
      assigned the lowest spectral window id from the input spectral
      windows.  This solution can be applied to any other spectral
      window by using *spwmap* and adding *'rel'* to the frequency
      interpolation string for the **bandpass** table in the *interp*
      parameter. See the section on "Prior calibration" at `Solve
      for
      Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__
      for more information about the mechanics of applying bandpass
      solutions of this sort.





Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file
   |                      default: non
   | 
   |                         Example: vis='ngc5921.ms'

.. _caltable:

   .. rubric:: caltable

   | Name of output bandpass calibration table
   |                      default: none
   | 
   |                         Example: caltable='ngc5921.bcal'

.. _field:

   .. rubric:: field

   | Select field using field id(s) or field name(s)
   |                      default: '' --> all fields
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
   |                         type 'help par.selection' for more examples.

.. _intent:

   .. rubric:: intent

   | Select observing intent
   |                      default: '' (no selection by intent)
   | 
   |                         Example: intent='*BANDPASS*'  (selects data
   |                         labelled with BANDPASS intent)

.. _selectdata:

   .. rubric:: selectdata

   | Other data selection parameters
   |                      default: True

.. _timerange:

   .. rubric:: timerange

   | Select data based on time range
   |                      Subparameter of selectdata=True
   |                      default = '' (all)
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

   | Select data within uvrange (default units meters)
   |                      Subparameter of selectdata=True
   |                      default: '' (all)
   | 
   |                         Examples:
   |                         uvrange='0~1000klambda'; uvrange from 0-1000
   |                         kilo-lambda
   |                         uvrange='>4klambda';uvranges greater than 4
   |                         kilolambda

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline
   |                      Subparameter of selectdata=True
   |                      default: '' (all)
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
   | 
   |                      Note: just for antenna selection, an integer (or
   |                      integer list) is converted to a string and
   |                      matched against the antenna 'name' first. Only if
   |                      that fails, the integer is matched with the
   |                      antenna ID. The latter is the case for most
   |                      observatories, where the antenna name is not
   |                      strictly an integer.

.. _scan:

   .. rubric:: scan

   | Scan number range
   |                      Subparameter of selectdata=True
   |                      default: '' = all
   | 
   |                      Check 'go listobs' to insure the scan numbers are
   |                      in order.

.. _observation:

   .. rubric:: observation

   | Select by observation ID(s)
   |                      Subparameter of selectdata=True
   |                      default: '' = all
   | 
   |                          Example: observation='0~2,4'

.. _msselect:

   .. rubric:: msselect

   | Optional complex data selection (ignore for now)

.. _solint:

   .. rubric:: solint

   | Solution interval in time[,freq]
   |                      default: 'inf' (~infinite, up to boundaries
   |                      controlled by combine, with no pre-averaging in
   |                      frequency)
   |                      Options for time: 'inf' (~infinite), 'int' (per
   |                      integration), any float or integer value with or
   |                      without units
   |                      Options for freq: an integer with 'ch' suffix
   |                      will enforce pre-averaging by the specified
   |                      number of channels. A numeric value suffixed with
   |                      frequency units (e.g., 'Hz','kHz','MHz') will
   |                      enforce pre-averaging by an integral number of
   |                      channels amounting to no more than the specified
   |                      bandwidth.
   | 
   |                         Examples: solint='1min'; solint='60s',
   |                         solint=60 --> 1 minute
   |                         solint='0s'; solint=0; solint='int' --> per
   |                         integration
   |                         solint='-1s'; solint='inf' --> ~infinite, up
   |                         to boundaries enforced by combine 
   |                         solint='inf,8Mhz' --> ~infinite in time, with
   |                         8MHz pre-average in freq 
   |                         solint='int,32ch' --> per-integration in time,
   |                         with 32-channel pre-average in freq

.. _combine:

   .. rubric:: combine

   | Data axes to combine for solving
   |                      default: 'scan' --> solutions will break at obs,
   |                      field, and spw boundaries but may extend over
   |                      multiple scans (per obs, field and spw) up to
   |                      solint.
   |                      Options: '','obs','scan','spw',field', or any
   |                      comma-separated combination in a single string.
   | 
   |                         Example: combine='scan,spw' --> extend
   |                         solutions over scan boundaries (up to the
   |                         solint), and combine spws for solving.

.. _refant:

   .. rubric:: refant

   | Reference antenna name(s); a prioritized list may be
   | specified
   |                      default: '' (no reference antenna)
   | 
   |                         Examples:
   |                         refant='13' (antenna with index 13) 
   |                         refant='VA04' (VLA antenna #4)
   |                         refant='EA02,EA23,EA13' (EVLA antenna EA02,
   |                         use EA23 and EA13 as alternates if/when EA02
   |                         drops out)
   |                      
   |                      Use 'go listobs' for antenna listing

.. _minblperant:

   .. rubric:: minblperant

   | Minimum baselines _per antenna_ required for solve
   |                      default: 4
   | 
   |                      Antennas with fewer baselines are excluded from
   |                      solutions. Amplitude solutions with fewer than 4
   |                      baselines, and phase solutions with fewer than 3
   |                      baselines are only trivially constrained, and are
   |                      no better than baseline-based solutions.
   | 
   |                         example: minblperant=10 --> Antennas
   |                         participating on 10 or more baselines are
   |                         included in the solve.

.. _minsnr:

   .. rubric:: minsnr

   | Reject solutions below this SNR (only applies for
   | bandtype = B)
   |                      default: 3.0

.. _solnorm:

   .. rubric:: solnorm

   | Normalize bandpass amplitudes and phase for each spw,
   | pol, ant, and timestamp
   |                      default: False (no normalization)

.. _bandtype:

   .. rubric:: bandtype

   | Type of bandpass solution (B or BPOLY)
   |                       default: 'B'
   | 
   |                       'B' does a channel by channel solution for each
   |                       specified spw. 
   |                       'BPOLY' is somewhat experimental. It will fit an
   |                       nth order polynomial for the amplitude and phase
   |                       as a function of frequency. Only one fit is made
   |                       for all specified spw, and edge channels should
   |                       be omitted.
   |                       Use taskname=plotcal in order to compare the
   |                       results from B and BPOLY.
   | 
   |                          Example: bandtype='BPOLY'

.. _smodel:

   .. rubric:: smodel

   | Point source Stokes parameters for source model.

.. _corrdepflags:

   .. rubric:: corrdepflags

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

.. _append:

   .. rubric:: append

   | Append solutions to the (existing) table
   |                      default: False (overwrite existing table or make
   |                      new table)
   | 
   |                      Append solutions to the (existing) table.
   |                      Appended solutions must be derived from the same
   |                      MS as the existing caltable, and solution spws
   |                      must have the same meta-info (according to spw
   |                      selection and solint) or be non-overlapping.

.. _fillgaps:

   .. rubric:: fillgaps

   | Fill flagged solution channels by interpolation
   |                      Subparameter of bandtype='B'  
   |                      default: 0 (don't interpolate)
   | 
   |                         Example: fillgaps=3 (interpolate gaps 3
   |                         channels wide and narrower)

.. _degamp:

   .. rubric:: degamp

   | Polynomial degree for BPOLY amplitude solution
   |                      Subparameter of bandtype='BPOLY'
   |                      default: 3
   | 
   |                         Example: degamp=2

.. _degphase:

   .. rubric:: degphase

   | Polynomial degree for BPOLY phase solution
   |                      Subparameter of bandtype='BPOLY'
   |                      default: 3
   | 
   |                         Example: degphase=2

.. _visnorm:

   .. rubric:: visnorm

   | Normalize data prior to BPOLY solution
   |                      Subparameter of bandtype='BPOLY'
   |                      default: False
   | 
   |                         Example: visnorm=True

.. _maskcenter:

   .. rubric:: maskcenter

   | Number of channels to avoid in center of each band
   |                      Subparameter of bandtype='BPOLY'
   |                      default: 0
   | 
   |                         Example: maskcenter=5 (BPOLY only)

.. _maskedge:

   .. rubric:: maskedge

   | Fraction of channels to avoid at each band edge (in %)
   |                      Subparameter of bandtype='BPOLY'
   |                      default: 5
   | 
   |                         Example: maskedge=3 (BPOLY only)

.. _docallib:

   .. rubric:: docallib

   | Control means of specifying the caltables
   |                      default: False --> Use gaintable, gainfield,
   |                      interp, spwmap, calwt. 
   | 
   |                      If True, specify a file containing cal library in
   |                      callib

.. _callib:

   .. rubric:: callib

   | Cal Library filename
   |                      Subparameter of callib=True
   | 
   |                      If docallib=True, specify a file containing cal
   |                      library directives

.. _gaintable:

   .. rubric:: gaintable

   | Gain calibration table(s) to apply on the fly
   |                      Subparameter of callib=False
   |                      default: '' (none)
   | 
   |                         Examples: gaintable='ngc5921.gcal'
   |                         gaintable=['ngc5921.ampcal','ngc5921.phcal']

.. _gainfield:

   .. rubric:: gainfield

   | Select a subset of calibrators from gaintable(s)
   |                      Subparameter of callib=False
   |                      default:'' --> all sources in table
   |                      
   |                      gaintable='nearest' --> nearest (on sky)
   |                      available field in table. Otherwise, same syntax
   |                      as field
   | 
   |                         Examples: 
   |                         gainfield='0~2,5' means use fields 0,1,2,5
   |                         from gaintable
   |                         gainfield=['0~3','4~6'] (for multiple
   |                         gaintables)

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
   |                      the same MS spw only)
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
   |                      default: False
   | 
   |                      If True, apply the parallactic angle correction
   |                      (required for polarization calibration)


    """
    pass
