split -- Create a visibility subset from an existing visibility set -- manipulation task
=======================================

Description
---------------------------------------

-----------------------------------------------------------------------------
           This is the new implementation of split. 

* The old implementation is available for a short time as oldsplit.
* Task split2 has been renamed to split. The split2 alias will be removed soon.
* Please, update your scripts to call split instead.
-----------------------------------------------------------------------------

This new split task uses the MSTransform framework underneath.
Split is the general purpose program to make a new data set that is a
subset or averaged form of an existing data set.  General selection
parameters are included, and one or all of the various data columns
(DATA, LAG_DATA and/or FLOAT_DATA, MODEL_DATA and/or
CORRECTED_DATA) can be selected.

Split is often used after the initial calibration of the data to make a
smaller Measurement Set with only the data that will be used in
further flagging, imaging and/or self-calibration.  Split can
average over frequency (channels) and time (integrations).
	
Split also supports the Multi-MS (MMS) format as input. For more information about MMS, 
see the help of partition and mstransform.
	



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
     - :code:`'corrected'`
     - 
   * - keepflags
     - :code:`True`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - timebin
     - :code:`'0s'`
     - 
   * - combine
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input Measurement set or Multi-MS


outputvis
---------------------------------------

:code:`''`

Name of output Measurement set or Multi-MS


keepmms
---------------------------------------

:code:`True`

If the input is a Multi-MS the output will also be a Multi-MS.


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

Correlation: '' ==> all, correlation="XX,YY".


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

:code:`'corrected'`

Which data column(s) to process.


keepflags
---------------------------------------

:code:`True`

Keep *completely flagged rows* instead of dropping them.


width
---------------------------------------

:code:`int(1)`

Number of channels to average to form one output channel


timebin
---------------------------------------

:code:`'0s'`

Bin width for time averaging


combine
---------------------------------------

:code:`''`

Span the timebin across scan, state or both




