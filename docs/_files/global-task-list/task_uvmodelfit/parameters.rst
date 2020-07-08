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

               vis : string

            Name of input visibility file

Example

.. container:: param

   .. container:: parameters2

      field : string

   Select field using field id(s) or field name(s)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Select spectral window/channels

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Other data selection parameters

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Select data based on time range

Example

.. container:: param

   .. container:: parameters2

      uvrange : undefined

   Select data within uvrange (default units meters)

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Select data based on antenna/baseline

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Scan number range

Example

.. container:: param

   .. container:: parameters2

      msselect : string

   Optional complex data selection (ignore for now)

Example

.. container:: param

   .. container:: parameters2

      niter : int = 5

   Number of fitting iterations to execute

Example

.. container:: param

   .. container:: parameters2

      comptype : string = P

   component model type: P(oint), G(aussian), or D(isk)

Allowed Value(s)

P G D

Example

.. container:: param

   .. container:: parameters2

      sourcepar : doubleArray = 1.0 0.0 0.0

   Starting guess for component parameters (3 values for type P, 5 for G
   and D)

Example

.. container:: param

   .. container:: parameters2

      varypar : boolArray

   Control which parameters to let vary in the fit

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Optional output component list table

Example

.. container:: section
   :name: viewlet-below-content-body
