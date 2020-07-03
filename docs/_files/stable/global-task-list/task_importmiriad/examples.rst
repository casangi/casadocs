.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Reading a MIRIAD file and converting it into a
         MeasurementSet   
         :name: reading-a-miriad-file-and-converting-it-into-a-measurementset

      .. container:: casa-input-box

         #In CASA

         importmiriad(mirfile='ngc5921.uv', vis='ngc5921.ms',tsys=True)

      We read the MIRIAD dataset ngc5921.uv and converted it to a
      MeasurementSet, using the recorded Tsys values to set the weights.

.. container:: section
   :name: viewlet-below-content-body
