.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To look up the pointing direction from antenna 0 for field 'Titan'
      in the POINTING table based on the first timestamp in the main
      table rows for this field, write this direction in the FIELD and
      SOURCE tables, and then recalculate the UVW coordinates for this
      field:

      .. container:: casa-input-box

         fixplanets(vis='uid___A002_X1c6e54_X223.ms', field='Titan',
         fixuvw=True)

      To attach the ephemeris table 'Titan_55438-56292dUTC.tab' to field
      'Titan' and then recalculate the UVW coordinates for this field:

      .. container:: casa-input-box

         fixplanets(vis='uid___A002_X1c6e54_X223.ms', field='Titan',
         fixuvw=True, direction='Titan_55438-56292dUTC.tab')

      To set the directions for field 'Titan' in the FIELD and SOURCE
      table to the given direction and not recalculate the UVW
      coordinates; this can be useful for several purposes, among them
      preparing a concatenation of datasets. (Only fields with the same
      direction will be recognised as identical.):

      .. container:: casa-input-box

         fixplanets(vis='uid___A002_X1c6e54_X223.ms', field='Titan',
         fixuvw=False, direction='J2000 12h30m15 -02d12m00')

      To use an ephemeris file returned from JPL via the email query
      described in the Description tab in the case where the source is
      unavailable via recipes.ephemerides.request, first copy the entire
      email received from JPL into a file with a .eph extension (for
      example, "target.eph"), and then attach the ephemeris using
      **fixplanets**: 

      .. container:: casa-input-box

         fixplanets(vis='uid___A002_X1c6e54_X223.ms', fixuvw=True,
         direction='target.eph')

.. container:: section
   :name: viewlet-below-content-body
