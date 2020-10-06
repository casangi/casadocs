

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To smooth the caltable 'n4826_16apr.gcal' on a 3-hour timescale
   with a boxcar mean (and plot the result with **plotcal**):
   
   ::
   
      | smoothcal(vis='n4826_16apr.ms',
      |           tablein='n4826_16apr.gcal',
      |           caltable='n4826_16apr.smoothcal',
      |           smoothtime=7200.,
      |           smoothtype='mean')
   
      | plotcal(caltable='n4826_16apr.gcal',xaxis='time',yaxis='amp',antenna='1',subplot=211)
      | plotcal(caltable='n4826_16apr.smoothcal',xaxis='time',yaxis='amp',antenna='1',subplot=212)
   
   This yields the following figure:
   
   |image1|
   
   .. note:: **NOTE**: The first solution at the left end of the plot is for
      a different field, and so it is not smoothed together with the
      rest of the solutions.
   
   .. |image1| image:: _apimedia/18a289edf865eab608514029e04e275b0824a968.png
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   