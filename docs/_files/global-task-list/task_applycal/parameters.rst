.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task applycal parameters

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

            Name of input visibility file default: non Example:
            vis='ngc5921.ms'

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
   default: '' (all) If antenna string is a non-negative integer, it is
   assumed an antenna index, otherwise, it is assumed as an antenna name
   Examples: antenna='5&6'; baseline between antenna index 5 and index
   6. antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
   antenna='5&6;7&8'; baselines with indices 5-6 and 7-8 antenna='5';
   all baselines with antenna index 5 antenna='05'; all baselines with
   antenna number 05 (VLA old name) antenna='5,6,10'; all baselines with
   antennas 5,6,10 index numbers

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Scan number range Subparameter of selectdata=True default: '' = all

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
   callib=False default: '' (none) All gain table types: 'G', GSPLINE,
   'T', 'B', 'BPOLY', 'D's' can be applied. Examples:
   gaintable='ngc5921.gcal' gaintable=['ngc5921.ampcal','ngc5921.phcal']

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

   Spectral windows combinations to form for gaintables(s) Subparameter
   of callib=False default: [] (apply solutions from each spw to that
   spw only) Examples: spwmap=[0,0,1,1] means apply the caltable
   solutions from spw = 0 to the spw 0,1 and spw 1 to spw 2,3.
   spwmap=[[0,0,1,1],[0,1,0,1]] (for multiple gaintables)

Example

.. container:: param

   .. container:: parameters2

      calwt : boolArray = True

   Calibrate data weights per gaintable. default: True (for all
   specified gaintables) Examples: calwt=False (for all specified
   gaintables) calwt=[True,False,True] (specified per gaintable)

Example

.. container:: param

   .. container:: parameters2

      parang : bool = False

   Apply parallactic angle correction default: False If True, apply the
   parallactic angle correction. FOR ANY POLARIZATION CALIBRATION AND
   IMAGING, parang = True

Example

.. container:: param

   .. container:: parameters2

      applymode : string

   Calibration apply mode default: 'calflag' Options: "calflag",
   "calflagstrict", "trial", "flagonly", "flagonlystrict", "calonly" --
   applymode='calflag': calibrate data and apply flags from solutions --
   applymode='trial': report on flags from solutions, dataset entirely
   unchanged -- applymode='flagonly': apply flags from solutions only,
   data not calibrated -- applymode='calonly' calibrate data only, flags
   from solutions NOT applied (use with extreme caution!) --
   applymode='calflagstrict' or 'flagonlystrict' same as above except
   flag spws for which calibration is unavailable in one or more tables
   (instead of allowing them to pass uncalibrated and unflagged)

Allowed Value(s)

calflag calflagstrict trial flagonly flagonlystrict calonly

Example

.. container:: param

   .. container:: parameters2

      flagbackup : bool = True

   Automatically back up the state of flags before the run? default:
   True

Example

.. container:: section
   :name: viewlet-below-content-body
