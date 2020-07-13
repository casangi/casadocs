Examples
========

.. container:: documentDescription description

   task applycal examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Often, it is desirable to calibrate calibrators and science
      targets in separate runs of **applycal**, perhaps with different
      interpolation parameters. First we calibrate the calibrators
      (fields 0 and 1) using gainfield='nearest' for the gain caltable
      to ensure that each calibrator will be calibrated by solutions
      obtained from itself. (The bandpass calibration is typically
      solved from one field but applied to all fields.):

      .. container:: casa-input-box

         | applycal(vis='n5921.ms',
         |          field='0,1',                             #
           calibrators
         |          spw='',                                  # all
           channels
         |          gaintable=['n5921.gcal','n5921.bcal']    # gain and
           bandpass tables
         |          gainfield=['nearest',''],                # nearest
           on sky for gcal
         |          interp=['nearest','nearest,linear'],     # nearest
           in time for gcal
         |          calwt=True)                              # calibrate
           the weights

      Next, calibrate the science target with explicit gainfield
      selection for the gain caltable, and linear interpolation in time:

      .. container:: casa-input-box

         | applycal(vis='n5921.ms',
         |          field='2',                               # science
           field
         |          spw='',                                  # all
           channels
         |          gaintable=['n5921.gcal','n5921.bcal']    # gain and
           bandpass tables
         |          gainfield=['1',''],                      # field 1
           calibrates field 2 for gcal table
         |          interp=['linear','nearest,linear'],      # linear in
           time for gcal
         |          calwt=True)                              # calibrate
           the weights
         |  

       

       

       

       

       

       

       

       

       

       

       

       

       

.. container:: section
   :name: viewlet-below-content-body
