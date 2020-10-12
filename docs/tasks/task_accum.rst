

.. _Description:

Description
   

.. _Examples:

Examples
   task accum examples
   
   Create an **accum** table with 10-sec sampling, filling it with
   the calibration in 'first_cal' with the desired interpolation.
   
   ::
   
      accum(vis='mydata.ms', tablein='', accumtime=10,
      incrtable='first_cal', caltable='accum1_cal')
   
   If you plot 'accum1_cal' with **plotms**, you can see how the
   *incrtable* was interpolated.
   
   Continue accumulating calibrations in 'accum1_cal' from
   'second_cal'
   
   ::
   
      accum(vis='mydata.ms', tablein='accum1_cal',
      incrtable='second_cal', caltable='accum1_cal')
   

.. _Development:

Development
   task accum developer
   
   --CASA Developer--
   
   