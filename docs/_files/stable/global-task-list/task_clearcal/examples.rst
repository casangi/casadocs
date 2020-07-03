.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task clearcal examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To reinitialize the CORRECTED_DATA and fill the column with the
      (original) observed DATA, and in addition also add a MODEL_DATA
      column that is set to unity in total intensity and zero in
      polarization:

      .. container:: casa-input-box

         clearcal(vis='measurementset.ms', spw='0:5~61', addmodel=True)

      .. container:: info-box

         **NOTE**: The above will only be done for channels 5 to 61 in
         spw 0, provided that the scratch columns already existed in the
         input MeasurementSet. If the scratch columns initially did not
         exist and are thus added, they will be initialized for the
         whole data set and the *spw* parameter will be ignored.

.. container:: section
   :name: viewlet-below-content-body
