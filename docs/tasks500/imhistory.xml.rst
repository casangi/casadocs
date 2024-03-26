imhistory -- Retrieve and modify image history -- analysis task
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
   * - imagename
     - :code:`''`
     - 
   * - mode
     - :code:`'list'`
     - 
   * - verbose
     - :code:`True`
     - 
   * - origin
     - :code:`'imhistory'`
     - 
   * - message
     - :code:`''`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


mode
---------------------------------------

:code:`'list'`

Mode to run in, "list" to retrieve history, "append" to append a record to history.


verbose
---------------------------------------

:code:`True`

Write history to logger if mode="list"?


origin
---------------------------------------

:code:`'imhistory'`

Origin of appended message. Only used for mode="append".


message
---------------------------------------

:code:`''`

Message to append. Only used of mode="append".




