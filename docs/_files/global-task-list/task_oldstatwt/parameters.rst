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

            Name of measurement set

Example

.. container:: param

   .. container:: parameters2

      dorms : bool = False

   Use rms instead of stddev?

Example

.. container:: param

   .. container:: parameters2

      byantenna : bool = False

   Estimate the noise per antenna -not implemented (vs. per baseline)

Example

.. container:: param

   .. container:: parameters2

      sepacs : bool = True

   If solving by antenna, treat autocorrs separately (not implemented)

Example

.. container:: param

   .. container:: parameters2

      fitspw : string stringArray int intArray

   The signal-free spectral window:channels to estimate the scatter from

Example

.. container:: param

   .. container:: parameters2

      fitcorr : string stringArray int intArray

   The signal-free correlation(s) to estimate the scatter from (not
   implemented)

Example

.. container:: param

   .. container:: parameters2

      combine : string stringArray

   Let estimates span changes in spw, corr, scan and/or state

Example

.. container:: param

   .. container:: parameters2

      timebin : string = 0s

   Bin length for estimates (not implemented)

Example

.. container:: param

   .. container:: parameters2

      minsamp : int = 2

   Minimum number of unflagged visibilities for estimating the scatter

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray int intArray

   Select field using ID(s) or name(s)

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray int intArray

   Select spectral window/channels

Example

.. container:: param

   .. container:: parameters2

      antenna : string stringArray int intArray

   Select data based on antenna/baseline

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Select data by time range

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Select data by scan numbers

Example

.. container:: param

   .. container:: parameters2

      intent : string

   Select data by scan intents

Example

.. container:: param

   .. container:: parameters2

      array : string

   Select (sub)array(s) by array ID number

Example

.. container:: param

   .. container:: parameters2

      correlation : string stringArray

   Select correlations to reweight (DEPRECATED in CASA v4.5)

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Select by observation ID(s)

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = corrected

   Which data column to calculate the scatter from

Allowed Value(s)

data corrected float_data model

Example

.. container:: section
   :name: viewlet-below-content-body
