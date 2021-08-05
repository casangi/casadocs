.. _Description:

Description

   .. danger:: **ALERT:** **fixvis** is deprecated in CASA 5.9/6.3. Please use task **phaseshift** instead.

   **fixvis** recalculates (u, v, w) in an MS based on antenna
   positions, time and source position. **fixvis** can also change
   the phase center of visibilities.
   
   If the phase center is changed, the corresponding modifications
   are applied to the visibility columns given by the parameter
   *datacolumn* which is by default set to *all* (DATA, CORRECTED,
   and MODEL).
   
   .. warning:: **ALERT:** **fixvis** uses the small angle approximation and
      may be incorrect for large phase shifts. This may result in
      sources shifting position if large phase shifts are being
      applied (shifts up to a few beam sizes have been reported).
      Please use **tclean** for phase center shifts during imaging
      when applicable.
   
   See also `the description in section UV
   Manipulation <../../notebooks/uv_manipulation.ipynb#Recalculate-UVW-Values>`__.

   .. rubric:: Parameter descriptions
      
   *vis*

   Name of the input visibility MS. 
   
   *outputvis*

   Name of the output MS. Default: same as *vis*
   
   *field*

   The field selection string. Default: '' = all.
   
   *refcode*
   
   The UVW coordinates are calculated based on a celestial position,
   the phase direction of the given field. This direction has a
   reference frame. If that frame is not the desired one, one can use
   the parameter refcode to convert to a different frame when the UVW
   coordinates are recalculated. Default: the refcode of PHASE_DIR in
   the FIELD table. Example: *refcode='B1950'*
   
   *reuse*
   
   If *True* and the given *refcode* is different from the original,
   the present UVW coordinates are just rotated to the new *refcode*.
   If False, the coordinates are re-calculated from the phase
   direction. Default: True; The parameter is ignored when the
   parameter *phasecenter* is set.
   
   *phasecenter*
   
   If set to a valid direction: change the phase center for the
   given field to this value. Example: *phasecenter='J2000 9h25m00s
   -05d12m00s'.* If given without the equinox, e.g. '*0h01m00s
   +00d12m00s'*, the parameter is interpreted as a pair of offsets in
   RA and DEC to the present phase center. 
   
   .. note:: **NOTE**: The RA offset can be given in units of time or angle.
      If given as a time (i.e. as a single number with a time unit as
      in, e.g., 12s or in the XXhXXmXXs or XX:XX:XX.XXX formats), it
      is applied as is. If given as an angle (e.g., 0.01deg), it is
      divided by the cos(DEC) before it is applied.
   
   .. rubric:: *distances*

   *(experimental)* List of the distances (as quanta) of the fields
   selected by field to be used for refocusing. If empty, the
   distances of all fields are assumed to be infinity. If not a list
   but just a single value is given, this is applied to all fields.
   Default: [ ].  Examples: *distances=['2E6km', '3E6km'],
   distances='15au'*
   
   .. rubric:: *datacolumn*
      
   
   When applying a phase center shift, modify visibilities only
   in this/these column(s). Default: 'all' (DATA, CORRECTED, and
   MODEL). Example: 'DATA,CORRECTED' (will not modify MODEL).
   

.. _Examples:

Examples
   **Example 1:**
   
   Recalculate the UVW coordinates for all fields based on the
   existing phase center information in the FIELD table.
   
   ::
   
      fixvis(vis='NGC3256.ms',outputvis='NGC3256-fixed.ms')
   
   **Example 2: **
   
   Set the phase center for field 'Moon' to the given direction and
   recalculate the UVW coordinates.
   
   ::
   
       fixvis(vis='Moon.ms',outputvis='Moon-fixed.ms',field='Moon',
              phasecenter='J2000 9h25m00s 05d12m00s')


.. _Development:

Development
   No additional development details

