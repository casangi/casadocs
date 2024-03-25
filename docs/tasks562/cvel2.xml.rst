cvel2 -- Regrid an MS or MMS to a new spectral window, channel structure or frame -- manipulation task
=======================================

Description
---------------------------------------

The intent of cvel2 is to transform channel labels and the
visibilities to a spectral reference frame which is appropriate for
the science analysis, e.g. from TOPO to LSRK to correct for Doppler
shifts throughout the time of the observation. Naturally, this will
change the shape of the spectral feature to some extent. According to
the Nyquist theorem you should oversample a spectrum with twice the
numbers of channels to retain the shape. Based on some tests, however,
we recommend to observe with at least 3-4 times the number of channels
for each significant spectral feature (like 3-4 times the
linewidth). This will minimize regridding artifacts in cvel2.

If cvel2 has already established the grid that is desired for the
imaging, tclean should be run with exactly the same frequency/velocity
parameters as used in cvel2 in order to avoid additional regridding in
clean.

Hanning smoothing is optionally offered in cvel2, but tests have shown
that already the regridding process itself, if it involved a
transformation from TOPO to a non-terrestrial reference frame, implies
some smoothing (due to channel interpolation) such that Hanning
smoothing may not be necessary.
   
This version of cvel2 also supports Multi-MS input, in which case it
will create an output Multi-MS too.

    NOTE:
    The parameter passall is not supported in cvel2. The user may
    achieve the same results of passall=True by splitting out the data
    that will not be regridded with cvel2 and concatenate regridded
    and non-regridded sets at the end. In the case of Multi-MS input,
    the user should use virtualconcat to achieve a concatenated MMS.    



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input visibility file
   * - outputvis
     - :code:`''`
     - Name of output visibility file
   * - keepmms
     - :code:`True`
     - Create a Multi-MS as the output if the input is a Multi-MS
   * - passall
     - :code:`False`
     - Hidden parameter
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - scan
     - :code:`''`
     - Scan number range
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - correlation
     - :code:`''`
     - Select data based on correlation
   * - timerange
     - :code:`''`
     - Select data based on time range
   * - intent
     - :code:`''`
     - Select observing intent
   * - array
     - :code:`''`
     - Select (sub)array(s) by array ID number.
   * - uvrange
     - :code:`''`
     - Select data by baseline length.
   * - observation
     - :code:`''`
     - Select by observation ID(s)
   * - feed
     - :code:`''`
     - Multi-feed numbers: Not yet implemented.
   * - datacolumn
     - :code:`'all'`
     - Data column(s) to process.
   * - mode
     - :code:`'channel'`
     - Regridding mode (channel/velocity/frequency/channel_b).
   * - nchan
     - :code:`int(-1)`
     - Number of channels in the output spw
   * - start
     - :code:`int(0)`
     - First input channel to use
   * - width
     - :code:`int(1)`
     - Channel width of the output visibilities.
   * - interpolation
     - :code:`'linear'`
     - Spectral interpolation method
   * - phasecenter
     - :code:`''`
     - Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
   * - restfreq
     - :code:`''`
     - Rest frequency to use for output.
   * - outframe
     - :code:`''`
     - Output reference frame.
   * - veltype
     - :code:`'radio'`
     - Velocity definition.
   * - hanning
     - :code:`False`
     - Hanning smooth data to remove Gibbs ringing.


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



outputvis
---------------------------------------

:code:`''`

Name of output visibility file or Multi-MS
                     Default: none

                        Example: vis='ngc5921_out.ms'



keepmms
---------------------------------------

:code:`True`

If the input is a Multi-MS the output will also be a
Multi-MS.
                     Default: True

                     By default it will create a Multi-MS when the
                     input is a Multi-MS. The output Multi-MS will
                     have the same partition axis of the input
                     MMS. See 'help partition' for more information on
                     the MMS format.

                     NOTE: It is not possible to combine the spws if
                     the input MMS was partitioned with
                     separationaxis='spw'. In this case, the task will
                     abort with an error.



passall
---------------------------------------

:code:`False`

HIDDEN parameter. Pass through (write to output MS) non-selected data with no change


field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative integer,
                     it is assumed a field index,  otherwise, it is
                     assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C



spw
---------------------------------------

:code:`''`

Select spectral window/channels
                     Default: ''=all spectral windows and channels
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.

                     NOTE: mstransform does not support multiple
                     channel ranges per spectral window.



scan
---------------------------------------

:code:`''`

Scan number range
                     Subparameter of selectdata=True
                     default: '' = all



antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     default: '' (all)

                     If antenna string is a non-negative integer, it
                     is assumed an antenna index, otherwise, it is
                     assumed as an antenna name
  
                         Examples: 
                         antenna='5&6'; baseline between antenna
                         index 5 and index 6.
                         antenna='VA05&VA06'; baseline between VLA
                         antenna 5 and 6.
                         antenna='5&6;7&8'; baselines with
                         indices 5-6 and 7-8
                         antenna='5'; all baselines with antenna index
                         5
                         antenna='05'; all baselines with antenna
                         number 05 (VLA old name)
                         antenna='5,6,10'; all baselines with antennas
                         5,6,10 index numbers
                         antenna='!ea03,ea12,ea17': all baselines
                         except those that include EVLA antennas ea03,
                         ea12, or ea17.



correlation
---------------------------------------

:code:`''`

Select data based on correlation
                     Default: '' (all)

                        Example: correlation='XX,YY'.



timerange
---------------------------------------

:code:`''`

