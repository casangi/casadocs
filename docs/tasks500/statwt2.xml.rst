statwt2 -- THIS APPLICATION IS CURRENTLY FOR TESTING ONLY! USE AT YOUR OWN RISK! Compute and set weights based on variance of data. -- misc task
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
   * - timebin
     - :code:`int(1)`
     - 
   * - chanbin
     - :code:`'spw'`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of measurement set


timebin
---------------------------------------

:code:`int(1)`

Length for binning in time to determine statistics. Can either be integer to be multiplied by the representative integration time, a quantity (string) in time units


chanbin
---------------------------------------

:code:`'spw'`

Channel bin width for computing weights. Can either be integer, in which case it is interpreted as number of channels to include in each bin, or a string "spw" or quantity with frequency units.




