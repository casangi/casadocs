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

            Name of the source image

Example

.. container:: param

   .. container:: parameters2

      template : undefined = get

   A dictionary, refcode, or name of an image that provides the output
   shape and coordinate system

Example

.. container:: param

   .. container:: parameters2

      output : string

   Name for the regridded image

Example

.. container:: param

   .. container:: parameters2

      asvelocity : bool = True

   Regrid spectral axis in velocity space rather than frequency space?

Example

.. container:: param

   .. container:: parameters2

      axes : intArray = -1

   The pixel axes to regrid. -1 => all.

Example

.. container:: param

   .. container:: parameters2

      shape : intArray = -1

   Shape of the output image. Only used if template is an image. If not
   specified (-1), the output image shape will be the same as the
   template image shape along the axes that are regridded and the same
   as input image shape along the axes which are not regridded.

Example

.. container:: param

   .. container:: parameters2

      interpolation : string = linear

   The interpolation method. One of "nearest", "linear", "cubic".

Example

.. container:: param

   .. container:: parameters2

      decimate : int = 10

   Decimation factor for coordinate grid computation

Example

.. container:: param

   .. container:: parameters2

      replicate : bool = False

   Replicate image rather than regrid?

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite (unprompted) pre-existing output file?

Example

.. container:: section
   :name: viewlet-below-content-body
