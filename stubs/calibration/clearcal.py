#
# stub function definition file for docstring parsing
#

def clearcal(vis, field='', spw='', intent='', addmodel=False):
    r"""
Re-initializes the calibration for a visibility data set

Parameters
   - **vis** (string) - Name of input visibility file (MS) [1]_
   - **field** (string='') - Select field using field id(s) or field name(s) [2]_
   - **spw** (string='') - Select spectral window/channels [3]_
   - **intent** (string='') - Select observing intent [4]_
   - **addmodel** (bool=False) - Add MODEL_DATA scratch column [5]_


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
      

   .. rubric:: *vis*
      

   Name of input visibility file.

   .. rubric:: *field*
      

   Standard selection of fields using the field id(s) or field
   name(s).

   .. rubric:: *spw*
      

   Standard selection of spectral windows.

   .. note:: **NOTE:** Multiple channel ranges per spw are not supported in
      **clearcal**.

   .. rubric:: *intent*
      

   Select observing intent. For example, *intent='*BANDPASS*'*
   selects data labelled with BANDPASS intent.

   .. rubric:: *addmodel*
      

   If True, add a MODEL_DATA column along with CORRECTED_DATA column.
   If False, only the CORRECTED_DATA will be added and reset, model
   visibilities will then be evaluated when needed. Default is False
   (i.e., MODEL_DATA column will not be added).




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file (MS)
      |                      Default: none
      | 
      |                         Example: vis='ngc5921.ms'
.. [2] 
   **field** (string='')
      | Select field using field id(s) or field name(s)
      |                      default: '' (all fields)
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
.. [3] 
   **spw** (string='')
      | Select spectral window/channels
      | 
      |                         Examples:
      |                         spw='0~2,4'; spectral windows 0,1,2,4 (all
      |                         channels)
      |                         spw='<2';  spectral windows less than 2
      |                         (i.e. 0,1)
      |                         spw='0:5~61'; spw 0, channels 5 to 61,
      |                         INCLUSIVE
      |                         spw='*:5~61'; all spw with channels 5 to 61
      |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
      |                         3, channels 3 to 45.
      |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
      |                         through 6 in each.
      |                         spw='0:0~10;15~60'; spectral window 0 with
      |                         channels 0-10,15-60. (NOTE ';' to separate
      |                         channel selections)
      |                         spw='0:0~10^2,1:20~30^5'; spw 0, channels
      |                         0,2,4,6,8,10, spw 1, channels 20,25,30 
      |                         type 'help par.selection' for more examples.
.. [4] 
   **intent** (string='')
      | Select observing intent
      |                      default: '' (no selection by intent)
      | 
      |                         Example: intent='*BANDPASS*'  (selects data
      |                         labelled with BANDPASS intent)
.. [5] 
   **addmodel** (bool=False)
      | add MODEL_DATA along with CORRECTED_DATA?
      |                      Default: False (model will not be added)
      |                      Options: False|True
      | 
      |                      If False, it will add/reset only CORRECTED_DATA,
      |                      model visibilities will then be evaluated when
      |                      needed.

    """
    pass
