exportasdm -- Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model -- import/export task
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
     - :code:`''`
     - 
   * - asdm
     - :code:`''`
     - 
   * - datacolumn
     - :code:`'data'`
     - 
   * - archiveid
     - :code:`'S0'`
     - 
   * - rangeid
     - :code:`'X1'`
     - 
   * - subscanduration
     - :code:`'24h'`
     - 
   * - sbduration
     - :code:`'2700s'`
     - 
   * - apcorrected
     - :code:`False`
     - 
   * - verbose
     - :code:`True`
     - 
   * - showversion
     - :code:`True`
     - 
   * - useversion
     - :code:`'v3'`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

MS name


asdm
---------------------------------------

:code:`''`

Name of output ASDM directory (on disk)


datacolumn
---------------------------------------

:code:`'data'`

specifies which MS data column is used to fill the visibilites in the ASDM


archiveid
---------------------------------------

:code:`'S0'`

the X0 in uid://X0/X1/X2


rangeid
---------------------------------------

:code:`'X1'`

the X1 in uid://X0/X1/X2


subscanduration
---------------------------------------

:code:`'24h'`

maximum duration of a subscan in the output ASDM


sbduration
---------------------------------------

:code:`'2700s'`

maximum duration of a scheduling block (and therefore exec block) in the output ASDM


apcorrected
---------------------------------------

:code:`False`

data to be marked as having atmospheric phase correction


verbose
---------------------------------------

:code:`True`

produce log output


showversion
---------------------------------------

:code:`True`

Report the version of ASDM class set being used


useversion
---------------------------------------

:code:`'v3'`

Selects the version of MS2asdm to be used (\'v3\')




