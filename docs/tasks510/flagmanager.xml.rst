flagmanager -- Enable list, save, restore, delete and rename flag version files. -- editing task
=======================================

Description
---------------------------------------

        These flag version files are copies of the flag column for a
        measurement set.  They can be restored to the data set to get
        back to a previous flag version.  On running importvla, a flag
        version call 'Original' is automatically produced.
        


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
   * - mode
     - :code:`'list'`
     - 
   * - versionname
     - :code:`''`
     - 
   * - oldname
     - :code:`''`
     - 
   * - comment
     - :code:`''`
     - 
   * - merge
     - :code:`'replace'`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


mode
---------------------------------------

:code:`'list'`

Operation: list, save, restore, delete, rename


versionname
---------------------------------------

:code:`''`

Flag version name


oldname
---------------------------------------

:code:`''`

Flag version to rename


comment
---------------------------------------

:code:`''`

Short description of a versionname


merge
---------------------------------------

:code:`'replace'`

Merge option: replace will save or over-write the flags




