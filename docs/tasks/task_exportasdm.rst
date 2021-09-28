

.. _Description:

Description
   This task serves to convert a CASA visibility file (MS) into an
   ALMA or EVLA `Science Data
   Model <../../notebooks/casa-fundamentals.ipynb#Science-Data-Model>`__
   dataset. They are mostly identical and mostly use the general SDM
   and ALMA ASDM terms interchangibly. A description of the SDM
   format can be found
   `here <../../notebooks/casa-fundamentals.ipynb#Science-Data-Model>`__.
   
   The main purpose of creating this task was to (a) enable the
   creation of simulated ASDMs and (b) facilitate the testing of
   (A)SDM to MS conversion. The user may think of other purposes.
   
   The *sbduration* parameter controls the number of execution blocks
   (EBs) into which **exportasdm** subdivides the visibilities from
   your input MS. If the total observation time in the MS is shorter
   than what is given in *sbduration*, a single EB will be created.
   
   **Note:** **exportasdm** will first create a temporary time-sorted
   reference MS using the name of the *vis* parameter plus "-tsorted".
   If such a file or directory already exists with that name, it will
   be removed **without warning**. 
   
   **Note**: **exportasdm** requires that the input MS (*vis*) all have
   the same value for the PROCESSOR_ID column (only a single PROCESSOR
   row can be exported). The **split** task should can be used to produce
   such a MS, often by chosing appropriate SPWs.
   
   Note concerning ALMA data: **exportasdm** presently is only able to
   export from MSs containing processor type "CORRELATOR" data (e.g. WVR 
   data can not be exported).
   If you attempt to export other types you will receive an error message 
   saying that you can only export data of processor type "CORRELATOR". 
   It will also try to give you the list of SPWs which contain CORRELATOR 
   data, but that list is almost certain to be empty because of the requirement
   noted earlier that the main table of the MS only references one
   PROCESSOR_ID. 
   
   Also EVLA data can be exported. Note here that **exportasdm** does
   not produce online flags and that a subsequent re-import of the
   data must be done with *online=False*.
   

.. _Examples:

Examples
   To produce an ASDM named 'uid___S021_X1418_X1' using the
   datacolumn 'corrected' in the MS 'ngc4826.ms' with minimal log
   output:
   
   ::
   
      exportasdm(vis=’ngc4826.ms’, asdm=’uid___S021_X1418_X1’,
                 datacolumn=’corrected’, archiveid=’S021’, rangeid=’X1418’,
                 verbose=False)


.. _Development:

Development
   No additional development details
