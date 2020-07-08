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

            Name of MeasurementSet or Multi-MS

Example

vis='ngc5921.ms'

.. container:: param

   .. container:: parameters2

      axis : string = amplitude

   Values on which to compute statistics

Allowed Value(s)

flag antenna1 antenna2 feed1 feed2 field_id array_id data_desc_id
flag_row interval scan scan_number time weight_spectrum amp amplitude
phase real imag imaginary uvrange

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = data

   Which data column to use (data, corrected, model, float_data)

Allowed Value(s)

data corrected model float_data

Example

.. container:: param

   .. container:: parameters2

      useflags : bool = True

   Take flagging into account?

Example

useflags=True

.. container:: param

   .. container:: parameters2

      spw : string

   spectral-window/frequency/channel

Example

.. container:: param

   .. container:: parameters2

      field : string

   Field names or field index numbers: \\'\'==>all, field=\'0~2,3C286\'

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   More data selection parameters (antenna, timerange etc)

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   antenna/baselines: \\'\'==>all, antenna = \\'3,VA04\'

Example

.. container:: param

   .. container:: parameters2

      uvrange : string

   uv range: \\'\'==>all; uvrange = \\'0~100klambda\', default
   units=meters

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   time range: \\'\'==>all, timerange=\'09:14:0~09:54:0\'

Example

.. container:: param

   .. container:: parameters2

      correlation : string

   Select data based on correlation

Example

.. container:: param

   .. container:: parameters2

      scan : string

   scan numbers: \\'\'==>all

Example

.. container:: param

   .. container:: parameters2

      array : string

   (sub)array numbers: \\'\'==>all

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   observation ID number(s): \\'\' = all

Example

.. container:: param

   .. container:: parameters2

      timeaverage : bool = False

   Average data in time.

Example

.. container:: param

   .. container:: parameters2

      timebin : string = 0s

   Bin width for time averaging.

Example

.. container:: param

   .. container:: parameters2

      timespan : string stringArray

   Span the timebin across scan, state or both.

Example

.. container:: param

   .. container:: parameters2

      maxuvwdistance : double = 0.0

   Maximum separation of start-to-end baselines that can be included in
   an average. (meters)

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray int intArray

   Select data by scan intent.

Example

.. container:: param

   .. container:: parameters2

      reportingaxes : string = ddid

   Which reporting axis to use (ddid, field, integration)

Allowed Value(s)

ddid field integration

Example

.. container:: section
   :name: viewlet-below-content-body
