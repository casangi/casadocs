sdscaleold -- ASAP SD task [DEPRECATED]: Scale the sd spectra -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
The functionality of this task with MeasurementSet format is replicated
with gencal and applycal, and with CASA image format is replicated with immath.
#########################################################################

Task sdscaleold performs scaling of single-dish spectra by scaling
factor given by parameter named factor.
By setting scaletsys = True, associated Tsys is also scaled.
  


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
   * - factor
     - :code:`float(1.0)`
     - 
   * - scaletsys
     - :code:`True`
     - scaling of associated Tsys [True, False]
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - verbose
     - :code:`True`
     - Print verbose log output [True, False]


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


factor
---------------------------------------

:code:`float(1.0)`

scaling factor (float or float list)


scaletsys
---------------------------------------

:code:`True`

scaling of associated Tsys


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists


verbose
---------------------------------------

:code:`True`

Print verbose log output




