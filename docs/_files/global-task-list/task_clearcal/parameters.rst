Parameters
==========

.. container:: documentDescription description

   task clearcal parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file (MS) Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      field : string

   Select field using field id(s) or field name(s) default: '' (all
   fields) Use 'go listobs' to obtain the list id's or names. If field
   string is a non-negative integer, it is assumed a field index,
   otherwise, it is assumed a field name. Examples: field='0~2'; field
   ids 0,1,2 field='0,4,5~7'; field ids 0,4,5,6,7 field='3C286,3C295';
   field named 3C286 and 3C295 field = '3,4C*'; field id 3, all names
   starting with 4C

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Select spectral window/channels Examples: spw='0~2,4'; spectral
   windows 0,1,2,4 (all channels) spw='<2'; spectral windows less than 2
   (i.e. 0,1) spw='0:5~61'; spw 0, channels 5 to 61, INCLUSIVE
   spw='*:5~61'; all spw with channels 5 to 61 spw='0,10,3:3~45'; spw
   0,10 all channels, spw 3, channels 3 to 45. spw='0~2:2~6'; spw 0,1,2
   with channels 2 through 6 in each. spw='0:0~10;15~60'; spectral
   window 0 with channels 0-10,15-60. (NOTE ';' to separate channel
   selections) spw='0:0~10^2,1:20~30^5'; spw 0, channels 0,2,4,6,8,10,
   spw 1, channels 20,25,30 type 'help par.selection' for more examples.

Example

.. container:: param

   .. container:: parameters2

      intent : string

   Select observing intent default: '' (no selection by intent) Example:
   intent='*BANDPASS*' (selects data labelled with BANDPASS intent)

Example

.. container:: param

   .. container:: parameters2

      addmodel : bool = False

   add MODEL_DATA along with CORRECTED_DATA? Default: False (model will
   not be added) Options: False|True If False, it will add/reset only
   CORRECTED_DATA, model visibilities will then be evaluated when
   needed.

Example

.. container:: section
   :name: viewlet-below-content-body
