

.. _Description:

Description
   .. warning:: There is a `Known Issues <../../notebooks/introduction.html#Known-Issues>`__ for statwt: If not run in preview mode, this application can
      modify the WEIGHT, WEIGHT_SPECTRUM, SIGMA, SIGMA_SPECTRUM,
      FLAG, and FLAG_ROW columns of the input MS. If you want a
      pristine copy of the input MS to be preserved, you should make
      a copy of it before running this application.
   
   This application computes values for the WEIGHT and
   WEIGHT_SPECTRUM (if present) columns and/or the SIGMA and
   SIGMA_SPECTRUM (if present) columns based on the variance of
   values in the CORRECTED_DATA or DATA column. If the MS does not
   have the specified data column, the application will fail. The
   following algorithm is used:
   
   #. For unflagged data in each sample, create two sets of values,
      one set is composed solely of the real part of the data values,
      the other set is composed solely of the imaginary part of the
      data values.
   #. Compute the weighted (by exposure time) variance of each of
      these sets, v :math:`_r` and v :math:`_i`. The weighted
      variance per unit inverse exposure time, v, is computed using v
      = sum(e :math:`_i` \* (V :math:`_i` - <V>) :math:`^2`)/N,
      where e :math:`_i` is the exposure time for real/imaginary
      part of  visibility V :math:`_i` and <V> = sum(e :math:`_i`
      \* V :math:`_i`)/sum(e :math:`_i`) is the weighted mean of
      all the visibilities in the set, and N is the number of
      (unflagged) visibilities (see also this `Knowledgebase
      Article) <../../notebooks/memo-series.ipynb#Calculation-of-Weights-for-Data-with-Varying-Integration-Time>`__
   #. Compute v :math:`_{eq}` :math:`=` (v :math:`_{r}` :math:`+`
      v :math:`_{i}`) :math:`/` 2.
   #. The associated weight of visibility V :math:`_i`  is 
      e :math:`_i` / V (see `Knowledgebase
      Article) <../../notebooks/memo-series.ipynb#Calculation-of-Weights-for-Data-with-Varying-Integration-Time>`__.
      The weight will have unit of (data unit), e.g., Jy. The
      visibility weights are what this application computes and
      writes.
   
   Data are aggregated on a per-baseline, per-data description ID
   basis. Data are aggregated in bins determined by the specified
   values of the timebin and chanbin parameters. By default, data for
   separate correlations are aggregated separately. This behavior can
   be overriden by specifying combine="corr" (see below).
   
   .. rubric:: Rules regarding creating/initializing WEIGHT_SPECTRUM column
   
   #. If run in preview mode (preview=True), no data are modified and
      no columns are added.
   #. Else if datacolumn='residual' or 'residual_data' and a
      CORRECTED_DATA column exists, the WEIGHT and WEIGHT_SPECTRUM
      columns are not modified.
   #. Else if the MS already has a WEIGHT_SPECTRUM and this column
      has been initialized (has values) it will always be populated
      with the new weights. The WEIGHT column will be populated with
      the corresponding median values of the associated
      WEIGHT_SPECTRUM array.
   #. Else if the frequency interval (chanbin) is not the default
      ('spw', not to be confused with the parameter spw), the
      WEIGHT_SPECTRUM column will be created (if it doesn't already
      exist) and the new weights will be written to it. The WEIGHT
      column should be populated with the corresponding median values
      of the WEIGHT_SPECTRUM array.
   #. Otherwise the single value for each spectral window will be
      written to the WEIGHT column; the WEIGHT_SPECTRUM column will
      not be added if it doesn't already exist, and if it does, it
      will remain uninitialized (no values will be written to it).
   #. In cases where columns are added and initialized, the
      WEIGHT_SPECTRUM values will be set equal to the corresponding
      WEIGHT values, and the SIGMA_SPECTRUM values will be set to the
      corresponding SIGMA values.
   
   In cases where columns are added and initialized, the
   WEIGHT_SPECTRUM values will be set equal to the corresponding
   WEIGHT values, and the SIGMA_SPECTRUM values will be set to the
   corresponding SIGMA values.
   
   .. warning:: WARNING: For some cases when only a subset of data is selected
      and the WEIGHT_SPECTRUM and/or SIGMA_SPECTRUM columns are
      created, there is a known code issue in which these columns are
      not properly created and initialized for the specified subset
      of data, although they are properly initialized for the entire
      dataset. In such cases, an exception will be thrown. Because
      the columns are created for the entire dataset, the user simply
      needs to rerun the statwt task using the same parameters and
      the task should complete as expected. Should this condition
      occur when the user is using the ms.statwt() tool method, the
      user should close the ms tool, and then reopen it using the
      same data set and configure the same selection, and rerun
      ms.statwt(). The tool method should then complete as expected.

   
   .. rubric:: Rules for modifying WEIGHT, WEIGHT_SPECTRUM, SIGMA, and SIGMA_SPECTRUM
   
   #. If datacolumn='corrected' or 'residual', then values are
      written to the WEIGHT and WEIGHT_SPECTRUM (if applicable)
      columns only.
   #. If datacolumn='data' or 'residual_data' and the CORRECTED_DATA
      column does not exist, then values are written to the WEIGHT
      and WEIGHT_SPECTRUM (if applicable) columns and values in the
      SIGMA and SIGMA_SPECTRUM are set to
      1/ :math:`\sqrt{\rm {newly\,computed\,weight}}`. If a weight
      value is 0, the corresponding sigma value is -1.
   #. If datacolumn='data' or 'residual_data' and the CORRECTED_DATA
      column does exist, then the WEIGHT and WEIGHT_SPECTRUM columns
      are not updated and values in the SIGMA and SIGMA_SPECTRUM are
      set to 1/ :math:`\sqrt{\rm {newly\,computed\,weight}}`. If a
      weight value is 0, the corresponding sigma value is -1. In this
      case, you should either split out the DATA column and run
      **statwt**, or run with *datacolumn='corrected'* or
      *'residual'* to update WEIGHT/WEIGHT_SPECTRUM. Otherwise the
      data are internally not consistent.
   
   .. note:: NOTE: statwt will produce an error if the measurement set has
      WEIGHT_SPECTRUM and/or SIGMA_SPECTRUM columns for which some
      rows are initialized (have values) and other rows have no data.
      It is recommended to run the initweights task to completely
      initialize these columns if you encounter this error.

   
   .. rubric:: Time Binning
   
   One of two algorithms can be used for time binning. If
   slidetimebin=True, then a sliding time bin of the specified width
   is used. If slidetimebin=False, then block time processing is
   used. The sliding time bin algorithm will generally be both more
   memory intensive and take longer than the block processing
   algorithm. Each algorithm is discussed in detail below.
   
   If the value of timebin is an integer,this value represents the
   number of contiguous, unique time stamps (from the MS TIME column)
   that should be used for averaging.
   
   The timebin parameter can also be specified as a quantity (string)
   that must have time conformant units.
   
   .. rubric:: Block Time Processing
   
   The data are processed in contiguous time blocks in this case.
   This means that all WEIGHT_SPECTRUM values will be set to the same
   value for all data within the same time bin/channel
   bin/correlation bin (see the section on channel binning and
   description of combine="corr" for more details on channel binning
   and correlation binning).
   
   If timebin is specified as a time quantity (eg, '110s'), then the
   time bins are not necessarily contiguous and are not necessarily
   the same width. The start of a bin is always coincident with a
   value from the TIME column, So for example, if values from the
   TIME column are [20s, 60s, 100s, 140s, 180s, 230s], and timebin =
   110s, the first bin would start at 20s and run to 130s, so that
   data from timestamps 20s, 60s, and 100s will be included in the
   first bin. The second bin would start at 140s, so that data for
   timestamps 140s, 180s, and 230s would be included in the second
   bin.
   
   In the case where timebin is an integer, this denotes the number
   of contigous timestamps that should be binned together. Note that,
   in this case, for rows "left over" in the upper edge of the bin,
   their values are computed using timebin that would include rows
   with times earlier than them. For example, in an MS with 8 rows in
   one block to be processed and timebin=3, timestamps 1, 2, and 3
   would be used to compute the weights of the first three three
   rows, and rows 4, 5, and 6 would be used to compute weights for
   the next three rows as expected. Rows 7 and 8 are "left over"
   rows, but three rows (as per the integer timebin specification)
   are still used to compute them. Row 7 and 8 weights are computed
   by combining data in rows 6, 7, and 8.
   
   .. rubric:: Sliding Time Window Processing
   
   In the sliding time window case, in the case where timebin is a
   time quantity, the time window is always centered on the timestamp
   of the row in question and extends timebin 2 around that
   timestamp, subject the the time block boundaries. In the case
   where timebin is an integer, there are two cases to consider:
   
   #. timebin is odd: In this case the target row's data and the data
      from the +/-(n-1)/2 rows around the target row are also used.
   #. timebin is even: In this case, the target row's data and the
      data from the n/2 rows after the target row and the n/2 - 1
      rows before the target row are used.
   
   In all cases for "edge" rows, the timebin extends from the edge of
   the block to the corresponding timebin value of rows away from the
   edge, so that the timebin is not symmetrical around the target
   rows, but includes the number of rows specified by the timebin
   value.
   
   .. rubric:: Overriding Default Block Boundaries
   
   Rows with the same baselines and data description IDs which are
   included in that window are used for determining the weight of
   that row. The boundaries of the time block to which the window is
   restricted are determined by changes in FIELD_ID, ARRAY_ID, and
   SCAN_NUMBER. One can override this behavior for FIELD_ID and/or
   SCAN_NUMBER by specifying the combine parameter (see below).
   Unlike the time block processing algorithm, this sliding time
   window algorithm requires that details of all rows for the time
   window in question are kept in memory, and thus the sliding window
   algorithm in general and the block processing row when timebin is
   an int, requires more memory than the block processing method when
   timebin is a quantity. Also, unlike the block processing method
   which computes a single value for all weights within a single bin,
   the sliding window method requires that each row (along with each
   channel and correlation bin) be processed individually, so in
   general the sliding window method will take longer than the block
   processing method.

   
   .. rubric:: Channel Binning
   
   The width of channel bins is specified via the chanbin parameter.
   Channel binning occurs within individual spectral windows; bins
   never span multiple spectral windows. Each channel will be
   included in exactly one bin. The default value 'spw' indicates
   that all channels in each spectral window are to be included in a
   single bin.
   
   Any other string value is interpreted as a quantity, and so
   should have frequency units, e.g., "1MHz". In this case, the
   channel frequencies from the CHAN_FREQ column of the
   SPECTRAL_WINDOW subtable of the MS are used to determine the
   bins. The first bin starts at the channel frequency of the 0th
   channel in the spectral window. Channels with frequencies that
   differ by less than the value specified by the chanbin parameter
   are included in this bin. The next bin starts at the frequency
   of the first channel outside the first bin, and the process is
   repeated until all channels have been binned.

   If specified as an integer, the value is interpreted as the
   number of channels to include in each bin. The final bin in the
   spectral window may not necessarily contain this number of
   channels. For example, if a spectral window has 15 channels, and
   chanbin is specified to be 6, then channels 0-5 will comprise
   the first bin, channels 6-11 the second, and channels 12-14 the
   third, so that only three channels will comprise the final bin.
   
   .. rubric:: Minimum required number of visibilities
   
   The minsamp parameter allows the user to specify the minimum
   number of unflagged visibilities that must be present in a sample
   for that sample's weight to be computed. If a sample has less than
   this number of unflagged points, the associated weights of all the
   points in the sample are set to zero, and all the points in the
   sample are flagged.
   
   .. warning:: WARNING: Since statwt treats each baseline
      separately, selecting only a single channel in a spectral
      window will not satisfy the minimum number of samples (minsamp)
      if statwt is run with default parameters, leading to all the
      data in that spectral window being flagged. For such data, the
      user will need to change the default parameters in order to
      aggregate enough samples to satisfy minsamp (e.g., by setting
      combine='corr' if there are multiple correlation products, or
      timebin>1).

   
   .. rubric:: Aggregating data across boundaries
   
   By default, data are not aggregated across changes in values in
   the columns ARRAY_ID, SCAN_NUMBER, STATE_ID, FIELD_ID, and
   DATA_DESC_ID. One can override this behavior for SCAN_NUMBER,
   STATE_ID, and FIELD_ID by specifying the combine parameter. For
   example, specifying combine="scan" will ignore scan boundaries
   when aggregating data. Specifying combine="field, scan" will
   ignore both scan and field boundaries when aggregating data. Also
   by default, data for separate correlations are aggregated
   separately. Data for all correlations within each spectral window
   can be aggregated together by specifying "corr" in the combine
   parameter. Any combination and permutation of "scan", "field",
   "state", and "corr" are supported by the combine parameter. Other
   values will be silently ignored.

   
   .. rubric:: Statistics algorithms
   
   The supported statistics algorithms are described in detail in the
   imstat and ia.statistics() help. For the current application,
   these algorithms are used to compute vr and vi (see above), such
   that the set of the real parts of the visibilities and the set of
   the imaginary parts of the visibilities are treated as independent
   data sets.  Care should be taken not to tune these algorithms in a
   way that will discard significant portions of the tails of the
   underlying noise distribution (e.g., fence < 2 for the
   'HINGES-FENCES' algorithm).

   
   .. rubric:: Range of acceptable weights
   
   The wtrange parameter allows one to specify the acceptable range
   (inclusive, except for zero) for weights. Data with weights
   computed to be outside this range will be flagged. If not
   specified (empty array), all weights are considered to be
   acceptable. If specified, the array must contain exactly two
   non-negative numeric values. Note that data with weights of zero
   are always flagged. The units of the wtrange parameter will always
   match that of the WEIGHT column, even if the task is modifying the
   SIGMA column.

   
   .. rubric:: Including/excluding channels
   
   Channels can be included in the computation of the weights by
   specifying the fitspw parameter. This parameter accepts a valid MS
   channel selection string. Data associated with the selected
   channels will be used in computing the weights; all other channels
   will be excluded from the computation of weights. By default
   (empty string), all channels are included. If the
   Boolean excludechans parameter is set to True, the channel
   selection will be inverted and exclude the selection made
   in fitspw. 
   
   .. warning:: CAUTION: Use of fitspw, when chanbin is not 'spw', may lead to
      the excluded channels being flagged for having less than the
      minimum number of samples (minsamp).

   
   .. rubric:: Preview mode
   
   By setting preview=True, the application is run in preview mode.
   In this mode, no data in the input MS are changed, although the
   amount of data that the application would have flagged is
   reported.

   
   .. rubric:: DATA column
   
   The datacolumn parameter can be specified to indicate which data
   column should be used for computing the weights. The values
   "corrected" for the CORRECTED_DATA column and "data" for the DATA
   column are supported (minimum match, case insensitive). One may
   specify 'residual' in which case the values used are the result of
   the CORRECTED_DATA column minus the model, or 'residual_data' in
   which case the values used are the DATA column minus the model,
   where model is the MODEL_DATA column if it exists, or if it
   doesn't, the virtual source model if one exists, or if that
   doesn't, then no model is used and the 'residual' and
   'residual_data' cases are equivalent to the 'corrected' and 'data'
   cases, respectively. The last two options are to allow for
   operation on timescales or frequency ranges which are larger than
   that over which the sky signal is expected to be constant. This
   situation arises in e.g., OTF mapping, and also perhaps with
   sources with significant spectral structure. In cases where a
   necessary column doesn't exist, an exception will be thrown and no
   data will be changed.
   
   .. note:: NOTE: It is the user's responsibility to ensure that a model
      has been set for all selected fields before using
      datacolumn='residual' or 'residual_data'.

   
   .. rubric:: Return value
   
   In all cases, the mean and variance of the set of all weights
   computed by the application is reported and returned in a
   dictionary with keys 'mean' and 'variance'. Weights for which
   there are corresponding flags (=True) prior to running the
   application are excluded from the computation of these statistics.
   If the WEIGHT_SPECTRUM values are available, they are used to
   compute the statistics, otherwise, the WEIGHT values are used. The
   returned statistics are always computed using the 'CLASSIC'
   algorithm; the value of *statalg* has no impact on how they are
   computed. The units of the the returned statistics will always
   match that of the WEIGHT column, even if the task is modifying the
   SIGMA column.

   
   .. rubric:: Other considerations
   
   Flagged values are not used in computing the weights, although the
   associated weights of these values are updated. If the variance
   for a set of data is 0, all associated flags for that data are set
   to True, and the corresponding weights are set to 0.
   

.. _Examples:

Examples
   Update the weights of a MS as in the **statwt** task. All channels
   in a SPW will receive equal weight:
   
   ::
   
      statwt("my.ms")

   
   Update the weights of a MS, using a calculation that disregards
   visibilities in spectral window 2 between channels 7 and 16. All
   channels in a SPW will receive equal weight, even those
   disregarded in the calculation:
   
   ::
   
      statwt("my.ms", fitspw='2:7~16’, excludechans=True)

   
   Update the weights of a MS using an algorithm robust to outliers.
   All channels in a SPW will receive equal weight:
   
   ::
   
      statwt("my.ms", statalg='chauvenet')

   
   Update the weights of a MS using time binning of 300s. All
   channels in a SPW will receive equal weight, and all times within
   a *timebin* will receive equal weight:
   
   ::
   
      statwt("my.ms", timebin="300s")

   
   Update the weights of a MS using time binning of 10 integrations.
   Each channel and integration will receive a unique weight. The
   weight calculation will consider all visibilities within the time
   bin:
   
   ::
   
      statwt("my.ms", timebin=10, slidetimebin=True, chanbin=1)

   
   Calculate, but do not update the weights of spectral window 3 of a
   MS. Return statistics which summarize the calculated weights as a
   dictionary:
   
   ::
   
      weight_stats = statwt("my.ms", preview=True, spw='3')
   

.. _Development:

Development
   No additional development details

