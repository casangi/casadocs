

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   Compute standard deviations in circles of diameter 10arcsec around
   grid pixels spaced every 4 x 5 pixels and anchored at pixel [30,
   40], and use linear interpolation to compute values at
   non-grid-pixels:
   
   ::
   
      imdev("my.im", "sigma.im", grid=[4, 5], anchor=[30, 40],
      xlength="10arcsec", stattype="sigma", interp="lin",
      statalg="cl")
   
   Compute median of the absolute deviations from the median values
   using the z-score/Chauvenet algorithm, by fixing the maximum
   z-score to determine outliers to 5. Use cubic interpolation to
   compute values for non-grid-point pixels. Use a rectangular region
   of dimensions 5arcsec x 20arcsec centered on each grid point as
   the region in which to include pixels for the computation of stats
   for that grid point.
   
   ::
   
      imdev("my.im", "madm.im", grid=[4, 5], anchor=[30, 40],
      xlength="5arcsec", ylength="20arcsec, stattype="madm",
      interp="cub", statalg="ch", zscore=5)
   

.. _Development:

Development
   