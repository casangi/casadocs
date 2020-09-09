Description
   .. rubric:: Summary
      

   The **calstat** task returns statistical information about a
   column in a calibration table. The following values are computed:
   mean value, sum of values, sum of squared values, median, median
   absolute deviation, quartile, minimum, maximum, variance, standard
   deviation, root mean square. The results are printed in the CASA
   logger. The statistics info can also be captured as a python
   dictionary return variable. See the examples.

   At this time, it is not possible to apply selection to the
   caltable.

   .. warning:: NB: The *useflags* parameter is not yet implemented.
