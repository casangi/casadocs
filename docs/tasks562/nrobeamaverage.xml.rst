nrobeamaverage -- Average SD data over beams and do time averaging -- single dish task
=======================================

Description
---------------------------------------

    
    The task nrobeamaverage is for Nobeyama dataset of ON-ON observations.
    It averages on-source spectra having specified beam IDs over specified 
    time bins. 
    



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
     - 
   * - datacolumn
     - :code:`'float_data'`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - beam
     - :code:`''`
     - 
   * - timebin
     - :code:`'0s'`
     - 
   * - outfile
     - :code:`''`
     - 


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

select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)


timerange
---------------------------------------

:code:`''`

select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. "21~23" (""=all)


beam
---------------------------------------

:code:`''`

beam IDs to be averaged over, e.g. "1,3" (""=all)


timebin
---------------------------------------

:code:`'0s'`

bin width for time averaging.


outfile
---------------------------------------

:code:`''`

name of output file




