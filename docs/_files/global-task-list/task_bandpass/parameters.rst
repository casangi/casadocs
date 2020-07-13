Parameters
==========

.. container:: documentDescription description

   task bandpass parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file default: non Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      caltable : string

   Name of output bandpass calibration table default: none Example:
   caltable='ngc5921.bcal'

Example

.. container:: param

   .. container:: parameters2

      field : string

   Select field using field id(s) or field name(s) default: '' --> all
   fields Use 'go listobs' to obtain the list id's or names. If field
   string is a non-negative integer, it is assumed a field index,
   otherwise, it is assumed a field name. Examples: field='0~2'; field
   ids 0,1,2 field='0,4,5~7'; field ids 0,4,5,6,7 field='3C286,3C295';
   field named 3C286 and 3C295 field = '3,4C*'; field id 3, all names
   starting with 4C

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Select spectral window/channels Examples: spw='0~2,4'; spectral
   windows 0,1,2,4 (all channels) spw='<2'; spectral windows less than 2
   (i.e. 0,1) spw='0:5~61'; spw 0, channels 5 to 61, INCLUSIVE
   spw='*:5~61'; all spw with channels 5 to 61 spw='0,10,3:3~45'; spw
   0,10 all channels, spw 3, channels 3 to 45. spw='0~2:2~6'; spw 0,1,2
   with channels 2 through 6 in each. spw='0:0~10;15~60'; spectral
   window 0 with channels 0-10,15-60. (NOTE ';' to separate channel
   selections) spw='0:0~10^2,1:20~30^5'; spw 0, channels 0,2,4,6,8,10,
   spw 1, channels 20,25,30 type 'help par.selection' for more examples.

Example

.. container:: param

   .. container:: parameters2

      intent : string

   Select observing intent default: '' (no selection by intent) Example:
   intent='*BANDPASS*' (selects data labelled with BANDPASS intent)

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Other data selection parameters default: True

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Select data based on time range Subparameter of selectdata=True
   default = '' (all) Examples: timerange =
   'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss' (Note: if YYYY/MM/DD is
   missing date defaults to first day in data set.)
   timerange='09:14:0~09:54:0' picks 40 min on first day timerange=
   '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
   timerange='09:44:00' pick data within one integration of time
   timerange='>10:24:00' data after this time

Example

.. container:: param

   .. container:: parameters2

      uvrange : undefined

   Select data within uvrange (default units meters) Subparameter of
   selectdata=True default: '' (all) Examples: uvrange='0~1000klambda';
   uvrange from 0-1000 kilo-lambda uvrange='>4klambda';uvranges greater
   than 4 kilolambda

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Select data based on antenna/baseline Subparameter of selectdata=True
   default: '' (all) Examples: antenna='5&6'; baseline between antenna
   index 5 and index 6. antenna='VA05&VA06'; baseline between VLA
   antenna 5 and 6. antenna='5&6;7&8'; baselines with indices 5-6 and
   7-8 antenna='5'; all baselines with antenna index 5 antenna='05'; all
   baselines with antenna number 05 (VLA old name) antenna='5,6,10'; all
   baselines with antennas 5,6,10 index numbers Note: just for antenna
   selection, an integer (or integer list) is converted to a string and
   matched against the antenna 'name' first. Only if that fails, the
   integer is matched with the antenna ID. The latter is the case for
   most observatories, where the antenna name is not strictly an
   integer.

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Scan number range Subparameter of selectdata=True default: '' = all
   Check 'go listobs' to insure the scan numbers are in order.

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Select by observation ID(s) Subparameter of selectdata=True default:
   '' = all Example: observation='0~2,4'

Example

.. container:: param

   .. container:: parameters2

      msselect : string

   Optional complex data selection (ignore for now)

Example

.. container:: param

   .. container:: parameters2

      solint : undefined = inf

   Solution interval in time[,freq] default: 'inf' (~infinite, up to
   boundaries controlled by combine, with no pre-averaging in frequency)
   Options for time: 'inf' (~infinite), 'int' (per integration), any
   float or integer value with or without units Options for freq: an
   integer with 'ch' suffix will enforce pre-averaging by the specified
   number of channels. A numeric value suffixed with frequency units
   (e.g., 'Hz','kHz','MHz') will enforce pre-averaging by an integral
   number of channels amounting to no more than the specified bandwidth.
   Examples: solint='1min'; solint='60s', solint=60 --> 1 minute
   solint='0s'; solint=0; solint='int' --> per integration solint='-1s';
   solint='inf' --> ~infinite, up to boundaries enforced by combine
   solint='inf,8Mhz' --> ~infinite in time, with 8MHz pre-average in
   freq solint='int,32ch' --> per-integration in time, with 32-channel
   pre-average in freq

