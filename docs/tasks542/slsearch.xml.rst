slsearch -- Search a spectral line table. -- analysis task
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
   * - tablename
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - freqrange
     - :code:`numpy.array( [ float(84),float(90) ] )`
     - 
   * - species
     - :code:`numpy.array( [  ] )`
     - 
   * - reconly
     - :code:`False`
     - 
   * - chemnames
     - :code:`numpy.array( [  ] )`
     - 
   * - qns
     - :code:`numpy.array( [  ] )`
     - 
   * - intensity
     - :code:`numpy.array( [  ] )`
     - 
   * - smu2
     - :code:`numpy.array( [  ] )`
     - 
   * - loga
     - :code:`numpy.array( [  ] )`
     - 
   * - el
     - :code:`numpy.array( [  ] )`
     - 
   * - eu
     - :code:`numpy.array( [  ] )`
     - 
   * - rrlinclude
     - :code:`True`
     - 
   * - rrlonly
     - :code:`False`
     - 
   * - verbose
     - :code:`False`
     - 
   * - logfile
     - :code:`'""'`
     - 
   * - append
     - :code:`False`
     - 


Parameter Explanations
=======================================



tablename
---------------------------------------

:code:`''`

Input spectral line table name to search. If not specified, use the default table in the system.


outfile
---------------------------------------

:code:`''`

Results table name. Blank means do not write the table to disk.


freqrange
---------------------------------------

:code:`numpy.array( [ float(84),float(90) ] )`

Frequency range in GHz.


species
---------------------------------------

:code:`numpy.array( [  ] )`

Species to search for.


reconly
---------------------------------------

:code:`False`

List only NRAO recommended frequencies.


chemnames
---------------------------------------

:code:`numpy.array( [  ] )`

Chemical names to search for.


qns
---------------------------------------

:code:`numpy.array( [  ] )`

Resolved quantum numbers to search for.


intensity
---------------------------------------

:code:`numpy.array( [  ] )`

CDMS/JPL intensity range. -1 -> do not use an intensity range.


smu2
---------------------------------------

:code:`numpy.array( [  ] )`

Quantum mechanical line strength. -1 -> do not use a smu2 range.


loga
---------------------------------------

:code:`numpy.array( [  ] )`

log(A) (Einstein coefficient) range. -1 -> do not use a loga range.


el
---------------------------------------

:code:`numpy.array( [  ] )`

Lower energy state range in Kelvin. -1 -> do not use an el range.


eu
---------------------------------------

:code:`numpy.array( [  ] )`

Upper energy state range in Kelvin. -1 -> do not use an eu range.


rrlinclude
---------------------------------------

:code:`True`

Include RRLs in the result set?


rrlonly
---------------------------------------

:code:`False`

Include only RRLs in the result set?


verbose
---------------------------------------

:code:`False`

List result set to logger (and optionally logfile)?


logfile
---------------------------------------

:code:`'""'`

List result set to this logfile (only used if verbose=True).


append
---------------------------------------

:code:`False`

If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.




