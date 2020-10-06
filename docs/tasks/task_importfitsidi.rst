

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To convert a single observation spread across two FITS-IDI files
   into a single CASA MeasurementSet while treating gaps of 15
   seconds or more as scan boundaries:
   
   ::
   
      importfitsidi(fitsidifile=['N18C1_1.IDI', 'N18C1_2.IDI'],
      vis='n18c1.ms', constobsid=True, scanreindexgap_s=15)
   

.. _Development:

Development
   