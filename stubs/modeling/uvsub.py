#
# stub function definition file for docstring parsing
#

def uvsub(vis, reverse=False):
    r"""
Subtract/add model from/to the corrected visibility data.

Parameters
   - vis_ (string) - Name of input visibility file (MS)
   - reverse_ (bool=False) - reverse the operation (add rather than subtract)


Description
   Subtracts model visibilities from the corrected visibility data in
   a MeasurementSet.

   This task subtracts the model visibilities in the MODEL_DATA
   column of a MeasurementSet from the corrected visbilities in the
   CORRECTED_DATA column. The MODEL_DATA column can either be the
   scratch column or a virtual one. The residuals after subtraction
   are placed in the CORRECTED_DATA column. If the parameter
   *reverse* is set to True, the process is reversed and the model
   will instead be added to the corrected data. The DATA column is
   left untouched. If the MeasurementSet has no CORRECTED_DATA
   column, one is created and the content of the DATA column is
   copied into it ahead of the **uvsub** process.

   .. note:: **NOTE**: **uvsub** does the subtraction over the whole MS. The
      model visibilities are usually populated by the tasks
      **clean**/**tclean**, **ft** and **setjy**. If only a
      subsection of the MS was used in these tasks (e.g., when
      selecting *field*or *spw*in **clean** or **ft**), then only
      this subset of model visibilities will be populated and the
      **uvsub** operation will give expected results only for this
      subsection of the MS. The remainder of the MS will get the
      CORRECTED_DATA added/subtracted with whatever was there
      originally in the MODEL_DATA column (on initialization, the
      model visibilities are 1 for parallel hand and 0 for cross
      hand).\\

   .. warning:: **WARNING:** Currently, **uvsub** will not work if the
      frequency axis is different between the MS file the model is
      derived from and the MS file you are subtracting from. Please
      use **cvel2** to regrid the frequency axis of the MS to match
      that of the model.

   See also the CASA Docs chapter pages on `Subtracting and Adding
   Model
   Visibilities <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/subtracting-or-adding-model-visibilities>`__.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: vis
      

   Name of input visibility file (MS).

   .. rubric:: *reverse*
      

   Reverse the operation (add rather than subtract). Default is
   reverse=False.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file (MS)

.. _reverse:

   .. rubric:: reverse

   | reverse the operation (add rather than subtract)


    """
    pass
