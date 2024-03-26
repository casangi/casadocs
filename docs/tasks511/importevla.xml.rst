importevla -- Convert an Science Data Model observation into a CASA Measurement Set -- import/export task
=======================================

Description
---------------------------------------



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - asdm
     - :code:`''`
     - 
   * - vis
     - :code:`''`
     - 
   * - ocorr_mode
     - :code:`'co'`
     - 
   * - compression
     - :code:`False`
     - 
   * - asis
     - :code:`''`
     - 
   * - scans
     - :code:`''`
     - 
   * - verbose
     - :code:`False`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - online
     - :code:`True`
     - 
   * - tbuff
     - :code:`float(0.0)`
     - 
   * - flagzero
     - :code:`True`
     - 
   * - flagpol
     - :code:`True`
     - 
   * - shadow
     - :code:`True`
     - 
   * - tolerance
     - :code:`float(0.0)`
     - 
   * - addantenna
     - :code:`''`
     - 
   * - applyflags
     - :code:`False`
     - 
   * - savecmds
     - :code:`False`
     - 
   * - outfile
     - :code:`''`
     - 
   * - flagbackup
     - :code:`True`
     - 
   * - polyephem_tabtimestep
     - :code:`float(0.001)`
     - 


Parameter Explanations
=======================================



asdm
---------------------------------------

:code:`''`

Name of input asdm directory (on disk)


vis
---------------------------------------

:code:`''`

Root name of the ms to be created. Note the .ms is NOT added 


ocorr_mode
---------------------------------------

:code:`'co'`

Fill correlation mode AUTO_ONLY (ao), CROSS_ONLY (co) or CROSS_AND_AUTO (ca)


compression
---------------------------------------

:code:`False`

Flag for turning on data compression


asis
---------------------------------------

:code:`''`

Create verbatim copies of these SDM tables in the MS.


scans
---------------------------------------

:code:`''`

List of scans to fill (default is all scans).


verbose
---------------------------------------

:code:`False`

Output lots of information while the filler is working


overwrite
---------------------------------------

:code:`False`

Over write an existing MS


online
---------------------------------------

:code:`True`

Create online flags


tbuff
---------------------------------------

:code:`float(0.0)`

Time padding buffer (in seconds)


flagzero
---------------------------------------

:code:`True`

Create flag commands for zero points


flagpol
---------------------------------------

:code:`True`

Create flag commands for cross-hand correlations


shadow
---------------------------------------

:code:`True`

Create flag commands for shadowed data


tolerance
---------------------------------------

:code:`float(0.0)`

Amount of shadow allowed (in meters)


addantenna
---------------------------------------

:code:`''`

File name or dictionary with additional antenna names, positions and diameters


applyflags
---------------------------------------

:code:`False`

Apply flag commands to MS


savecmds
---------------------------------------

:code:`False`

Save flag commands to an ASCII file


outfile
---------------------------------------

:code:`''`

Name of ASCII file to save flag commands


flagbackup
---------------------------------------

:code:`True`

Back up flag column before applying flags


polyephem_tabtimestep
---------------------------------------

:code:`float(0.001)`

Timestep (days) for the tabulation of polynomial ephemerides. A value <= 0 disables tabulation.




