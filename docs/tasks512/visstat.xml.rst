visstat -- Displays statistical information from a Measurement Set, or from a Multi-MS -- information task
=======================================

Description
---------------------------------------



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
   * - axis
     - :code:`'amplitude'`
     - 
   * - datacolumn
     - :code:`'data'`
     - 
   * - useflags
     - :code:`True`
     - 
   * - spw
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - selectdata
     - :code:`True`
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
   * - array
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - timeaverage
     - :code:`False`
     - 
   * - timebin
     - :code:`'0s'`
     - 
   * - timespan
     - :code:`''`
     - 
   * - maxuvwdistance
     - :code:`float(0.0)`
     - 
   * - disableparallel
     - :code:`False`
     - 
   * - ddistart
     - :code:`int(-1)`
     - 
   * - taql
     - :code:`''`
     - 
   * - monolithic_processing
     - :code:`False`
     - 
   * - intent
     - :code:`''`
     - 
   * - reportingaxes
     - :code:`'ddid'`
     - 
   * - xstat
     - :code:`[ ]`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of Measurement Set or Multi-MS


axis
---------------------------------------

:code:`'amplitude'`

Which values to use


datacolumn
---------------------------------------

:code:`'data'`

Which data column to use (data, corrected, model, float_data)


useflags
---------------------------------------

:code:`True`

Take flagging into account?


spw
---------------------------------------

:code:`''`

spectral-window/frequency/channel


field
---------------------------------------

:code:`''`

Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'


selectdata
---------------------------------------

:code:`True`

More data selection parameters (antenna, timerange etc)


antenna
---------------------------------------

:code:`''`

antenna/baselines: \'\'==>all, antenna = \'3,VA04\'


uvrange
---------------------------------------

:code:`''`

uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters


timerange
---------------------------------------

:code:`''`

time range: \'\'==>all, timerange=\'09:14:0~09:54:0\'


correlation
---------------------------------------

:code:`''`

Select data based on correlation


scan
---------------------------------------

:code:`''`

scan numbers: \'\'==>all


array
---------------------------------------

:code:`''`

(sub)array numbers: \'\'==>all


observation
---------------------------------------

:code:`''`

observation ID number(s): \'\' = all


timeaverage
---------------------------------------

:code:`False`

Average data in time.


timebin
---------------------------------------

:code:`'0s'`

Bin width for time averaging.


timespan
---------------------------------------

:code:`''`

Span the timebin across scan, state or both.


maxuvwdistance
---------------------------------------

:code:`float(0.0)`

Maximum separation of start-to-end baselines that can be included in an average. (meters)


disableparallel
---------------------------------------

:code:`False`

Hidden parameter for internal use only. Do not change it!


ddistart
---------------------------------------

:code:`int(-1)`

Hidden parameter for internal use only. Do not change it!


taql
---------------------------------------

:code:`''`

Table query for nested selections


monolithic_processing
---------------------------------------

:code:`False`

Hidden parameter for internal use only. Do not change it!


intent
---------------------------------------

:code:`''`

Select data by scan intent.


reportingaxes
---------------------------------------

:code:`'ddid'`

Which reporting axis to use (ddid, field, integration)


xstat
---------------------------------------

:code:`[ ]`

Statistical information for the selected measurement set




