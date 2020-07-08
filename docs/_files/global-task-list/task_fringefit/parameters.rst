.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file

Example

.. container:: param

   .. container:: parameters2

      caltable : string

   Name of output gain calibration table

Example

.. container:: param

   .. container:: parameters2

      field : string

   Select field using field id(s) or field name(s)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Select spectral window/channels

Example

.. container:: param

   .. container:: parameters2

      intent : string

   Select observing intent

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Other data selection parameters

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Select data based on time range

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Select data based on antenna/baseline

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Scan number range

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Select by observation ID(s)

Example

.. container:: param

   .. container:: parameters2

      msselect : string

   Optional complex data selection (ignore for now)

Example

.. container:: param

   .. container:: parameters2

      solint : undefined = inf

   Solution interval: egs. \\'inf\', \\'60s\' (see help)

Example

.. container:: param

   .. container:: parameters2

      combine : string

   Data axes which to combine for solve (obs, scan, spw, and/or field)

Example

.. container:: param

   .. container:: parameters2

      refant : string

   Reference antenna name(s)

Example

.. container:: param

   .. container:: parameters2

      minsnr : double = 3.0

   Reject solutions below this signal-to-noise ratio (at the FFT stage)

Example

.. container:: param

   .. container:: parameters2

      zerorates : bool = False

   Zero delay-rates in solution table Write a solution table with
   delay-rates zeroed, for the case of "manual phase calibration", so
   that the calibration table can be applied to the full dataset without
   the extrapolation of a non-zero delay-rate term affecting the data

Example

.. container:: param

   .. container:: parameters2

      globalsolve : bool = True

   Refine estimates of delay and rate with global least-squares solver

Example

.. container:: param

   .. container:: parameters2

      niter : int = 100

   Maximum number of iterations for least-squares solver

Example

.. container:: param

   .. container:: parameters2

      delaywindow : doubleArray

   Constrain FFT delay search to a window specified as a two-element
   list with units of nanoseconds Default: [None, None] Examples: [-10,
   10]

Example

.. container:: param

   .. container:: parameters2

      ratewindow : doubleArray

   Constrain FFT rate search to a window specified as a two-element list
   with units of seconds per second Default: [None, None] Examples:
   [-1e-13, 1e-13]

Example

.. container:: param

   .. container:: parameters2

      append : bool = False

   Append solutions to the (existing) table Default: False (overwrite
   existing table or make new table) Appended solutions must be derived
   from the same MS as the existing caltable, and solution spws must
   have the same meta-info (according to spw selection and solint) or be
   non-overlapping.

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

      docallib : bool = False

   Control means of specifying the caltables Default: False (Use
   gaintable, gainfield, interp, spwmap, calwt) Options: False|True If
   True, specify a file containing cal library in callib

Example

.. container:: param

   .. container:: parameters2

      callib : string

   Specify a file containing cal library directives Subparameter of
   docallib=True

Example

.. container:: param

   .. container:: parameters2

      gaintable : stringArray

   Gain calibration table(s) to apply on the fly Default: '' (none)
   Subparameter of docallib=False Examples: gaintable='ngc5921.gcal'
   gaintable=['ngc5921.ampcal','ngc5921.phcal']

Example

.. container:: param

   .. container:: parameters2

      gainfield : stringArray

   Select a subset of calibrators from gaintable(s) Default: '' (all
   sources on the sky) 'nearest' ==> nearest (on sky) available field in
   table otherwise, same syntax as field Examples: gainfield='0~2,5'
   means use fields 0,1,2,5 from gaintable gainfield=['0~3','4~6'] means
   use field 0 through 3

Example

.. container:: param

   .. container:: parameters2

      interp : stringArray

   Interpolation parameters (in time[,freq]) for each gaintable, as a
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

      paramactive : boolArray

   Control which parameters are solved for; a vector of (exactly) three
   booleans for delay, delay-rate and dispersive delay (in that order)

Example

.. container:: param

   .. container:: parameters2

      parang : bool = False

   Apply parallactic angle correction on the fly.

Example

.. container:: section
   :name: viewlet-below-content-body
