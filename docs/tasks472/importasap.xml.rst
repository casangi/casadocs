importasap -- Convert ASAP Scantable data  into a CASA visibility file (MS) -- single dish task
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
   * - infile
     - :code:`''`
     - 
   * - outputvis
     - :code:`''`
     - 
   * - flagbackup
     - :code:`True`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - parallel
     - :code:`False`
     - 


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

Name of input ASAP Scantable data


outputvis
---------------------------------------

:code:`''`

Root name of the ms to be created. Note the .ms is NOT added 


flagbackup
---------------------------------------

:code:`True`

Back up flag column before applying flags.


overwrite
---------------------------------------

:code:`False`

Over write an existing MS(s)


parallel
---------------------------------------

:code:`False`

Turn on parallel execution




