Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: casa-input-box

         # create a pv image with the position axis running from ra, dec
         pixel positions of [45, 50] to [100, 120]
         # in the input image
         impv(imagename="my_spectral_cube.im", outfile="mypv.im",
         start=[45,50], end=[100,120])
         # analyze the pv image, such as get statistics
         pvstats = imstat("mypv.im")
         # get the alternate coordinate system information
         tb.open("mypv.im")
         alternate_csys_record =
         tb.getkeyword("misc")["secondary_coordinates"]
         tb.done()

.. container:: section
   :name: viewlet-below-content-body
