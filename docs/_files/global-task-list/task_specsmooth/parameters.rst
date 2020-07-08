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

imagename='ngc5921_task.image'

.. container:: param

   .. container:: parameters2

      outfile : string

   Output image name.

Example

outfile='mysmoothed.im'

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region to select in direction plane. Default is to use
   the entire direction plane.

Example

box="4,4,10,10"

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Channels must be contiguous. Default is to use all
   channels.

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Planes specified must be contiguous. Default is
   to use all Stokes planes.

Example

stokes="I"

.. container:: param

   .. container:: parameters2

      region : undefined

   Region selection. Default is to use the full image.

Example

region="myregion.rgn"

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none..

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite the output if it exists?

Example

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible? Default False

Example

.. container:: param

   .. container:: parameters2

      axis : int = -1

   The profile axis. Default: use the spectral axis if one exists, axis
   0 otherwise (<0).

Example

axis=3

.. container:: param

   .. container:: parameters2

      function : string = boxcar

   Convolution function. hanning and boxcar are supported functions.
   Minimum match is supported.

Example

function="boxcar"

.. container:: param

   .. container:: parameters2

      width : int = 2

   Width of boxcar, in pixels.

Example

width=2

.. container:: param

   .. container:: parameters2

      dmethod : string = copy

   Decimation method. "" means no decimation, "copy" and "mean" are also
   supported (minimum match).

Example

dmethod="mean"

.. container:: section
   :name: viewlet-below-content-body
