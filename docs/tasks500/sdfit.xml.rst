sdfit -- Fit a spectral line -- single dish task
=======================================

Description
---------------------------------------

Task sdfit is a basic line-fitter for single-dish spectra.
It assumes that the spectra have been calibrated in tsdcal
or sdreduce.
  


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
   * - timebin
     - :code:`''`
     - 
   * - timespan
     - :code:`''`
     - 
   * - polaverage
     - :code:`''`
     - 
   * - fitfunc
     - :code:`'gaussian'`
     - function for fitting [\'gaussian\', \'lorentzian\']
   * - fitmode
     - :code:`'list'`
     - mode for setting additional channel masks. \'list\' and \'auto\' are available now.
   * - nfit
     - :code:`numpy.array( [ int(0) ] )`
     - 
   * - thresh
     - :code:`float(5.0)`
     - 
   * - avg_limit
     - :code:`int(4)`
     - 
   * - minwidth
     - :code:`int(4)`
     - 
   * - edge
     - :code:`numpy.array( [ int(0),int(0) ] )`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - xstat
     - :code:`[ ]`
     - 


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset


datacolumn
---------------------------------------

:code:`'data'`

name of data column to be used [\'data\', \'float_data\', or \'corrected_data\']


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

select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)


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

select data by polarization IDs, e.g. \'XX,YY\' (\'\'=all)


intent
---------------------------------------

:code:`''`

select data by observational intent, e.g. \'*ON_SOURCE*\' (\'\'=all)


timebin
---------------------------------------

:code:`''`

bin width for time averaging


timespan
---------------------------------------

:code:`''`

span the timebin across \'scan\', \'state\', \'field\', or a combination of them (e.g., \'scan,state\')


polaverage
---------------------------------------

:code:`''`

polarization averaging mode (\'\', \'stokes\' or \'geometric\').


fitfunc
---------------------------------------

:code:`'gaussian'`

function for fitting


fitmode
---------------------------------------

:code:`'list'`

mode for setting additional channel masks.


nfit
---------------------------------------

:code:`numpy.array( [ int(0) ] )`

list of number of lines to fit in maskline region.


thresh
---------------------------------------

:code:`float(5.0)`

S/N threshold for linefinder


avg_limit
---------------------------------------

:code:`int(4)`

channel averaging for broad lines


minwidth
---------------------------------------

:code:`int(4)`

the minimum channel width to detect as a line


edge
---------------------------------------

:code:`numpy.array( [ int(0),int(0) ] )`

channels to drop at beginning and end of spectrum


outfile
---------------------------------------

:code:`''`

name of output file


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists


xstat
---------------------------------------

:code:`[ ]`

RETURN ONLY: a Python dictionary of line statistics




