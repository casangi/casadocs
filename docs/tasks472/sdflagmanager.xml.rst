sdflagmanager -- ASAP SD task to manipulate flag version files -- single dish task
=======================================

Description
---------------------------------------

Task sdflagmanager enables users to save the current flag information 
(both channel and row flags) in the given SD dataset out to a separate 
'flag version file'. In the current implementation, sdflagmanager calls 
flagmanager internally, so these flag version files are copies of the 
flag columns for a measurement set actually. They can be restored to 
the data set to obtain a previous flag version. Users can also list, 
delete and rename flag version files using sdflagmanager. It is wise 
to save a flagversion at the beginning or after serious editing.    
  


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
   * - mode
     - :code:`'list'`
     - operation mode [\'list\',\'save\',\'restore\',\'delete\', or \'rename\']
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



infile
---------------------------------------

:code:`''`

name of input SD dataset (ASAP scantable)


mode
---------------------------------------

:code:`'list'`

operation mode


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




