cvel2 -- Regrid an MS or MMS to a new spectral window, channel structure or frame -- manipulation task
=======================================

Description
---------------------------------------

The intent of cvel2 is to transform channel labels and the 
visibilities to a spectral reference frame which is appropriate
for the science analysis, e.g. from TOPO to LSRK to correct for 
Doppler shifts throughout the time of the observation. Naturally, 
this will change the shape of the spectral feature to some extent. 
According to the Nyquist theorem you should oversample a spectrum 
with twice the numbers of channels to retain the shape. Based on 
some tests, however, we recommend to observe with at least 
3-4 times the number of channels for each significant spectral 
feature (like 3-4 times the linewidth). This will minimize 
regridding artifacts in cvel2.

If cvel2 has already established the grid that is desired for the
imaging, clean should be run with exactly the same frequency/velocity 
parameters as used in cvel2 in order to avoid additional regridding in 
clean.

Hanning smoothing is optionally offered in cvel2, but tests have 
shown that already the regridding process itself, if it involved 
a transformation from TOPO to a non-terrestrial reference frame, 
implies some smoothing (due to channel interpolation) such that 
Hanning smoothing may not be necessary.
    
This version of cvel2 also supports Multi-MS input, in which case it
will create an output Multi-MS too.
    
NOTE:
    The parameter passall is not supported in cvel2. The user may achieve
    the same results of passall=True by splitting out the data that will not
    be regridded with cvel2 and concatenate regridded and non-regridded sets 
    at the end. In the case of Multi-MS input, the user should use virtualconcat 
    to achieve a concatenated MMS.
    
    



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
     - 
   * - outputvis
     - :code:`''`
     - 
   * - keepmms
     - :code:`True`
     - 
   * - passall
     - :code:`False`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - feed
     - :code:`''`
     - 
   * - datacolumn
     - :code:`'all'`
     - 
   * - mode
     - :code:`'channel'`
     - 
   * - nchan
     - :code:`int(-1)`
     - 
   * - start
     - :code:`int(0)`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - interpolation
     - :code:`'linear'`
     - 
   * - phasecenter
     - :code:`''`
     - 
   * - restfreq
     - :code:`''`
     - 
   * - outframe
     - :code:`''`
     - 
   * - veltype
     - :code:`'radio'`
     - 
   * - hanning
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input Measurement set or Multi-MS.


outputvis
---------------------------------------

:code:`''`

Name of output Measurement Set or Multi-MS.


keepmms
---------------------------------------

:code:`True`

If the input is a Multi-MS the output will also be a Multi-MS.


passall
---------------------------------------

:code:`False`

HIDDEN parameter. Pass through (write to output MS) non-selected data with no change


field
---------------------------------------

:code:`''`

Select field using ID(s) or name(s).


spw
---------------------------------------

:code:`''`

Select spectral window/channels.


scan
---------------------------------------

:code:`''`

Select data by scan numbers.


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline.


correlation
---------------------------------------

:code:`''`

Correlation: \'\' ==> all, correlation=\'XX,YY\'.


timerange
---------------------------------------

:code:`''`

Select data by time range.


intent
---------------------------------------

:code:`''`

Select data by scan intent.


array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number.


uvrange
---------------------------------------

:code:`''`

Select data by baseline length.


observation
---------------------------------------

:code:`''`

Select by observation ID(s).


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


nchan
---------------------------------------

:code:`int(-1)`

Number of channels in the output spw (-1=all).


start
---------------------------------------

:code:`int(0)`

First channel to use in the output spw (mode-dependant).


width
---------------------------------------

:code:`int(1)`

Number of input channels that are used to create an output channel.


interpolation
---------------------------------------

:code:`'linear'`

Spectral interpolation method


phasecenter
---------------------------------------

:code:`''`

Image phase center: position or field index


restfreq
---------------------------------------

:code:`''`

Rest frequency to use for output.


outframe
---------------------------------------

:code:`''`

Output reference frame (\'\'=keep input frame).


veltype
---------------------------------------

:code:`'radio'`

Velocity definition.


hanning
---------------------------------------

:code:`False`

Hanning smooth data to remove Gibbs ringing.




