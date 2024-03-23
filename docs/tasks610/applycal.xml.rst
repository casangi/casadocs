applycal -- Apply calibrations solutions(s) to data -- calibration task
=======================================

Description
---------------------------------------

Applycal reads the specified gain calibration tables or cal library,
applies them to the (raw) data column (with the specified selection),
and writes the calibrated results into the corrected column. This is
done in one step, so all available calibration tables must be
specified.

Applycal will overwrite existing corrected data, and will flag data
for which there is no calibration available.

Standard data selection is supported.  See help par.selectdata for
more information.



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
     - Spectral windows combinations to form for gaintables(s)
   * - calwt
     - :code:`numpy.array( [  ] )`
     - Calibrate data weights per gaintable.
   * - parang
     - :code:`False`
     - Apply parallactic angle correction
   * - applymode
     - :code:`''`
     - Calibration mode: ""="calflag","calflagstrict","trial","flagonly","flagonlystrict", or "calonly"
   * - flagbackup
     - :code:`True`
     - Automatically back up the state of flags before the run?


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     default: non

                        Example: vis='ngc5921.ms'



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
                     default: '' = all



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

                     All gain table types: 'G', GSPLINE, 'T', 'B',
                     'BPOLY', 'D's' can be applied.

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



calwt
---------------------------------------

:code:`numpy.array( [  ] )`

Calibrate data weights per gaintable.
                     default: True (for all specified gaintables)
 
                        Examples:
                        calwt=False (for all specified gaintables)
                        calwt=[True,False,True] (specified per
                        gaintable)



parang
---------------------------------------

:code:`False`

Apply parallactic angle correction
                     default: False

                     If True, apply the parallactic angle
                     correction. FOR ANY POLARIZATION CALIBRATION AND
                     IMAGING, parang = True



applymode
---------------------------------------

:code:`''`

Calibration apply mode
                     default: 'calflag' 
                     Options: "calflag", "calflagstrict", "trial",
                     "flagonly", "flagonlystrict", "calonly"

                     -- applymode='calflag': calibrate data and apply
                     flags from solutions
                     -- applymode='trial': report on flags from
                     solutions, dataset entirely unchanged
                     -- applymode='flagonly': apply flags from
                     solutions only, data not calibrated
                     -- applymode='calonly' calibrate data only, flags
                     from solutions NOT applied (use with extreme
                     caution!)
                     -- applymode='calflagstrict' or 'flagonlystrict'
                     same as above except flag spws for which
                     calibration is unavailable in one or more tables
                     (instead of allowing them to pass uncalibrated
                     and unflagged)



flagbackup
---------------------------------------

:code:`True`

Automatically back up the state of flags before the run?
                     default: True





