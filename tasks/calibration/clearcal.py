#
# stub function definition file for docstring parsing
#

def clearcal(vis, field='', spw='', intent='', addmodel=False):
    r"""
Re-initializes the calibration for a visibility data set

Parameters
   - **vis** (string) - Name of input visibility file (MS)
   - **field** (string) - Select field using field id(s) or field name(s)
   - **spw** (string) - Select spectral window/channels
   - **intent** (string) - Select observing intent
   - **addmodel** (bool) - Add MODEL_DATA scratch column


Description
      Re-initializes the calibration columns in a MeasurementSet.
      Specificially, it will set the MODEL_DATA column (if present) to
      unity in total intensity and zero in polarization, and it will set
      the CORRECTED_DATA column to the original (observed) DATA in the
      DATA column. Use the *field* and *spw* parameters to select which
      data to initialize. 

      If the dataset does not yet have the scratch columns, they will be
      created (MODEL_DATA only if *addmodel=True*) and initilized for
      the whole dataset. In this case, the arguments *field*, *spw*, and
      *intent* will be ignored.  

       

      .. rubric:: Parameters
         :name: parameters

      .. rubric:: *vis*
         :name: vis

      Name of input visibility file.

      .. rubric:: *field*
         :name: field

      Standard selection of fields using the field id(s) or field
      name(s).

      .. rubric:: *spw*
         :name: spw

      Standard selection of spectral windows.

      .. note:: **NOTE:** Multiple channel ranges per spw are not supported in
         **clearcal**.

      .. rubric:: *intent*
         :name: intent

      Select observing intent. For example, *intent='*BANDPASS*'* 
      selects data labelled with BANDPASS intent.

      .. rubric:: *addmodel*
         :name: addmodel

      If True, add a MODEL_DATA column along with CORRECTED_DATA column.
      If False, only the CORRECTED_DATA will be added and reset, model
      visibilities will then be evaluated when needed. Default is False
      (i.e., MODEL_DATA column will not be added).

    """
    pass
