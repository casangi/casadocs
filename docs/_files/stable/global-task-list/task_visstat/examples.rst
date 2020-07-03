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

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      To create and view a dictionary called 'mystat' containing the
      visibility statistics of ngc5921.ms:

      .. container:: casa-input-box

         CASA <1>:
         mystat=visstat(vis='data/regression/unittest/setjy/ngc5921.ms',
         axis='amp', datacolumn='data', useflags=False, spw='',
         field='', selectdata=True, correlation='RR', timeaverage=False,
         intent='', reportingaxes='ddid')

         CASA <2>: mystat

      .. container:: casa-output-box

         | Out[2]:
         | {'DATA_DESC_ID=0': {'firstquartile': 0.023732144385576248,
         |   'isMasked': False,
         |   'isWeighted': False,
         |   'max': 73.75,
         |   'maxDatasetIndex': 12,
         |   'maxIndex': 1204,
         |   'mean': 4.511831488357214,
         |   'medabsdevmed': 0.0432449858635664,
         |   'median': 0.051963627338409424,
         |   'min': 2.2130521756480448e-05,
         |   'minDatasetIndex': 54,
         |   'minIndex': 4346,
         |   'npts': 1427139.0,
         |   'rms': 16.42971891790897,
         |   'stddev': 15.798076313999745,
         |   'sum': 6439010.678462409,
         |   'sumOfWeights': 1427139.0,
         |   'sumsq': 385235713.187832,
         |   'thirdquartile': 0.3004012107849121,
         |   'variance': 249.57921522295976}}

      To access only the standard deviation statistic:

      .. container:: casa-input-box

         CASA <3>: mystat['DATA_DESC_ID=0']['stddev']

      .. container:: casa-output-box

         Out[3]: 15.798076313999745

.. container:: section
   :name: viewlet-below-content-body
