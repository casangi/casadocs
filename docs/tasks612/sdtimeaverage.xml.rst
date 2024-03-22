sdtimeaverage -- Average SD data, perform time averaging -- single dish task
=======================================

Description
---------------------------------------

    
    The task sdtimeaverage is an SD task for averaging spectral data
    over specified time range.    
    



Parameters
---------------------------------------
.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   * - Parameter
     - Default
     - Description
   * - infile
     - :code:`''`
     - name of input SD dataset
   * - datacolumn
     - :code:`'float_data'`
     - name of data column to be used ["data", "float_data", or "corrected_data"]
   * - field
     - :code:`''`
     - select data by field IDs and names, e.g. "3C2*" (""=all)
   * - spw
     - :code:`''`
     - select data by spectral windows and channels, e.g. "3,5,7" (""=all)
   * - timerange
     - :code:`''`
     - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   * - scan
     - :code:`''`
     - select data by scan numbers, e.g. "21~23" (""=all)
   * - antenna
     - :code:`''`
     - antenna IDs to be averaged over, e.g. "PM03" (""=all)
   * - timebin
     - :code:`'all'`
     - bin width for time averaging.
   * - timespan
     - :code:`'scan'`
     - span across scan, state or both.
   * - outfile
     - :code:`''`
     - name of output file


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset


datacolumn
---------------------------------------

:code:`'float_data'`

name of data column to be used ["data", "float_data", or "corrected_data"]


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. "3C2*" (""=all)


spw
---------------------------------------

:code:`''`

select data by spectral windows and channels, e.g. "3,5,7" (""=all)


timerange
---------------------------------------

:code:`''`

select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. "21~23" (""=all)


antenna
---------------------------------------

:code:`''`

antenna IDs to be averaged over, e.g. "PM03" (""=all)


timebin
---------------------------------------

:code:`'all'`

bin width for time averaging.


timespan
---------------------------------------

:code:`'scan'`

span across scan, state or both.


outfile
---------------------------------------

:code:`''`

name of output file




