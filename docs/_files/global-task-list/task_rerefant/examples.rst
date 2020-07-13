Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To apply a prioritized list of reference antennas using
      *refantmode='flex'*:

      .. container:: casa-input-box

         | rerefant(vis='n5921.ms',
         |          tablein='n5921.gcal',
         |          caltable='n5921_ea03ish.gcal',  # Output caltable
         |          refant='ea03,ea05,ea23,ea01',   # prioritized list
           of reference antennas
         |          refantmode='flex')              # flexible use of
           alternates

      To strictly apply a preferred reference antenna:

      .. container:: casa-input-box

         | rerefant(vis='n5921.ms',
         |          tablein='n5921.gcal',
         |          caltable='n5921_ea03.gcal',     # Output caltable
         |          refant='ea03',                  # the strictly
           preferred reference antenna
         |          refantmode='strict')            # strict!

       

.. container:: section
   :name: viewlet-below-content-body
