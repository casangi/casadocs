.. _Description:

Description
  Export the system temperature (SYSCAL table) and gain cure (GAIN_CURVE) table
  to `ANTAB <https://www.aips.nrao.edu/cgi-bin/ZXHLP2.PL?ANTAB>`_ format.

.. _Examples:

Examples
  Example use of exportantab to extract the system temperature and gain curve information 
  from a ms (my.ms) into an ANTAB text file (my.antab)

  ::

    exportantab(vis="my.ms", antab="my.antab", write_gc=True, write_tsys=True, overwrite=False)


  Example use of exportantab to write the system temperature and gain curve to separate files
  for antennas FD, PT and OV. The system temperature table would be written to my.antab.tsys and 
  the gain curve to my.antab.gc.

  ::

    exportantab(vis="my.ms", antab="my.antab", write_gc=True, write_tsys=True, overwrite=False, mode="split", antenna="FD,PT,OV")

  Example use of exportantab to write the system temperature and gain curve tables for each antenna 
  to separate files. This would generate two files per antenna, one for the system temperature and one for
  the gain curve. For example, for antenna PT these would be in files my.antab.tsys.PT and my.antab.gc.PT.

  ::

    exportantab(vis="my.ms", antab="my.antab", write_gc=True, write_tsys=True, overwrite=False, mode="split-antenna")

  Example use of exportantab to overwrite an existing ANTAB file with the system temperature and gain curve 
  contents from my.ms into the existing file my.antab.

  ::
    
    exportantab(vis="my.ms", antab="my.antab", write_gc=True, write_tsys=True, overwrite=True)


.. _Development:

Development
   No additional development details
