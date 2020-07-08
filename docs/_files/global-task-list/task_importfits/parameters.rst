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

               fitsimage : string

            Name of input image FITS file Default: none Example:
            fitsimage='3C273XC1.fits'

Example

.. container:: param

   .. container:: parameters2

      imagename : string

   Name of output CASA image Default: none Example:
   fitsimage='3C273XC1.image'

Example

.. container:: param

   .. container:: parameters2

      whichrep : int = 0

   If fits image has multiple coordinate reps, choose one. Default: 0
   (means first) Example: whichrep=1

Example

.. container:: param

   .. container:: parameters2

      whichhdu : int = -1

   If fits file contains multiple images, choose one Default: -1 (use
   the first valid one) NOTE: 0 = first HDU, -1 = first valid image
   Example: whichhdu=1

Example

.. container:: param

   .. container:: parameters2

      zeroblanks : bool = True

   Set blanked pixels to zero (not NaN) Default: True Options:
   True|False

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite output file if it exists? Default: False Options:
   False|True

Example

.. container:: param

   .. container:: parameters2

      defaultaxes : bool = False

   Add the default 4D coordinate axes where they are missing Default:
   False Options: False|True IMPORTANT: value True requires setting
   defaultaxesvalues

Example

.. container:: param

   .. container:: parameters2

      defaultaxesvalues : variant = []

   List of values to assign to added degenerate axes when
   defaultaxes==True (ra,dec,freq,stokes) Default: [] For existing axes,
   empty strings can be given as values. For the directions and spectral
   values, any valid angle/frequency expressions can be given. Example:
   defaultaxesvalues=['19h30m00', '-02d30m00', '88.5GHz', 'Q']

Example

.. container:: param

   .. container:: parameters2

      beam : variant = []

   List of values to be used to define the synthesized beam
   [BMAJ,BMIN,BPA] (as in the FITS keywords) Default: [] (i.e.take from
   FITS file) Example: beam=['0.35arcsec', '0.24arcsec', '25deg']

Example

.. container:: section
   :name: viewlet-below-content-body
