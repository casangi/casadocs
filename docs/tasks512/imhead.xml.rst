imhead -- List, get and put image header parameters -- analysis, information, manipulation task
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
     - :code:`'summary'`
     - 
   * - hdkey
     - :code:`''`
     - 
   * - hdvalue
     - :code:`''`
     - 
   * - verbose
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


mode
---------------------------------------

:code:`'summary'`

Mode of operation: "add", "del", "get", "history", "list", "put", or "summary". Modes "add", "del", and "put" will not work if the image is read-only (eg a FITS image). 


hdkey
---------------------------------------

:code:`''`

The associated keyword for modes "add", "del", "get", or "put". Only "get" will work if the image is read-only (eg, a FITS image). 


hdvalue
---------------------------------------

:code:`''`

Value of keyword for modes add or put.


verbose
---------------------------------------

:code:`False`

Give a full listing of beams or just a short summary? Only used when the image has multiple beams and mode="summary".




