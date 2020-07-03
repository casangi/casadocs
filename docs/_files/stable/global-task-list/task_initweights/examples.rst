.. contents::
   :depth: 3
..

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

      **Example 1: **

      Initialize the WEIGHT and the SIGMA column of myMS.ms based on the
      channel widths and integration time of each visibility.
      *dowtsp=True* will create a SIGMA_SPECTRUM and WEIGHT_SPECTRUM
      column if they did not exist in the original myMS.ms. 

      .. container:: casa-input-box

         initweights(vis='myMS.ms', wtmode='nyq', dowtsp=True)

       

      **Example 2: **

      Use **initweights** to create WEIGHT_SPECTRUM column if it does
      not exist and fill the WEIGHT values into WEIGHT_SPECTRUM 

      .. container:: casa-input-box

         initweights(vis='myMS.ms', wtmode='weight') 

       and here's a call that will remove the WEIGHT_SPECTRUM column,
      but keep WEIGHT

      .. container:: casa-input-box

         initweights(vis='myMS.ms', wrtmode='delwtsp')

       

       

       

.. container:: section
   :name: viewlet-below-content-body
