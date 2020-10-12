

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   .. rubric:: Examples for 'Basket-Weaving'
      
   
   ::
   
      sdfixscan(mode='fft_mask', infiles = ['scan_0deg.im',
      'scan_90deg.im'], direction=[0., 90.], maskwidth=5.0,
      outfile='basket_0_90.im')
   
      sdfixscan(mode='fft_mask', infiles = ['scan_30deg.im',
      'scan_120deg.im'], direction=[30., 120.], maskwidth=10.0,
      outfile='basket_30_120.im')
   
   
   
   .. rubric:: Example for  'Pressed-out'
      
   
   ::
   
      sdfixscan(mode='model', infiles = 'scan_0deg.im',
      direction=90., smoothsize='100arcsec', outfile='press_0.im')
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   