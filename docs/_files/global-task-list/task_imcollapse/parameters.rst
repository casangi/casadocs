Parameters
==========

.. container:: documentDescription description

   task imcollapse parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : string

            Name of the input image Default: none Example:
            imagename='ngc5921.im'

Example

imagename='ngc5921.im'

.. container:: param

   .. container:: parameters2

      function : string

   Function used to compute aggregation of pixel values along the
   collapsed axis. Default: none Options: flux, madm, max, mean, median,
   min, npts, rms, stddev, sum, variance, xmadm Minimum match is
   supported for the function parameter (eg, function="r" will compute
   the rms of the pixel values). If one specifies function='flux', the
   following constraints must be true: 1. The image must have a
   direction coordinate, 2. The image must have at least one beam, 3.
   The specified axes must be exactly the direction coordinate axes, 4.
   Only one of the non-directional axes may be non-degenerate, 5. The
   iamge brightness unit must be conformant with x*yJy/beam, where x is
   an optional unit (such as km/s for moments images) and y is an
   optional SI prefix.

Example

function="max"function="rmsfunction="mean"

.. container:: param

   .. container:: parameters2

      axes : variant = [0]

   Zero-based axis number(s) or minimal match strings to collapse.
   Default: [0] Axes can be specified as a single integer or array of
   integers indicating the zero-based axes along which to collapse the
   image. Axes may also be specified as a single or array of strings
   which minimally and uniquely match (ignoring case) world axes names
   in the image (eg "dec" or ["ri, "d"] for collapsing along the
   declination axis or along the right ascension and declination axes,
   respectively).

Example

axis=2

.. container:: param

   .. container:: parameters2

      outfile : string

   Name of output CASA image. Must be specified. Default: none Example:
   outfile='collapsed.im'

Example

outfile='collapsed.im'

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default: '' (use the
   entire direction plane) Example: box="100,100,200,200"

Example

box="100,100,200,200"

.. container:: param

   .. container:: parameters2

      region : string

   Region selection. Default: '' (use the full image)

Example

region="my.rgn"

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default: '' (use all channels)

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default: '' (use all stokes planes)

Example

stokes="iq"

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default: none

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite output image if it exists? Default: False Options:
   False|True

Example

overwrite=true

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible? Default: False Options:
   False|True Stretch the input mask if necessary and possible. Only
   used if a mask is specified.

Example

.. container:: section
   :name: viewlet-below-content-body
