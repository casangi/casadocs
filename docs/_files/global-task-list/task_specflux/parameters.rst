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

      region : undefined

   Region selection. Default is to use the full image.

Example

region="my.rgn"

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default is to use
   the entire direction plane.

Example

box="100,100,200,200"

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default is to use all channels.

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default is to use all Stokes planes.

Example

stokes="iq"

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible?

Example

.. container:: param

   .. container:: parameters2

      function : string = flux density

   Aggregate function to use for computing per channel values. Supported
   values are "flux density", "mean", "median", "sum". Minimal match
   supported.

Example

.. container:: param

   .. container:: parameters2

      unit : string = km/s

   Unit to use for the spectral flux calculation. Must be conformant
   with a typical spectral axis unit.

Example

.. container:: param

   .. container:: parameters2

      major : undefined

   Major axis of overriding restoring beam. If specified, must be a
   valid quantity.

Example

"4arcsec"

.. container:: param

   .. container:: parameters2

      minor : undefined

   Minor axis of overriding restoring beam. If specified, must be a
   valid quantity

Example

"3arcsec"

.. container:: param

   .. container:: parameters2

      logfile : string

   File which to write details. Default is to not write to a file.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite exisitng ouput file if it exists?

Example

overwrite=true

.. container:: section
   :name: viewlet-below-content-body
