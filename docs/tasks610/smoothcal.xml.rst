smoothcal -- Smooth calibration solution(s) derived from one or more sources: -- calibration task
=======================================

Description
---------------------------------------

        A G- or T-type gain calibration can be smoothed.  Amplitude and
        phase are currently smoothed with the same time.  Calibration values
        will be smoothed over all fields.
        


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
     - Name of input visibility file (MS)
   * - tablein
     - :code:`''`
     - Input calibration table
   * - caltable
     - :code:`''`
     - Output calibration table (overwrite tablein if unspecified)
   * - field
     - :code:`numpy.array( [  ] )`
     - Field name list
   * - smoothtype
     - :code:`'median'`
     - Smoothing filter to use
   * - smoothtime
     - :code:`float(60.0)`
     - Smoothing time (sec)


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


tablein
---------------------------------------

:code:`''`

Input calibration table


caltable
---------------------------------------

:code:`''`

Output calibration table (overwrite tablein if unspecified)


field
---------------------------------------

:code:`numpy.array( [  ] )`

Field name list


smoothtype
---------------------------------------

:code:`'median'`

Smoothing filter to use


smoothtime
---------------------------------------

:code:`float(60.0)`

Smoothing time (sec)




