rmtables -- Remove tables cleanly, use this instead of rm -rf -- utility task
=======================================

Description
---------------------------------------

                This task removes tables if they are not being currently accessed via
                the casapy process. Note: if you have multiple sessions running bad things
                could happen if you remove a table being accessed by another process.
    


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - tablenames
     - :code:`numpy.array( [  ] )`
     - Name of the tables


Parameter Explanations
=======================================



tablenames
---------------------------------------

:code:`numpy.array( [  ] )`

Name of the tables




