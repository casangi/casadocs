

.. _Description:

Description

   .. warning:: There are `Known Issues <../../notebooks/introduction.html#Known-Issues>`__ for mstransform.

   **mstransform** is a multipurpose task that provides all the
   functionality of
   `split, partition, cvel, hanningsmooth, uvcontsub and applycal <../../api/casatasks.rst>`__
   with the possibility of applying each of these transformations
   separately or together in an in-memory pipeline, thus avoiding
   unnecessary I/O steps. Each transformation can be activated
   through a boolean parameter in the task interface. Below are the
   main parameter descriptions. See also how to run **mstransform**
   for some use-cases in the Examples section below.

   
   .. rubric:: Parameter Descriptions
   
   *createmms*
   
   When set to True, this parameter will create an output Multi-MS,
   which is the basic step for running CASA in parallel. See more
   about this in the
   `Parallelization <../../notebooks/parallel-processing.ipynb>`__
   chapter.

   
   .. rubric:: Combination of spws: *combinespws*
   
   Combine the input spectral windows into a new output spectral
   window. Whenever the data to be combined has different *EXPOSURE*
   values in the spectral windows, mstransform will use the
   *WEIGHT_SPECTRUM* for the combination. If *WEIGHT_SPECTRUM* is not
   available, it will use the values from the *WEIGHT* column. Each
   output channel is calculated using the following equation:
   
   .. math:: outputChannel_{j} = \frac{\sum (inputChannel_{i}*contributionFraction_{i}*inputWeightSpectrum_{i})}{\sum(contributionFraction_{i}*inputWeightSpectrum_{i})}
   
   .. warning:: **ALERT**: The combination of spws is only supported when the
      number of channels is the same for all the spws. Using this
      option with different numbers of channels for different spws
      will result in an error.

   
   .. rubric:: Channel averaging: *chanaverage*
   
   Average data across channels. Partially flagged data is not
   included in the average unless all data contributing to a given
   output channel is flagged. In this case, **mstransform**
   calculates the average of all flagged data, and writes it to the
   output MS with the corresponding flag set to true. If present,
   *WEIGHT_SPECTRUM*/*SIGMA_SPECTRUM* are used together with the
   channelized flags (FLAG), to compute a weighted average (using
   *WEIGHT_SPECTRUM* for *CORRECTED_DATA* and *SIGMA_SPECTRUM* for
   *DATA*). The sub-parameter *chanbin* takes an integer number or a
   list of integers. If a list is given, each bin applies to one of
   the selected spws.
   
   .. note:: **NOTE**: *WEIGHT_SPECTRUM*/*SIGMA_SPECTRUM* will be used (if
      present) in addition to the flags to compute a weighted
      average. The calculations is done as follows:
   
   #. When WEIGHT_SPECTRUM/SIGMA_SPECTRUM are not present:
   
   .. math:: Average = \frac{\sum(Chan_{i}*Flag_{i})}{\sum(Flag_{i})}
   
   #. When WEIGHT_SPECTRUM/SIGMA_SPECTRUM are present:

   
   .. math:: Average = \frac{\sum(Chan_i*Flag_i*WeightSpectrum_i)}{\sum(Flag_i*WeightSpectrum_i)}

   
   .. rubric:: Hanning smoothing: *hanning*
   
   This function Hanning smooths the frequency channels with a
   weighted running average to remove Gibbs ringing. The weights are
   0.5 for the central channel and 0.25 for each of the two adjacent
   channels. The first and last channels are flagged. Inclusion of a
   flagged value in an average causes that data value to be flagged.
   By default, all visibility data columns available in the MS will
   be smoothed, unless a specific column is given in the *datacolumn*
   parameter.

   
   .. rubric:: Reference frame transformation: *regridms*
   
   Transform channel labels and visibilities to a different spectral
   reference frame, which is appropriate for science analysis. For
   example, transform from TOPO to LSRK to correct for Doppler shifts
   throughout the time of the observation.
   
   .. note:: **NOTE**: U,V,W data are not transformed with this function
   
   The regridding *mode* can be "channel", "velocity", "frequency" or
   "channel_b", *channel* being the default. When set to *velocity*
   or *frequency*, it means that the channels must be specified in
   the respective units. When set to *channel_b* it means an
   alternative channel mode that does not force an equidistant grid,
   which is faster to process.
   
   The *start* sub-parameter gives the first channel to use in the
   output spw (depending on the *mode*). When *mode='channel'*,
   *start* means the first channel in the input spw to use when
   creating the output spw. When *mode='frequency'*, *start* means
   the lowest frequency of the output spw. If this information is not
   available, **mstransform** will calculate it automatically.
   
   The *width* sub-parameter gives the width of the output channels.
   The *width* is expressed in different units, depending on the
   *mode* chosen. This way the sub-parameter *width* can take units
   of either number of input channels (mode="channel"), velocity
   (mode="velocity"), or frequency (mode="frequency"). For example,
   the value of the *width* parameter can be "4" (mode="channel"),
   "-1.0km/s" (mode="velocity"), or "1.0kHz" (mode="frequency").
   
   .. warning:: **NOTE**: **mstransform** will only shift spws with channel
      widths of the same sign in a single operation. If you are
      regridding spws with mixed positive and negative channel
      widths, you should run this task separated for each group of
      spws. You can verify the channel widths for your MS using
      **listobs** for example, and looking at the SPW table, column
      ChanWidth.
   
   It is possible to separate the spectral windows into a given
   number of spws. This is achieved with the sub-parameter *nspw*,
   which is activate when set to > 1. Internally, the framework will
   combine the selected spws before separating them so that channel
   gaps and overlaps are taken into account. This sub-parameter will
   create a regular grid of spws in the output MS. If *nchan* is set,
   it will refer to the number of output channels in each of the
   separated spws.

   
   .. rubric:: Time averaging: *timeaverage*
   
   Average data across time by setting *timeaverage=True* and giving
   the bin for averaging using the sub-parameter *timebin*. Partially
   flagged data is not included in the average unless all data
   contributing to a given output channel is flagged. In this case,
   **mstransform** calculates the average of all flagged data, and
   writes it to the output MS with the corresponding flag set to
   True. If *keepflags=False*, the fully flagged data is not written
   to the output MS. If present,
   *WEIGHT_SPECTRUM*/*SIGMA_SPECTRUM* are used together with the
   channelized flags (*FLAG*), to compute a weighted average (using
   *WEIGHT_SPECTRUM* for *CORRECTED_DATA* and *SIGMA_SPECTRUM* for
   *DATA*). Otherwise *WEIGHT*/*SIGMA* are used instead to average
   together data from different integrations.
   
   The *timespan* sub-parameter will span the *timebin* across scans,
   states or both. State is equivalent to sub-scans and one scan may
   have several state IDs. Another option when doing time averaging
   is to provide a maximum separation of start-to-end baselines that
   can be included in an average with the use of the *maxuvwdistance*
   sub-parameter.

   
   .. rubric:: On-the-fly calibration parameters: *docallib*
   
   **mstransform** is able to apply the calibrations on the fly,
   similar to the **applycal** task. This is possible by specifying a
   `Cal
   Library <../../notebooks/uv_manipulation.ipynb#On-the-fly-calibration>`__
   filename that contains the actual specification for the
   calibrations to be applied. See more about the Cal Library file
   syntax `here <../../build/notebooks/cal_library_syntax.ipynb>`__.
   See also the examples section below for how to apply the Cal library in
   mstransform.


   .. rubric:: Multi-MS Processing using mstransform
   
   Task **mstransform** will process an input
   `Multi-MS <../../notebooks/parallel-processing.ipynb#The-Multi-MS>`__
   (MMS) in parallel whenever possible. Each Sub-MS of the MMS will
   be processed in a separate computer core and the results will be
   post-processed at the end to create an output MMS. The output MMS
   will have the same *separationaxis* of the input MMS, which will
   be written to the table.info file inside the MMS directory. 
   
   Naturally, some transformations available in **mstransform**
   require more care when the user first partition the MS. If one
   wants to do a combination of spws by setting the
   parameter *combinespws=True* in **mstransform**, the input MMS
   needs to contain all the selected spws in each of the Sub-MSs or
   the processing will fail. For this, one may set the
   initial *separationaxis* to 'scan' or use the default 'auto' with
   a proper *numsubms* set so that each Sub-MS in the MMS is
   self-contained with all the necessary spws for the combination.
   
   The task will check if the Sub-MSs contain all the selected spws
   when *combinespws=True* and if not, it will issue a warning and
   process the input MMS as a monolithic MS. In this case, the
   separation axis of the output MMS will be set to 'scan',
   regardless of what the input axis was.
   
   A similar case happens when the separation axis of the input MMS
   is per 'scan' and the user wants to do time averaging with time
   spanning across scans. If the individual Sub-MSs are
   not self-contained of the necessary scans and the duration of the
   scans is shorter than the given *timebin*, the spanning will not
   be possible. In this case, the task will process the input MMS
   as a monolithic MS and will set the axis of the output MMS to spw.
   
   It is important that the user sets the separation axis correctly
   when first partitioning the MS. See the table below for when it is
   possible to process the input MMS in parallel or not,
   using **mstransform**.
   
   +-----------------+-----------------+-----------------+-----------------+
   | **input MMS     | **combinespws = | **nspw > 1**    | **timeaverage = |
   | axis**          | True**          |                 | True**          |
   |                 |                 |                 |                 |
   |                 |                 |                 | **timespan =    |
   |                 |                 |                 | 'scan'**        |
   +-----------------+-----------------+-----------------+-----------------+
   | scan            | YES             | YES             | NO              |
   +-----------------+-----------------+-----------------+-----------------+
   | spw             | NO              | NO              | YES             |
   +-----------------+-----------------+-----------------+-----------------+
   | auto            | maybe           | maybe           | maybe           |
   +-----------------+-----------------+-----------------+-----------------+
   
   .. note:: **NOTE**: If **mstransform** decides it's not possible to
      process the MMS in parallel, it will still create an output but
      the processing will run serially without any parallelization
      involved.
   

