sdbaseline -- Fit/subtract a spectral baseline -- single dish task
=======================================

Description
---------------------------------------

Task sdbaseline fits and/or subtracts baseline from single-dish spectra.
Given baseline parameters (baseline type, order, etc.), sdbaseline 
computes the best-fit baseline for each spectrum by least-square fitting 
method and, if you want, subtracts it. The best-fit baseline parameters 
(including baseline type, coefficients of basis functions, etc.) and 
other values such as residual rms can be saved in various formats 
including ascii text (in human-readable format or CSV format) or baseline 
table (a CASA table).
Sdbaseline has another mode to 'apply' a baseline table to a MS data; 
for each spectrum in MS, the best-fit baseline is reproduced from the 
baseline parameters stored in the given baseline table and subtracted. 
Putting 'fit' and 'subtract' into separate processes can be useful for 
pipeline processing for huge dataset.
  


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
   * - reindex
     - :code:`True`
     - Re-index indices in subtables based on data selection
   * - maskmode
     - :code:`'list'`
     - mode of setting additional channel masks
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
   * - blmode
     - :code:`'fit'`
     - 
   * - dosubtract
     - :code:`True`
     - 
   * - blformat
     - :code:`'text'`
     - format(s) of file(s) in which best-fit parameters are written
   * - bloutput
     - :code:`''`
     - 
   * - bltable
     - :code:`''`
     - 
   * - blfunc
     - :code:`'poly'`
     - baseline model function
   * - order
     - :code:`int(5)`
     - 
   * - npiece
     - :code:`int(2)`
     - 
   * - applyfft
     - :code:`True`
     - 
   * - fftmethod
     - :code:`'fft'`
     - method for automatically set wave numbers of sinusoids ["fft"]
   * - fftthresh
     - :code:`float(3.0)`
     - 
   * - addwn
     - :code:`*UNKNOWN*`
     - 
   * - rejwn
     - :code:`*UNKNOWN*`
     - 
   * - clipthresh
     - :code:`float(3.0)`
     - 
   * - clipniter
     - :code:`int(0)`
     - 
   * - blparam
     - :code:`''`
     - 
   * - verbose
     - :code:`False`
     - output fitting parameters to logger [True, False]
   * - showprogress
     - :code:`False`
     - (NOT SUPPORTED YET) show progress status for large data [True, False] (NOT SUPPORTED YET)
   * - minnrow
     - :code:`int(1000)`
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

name of data column to be used ["data", "float_data", or "corrected"]


antenna
---------------------------------------

:code:`''`

select data by antenna name or ID, e.g. "PM03"


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


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g. "XX,YY" (""=all)


intent
---------------------------------------

:code:`''`

select data by observational intent, e.g. "*ON_SOURCE*" (""=all)


reindex
---------------------------------------

:code:`True`

Re-index indices in subtables based on data selection. Ignored when blmode='apply'.


maskmode
---------------------------------------

:code:`'list'`

mode of setting additional channel masks. "list" and "auto" are available now.


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


blmode
---------------------------------------

:code:`'fit'`

baselining mode ["fit" or "apply"]


dosubtract
---------------------------------------

:code:`True`

subtract baseline from input data [True, False] 


blformat
---------------------------------------

:code:`'text'`

format(s) of file(s) in which best-fit parameters are written ["text", "csv", "table" or ""]


bloutput
---------------------------------------

:code:`''`

name(s) of file(s) in which best-fit parameters are written


bltable
---------------------------------------

:code:`''`

name of baseline table to apply


blfunc
---------------------------------------

:code:`'poly'`

baseline model function ["poly", "chebyshev", "cspline", "sinusoid", or "variable"(expert mode)]


order
---------------------------------------

:code:`int(5)`

order of baseline model function


npiece
---------------------------------------

:code:`int(2)`

number of element polynomials for cubic spline curve


applyfft
---------------------------------------

:code:`True`

automatically set wave numbers of sinusoids


fftmethod
---------------------------------------

:code:`'fft'`

method for automatically set wave numbers of sinusoids


fftthresh
---------------------------------------

:code:`float(3.0)`

threshold to select wave numbers of sinusoids


addwn
---------------------------------------

:code:`*UNKNOWN*`

additional wave numbers to use


rejwn
---------------------------------------

:code:`*UNKNOWN*`

wave numbers NOT to use


clipthresh
---------------------------------------

:code:`float(3.0)`

clipping threshold for iterative fitting


clipniter
---------------------------------------

:code:`int(0)`

maximum iteration number for iterative fitting


blparam
---------------------------------------

:code:`''`

text file that stores per spectrum fit parameters


verbose
---------------------------------------

:code:`False`

output fitting parameters to logger


showprogress
---------------------------------------

:code:`False`

(NOT SUPPORTED YET) show progress status for large data


minnrow
---------------------------------------

:code:`int(1000)`

(NOT SUPPORTED YET) minimum number of input spectra to show progress status


outfile
---------------------------------------

:code:`''`

name of output file


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists




