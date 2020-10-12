

.. _Description:

Description
   

.. _Examples:

Examples
   task cvel2 examples
   
   **Example 1: **
   
   Regrid a MeasurementSet 'myMS.ms'  to a new 'myMSregridded.ms',
   using velocity mode and a LSRK radio velocity definition.  The
   output width is given in velocity units. The output data has a
   structure of 10 channels, starting at 123 km/s with a width of
   0.1km/s. We use the HI rest frequency of 1.420405 GHz. 
   
   ::
   
      cvel2(vis='myMS.ms', outputvis='myMSregriddedVelMode.ms',
      outframe='LSRK', mode='velocity', veltype='radio',
      restfreq='1.420405GHz', nchan=10, start='123km/s',
      width='0.1km/s')
   
   **Example 2: **
   
   Regrid the same MS, but this time using channel mode. We start at
   channel 5, and create 10 new output channels, grouping 7 channels
   in the new bins. The output width is given in units of number of
   input channels. We also run the output MeasurementSet in reverse
   spectral order (note the negative value of width). This time we
   request a BARYcentric frame and use the interpolation method
   'fftshift'.
   
   ::
   
      cvel2(vis='myMS.ms', outputvis='myMSregriddedChannelMode.ms',
      outframe='BARY',  mode='channel', nchan=10, start=5, width=-7,
      interpolation='fftshift')
   

.. _Development:

Development
   