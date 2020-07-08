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

            Name of input visibility file (MS)

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Data selection parameters

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray

   Selection based on spectral-window/frequency/channel.

Example

"1~3"

.. container:: param

   .. container:: parameters2

      field : string stringArray

   Selection based on field names or field index numbers. Default is
   all.

Example

"0~2", or "3C286"

.. container:: param

   .. container:: parameters2

      antenna : string stringArray

   Selection based on antenna/baselines. Default is all.

Example

["3, VA04"]

.. container:: param

   .. container:: parameters2

      uvrange : string stringArray

   Selection based on uv range. Default: entire range. Default units:
   meters.

Example

"0~100klambda"

.. container:: param

   .. container:: parameters2

      timerange : string stringArray

   Selection based on time range. Default is entire range.

Example

"09:14:0~09:54:0"

.. container:: param

   .. container:: parameters2

      correlation : string stringArray

   Selection based on correlation. Default is all.

Example

"RR,LL"

.. container:: param

   .. container:: parameters2

      scan : string stringArray

   Selection based on scan numbers. Default is all.

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray

   Selection based on observation intent. Default is all.

Example

.. container:: param

   .. container:: parameters2

      feed : string stringArray

   Selection based on multi-feed numbers: Not yet implemented

Example

.. container:: param

   .. container:: parameters2

      array : string stringArray

   Selection based on (sub)array numbers. Default is all.

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Selection based on observation ID. Default is all.

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = True

   Controls level of information detail reported. True reports more than
   False.

Example

.. container:: param

   .. container:: parameters2

      listfile : string

   Name of disk file to write output. Default is none (output is written
   to logger only).

Example

.. container:: param

   .. container:: parameters2

      listunfl : bool = False

   List unflagged row counts? If true, it can have significant negative
   performance impact.

Example

.. container:: param

   .. container:: parameters2

      cachesize : double = 50

   EXPERIMENTAL. Maximum size in megabytes of cache in which data
   structures can be held.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   If True, tacitly overwrite listfile if it exists.

Example

.. container:: section
   :name: viewlet-below-content-body
