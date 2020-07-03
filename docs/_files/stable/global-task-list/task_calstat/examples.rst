.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task calstat examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To extract amplitude statistics from a 'G' caltable called
      ngc5921.demo.gcal with **calstat**:

      .. container:: casa-input-box

         gstat=calstat('ngc5921.demo.gcal',axis='amp',datacolumn='CPARAM')

      The gstat variable will contain the following dictionary:

      .. container:: casa-output-box

         | {'CPARAM': {'max': 1.6031942367553711,
         |             'mean': 1.4448433067117419,
         |             'medabsdevmed': 0.0086394548416137695,
         |             'median': 1.5732669830322266,
         |             'min': 0.99916577339172363,
         |             'npts': 280.0,
         |             'quartile': 0.020265340805053711,
         |             'rms': 1.4650156497955322,
         |             'stddev': 0.24271160321065546,
         |             'sum': 404.55612587928772,
         |             'sumsq': 600.95579999685287,
         |             'var': 0.058908922333086665}}

       

       

.. container:: section
   :name: viewlet-below-content-body
