fixvis
======

.. container:: documentDescription description

   task fixvis description

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **fixvis** recalculates (u, v, w) in an MS based on antenna
      positions, time and source position. **fixvis** can also change
      the phase center of visibilities.

      If the phase center is changed, the corresponding modifications
      are applied to the visibility columns given by the parameter
      *datacolumn* which is by default set to *all* (DATA, CORRECTED,
      and MODEL).

      .. container:: alert-box

         **ALERT:** **fixvis** uses the small angle approximation and
         may be incorrect for large phase shifts. This may result in
         sources shifting position if large phase shifts are being
         applied (shifts up to a few beam sizes have been reported).
         Please use **tclean** for phase center shifts during imaging
         when applicable.

      See also `the description in section UV
      Manipulation <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/recalculation-of-uvw-values-fixvis>`__. 

       

      .. rubric:: Parameter descriptions
         :name: title0

      .. rubric:: *vis*
         :name: vis

      Name of the input visibility MS. 

      .. rubric:: *outputvis*
         :name: outputvis

      Name of the output MS. Default: same as *vis*

      .. rubric:: *field*
         :name: field

      The field selection string. Default: '' = all.

      .. rubric:: *refcode*
         :name: refcode

      The UVW coordinates are calculated based on a celestial position,
      the phase direction of the given field. This direction has a
      reference frame. If that frame is not the desired one, one can use
      the parameter refcode to convert to a different frame when the UVW
      coordinates are recalculated. Default: the refcode of PHASE_DIR in
      the FIELD table. Example: *refcode='B1950'*

      .. rubric:: *reuse*
         :name: reuse

      If *True* and the given *refcode* is different from the original,
      the present UVW coordinates are just rotated to the new *refcode*.
      If False, the coordinates are re-calculated from the phase
      direction. Default: True; The parameter is ignored when the
      parameter *phasecenter* is set.

      .. rubric:: *phasecenter*
         :name: phasecenter

      If set to a valid direction: change the phase center for the
      given field to this value. Example: *phasecenter='J2000 9h25m00s
      -05d12m00s'.* If given without the equinox, e.g. '*0h01m00s
      +00d12m00s'*, the parameter is interpreted as a pair of offsets in
      RA and DEC to the present phase center. 

      .. container:: info-box

         **NOTE**: The RA offset can be given in units of time or angle.
         If given as a time (i.e. as a single number with a time unit as
         in, e.g., 12s or in the XXhXXmXXs or XX:XX:XX.XXX formats), it
         is applied as is. If given as an angle (e.g., 0.01deg), it is
         divided by the cos(DEC) before it is applied.

      .. rubric:: *distances*
         :name: distances

      *(experimental)* List of the distances (as quanta) of the fields
      selected by field to be used for refocusing. If empty, the
      distances of all fields are assumed to be infinity. If not a list
      but just a single value is given, this is applied to all fields.
      Default: [ ].  Examples: *distances=['2E6km', '3E6km'],
      distances='15au'*

      .. rubric:: *datacolumn*
         :name: datacolumn

      When applying a phase center shift, modify visibilities only
      in this/these column(s). Default: 'all' (DATA, CORRECTED, and
      MODEL). Example: 'DATA,CORRECTED' (will not modify MODEL).

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_fixvis/changelog
   task_fixvis/examples
