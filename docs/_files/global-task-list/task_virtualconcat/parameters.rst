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

               vis : stringArray

            List of names of input visibility files to be concatenated

Example

.. container:: param

   .. container:: parameters2

      concatvis : string

   Name of the output visibility file (a multi-MS)

Example

.. container:: param

   .. container:: parameters2

      freqtol : undefined

   Frequency shift tolerance for considering data as the same spwid

Example

.. container:: param

   .. container:: parameters2

      dirtol : undefined

   Direction shift tolerance for considering data as the same field

Example

.. container:: param

   .. container:: parameters2

      respectname : bool = True

   If true, fields with a different name are not merged even if their
   direction agrees

Example

.. container:: param

   .. container:: parameters2

      visweightscale : doubleArray

   List of the weight scaling factors to be applied to the individual
   MSs

Example

.. container:: param

   .. container:: parameters2

      keepcopy : bool = False

   If true, a copy of the input MSs is kept in their original place.

Example

.. container:: param

   .. container:: parameters2

      copypointing : bool = True

   If true, keep the POINTING table information in the output MMS. If
   false, don\'t.

Example

.. container:: section
   :name: viewlet-below-content-body
