sdbaseline2old -- ASAP SD task [DEPRECATED]: Fit/subtract a spectral baseline -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
To a very great extent, the functionality of this task with MeasurementSet
format is replicated with sdbaseline.
#########################################################################

Task sdbaseline2old performs baseline fitting/removal for single-dish spectra.
  


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
   * - row
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
   * - blmode
     - :code:`'subtract'`
     - 
   * - blparam
     - :code:`*UNKNOWN*`
     - 
   * - bltable
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - keeprows
     - :code:`False`
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


row
---------------------------------------

:code:`''`

select data by row IDs, e.g. \'3,5,7\' (\'\'=all)


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


blmode
---------------------------------------

:code:`'subtract'`

baselining mode (\'subtract\' or \'apply\')


blparam
---------------------------------------

:code:`*UNKNOWN*`

per spectrum fit parameters


bltable
---------------------------------------

:code:`''`

name of baseline table


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists


keeprows
---------------------------------------

:code:`False`

keep all rows of input scantable in output table [True, False] 




