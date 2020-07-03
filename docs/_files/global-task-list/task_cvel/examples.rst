.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task cvel examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **Example 1: **

      Regrid 'myMS.ms' to a new 'myMSregridded.ms' using veolicty mode
      and a LSRK radio velocity definition.  The output data has a
      structure of 10 channels, starting at 123 km/s with a width of
      0.1km/s. We use the HI rest frequency of 1.420405752 GHz. 

      .. container:: casa-input-box

         cvel(vis='myMS.ms', outputvis='myMSregridded.ms',
         outframe='LSRK', mode='velocity', veltype='radio',
         restfreq='1.420405752GHz', nchan=10, start='123km/s',
         width='0.1km/s')

      **Example 2: **

      Regrid the same MS, but this time using channel mode. We start at
      channel 5, and create 10 new output channels, grouping 7 channels
      in the new bins. We also run the output MS in reverse spectral
      order (note the negative value of width). This time we request a
      BARYcentric frame and use the interpolation method 'fftshift'.

      .. container:: casa-input-box

         cvel(vis='myMS.ms', outputvis='myMSregridded.ms',
         outframe='BARY',  mode='channel', nchan=10, start=5, width=-7,
         interpolation='fftshift')

       

       

       

       

       

.. container:: section
   :name: viewlet-below-content-body
