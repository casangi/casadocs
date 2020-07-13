Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To spectrally smooth part of a data set for both polarizations,
      selecting by frequency and scan with a boxcar kernel having a
      width of 50 channels:

      .. container:: casa-input-box

         sdsmooth(infile='sd_data.ms',spw='116~117GHz',scan='21~23',pol='0,1',kernel='boxcar',kwidth='50',antenna='PM03',outfile='sd_data_smoothed.ms',overwrite=T)

       

       

       

       

.. container:: section
   :name: viewlet-below-content-body
