Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To list the available keywords in a MeasurementSet:

      .. container:: casa-input-box

         vishead(vis='measurementset.ms',mode='list')

       

      To get the values for the phase center:

      .. container:: casa-input-box

         vishead(vis='measurementset.ms',mode='get',hdkey='ptcs',hdindex
         = '1')

      In this example, hdvalue [0][0] gives the RA,
      while hdvalue [0][1] gives the DEC in field '1'.

       

      To get the name for field 2:

      .. container:: casa-input-box

         vishead(vis='measurementset.ms',mode='get',hdkey='field',hdindex='2')

       

      To change the name for field 2 into "junk".

      .. container:: casa-input-box

         vishead(vis='measurementset.ms',mode='put',hdkey='field',hdindex='2',hdvalue='junk')

       

      .. container:: info-box

         NOTE: To transfer the parameters to useful python items
         requires some care. Changing a number (e.g. RA of field=1 to
         0.5 radian) may be complicated to figure out.

       

.. container:: section
   :name: viewlet-below-content-body
