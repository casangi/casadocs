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

               tablename : string

            Input spectral line table name to search. If not specified,
            use the default table in the system.

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Results table name. Blank means do not write the table to disk.

Example

.. container:: param

   .. container:: parameters2

      freqrange : doubleArray = 84 90

   Frequency range in GHz.

Example

.. container:: param

   .. container:: parameters2

      species : stringArray

   Species to search for.

Example

.. container:: param

   .. container:: parameters2

      reconly : bool = False

   List only NRAO recommended frequencies.

Example

.. container:: param

   .. container:: parameters2

      chemnames : stringArray

   Chemical names to search for.

Example

.. container:: param

   .. container:: parameters2

      qns : stringArray

   Resolved quantum numbers to search for.

Example

.. container:: param

   .. container:: parameters2

      intensity : doubleArray = -1

   CDMS/JPL intensity range. -1 -> do not use an intensity range.

Example

.. container:: param

   .. container:: parameters2

      smu2 : doubleArray = -1

   Quantum mechanical line strength. -1 -> do not use a smu2 range.

Example

.. container:: param

   .. container:: parameters2

      loga : doubleArray = -1

   log(A) (Einstein coefficient) range. -1 -> do not use a loga range.

Example

.. container:: param

   .. container:: parameters2

      el : doubleArray = -1

   Lower energy state range in Kelvin. -1 -> do not use an el range.

Example

.. container:: param

   .. container:: parameters2

      eu : doubleArray = -1

   Upper energy state range in Kelvin. -1 -> do not use an eu range.

Example

.. container:: param

   .. container:: parameters2

      rrlinclude : bool = True

   Include RRLs in the result set?

Example

.. container:: param

   .. container:: parameters2

      rrlonly : bool = False

   Include only RRLs in the result set?

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = False

   List result set to logger (and optionally logfile)?

Example

.. container:: param

   .. container:: parameters2

      logfile : string = ""

   List result set to this logfile (only used if verbose=True).

Example

.. container:: param

   .. container:: parameters2

      append : bool = False

   If true, append to logfile if it already exists, if false overwrite
   logfile it it exists. Only used if verbose=True and logfile not
   blank.

Example

.. container:: section
   :name: viewlet-below-content-body
