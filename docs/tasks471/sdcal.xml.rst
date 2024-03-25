sdcal -- ASAP SD calibration task -- single dish task
=======================================

Description
---------------------------------------

Task sdcal performs calibration for single-dish spectra.
The parameter, calmode, defines calibration mode. The available
calibration modes are 'ps' (for position switching with explicit
reference scans), 'otfraster' (for raster OTF scan without explicit
reference scans), 'otf' (for non-raster OTF scan without explicit
reference scans, e.g, Lissajous, double circle), 'fs' (for frequency
switching), 'nod' (beam switching), and 'quotient' (for position
switching scans by ATNF telescopes).
The task selects appropriate calbiration equation based on the value
of calmode and telescope with which the data is taken. See below for 
details of calibration equation adopted in this task.

By setting calmode='none', one can run sdcal on already calibrated data
for atmospheric optical depth correction.



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
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - calmode
     - :code:`'ps'`
     - SD calibration mode [\'ps\', \'nod\', \'otf\', \'otfraster\', \'fs\', \'quotient\' or \'none\']
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
   * - verify
     - :code:`False`
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

select an antenna name or ID, e.g, \'PM03\' (only effective for MS input)


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


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g, \'21~23\' (\'\' = all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g, \'0,1\' (\'\' = all)


calmode
---------------------------------------

:code:`'ps'`

SD calibration mode


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


verify
---------------------------------------

:code:`False`

interactively verify the results of calibration [True, False] (see description in help)


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

plot and summarize results (0=none) see description in help




