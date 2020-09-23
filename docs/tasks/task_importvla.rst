

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To import all K-band data from two archival VLA data-sets and
   write them out in a single MeasurementSet, taking into account all
   bands (and placing them in different spectral windows), applying
   the system temperatures and excluding the auto-correlations:
   
   ::
   
      importvla(archivefiles=['inputfile1','inputfile2'],
      vis='output.ms', bandname='K', applytsys=True, autocorr=False)
   

.. _Development:

Development
   