Example

.. container:: param

   .. container:: parameters2

      combine : string = scan

   Data axes to combine for solving default: 'scan' --> solutions will
   break at obs, field, and spw boundaries but may extend over multiple
   scans (per obs, field and spw) up to solint. Options:
   '','obs','scan','spw',field', or any comma-separated combination in a
   single string. Example: combine='scan,spw' --> extend solutions over
   scan boundaries (up to the solint), and combine spws for solving.

Example

.. container:: param

   .. container:: parameters2

      refant : string

   Reference antenna name(s); a prioritized list may be specified
   default: '' (no reference antenna) Examples: refant='13' (antenna
   with index 13) refant='VA04' (VLA antenna #4) refant='EA02,EA23,EA13'
   (EVLA antenna EA02, use EA23 and EA13 as alternates if/when EA02
   drops out) Use 'go listobs' for antenna listing

Example

.. container:: param

   .. container:: parameters2

      minblperant : int = 4

   Minimum baselines \_per antenna\_ required for solve default: 4
   Antennas with fewer baselines are excluded from solutions. Amplitude
   solutions with fewer than 4 baselines, and phase solutions with fewer
   than 3 baselines are only trivially constrained, and are no better
   than baseline-based solutions. example: minblperant=10 --> Antennas
   participating on 10 or more baselines are included in the solve.

Example

.. container:: param

   .. container:: parameters2

      minsnr : double = 3.0

   Reject solutions below this SNR (only applies for bandtype = B)
   default: 3.0

Example

.. container:: param

   .. container:: parameters2

      solnorm : bool = False

   Normalize bandpass amplitudes and phase for each spw, pol, ant, and
   timestamp default: False (no normalization)

Example

.. container:: param

   .. container:: parameters2

      bandtype : string = B

   Type of bandpass solution (B or BPOLY) default: 'B' 'B' does a
   channel by channel solution for each specified spw. 'BPOLY' is
   somewhat experimental. It will fit an nth order polynomial for the
   amplitude and phase as a function of frequency. Only one fit is made
   for all specified spw, and edge channels should be omitted. Use
   taskname=plotcal in order to compare the results from B and BPOLY.
   Example: bandtype='BPOLY'

Allowed Value(s)

B BPOLY

Example

.. container:: param

   .. container:: parameters2

      smodel : doubleArray

   Point source Stokes parameters for source model.

Example

.. container:: param

   .. container:: parameters2

      corrdepflags : bool = False

   If False (default), if any correlation is flagged, treat all
   correlations in the visibility vector as flagged when solving (per
   channel, per baseline). If True, use unflagged correlations in a
   visibility vector, even if one or more other correlations are
   flagged. Default: False (treat correlation vectors with one or more
   correlations flagged as entirely flagged) Traditionally, CASA has
   observed a strict interpretation of correlation-dependent flags: if
   one or more correlations (for any baseline and channel) is flagged,
   then all available correlations for the same baseline and channel are
   treated as flagged. However, it is desirable in some circumstances to
   relax this stricture, e.g., to preserve use of data from antennas
   with only one good polarization (e.g., one polarization is bad or
   entirely absent). Solutions for the bad or missing polarization will
   be rendered as flagged.

Example

.. container:: param

   .. container:: parameters2

      append : bool = False

   Append solutions to the (existing) table default: False (overwrite
   existing table or make new table) Append solutions to the (existing)
   table. Appended solutions must be derived from the same MS as the
   existing caltable, and solution spws must have the same meta-info
   (according to spw selection and solint) or be non-overlapping.

Example

.. container:: param

   .. container:: parameters2

      fillgaps : int = 0

   Fill flagged solution channels by interpolation Subparameter of
   bandtype='B' default: 0 (don't interpolate) Example: fillgaps=3
   (interpolate gaps 3 channels wide and narrower)

Example

.. container:: param

   .. container:: parameters2

      degamp : int = 3

   Polynomial degree for BPOLY amplitude solution Subparameter of
   bandtype='BPOLY' default: 3 Example: degamp=2

Example

.. container:: param

   .. container:: parameters2

      degphase : int = 3

   Polynomial degree for BPOLY phase solution Subparameter of
   bandtype='BPOLY' default: 3 Example: degphase=2

Example

.. container:: param

   .. container:: parameters2

      visnorm : bool = False

   Normalize data prior to BPOLY solution Subparameter of
   bandtype='BPOLY' default: False Example: visnorm=True

Example

.. container:: param

   .. container:: parameters2

      maskcenter : int = 0

   Number of channels to avoid in center of each band Subparameter of
   bandtype='BPOLY' default: 0 Example: maskcenter=5 (BPOLY only)

Example

.. container:: param

   .. container:: parameters2

      maskedge : int = 5

   Fraction of channels to avoid at each band edge (in %) Subparameter
   of bandtype='BPOLY' default: 5 Example: maskedge=3 (BPOLY only)

Example

.. container:: param

   .. container:: parameters2

      docallib : bool = False

   Control means of specifying the caltables default: False --> Use
   gaintable, gainfield, interp, spwmap, calwt. If True, specify a file
   containing cal library in callib

Example

.. container:: param

   .. container:: parameters2

      callib : string

   Cal Library filename Subparameter of callib=True If docallib=True,
   specify a file containing cal library directives

Example

.. container:: param

   .. container:: parameters2

      gaintable : stringArray

   Gain calibration table(s) to apply on the fly Subparameter of
   callib=False default: '' (none) Examples: gaintable='ngc5921.gcal'
   gaintable=['ngc5921.ampcal','ngc5921.phcal']

Example

.. container:: param

   .. container:: parameters2

      gainfield : stringArray

   Select a subset of calibrators from gaintable(s) Subparameter of
   callib=False default:'' --> all sources in table gaintable='nearest'
   --> nearest (on sky) available field in table. Otherwise, same syntax
   as field Examples: gainfield='0~2,5' means use fields 0,1,2,5 from
   gaintable gainfield=['0~3','4~6'] (for multiple gaintables)

Example

.. container:: param

   .. container:: parameters2

      interp : stringArray

   Interpolation parmameters (in time[,freq]) for each gaintable, as a
   list of strings. Default: '' --> 'linear,linear' for all gaintable(s)
   Options: Time: 'nearest', 'linear' Freq: 'nearest', 'linear',
   'cubic', 'spline' Specify a list of strings, aligned with the list of
   caltable specified in gaintable, that contain the required
   interpolation parameters for each caltable. \* When frequency
   interpolation is relevant (B, Df, Xf), separate time-dependent and
   freq-dependent interp types with a comma (freq_after\_ the comma). \*
   Specifications for frequency are ignored when the calibration table
   has no channel-dependence. \* Time-dependent interp options ending in
   'PD' enable a "phase delay" correction per spw for
   non-channel-dependent calibration types. \* For multi-obsId datasets,
   'perobs' can be appended to the time-dependent interpolation
   specification to enforce obsId boundaries when interpolating in time.
   \* Freq-dependent interp options can have 'flag' appended to enforce
   channel-dependent flagging, and/or 'rel' appended to invoke relative
   frequency interpolation Examples: interp='nearest' (in time, freq-dep
   will be linear, if relevant) interp='linear,cubic' (linear in time,
   cubic in freq) interp='linearperobs,splineflag' (linear in time per
   obsId, spline in freq with channelized flagging)
   interp='nearest,linearflagrel' (nearest in time, linear in freq with
   with channelized flagging and relative-frequency interpolation)
   interp=',spline' (spline in freq; linear in time by default)
   interp=['nearest,spline','linear'] (for multiple gaintables)

Example

.. container:: param

   .. container:: parameters2

      spwmap : intArray

   Spectral window mappings to form for gaintable(s) Only used if
   callib=False default: [] (apply solutions from each calibration spw
   to the same MS spw only) Any available calibration spw can be
   mechanically mapped to any MS spw. Examples: spwmap=[0,0,1,1] means
   apply calibration from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS
   spws 2,3. spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for
   multiple gaintables)

Example

.. container:: param

   .. container:: parameters2

      parang : bool = False

   Apply parallactic angle correction default: False If True, apply the
   parallactic angle correction (required for polarization calibration)

Example

.. container:: section
   :name: viewlet-below-content-body
