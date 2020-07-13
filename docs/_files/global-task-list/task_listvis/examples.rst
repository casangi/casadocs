Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To list the visibilities from the DATA column of a MeasurementSet,
      including all data from spectral windows 2 to 4 which have RR
      correlation:

      .. container:: casa-input-box

         listvis(vis='filename.ms', datacolumn='data', spw='2~4',
         selectdata=True, correlation='RR', pagerows=5,
         listfile='listfile.txt')

      The visibilities are listed with 5 rows per page and written out
      in a text file called 'listfile.txt'.

       

       

.. container:: section
   :name: viewlet-below-content-body
