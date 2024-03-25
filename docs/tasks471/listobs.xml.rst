listobs -- List the summary of a data set in the logger or in a file -- information task
=======================================

Description
---------------------------------------

       List the summary information of a data set in the logger or in a file, based on
       a data selection. Only rows can be selected and printed. No in-row selection is
       possible (channel or correlation).

       Lists the following properties of a measurement set:
       scan list, field list, spectral window list with
       correlators, antenna locations, ms table information.
	


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
   * - selectdata
     - :code:`True`
     - 
   * - spw
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - feed
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - verbose
     - :code:`True`
     - 
   * - listfile
     - :code:`''`
     - 
   * - listunfl
     - :code:`False`
     - 
   * - cachesize
     - :code:`float(50)`
     - 
   * - overwrite
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


selectdata
---------------------------------------

:code:`True`

Data selection parameters


spw
---------------------------------------

:code:`''`

spectral-window/frequency/channel


field
---------------------------------------

:code:`''`

Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'


antenna
---------------------------------------

:code:`''`

antenna/baselines: \'\'==>all, antenna =\'3,VA04\'


uvrange
---------------------------------------

:code:`''`

uv range: \'\'==>all; uvrange =\'0~100klambda\', default units=meters


timerange
---------------------------------------

:code:`''`

time range: \'\'==>all,timerange=\'09:14:0~09:54:0\'


correlation
---------------------------------------

:code:`''`

Select data based on correlation


scan
---------------------------------------

:code:`''`

scan numbers: \'\'==>all


intent
---------------------------------------

:code:`''`

Select data based on observation intent: \'\'==>all


feed
---------------------------------------

:code:`''`

multi-feed numbers: Not yet implemented


array
---------------------------------------

:code:`''`

(sub)array numbers: \'\'==>all


observation
---------------------------------------

:code:`''`

Select data based on observation ID: \'\'==>all


verbose
---------------------------------------

:code:`True`




listfile
---------------------------------------

:code:`''`

Name of disk file to write output: \'\'==>to terminal


listunfl
---------------------------------------

:code:`False`

List unflagged row counts? If true, it can have significant negative performance impact.


cachesize
---------------------------------------

:code:`float(50)`

EXPERIMENTAL. Maximum size in megabytes of cache in which data structures can be held.


overwrite
---------------------------------------

:code:`False`

If True, tacitly overwrite listfile if it exists.




