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

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

vis='ngc5921.ms'

.. container:: param

   .. container:: parameters2

      outputvis : string

   Name of output visibility file Default: '' (same as vis) Example:
   outputvis='ngc5921_out.ms'

Example

vis='ngc5921fixedvis.ms'

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

      refcode : string

   Reference frame to convert UVW coordinates to Default: '' (refcode of
   PHASE_DIR in the FIELD table) Example: refcode='B1950'

Example

.. container:: param

   .. container:: parameters2

      reuse : bool = True

   Base UVW calculation on the old values? Default: True Options:
   True|False Note: ignored if parameter 'phasecenter' is set

Example

.. container:: param

   .. container:: parameters2

      phasecenter : string

   If set to a valid direction: change the phase center for the given
   field to this value If given without the equinox, e.g. '0h01m00s
   +00d12m00s', the parameter is interpreted as a pair of offsets in RA
   and DEC to the present phasecenter. Example: phasecenter='J2000
   9h25m00s -05d12m00s' Note: The RA offset can be given in units of
   time or angle. If given as a time (i.e. as a single number with a
   time unit as in, e.g., 12s or in the XXhXXmXXs or XX:XX:XX.XXX
   formats), it is applied as is. If given as an angle (e.g., 0.01deg),
   it is divided by the cos(DEC) before it is applied.

Example

.. container:: param

   .. container:: parameters2

      distances : undefined = ""

   (experimental) List of the distances (as quanta) of the fields
   selected by field. Default: [] (the distances of all fields are
   assumed to be infinity.) If not a list but just a single value is
   given, this is applied to all fields. Examples: distances=['2E6km',
   '3E6km'] distances='15au'

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string = all

   when applying a phase center shift, modify visibilities only in
   this/these column(s) Default: 'all' (DATA, CORRECTED, and MODEL)
   Example: datacolumn='DATA,CORRECTED' (will not modify MODEL)

Example

.. container:: section
   :name: viewlet-below-content-body
