.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task cvel2 parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      outputvis : string

   Name of output visibility file or Multi-MS Default: none Example:
   vis='ngc5921_out.ms'

Example

.. container:: param

   .. container:: parameters2

      keepmms : bool = True

   If the input is a Multi-MS the output will also be a Multi-MS.
   Default: True By default it will create a Multi-MS when the input is
   a Multi-MS. The output Multi-MS will have the same partition axis of
   the input MMS. See 'help partition' for more information on the MMS
   format. NOTE: It is not possible to combine the spws if the input MMS
   was partitioned with separationaxis='spw'. In this case, the task
   will abort with an error.

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray int intArray

   Select field using field id(s) or field name(s) Default: '' (all
   fields) Use 'go listobs' to obtain the list id's or names. If field
   string is a non-negative integer, it is assumed a field index,
   otherwise, it is assumed a field name. Examples: field='0~2'; field
   ids 0,1,2 field='0,4,5~7'; field ids 0,4,5,6,7 field='3C286,3C295';
   field named 3C286 and 3C295 field = '3,4C*'; field id 3, all names
   starting with 4C

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray int intArray

   Select spectral window/channels Default: ''=all spectral windows and
   channels Examples: spw='0~2,4'; spectral windows 0,1,2,4 (all
   channels) spw='<2'; spectral windows less than 2 (i.e. 0,1)
   spw='0:5~61'; spw 0, channels 5 to 61 spw='0,10,3:3~45'; spw 0,10 all
   channels, spw 3 - chans 3 to 45. spw='0~2:2~6'; spw 0,1,2 with
   channels 2 through 6 in each. spw = '*:3~64' channels 3 through 64
   for all sp id's spw = ' :3~64' will NOT work. NOTE: mstransform does
   not support multiple channel ranges per spectral window.

Example

.. container:: param

   .. container:: parameters2

      scan : string stringArray int intArray

   Scan number range Subparameter of selectdata=True default: '' = all

Example

.. container:: param

   .. container:: parameters2

      antenna : string stringArray int intArray

   Select data based on antenna/baseline Subparameter of selectdata=True
   default: '' (all) If antenna string is a non-negative integer, it is
   assumed an antenna index, otherwise, it is assumed as an antenna name
   Examples: antenna='5&6'; baseline between antenna index 5 and index
   6. antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
   antenna='5&6;7&8'; baselines with indices 5-6 and 7-8 antenna='5';
   all baselines with antenna index 5 antenna='05'; all baselines with
   antenna number 05 (VLA old name) antenna='5,6,10'; all baselines with
   antennas 5,6,10 index numbers antenna='!ea03,ea12,ea17': all
   baselines except those that include EVLA antennas ea03, ea12, or
   ea17.

Example

.. container:: param

   .. container:: parameters2

      correlation : string stringArray

   Select data based on correlation Default: '' (all) Example:
   correlation='XX,YY'.

Example

.. container:: param

   .. container:: parameters2

      timerange : string stringArray int intArray

   Select data based on time range Subparameter of selectdata=True
   Default = '' (all) Examples: timerange =
   'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss' (Note: if YYYY/MM/DD is
   missing date defaults to first day in data set.)
   timerange='09:14:0~09:54:0' picks 40 min on first day timerange=
   '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
   timerange='09:44:00' pick data within one integration of time
   timerange='>10:24:00' data after this time

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray int intArray

   Select observing intent Default: '' (no selection by intent) Example:
   intent='*BANDPASS*' (selects data labelled with BANDPASS intent)

Example

.. container:: param

   .. container:: parameters2

      array : string stringArray int intArray

   Select (sub)array(s) by array ID number. Default = '' (all)

Example

.. container:: param

   .. container:: parameters2

      uvrange : string stringArray int intArray

   Select data by baseline length.

Example

.. container:: param

   .. container:: parameters2

      observation : string stringArray int intArray

   Select by observation ID(s) Subparameter of selectdata=True Default:
   '' = all Example: observation='0~2,4'

Example

.. container:: param

   .. container:: parameters2

      feed : string stringArray int intArray

   Multi-feed numbers: Not yet implemented.

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = all

   Which data column(s) to process.

Allowed Value(s)

all data corrected model data,model,corrected float_data lag_data
float_data,data lag_data,data

Example

