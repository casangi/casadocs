uvsub -- Subtract/add model from/to the corrected visibility data. -- modeling, calibration task
=======================================

Description
---------------------------------------

        This function subtracts model visibility data (MODEL_DATA column) from corrected visibility
        data (CORRECTED_DATA column) leaving the residuals in the corrected data column.  If the
        parameter 'reverse' is set true, the process is reversed. Note the DATA column is left untouched.
        If the ms has no CORRECTED _DATA column, one is made, copying DATA column, ahead of doing the 
        uvsub process
        


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
   * - reverse
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


reverse
---------------------------------------

:code:`False`

reverse the operation (add rather than subtract)




