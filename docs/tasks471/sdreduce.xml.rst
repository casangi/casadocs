sdreduce -- ASAP SD task: do sdcal, sdaverage, and sdbaseline in one task -- single dish task
=======================================

Description
---------------------------------------

Task sdreduce performs data selection, calibration, spectral averaging
and/or baseline fitting for single-dish spectra. This task internally
calls the tasks, sdcal, sdaverage, and sdbaseline and it can be used to
run all the three steps in one task execution. This task has better
performance than invoking the three tasks separately because it runs all
three steps without writing intermediate data to disk.

It is possible to skip arbitrary operations by setting calmode = 'none'
(for calibration), average=False (for time and polarization averaging),
kernel = 'none' (for smoothing), and/or blfunc='none' (for baseline
fitting).

Please take a look at descriptions of tasks, sdcal, sdaverage, and
sdbalseline, for more information.



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
   * - calmode
     - :code:`'none'`
     - SD calibration mode [\'ps\', \'nod\', \'otf\', \'otfraster\', \'fs\', \'fsotf\' or \'none\'] (\'none\' = skip calibration)
   * - fraction
     - :code:`'10%'`
     - 
   * - noff
     - :code:`int(-1)`
     - number of the OFF data to mark, e.g., 10 (-1 = use fraction instead of number)
   * - width
     - :code:`float(0.5)`
     - 
   * - elongated
     - :code:`False`
     - the observed area is elongated in one direction [True, False]
   * - markonly
     - :code:`False`
     - 
   * - plotpointings
     - :code:`False`
     - plot pointing directions for ON and OFF [True, False]
   * - tau
     - :code:`float(0.0)`
     - 
   * - average
     - :code:`False`
     - 
   * - timeaverage
     - :code:`False`
     - 
   * - tweight
     - :code:`'tintsys'`
     - weighting for time averaging [\'tintsys\', \'tsys\', \'tint\', \'var\', or \'median\']
   * - scanaverage
     - :code:`False`
     - 
   * - averageall
     - :code:`False`
     - 
   * - polaverage
     - :code:`False`
     - 
   * - pweight
     - :code:`'tsys'`
     - weighting for polarization averaging [\'tsys\' or \'var\']
   * - kernel
     - :code:`'none'`
     - type of spectral smoothing kernel [\'hanning\', \'gaussian\', \'boxcar\', \'regrid\'] (\'\'=no smoothing)
   * - kwidth
     - :code:`int(5)`
     - 
   * - chanwidth
     - :code:`'5'`
     - 
   * - maskmode
     - :code:`'auto'`
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
     - :code:`'none'`
     - baseline model function [\'poly\', \'chebyshev\', \'cspline\', \'sinusoid\' or \'none\'] (\'none\' = skip baseline fit)
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
     - method for automatically set wave numbers of sinusoids (only \'fft\' is available now)
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
   * - verifycal
     - :code:`False`
     - 
   * - verifysm
     - :code:`False`
     - 
   * - verifybl
     - :code:`False`
     - interactively verify the results of operation for each spectrum [True, False] (see description in help)
   * - verbosebl
     - :code:`True`
     - 
   * - bloutput
     - :code:`True`
     - 
   * - blformat
     - :code:`''`
     - format of the text file specified with bloutput [\'\' or \'csv\']
   * - showprogress
     - :code:`True`
     - 
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
     - 
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

parameters of telescope for flux conversion (see description in help of sdcal)


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

select data by time range, e.g. \'09:14:0~09:54:0\' (\'\'=all) (see examples in help of sdcal)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g. \'0,1\' (\'\'=all)


calmode
---------------------------------------

:code:`'none'`

SD calibration mode (\'none\' = skip calibration)


fraction
---------------------------------------

:code:`'10%'`

fraction of the OFF data to mark as OFF spectra, e.g., \'10%\'


noff
---------------------------------------

:code:`int(-1)`

number of the OFF data to mark (-1 = use fraction instead of number)


width
---------------------------------------

:code:`float(0.5)`

width of the pixel for edge detection


elongated
---------------------------------------

:code:`False`

the observed area is elongated in one direction


markonly
---------------------------------------

:code:`False`

do calibration (False) or just mark OFF (True)


plotpointings
---------------------------------------

:code:`False`

plot pointing direction for ON and OFF


tau
---------------------------------------

:code:`float(0.0)`

the zenith atmospheric optical depth for correction (0. = no correction)


average
---------------------------------------

:code:`False`

data averaging [True, False] 


timeaverage
---------------------------------------

:code:`False`

average spectra over time [True, False] (see examples in help of sdaverage)


tweight
---------------------------------------

:code:`'tintsys'`

weighting for time averaging


scanaverage
---------------------------------------

:code:`False`

average spectra within a scan number [True, False] (see examples in help of sdaverage)


averageall
---------------------------------------

:code:`False`

set True only when averaging spectra with different spectral resolutions


polaverage
---------------------------------------

:code:`False`

average spectra over polarizations [True, False]


pweight
---------------------------------------

:code:`'tsys'`

weighting for polarization averaging


kernel
---------------------------------------

:code:`'none'`

type of spectral smoothing kernel  (\'none\'=no smoothing)


kwidth
---------------------------------------

:code:`int(5)`

width of smoothing kernel in channels


chanwidth
---------------------------------------

:code:`'5'`

width of regridded channels


maskmode
---------------------------------------

:code:`'auto'`

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

:code:`'none'`

baseline model function  (\'none\' = skip baseline fit)


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

automatically set wave numbers of sinusoids [True, False]


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


verifycal
---------------------------------------

:code:`False`

interactively verify the results of calibration [True, False] (see description in sdcal)


verifysm
---------------------------------------

:code:`False`

interactively verify the results of smoothing for each spectrum. [not available for kernel="regrid"]


verifybl
---------------------------------------

:code:`False`

interactively verify the results of baseline fitting for each spectrum (only for blfunc="poly". see description in help)


verbosebl
---------------------------------------

:code:`True`

output baseline fitting results to logger [True, False]


bloutput
---------------------------------------

:code:`True`

output baseline fitting results to a text file [True, False]


blformat
---------------------------------------

:code:`''`

format of the text file specified with bloutput


showprogress
---------------------------------------

:code:`True`

show progress status for large data [True, False]


minnrow
---------------------------------------

:code:`int(1000)`

minimum number of input spectra to show progress status in baseline fitting


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

overwrite the output file if already exists  [True, False]


plotlevel
---------------------------------------

:code:`int(0)`

plot and summarize results (0=none). See description in each task




