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

               infile : string

            name of input SD dataset

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = data

   name of data column to be used ["data", "float_data", or "corrected"]

Allowed Value(s)

data float_data corrected

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   select data by antenna name or ID, e.g. "PM03"

Example

.. container:: param

   .. container:: parameters2

      field : string

   select data by field IDs and names, e.g. "3C2*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   select data by spectral window IDs, e.g. "3,5,7" (""=all)

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see
   examples in help)

Example

.. container:: param

   .. container:: parameters2

      scan : string

   select data by scan numbers, e.g. "21~23" (""=all)

Example

.. container:: param

   .. container:: parameters2

      pol : string

   select data by polarization IDs, e.g. "0,1" (""=all)

Example

.. container:: param

   .. container:: parameters2

      intent : string

   select data by observational intent, e.g. "*ON_SOURCE*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      reindex : bool = True

   Re-index indices in subtables based on data selection

Example

.. container:: param

   .. container:: parameters2

      kernel : string = gaussian

   spectral smoothing kernel type

Allowed Value(s)

gaussian boxcar

Example

.. container:: param

   .. container:: parameters2

      kwidth : int = 5

   smoothing kernel width in channel

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   name of output file

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite the output file if already exists

Example

.. container:: section
   :name: viewlet-below-content-body
