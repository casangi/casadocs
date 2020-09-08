#
# stub function definition file for docstring parsing
#

def split(vis, outputvis='', keepmms=True, field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='corrected', keepflags=True, width='1', timebin='0s', combine=''):
    r"""
Create a visibility subset from an existing visibility set

Parameters
   - vis_ (string) - Name of input visibility file
   - outputvis_ (string='') - Name of output visibility file
   - keepmms_ (bool=True) - If the input is a Multi-MS the output will also be a Multi-MS.
   - field_ ({string, stringArray, int, intArray}='') - Select field using field id(s) or field name(s)
   - spw_ ({string, stringArray, int, intArray}='') - Select spectral window/channels
   - scan_ ({string, stringArray, int, intArray}='') - Scan number range
   - antenna_ ({string, stringArray, int, intArray}='') - Select data based on antenna/baseline
   - correlation_ ({string, stringArray}='') - Select data based on correlation
   - timerange_ ({string, stringArray, int, intArray}='') - Select data based on time range
   - intent_ ({string, stringArray, int, intArray}='') - Select observing intent
   - array_ ({string, stringArray, int, intArray}='') - Select (sub)array(s) by array ID number.
   - uvrange_ ({string, stringArray, int, intArray}='') - Select data by baseline length.
   - observation_ ({string, stringArray, int, intArray}='') - Select by observation ID(s)
   - feed_ ({string, stringArray, int, intArray}='') - Multi-feed numbers: Not yet implemented.
   - datacolumn_ (string='corrected') - Which data column(s) to process.
   - keepflags_ (bool=True)
   - width_ ({string, stringArray, int, intArray}='1') - Number of channels to average to form one output channel
   - timebin_ (string='0s') - Bin width for time averaging


Description
   .. note:: **NOTE**: This is the new implementation of **split**. The old
      implementation is available for a short time as oldsplit.

   This new **split** task uses the MSTransform framework underneath.
   **split** is the general purpose program to make a new data set
   that is a subset or averaged form of an existing data set.

   **split** is often used after the initial calibration of the data
   to make a smaller MeasurementSet with only the data that will be
   used in further flagging, imaging and/or self-calibration.
   **split** can average over frequency (channels) and time
   (integrations).

   **split** also supports the Multi-MS (MMS) format as input. For
   more information about MMS, see the help of **partition** and
   **mstransform**.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input MeasurementSet or Multi-MS.

   .. rubric:: *outputvis*
      

   Name of output MeasurementSet or Multi-MS.

   .. note:: **NOTE**: If a .flagversions file with the name of the output
      MS exist, this task will exit with an error. The user needs to
      rename or remove the existing flagbackup or choose a different
      output name for the MS.

   .. rubric:: *keepmms*
      

   If the input is a Multi-MS the output will also be a Multi-MS. The
   default value is set to True. The output Multi-MS will have the
   same partition axis of the input MMS.

   .. rubric:: General selection: *field, spw, antenna, timerange*,
      scan
      

   The **split** task uses the same selection syntax as the solving
   tasks for these parameters. See
   `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
   for more information.

   .. rubric:: *datacolumn*
      

   Give the name of the input data column(s) to process. The default
   is set to "corrected_data". Allowed values are:

   -  corrected
   -  data
   -  model
   -  data,model,corrected
   -  float_data
   -  lag_data
   -  float_data,data
   -  lag_data,data
   -  all (= whichever of the above that are present)

   If the requested column does not exist, the task will exit with an
   error.

   .. note:: **NOTE**: When a single column is chosen for 'datacolumn', the
      output MS always fill the 'DATA' column, regardless of the
      original name of the column in the input MeasurementSet. The
      reason is that the newly created MS needs a DATA column to be
      valid.

   .. rubric:: *keepflags*
      

   Keep completely flagged rows in the output or drop them. This has
   no effect on partially flagged rows. All of the channels and
   correlations of a row must be flagged for it to be droppable, and
   a row must be well defined to be keepable. The default is True,
   which will keep completely flagged rows in the output MS.

   .. warning:: **IMPORTANT**: Regardless of this parameter, flagged data is
      never included in channel averaging. On the other hand,
      partially flagged rows will always be included in time
      averaging. The average value of the flagged data for averages
      containing ONLY flagged data in the relevant output channel
      will be written to the output with the corresponding flag set
      to True, while only unflagged data is used on averages where
      there is some unflagged data with the flag set to False.

   .. rubric:: Channel averaging parameter: *width*
      

   This parameter gives the number of input channels to average to
   create one output channel. If a list is given, each bin will apply
   to one spw in the selection. The default 1 means that no averaging
   will be applied.

   .. rubric:: Time averaging parameters: *timebin, combine*
      

   The parameter *timebin* gives the width for time averaging. When
   *timebin* is greater than 0s, the task will average data in time.
   Flagged data will be included in the average calculation, unless
   the parameter *keepflags* is set to False. In this case only
   partially flagged rows will be used in the average. If present,
   WEIGHT_SPECTRUM/SIGMA_SPECTRUM are used together with the
   channelized flags (FLAG), to compute a weighted average (using
   WEIGHT_SPECTRUM for CORRECTED_DATA and SIGMA_SPECTRUM for DATA).
   Otherwise WEIGHT/SIGMA are used instead to average together data
   from different integrations.

   The *combine* parameter will let the *timebin* span across scan,
   state or both. State is equivalent to sub-scans. One scan may have
   several state ids.

   .. note:: **NOTE**: For ALMA MSs, the sub-scans are limited to about 30s
      duration each. In these cases, the task will automatically add
      state to the *combine* parameter.

   To see the number of states in an MS, use the
   `msmd <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_msmetadata/about>`__
   tool. The default is set to *combine=''*, which will not cross the
   scan or state boundaries when averaging intime. Options are:
   'scan', 'state', 'state,scan'.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _outputvis:

   .. rubric:: outputvis

   | Name of output visibility file
   |                      Default: '' (same as vis)
   | 
   |                         Example: outputvis='ngc5921_out.ms'
   | 
   |                      IMPORTANT: if a .flagversions file with the name
   |                      of the output MS exist, this task will exit with
   |                      an error. The user needs to rename or remove the
   |                      existing flagbackup or choose a different output
   |                      name for the MS.

.. _keepmms:

   .. rubric:: keepmms

   | Create a Multi-MS as the output if the input is a
   | Multi-MS.
   |                      Default: True
   |                      Options: True|False
   | 
   |                      By default it will create a Multi-MS when the
   |                      input is a Multi-MS. The output Multi-MS will
   |                      have the same partition axis of the input
   |                      MMS. See CASA Docs for more information on
   |                      the MMS format.
   | 
   |                      NOTE: It is not possible to do time average with
   |                      combine='scan' if the input MMS was partitioned
   |                      with separationaxis='scan' or 'auto'. In this
   |                      case, the task will abort with an error.

.. _field:

   .. rubric:: field

   | Select field using field id(s) or field name(s)
   |                      Default: '' (all fields)
   |                      
   |                      Use 'go listobs' to obtain the list id's or
   |                      names. If field string is a non-negative integer,
   |                      it is assumed a field index,  otherwise, it is
   |                      assumed a field name.
   | 
   |                         Examples:
   |                         field='0~2'; field ids 0,1,2
   |                         field='0,4,5~7'; field ids 0,4,5,6,7
   |                         field='3C286,3C295'; field named 3C286 and
   |                         3C295
   |                         field = '3,4C*'; field id 3, all names
   |                         starting with 4C

.. _spw:

   .. rubric:: spw

   | Select spectral window/channels
   |                      Default: ''=all spectral windows and channels
   |            
   |                         Examples:
   |                         spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
   |                         spw='<2';  spectral windows less than 2 (i.e. 0,1)
   |                         spw='0:5~61'; spw 0, channels 5 to 61
   |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
   |                         3 - chans 3 to 45.
   |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
   |                         through 6 in each.
   |                         spw = '*:3~64'  channels 3 through 64 for all sp id's
   |                         spw = ' :3~64' will NOT work.
   | 
   |                      NOTE: mstransform does not support multiple
   |                      channel ranges per spectral window (';').

.. _scan:

   .. rubric:: scan

   | Scan number range
   |                      Subparameter of selectdata=True
   |                      Default: '' = all

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline
   |                      Subparameter of selectdata=True
   |                      Default: '' (all)
   | 
   |                      If antenna string is a non-negative integer, it
   |                      is assumed an antenna index, otherwise, it is
   |                      assumed as an antenna name
   |   
   |                          Examples: 
   |                          antenna='5&6'; baseline between antenna
   |                          index 5 and index 6.
   |                          antenna='VA05&VA06'; baseline between VLA
   |                          antenna 5 and 6.
   |                          antenna='5&6;7&8'; baselines with
   |                          indices 5-6 and 7-8
   |                          antenna='5'; all baselines with antenna index
   |                          5
   |                          antenna='05'; all baselines with antenna
   |                          number 05 (VLA old name)
   |                          antenna='5,6,10'; all baselines with antennas
   |                          5,6,10 index numbers

.. _correlation:

   .. rubric:: correlation

   | Select data based on correlation
   |                      Default: '' ==> all
   | 
   |                         Example: correlation="XX,YY".

.. _timerange:

   .. rubric:: timerange

   | Select data based on time range
   |                      Subparameter of selectdata=True
   |                      Default = '' (all)
   | 
   |                         Examples:
   |                         timerange =
   |                         'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   |                         (Note: if YYYY/MM/DD is missing date defaults
   |                         to first day in data set.)
   |                         timerange='09:14:0~09:54:0' picks 40 min on
   |                         first day 
   |                         timerange= '25:00:00~27:30:00' picks 1 hr to 3
   |                         hr 30min on NEXT day
   |                         timerange='09:44:00' pick data within one
   |                         integration of time
   |                         timerange='>10:24:00' data after this time

.. _intent:

   .. rubric:: intent

   | Select observing intent
   |                      Default: '' (no selection by intent)
   | 
   |                         Example: intent='*BANDPASS*'  (selects data
   |                         labelled with BANDPASS intent)

.. _array:

   .. rubric:: array

   | (Sub)array number range
   |                      Default: '' (all)

.. _uvrange:

   .. rubric:: uvrange

   | Select data by baseline length.
   |                      Default = '' (all)
   | 
   |                         Examples:
   |                         uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
   |                         uvrange='>4klambda';uvranges greater than 4 kilo-lambda
   |                         uvrange='0~1000km'; uvrange in kilometers

.. _observation:

   .. rubric:: observation

   | Select by observation ID(s)
   |                      Subparameter of selectdata=True
   |                      Default: '' = all
   | 
   |                          Example: observation='0~2,4'

.. _feed:

   .. rubric:: feed

   | Selection based on the feed 
   |                      NOT IMPLEMENTED YET!
   |                      Default: '' = all

.. _datacolumn:

   .. rubric:: datacolumn

   | Which data column(s) to use for processing
   |                      (case-insensitive).
   |                      Default: 'corrected'
   |                      Options: 'data', 'model', 'corrected',
   |                      'all','float_data', 'lag_data',
   |                      'float_data,data', 'lag_data,data'
   | 
   |                         Example: datacolumn='data'
   |     
   |                      NOTE: 'all' = whichever of the above that are
   |                      present. If the requested column does not exist,
   |                      the task will exit with an error.

.. _keepflags:

   .. rubric:: keepflags

   | Keep *completely flagged rows* instead of dropping them.
   |                      Default: True (keep completely flagged rows in
   |                      the output)
   |                      Options: True|False
   | 
   |                      Keepflags has no effect on partially flagged
   |                      rows. All of the channels and correlations of a
   |                      row must be flagged for it to be droppable, and a
   |                      row must be well defined to be keepable.
   | 
   |                      IMPORTANT: Regardless of this parameter, flagged
   |                      data is never included in channel averaging. On
   |                      the other hand, partially flagged rows will
   |                      always be included in time averaging. The average
   |                      value of the flagged data for averages containing
   |                      ONLY flagged data in the relevant output channel
   |                      will be written to the output with the
   |                      corresponding flag set to True, while only
   |                      unflagged data is used on averages where there is
   |                      some unflagged data with the flag set to False.

.. _width:

   .. rubric:: width

   | Number of channels to average to form one output channel
   |                      If a list is given, each bin will apply to one
   |                      spw in the selection.
   |                      Default: 1 (no channel average)
   |                      Options: (int)|[int]
   | 
   |                         Example: chanbin=[2,3] => average 2 channels
   |                         of 1st selected spectral window and 3 in the
   |                         second one.

.. _timebin:

   .. rubric:: timebin

   | Bin width for time averaging
   |                      Default: '0s'
   | 
   |                      Bin width for time averaging. When timebin is
   |                      greater than 0s, the task will average data in
   |                      time. Flagged data will be included in the
   |                      average calculation, unless the parameter
   |                      keepflags is set to False. In this case only
   |                      partially flagged rows will be used in the
   |                      average.

.. _combine:

   .. rubric:: combine

   | Let the timebin span across scan, state or both.
   |                      Default: '' (separate time bins by both of the
   |                      above)
   |                      Options: 'scan', 'state', 'state,scan'
   | 
   |                      State is equivalent to sub-scans. One scan may
   |                      have several state ids. For ALMA MSs, the
   |                      sub-scans are limited to about 30s duration
   |                      each. In these cases, the task will automatically
   |                      add state to the combine parameter. To see the
   |                      number of states in an MS, use the msmd tool. See
   |                      help msmd.
   | 
   |                         Examples: 
   |                       * combine = 'scan'; can be useful when the scan
   |                         number goes up with each integration as in
   |                         many WSRT MSs.
   |                       * combine = ['scan', 'state']: disregard scan
   |                         and state numbers when time averaging.
   |                       * combine = 'state,scan'; same as above.
   | 
   |                      NOTE: It is not possible to do time average with
   |                      combine='scan' if the input MMS was partitioned
   |                      with separationaxis='scan' or 'auto'. In this
   |                      case, the task will abort with an error.


    """
    pass
