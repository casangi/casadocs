sdcoadd -- Coadd multiple scantables into one -- single dish task
=======================================

Description
---------------------------------------

Task sdcoadd performs co-add multiple single dish spectral data given
by a list of spectral data file names in any of the following formats,
ASAP, MS2,SDFITS, and ASCII.
The units of line flux, the units of spectral axis, frame, and doppler
are assumed to be those of the first one in the infiles.

The task tries to combine spws according to a tolerance value specified
by the parameter freqtol. Default tolerance is '0Hz', which means spws
are combined only when spectral setup are the same. Note that, except
for first data in the infiles, spw is ignored if there are no corresponding
spectral data in the main table.

  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infiles
     - :code:`numpy.array( [  ] )`
     - 
   * - antenna
     - :code:`int(0)`
     - 
   * - freqtol
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - outform
     - :code:`'ASAP'`
     - output file format [\'ASAP\', \'MS2\', \'ASCII\', or \'SDFITS\'] (See a WARNING in help)
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False] (See a WARNING in help)


Parameter Explanations
=======================================



infiles
---------------------------------------

:code:`numpy.array( [  ] )`

list of names of input SD dataset


antenna
---------------------------------------

:code:`int(0)`

select an antenna name or ID, e.g. \'PM03\' (only effective for MS input)


freqtol
---------------------------------------

:code:`''`

Frequency shift tolerance for considering data as the same spwid


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

overwrite the output file if already exists (See a WARNING in help)




