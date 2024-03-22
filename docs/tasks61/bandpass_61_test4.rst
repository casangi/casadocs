bandpass -- Calculates a bandpass calibration solution -- calibration task
=======================================

Description
---------------------------------------

Determines the amplitude and phase as a function of frequency for each
spectral window containing more than one channel.  Strong sources (or
many observations of moderately strong sources) are needed to obtain
accurate bandpass functions.  The two solution choices are: Individual
antenna/based channel solutions 'B'; and a polynomial fit over the
channels 'BPOLY'.  The 'B' solutions can determined at any specified
time interval, and is recommended if each channel has good
signal-to-noise.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input visibility file
   * - caltable
     - :code:`''`
     - Name of output bandpass calibration table
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - intent
     - :code:`''`
     - Select observing intent
   * - selectdata
     - :code:`True`
     - Other data selection parameters
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - uvrange
     - :code:`''`
     - Select data within uvrange (default units meters)
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - scan
     - :code:`''`
     - Scan number range
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - msselect
     - :code:`''`
     - Optional complex data selection (ignore for now)
   * - solint
     - :code:`'inf'`
     - Solution interval in time[,freq]
   * - combine
     - :code:`'scan'`
     - Data axes which to combine for solve (obs, scan, spw, and/or field)
   * - refant
     - :code:`''`
     - Reference antenna name(s)
   * - minblperant
     - :code:`int(4)`
     - Minimum baselines _per antenna_ required for solve
   * - minsnr
     - :code:`float(3.0)`
     - Reject solutions below this SNR (only applies for bandtype = B)
   * - solnorm
     - :code:`False`
     - Normalize average solution amplitudes to 1.0
   * - bandtype
     - :code:`'B'`
     - Type of bandpass solution (B or BPOLY)
   * - smodel
     - :code:`numpy.array( [  ] )`
     - Point source Stokes parameters for source model.
   * - corrdepflags
     - :code:`False`
     - Respect correlation-dependent flags
   * - append
     - :code:`False`
     - Append solutions to the (existing) table
   * - fillgaps
     - :code:`int(0)`
     - Fill flagged solution channels by interpolation
   * - degamp
     - :code:`int(3)`
     - Polynomial degree for BPOLY amplitude solution
   * - degphase
     - :code:`int(3)`
     - Polynomial degree for BPOLY phase solution
   * - visnorm
     - :code:`False`
     - Normalize data prior to BPOLY solution
   * - maskcenter
     - :code:`int(0)`
     - Number of channels to avoid in center of each band
   * - maskedge
     - :code:`int(5)`
     - Fraction of channels to avoid at each band edge (in %)
   * - docallib
     - :code:`False`
     - Use callib or traditional cal apply parameters
   * - callib
     - :code:`''`
     - Cal Library filename
   * - gaintable
     - :code:`numpy.array( [  ] )`
     - Gain calibration table(s) to apply on the fly
   * - gainfield
     - :code:`numpy.array( [  ] )`
     - Select a subset of calibrators from gaintable(s)
   * - interp
     - :code:`numpy.array( [  ] )`
     - Interpolation parameters for each gaintable, as a list
   * - spwmap
     - :code:`[ ]`
     - Spectral window mappings to form for gaintable(s)
   * - parang
     - :code:`False`
     - Apply parallactic angle correction


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     default: non

                        Example: vis='ngc5921.ms'



caltable
---------------------------------------

:code:`''`

Name of output bandpass calibration table
                     default: none

                        Example: caltable='ngc5921.bcal'



field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     default: '' --> all fields
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative integer,
                     it is assumed a field index,  otherwise, it is
                     assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C



spw
---------------------------------------

:code:`''`

Select spectral window/channels

                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all
                        channels)
                        spw='<2';  spectral windows less than 2
                        (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61,
                        INCLUSIVE
                        spw='*:5~61'; all spw with channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3, channels 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw='0:0~10;15~60'; spectral window 0 with
                        channels 0-10,15-60. (NOTE ';' to separate
                        channel selections)
                        spw='0:0~10^2,1:20~30^5'; spw 0, channels
                        0,2,4,6,8,10, spw 1, channels 20,25,30 
                        type 'help par.selection' for more examples.



intent
---------------------------------------

:code:`''`

Select observing intent
                     default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)



