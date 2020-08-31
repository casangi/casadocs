#
# stub function definition file for docstring parsing
#

def split(vis, outputvis='', keepmms=True, field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='corrected', keepflags=True, width='1', timebin='0s', combine=''):
    r"""
Create a visibility subset from an existing visibility set

Parameters
   - **vis** (string) - Name of input visibility file
   - **outputvis** (string) - Name of output visibility file
   - **keepmms** (bool) - If the input is a Multi-MS the output will also be a Multi-MS.
   - **field** (string, stringArray, int, intArray) - Select field using field id(s) or field name(s)
   - **spw** (string, stringArray, int, intArray) - Select spectral window/channels
   - **scan** (string, stringArray, int, intArray) - Scan number range
   - **antenna** (string, stringArray, int, intArray) - Select data based on antenna/baseline
   - **correlation** (string, stringArray) - Select data based on correlation
   - **timerange** (string, stringArray, int, intArray) - Select data based on time range
   - **intent** (string, stringArray, int, intArray) - Select observing intent
   - **array** (string, stringArray, int, intArray) - Select (sub)array(s) by array ID number.
   - **uvrange** (string, stringArray, int, intArray) - Select data by baseline length.
   - **observation** (string, stringArray, int, intArray) - Select by observation ID(s)
   - **feed** (string, stringArray, int, intArray) - Multi-feed numbers: Not yet implemented.
   - **datacolumn** (string) - Which data column(s) to process.
   - **keepflags** (bool)
   - **width** (string, stringArray, int, intArray) - Number of channels to average to form one output channel
   - **timebin** (string) - Bin width for time averaging

Subparameters
   .. raw:: html

      <details><summary><i> timebin != 0s </i></summary>

   - **combine** (string='', stringArray) - Span the timebin across scan, state or both

   .. raw:: html

      </details>


Description
      .. note:: **NOTE**: This is the new implementation of **split**.  The old
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
         :name: parameter-descriptions

      .. rubric:: *vis*
         :name: vis

      Name of input MeasurementSet or Multi-MS.

      .. rubric:: *outputvis*
         :name: outputvis

      Name of output MeasurementSet or Multi-MS.

      .. note:: **NOTE**: If a .flagversions file with the name of the output
         MS exist, this task will exit with an error. The user needs to
         rename or remove the existing flagbackup or choose a different
         output name for the MS.

      .. rubric:: *keepmms*
         :name: keepmms

      If the input is a Multi-MS the output will also be a Multi-MS. The
      default value is set to True. The output Multi-MS will have the
      same partition axis of the input MMS.

      .. rubric:: General selection:  *field, spw, antenna, timerange*,
         scan
         :name: general-selection-field-spw-antenna-timerange-scan

      The **split** task uses the same selection syntax as the solving
      tasks for these parameters. See
      `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
      for more information.

      .. rubric:: *datacolumn*
         :name: datacolumn

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
      -  all  (= whichever of the above that are present)

      If the requested column does not exist, the task will exit with an
      error.

      .. note:: **NOTE**: When a single column is chosen for 'datacolumn', the
         output MS always fill the 'DATA' column, regardless of the
         original name of the column in the input MeasurementSet. The
         reason is that the newly created MS needs a DATA  column to be
         valid.

      .. rubric:: *keepflags*
         :name: keepflags

      Keep completely flagged rows in the output or drop them. This has
      no effect on partially flagged rows. All of the channels and
      correlations of a row must be flagged for it to be droppable, and
      a row must be well defined to be keepable. The default is True,
      which will keep completely flagged rows in the output MS.

      .. note:: **IMPORTANT**: Regardless of this parameter, flagged data is
         never included in channel averaging. On the other hand,
         partially flagged rows will always be included in time
         averaging. The average value of the flagged data for averages
         containing ONLY flagged data in the relevant output channel
         will be written to the output with the corresponding flag set
         to True, while only unflagged data is used on averages where
         there is some unflagged data with the flag set to False.

      .. rubric:: Channel averaging parameter: *width*
         :name: channel-averaging-parameter-width

      This parameter gives the number of input channels to average to
      create one output channel. If a list is given, each bin will apply
      to one spw in the selection. The default 1 means that no averaging
      will be applied.

      .. rubric:: Time averaging parameters: *timebin, combine*
         :name: time-averaging-parameters-timebin-combine

      The parameter *timebin* gives the width for time averaging. When
      *timebin* is greater than 0s, the task will average data in time.
      Flagged data will be included  in the average calculation, unless
      the parameter *keepflags* is set to False. In this case only
      partially flagged rows will be used in the average. If present,
      WEIGHT_SPECTRUM/SIGMA_SPECTRUM are used together with the
      channelized flags (FLAG), to compute a weighted average  (using
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
      scan or state boundaries when averaging in time. Options are:
      'scan', 'state', 'state,scan'.

    """
    pass
