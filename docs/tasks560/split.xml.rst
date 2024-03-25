split -- Create a visibility subset from an existing visibility set -- manipulation task
=======================================

Description
---------------------------------------

Split is the general purpose program to make a new data set that is a
subset or averaged form of an existing data set. General selection
parameters are included, and one or all of the various data columns
(DATA, LAG_DATA and/or FLOAT_DATA, MODEL_DATA and/or CORRECTED_DATA)
can be selected.

Split is often used after the initial calibration of the data to make
a smaller Measurement Set with only the data that will be used in
further flagging, imaging and/or self-calibration. Split can average
over frequency (channels) and time (integrations).

The split task uses the MSTransform framework underneath. Split also
supports the Multi-MS (MMS) format as input.



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
   * - outputvis
     - :code:`''`
     - Name of output visibility file
   * - keepmms
     - :code:`True`
     - If the input is a Multi-MS the output will also be a Multi-MS.
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - scan
     - :code:`''`
     - Scan number range
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - correlation
     - :code:`''`
     - Select data based on correlation
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - intent
     - :code:`''`
     - Select observing intent
   * - array
     - :code:`''`
     - Select (sub)array(s) by array ID number.
   * - uvrange
     - :code:`''`
     - Select data by baseline length.
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - feed
     - :code:`''`
     - Multi-feed numbers: Not yet implemented.
   * - datacolumn
     - :code:`'corrected'`
     - Which data column(s) to process.
   * - keepflags
     - :code:`True`
     - 
   * - width
     - :code:`int(1)`
     - Number of channels to average to form one output channel
   * - timebin
     - :code:`'0s'`
     - Bin width for time averaging
   * - combine
     - :code:`''`
     - Span the timebin across scan, state or both


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



outputvis
---------------------------------------

:code:`''`

Name of output visibility file
                     Default: '' (same as vis)

                        Example: outputvis='ngc5921_out.ms'

                     IMPORTANT: if a .flagversions file with the name
                     of the output MS exist, this task will exit with
                     an error. The user needs to rename or remove the
                     existing flagbackup or choose a different output
                     name for the MS.



keepmms
---------------------------------------

:code:`True`

Create a Multi-MS as the output if the input is a
Multi-MS.
                     Default: True
                     Options: True|False

                     By default it will create a Multi-MS when the
                     input is a Multi-MS. The output Multi-MS will
                     have the same partition axis of the input
                     MMS. See CASA Docs for more information on
                     the MMS format.

                     NOTE: It is not possible to do time average with
                     combine='scan' if the input MMS was partitioned
                     with separationaxis='scan' or 'auto'. In this
                     case, the task will abort with an error.



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
                     Default: ''=all spectral windows and channels
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.

                     NOTE: mstransform does not support multiple
                     channel ranges per spectral window (';').



scan
---------------------------------------

:code:`''`

Scan number range
                     Subparameter of selectdata=True
                     Default: '' = all



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



correlation
---------------------------------------

:code:`''`

Select data based on correlation
                     Default: '' ==> all

                        Example: correlation="XX,YY".



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



intent
---------------------------------------

:code:`''`

Select observing intent
                     Default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)



array
---------------------------------------

:code:`''`

(Sub)array number range
                     Default: '' (all)



uvrange
---------------------------------------

:code:`''`

Select data by baseline length.
                     Default = '' (all)

                        Examples:
                        uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                        uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                        uvrange='0~1000km'; uvrange in kilometers



observation
---------------------------------------

:code:`''`

Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'



feed
---------------------------------------

:code:`''`

Selection based on the feed 
                     NOT IMPLEMENTED YET!
                     Default: '' = all



datacolumn
---------------------------------------

:code:`'corrected'`

Which data column(s) to use for processing
                     (case-insensitive).
                     Default: 'corrected'
                     Options: 'data', 'model', 'corrected',
                     'all','float_data', 'lag_data',
                     'float_data,data', 'lag_data,data'

                        Example: datacolumn='data'
    
                     NOTE: 'all' = whichever of the above that are
                     present. If the requested column does not exist,
                     the task will exit with an error.



keepflags
---------------------------------------

:code:`True`

Keep *completely flagged rows* instead of dropping them.
                     Default: True (keep completely flagged rows in
                     the output)
                     Options: True|False

                     Keepflags has no effect on partially flagged
                     rows. All of the channels and correlations of a
                     row must be flagged for it to be droppable, and a
                     row must be well defined to be keepable.

                     IMPORTANT: Regardless of this parameter, flagged
                     data is never included in channel averaging. On
                     the other hand, partially flagged rows will
                     always be included in time averaging. The average
                     value of the flagged data for averages containing
                     ONLY flagged data in the relevant output channel
                     will be written to the output with the
                     corresponding flag set to True, while only
                     unflagged data is used on averages where there is
                     some unflagged data with the flag set to False.




width
---------------------------------------

:code:`int(1)`

Number of channels to average to form one output channel
                     If a list is given, each bin will apply to one
                     spw in the selection.
                     Default: 1 (no channel average)
                     Options: (int)|[int]

                        Example: chanbin=[2,3] => average 2 channels
                        of 1st selected spectral window and 3 in the
                        second one.



timebin
---------------------------------------

:code:`'0s'`

Bin width for time averaging
                     Default: '0s'

                     Bin width for time averaging. When timebin is
                     greater than 0s, the task will average data in
                     time. Flagged data will be included in the
                     average calculation, unless the parameter
                     keepflags is set to False. In this case only
                     partially flagged rows will be used in the
                     average.



combine
---------------------------------------

:code:`''`

Let the timebin span across scan, state or both.
                     Default: '' (separate time bins by both of the
                     above)
                     Options: 'scan', 'state', 'state,scan'

                     State is equivalent to sub-scans. One scan may
                     have several state ids. For ALMA MSs, the
                     sub-scans are limited to about 30s duration
                     each. In these cases, the task will automatically
                     add state to the combine parameter. To see the
                     number of states in an MS, use the msmd tool. See
                     help msmd.

                        Examples: 
                      * combine = 'scan'; can be useful when the scan
                        number goes up with each integration as in
                        many WSRT MSs.
                      * combine = ['scan', 'state']: disregard scan
                        and state numbers when time averaging.
                      * combine = 'state,scan'; same as above.

                     NOTE: It is not possible to do time average with
                     combine='scan' if the input MMS was partitioned
                     with separationaxis='scan' or 'auto'. In this
                     case, the task will abort with an error.





