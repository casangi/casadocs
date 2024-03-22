fringefit -- Fringe fit delay and rates -- calibration task
=======================================

Description
---------------------------------------

Phase offsets, groups delays and delay rates are calculated with
respect to a specified referance antenna by a two-dimensional FFT and
subsequent least-squares optimisation.

Previous calibrations should be applied on the fly.




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
     - Name of output gain calibration table
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
     - Solution interval: egs. \'inf\', \'60s\' (see help)
   * - combine
     - :code:`''`
     - Data axes which to combine for solve (obs, scan, spw, and/or field)
   * - refant
     - :code:`''`
     - Reference antenna name(s)
   * - minsnr
     - :code:`float(3.0)`
     - Reject solutions below this signal-to-noise ratio (at the FFT stage)
   * - zerorates
     - :code:`False`
     - Zero delay-rates in solution table
   * - globalsolve
     - :code:`True`
     - Refine estimates of delay and rate with global least-squares solver
   * - niter
     - :code:`int(100)`
     - Maximum number of iterations for least-squares solver
   * - delaywindow
     - :code:`numpy.array( [  ] )`
     - Constrain FFT delay search to a window
   * - ratewindow
     - :code:`numpy.array( [  ] )`
     - Constrain FFT rate search to a window
   * - append
     - :code:`False`
     - Append solutions to the (existing) table
   * - corrdepflags
     - :code:`False`
     - Respect correlation-dependent flags
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
     - Temporal interpolation for each gaintable (''=linear)
   * - spwmap
     - :code:`[ ]`
     - Spectral window mappings to form for gaintable(s)
   * - paramactive
     - :code:`numpy.array( [  ] )`
     - Control which parameters are solved for
   * - parang
     - :code:`False`
     - Apply parallactic angle correction on the fly


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


caltable
---------------------------------------

:code:`''`

Name of output gain calibration table


field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


intent
---------------------------------------

:code:`''`

Select observing intent


selectdata
---------------------------------------

:code:`True`

Other data selection parameters


timerange
---------------------------------------

:code:`''`

Select data based on time range


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


scan
---------------------------------------

:code:`''`

Scan number range


observation
---------------------------------------

:code:`''`

Select by observation ID(s)


msselect
---------------------------------------

:code:`''`

Optional complex data selection (ignore for now)


solint
---------------------------------------

:code:`'inf'`

Solution interval: egs. \'inf\', \'60s\' (see help)


combine
---------------------------------------

:code:`''`

Data axes which to combine for solve (obs, scan, spw, and/or field)


refant
---------------------------------------

:code:`''`

Reference antenna name(s)


minsnr
---------------------------------------

:code:`float(3.0)`

Reject solutions below this signal-to-noise ratio (at the FFT stage)


zerorates
---------------------------------------

:code:`False`

Zero delay-rates in solution table

        Write a solution table with delay-rates zeroed, for the case of
    "manual phase calibration", so that the calibration table can be
    applied to the full dataset without the extrapolation of a non-zero delay-rate term
    affecting the data
    


globalsolve
---------------------------------------

:code:`True`

Refine estimates of delay and rate with global least-squares solver


niter
---------------------------------------

:code:`int(100)`

Maximum number of iterations for least-squares solver


delaywindow
---------------------------------------

:code:`numpy.array( [  ] )`

Constrain FFT delay search to a window specified as a two-element list with units of nanoseconds
    Default: [None, None]
    Examples: [-10, 10]
    


ratewindow
---------------------------------------

:code:`numpy.array( [  ] )`

Constrain FFT rate search to a window specified as a two-element list with units of seconds per second
      Default: [None, None]
      Examples: [-1e-13, 1e-13]
    


append
---------------------------------------

:code:`False`

Append solutions to the (existing) table
    Default: False (overwrite existing table or make
    new table)

    Appended solutions must be derived from the same
    MS as the existing caltable, and solution spws
    must have the same meta-info (according to spw
    selection and solint) or be non-overlapping.
    


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

      


docallib
---------------------------------------

:code:`False`

Control means of specifying the caltables
                     Default: False (Use gaintable, gainfield, interp,
                     spwmap, calwt)
                     Options: False|True

                     If True, specify a file containing cal library in
                     callib
    


callib
---------------------------------------

:code:`''`

Specify a file containing cal library directives
    Subparameter of docallib=True
    


gaintable
---------------------------------------

:code:`numpy.array( [  ] )`

Gain calibration table(s) to apply on the fly
    Default: '' (none)
    Subparameter of docallib=False
    Examples: 
    gaintable='ngc5921.gcal'
    gaintable=['ngc5921.ampcal','ngc5921.phcal']
    


gainfield
---------------------------------------

:code:`numpy.array( [  ] )`

Select a subset of calibrators from gaintable(s)
    Default: '' (all sources on the sky)

    'nearest' ==> nearest (on sky) available field in
    table otherwise, same syntax as field

    Examples: 
    gainfield='0~2,5' means use fields 0,1,2,5
    from gaintable
    gainfield=['0~3','4~6'] means use field 0
    through 3
    


interp
---------------------------------------

:code:`numpy.array( [  ] )`

Interpolation parameters (in time[,freq]) for each gaintable, as a list of strings.
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
	  


paramactive
---------------------------------------

:code:`numpy.array( [  ] )`

Control which parameters are solved for; a vector of (exactly) three booleans for delay, delay-rate and dispersive delay (in that order)


parang
---------------------------------------

:code:`False`

Apply parallactic angle correction on the fly.
            




