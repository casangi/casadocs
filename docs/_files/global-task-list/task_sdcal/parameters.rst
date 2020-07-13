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

            name of input SD dataset (must be MS)

Example

.. container:: param

   .. container:: parameters2

      calmode : string = ps

   SD calibration mode

Allowed Value(s)

ps otfraster otf tsys apply ps,apply tsys,apply ps,tsys,apply
otfraster,apply otfraster,tsys,apply otf,apply otf,tsys,apply

Example

.. container:: param

   .. container:: parameters2

      fraction : undefined = 10%

   fraction of the OFF data to mark

Example

.. container:: param

   .. container:: parameters2

      noff : int = -1

   number of the OFF data to mark

Example

.. container:: param

   .. container:: parameters2

      width : double = 0.5

   width of the pixel for edge detection

Example

.. container:: param

   .. container:: parameters2

      elongated : bool = False

   whether observed area is elongated in one direction or not

Example

.. container:: param

   .. container:: parameters2

      applytable : undefined

   (List of) sky and/or tsys tables

Example

.. container:: param

   .. container:: parameters2

      interp : string

   Interpolation type in time[,freq]. Valid options for time are
   "nearest", "linear", and "cubic", while valid options for frequency
   include "nearest", "linear", "cspline", or any numeric string that
   indicates an order of polynomial interpolation. You can specify
   interpolation type for time and frequency separately by joining two
   of the above options by comma (e.g., "linear,cspline").

Example

.. container:: param

   .. container:: parameters2

      spwmap : undefined

   A dictionary indicating spw combinations to apply Tsys calibration to
   target. The key should be spw for Tsys calibration and its associated
   value must be a list of science spws to be applied.

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   name of output file (See a WARNING in help)

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite the output file if already exists

Example

.. container:: param

   .. container:: parameters2

      field : string

   select data by field IDs and names, e.g. "3C2*" ("" = all)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)

Example

.. container:: param

   .. container:: parameters2

      scan : string

   select data by scan numbers, e.g. "21~23" (""=all)

Example

.. container:: param

   .. container:: parameters2

      intent : string

   select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE"
   (""=all)

Example

.. container:: section
   :name: viewlet-below-content-body
