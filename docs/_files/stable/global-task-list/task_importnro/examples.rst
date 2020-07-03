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

      To import NRO45m OTF data:

      .. container:: casa-input-box

         infile = 'OriKLA.OriKL.20170101235959.32.Y'  # The NRO45m OTF
         data obtained using the SAM45 spectrometer has an extention of
         "Y".
         outputvis = 'OriKLA.OriKL.20170101235959.32.Y.ms'
         importnro(infile = infile, outputvis = outputvis, overwrite =
         True, parallel = False)

       

       

.. container:: section
   :name: viewlet-below-content-body
