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

            Name of input CASA image Default: none Example:
            fitsimage='3C273XC1.image'

Example

.. container:: param

   .. container:: parameters2

      fitsimage : string

   Name of output image FITS file Default: none Example:
   fitsimage='3C273XC1.fits'

Example

.. container:: param

   .. container:: parameters2

      velocity : bool = False

   Use velocity (rather than frequency) as spectral axis Default: False
   Options: False|True

Example

.. container:: param

   .. container:: parameters2

      optical : bool = False

   Use the optical (rather than radio) velocity convention Default:
   False Options: False|True

Example

.. container:: param

   .. container:: parameters2

      bitpix : int = -32

   Bits per pixel Default: -32 Example: bitpix=16

Allowed Value(s)

-32 16

Example

.. container:: param

   .. container:: parameters2

      minpix : int double = 0

   Minimum pixel value (if minpix > maxpix, value is automatically
   determined)

Example

.. container:: param

   .. container:: parameters2

      maxpix : int double = -1

   Maximum pixel value (if minpix > maxpix, value is automatically
   determined) Default: -1

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite output file if it exists? Default: False Options:
   False|True

Example

.. container:: param

   .. container:: parameters2

      dropstokes : bool = False

   Drop the Stokes axis?

Example

.. container:: param

   .. container:: parameters2

      stokeslast : bool = True

   Put Stokes axis last in header? Default: True Options: True|False

Example

.. container:: param

   .. container:: parameters2

      history : bool = True

   Write history to the FITS image? Default: True Options: True|False

Example

.. container:: param

   .. container:: parameters2

      dropdeg : bool = False

   Drop all degenerate axes (e.g. Stokes and/or Frequency)? Default:
   False Options: False|True

Example

.. container:: section
   :name: viewlet-below-content-body
