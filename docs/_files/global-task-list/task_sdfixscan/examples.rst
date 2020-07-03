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

      .. rubric:: Examples for 'Basket-Weaving'
         :name: examples-for-basket-weaving

      .. container:: casa-input-box

         sdfixscan(mode='fft_mask', infiles = ['scan_0deg.im',
         'scan_90deg.im'], direction=[0., 90.], maskwidth=5.0,
         outfile='basket_0_90.im')

         sdfixscan(mode='fft_mask', infiles = ['scan_30deg.im',
         'scan_120deg.im'], direction=[30., 120.], maskwidth=10.0,
         outfile='basket_30_120.im')

      .. rubric::  
         :name: section

      .. rubric:: Example for  'Pressed-out'
         :name: example-for-pressed-out

      .. container:: casa-input-box

         sdfixscan(mode='model', infiles = 'scan_0deg.im',
         direction=90., smoothsize='100arcsec', outfile='press_0.im')

.. container:: section
   :name: viewlet-below-content-body
