.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task browsetable parameters

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

            Name of table file (vis, calibration table, image) Default:
            none Example: tablename='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      mightedit : bool = False

   Disable the filtering options (below) and allow editing the table.
   Default: False Options: False|True Warning: the GUI seems to ignore
   whether the table tool is opened read-only - just be careful, esp. if
   filtering.

Example

.. container:: param

   .. container:: parameters2

      sortlist : string stringArray

   List of columns to sort by Default: none

Example

.. container:: param

   .. container:: parameters2

      taql : string

   TaQL query string for prefiltering the table. Default: none Example:
   taql="ANTENNA2 < 6

Example

.. container:: param

   .. container:: parameters2

      skipcols : string stringArray

   Columns to NOT display. Default: none Example: skipcols='feed1,
   feed2'

Example

.. container:: section
   :name: viewlet-below-content-body
