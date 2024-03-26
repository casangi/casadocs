fixvis -- Recalculates (u, v, w) and/or changes Phase Center -- editing, manipulation task
=======================================

Description
---------------------------------------

Recalculates (u, v, w) and/or changes Phase Center



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
   * - outputvis
     - :code:`''`
     - 
   * - field
     - :code:`[ ]`
     - 
   * - refcode
     - :code:`''`
     - 
   * - reuse
     - :code:`True`
     - 
   * - phasecenter
     - :code:`''`
     - 
   * - distances
     - :code:`[ ]`
     - 
   * - datacolumn
     - :code:`'all'`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of the input visibility set.


outputvis
---------------------------------------

:code:`''`

Name of the output visibility set.  (Can be the same as vis.)


field
---------------------------------------

:code:`[ ]`

Fields to operate on.  '' = all.


refcode
---------------------------------------

:code:`''`

reference frame to convert UVW coordinates to


reuse
---------------------------------------

:code:`True`

base UVW calculation on the old values?


phasecenter
---------------------------------------

:code:`''`

use this direction as phase center


distances
---------------------------------------

:code:`[ ]`

(experimental) List of the distances (as quanta) of the fields selected by field.


datacolumn
---------------------------------------

:code:`'all'`

when applying a phase center shift, modify visibilities only in this/these column(s)




