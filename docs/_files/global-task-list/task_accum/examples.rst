.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task accum examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Create an **accum** table with 10-sec sampling, filling it with
      the calibration in 'first_cal' with the desired interpolation.

      .. container:: casa-input-box

         accum(vis='mydata.ms', tablein='', accumtime=10,
         incrtable='first_cal', caltable='accum1_cal')

      If you plot 'accum1_cal' with **plotms**, you can see how the
      *incrtable* was interpolated.

      Continue accumulating calibrations in 'accum1_cal' from
      'second_cal'

      .. container:: casa-input-box

         accum(vis='mydata.ms', tablein='accum1_cal',
         incrtable='second_cal', caltable='accum1_cal')

       

.. container:: section
   :name: viewlet-below-content-body
