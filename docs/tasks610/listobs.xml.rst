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
     - Name of input visibility file (MS)
   * - selectdata
     - :code:`True`
     - Data selection parameters
   * - spw
     - :code:`''`
     - Selection based on spectral-window/frequency/channel.
   * - field
     - :code:`''`
     - Selection based on field names or field index numbers. Default is all.
   * - antenna
     - :code:`''`
     - Selection based on antenna/baselines. Default is all.
   * - uvrange
     - :code:`''`
     - Selection based on uv range. Default: entire range. Default units: meters.
   * - timerange
     - :code:`''`
     - Selection based on time range. Default is entire range.
   * - correlation
     - :code:`''`
     - Selection based on correlation. Default is all.
   * - scan
     - :code:`''`
     - Selection based on scan numbers. Default is all.
   * - intent
     - :code:`''`
     - Selection based on observation intent. Default is all.
   * - feed
     - :code:`''`
     - Selection based on multi-feed numbers: Not yet implemented
   * - array
     - :code:`''`
     - Selection based on (sub)array numbers. Default is all.
   * - observation
     - :code:`''`
     - Selection based on observation ID. Default is all.
   * - verbose
     - :code:`True`
     - Controls level of information detail reported. True reports more than False.
   * - listfile
     - :code:`''`
     - Name of disk file to write output. Default is none (output is written to logger only).
   * - listunfl
     - :code:`False`
     - List unflagged row counts? If true, it can have significant negative performance impact.
   * - cachesize
     - :code:`float(50)`
     - EXPERIMENTAL. Maximum size in megabytes of cache in which data structures can be held.
   * - overwrite
     - :code:`False`
     - If True, tacitly overwrite listfile if it exists.


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

Selection based on spectral-window/frequency/channel.


field
---------------------------------------

:code:`''`

Selection based on field names or field index numbers. Default is all.


antenna
---------------------------------------

:code:`''`

Selection based on antenna/baselines. Default is all.


uvrange
---------------------------------------

:code:`''`

Selection based on uv range. Default: entire range. Default units: meters.


timerange
---------------------------------------

:code:`''`

Selection based on time range. Default is entire range.


correlation
---------------------------------------

:code:`''`

Selection based on correlation. Default is all.


scan
---------------------------------------

:code:`''`

Selection based on scan numbers. Default is all.


intent
---------------------------------------

:code:`''`

Selection based on observation intent. Default is all.


feed
---------------------------------------

:code:`''`

Selection based on multi-feed numbers: Not yet implemented


array
---------------------------------------

:code:`''`

Selection based on (sub)array numbers. Default is all.


observation
---------------------------------------

:code:`''`

Selection based on observation ID. Default is all.


verbose
---------------------------------------

:code:`True`

Controls level of information detail reported. True reports more than False.


listfile
---------------------------------------

:code:`''`

Name of disk file to write output. Default is none (output is written to logger only).


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




