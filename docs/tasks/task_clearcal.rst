

.. _Description:

Description
   re-initializes the calibration for a visibility data set
   
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
   

.. _Examples:

Examples
   task clearcal examples
   
   To reinitialize the CORRECTED_DATA and fill the column with the
   (original) observed DATA, and in addition also add a MODEL_DATA
   column that is set to unity in total intensity and zero in
   polarization:
   
   ::
   
      clearcal(vis='measurementset.ms', spw='0:5~61', addmodel=True)
   
   .. note:: **NOTE**: The above will only be done for channels 5 to 61 in
      spw 0, provided that the scratch columns already existed in the
      input MeasurementSet. If the scratch columns initially did not
      exist and are thus added, they will be initialized for the
      whole data set and the *spw* parameter will be ignored.
   

.. _Development:

Development
   task clearcal developer
   
   --CASA Developer--
   
   