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

            Name of output feathered image Default: none Example:
            imagename='orion_combined.im'

Example

.. container:: param

   .. container:: parameters2

      highres : string

   Name of high resolution (interferometer) image Default: none Example:
   imagename='orion_vla.im'

Example

.. container:: param

   .. container:: parameters2

      lowres : string

   Name of low resolution (single dish) image Default: none Example:
   imagename='orion_gbt.im'

Example

.. container:: param

   .. container:: parameters2

      sdfactor : double = 1.0

   Value by which to scale the Single Dish image. Default: 1.0 Basically
   modifying the flux scale of the SD image

Example

.. container:: param

   .. container:: parameters2

      effdishdiam : double = -1.0

   New effective SingleDish diameter to use in m Default: -1.0 (leave as
   is) Obviously one can only reduce the dish effective dish diameter in
   feathering.

Example

.. container:: param

   .. container:: parameters2

      lowpassfiltersd : bool = False

   Filter out the high spatial frequencies of the SD image Default:
   False If True the high spatial frequency in the SD image is rejected.
   Any data outside the maximum uv distance that the SD has illuminated
   is filtered out.

Example

.. container:: section
   :name: viewlet-below-content-body