.. _Examples:

Examples
   Split out a single channel:
   
   ::
   
      mstransform(vis='ctb80-vsm.ms', outputvis='mychn.ms',
                  datacolumn='data', spw='0:25')
   
   Combine the selected spws into a single output spw:
   
   ::
   
      mstransform(vis='Four_ants.ms', outputvis='myspw.ms',
                  combinespws=True, spw='0~3')
   
   Combine two spws and regrid one field, using two input channels to
   make one output:
   
   ::
   
      mstransform(vis='jupiter6cm.demo.ms',outputvis='test1.ms',datacolumn='DATA',field='11',
                  spw='0,1', combinespws=True, regridms=True, nchan=1, width=2)
   
   Combine 24 spws and regrid in frequency mode to create 21 output
   channels, change the phase center:
   
   ::
   
      mstransform(vis='g19_d2usb_targets_line.ms',
                  outputvis='test2.ms', datacolumn='DATA', combinespws=True,
                  regridms=True, mode='frequency', nchan=21, start='229587.0MHz',
                  width='1600kHz', phasecenter="J2000 18h25m56.09 -12d04m28.20")
   
   Apply Hanning smoothing to an MS:
   
   ::
   
      mstransform(vis='g19_d2usb_targets_line.ms',
                  outputvis='test3.ms', datacolumn='DATA', hanning=True)
   
   Change the reference frame and apply Hanning smoothing after
   combining all spws:
   
   ::
   
      mstransform(vis='g19_d2usb_targets_line.ms',
                  outputvis='test4.ms', datacolumn='DATA', combinespws=True,
                  regridms=True, mode="channel", outframe="BARY",
                  phasecenter="J2000 18h25m56.09 -12d04m28.20", hanning = True)
   
   Apply time averaging using a bin of 30 seconds on the default
   *CORRECTED* column:
   
   ::
   
      mstransform(vis='g19_d2usb_targets_line.ms',
                  outputvis='test5.ms', timeaverage=True, timebin='30s')
   
   Apply OTF calibration to ngc5921 using a calibration library:
   
   ::
   
      mstransform(vis='ngc5921.ms',
                  outputvis='ngc5921_calibrated.ms',docallib=True,
                  callib='./ngc5921_callib.txt')
   
   The calibration file (ngc5921_callib.txt) used in the above
   example contains the following information:
   
   ::
   
      caltable='ngc5921_regression/ngc5921.bcal' calwt=True tinterp='nearest' 
      caltable='ngc5921_regression/ngc5921.fluxscale' calwt=True tinterp='nearest' fldmap='nearest' 
      caltable='ngc5921_regression/ngc5921.gcal' calwt=True field='0' tinterp='nearest' fldmap=[0] 
      caltable='ngc5921_regression/ngc5921.gcal' calwt=True field='1,2' tinterp='linear' fldmap='1'
   

.. _Development:

Development
   No additional development details

