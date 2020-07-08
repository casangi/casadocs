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

            Input image name

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Output image file name. If left blank (the default), no image is
   written but a new image tool referencing the collapsed image is
   returned.

Example

.. container:: param

   .. container:: parameters2

      region : string record

   Region selection. Default is to use the full image.

Example

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region(s) to select in direction plane. Default is to use
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

stokes="IQ"stokes="RR,LL"

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default setting is none.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite (unprompted) pre-existing output file? Ignored if "outfile"
   is left blank.

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible? Default value is False.

Example

.. container:: param

   .. container:: parameters2

      grid : intArray = 11

   x,y grid spacing. Array of exactly two positive integers.

Example

.. container:: param

   .. container:: parameters2

      anchor : variant = ref

   x,y anchor pixel location. Either "ref" to use the image reference
   pixel, or an array of exactly two integers.

Example

.. container:: param

   .. container:: parameters2

      xlength : variant = 1pix

   Either x coordinate length of box, or diameter of circle. Circle is
   used if ylength is empty string.

Example

.. container:: param

   .. container:: parameters2

      ylength : variant = 1pix

   y coordinate length of box. Use a circle if ylength is empty string.

Example

.. container:: param

   .. container:: parameters2

      interp : string = cubic

   Interpolation algorithm to use. One of "nearest", "linear", "cubic",
   or "lanczos". Minimum match supported.

Example

.. container:: param

   .. container:: parameters2

      stattype : string = sigma

   Statistic to compute. See full description for supported statistics.

Example

.. container:: param

   .. container:: parameters2

      statalg : string = classic

   Statistics computation algorithm to use. Supported values are
   "chauvenet" and "classic", Minimum match is supported.

Example

.. container:: param

   .. container:: parameters2

      zscore : double = -1

   For chauvenet, this is the target maximum number of standard
   deviations data may have to be included. If negative, use Chauvenet"s
   criterion. Ignored if algorithm is not "chauvenet".

Example

.. container:: param

   .. container:: parameters2

      maxiter : int = -1

   For chauvenet, this is the maximum number of iterations to attempt.
   Iterating will stop when either this limit is reached, or the zscore
   criterion is met. If negative, iterate until the zscore criterion is
   met. Ignored if algortihm is not "chauvenet".

Example

.. container:: section
   :name: viewlet-below-content-body
