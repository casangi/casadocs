oldsplit -- Create a visibility subset from an existing visibility set -- manipulation task
=======================================

Description
---------------------------------------


    T H I S   T A S K   I S    D E P R E C A T E D
    I T   W I L L   B E   R E M O V E D   S O O N

Oldsplit is the general purpose program to make a new data set that is a
subset or averaged form of an existing data set. Oldsplit is often used after the initial calibration of the data to make a
smaller measurement set with only the data that will be used in
further flagging, imaging and/or self-calibration. Oldsplit includes
general selection parameters and can average over frequency (channels) and time (integrations).




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
     - Name of input measurement set
   * - outputvis
     - :code:`''`
     - Name of output measurement set
   * - datacolumn
     - :code:`'corrected'`
     - Data column(s) to Oldsplit out
   * - field
     - :code:`''`
     - Select field using ID(s) or name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - width
     - :code:`int(1)`
     - Number of channels to average to form one output channel
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - timebin
     - :code:`'0s'`
     - Interval for time averaging
   * - timerange
     - :code:`''`
     - Select data by time range
   * - array
     - :code:`''`
     - Select (sub)array(s) by array ID number
   * - uvrange
     - :code:`''`
     - Select data by baseline length (default units meters)
   * - scan
     - :code:`''`
     - Select data by scan numbers
   * - intent
     - :code:`''`
     - Select data by scan intents
   * - correlation
     - :code:`''`
     - Select correlations
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - combine
     - :code:`''`
     - Let time bins span changes in scan and/or stat
   * - keepflags
     - :code:`True`
     - If practical, keep *completely flagged rows* instead of dropping them.
   * - keepmms
     - :code:`False`
     - If the input is a multi-MS, make the output one,too.


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input MeasurementSet
               Default: none;
                 Example: vis='ngc5921.ms'



outputvis
---------------------------------------

:code:`''`

Name of output measurement set
               Default: none;
                 Example: outputvis='ngc5921_src.ms'



datacolumn
---------------------------------------

:code:`'corrected'`

Data column(s) to Oldsplit out
                Default='corrected';
                Options: 'data', 'model', 'corrected', 'all',
                'float_data', 'lag_data', 'float_data,data', and
                'lag_data,data'.
                  Example: datacolumn='data'

                  Note: 'all' = whichever of the above that are
                  present. Otherwise the selected column will go to
                  DATA (or FLOAT_DATA) in the output. Splitting with
                  the default datacolumn='corrected' before clean is
                  normally required for self-calibration!



field
---------------------------------------

:code:`''`

Select field using ID(s) or name(s)
                (Run listobs to obtain list of field IDs and names)
                Default: ''=all fields.
                If field string is a non-negative integer, it is
                assumed to be a field index otherwise, it is assumed
                to be a field name.

                  Examples:
                  field='0~2'; field ids 0,1,2
                  field='0,4,5~7'; field ids 0,4,5,6,7
                  field='3C286,3C295'; fields named 3C286 and 3C295
                  field = '3,4C*'; field id 3, all names starting with
                  4C



spw
---------------------------------------

:code:`''`

Select spectral window/channels
                Default: ''=all spectral windows and channels

                  Examples:
                  spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                  spw='<2';  spectral windows less than 2 (i.e. 0,1)
                  spw='0:5~61'; spw 0, channels 5 to 61
                  spw='0,10,3:3~45'; spw 0,10 all channels, spw 3 - chans 3 to 45.
                  spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                  spw = '*:3~64'  channels 3 through 64 for all sp id's
                  spw = ' :3~64' will NOT work.

                    Note: Oldsplit does not support multiple channel
                    ranges per spectral window (';') because it is not
                    clear whether to keep the ranges in the original
                    spectral window or make a new spectral window for
                    each additional range.



width
---------------------------------------

:code:`int(1)`

Number of channels to average to form one output channel
               Default: '1' => no channel averaging
                 Example: width=[2,3] => average 2 channels of 1s
                 spectral window selected and 3 in the second one.



antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline
               Default: '' (all)
               Non-negative integers are assumed to be antenna
               indices, and anything else is taken as an antenna name.

                 Examples:
                 antenna='5&6': baseline between antenna index 5 and index 6.
                 antenna='VA05&VA06': baseline between VLA antenna 5 and 6.
                 antenna='5&6;7&8': baselines 5-6 and 7-8
                 antenna='5': all baselines with antenna 5
                 antenna='5,6,10': all baselines including antennas 5, 6, or 10
                 antenna='5,6,10&': all baselines
                 with *only* antennas 5, 6, or 10.
                 (cross-correlations only.  Use
                 && to include
                 autocorrelations, and &&&
                 to get only autocorrelations.)
                 antenna='!ea03,ea12,ea17': all
                 baselines except those that include EVLA antennas
                 ea03, ea12, or ea17.



timebin
---------------------------------------

:code:`'0s'`

Interval for time averaging
               Default: '0s' or '-1s' (no averaging)
                 Example: timebin='30s'
                 '10' means '10s'



timerange
---------------------------------------

:code:`''`

Select data by time range
               timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
               Note: if YYYY/MM/DD is missing date, timerange defaults
               to the first day in the dataset.

               Default = '' (all); examples,

                 Examples:
                 timerange='09:14:0~09:54:0' picks 40 min on first day
                 timerange='25:00:00~27:30:00' picks 1
                 hr to 3 hr 30min on next day
                 timerange='09:44:00' data within one integration of time
                 timerange='>10:24:00' data after this time



array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number
               Default: ''=all



uvrange
---------------------------------------

:code:`''`

Select data by baseline length (default units meters)
               Default: ''=all

                  Examples:
                  uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                  uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                  uvrange='0~1000km'; uvrange in kilometers



scan
---------------------------------------

:code:`''`

Select data by scan numbers
               Default: ''=all



intent
---------------------------------------

:code:`''`

Select data by scan intents
               Default: '' = all

                 Examples:
                 intent = 'CALIBRATE_ATMOSPHERE_REFERENCE'
                 intent = 'calibrate_atmosphere_reference'.upper() # same as above
                 # Select states that include one or
                 both of CALIBRATE_WVR.REFERENCE or OBSERVE_TARGET_ON_SOURCE.
                 intent = 'CALIBRATE_WVR.REFERENCE, OBSERVE_TARGET_ON_SOURCE'



correlation
---------------------------------------

:code:`''`

Select correlations
               Default: '' = all

                 Examples:
                 correlation = 'rr, ll'
                 correlation = ['XY', 'YX'].



observation
---------------------------------------

:code:`''`

Select by observation ID(s)
               Default: '' = all



combine
---------------------------------------

:code:`''`

Let time bins span changes in scan and/or state
               Default = '' (separate time bins by both of the above)

                  Examples:
                  combine = 'scan': Can be useful when the scan number
                  goes up with each integration, as in many WSRT MSs.
                  combine = ['scan', 'state']: disregard
                  scan and state numbers when time averaging.
                  combine = 'state,scan': Same as above.



keepflags
---------------------------------------

:code:`True`

If practical, keep *completely flagged rows* instead of
dropping them.
               This has absolutely no effect on averaging
               calculations, or partially flagged rows.  All of the
               channels and correlations of a row must be flagged for
               it to be droppable, and a row must be well defined to
               be keepable.  The latter condition means that this
               option has no effect on time averaging - in that case
               fully flagged rows are automatically
               omitted. Regardless of this parameter, flagged data is
               never included in averaging calculations.

               The only time keepflags matters is if
               1. the input MS has some completely flagged rows
               and
               2. time averaging is not being done.

               Then, if keepflags is False, the completely flagged
               rows will be omitted from the output MS.  Otherwise,
               they will be included (subject to the selection
               parameters).



keepmms
---------------------------------------

:code:`False`

If the input is a multi-MS, make the output one,
too. (experimental)
               Default: False => the output will be a normal MS
               without partitioning.





