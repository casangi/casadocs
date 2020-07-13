Parameters
==========

.. container:: documentDescription description

   task conjugatevis parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      spwlist : undefined = ""

   Spectral window selection Default:[] (all spws will be conjugated)
   Example: spw=[1,2]

Example

.. container:: param

   .. container:: parameters2

      outputvis : string

   Name of output visibility file Default: 'conjugated_'+vis Example:
   outputvis='conjugated.ms'

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite the outputvis if it exists? Default: False Options:
   False|True

Example

.. container:: section
   :name: viewlet-below-content-body
