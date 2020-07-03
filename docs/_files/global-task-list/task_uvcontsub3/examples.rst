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

      Subtract the continuum of channels 10~100 and 300~350 in spw 0
      (assuming that the line is in channels 101~299). Note that we also
      exclude edge channels, e.g. the first 9 channels. We use a
      fitorder of 0 (default). 

      .. container:: casa-input-box

         uvcontsub3(vis='myMS.ms',fitspw='0:10~100;300~350')

       

       

.. container:: section
   :name: viewlet-below-content-body