.. container:: param

   .. container:: parameters2

      mode : string = channel

   Regridding mode (channel/velocity/frequency/channel_b). Default:
   'channel' Options: 'channel', 'velocity', 'frequency', 'channel_b' \*
   mode = 'channel'; Use with nchan, start, width to specify output spw.
   Produces equidistant grid based on first selected channel. \* mode =
   'velocity', means channels are specified in velocity. \* mode =
   'frequency', means channels are specified in frequency. \* mode =
   'channel_b', alternative 'channel' mode. Does not force an
   equidistant grid. Faster. Examples: spw = '0,1'; mode = 'channel'
   will produce a single spw containing all channels in spw 0 and 1
   spw='0:5~28^2'; mode = 'channel' will produce a single spw made with
   channels (5,7,9,...,25,27) spw = '0'; mode = 'channel': nchan=3;
   start=5; width=4 will produce an spw with 3 output channels - new
   channel 1 contains data from channels (5+6+7+8) - new channel 2
   contains data from channels (9+10+11+12) - new channel 3 contains
   data from channels (13+14+15+16) spw = '0:0~63^3'; mode='channel';
   nchan=21; start = 0; width = 1 will produce an spw with 21 channels -
   new channel 1 contains data from channel 0 - new channel 2 contains
   data from channel 2 - new channel 21 contains data from channel 61
   spw = '0:0~40^2'; mode = 'channel'; nchan = 3; start = 5; width = 4
   will produce an spw with three output channels - new channel 1
   contains channels (5,7) - new channel 2 contains channels (13,15) -
   new channel 3 contains channels (21,23)

Allowed Value(s)

channel velocity frequency channel_b

Example

.. container:: param

   .. container:: parameters2

      nchan : int = -1

   Number of channels in the output spw (-1=all). Subparameter of
   mode='channel|velocity|frequency|channel_b' Default: -1 = all
   channels Used for regridding, together with 'start' and 'width'.
   Example: nchan=3

Example

.. container:: param

   .. container:: parameters2

      start : undefined = 0

   Start or end input channel (zero-based), depending on the sign of the
   width parameter Subparameter of
   mode='channel|velocity|frequency|channel_b' Used for regridding,
   together with 'width' and 'nchan'. It can be in different units,
   depending on the regridding mode: - first input channel
   (mode='channel'), - first velocity (mode='velocity'), or - first
   frequency (mode='frequency'). Example values: '5', '0.0km/s',
   '1.4GHz', for channel, velocity, and frequency modes, respectively.

Example

.. container:: param

   .. container:: parameters2

      width : undefined = 1

   Channel width of the output visibilities. Subparameter of
   mode='channel|velocity|frequency|channel_b' Used for regridding,
   together with 'start', and 'nchan'. It can be in different units,
   depending on the regridding mode: number of input channels
   (mode='channel'), velocity (mode='velocity'), or frequency
   (mode='frequency'. Example values: '2', '1.0km/s', '1.0kHz', for
   channel, velocity, and frequency modes, respectively. Note: the sign
   indicates whether the start parameter is lower(+) or upper(-) end of
   the range.

Example

.. container:: param

   .. container:: parameters2

      interpolation : string = linear

   Spectral interpolation method Subparameter of
   mode='channel|velocity|frequency|channel_b' Default = 'linear'
   Options: linear, nearest, cubic, spline, fftshift

Allowed Value(s)

nearest linear cubic spline fftshift

Example

.. container:: param

   .. container:: parameters2

      phasecenter : undefined

   Phase center direction to be used for the spectral coordinate
   transformation. Default: '' (first selected field) Options: FIELD_ID
   (int) or center coordinate measure (str). Phase direction measure or
   fieldid. To be used in mosaics to indicate the center direction to be
   used in the spectral coordinate transformation. Examples:
   phasecenter=6 phasecenter='J2000 19h30m00 -40d00m00'

Example

.. container:: param

   .. container:: parameters2

      restfreq : string

   Rest frequency to use for output visibilities. Default=''
   Occasionally it is necessary to set this (for example some VLA
   spectral line data). For example for NH_3 (1,1) put
   restfreq='23.694496GHz'

Example

.. container:: param

   .. container:: parameters2

      outframe : string

   Output reference frame (not case-sensitive). Default: '' (keep
   original reference frame) Options: LSRK, LSRD, BARY, GALACTO, LGROUP,
   CMB, GEO, TOPO, or SOURCE SOURCE is meant for solar system work and
   corresponds to GEO + radial velocity correction for ephemeris
   objects. Example: outframe='BARY'

Allowed Value(s)

topo geo lsrk lsrd bary galacto lgroup cmb source

Example

.. container:: param

   .. container:: parameters2

      veltype : string = radio

   Definition of velocity (in mode) Default = 'radio'

Allowed Value(s)

optical radio

Example

.. container:: param

   .. container:: parameters2

      hanning : bool = False

   Hanning smooth data to remove Gibbs ringing. Default: False Options:
   False|True

Example

.. container:: section
   :name: viewlet-below-content-body
