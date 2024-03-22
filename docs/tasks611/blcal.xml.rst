blcal -- Calculate a baseline-based calibration solution (gain or bandpass) -- calibration task
=======================================

Description
---------------------------------------

This task determines a baseline by baseline gain (time) or bandpass
(freq) for all baseline pairs in the data set. For the usual
antenna-based calibration of interferometric data, this task gaincal
is recommended, even with only one to three baselines.  For arrays
with closure errors, use blcal.



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
     - :code:`'scan'`
     - Data axes which to combine for solve (obs, scan, spw, and/or field)
   * - freqdep
     - :code:`False`
     - Solve for frequency dependent solutions
   * - calmode
     - :code:`'ap'`
     - Type of solution" (\'ap\', \'p\', \'a\')
   * - solnorm
     - :code:`False`
     - Normalize average solution amplitudes to 1.0
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

:code:`'scan'`

Data axes which to combine for solve
                     Default: 'scan' (solutions will break at obs,
                     field, and spw boundaries, but may extend over
                     multiple scans [per obs, field, and spw] up to
                     solint.)
                     Options: '','obs','scan','spw',field', or any
                     comma-separated combination in a single string

                        Example: combine='scan,spw' - Extend solutions
                        over scan boundaries (up to the solint), and
                        combine spws for solving



freqdep
---------------------------------------

:code:`False`

Solve for frequency dependent solutions
                     Default: False (gain; True=bandpass)
                     Options: False|True



calmode
---------------------------------------

:code:`'ap'`

Type of solution" ('ap', 'p', 'a')
                     Default: 'ap' (amp and phase)
                     Options: 'p' (phase) ,'a' (amplitude), 'ap'
                     (amplitude and phase)

                        Example: calmode='p'



solnorm
---------------------------------------

:code:`False`

Normalize average solution amplitudes to 1.0
                     Default: False (no normalization)

                     For freqdep=False, this is a global (per-spw)
                     normalization of amplitudes (only). For
                     freqdep=True, each baseline  solution spectrum is
                     separately normalized by its (complex) mean.



gaintable
---------------------------------------

:code:`numpy.array( [  ] )`

Gain calibration table(s) to apply on the fly
                     Default: '' (none)

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
                        gainfield='0~3'
                        gainfield=['0~3','4~6']



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
                     Default: False

                     If True, apply the parallactic angle correction
                     (required for polarization calibration)





