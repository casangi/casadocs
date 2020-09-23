

.. _Description:

Description
   deletes stored MODELs in the MS
   
   **delmod** is a task to remove MODEL data from MeasurementSets.
   
   The MODEL can be either the scratch-less virtual model (stored in
   the MS SOURCE sub-table), and/or as model visibilities the
   MODEL_DATA column (e.g., written by the tasks **setjy**, **ft**,
   **tclean**). In cases where both representations are present, the
   virtual model is used over the scratch column model and there may
   be a need to remove the virtual model to allow the MODEL_DATA
   column to take effect.  
   
    
   
   .. rubric:: Parameter descriptions
      
   
   .. rubric:: *vis*
      
   
   The input MeasurementSet.
   
   .. rubric:: *otf*
      
   
   *otf=True* will remove the virtual model informatiom from the MS
   SOURCE sub-table.
   
   .. rubric:: *otf=True* expandable parameters
      
   
   .. rubric:: *field*
      
   
   The field ID or name to be selected.  
   
   .. note:: **NOTE:** Currently the *field* selection only applies to the
      virtual model with *otf=True*, **not** the scratch MODEL_DATA
      column (*scr=True*)
   
    
   
   .. rubric:: scr
      
   
   *scr=True* will remove the scratch column MODEL_DATA.
   
   | 
   |
   

.. _Examples:

Examples
   task delmod examples
   
   To delete the on-the-fly model data from a MeasurementSet:
   
   ::
   
      delmod(vis='myfile.ms', otf=True, scr=False)
   

.. _Development:

Development
   task delmod developer
   
   --CASA Developer--
   
   