

.. _Description:

Description
   The **calstat** task returns statistical information about a
   column in a calibration table. The following values are computed:
   mean value, sum of values, sum of squared values, median, median
   absolute deviation, quartile, minimum, maximum, variance, standard
   deviation, root mean square. The results are printed in the CASA
   logger. The statistics info can also be captured as a python
   dictionary return variable. See the examples.
   
   At this time, it is not possible to apply selection to the
   caltable.
   
   .. rubric:: Parameters
      
   *caltable*

   Specify the name of the calibration table as a string in
   *caltable*.
   
   *axis*

   Specify the axis upon which to calculate statistics in *axis*. The
   possible values are 'amp' (or 'amplitude'), 'phase', 'real',
   'imag' (or 'imaginary'). Also, the name of any real valued
   CalTable column can be given, e.g. TIME, POLY_COEFF_AMP, REF_ANT,
   ANTENNA1, FLAG, etc.
   
   *datacolumn*
   
   For *axis='amp'*, *'amplitude'*, *'phase'*, *'real'*, *'imag'*, or
   *'imaginary'* specify the name of the column from which to extract
   the axis values and calculate statistics. E.g., for a 'G' table
   from **gaincal**, use *datacolumn='CPARAM'*.
   
   *useflags*
   
   .. warning:: NB: The *useflags* parameter is not yet implemented.
   

.. _Examples:

Examples
   To extract amplitude statistics from a 'G' caltable called
   ngc5921.demo.gcal with **calstat**:
   
   ::
   
      gstat=calstat('ngc5921.demo.gcal',axis='amp',datacolumn='CPARAM')
   
   The gstat variable will contain the following dictionary:
   
   ::
   
      {'CPARAM': {'max': 1.6031942367553711,
                  'mean': 1.4448433067117419,
                  'medabsdevmed': 0.0086394548416137695,
                  'median': 1.5732669830322266,
                  'min': 0.99916577339172363,
                  'npts': 280.0,
                  'quartile': 0.020265340805053711,
                  'rms': 1.4650156497955322,
                  'stddev': 0.24271160321065546,
                  'sum': 404.55612587928772,
                  'sumsq': 600.95579999685287,
                  'var': 0.058908922333086665}}

.. _Development:

Development
   No additional development details

