.. container::
   :name: viewlet-above-content-title

Subtract/Add Model Visibilities
===============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   uvsub

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **uvsub** is a simple task that allows one to subtract or add the
      MODEL_DATA column to the CORRECTED_DATA column of a given
      MeasurementSet. It has only 2 parameters: *vis* and *reverse.*

      If the CORRECTED_DATA column does not exist then it will be
      created first and the DATA column will be copied into it before
      the addition/subtraction of the MODEL_DATA is performed.

      The MODEL_DATA column can either be the scratch column or a
      virtual one; either one will work with **uvsub**. The model
      visibilities are usually populated by the tasks
      **clean**/**tclean**, **ft**, and **setjy**\ *.*

      Note that **uvsub** does the subtraction over the whole ms. If
      only a subsection (say *field* or *spw* selection was done whiile
      using **clean** or **ft**) of the MS was used in these tasks that
      populate the model visibilities, then the **uvsub** operation will
      give the expected results for only those parts. The remainder of
      the MS will get the CORRECTED_DATA added/subtracted with
      whatever existed originally in the MODEL_DATA. On initialization
      the model visbilities are 1 for parallel hand and 0 for cross
      hand. 

       

.. container:: section
   :name: viewlet-below-content-body
