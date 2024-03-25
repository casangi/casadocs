tsdsmooth -- Smooth spectral data -- single dish task
=======================================

Description
---------------------------------------

  Task tsdsmooth performs smoothing along spectral axis using user-specified 
  smoothing kernel. Currently gaussian and boxcar kernels are supported.
  


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
     - :code:`'data'`
     - 
   * - antenna
     - :code:`''`
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
   * - pol
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - kernel
     - :code:`'gaussian'`
     - 
   * - kwidth
     - :code:`int(5)`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset


datacolumn
---------------------------------------

:code:`'data'`

name of data column to be used [\'data\', \'float_data\', or \'corrected\']


antenna
---------------------------------------

:code:`''`

select data by antenna name or ID, e.g. \'PM03\'


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\'=all)


spw
---------------------------------------

:code:`''`

select data by spectral window IDs, e.g. \'3,5,7\' (\'\'=all)


timerange
---------------------------------------

:code:`''`

select data by time range, e.g. \'09:14:0~09:54:0\' (\'\'=all) (see examples in help)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g. \'0,1\' (\'\'=all)


intent
---------------------------------------

:code:`''`

select data by observational intent, e.g. \'*ON_SOURCE*\' (\'\'=all)


kernel
---------------------------------------

:code:`'gaussian'`

spectral smoothing kernel type


kwidth
---------------------------------------

:code:`int(5)`

smoothing kernel width in channel


outfile
---------------------------------------

:code:`''`

name of output file


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists




