

.. _Description:

Description
   .. warning:: **ALERT:** The task **cvel** will soon be replaced by the
      functionality (and underlying code) currently offered by
      **cvel2. cvel2** is using the mstransform framework for optimal
      performance and will be renamed **cvel** after complete
      validation of all modes in the near future. See below and also
      the discussion on the **cvel2** task page for differences
      between **cvel** and **cvel2**.
      
   .. warning:: There are `Known Issues <../../notebooks/introduction.html#Known-Issues>`__ for cvel.
   
   VLA and ALMA datasets are observed in TOPOcentric velocity frames
   with fixed sky frequencies that are calculated from the
   observatory velocity at the start of the observation, and kept
   throughout (Doppler setting). The data will need to be regridded
   to a constant velocity grid to avoid a smearing of spectral
   features (e.g. to the LSRK or BARYcentric velocity frames,
   see `Spectral Line
   Imaging <../../notebooks/synthesis_imaging.ipynb#Spectral-Line-Imaging>`__).
   **cvel** can perform this operation. We advise that for spectral
   regridding to a standard velocity system like LSRK or BARY the
   expected spectral features are oversampled at least by a factor of
   3-4 of the linewidth to preserve the spectral shape and to avoid
   regridding artifacts.  
   
   **cvel** is in fact a more general tasks that
   transforms visibilities between spectral frames for
   visibilities. Doppler correction is also applied during imaging
   with **tclean**, which is recommended for most cases. **cvel** is
   still useful if the MS itself needs to be stored in a specific
   frame, e.g. for self-calibration on fixed velocity channels. An MS
   that was regridded using **cvel** can be imaged in *channel* mode
   in **tclean** (although **tclean** will perform some internal
   regridding anyways). 
   
   .. rubric:: Gridding modes and parameters

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
   Imaging <../../notebooks/synthesis_imaging.ipynb#Spectral-Line-Imaging>`__ and
   `Spectral
   Frames <../../notebooks/memo-series.ipynb#Spectral-Frames>`__ chapters.
   
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

   Development of cvel has stopped. For a more up to date version
   please see task **cvel2**. The regridding calculations of
   **cvel2** have been modified in order to better align it with
   regridding in **tclean**. Also, **cvel2** will not perform a
   pre-average step automatically when the width of the output
   channels is more than twice the widtch of the input channels.
   

.. _Examples:

Examples
   **Example 1:**
   
   Regrid 'myMS.ms' to a new 'myMSregridded.ms' using veolicty mode
   and a LSRK radio velocity definition.  The output data has a
   structure of 10 channels, starting at 123 km/s with a width of
   0.1km/s. We use the HI rest frequency of 1.420405752 GHz. 
   
   ::
   
      cvel(vis='myMS.ms', outputvis='myMSregridded.ms',
      outframe='LSRK', mode='velocity', veltype='radio',
      restfreq='1.420405752GHz', nchan=10, start='123km/s',
      width='0.1km/s')
   
   **Example 2:**
   
   Regrid the same MS, but this time using channel mode. We start at
   channel 5, and create 10 new output channels, grouping 7 channels
   in the new bins. We also run the output MS in reverse spectral
   order (note the negative value of width). This time we request a
   BARYcentric frame and use the interpolation method 'fftshift'.
   
   ::
   
      cvel(vis='myMS.ms', outputvis='myMSregridded.ms',
      outframe='BARY',  mode='channel', nchan=10, start=5, width=-7,
      interpolation='fftshift')
   

.. _Development:

Development
   No additional development details

