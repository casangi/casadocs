.. container::
   :name: viewlet-above-content-title

delmod
======

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   deletes stored MODELs in the MS

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **delmod** is a task to remove MODEL data from MeasurementSets.

      The MODEL can be either the scratch-less virtual model (stored in
      the MS SOURCE sub-table), and/or as model visibilities the
      MODEL_DATA column (e.g., written by the tasks **setjy**, **ft**,
      **tclean**). In cases where both representations are present, the
      virtual model is used over the scratch column model and there may
      be a need to remove the virtual model to allow the MODEL_DATA
      column to take effect.  

       

      .. rubric:: Parameter descriptions
         :name: title0

      .. rubric:: *vis*
         :name: vis

      The input MeasurementSet.

      .. rubric:: *otf*
         :name: otf

      *otf=True* will remove the virtual model informatiom from the MS
      SOURCE sub-table.

      .. rubric:: *otf=True* expandable parameters
         :name: otftrue-expandable-parameters

      .. rubric:: *field*
         :name: field

      The field ID or name to be selected.  

      .. container:: info-box

         **NOTE:** Currently the *field* selection only applies to the
         virtual model with *otf=True*, **not** the scratch MODEL_DATA
         column (*scr=True*)

       

      .. rubric:: scr
         :name: scr

      *scr=True* will remove the scratch column MODEL_DATA.

      | 
      |  

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_delmod/about
   task_delmod/examples
