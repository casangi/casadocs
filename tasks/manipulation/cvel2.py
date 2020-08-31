#
# stub function definition file for docstring parsing
#

def cvel2(vis, outputvis='', keepmms=True, passall=False, field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='all', mode='channel', nchan=-1, start='0', width='1', interpolation='linear', phasecenter='', restfreq='', outframe='', veltype='radio', hanning=False):
    r"""
Regrid an MS or MMS to a new spectral window, channel structure or frame

Parameters
   - **vis** (string) - Name of input visibility file
   - **outputvis** (string) - Name of output visibility file
   - **keepmms** (bool) - Create a Multi-MS as the output if the input is a Multi-MS
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
   - **datacolumn** (string) - Data column(s) to process.
   - **mode** (string) - Regridding mode (channel/velocity/frequency/channel_b).
   - **phasecenter** (variant) - Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
   - **restfreq** (string) - Rest frequency to use for output.
   - **outframe** (string) - Output reference frame.
   - **veltype** (string) - Velocity definition.
   - **hanning** (bool) - Hanning smooth data to remove Gibbs ringing.

Subparameters
   .. raw:: html

      <details><summary><i> mode = channel </i></summary>

   - **nchan** (int=-1) - Number of channels in the output spw
   - **start** (variant=0) - First input channel to use
   - **width** (variant=1) - Channel width of the output visibilities.
   - **interpolation** (string=linear) - Spectral interpolation method

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> mode = channel_b </i></summary>

   - **nchan** (int=-1) - Number of channels in the output spw
   - **start** (variant=0) - First input channel to use
   - **width** (variant=1) - Channel width of the output visibilities.
   - **interpolation** (string=linear) - Spectral interpolation method

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> mode = velocity </i></summary>

   - **nchan** (int=-1) - Number of channels in the output spw
   - **start** (variant='') - First input channel to use
   - **width** (variant='') - Channel width of the output visibilities.
   - **interpolation** (string=linear) - Spectral interpolation method

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> mode = frequency </i></summary>

   - **nchan** (int=-1) - Number of channels in the output spw
   - **start** (variant='') - First input channel to use
   - **width** (variant='') - Channel width of the output visibilities.
   - **interpolation** (string=linear) - Spectral interpolation method

   .. raw:: html

      </details>


Description
      .. note:: ALERT: **cvel2** is currently an experimental task and will
         replace the current **cvel** in the near future. We will then
         remove current **cvel** and rename **cvel2** to **cvel**.

      The intent of **cvel2** is to transform channel labels and the
      visibilities to a spectral reference frame which is appropriate
      for the science analysis, e.g. from TOPO to LSRK to correct for
      Doppler shifts throughout the time of the observation. **cvel2**
      is based on **mstransform**.

      VLA and ALMA datasets are observed in TOPOcentric velocity frames
      with fixed sky frequencies that are calculated from the
      observatory velocity at the start of the observation, and kept
      throughout (Doppler setting). The data will need to be regridded
      to a constant velocity grid to avoid a smearing of spectral
      features (e.g. to the LSRK or BARYcentric velocity frames,
      see `Spectral Line
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/spectral-line-imaging>`__).
      **cvel2** can perform this operation. Naturally, the
      transformation of channel labels and visibilities into a different
      reference frame will change the shape of the spectral feature to
      some extent. According to the Nyquist theorem you should
      oversample a spectrum with twice the numbers of channels to retain
      the shape. We advise that for spectral regridding to a standard
      velocity system like LSRK or BARY the expected spectral features
      are oversampled at least by a factor of 3-4 of the linewidth to
      preserve the spectral shape and to minimize regridding artifacts. 

      **cvel2** is in fact a more general tasks that
      transforms visibilities between spectral frames for
      visibilities. Doppler correction is also applied during imaging
      with **tclean,** which is recommended for most cases. **cvel2** is
      still useful if the MS itself needs to be stored in a specific
      frame, e.g. for self-calibration on fixed velocity channels. An MS
      that was regridded using **cvel2** can be imaged in *channel* mode
      in **tclean** (although **tclean** will perform some internal
      regridding anyways). 

      .. rubric:: Gridding modes and parameters
         :name: gridding-modes-and-parameters

      **cvel2** offers four gridding *mode* s: '*channel'*,
      '*velocity'*, '*frequency'*, and '*channel_b'*. All of the modes
      have the same four subparameters *nchan*, *start*, *width*, and
      *interpolation*.  *nchan* is the number of channels for all modes.
      The meaning and units of the parameters *start* and *width* depend
      on the gridding mode used:

      -  For the modes '*channel'* and '*channel_b'*, *start* is the
         input starting channel, and *width* the number of input
         channels to be merged into a single output channel.
      -  In *velocity* and *frequency* mode, *start* defines the first
         channel of the output grid and *width* the width of each
         channel in the output in velocity or frequency units,
         respectively.

      Negative *width* numbers run the channel sequence in the opposite
      direction.

      The difference between '*channel*' and '*channel_b*' is that
      '*channel*' forces the output to be on an equidistant grid based
      on first selected channel, whereas '*channel_b*' does not (which
      improves the speed of **cvel2**). Mode '*velocity'* also requires
      the specification of a rest frequency (*restfreq* parameter,
      and definition type ('*radio*' or '*optical*') in the
      *veltype* parameter. See also the relevant sections of the
      `Spectral Line
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/spectral-line-imaging>`__ and
      `Spectral
      Frames <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/spectral-frames>`__ chapters. 

      *interpolation* specifies the interpolation method between the
      spectral channels. The interpolation method '*fftshift'*
      calculates the transformed visibilities by applying a FFT, then a
      phase ramp, and then an inverse FFT. It will also perform
      pre-averaging, if necessary for the output grid (this will also
      increase the S/N). Note that if you want to use this interpolation
      method, your frequency grid needs to be equidistant, i.e. it only
      works in mode velocity with *veltype='radio'*, in mode
      '*frequency'*, and in mode '*channel'* (in the latter only if the
      input grid is itself equidistant in frequency). Note also that, as
      opposed to all other interpolation methods, this method will apply
      a constant (frequency independent) shift in frequency which is not
      fully correct in the case of large fractional bandwidth of the
      given spectral window

      The *phasecenter* parameter can be used to specify the field id or
      position that is used for the transformations. This can be useful
      for larger mosaics.

      Hanning smoothing is optionally offered in **cvel2**, but tests
      have shown that already the regridding process itself, if it
      involved a transformation from TOPO to a non-terrestrial reference
      frame, implies some smoothing (due to channel interpolation) such
      that Hanning smoothing may not be necessary.

      If **cvel2** has already established the grid that is desired for
      the imaging,
      `tclean <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean>`__
      should be run with exactly the same frequency/velocity parameters
      as used in **cvel2** in order to avoid additional regridding in
      clean.

      .. rubric:: Multi-MS support
         :name: multi-ms-support

      The option *keepmms* is set by default. This implies that unless
      the value of *keepmms* is explicitly changed to False, **cvel2**
      will create a Multi-MS when the input is a Multi-MS. The output
      Multi-MS will keep the same partition axis of the input MMS. See
      the task
      `partition <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_partition>`__
      for more information on the Multi-MS (MMS) format. **NOTE**: It is
      not possible to combine the spws if the input MMS was partitioned
      with separationaxis='spw'. In this case, the task will abort with
      an error.

      .. rubric:: cvel and cvel2
         :name: cvel-and-cvel2

      **cvel2** replicates the functionality of **cvel**, although the
      following differences should be noted:

      -  The regridding calculations of **cvel2** have been modified in
         order to better align it with the regridding calculations of
         tclean. Also, **cvel2** will not perform a pre-average step
         automatically when the width of the output channels is more
         than twice the widtch of the input channels.
      -  **cvel2** also supports Multi-MS input, in which case it will
         create an output Multi-MS too.
      -  The parameter *passall* is not supported in **cvel2**. The user
         may achieve the same results of passall=True by splitting out
         the data that will not be regridded with **cvel2** and
         concatenate regridded and non-regridded sets at the end. In the
         case of Multi-MS input, the user should use virtualconcat to
         achieve a concatenated MMS.
      -  **cvel2** is based on and implemented in terms of the very
         general
         `mstransform <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_mstransform>`__
         framework (mstransform
         `tool <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_mstransformer>`__
         and
         `task <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_mstransform>`__).

    """
    pass
