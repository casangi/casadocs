.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task calstat parameters

.. container:: section
   :name: viewlet-above-content-body

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

      datacolumn : string = float_data

   name of data column to be used ["data", "float_data", or
   "corrected_data"]

Allowed Value(s)

data float_data corrected

Example

.. container:: param

   .. container:: parameters2

      field : string

   select data by field IDs and names, e.g. "3C2*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   select data by spectral windows and channels, e.g. "3,5,7" (""=all)

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

      antenna : string

   antenna IDs to be averaged over, e.g. "PM03" (""=all)

Example

.. container:: param

   .. container:: parameters2

      timebin : string = all

   bin width for time averaging.

Example

.. container:: param

   .. container:: parameters2

      timespan : string = scan

   span across scan, state or both.

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   name of output file

Example

.. container:: section
   :name: viewlet-below-content-body