Select data based on time range
                     Subparameter of selectdata=True
                     Default = '' (all)

                        Examples:
                        timerange =
                        'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                        (Note: if YYYY/MM/DD is missing date defaults
                        to first day in data set.)
                        timerange='09:14:0~09:54:0' picks 40 min on
                        first day 
                        timerange= '25:00:00~27:30:00' picks 1 hr to 3
                        hr 30min on NEXT day
                        timerange='09:44:00' pick data within one
                        integration of time
                        timerange='>10:24:00' data after this time



intent
---------------------------------------

:code:`''`

Select observing intent
                     Default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)



array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number.
                     Default = '' (all)



uvrange
---------------------------------------

:code:`''`

Select data by baseline length.


observation
---------------------------------------

:code:`''`

Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'



feed
---------------------------------------

:code:`''`

Multi-feed numbers: Not yet implemented.


datacolumn
---------------------------------------

:code:`'all'`

Which data column(s) to process.


mode
---------------------------------------

:code:`'channel'`

Regridding mode (channel/velocity/frequency/channel_b).
                     Default: 'channel'
                     Options: 'channel', 'velocity', 'frequency',
                     'channel_b'

                   * mode = 'channel'; Use with nchan, start, width to
                     specify output spw. Produces equidistant grid
                     based on first selected channel.
                   * mode = 'velocity', means channels are specified
                     in velocity.
                   * mode = 'frequency', means channels are specified
                     in frequency.
                   * mode = 'channel_b', alternative 'channel'
                     mode. Does not force an equidistant grid. Faster.

                        Examples: 
                        spw = '0,1'; mode = 'channel' will produce a
                        single spw containing all channels in spw 0
                        and 1
                        spw='0:5~28^2'; mode = 'channel' will produce
                        a single spw made with channels
                        (5,7,9,...,25,27)
                        spw = '0'; mode = 'channel': nchan=3; start=5;
                        width=4 will produce an spw with 3 output
                        channels
                        - new channel 1 contains data from channels
                        (5+6+7+8)
                        - new channel 2 contains data from channels
                        (9+10+11+12)
                        - new channel 3 contains data from channels
                        (13+14+15+16)
                        spw = '0:0~63^3'; mode='channel'; nchan=21;
                        start = 0; width = 1 will produce an spw with
                        21 channels
                        - new channel 1 contains data from channel 0
                        - new channel 2 contains data from channel 2
                        - new channel 21 contains data from channel 61
                        spw = '0:0~40^2'; mode = 'channel'; nchan = 3;
                        start = 5; width = 4 will produce an spw with
                        three output channels
                        - new channel 1 contains channels (5,7)
                        - new channel 2 contains channels (13,15)
                        - new channel 3 contains channels (21,23)



nchan
---------------------------------------

:code:`int(-1)`

Number of channels in the output spw (-1=all). 
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'                
                     Default: -1 = all channels

                     Used for regridding, together with 'start' and
                     'width'.

                        Example: nchan=3



start
---------------------------------------

:code:`int(0)`

Start or end input channel (zero-based), depending on the sign of the width parameter 
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'                

                     Used for regridding, together with 'width' and
                     'nchan'. It can be in different units, depending
                     on the regridding mode: 
                     - first input channel (mode='channel'), 
                     - first velocity (mode='velocity'), or 
                     - first frequency (mode='frequency'). 

                        Example values: '5', '0.0km/s', '1.4GHz', for
                        channel, velocity, and frequency modes,
                        respectively.



width
---------------------------------------

:code:`int(1)`

Channel width of the output visibilities. 
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'                

                     Used for regridding, together with 'start', and
                     'nchan'. It can be in different units, depending
                     on the regridding mode: number of input channels
                     (mode='channel'), velocity (mode='velocity'), or
                     frequency (mode='frequency'. 

                        Example values: '2', '1.0km/s', '1.0kHz', for
                        channel, velocity, and frequency modes,
                        respectively.

                     Note: the sign indicates whether the start
                     parameter is lower(+) or upper(-) end of the
                     range.



interpolation
---------------------------------------

:code:`'linear'`

Spectral interpolation method
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'
                     Default = 'linear'
                     Options: linear, nearest, cubic, spline, fftshift



phasecenter
---------------------------------------

:code:`''`

Phase center direction to be used for the spectral
coordinate transformation.
                     Default: '' (first selected field)
                     Options: FIELD_ID (int) or center coordinate measure (str).

                     Phase direction measure  or fieldid. To be used
                     in mosaics to indicate the center direction to be
                     used in the spectral coordinate transformation.

                        Examples: 
                        phasecenter=6
                        phasecenter='J2000 19h30m00 -40d00m00'



restfreq
---------------------------------------

:code:`''`

Rest frequency to use for output visibilities.
                     Default='' 

                     Occasionally it is necessary to set this (for
                     example some VLA spectral line data).  For
                     example for NH_3 (1,1) put
                     restfreq='23.694496GHz'



outframe
---------------------------------------

:code:`''`

Output reference frame (not case-sensitive).
                     Default: '' (keep original reference frame)
                     Options: LSRK, LSRD, BARY, GALACTO, LGROUP, CMB,
                     GEO, TOPO, or SOURCE 

                     SOURCE is meant for solar system work and
                     corresponds to GEO + radial velocity correction
                     for ephemeris objects.

                        Example: outframe='BARY'     



veltype
---------------------------------------

:code:`'radio'`

Definition of velocity (in mode)
                     Default = 'radio'



hanning
---------------------------------------

:code:`False`

Hanning smooth data to remove Gibbs ringing.
                     Default: False
                     Options: False|True





