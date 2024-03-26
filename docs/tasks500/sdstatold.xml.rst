sdstatold -- ASAP SD task [DEPRECATED]: list statistics of spectral -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
The functionality of this task with MeasurementSet format is replicated
with visstat2.
#########################################################################

Task sdstatold computes basic statistics for each of single-dish spectrum.
This task returns a Python dictionary of statistics. The return value
contains the maximum and minimum intensity and their channels ('max',
'max_abscissa', 'min', and 'min_abscissa'), RMS ('rms'), mean ('mean'),
sum ('sum'), median ('median'), standard deviation ('stddev'), total
intensity ('totint'), and equivalent width ('eqw').
If you do have multiple scantable rows, then the return values will
be lists.

It is possible to select channel regions to calculate spectra either
non-interactively by spw parameter or interactively on a plotter by
setting interactive=True.

If one of averaging parameters is set True, the spectra are averaged
before calculating the statistics.



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
   * - beam
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
   * - polaverage
     - :code:`False`
     - 
   * - pweight
     - :code:`'tsys'`
     - weighting for polarization averaging [\'tsys\' or \'var\']
   * - interactive
     - :code:`False`
     - 
   * - outfile
     - :code:`''`
     - 
   * - format
     - :code:`'3.3f'`
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


beam
---------------------------------------

:code:`''`

select data by beam IDs, e.g. \'0,1\' (\'\'=all)


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


polaverage
---------------------------------------

:code:`False`

average spectra over polarizations [True, False]


pweight
---------------------------------------

:code:`'tsys'`

weighting for polarization averaging 


interactive
---------------------------------------

:code:`False`

determines interactive masking [True, False]


outfile
---------------------------------------

:code:`''`

name of output file (ASCII) to save statistics


format
---------------------------------------

:code:`'3.3f'`

format string to print statistic values in file, e.g, \'.7e\'


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists


xstat
---------------------------------------

:code:`[ ]`

RETURN ONLY: a Python dictionary of line statistics




