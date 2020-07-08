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

            Input image name. Default is unset.

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Output image name. Default is unset.

Example

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default is to use
   the entire direction plane.

Example

box="100,100,200,200"

.. container:: param

   .. container:: parameters2

      region : string

   Region selection. Default is to use the full image.

Example

region="my.rgn"

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default is to use all channels.

Example

chans="5~20"

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default is to use all Stokes planes.

Example

stokes="iq"

.. container:: param

   .. container:: parameters2

      mask : undefined

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      dropdeg : bool = False

   Drop degenerate axes

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite (unprompted) pre-existing output file?

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = True

   Post additional informative messages to the logger

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible?

Example

.. container:: param

   .. container:: parameters2

      keepaxes : intArray

   If dropdeg=True, these are the degenerate axes to keep. Nondegenerate
   axes are implicitly always kept.

Example

.. container:: section
   :name: viewlet-below-content-body
