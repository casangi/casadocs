

.. _Description:

Description
   Converts a FITS file with visibility data from the Giant Metrewave
   Radio Telescope (GMRT) into a CASA MeasurementSet (MS).
   
   GMRT flag files can also be read and applied using the *flagfile*
   parameter.


.. _Examples:

Examples
   The following example shows how visibility data from the GMRT that
   is stored in a FITS file can be imported into CASA:
   
   ::
   
      importgmrt(fitsfile='fitsfile.fits', flagfile=['gmrt_flagfile1.flag','gmrt_flagfile2.flag'], vis='outputvis.ms')
   
   This imports GMRT visibilities from FITS file *'* fitsfile.fits',
   applies flagging that is captured in the two flag files
   'gmrt_flagfile1.flag' and 'gmrt_flagfile2.flag', and writes out
   the unflagged visibilites in MeasurementSet 'outputvis.ms'.
   
   .. note:: Don't forget to manually flag autocorrections using
      **flagdata** with *autocorr = True*
   

.. _Development:

Development
   No additional development details

