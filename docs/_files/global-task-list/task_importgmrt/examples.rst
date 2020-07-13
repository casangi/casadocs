Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The following example shows how visibility data from the GMRT that
      is stored in a FITS file can be imported into CASA:

      .. container:: casa-input-box

         importgmrt(fitsfile='fitsfile.fits',
         flagfile=['gmrt_flagfile1.flag','gmrt_flagfile2.flag'],
         vis='outputvis.ms')

      This imports GMRT visibilities from FITS file *'* fitsfile.fits',
      applies flagging that is captured in the two flag files
      'gmrt_flagfile1.flag' and 'gmrt_flagfile2.flag', and writes out
      the unflagged visibilites in MeasurementSet 'outputvis.ms'.

      .. container:: info-box

         **NOTE**: Don't forget to manually flag autocorrections using
         **flagdata** with *autocorr = True*

       

.. container:: section
   :name: viewlet-below-content-body
