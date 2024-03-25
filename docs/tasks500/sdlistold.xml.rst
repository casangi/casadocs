sdlistold -- ASAP SD task [DEPRECATED]: list summary of single dish data -- single dish task
=======================================

Description
---------------------------------------

### DEPRECATION WARNING #################################################
This task will be removed in CASA 5.1.
The functionality of this task with MeasurementSet format is replicated
with listobs.
#########################################################################

Task sdlistold lists the scan summary of the dataset after importing
as a scantable into ASAP.  It will optionally output this summary
as file.



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
   * - outfile
     - :code:`''`
     - 
   * - overwrite
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


outfile
---------------------------------------

:code:`''`

name of output file (ASCII) for summary list


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists [True, False]