selectdata
---------------------------------------

:code:`True`

Other data selection parameters
                     default: True 



timerange
---------------------------------------

:code:`''`

Select data based on time range
                     Subparameter of selectdata=True
                     default = '' (all)

                        Examples:
                        timerange =
                        'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                        (Note: if YYYY/MM/DD is missing date defaults
                        to first day in data set.)
                        timerange='09:14:0~09:54:0' picks 40 min on
                        first day 
                        timerange= '25:00:00~27:30:00' picks 1 hr to 3
                        hr 30min on NEXT day
                        timerange='09:44:00' pick data within one
                        integration of time
                        timerange='>10:24:00' data after this time



uvrange
---------------------------------------

:code:`''`

Select data within uvrange (default units meters)
                     Subparameter of selectdata=True
                     default: '' (all)

                        Examples:
                        uvrange='0~1000klambda'; uvrange from 0-1000
                        kilo-lambda
                        uvrange='>4klambda';uvranges greater than 4
                        kilolambda



antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     default: '' (all)

                         Examples: 
                         antenna='5&6'; baseline between antenna
                         index 5 and index 6.
                         antenna='VA05&VA06'; baseline between VLA
                         antenna 5 and 6.
                         antenna='5&6;7&8'; baselines with
                         indices 5-6 and 7-8
                         antenna='5'; all baselines with antenna index
                         5
                         antenna='05'; all baselines with antenna
                         number 05 (VLA old name)
                         antenna='5,6,10'; all baselines with antennas
                         5,6,10 index numbers

                     Note: just for antenna selection, an integer (or
                     integer list) is converted to a string and
                     matched against the antenna 'name' first. Only if
                     that fails, the integer is matched with the
                     antenna ID. The latter is the case for most
                     observatories, where the antenna name is not
                     strictly an integer.



scan
---------------------------------------

:code:`''`

Scan number range
                     Subparameter of selectdata=True
                     default: '' = all

                     Check 'go listobs' to insure the scan numbers are
                     in order.



observation
---------------------------------------

:code:`''`

Select by observation ID(s)
                     Subparameter of selectdata=True
                     default: '' = all

                         Example: observation='0~2,4'



msselect
---------------------------------------

:code:`''`

Optional complex data selection (ignore for now)


solint
---------------------------------------

:code:`'inf'`

Solution interval in time[,freq]
                     default: 'inf' (~infinite, up to boundaries
                     controlled by combine, with no pre-averaging in
                     frequency)
                     Options for time: 'inf' (~infinite), 'int' (per
                     integration), any float or integer value with or
                     without units
                     Options for freq: an integer with 'ch' suffix
                     will enforce pre-averaging by the specified
                     number of channels. A numeric value suffixed with
                     frequency units (e.g., 'Hz','kHz','MHz') will
                     enforce pre-averaging by an integral number of
                     channels amounting to no more than the specified
                     bandwidth.

                        Examples: solint='1min'; solint='60s',
                        solint=60 --> 1 minute
                        solint='0s'; solint=0; solint='int' --> per
                        integration
                        solint='-1s'; solint='inf' --> ~infinite, up
                        to boundaries enforced by combine 
                        solint='inf,8Mhz' --> ~infinite in time, with
                        8MHz pre-average in freq 
                        solint='int,32ch' --> per-integration in time,
                        with 32-channel pre-average in freq



combine
---------------------------------------

:code:`'scan'`

Data axes to combine for solving
                     default: 'scan' --> solutions will break at obs,
                     field, and spw boundaries but may extend over
                     multiple scans (per obs, field and spw) up to
                     solint.
                     Options: '','obs','scan','spw',field', or any
                     comma-separated combination in a single string.

                        Example: combine='scan,spw' --> extend
                        solutions over scan boundaries (up to the
                        solint), and combine spws for solving.



