.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Split out a single channel:

      .. container:: casa-input-box

         mstransform(vis='ctb80-vsm.ms', outputvis='mychn.ms',
         datacolumn='data', spw='0:25')

      Combine the selected spws into a single output spw:

      .. container:: casa-input-box

         mstransform(vis='Four_ants.ms', outputvis='myspw.ms',
         combinespws=True, spw='0~3')

      Combine two spws and regrid one field, using two input channels to
      make one output:

      .. container:: casa-input-box

         mstransform(vis='jupiter6cm.demo.ms',outputvis='test1.ms',datacolumn='DATA',field='11',
         spw='0,1', combinespws=True, regridms=True, nchan=1, width=2)

      Combine 24 spws and regrid in frequency mode to create 21 output
      channels, change the phase center:

      .. container:: casa-input-box

         mstransform(vis='g19_d2usb_targets_line.ms',
         outputvis='test2.ms', datacolumn='DATA', combinespws=True,
         regridms=True, mode='frequency', nchan=21, start='229587.0MHz',
         width='1600kHz', phasecenter="J2000 18h25m56.09 -12d04m28.20")

      Apply Hanning smoothing to an MS:

      .. container:: casa-input-box

         mstransform(vis='g19_d2usb_targets_line.ms',
         outputvis='test3.ms', datacolumn='DATA', hanning=True)

      Change the reference frame and apply Hanning smoothing after
      combining all spws:

      .. container:: casa-input-box

         mstransform(vis='g19_d2usb_targets_line.ms',
         outputvis='test4.ms', datacolumn='DATA', combinespws=True,
         regridms=True, mode="channel", outframe="BARY",
         phasecenter="J2000 18h25m56.09 -12d04m28.20", hanning = True)

      Apply time averaging using a bin of 30 seconds on the default
      *CORRECTED* column:

      .. container:: casa-input-box

         mstransform(vis='g19_d2usb_targets_line.ms',
         outputvis='test5.ms', timeaverage=True, timebin='30s')

      Apply OTF calibration to ngc5921 using a calibration library:

      .. container:: casa-input-box

         mstransform(vis='ngc5921.ms',
         outputvis='ngc5921_calibrated.ms',docallib=True,
         callib='./ngc5921_callib.txt')

      The calibration file (ngc5921_callib.txt) used in the above
      example contains the following information:

      ::

         caltable='ngc5921_regression/ngc5921.bcal' calwt=True tinterp='nearest' 
         caltable='ngc5921_regression/ngc5921.fluxscale' calwt=True tinterp='nearest' fldmap='nearest' 
         caltable='ngc5921_regression/ngc5921.gcal' calwt=True field='0' tinterp='nearest' fldmap=[0] 
         caltable='ngc5921_regression/ngc5921.gcal' calwt=True field='1,2' tinterp='linear' fldmap='1' 

       

       

.. container:: section
   :name: viewlet-below-content-body
