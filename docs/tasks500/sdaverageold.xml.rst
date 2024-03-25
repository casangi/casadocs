sdaverageold -- ASAP SD task [DEPRECATED]: averaging and smoothing of spectra -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
To a very great extent, the functionality of this task with MeasurementSet
format is replicated with sdsmooth and mstransform.
#########################################################################

Task sdaverageold performs averaging in time/polarization and smoothing
of the single-dish spectra. When timeaverage=True, spectra are averaged
in time. Spectra within each scan ID are averaged when scanaverage=True.
When polaverage=True, spectra are averaged in polarization and time
(Note time averaging with polaverage=True would be discarded in future).
See examples in below for details of time/polarization average.
When kernel is specified (!=\'\'), each spectrum is smoothed by
convolving the kernel after averaging of spectra.

If you give multiple IFs (spectral windows) in spw, then your scantable
will have multiple IFs by default. Averaging of multi-resolution
(multi-IFs) spectra can be achieved by setting a sub-parameter in
timeaverage, averageall = True. It handles multi-IFs by merging IFs
which have overlaps in frequency coverages and assigning new IFs in
the output spectra.

Set plotlevel >= 1 to plot spectrum before and after smoothing, and
verify=True to interactively select whether or not accept smoothing
results.
NOTE, so far, there is no mechanism to verify averaging of spectra in time
and/or polarization.



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
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
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
     - :code:`''`
     - type of spectral smoothing kernel [\'hanning\', \'gaussian\', \'boxcar\', \'regrid\'] (\'\'=no smoothing)
   * - kwidth
     - :code:`int(5)`
     - 
   * - chanwidth
     - :code:`'5'`
     - 
   * - verify
     - :code:`False`
     - 
   * - plotlevel
     - :code:`int(0)`
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


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\'=all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)


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

average spectra over time [True, False] (see examples in help)


tweight
---------------------------------------

:code:`'tintsys'`

weighting for time averaging


scanaverage
---------------------------------------

:code:`False`

average spectra within a scan number [True, False] (see examples in help)


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

:code:`''`

type of spectral smoothing kernel  (\'\'=no smoothing)


kwidth
---------------------------------------

:code:`int(5)`

width of smoothing kernel in channels


chanwidth
---------------------------------------

:code:`'5'`

width of regridded channels


verify
---------------------------------------

:code:`False`

interactively verify the results of smoothing for each spectrum. [not available for kernel="regrid"]


plotlevel
---------------------------------------

:code:`int(0)`

plot and summarize results (0=none). See description in help


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




