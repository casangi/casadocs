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

               vis : string

            Name of measurement set.

Example

.. container:: param

   .. container:: parameters2

      imagename : string

   Name-prefix of multi-termimages to operate on.

Example

.. container:: param

   .. container:: parameters2

      nterms : int = 2

   Number of taylor terms to use

Example

.. container:: param

   .. container:: parameters2

      threshold : string

   Intensity above which to re-calculate spectral index

Example

.. container:: param

   .. container:: parameters2

      action : string = pbcor

   PB-correction (pbcor) or only calc spectral-index (calcalpha)

Allowed Value(s)

pbcor calcalpha

Example

.. container:: param

   .. container:: parameters2

      reffreq : string

   Reference frequency (if specified in clean)

Example

.. container:: param

   .. container:: parameters2

      pbmin : double = 0.2

   PB threshold below which to not correct

Example

.. container:: param

   .. container:: parameters2

      field : string

   Fields to include in the PB calculation

Example

.. container:: param

   .. container:: parameters2

      spwlist : intArray =

   List of N spw ids

Example

.. container:: param

   .. container:: parameters2

      chanlist : intArray =

   List of N channel ids

Example

.. container:: param

   .. container:: parameters2

      weightlist : doubleArray =

   List of N weights (relative)

Example

.. container:: section
   :name: viewlet-below-content-body
