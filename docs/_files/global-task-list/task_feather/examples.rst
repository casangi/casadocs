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

      Creating a image called 'M100_Feather_CO.image' from an ALMA
      interferometric cube, 'M100_combine_CO_cube.image.subim', and a
      single dish ALMA total power image,
      'M100_TP_CO_cube.regrid.subim.depb'. The inputs have been
      appropriately cleaned, regridded, and cropped beforehand.

      ``feather(imagename='M100_Feather_CO.image',highres='M100_combine_CO_cube.image.subim',lowres='M100_TP_CO_cube.regrid.subim.depb')``

      Creating an image called 'feather.im' by combining the cleaned,
      synthesis image, 'synth.im' and the SD image, 'single_dish.im'
      while increasing the flux scale of the SD image by setting
      sdfactor = 1.2.

      ``feather(imagename ='feather.im', highres ='synth.im', lowres ='single_dish.im'sdfactor = 1.2)``

.. container:: section
   :name: viewlet-below-content-body
