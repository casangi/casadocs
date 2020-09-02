Description
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
