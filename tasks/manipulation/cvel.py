#
# stub function definition file for docstring parsing
#

def cvel(vis, outputvis='', passall=False, field='', spw='', selectdata=True, antenna='', timerange='', scan='', array='', mode='channel', nchan=-1, start='0', width='1', interpolation='linear', phasecenter='', restfreq='', outframe='', veltype='radio', hanning=False):
    r"""
regrid an MS to a new spectral window / channel structure or frame

Parameters
   - **vis** (string) - Name of input measurement set
   - **outputvis** (string) - Name of output measurement set
   - **passall** (bool) - Pass through (write to output MS) non-selected data with no change
   - **field** (string, stringArray, int, intArray) - Select field using field id(s) or field name(s)
   - **spw** (string, stringArray, int, intArray) - Select spectral window/channels
   - **selectdata** (bool) - Other data selection parameters
   - **mode** (string) -  Regridding mode 
   - **phasecenter** (variant) - Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
   - **restfreq** (string) - rest frequency (see help)
   - **outframe** (string) - Output frame (not case-sensitive, \'\'=keep input frame)
   - **veltype** (string) - velocity definition
   - **hanning** (bool) -  If true, Hanning smooth data before regridding to remove Gibbs ringing.

Subparameters
   *selectdata = True*

   - **timerange** (string='') - Range of time to select from data
   - **array** (string='') - (sub)array indices
   - **antenna** (string='') - Select data based on antenna/baseline
   - **scan** (string='') - scan number range

   *mode = channel*

   - **nchan** (int=-1) - Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
   - **start** (variant=0) - Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
   - **width** (variant=1) - Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
   - **interpolation** (string=linear) - Spectral interpolation method

   *mode = channel_b*

   - **nchan** (int=-1) - Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
   - **start** (variant=0) - Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
   - **width** (variant=1) - Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
   - **interpolation** (string=linear) - Spectral interpolation method

   *mode = velocity*

   - **nchan** (int=-1) - Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
   - **start** (variant='') - Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
   - **width** (variant='') - Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
   - **interpolation** (string=linear) - Spectral interpolation method

   *mode = frequency*

   - **nchan** (int=-1) - Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
   - **start** (variant='') - Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
   - **width** (variant='') - Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
   - **interpolation** (string=linear) - Spectral interpolation method


Description
      .. note:: **ALERT: ** The task **cvel** will soon be replaced by the
         functionality (and underlying code) currently offered by
         **cvel2. cvel2** is using the mstransform framework for optimal
         performance and will be renamed **cvel** after complete
         validation of all modes in the near future. See below and also
         the discussion on the **cvel2** task page for differences
         between **cvel** and **cvel2**.

      VLA and ALMA datasets are observed in TOPOcentric velocity frames
      with fixed sky frequencies that are calculated from the
      observatory velocity at the start of the observation, and kept
      throughout (Doppler setting). The data will need to be regridded
      to a constant velocity grid to avoid a smearing of spectral
      features (e.g. to the LSRK or BARYcentric velocity frames,
      see `Spectral Line
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/spectral-line-imaging>`__).
      **cvel** can perform this operation. We advise that for spectral
      regridding to a standard velocity system like LSRK or BARY the
      expected spectral features are oversampled at least by a factor of
      3-4 of the linewidth to preserve the spectral shape and to avoid
      regridding artifacts.  

      **cvel** is in fact a more general tasks that
      transforms visibilities between spectral frames for
      visibilities. Doppler correction is also applied during imaging
      with **tclean,** which is recommended for most cases. **cvel** is
      still useful if the MS itself needs to be stored in a specific
      frame, e.g. for self-calibration on fixed velocity channels. An MS
      that was regridded using **cvel** can be imaged in *channel* mode
      in **tclean** (although **tclean** will perform some internal
      regridding anyways). 

      .. rubric:: Gridding modes and parameters
         :name: gridding-modes-and-parameters

      **cvel** offers four gridding *mode* s: '*channel'*,
      '*velocity'*, '*frequency'*, and '*channel_b'*. All of the modes
      have the same four subparameters *nchan*, *start*, *width*, and
      *interpolation*.  *nchan* is the number of channels for all
      modes.The meaning and units of the parameter *start* and *width*
      depend on the gridding mode used:

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
      improves the speed of **cvel**). Mode '*velocity'* also requires
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
      pre-averaging, if necessary for the requested output grid (this
      will also increase the S/N). Note that if you want to use this
      interpolation method, your frequency grid needs to be equidistant,
      i.e. it only works in mode velocity with *veltype='radio'*, in
      mode '*frequency'*, and in mode '*channel'* (in the latter only if
      the input grid is itself equidistant in frequency). Note also
      that, as opposed to all other interpolation methods, this method
      will apply a constant (frequency independent) shift in frequency
      which is not fully correct in the case of large fractional
      bandwidth of the given spectral window

      The *phasecenter* parameter can be used to specify the field id or
      position that is used for the transformations. This can be useful
      for larger mosaics.

      Hanning smoothing is optionally offered in **cvel**, but tests
      have shown that already the regridding process itself, if it
      involved a transformation from TOPO to a non-terrestrial reference
      frame, implies some smoothing (due to channel interpolation) such
      that Hanning smoothing may not be necessary.

      .. rubric:: cvel and cvel2
         :name: cvel-and-cvel2

      Development of cvel has stopped. For a more up to date version
      please see task **cvel2**. The regridding calculations of
      **cvel2** have been modified in order to better align it with
      regridding in **tclean**. Also, **cvel2** will not perform a
      pre-average step automatically when the width of the output
      channels is more than twice the widtch of the input channels.

    """
    pass
