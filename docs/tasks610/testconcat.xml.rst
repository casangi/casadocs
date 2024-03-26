testconcat -- Concatenate the subtables of several visibility data sets, not the MAIN bulk data. -- utility, manipulation task
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
   * - vis
     - :code:`numpy.array( [  ] )`
     - 
   * - testconcatvis
     - :code:`''`
     - 
   * - freqtol
     - :code:`''`
     - 
   * - dirtol
     - :code:`''`
     - 
   * - copypointing
     - :code:`True`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`numpy.array( [  ] )`

Name(s) of input visibility files to be test-concatenated


testconcatvis
---------------------------------------

:code:`''`

Name of output MS containing the merged subtables


freqtol
---------------------------------------

:code:`''`

Frequency shift tolerance for considering data as the same spwid


dirtol
---------------------------------------

:code:`''`

Direction shift tolerance for considering data as the same field


copypointing
---------------------------------------

:code:`True`

Copy all rows of the POINTING table.




