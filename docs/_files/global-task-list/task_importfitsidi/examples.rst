Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To convert a single observation spread across two FITS-IDI files
      into a single CASA MeasurementSet while treating gaps of 15
      seconds or more as scan boundaries:

      .. container:: casa-input-box

         importfitsidi(fitsidifile=['N18C1_1.IDI', 'N18C1_2.IDI'],
         vis='n18c1.ms', constobsid=True, scanreindexgap_s=15)

       

.. container:: section
   :name: viewlet-below-content-body
