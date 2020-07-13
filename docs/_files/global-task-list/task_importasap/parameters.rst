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

            Name of input ASAP Scantable data Default: none Example:
            infile='mydata.asap'

Example

.. container:: param

   .. container:: parameters2

      outputvis : string

   Name of output visibility file Default: '' (same as vis) Example:
   outputvis='myms.ms' NOTE: Note the .ms is NOT added

Example

.. container:: param

   .. container:: parameters2

      flagbackup : bool = True

   Back up flag column before applying flags. Default: True Options:
   True|False

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Over write an existing MS(s) Default: False (do not overwrite)
   Options: False|True

Example

.. container:: param

   .. container:: parameters2

      parallel : bool = False

   Turn on parallel execution Default: False (serial execution) Options:
   False|True

Example

.. container:: section
   :name: viewlet-below-content-body
