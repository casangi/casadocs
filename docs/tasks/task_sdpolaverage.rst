

.. _Description:

Description
   Averaging over different polarizations for Single Dish MS data

   Task **sdpolaverage** is used to export Single Dish MS data
   averaged over different polarizations, to obtain Stokes I from
   orthogonal autocorrelation pairs (XXYY/LLRR).

   .. rubric:: Polarization Average


   Two modes of polarizaton averaging are available. One is 'stokes'
   which is an average based on a formulation of Stokes parameter. In
   this mode, averaged data is calculated by (XX + YY) / 2 or (RR +
   LL) / 2. The other option is 'geometric', which is a conventional
   way of averaging in the field of single-dish data reduction; the
   output data is given by weighted average of XX and YY, or RR and
   LL.


.. _Examples:

Examples
   The following example shows how to obtain Stokes I data from XX
   and YY or from LL and RR stored in FLOAT_DATA column:

   ::

      sdpolaverage(infile='sd_data.ms', datacolumn='float_data',
                   polaverage='stokes', outfile='sd_data_pave.ms')

   While the input dataset 'sd_data.ms' contains two (XX and YY or LL
   and RR) spectra in each row, the output MS 'sd_data_pave.ms'
   should have just one (Stokes I) spectrum in each row.


.. _Development:

Development
   Template

   --CASA Developer--

