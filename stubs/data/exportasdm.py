#
# stub function definition file for docstring parsing
#

def exportasdm(vis, asdm='', datacolumn='data', archiveid='S0', rangeid='X1', subscanduration='24h', sbduration='2700s', apcorrected=False, verbose=True, showversion=True, useversion='v3'):
    r"""
Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model

Parameters
   - **vis** (string) - Name of input visibility file [1]_
   - **asdm** (string='') - >Name of output ASDM directory (on disk) [2]_
   - **datacolumn** (string='data') - Which data column(s) to process. [3]_
   - **archiveid** (string='S0') - The X0 in uid://X0/X1/X2 [4]_
   - **rangeid** (string='X1') - The X1 in uid://X0/X1/X2 [5]_
   - **subscanduration** (string='24h') - Maximum duration of a subscan in the output ASDM [6]_
   - **sbduration** (string='2700s') - Maximum duration of a scheduling block (and therefore exec block) in the output ASDM [7]_
   - **apcorrected** (bool=False) - Data to be marked as having atmospheric phase correction [8]_
   - **verbose** (bool=True) - Produce log output [9]_
   - **showversion** (bool=True) - Report the version of ASDM class set being used [10]_
   - **useversion** (string='v3') - Selects the version of MS2asdm to be used [11]_


Description
   This task serves to convert a CASA visibility file (MS) into an
   ALMA or EVLA `Science Data
   Model <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-science-data-model>`__
   dataset. They are mostly identical and mostlyuse the general SDM
   and ALMA ASDM terms interchangibly. A description of the SDM
   format can be found
   `here <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-science-data-model>`__.

   The main purpose of creating this task was to (a) enable the
   creation of simulated ASDMs and (b) facilitate the testing of
   (A)SDM to MS conversion. The user may think of other purposes.

   The *sbduration* parameter controls the number of execution blocks
   (EBs) into which **exportasdm** subdivides the visibilities from
   your input MS. If the total observation time in the MS is shorter
   than what is given in *sbduration*, a single EB will be created.

   Note concerning ALMA data: **exportasdm** presently is not able to
   export from MSs containing WVR data. If you attempt to export such
   an MS, you will receive an error message saying that you can only
   export data of processor type "CORRELATOR". It will also give you
   the list of SPWs which contain CORRELATOR data. You will then have
   to split out these SPWs using the task **split** and run
   **exportasdm** on the resulting MS.

   Also EVLA data can be exported. Note here that **exportasdm** does
   not produce online flags and that a subsequent re-import of the
   data must be done with *online=False*.







Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file
      |                      Default: none
      | 
      |                         Example: vis='ngc5921.ms'
.. [2] 
   **asdm** (string='')
      | Name of output ASDM directory (on disk)
      |                      Default: none
.. [3] 
   **datacolumn** (string='data')
      | Which data column(s) to use for processing
      |                      (case-insensitive).
      |                      Default: 'corrected'
      |                      Options: 'data', 'model', 'corrected',
      |                      'all','float_data', 'lag_data',
      |                      'float_data,data', 'lag_data,data'
      | 
      |                         Example: datacolumn='data'
      |     
      |                      NOTE: 'all' = whichever of the above that are
      |                      present. If the requested column does not exist,
      |                      the task will exit with an error.
.. [4] 
   **archiveid** (string='S0')
      | The X0 in uid://X0/X1/X2
      |                      Default: 'S0'
.. [5] 
   **rangeid** (string='X1')
      | The X1 in uid://X0/X1/X2
      |                      Default: 'X1'
.. [6] 
   **subscanduration** (string='24h')
      | Maximum duration of a subscan in the output ASDM
      |                      Default: 24h
.. [7] 
   **sbduration** (string='2700s')
      | Maximum duration of a scheduling block (and therefore
      | exec block) in the output ASDM
      |                      Default: '2700s'
      | 
      |                      The sbduration parameter controls the number of
      |                      execution blocks (EBs) into which exportasdm
      |                      subdivides the visibilities from your input
      |                      MS. If the total observation time in the MS is
      |                      shorter than what is given in sbduration, a
      |                      single EB will be created.
.. [8] 
   **apcorrected** (bool=False)
      | Data to be marked as having atmospheric phase correction
      |                      Default: False
      |                      Options: False|True
.. [9] 
   **verbose** (bool=True)
      | Produce log output?
      |                      Default: True
      |                      Options: True|False
.. [10] 
   **showversion** (bool=True)
      | Report the version of ASDM class set being used
      |                      Default: True
      |                      Options: True|False
.. [11] 
   **useversion** (string='v3')
      | Selects the version of MS2asdm to be used
      |                      Default: 'v3'

    """
    pass
