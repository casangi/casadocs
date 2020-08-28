#
# stub function definition file for docstring parsing
#

def exportasdm(vis, asdm='', datacolumn='data', archiveid='S0', rangeid='X1', subscanduration='24h', sbduration='2700s', apcorrected=False, verbose=True, showversion=True, useversion='v3'):
    r"""
Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model

Parameters
   - **vis** (string) - Name of input visibility file
   - **asdm** (string) - >Name of output ASDM directory (on disk)
   - **datacolumn** (string) - Which data column(s) to process.
   - **archiveid** (string) - The X0 in uid://X0/X1/X2
   - **rangeid** (string) - The X1 in uid://X0/X1/X2
   - **subscanduration** (string) - Maximum duration of a subscan in the output ASDM
   - **sbduration** (string) - Maximum duration of a scheduling block (and therefore exec block) in the output ASDM
   - **apcorrected** (bool) - Data to be marked as having atmospheric phase correction
   - **verbose** (bool) - Produce log output
   - **showversion** (bool) - Report the version of ASDM class set being used
   - **useversion** (string) - Selects the version of MS2asdm to be used


Description
      This task serves to convert a CASA visibility file (MS) into an
      ALMA or EVLA `Science Data
      Model <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/the-science-data-model>`__
      dataset. They are mostly identical and mostly use the general SDM
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




    """
    pass
