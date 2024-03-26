sdfit -- Fit a spectral line -- single dish task
=======================================

Description
---------------------------------------

Task sdfit is a basic line-fitter for single-dish spectra.
It assumes that the spectra have been calibrated in sdcal
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
     - doppler convention [\'RADIO\', \'OPTICAL\', \'Z\', \'BETA\', or \'GAMMA\'] (\'\'=current).
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - timeaverage
     - :code:`False`
     - average spectra over time [True, False] (see examples in help)
   * - tweight
     - :code:`'tintsys'`
     - weighting for time averaging [\'tintsys\', \'tsys\', \'tint\', \'var\', or \'median\']
   * - scanaverage
     - :code:`False`
     - average spectra within a scan number [True, False] (see examples in help)
   * - polaverage
     - :code:`False`
     - average spectra over polarizations [True, False]
   * - pweight
     - :code:`'tsys'`
     - weighting for polarization averaging [\'tsys\' or \'var\']
   * - fitfunc
     - :code:`'gauss'`
     - function for fitting [\'gauss\', \'lorentz\']
   * - fitmode
     - :code:`'auto'`
     - mode for fitting [\'auto\', \'list\', or \'interact\']
   * - nfit
     - :code:`numpy.array( [  ] )`
     - 
   * - thresh
     - :code:`float(5.0)`
     - 
   * - min_nchan
     - :code:`int(3)`
     - 
   * - avg_limit
     - :code:`int(4)`
     - 
   * - box_size
     - :code:`float(0.2)`
     - 
   * - edge
     - :code:`numpy.array( [ int(0) ] )`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - plotlevel
     - :code:`int(0)`
     - 
   * - xstat
     - :code:`[ ]`
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


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g. \'0,1\' (\'\'=all)


timeaverage
---------------------------------------

:code:`False`

average spectra over time (see examples in help)


tweight
---------------------------------------

:code:`'tintsys'`

weighting for time averaging


scanaverage
---------------------------------------

:code:`False`

average spectra within a scan number (see examples in help)


polaverage
---------------------------------------

:code:`False`

average spectra over polarizations


pweight
---------------------------------------

:code:`'tsys'`

weighting for polarization averaging


fitfunc
---------------------------------------

:code:`'gauss'`

function for fitting


fitmode
---------------------------------------

:code:`'auto'`

mode for fitting


nfit
---------------------------------------

:code:`numpy.array( [  ] )`

list of number of gaussian/lorentzian lines to fit in in maskline region (ignored when fitmode="auto")


thresh
---------------------------------------

:code:`float(5.0)`

S/N threshold for linefinder


min_nchan
---------------------------------------

:code:`int(3)`

minimum number of consecutive channels for linefinder


avg_limit
---------------------------------------

:code:`int(4)`

channel averaging for broad lines


box_size
---------------------------------------

:code:`float(0.2)`

running mean box size


edge
---------------------------------------

:code:`numpy.array( [ int(0) ] )`

channels to drop at beginning and end of spectrum


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists


plotlevel
---------------------------------------

:code:`int(0)`

control for plotting of results (see examples in help)


xstat
---------------------------------------

:code:`[ ]`

RETURN ONLY: a Python dictionary of line statistics




