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

            Name of the input image. Must be specified.

Example

.. container:: param

   .. container:: parameters2

      kernel : string = gauss

   Type of kernel to use. Acceptable values are "b", "box", or "boxcar"
   for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian
   kernel, "c", "common", or "commonbeam" to use the common beam of an
   image with multiple beams as the gaussian to which to convolve all
   the planes, "i" or "image" to use an image as the kernel.

Allowed Value(s)

g gauss gaussian b box boxcar commonbeam common c image i

Example

.. container:: param

   .. container:: parameters2

      major : undefined

   Major axis for the kernels. Standard quantity representation. Must be
   specified for kernel="boxcar".

Example

"4arcsec"

.. container:: param

   .. container:: parameters2

      minor : undefined

   Minor axis. Standard quantity representation. Must be specified for
   kernel="boxcar".

Example

"2arcsec"

.. container:: param

   .. container:: parameters2

      pa : undefined

   Position angle used only for gaussian kernel. Standard quantity
   representation.

Example

"40deg"

.. container:: param

   .. container:: parameters2

      targetres : bool = False

   If gaussian kernel, specified parameters are to be resolution of
   output image (True) or parameters of gaussian to convolve with input
   image (False).

Example

.. container:: param

   .. container:: parameters2

      kimage : string

   Kernel image name. Only used if kernel="i" or "image".

Example

.. container:: param

   .. container:: parameters2

      scale : double = -1.0

   Scale factor. -1.0 means auto-scale. Only used if kernel="i" or
   "image".

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

   Stokes planes to use. Default is to use all Stokes planes.

Example

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Output image name. Must be specified.

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   If true, stretch the mask if necessary and possible.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   If true, overwrite (unprompted) pre-existing output file.

Example

.. container:: param

   .. container:: parameters2

      beam : undefined

   Alternate way of describing a Gaussian. If specified, must be a
   dictionary with keys "major", "minor", and "pa" (or "positionangle").
   Do not specify beam if specifying major, minor, and pa.

Example

{"major": "5arcsec", "minor": "2arcsec", "pa": "20deg"}

.. container:: section
   :name: viewlet-below-content-body
