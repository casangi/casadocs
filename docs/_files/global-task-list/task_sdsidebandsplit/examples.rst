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

      Obtain an image of signal sideband (side band supression):

      .. container:: casa-input-box

         sdsidebandsplit(imagename=['shift_0ch.image',
         'shift_132ch.image', 'shift_neg81ch.image'],
         outfile='separated.image', signalshift=[0.0, +132.0,
         -81.0],imageshift=[0.0, -132.0, +81.0])

      The output image is 'separated.image.signalband'.

       

      To solve both signal and image sidebands, set frequency of image
      sideband explicitly in addtion to *getbothside=True*.

      .. container:: casa-input-box

         sdsidebandsplit(imagename=['shift_0ch.image',
         'shift_132ch.image', 'shift_neg81ch.image'],
         outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
         imageshift=[0.0, -132.0, +81.0], getbothside=True, refpix=0.0,
         refval='805.8869GHz')

      The output images are 'separated.image.signalband' and
      'separated.image.imageband' for signal and image sideband,
      respectively.

       

      To obtain signal sideband image by solving image sideband, set
      *otherside=True*:

      .. container:: casa-input-box

         sdsidebandsplit(imagename=['shift_0ch.image',
         'shift_132ch.image', 'shift_neg81ch.image'],
         outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
         imageshift=[0.0, -132.0, +81.0], otherside=True)

      Solution of image sideband is obtained and subtracted from the
      original (double sideband) spectra to derive spectra of signal
      sideband. The output image is 'separated.image.signalband'.

       

       

.. container:: section
   :name: viewlet-below-content-body
