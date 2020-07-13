Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **plotprofilemap** chooses the size and number of subplots based
      on that specified by the user, though blank data in the set may
      produce unexpected results. The appearance of the blank data can
      be changed using the *plotmasked* function, as shown below.

       

      The default case for the M100 CSV data:

      .. container:: casa-input-box

         plotprofilemap(imagename='M100_TP_CO_cube.spw3.image')

      |image1|

       

      Obviously, the inner 4x5 region only, contains data that is not
      blanked. A naive solution is to select only those:

      .. container:: casa-input-box

         plotprofilemap(imagename='M100_TP_CO_cube.spw3.image',numpanels='4,5')

      |image2|

      But the masked data still persists of course, and causes the
      outer-edges to be blanked. A solution is to set
      *plotmasked='none'*:

      .. container:: casa-input-box

         plotprofilemap(imagename='M100_TP_CO_cube.spw3.image',plotmasked='none')

      |image3| 

      Which produces a plot that focuses only on the emission.

       

       

.. |image1| image:: 8ee9bc833d57e9f01375e4974c2833c2f15b64a8.png
   :class: image-inline
   :width: 420px
   :height: 316px
.. |image2| image:: 67255e06643ff3f7320e412611835aa4b8624d72.png
   :class: image-inline
   :width: 412px
   :height: 310px
.. |image3| image:: 4b9eaef3de2494f54104e9f6a891ab1407c95730.png
   :class: image-inline
   :width: 411px
   :height: 309px
