.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Calculate the rotation measure for a single polarization image.

      .. container:: casa-input-box

         rmfit(imagename="mypol.im", rm="myrm.im", rmmax=50.0)

      Calculate the rotation measure using a set of polarization images
      from different spectral windows or bands.

      .. container:: casa-input-box

         rmfit(imagename=["pol1.im", "pol2.im", "pol3.im"],
         rm="myrm2.im", rmmax=50.0)

       

.. container:: section
   :name: viewlet-below-content-body
