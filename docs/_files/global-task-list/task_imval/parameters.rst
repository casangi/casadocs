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

      region : undefined

   Region selection. Empty string (default) means use rules for
   box/chans/stokes specification.

Example

.. container:: param

   .. container:: parameters2

      box : string

   Rectangular region(s) to select in direction plane. Empty string
   (default) means use the reference pixel.

Example

.. container:: param

   .. container:: parameters2

      chans : string

   Channels to use. Default is to use all channels.

Example

.. container:: param

   .. container:: parameters2

      stokes : string

   Stokes planes to use. Planes specified must be contiguous. Default is
   to use all Stokes planes.

Example

stokes="IQ"stokes="RR,LL"

.. container:: param

   .. container:: parameters2

      blc : undefined = {}

   Bottom-left corner of the bounding box that encloses the region being
   examined..

Example

.. container:: param

   .. container:: parameters2

      trc : undefined = {}

   top-right corner of the bounding box that encloses the region being
   examined.

Example

.. container:: param

   .. container:: parameters2

      axes : undefined = {}

   A listing of the axis index numbers and the data stored along that
   axis.

Example

.. container:: param

   .. container:: parameters2

      unit : undefined = {}

   The units the data values are stored and displayed in.

Example

.. container:: param

   .. container:: parameters2

      data : undefined = {}

   The pixel values found at the given point(s).

Example

.. container:: param

   .. container:: parameters2

      mask : undefined = {}

   The mask values found at the given point(s).

Example

.. container:: section
   :name: viewlet-below-content-body
