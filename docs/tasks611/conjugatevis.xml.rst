conjugatevis -- Change the sign of the phases in all visibility columns. -- utility, manipulation task
=======================================

Description
---------------------------------------

       Change the sign of the phases in all visibility columns.



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
     - Name of input visibility file
   * - spwlist
     - :code:`[ ]`
     - Spectral window selection
   * - outputvis
     - :code:`''`
     - Name of output visibility file
   * - overwrite
     - :code:`False`
     - Overwrite the outputvis if it exists?


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



spwlist
---------------------------------------

:code:`[ ]`

Spectral window selection
                     Default:[] (all spws will be conjugated)

                        Example: spw=[1,2]



outputvis
---------------------------------------

:code:`''`

Name of output visibility file
                     Default: 'conjugated_'+vis

                        Example: outputvis='conjugated.ms'



overwrite
---------------------------------------

:code:`False`

Overwrite the outputvis if it exists?
                     Default: False
                     Options: False|True





