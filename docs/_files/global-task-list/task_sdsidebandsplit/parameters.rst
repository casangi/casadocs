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

               imagename : stringArray

            a list of names of input images. At least two valid images
            are required for processing

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Prefix of output image name. A suffix, ".signalband" or ".imageband"
   is added to output image name depending on the side band side being
   solved.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite option

Example

.. container:: param

   .. container:: parameters2

      signalshift : doubleArray

   a list of channel number shifts in signal side band. The number of
   elements must be equal to that of imagename

Example

.. container:: param

   .. container:: parameters2

      imageshift : doubleArray

   a list of channel number shifts in image side band. The number of
   elements must be either zero or equal to that of imagename. In case
   of zero length array, the values are obtained from signalshift
   assuming the shifts are the same magnitude in opposite direction.

Example

.. container:: param

   .. container:: parameters2

      getbothside : bool = False

   sideband separation (True) or supression (False)

Example

.. container:: param

   .. container:: parameters2

      refchan : double = 0.0

   reference channel of spectral axis in image sideband

Example

.. container:: param

   .. container:: parameters2

      refval : string

   frequency at the reference channel of spectral axis in image sideband
   (e.g., "100GHz")

Example

.. container:: param

   .. container:: parameters2

      otherside : bool = False

   solve the solution of the other side band side and subtract the
   solution

Example

.. container:: param

   .. container:: parameters2

      threshold : double = 0.2

   Rejection limit of solution. The value must be greater than 0.0 and
   less than 1.0.

Allowed Value(s)

0.0 1.0

Example

.. container:: section
   :name: viewlet-below-content-body
