Examples
========

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The following example shows how to obtain Stokes I data from XX
      and YY or from LL and RR stored in FLOAT_DATA column:

      .. container:: casa-input-box

         sdpolaverage(infile='sd_data.ms', datacolumn='float_data',
         polaverage='stokes', outfile='sd_data_pave.ms')

      While the input dataset 'sd_data.ms' contains two (XX and YY or LL
      and RR) spectra in each row, the output MS 'sd_data_pave.ms'
      should have just one (Stokes I) spectrum in each row. 

       

.. container:: section
   :name: viewlet-below-content-body
