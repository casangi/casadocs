

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To subtract model visibilities stored in the MODEL_DATA column
   from the corrected visibility data in the CORRECTED_DATA column of
   a MeasurementSet, and write the residual visibilities back into
   the CORRECTED_DATA column:
   
   ::
   
      uvsub(vis='filename.ms', reverse=False)
   

.. _Development:

Development
   