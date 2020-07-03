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

      To smooth the caltable 'n4826_16apr.gcal' on a 3-hour timescale
      with a boxcar mean (and plot the result with **plotcal**):

      .. container:: casa-input-box

         | smoothcal(vis='n4826_16apr.ms',
         |           tablein='n4826_16apr.gcal',
         |           caltable='n4826_16apr.smoothcal',
         |           smoothtime=7200.,
         |           smoothtype='mean')

         | plotcal(caltable='n4826_16apr.gcal',xaxis='time',yaxis='amp',antenna='1',subplot=211)
         | plotcal(caltable='n4826_16apr.smoothcal',xaxis='time',yaxis='amp',antenna='1',subplot=212)

      This yields the following figure:

      |image1|

      .. container:: info-box

         **NOTE**: The first solution at the left end of the plot is for
         a different field, and so it is not smoothed together with the
         rest of the solutions.

       

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_smoothcal/smoothcal_n4826.png/@@images/54a31933-3a0e-440f-98ef-81e5cc3e3b15.png
   :class: image-inline
