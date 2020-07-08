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

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      asdm : string

   Name of output ASDM directory (on disk) Default: none

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = data

   Which data column(s) to use for processing (case-insensitive).
   Default: 'corrected' Options: 'data', 'model', 'corrected',
   'all','float_data', 'lag_data', 'float_data,data', 'lag_data,data'
   Example: datacolumn='data' NOTE: 'all' = whichever of the above that
   are present. If the requested column does not exist, the task will
   exit with an error.

Allowed Value(s)

data corrected model

Example

.. container:: param

   .. container:: parameters2

      archiveid : string = S0

   The X0 in uid://X0/X1/X2 Default: 'S0'

Example

.. container:: param

   .. container:: parameters2

      rangeid : string = X1

   The X1 in uid://X0/X1/X2 Default: 'X1'

Example

.. container:: param

   .. container:: parameters2

      subscanduration : string = 24h

   Maximum duration of a subscan in the output ASDM Default: 24h

Example

.. container:: param

   .. container:: parameters2

      sbduration : string = 2700s

   Maximum duration of a scheduling block (and therefore exec block) in
   the output ASDM Default: '2700s' The sbduration parameter controls
   the number of execution blocks (EBs) into which exportasdm subdivides
   the visibilities from your input MS. If the total observation time in
   the MS is shorter than what is given in sbduration, a single EB will
   be created.

Example

.. container:: param

   .. container:: parameters2

      apcorrected : bool = False

   Data to be marked as having atmospheric phase correction Default:
   False Options: False|True

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = True

   Produce log output? Default: True Options: True|False

Example

.. container:: param

   .. container:: parameters2

      showversion : bool = True

   Report the version of ASDM class set being used Default: True
   Options: True|False

Example

.. container:: param

   .. container:: parameters2

      useversion : string = v3

   Selects the version of MS2asdm to be used Default: 'v3'

Allowed Value(s)

v3

Example

.. container:: section
   :name: viewlet-below-content-body
