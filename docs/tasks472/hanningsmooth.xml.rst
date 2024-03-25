hanningsmooth -- Hanning smooth frequency channel data to remove Gibbs ringing -- manipulation task
=======================================

Description
---------------------------------------


-----------------------------------------------------------------------------
           This is the new implementation of hanningsmooth. 

* The old implementation is available for a short time as oldhanningsmooth.
* Task hanningsmooth2 has been renamed to hanningsmooth. The hanningsmooth2 alias 
  will be removed soon.
* Please, update your scripts to call hanningsmooth instead.
-----------------------------------------------------------------------------

		
    Th new hanningsmooth task uses the MSTransform framework underneath
    but keeps roughly the same interface as the old hanningsmooth task.
			
    This function Hanning smooths the frequency channels with
    a weighted running average. The weights are 0.5 for the central 
    channel and 0.25 for each of the two adjacent channels. The first 
    and last channels are flagged. Inclusion of a flagged value in an 
    average causes that data value to be flagged. 
				
    If the 'CORRECTED' data column is requested for an MS that does not contain this column, 
    it will use 'DATA' to calculate the smoothing and save it to 'DATA' in the output MS.
    
    WARNING: by default, all visibility columns will be smoothed. 




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
     - :code:`'all'`
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

Name of output Measurement set or Multi-MS.


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

Input data column(s) to process.




