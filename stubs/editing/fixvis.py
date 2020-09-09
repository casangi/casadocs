#
# stub function definition file for docstring parsing
#

def fixvis(vis, outputvis='', field='""', refcode='', reuse=True, phasecenter='', distances='""', datacolumn='all'):
    r"""
Recalculates (u, v, w) and/or changes Phase Center 

Parameters
   - vis_ (string) - Name of input visibility file
   - outputvis_ (string='') - Name of output visibility file
   - field_ (variant='""') - Select field using field id(s) or field name(s)
   - refcode_ (string='') - reference frame to convert UVW coordinates to
   - reuse_ (bool=True) - base UVW calculation on the old values?
   - phasecenter_ (string='') - use this direction as phase center
   - distances_ (variant='""') - (experimental) List of the distances (as quanta) of the fields selected by field.
   - datacolumn_ (string='all') - when applying a phase center shift, modify visibilities only in this/these column(s)


Description
   **fixvis**recalculates (u, v, w) in an MS based on antenna
   positions, time and source position. **fixvis**can alsochange
   the phase center of visibilities.

   If the phase center is changed, the corresponding modifications
   are applied to the visibility columns given by the parameter
   *datacolumn*which is by default set to *all*(DATA, CORRECTED,
   and MODEL).

   .. warning:: **ALERT:** **fixvis** uses the small angle approximation and
      may be incorrect for large phase shifts. This may result in
      sources shifting position if large phase shifts are being
      applied (shifts up to a few beam sizes have been reported).
      Please use **tclean** for phase center shifts during imaging
      when applicable.

   See also`the description in section UV
   Manipulation <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/uv-manipulation/recalculation-of-uvw-values-fixvis>`__.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of the input visibilityMS.

   .. rubric:: *outputvis*
      

   Name of the outputMS. Default: same as *vis*

   .. rubric:: *field*
      

   The field selection string. Default: '' = all.

   .. rubric:: *refcode*
      

   The UVW coordinates are calculated based on a celestial position,
   the phase direction of the given field. This direction has a
   reference frame. If that frame is not the desired one, one can use
   the parameter refcode to convert to a different frame when the UVW
   coordinates are recalculated. Default: the refcode of PHASE_DIR in
   theFIELD table. Example: *refcode='B1950'*

   .. rubric:: *reuse*
      

   If *True* and the given *refcode* is different from the original,
   the present UVW coordinates are just rotated to the new *refcode*.
   If False, the coordinates are re-calculated from the phase
   direction. Default:True; The parameter isignored when the
   parameter *phasecenter* is set.

   .. rubric:: *phasecenter*
      

   If set to a valid direction: change the phase center for the
   givenfield to this value. Example: *phasecenter='J2000 9h25m00s
   -05d12m00s'.* If given without the equinox, e.g. '*0h01m00s
   +00d12m00s'*, the parameter is interpreted as a pair of offsets in
   RA and DEC to the presentphase center.

   .. note:: **NOTE**: The RA offset can be given in units of time or angle.
      If givenas a time (i.e. as a single number with a time unit as
      in, e.g., 12sor in the XXhXXmXXs or XX:XX:XX.XXX formats), it
      is applied as is.If given as an angle (e.g., 0.01deg), it is
      divided by the cos(DEC)before it is applied.

   .. rubric:: *distances*
      

   *(experimental)* List of the distances (as quanta) of the fields
   selected by field to be used for refocusing. If empty, the
   distances of all fields are assumed to be infinity.If not a list
   but just a single value is given, this is applied toall fields.
   Default: [ ]. Examples: *distances=['2E6km', '3E6km'],
   distances='15au'*

   .. rubric:: *datacolumn*
      

   When applying a phase center shift, modify visibilities only
   inthis/these column(s). Default: 'all' (DATA, CORRECTED, and
   MODEL). Example: 'DATA,CORRECTED' (will not modify MODEL).


.. _vis:

vis (string)
   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _outputvis:

outputvis (string='')
   | Name of output visibility file
   |                      Default: '' (same as vis)
   | 
   |                         Example: outputvis='ngc5921_out.ms'

.. _field:

field (variant='""')
   | Select field using field id(s) or field name(s)
   |                      Default: '' (all fields)
   |                      
   |                      Use 'go listobs' to obtain the list id's or
   |                      names. If field string is a non-negative integer,
   |                      it is assumed a field index,  otherwise, it is
   |                      assumed a field name.
   | 
   |                         Examples:
   |                         field='0~2'; field ids 0,1,2
   |                         field='0,4,5~7'; field ids 0,4,5,6,7
   |                         field='3C286,3C295'; field named 3C286 and
   |                         3C295
   |                         field = '3,4C*'; field id 3, all names
   |                         starting with 4C

.. _refcode:

refcode (string='')
   | Reference frame to convert UVW coordinates to
   |                      Default: '' (refcode of PHASE_DIR in the FIELD
   |                      table)
   | 
   |                         Example: refcode='B1950'

.. _reuse:

reuse (bool=True)
   | Base UVW calculation on the old values?
   |                      Default: True
   |                      Options: True|False
   | 
   |                      Note: ignored if parameter 'phasecenter' is set

.. _phasecenter:

phasecenter (string='')
   | If set to a valid direction: change the phase center for
   | the given field to this value
   |                      If given without the equinox, e.g. '0h01m00s
   |                      +00d12m00s', the parameter is interpreted as a
   |                      pair of offsets in RA and DEC to the present
   |                      phasecenter.
   | 
   |                         Example: phasecenter='J2000 9h25m00s
   |                         -05d12m00s'
   | 
   |                      Note: The RA offset can be given in units of time
   |                      or angle. If given as a time (i.e. as a single
   |                      number with a time unit as in, e.g., 12s or in
   |                      the XXhXXmXXs or XX:XX:XX.XXX formats), it is
   |                      applied as is. If given as an angle (e.g.,
   |                      0.01deg), it is divided by the cos(DEC) before it
   |                      is applied.

.. _distances:

distances (variant='""')
   | (experimental) List of the distances (as quanta) of the
   | fields selected by field.
   |                      Default: [] (the distances of all fields are
   |                      assumed to be infinity.)
   | 
   |                      If not a list but just a single value is given,
   |                      this is applied to all fields.
   | 
   |                         Examples: 
   |                         distances=['2E6km', '3E6km']   
   |                         distances='15au'

.. _datacolumn:

datacolumn (string='all')
   | when applying a phase center shift, modify visibilities
   | only in this/these column(s)
   |                      Default: 'all' (DATA, CORRECTED, and MODEL)
   | 
   |                         Example: datacolumn='DATA,CORRECTED' (will not
   |                         modify MODEL)


    """
    pass
