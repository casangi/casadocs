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

      To plot amplitude and phase as a fuction of time on two panels of
      a single page, for 'G' solutions in a caltable called
      'ngc5121.usecase.fluxscale':

      .. container:: casa-input-box

         | plotcal(caltable='ngc5921.usecase.fluxscale',
         |         xaxis='time',yaxis = 'amp',
         |         subplot = 211)
         | plotcal(caltable='ngc5921.usecase.fluxscale',
         |         xaxis='time',yaxis = 'phase',
         |         subplot = 212)

      The result is shown in the following figure: |image1|

       

       

       

      Similarly, to plot amplitude, phase and SNR as a function of
      frequency on a three-panel plot, for a 'B' solution for a single
      antenna stored in 'ngc5921.usecase.bcal':

      .. container:: casa-input-box

         | plotcal(caltable='ngc5921.usecase.bcal',antenna='0',
         |         xaxis='freq',yaxis='amp',
         |         subplot=311)
         | plotcal(caltable='ngc5921.usecase.bcal',antenna='0',
         |         xaxis='freq',yaxis='phase',
         |         subplot=312)
         | plotcal(caltable='ngc5921.usecase.bcal',antenna='0',
         |         xaxis='freq',yaxis='snr',
         |         subplot=313)

      This will generate the following figure:

      |image2|

       

       

      To show one amplitude vs. freq bandpass per plot, with 6 plots per
      page, iterating over antennas:

      .. container:: casa-input-box

         | plotcal(caltable='ngc5921.usecase.bcal',antenna='0',
         |         xaxis='freq',yaxis='amp',
         |         iteration='antenna',subplot=231)

       This will generate the following figure:

      |image3|

       

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_plotcal/plotcal_n5921_g_2panel.png/@@images/3acb229a-bb54-4be5-9d67-d803215fe4da.png
   :class: image-inline
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_plotcal/plotcal_n5921_b_3panel.png/@@images/6e980754-7983-4339-bc9d-ed01240b422f.png
   :class: image-inline
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_plotcal/plotcal_n5921_b_6panel.png/@@images/5e8a36ad-0ab6-4dad-93b3-864833b333f9.png
   :class: image-inline
