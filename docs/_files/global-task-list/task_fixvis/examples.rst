Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **Example 1:**

      Recalculate the UVW coordinates for all fields based on the
      existing phase center information in the FIELD table.

      .. container:: casa-input-box

         fixvis(vis='NGC3256.ms',outputvis='NGC3256-fixed.ms')

      **Example 2: **

      Set the phase center for field 'Moon' to the given direction and
      recalculate the UVW coordinates.

      .. container:: casa-input-box

          fixvis(vis='Moon.ms',outputvis='Moon-fixed.ms',field='Moon',
         phasecenter='J2000 9h25m00s 05d12m00s')

       

.. container:: section
   :name: viewlet-below-content-body
