virtualconcat -- Concatenate several visibility data sets into a multi-MS -- utility, manipulation task
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
     - List of names of input visibility files to be concatenated
   * - concatvis
     - :code:`''`
     - Name of the output visibility file (a multi-MS)
   * - freqtol
     - :code:`''`
     - Frequency shift tolerance for considering data as the same spwid
   * - dirtol
     - :code:`''`
     - Direction shift tolerance for considering data as the same field
   * - respectname
     - :code:`True`
     - If true, fields with a different name are not merged even if their direction agrees
   * - visweightscale
     - :code:`numpy.array( [  ] )`
     - List of the weight scaling factors to be applied to the individual MSs
   * - keepcopy
     - :code:`False`
     - If true, a copy of the input MSs is kept in their original place.
   * - copypointing
     - :code:`True`
     - If true, keep the POINTING table information in the output MMS. If false, don\'t.


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`numpy.array( [  ] )`

List of names of input visibility files to be concatenated


concatvis
---------------------------------------

:code:`''`

Name of the output visibility file (a multi-MS)


freqtol
---------------------------------------

:code:`''`

Frequency shift tolerance for considering data as the same spwid


dirtol
---------------------------------------

:code:`''`

Direction shift tolerance for considering data as the same field


respectname
---------------------------------------

:code:`True`

If true, fields with a different name are not merged even if their direction agrees


visweightscale
---------------------------------------

:code:`numpy.array( [  ] )`

List of the weight scaling factors to be applied to the individual MSs


keepcopy
---------------------------------------

:code:`False`

If true, a copy of the input MSs is kept in their original place.


copypointing
---------------------------------------

:code:`True`

If true, keep the POINTING table information in the output MMS. If false, don\'t.




