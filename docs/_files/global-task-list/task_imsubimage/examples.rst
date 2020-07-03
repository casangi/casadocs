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

      .. container:: casa-input-box

         # make a subimage containing only channels 4 to 6 of the
         original image,
         imsubimage(imagename="my.im", outfile="first.im", chans="4~6")

      .. container:: casa-input-box

         # Same as above command, just specifying chans in an alternate,
         more verbose way
         imsubimage(imagename="my.im", outfile="second.im",
         chans="range=[4pix,6pix]")

      .. container:: casa-input-box

         # Same as the above command, but even more verbose way of
         specifying the spectral selection. Assumes the direction axes
         are axes numbers 0 and 1.
         ia.open("my.im")shape = ia.shape()axes = ia.coordsys().names()
         ia.done()xmax = shape[axes.index("Right Ascension")] - 1ymax =
         shape[axes.index("Declination")] - 1reg = "box[[0pix,0pix],[" +
         str(xmax) + "pix, " + str(ymax) + "pix]] range=[4pix,6pix]"
         imsubimage(imagename="my.im", outfile="third.im", region=reg)

      .. container:: casa-input-box

         # As an example of the usage of the keepaxes parameter,
         consider an image
         # that has axes RA, Dec, Stokes, and Freq. The Stokes and Freq
         axes are both
         # degenerate while the RA and Dec axes are not, and it is
         desired to make a
         # subimage in which the Stokes axis is discarded. The following
         command will accomplish that.
         imsubimage(imagename="my.im", outfile="discarded_stokes.im",
         dropdeg=True, keepaxes=[3])

.. container:: section
   :name: viewlet-below-content-body
