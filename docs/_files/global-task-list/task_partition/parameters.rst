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

            Name of input measurement set

Example

.. container:: param

   .. container:: parameters2

      outputvis : string

   Name of output measurement set

Example

.. container:: param

   .. container:: parameters2

      createmms : bool = True

   Should this create a multi-MS output

Example

.. container:: param

   .. container:: parameters2

      separationaxis : string = auto

   Axis to do parallelization across(scan, spw, baseline, auto)

Allowed Value(s)

auto scan spw baseline

Example

.. container:: param

   .. container:: parameters2

      numsubms : string int = auto

   The number of SubMSs to create (auto or any number)

Example

.. container:: param

   .. container:: parameters2

      flagbackup : bool = True

   Create a backup of the FLAG column in the MMS.

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = all

   Which data column(s) to process.

Allowed Value(s)

all data corrected model data,model,corrected float_data lag_data
float_data,data lag_data,data

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray int intArray

   Select field using ID(s) or name(s).

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray int intArray

   Select spectral window/channels.

Example

.. container:: param

   .. container:: parameters2

      scan : string stringArray int intArray

   Select data by scan numbers.

Example

.. container:: param

   .. container:: parameters2

      antenna : string stringArray int intArray

   Select data based on antenna/baseline.

Example

.. container:: param

   .. container:: parameters2

      correlation : string stringArray

   Correlation: '' ==> all, correlation="XX,YY".

Example

.. container:: param

   .. container:: parameters2

      timerange : string stringArray int intArray

   Select data by time range.

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray int intArray

   Select data by scan intent.

Example

.. container:: param

   .. container:: parameters2

      array : string stringArray int intArray

   Select (sub)array(s) by array ID number.

Example

.. container:: param

   .. container:: parameters2

      uvrange : string stringArray int intArray

   Select data by baseline length.

Example

.. container:: param

   .. container:: parameters2

      observation : string stringArray int intArray

   Select by observation ID(s).

Example

.. container:: param

   .. container:: parameters2

      feed : string stringArray int intArray

   Multi-feed numbers: Not yet implemented.

Example

.. container:: section
   :name: viewlet-below-content-body
