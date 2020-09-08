#
# stub function definition file for docstring parsing
#

def cvel2(vis, outputvis='', keepmms=True, passall=False, field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='all', mode='channel', nchan=-1, start='0', width='1', interpolation='linear', phasecenter='', restfreq='', outframe='', veltype='radio', hanning=False):
    r"""
Regrid an MS or MMS to a new spectral window, channel structure or frame

Parameters
   - vis_ (string) - Name of input visibility file
   - outputvis_ (string='') - Name of output visibility file
   - keepmms_ (bool=True) - Create a Multi-MS as the output if the input is a Multi-MS
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
   - datacolumn_ (string='all') - Data column(s) to process.
   - mode_ (string='channel') - Regridding mode (channel/velocity/frequency/channel_b).

      .. raw:: html

         <details><summary><i> mode = channel </i></summary>

      - nchan_ (int=-1) - Number of channels in the output spw
      - start_ (variant='0') - First input channel to use
      - width_ (variant='1') - Channel width of the output visibilities.
      - interpolation_ (string='linear') - Spectral interpolation method

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = channel_b </i></summary>

      - nchan_ (int=-1) - Number of channels in the output spw
      - start_ (variant='0') - First input channel to use
      - width_ (variant='1') - Channel width of the output visibilities.
      - interpolation_ (string='linear') - Spectral interpolation method

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = velocity </i></summary>

      - nchan_ (int=-1) - Number of channels in the output spw
      - start_ (variant='0') - First input channel to use
      - width_ (variant='1') - Channel width of the output visibilities.
      - interpolation_ (string='linear') - Spectral interpolation method

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = frequency </i></summary>

      - nchan_ (int=-1) - Number of channels in the output spw
      - start_ (variant='0') - First input channel to use
      - width_ (variant='1') - Channel width of the output visibilities.
      - interpolation_ (string='linear') - Spectral interpolation method

      .. raw:: html

         </details>
   - phasecenter_ (variant='') - Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
   - restfreq_ (string='') - Rest frequency to use for output.
   - outframe_ (string='') - Output reference frame.
   - veltype_ (string='radio') - Velocity definition.
   - hanning_ (bool=False) - Hanning smooth data to remove Gibbs ringing.


Description
   .. warning:: ALERT: **cvel2** is currently an experimental task and will
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
   see`Spectral Line
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/spectral-line-imaging>`__).
   **cvel2** can perform this operation.Naturally, the
   transformation of channel labels and visibilities into a different
   reference frame will change the shape of the spectral feature to
   some extent. According to the Nyquist theorem you should
   oversample a spectrum with twice the numbers of channels to retain
   the shape. We advise that for spectral regridding to a standard
   velocity system like LSRK or BARY the expected spectral features
   are oversampled at least by a factor of 3-4 of the linewidth to
   preserve the spectral shape and to minimize regridding artifacts.

   **cvel2** is in fact a more general tasks that
   transformsvisibilities betweenspectral frames for
   visibilities.Doppler correction is also applied during imaging
   with **tclean,** which is recommended for most cases. **cvel2** is
   still useful if the MS itself needs to be stored in a specific
   frame, e.g. for self-calibration on fixed velocity channels.An MS
   that was regridded using **cvel2** can be imaged in *channel* mode
   in **tclean** (although **tclean** will perform some internal
   regridding anyways).

   .. rubric:: Gridding modes and parameters
      

   **cvel2** offersfour gridding *mode* s: '*channel'*,
   '*velocity'*, '*frequency'*, and '*channel_b'*. All of the modes
   have the same four subparameters *nchan*,*start*, *width*, and
   *interpolation*. *nchan* is the number of channels for all modes.
   The meaning and units of the parameters *start* and *width* depend
   on the gridding mode used:

   -  For the modes '*channel'* and '*channel_b'*,*start* is the
      input starting channel, and *width* the number of input
      channels to be merged into a single output channel.
   -  In *velocity* and *frequency* mode, *start* defines the first
      channel of the output grid and *width* the width of each
      channel in the output in velocity or frequency units,
      respectively.

   Negative *width* numbers run the channel sequence in the opposite
   direction.

   The difference between '*channel*' and '*channel_b*' is that
   '*channel*' forces the output to be on anequidistant grid based
   on firstselected channel, whereas '*channel_b*' does not (which
   improves the speed of **cvel2**). Mode '*velocity'* also requires
   the specification of a rest frequency (*restfreq* parameter,
   anddefinitiontype ('*radio*' or '*optical*') in the
   *veltype*parameter. See also the relevant sections of the
   `Spectral Line
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/spectral-line-imaging>`__and
   `Spectral
   Frames <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/spectral-frames>`__chapters.

   *interpolation* specifies the interpolation method between the
   spectral channels.The interpolation method '*fftshift'*
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
   position that is used for the transformations. Thiscan be useful
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

   | Name of output visibility file or Multi-MS
   |                      Default: none
   | 
   |                         Example: vis='ngc5921_out.ms'

.. _keepmms:

   .. rubric:: keepmms

   | If the input is a Multi-MS the output will also be a
   | Multi-MS.
   |                      Default: True
   | 
   |                      By default it will create a Multi-MS when the
   |                      input is a Multi-MS. The output Multi-MS will
   |                      have the same partition axis of the input
   |                      MMS. See 'help partition' for more information on
   |                      the MMS format.
   | 
   |                      NOTE: It is not possible to combine the spws if
   |                      the input MMS was partitioned with
   |                      separationaxis='spw'. In this case, the task will
   |                      abort with an error.

.. _passall:

   .. rubric:: passall

   | HIDDEN parameter. Pass through (write to output MS) non-selected data with no change

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
   |                      channel ranges per spectral window.

.. _scan:

   .. rubric:: scan

   | Scan number range
   |                      Subparameter of selectdata=True
   |                      default: '' = all

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline
   |                      Subparameter of selectdata=True
   |                      default: '' (all)
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
   |                          antenna='!ea03,ea12,ea17': all baselines
   |                          except those that include EVLA antennas ea03,
   |                          ea12, or ea17.

.. _correlation:

   .. rubric:: correlation

   | Select data based on correlation
   |                      Default: '' (all)
   | 
   |                         Example: correlation='XX,YY'.

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

   | Select (sub)array(s) by array ID number.
   |                      Default = '' (all)

.. _uvrange:

   .. rubric:: uvrange

   | Select data by baseline length.

.. _observation:

   .. rubric:: observation

   | Select by observation ID(s)
   |                      Subparameter of selectdata=True
   |                      Default: '' = all
   | 
   |                          Example: observation='0~2,4'

.. _feed:

   .. rubric:: feed

   | Multi-feed numbers: Not yet implemented.

.. _datacolumn:

   .. rubric:: datacolumn

   | Which data column(s) to process.

.. _mode:

   .. rubric:: mode

   | Regridding mode (channel/velocity/frequency/channel_b).
   |                      Default: 'channel'
   |                      Options: 'channel', 'velocity', 'frequency',
   |                      'channel_b'
   | 
   |                    * mode = 'channel'; Use with nchan, start, width to
   |                      specify output spw. Produces equidistant grid
   |                      based on first selected channel.
   |                    * mode = 'velocity', means channels are specified
   |                      in velocity.
   |                    * mode = 'frequency', means channels are specified
   |                      in frequency.
   |                    * mode = 'channel_b', alternative 'channel'
   |                      mode. Does not force an equidistant grid. Faster.
   | 
   |                         Examples: 
   |                         spw = '0,1'; mode = 'channel' will produce a
   |                         single spw containing all channels in spw 0
   |                         and 1
   |                         spw='0:5~28^2'; mode = 'channel' will produce
   |                         a single spw made with channels
   |                         (5,7,9,...,25,27)
   |                         spw = '0'; mode = 'channel': nchan=3; start=5;
   |                         width=4 will produce an spw with 3 output
   |                         channels
   |                         - new channel 1 contains data from channels
   |                         (5+6+7+8)
   |                         - new channel 2 contains data from channels
   |                         (9+10+11+12)
   |                         - new channel 3 contains data from channels
   |                         (13+14+15+16)
   |                         spw = '0:0~63^3'; mode='channel'; nchan=21;
   |                         start = 0; width = 1 will produce an spw with
   |                         21 channels
   |                         - new channel 1 contains data from channel 0
   |                         - new channel 2 contains data from channel 2
   |                         - new channel 21 contains data from channel 61
   |                         spw = '0:0~40^2'; mode = 'channel'; nchan = 3;
   |                         start = 5; width = 4 will produce an spw with
   |                         three output channels
   |                         - new channel 1 contains channels (5,7)
   |                         - new channel 2 contains channels (13,15)
   |                         - new channel 3 contains channels (21,23)

.. _nchan:

   .. rubric:: nchan

   | Number of channels in the output spw (-1=all). 
   |                      Subparameter of
   |                      mode='channel|velocity|frequency|channel_b'                
   |                      Default: -1 = all channels
   | 
   |                      Used for regridding, together with 'start' and
   |                      'width'.
   | 
   |                         Example: nchan=3

.. _start:

   .. rubric:: start

   | Start or end input channel (zero-based), depending on the sign of the width parameter 
   |                      Subparameter of
   |                      mode='channel|velocity|frequency|channel_b'                
   | 
   |                      Used for regridding, together with 'width' and
   |                      'nchan'. It can be in different units, depending
   |                      on the regridding mode: 
   |                      - first input channel (mode='channel'), 
   |                      - first velocity (mode='velocity'), or 
   |                      - first frequency (mode='frequency'). 
   | 
   |                         Example values: '5', '0.0km/s', '1.4GHz', for
   |                         channel, velocity, and frequency modes,
   |                         respectively.

.. _width:

   .. rubric:: width

   | Channel width of the output visibilities. 
   |                      Subparameter of
   |                      mode='channel|velocity|frequency|channel_b'                
   | 
   |                      Used for regridding, together with 'start', and
   |                      'nchan'. It can be in different units, depending
   |                      on the regridding mode: number of input channels
   |                      (mode='channel'), velocity (mode='velocity'), or
   |                      frequency (mode='frequency'. 
   | 
   |                         Example values: '2', '1.0km/s', '1.0kHz', for
   |                         channel, velocity, and frequency modes,
   |                         respectively.
   | 
   |                      Note: the sign indicates whether the start
   |                      parameter is lower(+) or upper(-) end of the
   |                      range.

.. _interpolation:

   .. rubric:: interpolation

   | Spectral interpolation method
   |                      Subparameter of
   |                      mode='channel|velocity|frequency|channel_b'
   |                      Default = 'linear'
   |                      Options: linear, nearest, cubic, spline, fftshift

.. _phasecenter:

   .. rubric:: phasecenter

   | Phase center direction to be used for the spectral
   | coordinate transformation.
   |                      Default: '' (first selected field)
   |                      Options: FIELD_ID (int) or center coordinate measure (str).
   | 
   |                      Phase direction measure  or fieldid. To be used
   |                      in mosaics to indicate the center direction to be
   |                      used in the spectral coordinate transformation.
   | 
   |                         Examples: 
   |                         phasecenter=6
   |                         phasecenter='J2000 19h30m00 -40d00m00'

.. _restfreq:

   .. rubric:: restfreq

   | Rest frequency to use for output visibilities.
   |                      Default='' 
   | 
   |                      Occasionally it is necessary to set this (for
   |                      example some VLA spectral line data).  For
   |                      example for NH_3 (1,1) put
   |                      restfreq='23.694496GHz'

.. _outframe:

   .. rubric:: outframe

   | Output reference frame (not case-sensitive).
   |                      Default: '' (keep original reference frame)
   |                      Options: LSRK, LSRD, BARY, GALACTO, LGROUP, CMB,
   |                      GEO, TOPO, or SOURCE 
   | 
   |                      SOURCE is meant for solar system work and
   |                      corresponds to GEO + radial velocity correction
   |                      for ephemeris objects.
   | 
   |                         Example: outframe='BARY'

.. _veltype:

   .. rubric:: veltype

   | Definition of velocity (in mode)
   |                      Default = 'radio'

.. _hanning:

   .. rubric:: hanning

   | Hanning smooth data to remove Gibbs ringing.
   |                      Default: False
   |                      Options: False|True


    """
    pass
