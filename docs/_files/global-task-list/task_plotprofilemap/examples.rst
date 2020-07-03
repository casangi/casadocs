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

       

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_plotprofilemap/nxydefault_pm_def-1.png/@@images/ef3add58-ce6a-48c9-92dd-0dec4f08cb32.png
   :class: image-inline
   :width: 420px
   :height: 316px
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_plotprofilemap/nxy45_pm_def.png/@@images/54b0b126-e274-4573-92b8-065b88845ba8.png
   :class: image-inline
   :width: 412px
   :height: 310px
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_plotprofilemap/nxydefault_pm_none-1.png/@@images/ae8b3732-b18c-48f2-aacd-d4d28b6e57b2.png
   :class: image-inline
   :width: 411px
   :height: 309px
