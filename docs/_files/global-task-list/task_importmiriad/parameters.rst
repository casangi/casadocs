.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters for importmiriad

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               mirfile : string

            Name of input Miriad visibility file Default: none Example:
            mirfile='mydata.uv'

Example

mirfile='mydata.uv'

.. container:: param

   .. container:: parameters2

      vis : string

   Name of output MeasurementSet Default: none Example: vis='mydata.ms'

Example

vis='mydata.ms'

.. container:: param

   .. container:: parameters2

      tsys : bool = False

   Use the Tsys to set the visibility weights Default: False Options:
   False|True

Example

.. container:: param

   .. container:: parameters2

      spw : intArray = -1

   Select spectral window/channels Default: '' (all spectral windows and
   channels) Examples: spw='0~2,4'; spectral windows 0,1,2,4 (all
   channels) spw='<2'; spectral windows less than 2 (i.e. 0,1)
   spw='0:5~61'; spw 0, channels 5 to 61 spw='0,10,3:3~45'; spw 0,10 all
   channels, spw 3 - chans 3 to 45. spw='0~2:2~6'; spw 0,1,2 with
   channels 2 through 6 in each. spw = '*:3~64' channels 3 through 64
   for all sp id's spw = ' :3~64' will NOT work.

Example

spw='1,3,4'

.. container:: param

   .. container:: parameters2

      vel : string

   Select velocity reference Default: telescope dependent, ATCA -> TOPO,
   CARMA -> LSRK Options: TOPO|LSRK|LSRD Example: vel='LSRK'

Example

vel='LSRK'

.. container:: param

   .. container:: parameters2

      linecal : bool = False

   (CARMA) Apply line calibration Default: False Options: False|True
   Only useful for CARMA data

Example

.. container:: param

   .. container:: parameters2

      wide : intArray

   (CARMA) Select wide window averages Select which of the wide-band
   channels should be loaded Only useful for CARMA data

Example

.. container:: param

   .. container:: parameters2

      debug : int = 0

   Display increasingly verbose debug messages Default: 0 Example:
   debug=1

Example

debug=1

.. container:: section
   :name: viewlet-below-content-body
