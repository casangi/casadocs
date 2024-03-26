accum -- Accumulate incremental calibration solutions into a calibration table -- calibration task
=======================================

Description
---------------------------------------


       Accum will interpolate and extrapolate a calibration
       table onto a new table that has a regularly-space time grid.

       The first run of accum defines the time grid and fills this
       table with the results from the input table.

       Subsequent use of accum will combine additional calibration
       tables onto the same grid of the initial accum table to obtain
       an output accum table.  See below for concrete examples.

       Accum tables are similar to CL tables in AIPS
       Incremental tables are similar to SN tables in AIPS

	


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - 
   * - tablein
     - :code:`''`
     - 
   * - incrtable
     - :code:`''`
     - 
   * - caltable
     - :code:`''`
     - 
   * - field
     - :code:`numpy.array( [  ] )`
     - 
   * - calfield
     - :code:`numpy.array( [  ] )`
     - 
   * - interp
     - :code:`'linear'`
     - 
   * - accumtime
     - :code:`float(1.0)`
     - 
   * - spwmap
     - :code:`numpy.array( [  ] )`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


tablein
---------------------------------------

:code:`''`

Input cumulative calibration table; use \'\' on first run


incrtable
---------------------------------------

:code:`''`

Input incremental calibration table to add


caltable
---------------------------------------

:code:`''`

Output (cumulative) calibration table


field
---------------------------------------

:code:`numpy.array( [  ] )`

List of field names to process from tablein


calfield
---------------------------------------

:code:`numpy.array( [  ] )`

List of field names to use from incrtable.


interp
---------------------------------------

:code:`'linear'`

Interpolation mode to use for resampling incrtable solutions


accumtime
---------------------------------------

:code:`float(1.0)`

Time-interval when create cumulative table


spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral window combinations to apply




