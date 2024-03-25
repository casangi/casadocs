exportasdm -- Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model -- import/export task
=======================================

Description
---------------------------------------

Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model



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
   * - asdm
     - :code:`''`
     - >Name of output ASDM directory (on disk)
   * - datacolumn
     - :code:`'data'`
     - Which data column(s) to process.
   * - archiveid
     - :code:`'S0'`
     - The X0 in uid://X0/X1/X2
   * - rangeid
     - :code:`'X1'`
     - The X1 in uid://X0/X1/X2
   * - subscanduration
     - :code:`'24h'`
     - Maximum duration of a subscan in the output ASDM
   * - sbduration
     - :code:`'2700s'`
     - Maximum duration of a scheduling block (and therefore exec block) in the output ASDM
   * - apcorrected
     - :code:`False`
     - Data to be marked as having atmospheric phase correction
   * - verbose
     - :code:`True`
     - Produce log output
   * - showversion
     - :code:`True`
     - Report the version of ASDM class set being used
   * - useversion
     - :code:`'v3'`
     - Selects the version of MS2asdm to be used


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



asdm
---------------------------------------

:code:`''`

Name of output ASDM directory (on disk)
                     Default: none



datacolumn
---------------------------------------

:code:`'data'`

Which data column(s) to use for processing
                     (case-insensitive).
                     Default: 'corrected'
                     Options: 'data', 'model', 'corrected',
		     'all','float_data', 'lag_data',
		     'float_data,data', 'lag_data,data'

                        Example: datacolumn='data'
    
                     NOTE: 'all' = whichever of the above that are
		     present. If the requested column does not exist,
		     the task will exit with an error.



archiveid
---------------------------------------

:code:`'S0'`

The X0 in uid://X0/X1/X2
                     Default: 'S0'



rangeid
---------------------------------------

:code:`'X1'`

The X1 in uid://X0/X1/X2
                     Default: 'X1'



subscanduration
---------------------------------------

:code:`'24h'`

Maximum duration of a subscan in the output ASDM
                     Default: 24h



sbduration
---------------------------------------

:code:`'2700s'`

Maximum duration of a scheduling block (and therefore
exec block) in the output ASDM
                     Default: '2700s'

                     The sbduration parameter controls the number of
		     execution blocks (EBs) into which exportasdm
		     subdivides the visibilities from your input
		     MS. If the total observation time in the MS is
		     shorter than what is given in sbduration, a
		     single EB will be created.



apcorrected
---------------------------------------

:code:`False`

Data to be marked as having atmospheric phase correction
                     Default: False
                     Options: False|True



verbose
---------------------------------------

:code:`True`

Produce log output?
                     Default: True
                     Options: True|False



showversion
---------------------------------------

:code:`True`

Report the version of ASDM class set being used
                     Default: True
                     Options: True|False



useversion
---------------------------------------

:code:`'v3'`

Selects the version of MS2asdm to be used
                     Default: 'v3'





