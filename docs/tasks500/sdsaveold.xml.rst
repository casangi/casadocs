sdsaveold -- ASAP SD task [DEPRECATED]: Save the sd spectra in various format -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
Import of single dish data to MeasurementSet is supported by importasap 
(Scantable), importatca (ATCA RPFITS), and importnro (NRO NOSTAR).
However, there is no facility to export from MeasurementSet to these
formats (see plotms for export to ASCII).
#########################################################################

Task sdsaveold writes the single dish data to a disk file in 
specified format (ASAP, MS2, SDFITS, ASCII). It is possible to 
save the subset of the data by selecting field names, spw ids,
time ranges, scan numbers, and polarization ids. The ASAP
(scantable) format is recommended for further analysis using Sd
tool or tasks except imaging. For further imaging using imager
or sdimaging, save the data to the Measurement Set
(MS2).
  


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
   * - splitant
     - :code:`False`
     - split output file by antenna [True, False]
   * - antenna
     - :code:`int(0)`
     - 
   * - getpt
     - :code:`True`
     - fill DIRECTION column properly [True, False]
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
   * - beam
     - :code:`''`
     - 
   * - restfreq
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - outform
     - :code:`'ASAP'`
     - output file format [\'ASAP\', \'MS2\', \'ASCII\', or \'SDFITS\']
   * - fillweight
     - :code:`False`
     - fill the WEIGHT and SIGMA columns for output MS [True, False]
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset


splitant
---------------------------------------

:code:`False`

split output file by antenna (only effective for MS input)


antenna
---------------------------------------

:code:`int(0)`

select an antenna name or ID, e.g. \'PM03\' (only effective for MS input)


getpt
---------------------------------------

:code:`True`

fill DIRECTION column properly (True), or reuse POINTING table in original MS (False) (only effective for MS input)


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

select data by polarization IDs, e.g. \'0,1\' (\'\'=all)


beam
---------------------------------------

:code:`''`

select data by beam IDs, e.g. \'0,1\' (\'\'=all)


restfreq
---------------------------------------

:code:`''`

the rest frequency, e.g. \'1.41GHz\' (default unit: Hz) (see examples in help)


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


outform
---------------------------------------

:code:`'ASAP'`

output file format (See a WARNING in help)


fillweight
---------------------------------------

:code:`False`

fill the WEIGHT and SIGMA columns for output MS


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists




