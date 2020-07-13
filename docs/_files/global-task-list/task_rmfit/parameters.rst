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

               imagename : undefined

            Name(s) of the input image(s). Must be specified.

Example

imagename='ngc5921.im'

.. container:: param

   .. container:: parameters2

      rm : string

   Output rotation measure image name. If not specified, no image is
   written.

Example

.. container:: param

   .. container:: parameters2

      rmerr : string

   Output rotation measure error image name. If not specified, no image
   is written.

Example

.. container:: param

   .. container:: parameters2

      pa0 : string

   Output position angle (degrees) at zero wavelength image name. If not
   specified, no image is written.

Example

.. container:: param

   .. container:: parameters2

      pa0err : string

   Output position angle (degrees) at zero wavelength error image name.
   If not specified, no image is written.

Example

.. container:: param

   .. container:: parameters2

      nturns : string

   Output number of turns image name. If not specified, no image is
   written.

Example

.. container:: param

   .. container:: parameters2

      chisq : string

   Output reduced chi squared image name. If not specified, no image is
   written.

Example

.. container:: param

   .. container:: parameters2

      sigma : double = -1

   Estimate of the thermal noise. A value less than 0 means auto
   estimate.

Example

.. container:: param

   .. container:: parameters2

      rmfg : double = 0.0

   Foreground rotation measure in rad/m/m to subtract.

Example

.. container:: param

   .. container:: parameters2

      rmmax : double = 0.0

   Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO
   SPECIFY.

Example

.. container:: param

   .. container:: parameters2

      maxpaerr : double = 1e30

   Maximum input position angle error in degrees to allow in solution
   determination.

Example

.. container:: section
   :name: viewlet-below-content-body
