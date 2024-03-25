sdbaseline -- Fit/subtract a spectral baseline -- single dish task
=======================================

Description
---------------------------------------

Task sdbaseline performs baseline fitting/removal for single-dish spectra.
The fit parameters, terms and rms of base-line are saved to an ascii 
file, '<outfile>_blparam.txt'. 
  


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
   * - antenna
     - :code:`int(0)`
     - 
   * - fluxunit
     - :code:`''`
     - units of the flux [\'K\' or \'Jy\'] (\'\'=current)
   * - telescopeparam
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - restfreq
     - :code:`''`
     - 
   * - frame
     - :code:`''`
     - frequency reference frame [\'LSRK\', \'TOPO\', \'LSRD\', \'BARY\', \'GALACTO\', \'LGROUP\', or \'CMB\'] (\'\'=current)
   * - doppler
     - :code:`''`
     - doppler convention [\'RADIO\', \'OPTICAL\', \'Z\', \'BETA\', or \'GAMMA\'] (\'\'=current)
   * - timerange
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - tau
     - :code:`float(0.0)`
     - 
   * - maskmode
     - :code:`''`
     - mode of setting additional channel masks [\'auto\', \'list\', or \'interact\']
   * - thresh
     - :code:`float(5.0)`
     - 
   * - avg_limit
     - :code:`int(4)`
     - 
   * - edge
     - :code:`numpy.array( [ int(0) ] )`
     - 
   * - blfunc
     - :code:`'poly'`
     - baseline model function [\'poly\', \'chebyshev\', \'cspline\', or \'sinusoid\'
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
     - method for automatically set wave numbers of sinusoids [\'fft\']
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
   * - verify
     - :code:`False`
     - interactively verify the results of operation for each spectrum [True, False] (see description in help)
   * - verbose
     - :code:`True`
     - output fitting results to logger [True, False]
   * - bloutput
     - :code:`True`
     - output fitting results to a text file [True, False]
   * - blformat
     - :code:`''`
     - format of the text file specified with bloutput [\'\' or \'csv\']
   * - showprogress
     - :code:`True`
     - show progress status for large data [True, False]
   * - minnrow
     - :code:`int(1000)`
     - 
   * - outfile
     - :code:`''`
     - 
   * - outform
     - :code:`'ASAP'`
     - output file format [\'ASAP\', \'MS2\', \'ASCII\', or \'SDFITS\']
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - plotlevel
     - :code:`int(0)`
     - 


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset


antenna
---------------------------------------

:code:`int(0)`

select an antenna name or ID, e.g. \'PM03\' (only effective for MS input)


fluxunit
---------------------------------------

:code:`''`

units of the flux (\'\'=current)


telescopeparam
---------------------------------------

:code:`''`

parameters of telescope for flux conversion (see examples in help)


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\'=all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)


restfreq
---------------------------------------

:code:`''`

the rest frequency, e.g. \'1.41GHz\' (default unit: Hz) (see examples in help)


frame
---------------------------------------

:code:`''`

frequency reference frame (\'\'=current)


doppler
---------------------------------------

:code:`''`

doppler convention (\'\'=current). Effective only when spw selection is in velocity unit.


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


tau
---------------------------------------

:code:`float(0.0)`

the zenith atmospheric optical depth for correction


maskmode
---------------------------------------

:code:`''`

mode of setting additional channel masks


thresh
---------------------------------------

:code:`float(5.0)`

S/N threshold for linefinder


avg_limit
---------------------------------------

:code:`int(4)`

channel averaging for broad lines


edge
---------------------------------------

:code:`numpy.array( [ int(0) ] )`

channels to drop at beginning and end of spectrum


blfunc
---------------------------------------

:code:`'poly'`

baseline model function


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


verify
---------------------------------------

:code:`False`

interactively verify the results of operation for each spectrum (see description in help)


verbose
---------------------------------------

:code:`True`

output fitting results to logger


bloutput
---------------------------------------

:code:`True`

output fitting results to a text file


blformat
---------------------------------------

:code:`''`

format of the text file specified with bloutput


showprogress
---------------------------------------

:code:`True`

show progress status for large data


minnrow
---------------------------------------

:code:`int(1000)`

minimum number of input spectra to show progress status


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


outform
---------------------------------------

:code:`'ASAP'`

output file format (See a WARNING in help)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists


plotlevel
---------------------------------------

:code:`int(0)`

control for plotting of results (see examples in help)




