.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task caltabconvert parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               caltabold : string

            Name of the old-style caltable. Default: none Example:
            caltabold='gronk.g0'

Example

.. container:: param

   .. container:: parameters2

      vis : string

   Name of the visibility file (MS) associated with the old-style
   caltable. Default: none Example: 'blurp.ms'

Example

.. container:: param

   .. container:: parameters2

      ptype : string = complex

   Type of data in the new-format caltable. Default: "complex" Options:
   "complex" or "float" Note: The old-style caltables do not have this
   information, so it is imperative that users get it correct. "complex"
   refers to caltables that have complex gains (e.g., produced by
   gaincal, bpcal, etc.). "float" refers to caltables that real numbers
   such as delays (e.g., produced by gencal).

Example

.. container:: param

   .. container:: parameters2

      caltabnew : string

   Name of the new-style caltable. Default: '' (the suffix ".new" is
   appended to the name of old-style caltable)

Example

.. container:: section
   :name: viewlet-below-content-body
