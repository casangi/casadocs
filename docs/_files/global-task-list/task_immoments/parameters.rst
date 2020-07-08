.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task applycal parameters

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

imagename=ngc5921_task.image

.. container:: param

   .. container:: parameters2

      moments : intArray = 0

   List of moments you would like to compute

Example

moments=1

.. container:: param

   .. container:: parameters2

      axis : string int = spectral

   The momement axis: ra, dec, lat, long, spectral, or stokes

Example

axis="ra"

.. container:: param

   .. container:: parameters2

      region : string stringArray

   Region selection. Default is to use the full image.

Example

region="myregion.crtf"

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region(s) to select in direction plane. Default is to use
   the entire direction plane.

Example

box="40,40,120,120"

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default is to use all channels.

Example

chans="1~4"

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Default is to use all Stokes planes.

Example

stokes="IQ"

.. container:: param

   .. container:: parameters2

      mask : string

   Mask to use. Default is none.

Example

mask="my.im > 5"

.. container:: param

   .. container:: parameters2

      includepix : int doubleArray intArray = -1

   Range of pixel values to include

Example

includepix=[4, 5]

.. container:: param

   .. container:: parameters2

      excludepix : int doubleArray intArray = -1

   Range of pixel values to exclude

Example

excludepix=[-10, 0]

.. container:: param

   .. container:: parameters2

      outfile : string

   Output image file name (or root for multiple moments)

Example

outfile="mymoments.im"

.. container:: param

   .. container:: parameters2

      stretch : bool = False

   Stretch the mask if necessary and possible?

Example

stretch=true

.. container:: section
   :name: viewlet-below-content-body
