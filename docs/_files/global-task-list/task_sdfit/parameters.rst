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

   name of data column to be used ["data", "float_data", or
   "corrected_data"]

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

   select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)

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

   select data by polarization IDs, e.g. "XX,YY" (""=all)

Example

.. container:: param

   .. container:: parameters2

      intent : string

   select data by observational intent, e.g. "*ON_SOURCE*" (""=all)

Example

.. container:: param

   .. container:: parameters2

      timebin : string

   bin width for time averaging

Example

.. container:: param

   .. container:: parameters2

      timespan : string

   span the timebin across "scan", "state", "field", or a combination of
   them (e.g., "scan,state")

Example

.. container:: param

   .. container:: parameters2

      polaverage : string

   polarization averaging mode ("", "stokes" or "geometric").

Allowed Value(s)

stokes geometric

Example

.. container:: param

   .. container:: parameters2

      fitfunc : string = gaussian

   function for fitting

Allowed Value(s)

gaussian lorentzian

Example

.. container:: param

   .. container:: parameters2

      fitmode : string = list

   mode for setting additional channel masks.

Allowed Value(s)

auto list

Example

.. container:: param

   .. container:: parameters2

      nfit : intArray = 0

   list of number of lines to fit in maskline region.

Example

.. container:: param

   .. container:: parameters2

      thresh : double = 5.0

   S/N threshold for linefinder

Example

.. container:: param

   .. container:: parameters2

      avg_limit : int = 4

   channel averaging for broad lines

Example

.. container:: param

   .. container:: parameters2

      minwidth : int = 4

   the minimum channel width to detect as a line

Example

.. container:: param

   .. container:: parameters2

      edge : intArray = 00

   channels to drop at beginning and end of spectrum

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
