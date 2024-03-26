cvel -- regrid an MS to a new spectral window / channel structure or frame -- manipulation task
=======================================

Description
---------------------------------------

The intent of cvel is to transform channel labels and the 
visibilities to a spectral reference frame which is appropriate
for the science analysis, e.g. from TOPO to LSRK to correct for 
Doppler shifts throughout the time of the observation. Naturally, 
this will change the shape of the spectral feature to some extent. 
According to the Nyquist theorem you should oversample a spectrum 
with twice the numbers of channels to retain the shape. Based on 
some tests, however, we recommend to observe with at least 
3-4 times the number of channels for each significant spectral 
feature (like 3-4 times the linewidth). This will minimize 
regridding artifacts in cvel.

If cvel has already established the grid that is desired for the
imaging, clean should be run with exactly the same frequency/velocity 
parameters as used in cvel in order to avoid additional regridding in 
clean.

Hanning smoothing is optionally offered in cvel, but tests have 
shown that already the regridding process itself, if it involved 
a transformation from TOPO to a non-terrestrial reference frame, 
implies some smoothing (due to channel interpolation) such that 
Hanning smoothing may not be necessary.



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
     - Name of input measurement set
   * - outputvis
     - :code:`''`
     - Name of output measurement set
   * - passall
     - :code:`False`
     - Pass through (write to output MS) non-selected data with no change
   * - field
     - :code:`''`
     - Select field using field id(s) or field name(s)
   * - spw
     - :code:`''`
     - Select spectral window/channels
   * - selectdata
     - :code:`True`
     - Other data selection parameters
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - timerange
     - :code:`''`
     - Range of time to select from data
   * - scan
     - :code:`''`
     - scan number range
   * - array
     - :code:`''`
     - (sub)array indices
   * - mode
     - :code:`'channel'`
     - Regridding mode
   * - nchan
     - :code:`int(-1)`
     - Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
   * - start
     - :code:`int(0)`
     - Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
   * - width
     - :code:`int(1)`
     - Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
   * - interpolation
     - :code:`'linear'`
     - Spectral interpolation method
   * - phasecenter
     - :code:`''`
     - Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
   * - restfreq
     - :code:`''`
     - rest frequency (see help)
   * - outframe
     - :code:`''`
     - Output frame (not case-sensitive, \'\'=keep input frame)
   * - veltype
     - :code:`'radio'`
     - velocity definition
   * - hanning
     - :code:`False`
     - If true, Hanning smooth data before regridding to remove Gibbs ringing.


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input measurement set


outputvis
---------------------------------------

:code:`''`

Name of output measurement set


passall
---------------------------------------

:code:`False`

Pass through (write to output MS) non-selected data with no change


field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


selectdata
---------------------------------------

:code:`True`

Other data selection parameters


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


timerange
---------------------------------------

:code:`''`

Range of time to select from data


scan
---------------------------------------

:code:`''`

scan number range


array
---------------------------------------

:code:`''`

(sub)array indices


mode
---------------------------------------

:code:`'channel'`

 Regridding mode 


nchan
---------------------------------------

:code:`int(-1)`

Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.


start
---------------------------------------

:code:`int(0)`

Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.


width
---------------------------------------

:code:`int(1)`

Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.


interpolation
---------------------------------------

:code:`'linear'`

Spectral interpolation method


phasecenter
---------------------------------------

:code:`''`

Phase center direction to be used for the spectral coordinate transformation: direction measure or field index


restfreq
---------------------------------------

:code:`''`

rest frequency (see help)


outframe
---------------------------------------

:code:`''`

Output frame (not case-sensitive, \'\'=keep input frame)


veltype
---------------------------------------

:code:`'radio'`

velocity definition


hanning
---------------------------------------

:code:`False`

 If true, Hanning smooth data before regridding to remove Gibbs ringing.




