

.. _Description:

Description
   

.. _Examples:

Examples
   To import NRO45m OTF data:
   
   ::
   
      infile = 'OriKLA.OriKL.20170101235959.32.Y'  # The NRO45m OTF
      data obtained using the SAM45 spectrometer has an extention of
      "Y".
      outputvis = 'OriKLA.OriKL.20170101235959.32.Y.ms'
      importnro(infile = infile, outputvis = outputvis, overwrite =
      True, parallel = False)
   

.. _Development:

Development
   