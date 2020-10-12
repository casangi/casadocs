

.. _Description:

Description
   

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
   
   