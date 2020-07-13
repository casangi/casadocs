Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               infile : string

            (Optional) Name of file to visualize.

Example

.. container:: param

   .. container:: parameters2

      displaytype : string = raster

   (Optional) Type of visual rendering (raster, contour, vector or
   marker). lel if an lel expression is given for infile (advanced).

Example

.. container:: param

   .. container:: parameters2

      channel : int = 0

   (Optional) access a specific channel in the image cube

Example

.. container:: param

   .. container:: parameters2

      zoom : int = 1

   (Optional) zoom in/out by increments

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   (Optional) name of the output file to generate

Example

.. container:: param

   .. container:: parameters2

      outscale : double = 1.0

   (Optional) amount to scale output bitmap formats (non-PS, non-PDF)

Example

.. container:: param

   .. container:: parameters2

      outdpi : int = 300

   (Optional) output DPI for PS/PDF

Example

.. container:: param

   .. container:: parameters2

      outformat : string = jpg

   (Optional) format of the output e.g. jpg or pdf (this is overridden
   by the output files extension

Example

.. container:: param

   .. container:: parameters2

      outlandscape : bool = False

   (Optional) should the output mode be landscape (PS or PDF)

Example

.. container:: param

   .. container:: parameters2

      gui : bool = True

   (Optional) Display the panel in a GUI.

Example

.. container:: section
   :name: viewlet-below-content-body
