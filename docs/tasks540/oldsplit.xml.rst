oldsplit -- Create a visibility subset from an existing visibility set -- manipulation task
=======================================

Description
---------------------------------------


    T H I S   T A S K   I S    D E P R E C A T E D
    I T   W I L L   B E   R E M O V E D   S O O N

Oldsplit is the general purpose program to make a new data set that is a
subset or averaged form of an existing data set.  General selection
parameters are included, and one or all of the various data columns
(DATA, LAG_DATA and/or FLOAT_DATA, and possibly MODEL_DATA and/or
CORRECTED_DATA) can be selected.

Oldsplit is often used after the initial calibration of the data to make a
smaller measurement set with only the data that will be used in
further flagging, imaging and/or self-calibration.  Oldsplit can
average over frequency (channels) and time (integrations).




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
   * - datacolumn
     - :code:`'corrected'`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - antenna
     - :code:`''`
     - 
   * - timebin
     - :code:`'0s'`
     - 
   * - timerange
     - :code:`''`
     - 
   * - scan
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
   * - correlation
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - combine
     - :code:`''`
     - 
   * - keepflags
     - :code:`True`
     - 
   * - keepmms
     - :code:`False`
     - 


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


datacolumn
---------------------------------------

:code:`'corrected'`

Which data column(s) to Oldsplit out


field
---------------------------------------

:code:`''`

Select field using ID(s) or name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


width
---------------------------------------

:code:`int(1)`

Number of channels to average to form one output channel


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


timebin
---------------------------------------

:code:`'0s'`

Bin width for time averaging


timerange
---------------------------------------

:code:`''`

Select data by time range


scan
---------------------------------------

:code:`''`

Select data by scan numbers


intent
---------------------------------------

:code:`''`

Select data by scan intents


array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number


uvrange
---------------------------------------

:code:`''`

Select data by baseline length


correlation
---------------------------------------

:code:`''`

Select correlations


observation
---------------------------------------

:code:`''`

Select by observation ID(s)


combine
---------------------------------------

:code:`''`

Let time bins span changes in scan and/or state


keepflags
---------------------------------------

:code:`True`

If practical, keep *completely flagged rows* instead of dropping them.


keepmms
---------------------------------------

:code:`False`

If the input is a multi-MS, make the output one, too. (experimental)




