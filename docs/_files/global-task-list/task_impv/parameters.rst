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

               imagename : string

            Name of the input image

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Output image name. If empty, no image is written.

Example

.. container:: param

   .. container:: parameters2

      mode : string = coords

   If "coords", use start and end values. If "length", use center,
   length, and pa values.

Example

mode="coords"

.. container:: param

   .. container:: parameters2

      start : string stringArray intArray doubleArray

   The starting pixel in the direction plane (array of two values).

Example

[20, 5]

.. container:: param

   .. container:: parameters2

      end : string stringArray intArray doubleArray

   The ending pixel in the direction plane (array of two values).

Example

[200,300]

.. container:: param

   .. container:: parameters2

      center : string stringArray intArray doubleArray

   The center point in the direction plane (array of two values). If
   specified, length and pa must also be specified and neither of start
   nor end may be specified.

Example

.. container:: param

   .. container:: parameters2

      length : string int double stringArray record

   The length of the segment in the direction plane. If specified,
   center and pa must also be specified and neither of start nor end may
   be specified.

Example

.. container:: param

   .. container:: parameters2

      pa : string record

   The position angle of the segment in the direction plane, measured
   from north through east. If specified, center and length must also be
   specified and neither of start nor end may be specified.

Example

.. container:: param

   .. container:: parameters2

      width : string int record = 1

   Width of slice for averaging pixels perpendicular to the slice. Must
   be an odd positive integer or valid quantity. See help for details.

Example

.. container:: param

   .. container:: parameters2

      unit : string = arcsec

   Unit for the offset axis in the resulting image. Must be a unit of
   angular measure.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite the output if it exists?

Example

.. container:: param

   .. container:: parameters2

      region : string record = ""

   Region selection. Default is entire image. No selection is permitted
   in the direction plane.

Example

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Channels must be contiguous. Default is to use all
   channels.

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Planes must be contiguous. Default is to use
   all stokes.

Example

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible? Default False

Example

.. container:: section
   :name: viewlet-below-content-body
