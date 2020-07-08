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

vis='ngc5921.ms'

.. container:: param

   .. container:: parameters2

      field : undefined = ""

   Select field using field id(s) or field name(s) Default: '' (all
   fields) Use 'go listobs' to obtain the list id's or names. If field
   string is a non-negative integer, it is assumed a field index,
   otherwise, it is assumed a field name. Examples: field='0~2'; field
   ids 0,1,2 field='0,4,5~7'; field ids 0,4,5,6,7 field='3C286,3C295';
   field named 3C286 and 3C295 field = '3,4C*'; field id 3, all names
   starting with 4C

Example

.. container:: param

   .. container:: parameters2

      fixuvw : bool = False

   Recalculate Fourier-plane u,v,w coordinates? Default: False Options:
   False|True

Example

.. container:: param

   .. container:: parameters2

      direction : undefined

   If set, do not use pointing table but set direction to this value
   Default: '' (use pointing table) Example: 'J2000 19h30m00 -40d00m00'
   The direction can either be given explicitly or as the path to a JPL
   Horizons ephemeris. Alternatively, the ephemeris table can also be
   provided as mime format file. For more information, see the task
   pages of fixplanets in CASA Docs (https://casa.nrao.edu/casadocs/).

Example

.. container:: param

   .. container:: parameters2

      refant : undefined = 0

   Reference antenna name(s); a prioritized list may be specified
   Default: 0 (antenna ID 0) Examples: refant='4' (antenna with index 4)
   refant='VA04' (VLA antenna #4) refant='EA02,EA23,EA13' (EVLA antenna
   EA02, use EA23 and EA13 as alternates if/when EA02 drops out) Use
   taskname=listobs for antenna listing

Example

.. container:: param

   .. container:: parameters2

      reftime : string = first

   If using pointing table information, use it from this timestamp
   Default: 'first' Examples: \* 'median' will use the median timestamp
   for the given field using only the unflagged maintable rows \*
   '2012/07/11/08:41:32' will use the given timestamp (must be within
   the observaton time)

Example

.. container:: section
   :name: viewlet-below-content-body
