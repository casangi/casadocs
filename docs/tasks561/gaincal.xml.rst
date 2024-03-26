gaincal -- Determine temporal gains from calibrator observations -- calibration task
=======================================

Description
---------------------------------------

The complex gains for each antenna/spwid are determined from the data
column (raw data) divided by the model column. The gains can be
obtained for a specified solution interval, spw combination and field
combination. The GSPLINE spline (smooth) option is still under
development.

Previous calibrations (egs, bandpass, opacity, parallactic angle) can
be applied on the fly. At present with dual-polarized data, both
polarizations must be unflagged for any solution to be obtained.



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
   * - uvrange
     - :code:`''`
     - Select data by baseline length.
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
     - Solution interval
   * - combine
     - :code:`''`
     - Data axes which to combine for solve (obs, scan, spw, and/or field)
   * - preavg
     - :code:`float(-1.0)`
     - Pre-averaging interval (sec) (rarely needed)
   * - refant
     - :code:`''`
     - Reference antenna name(s)
   * - refantmode
     - :code:`'flex'`
     - Reference antenna mode
   * - minblperant
     - :code:`int(4)`
     - Minimum baselines _per antenna_ required for solve
   * - minsnr
     - :code:`float(3.0)`
     - Reject solutions below this SNR
   * - solnorm
     - :code:`False`
     - Normalize (squared) solution amplitudes (G, T only)
   * - normtype
     - :code:`'mean'`
     - Solution normalization calculation type: mean or median
   * - gaintype
     - :code:`'G'`
     - Type of gain solution (G,T,GSPLINE,K,KCROSS)
   * - smodel
     - :code:`numpy.array( [  ] )`
     - Point source Stokes parameters for source model.
   * - calmode
     - :code:`'ap'`
     - Type of solution" (\'ap\', \'p\', \'a\')
   * - solmode
     - :code:`''`
     - Robust solving mode: (\'\', \'L1\', \'R\',\'L1R\')
   * - rmsthresh
     - :code:`numpy.array( [  ] )`
     - RMS Threshold sequence (for solmode=\'R\' or \'L1R\'; see help)
   * - append
     - :code:`False`
     - Append solutions to the (existing) table
   * - splinetime
     - :code:`float(3600.0)`
     - Spline timescale(sec); All spw\'s are first averaged.
   * - npointaver
     - :code:`int(3)`
     - The phase-unwrapping algorithm
   * - phasewrap
     - :code:`float(180.0)`
     - Wrap the phase for jumps greater than this value (degrees)
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
     - :code:`numpy.array( [  ] )`
     - Spectral windows combinations to form for gaintables(s)
   * - parang
     - :code:`False`
     - Apply parallactic angle correction


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



caltable
---------------------------------------

:code:`''`

Name of output gain calibration table
                     Default: none

                        Example: caltable='ngc5921.gcal'



field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
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
                     Default: '' (all spectral windows and channels)

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



intent
---------------------------------------

:code:`''`

Select observing intent
                     Default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)



selectdata
---------------------------------------

:code:`True`

Other data selection parameters
                     Default: True
                     Options: True|False



timerange
---------------------------------------

:code:`''`

Select data based on time range
                     Subparameter of selectdata=True
                     Default = '' (all)

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

Select data by baseline length.
                     Default = '' (all)

                        Examples:
                        uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                        uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                        uvrange='0~1000km'; uvrange in kilometers



antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     Default: '' (all)

                     If antenna string is a non-negative integer, it
                     is assumed an antenna index, otherwise, it is
                     assumed as an antenna name
  
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



scan
---------------------------------------

:code:`''`

Scan number range
                     Subparameter of selectdata=True
                     Default: '' = all

                     Check 'go listobs' to insure the scan numbers are
                     in order.



observation
---------------------------------------

:code:`''`

Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'



msselect
---------------------------------------

:code:`''`

Optional complex data selection (ignore for now)


solint
---------------------------------------

:code:`'inf'`

Solution interval
                     Default: 'inf' (infinite, up to boundaries
                     controlled by combine); 
                     Options: 'inf' (~infinite), 'int' (per
                     integration), any float or integer value with or
                     without units

                        Examples: 
                        solint='1min'; solint='60s', solint=60 (i.e.,
                        1 minute); solint='0s'; solint=0; solint='int'
                        (i.e., per integration); solint-'-1s';
                        solint='inf' (i.e., ~infinite, up to
                        boundaries enforced by combine)



combine
---------------------------------------

:code:`''`

Data axes which to combine for solve
                     Default: 'scan' (solutions will break at obs,
                     field, and spw boundaries)
                     Options: '','obs','scan','spw',field', or any
                     comma-separated combination in a single string

                        Example: combine='scan,spw' - Extend solutions
                        over scan boundaries (up to the solint), and
                        combine spws for solving



preavg
---------------------------------------

:code:`float(-1.0)`

Pre-averaging interval (sec)
                     Default: -1.0 (none)

                     Rarely needed.  Will average data over periods
                     shorter than the solution interval first.



refant
---------------------------------------

:code:`''`

Reference antenna name(s); a prioritized list may be
specified
                     Default: '' (No refant applied)

                        Examples: 
                        refant='4' (antenna with index 4)
                        refant='VA04' (VLA antenna #4)
                        refant='EA02,EA23,EA13' (EVLA antenna EA02,
                        use EA23 and EA13 as alternates if/when EA02
                        drops out)

                     Use taskname=listobs for antenna listing



refantmode
---------------------------------------

:code:`'flex'`

Reference antenna mode



minblperant
---------------------------------------

:code:`int(4)`

Minimum number of baselines required per antenna for each
solve
                     Default: 4

                     Antennas with fewer baselines are excluded from
                     solutions.

                        Example: minblperant=10 --> Antennas
                        participating on 10 or more baselines are
                        included in the solve

                     minblperant = 1 will solve for all baseline
                     pairs, even if only one is present in the data
                     set.  Unless closure errors are expected, use
                     taskname=gaincal rather than taskname=blcal to
                     obtain more options in data analysis.



minsnr
---------------------------------------

:code:`float(3.0)`

Reject solutions below this SNR
                     Default: 3.0



solnorm
---------------------------------------

:code:`False`

Normalize (squared) solution amplitudes (G, T only)
                     Default: False (no normalization)



normtype
---------------------------------------

:code:`'mean'`

Solution normalization calculation type: mean or median
                     Default: 'mean'



gaintype
---------------------------------------

:code:`'G'`

Type of gain solution (G,T,GSPLINE,K,KCROSS)
                     Default: 'G'

                        Example: gaintype='GSPLINE'

                   * 'G' means determine gains for each polarization and sp_wid
                   * 'T' obtains one solution for both polarizations;
                     Hence. their phase offset must be first removed
                     using a prior G.
                   * 'GSPLINE' makes a spline fit to the calibrator
                     data. It is useful for noisy data and fits a
                     smooth curve through the calibrated amplitude and
                     phase. However, at present GSPLINE is somewhat
                     experimental. Use with caution and check
                     solutions.
                   * 'K' solves for simple antenna-based delays via
                     FFTs of the spectra on baselines to the reference
                     antenna.  (This is not global fringe-fitting.)
                     If combine includes 'spw', multi-band delays are
                     determined; otherwise, per-spw single-band delays
                     will be determined.
                   * 'KCROSS' solves for a global cross-hand delay.
                     Use parang=T and apply prior gain and bandpass
                     solutions.  Multi-band delay solves
                     (combine='spw') not yet supported for KCROSS.



smodel
---------------------------------------

:code:`numpy.array( [  ] )`

Point source Stokes parameters for source model
(experimental).
                     Default: [] (use MODEL_DATA column)

                        Example: [1,0,0,0] (I=1, unpolarized)



calmode
---------------------------------------

:code:`'ap'`

Type of solution" ('ap', 'p', 'a')
                     Default: 'ap' (amp and phase)
                     Options: 'p' (phase) ,'a' (amplitude), 'ap'
                     (amplitude and phase)

                        Example: calmode='p'



solmode
---------------------------------------

:code:`''`

Robust solving mode: 
                     Options: '', 'L1', 'R', 'L1R'



rmsthresh
---------------------------------------

:code:`numpy.array( [  ] )`

RMS Threshold sequence
                     Subparameter of solmode='R' or 'L1R'

                     See CASA Docs for more information
                     (https://casa.nrao.edu/casadocs/)



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



splinetime
---------------------------------------

:code:`float(3600.0)`

Spline timescale(sec); All spw\'s are first averaged.
                     Subparameter of gaintype='GSPLINE'
                     Default: 3600 (1 hour)

                        Example: splinetime=1000

                     Typical splinetime should cover about 3 to 5
                     calibrator scans.



npointaver
---------------------------------------

:code:`int(3)`

Tune phase-unwrapping algorithm
                     Subparameter of gaintype='GSPLINE'
                     Default: 3; Keep at this value



phasewrap
---------------------------------------

:code:`float(180.0)`

Wrap the phase for jumps greater than this value
(degrees)
                     Subparameter of gaintype='GSPLINE'
                     Default: 180; Keep at this value



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

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintables(s)
                     Subparameter of callib=False
                     default: [] (apply solutions from each spw to
                     that spw only)

                        Examples:
                        spwmap=[0,0,1,1] means apply the caltable
                        solutions from spw = 0 to the spw 0,1 and spw
                        1 to spw 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]] (for multiple
                        gaintables)



parang
---------------------------------------

:code:`False`

Apply parallactic angle correction
                     Default: False

                     If True, apply the parallactic angle correction
                     (required for polarization calibration)