refant
---------------------------------------

:code:`''`

Reference antenna name(s); a prioritized list may be
specified
                     default: '' (no reference antenna)

                        Examples:
                        refant='13' (antenna with index 13) 
                        refant='VA04' (VLA antenna #4)
                        refant='EA02,EA23,EA13' (EVLA antenna EA02,
                        use EA23 and EA13 as alternates if/when EA02
                        drops out)
                     
                     Use 'go listobs' for antenna listing



minblperant
---------------------------------------

:code:`int(4)`

Minimum baselines _per antenna_ required for solve
                     default: 4

                     Antennas with fewer baselines are excluded from
                     solutions. Amplitude solutions with fewer than 4
                     baselines, and phase solutions with fewer than 3
                     baselines are only trivially constrained, and are
                     no better than baseline-based solutions.

                        example: minblperant=10 --> Antennas
                        participating on 10 or more baselines are
                        included in the solve.



minsnr
---------------------------------------

:code:`float(3.0)`

Reject solutions below this SNR (only applies for
bandtype = B)
                     default: 3.0



solnorm
---------------------------------------

:code:`False`

Normalize bandpass amplitudes and phase for each spw,
pol, ant, and timestamp
                     default: False (no normalization)



bandtype
---------------------------------------

:code:`'B'`

Type of bandpass solution (B or BPOLY)
                      default: 'B'

                      'B' does a channel by channel solution for each
                      specified spw. 
                      'BPOLY' is somewhat experimental. It will fit an
                      nth order polynomial for the amplitude and phase
                      as a function of frequency. Only one fit is made
                      for all specified spw, and edge channels should
                      be omitted.
                      Use taskname=plotcal in order to compare the
                      results from B and BPOLY.

                         Example: bandtype='BPOLY'



smodel
---------------------------------------

:code:`numpy.array( [  ] )`

Point source Stokes parameters for source model.


corrdepflags
---------------------------------------

:code:`False`

 If False (default), if any correlation is flagged, treat all correlations in
        the visibility vector as flagged when solving (per channel, per baseline).
        If True, use unflagged correlations in a visibility vector, even if one or more
        other correlations are flagged.
              
        Default: False (treat correlation vectors with one or more correlations flagged as entirely flagged)
  
        Traditionally, CASA has observed a strict interpretation of 
        correlation-dependent flags: if one or more correlations 
        (for any baseline and channel) is flagged, then all available 
        correlations for the same baseline and channel are 
        treated as flagged.  However, it is desirable in some 
        circumstances to relax this stricture, e.g., to preserve use
        of data from antennas with only one good polarization (e.g., one polarization
        is bad or entirely absent).  Solutions for the bad or missing polarization 
        will be rendered as flagged.

      


append
---------------------------------------

:code:`False`

Append solutions to the (existing) table
                     default: False (overwrite existing table or make
                     new table)

                     Append solutions to the (existing) table.
                     Appended solutions must be derived from the same
                     MS as the existing caltable, and solution spws
                     must have the same meta-info (according to spw
                     selection and solint) or be non-overlapping.



fillgaps
---------------------------------------

:code:`int(0)`

Fill flagged solution channels by interpolation
                     Subparameter of bandtype='B'  
                     default: 0 (don't interpolate)

                        Example: fillgaps=3 (interpolate gaps 3
                        channels wide and narrower)



degamp
---------------------------------------

:code:`int(3)`

Polynomial degree for BPOLY amplitude solution
                     Subparameter of bandtype='BPOLY'
                     default: 3

                        Example: degamp=2



degphase
---------------------------------------

:code:`int(3)`

Polynomial degree for BPOLY phase solution
                     Subparameter of bandtype='BPOLY'
                     default: 3

                        Example: degphase=2



visnorm
---------------------------------------

:code:`False`

Normalize data prior to BPOLY solution
                     Subparameter of bandtype='BPOLY'
                     default: False

                        Example: visnorm=True



maskcenter
---------------------------------------

:code:`int(0)`

Number of channels to avoid in center of each band
                     Subparameter of bandtype='BPOLY'
                     default: 0

                        Example: maskcenter=5 (BPOLY only)



maskedge
---------------------------------------

:code:`int(5)`

Fraction of channels to avoid at each band edge (in %)
                     Subparameter of bandtype='BPOLY'
                     default: 5

                        Example: maskedge=3 (BPOLY only)



docallib
---------------------------------------

:code:`False`

Control means of specifying the caltables
                     default: False --> Use gaintable, gainfield,
                     interp, spwmap, calwt. 

                     If True, specify a file containing cal library in
                     callib



callib
---------------------------------------

:code:`''`

Cal Library filename
                     Subparameter of callib=True

                     If docallib=True, specify a file containing cal
                     library directives



gaintable
---------------------------------------

:code:`numpy.array( [  ] )`

Gain calibration table(s) to apply on the fly
                     Subparameter of callib=False
                     default: '' (none)

                        Examples: gaintable='ngc5921.gcal'
                        gaintable=['ngc5921.ampcal','ngc5921.phcal']



gainfield
---------------------------------------

:code:`numpy.array( [  ] )`

Select a subset of calibrators from gaintable(s)
                     Subparameter of callib=False
                     default:'' --> all sources in table
                     
                     gaintable='nearest' --> nearest (on sky)
                     available field in table. Otherwise, same syntax
                     as field

                        Examples: 
                        gainfield='0~2,5' means use fields 0,1,2,5
                        from gaintable
                        gainfield=['0~3','4~6'] (for multiple
                        gaintables)



interp
---------------------------------------

:code:`numpy.array( [  ] )`

Interpolation parmameters (in time[,freq]) for each gaintable, as a list of strings.
                     Default: '' --> 'linear,linear' for all gaintable(s)
                     Options: Time: 'nearest', 'linear'
                              Freq: 'nearest', 'linear', 'cubic',
                              'spline'
                   Specify a list of strings, aligned with the list of caltable specified
                   in gaintable, that contain the required interpolation parameters
                   for each caltable.
                   * When frequency interpolation is relevant (B, Df,
                     Xf), separate time-dependent and freq-dependent
                     interp types with a comma (freq_after_ the
                     comma). 
                   * Specifications for frequency are ignored when the
                     calibration table has no channel-dependence. 
                   * Time-dependent interp options ending in 'PD'
                     enable a "phase delay" correction per spw for
                     non-channel-dependent calibration types.
                   * For multi-obsId datasets, 'perobs' can be
                     appended to the time-dependent interpolation
                     specification to enforce obsId boundaries when
                     interpolating in time. 
                   * Freq-dependent interp options can have 'flag' appended
                     to enforce channel-dependent flagging, and/or 'rel' 
                     appended to invoke relative frequency interpolation

                        Examples: 
                        interp='nearest' (in time, freq-dep will be
                        linear, if relevant)
                        interp='linear,cubic'  (linear in time, cubic
                        in freq)
                        interp='linearperobs,splineflag' (linear in
                        time per obsId, spline in freq with
                        channelized flagging)
                        interp='nearest,linearflagrel' (nearest in
                        time, linear in freq with with channelized 
                        flagging and relative-frequency interpolation)
                        interp=',spline'  (spline in freq; linear in
                        time by default)
                        interp=['nearest,spline','linear']  (for
                        multiple gaintables)



spwmap
---------------------------------------

:code:`[ ]`

Spectral window mappings to form for gaintable(s)
                     Only used if callib=False
                     default: [] (apply solutions from each calibration spw to
                     the same MS spw only)
                     Any available calibration spw can be mechanically mapped to any 
                      MS spw. 
                     Examples:
                        spwmap=[0,0,1,1] means apply calibration 
                          from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
                          gaintables)



parang
---------------------------------------

:code:`False`

Apply parallactic angle correction
                     default: False

                     If True, apply the parallactic angle correction
                     (required for polarization calibration)






