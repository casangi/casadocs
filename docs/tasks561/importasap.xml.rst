importasap -- Convert ASAP Scantable data  into a CASA visibility file (MS) -- single dish, import/export task
=======================================

Description
---------------------------------------

Convert ASAP Scantable data  into a CASA visibility file (MS)



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
     - Name of input ASAP Scantable data
   * - outputvis
     - :code:`''`
     - Root name of the ms to be created. Note the .ms is NOT added.
   * - flagbackup
     - :code:`True`
     - Back up flag column before applying flags.
   * - overwrite
     - :code:`False`
     - Over write an existing MS(s)
   * - parallel
     - :code:`False`
     - Turn on parallel execution


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

Name of input ASAP Scantable data
                     Default: none

                        Example: infile='mydata.asap'



outputvis
---------------------------------------

:code:`''`

Name of output visibility file
                     Default: '' (same as vis)

                        Example: outputvis='myms.ms'

                     NOTE: Note the .ms is NOT added 



flagbackup
---------------------------------------

:code:`True`

Back up flag column before applying flags.
                     Default: True
                     Options: True|False



overwrite
---------------------------------------

:code:`False`

Over write an existing MS(s)
                     Default: False (do not overwrite)
                     Options: False|True



parallel
---------------------------------------

:code:`False`

Turn on parallel execution
                     Default: False (serial execution)
                     Options: False|True





