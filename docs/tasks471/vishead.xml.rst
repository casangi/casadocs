vishead -- List, summary, get, and put metadata in a measurement set -- information, manipulation task
=======================================

Description
---------------------------------------
List, summary, get, and put "header" information in a measurement set.


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
     - :code:`'summary'`
     - 
   * - listitems
     - :code:`numpy.array( [ 'telescope','observer','project','field','freq_group_name','spw_name','schedule','schedule_type','release_date' ] )`
     - 
   * - hdkey
     - :code:`''`
     - 
   * - hdindex
     - :code:`''`
     - 
   * - hdvalue
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


mode
---------------------------------------

:code:`'summary'`

options: list, summary, get, put


listitems
---------------------------------------

:code:`numpy.array( [ 'telescope','observer','project','field','freq_group_name','spw_name','schedule','schedule_type','release_date' ] )`

items to list ([] for all)


hdkey
---------------------------------------

:code:`''`

keyword to get/put


hdindex
---------------------------------------

:code:`''`

keyword index to get/put, counting from zero. ''==>all


hdvalue
---------------------------------------

:code:`''`

value of hdkey




