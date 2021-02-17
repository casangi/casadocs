

.. _Description:

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
   
   *vis*
   
   Name of input MeasurementSet or Multi-MS.
   
   *outputvis*
   
   Name of output MeasurementSet or Multi-MS.
   
   .. note:: **NOTE**: If a .flagversions file with the name of the output
      MS exist, this task will exit with an error. The user needs to
      rename or remove the existing flagbackup or choose a different
      output name for the MS.
   
   *keepmms*
   
   If the input is a Multi-MS the output will also be a Multi-MS. The
   default value is set to True. The output Multi-MS will have the
   same partition axis of the input MMS.
   
   .. rubric:: General selection:  *field, spw, antenna, timerange*, scan
   
   The **split** task uses the same selection syntax as the solving
   tasks for these parameters. See
   `here <../../notebooks/visibility_data_selection.ipynb>`__
   for more information.
   
   *datacolumn*
   
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
   
   *keepflags*
   
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
   
   Channel averaging parameter: *width*
   
   This parameter gives the number of input channels to average to
   create one output channel. If a list is given, each bin will apply
   to one spw in the selection. The default 1 means that no averaging
   will be applied.
   
   Time averaging parameters: *timebin, combine*
   
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
   `msmd <../../api/casatools.rst>`__
   tool. The default is set to *combine=''*, which will not cross the
   scan or state boundaries when averaging in time. Options are:
   'scan', 'state', 'state,scan'.
   

.. _Examples:

Examples
   .. rubric:: Split with field selections
   
   Create a new MS with field ID 3 and all field names starting with
   4C.
   
   ::
   
      split(vis='example.ms',outputvis='test.ms',field='3,4C*')
   
   .. rubric:: Split with spectral window and channel selections
   
   Split channels 3 through 64 for all SPW IDs.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms', spw='*:3~64')
   
   Split with multiple channel selection. The following example will
   select channels 4 through 13 and 10 through 59 inclusive from spw
   8.
   
   ::
   
      split('example.ms',outputvis='test.ms',spw='8:4~13;10~59')
   
   Split with multiple spws and channel selections. The following
   example will select all channels from spw 4, channels 4 through 59
   inclusive from spw 7. It will also select channels 4 through 13
   and 10 through 59 from spw 8. The output MS will have three
   spectral windows, reindexed from 0 through 2.
   
   ::
   
      split('example.ms',outputvis='test.ms',spw='4,7:4~59,8:4~13;10~59')
   
   On the other hand, the following example will select only channels
   4 through 59 from all three spectral windows 4, 5 and 6.
   
   ::
   
      split('example.ms',outputvis='test.ms',spw='4~6:4~59')

   
   .. rubric:: Split with antenna selections
   
   Split using antenna selection. Non-negative integers are assumed
   to be antenna indices, and anything else is taken as an antenna
   name. The following example will split the baseline between
   antennas VA05 and VA06.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms', antenna='VA05&VA06')
   
   .. rubric:: Channel Averaging
   
   Average 2 channels of first selected SPW and 3 channels in second
   SPW.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms',spw='0,1', width=[2,3])
   
   .. rubric:: Time Averaging
   
   Average in time across scans. The following example can be useful
   when the scan number goes up with each integration as in many WSRT
   MSs.
   
   ::
   
      split(vis='example.ms', outputvis='test.ms',timebin='20s', combine='scan')
   

.. _Development:

Development
   No additional development details

