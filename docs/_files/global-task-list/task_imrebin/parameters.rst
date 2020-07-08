.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : string

            Name of the input image

Example

imagename='ngc5921.im'

.. container:: param

   .. container:: parameters2

      outfile : string

   Output image name.

Example

.. container:: param

   .. container:: parameters2

      factor : intArray

   Binning factors for each axis. Use imhead or ia.summary to determine
   axis ordering.

Example

.. container:: param

   .. container:: parameters2

      region : undefined

   Region selection. Default is to use the full image.

Example

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default is to use
   the entire direction plane.

Example

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default is to use all channels.

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default is to use all Stokes planes. Stokes
   planes cannot be rebinned.

Example

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      dropdeg : bool = False

   Drop degenerate axes?

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite the output if it exists? Default False

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible?

Example

.. container:: param

   .. container:: parameters2

      crop : bool = True

   Remove pixels from the end of an axis to be rebinned if there are not
   enough to form an integral bin?

Example

.. container:: section
   :name: viewlet-below-content-body
