

.. _Description:

Description
   

.. _Examples:

Examples
   task calstat examples
   
   To extract amplitude statistics from a 'G' caltable called
   ngc5921.demo.gcal with **calstat**:
   
   ::
   
      gstat=calstat('ngc5921.demo.gcal',axis='amp',datacolumn='CPARAM')
   
   The gstat variable will contain the following dictionary:
   
   ::
   
      | {'CPARAM': {'max': 1.6031942367553711,
      |             'mean': 1.4448433067117419,
      |             'medabsdevmed': 0.0086394548416137695,
      |             'median': 1.5732669830322266,
      |             'min': 0.99916577339172363,
      |             'npts': 280.0,
      |             'quartile': 0.020265340805053711,
      |             'rms': 1.4650156497955322,
      |             'stddev': 0.24271160321065546,
      |             'sum': 404.55612587928772,
      |             'sumsq': 600.95579999685287,
      |             'var': 0.058908922333086665}}
   

.. _Development:

Development
   task calstat developer
   
   --CASA Developer--
   
   