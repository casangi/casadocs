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

               vis : string

            Name of input MS. Output goes to vis + ".contsub" (will be
            overwritten if already exists)

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray int intArray

   Select field(s) using id(s) or name(s)

Example

.. container:: param

   .. container:: parameters2

      fitspw : string

   Spectral window:channel selection for fitting the continuum

Example

.. container:: param

   .. container:: parameters2

      excludechans : bool = False

   exclude Spectral window:channel selection in fitspw for fitting

Example

.. container:: param

   .. container:: parameters2

      combine : string

   Data axes to combine for the continuum estimation (none, or spw
   and/or scan)

Example

.. container:: param

   .. container:: parameters2

      solint : undefined = int

   Continuum fit timescale (int recommended!)

Example

.. container:: param

   .. container:: parameters2

      fitorder : int = 0

   Polynomial order for the fits

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Spectral window selection for output

Example

.. container:: param

   .. container:: parameters2

      want_cont : bool = False

   Create vis + ".cont" to hold the continuum estimate.

Example

.. container:: section
   :name: viewlet-below-content-body
