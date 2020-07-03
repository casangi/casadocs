.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Visibility Statistics
=====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Using visstat

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: MS statistics (visstat)
         :name: sec116
         :class: subsection

      The **visstat** task is provided to obtain simple statistics for a
      MeasurementSet, useful in regression tests.

      The inputs are:

      .. container:: casa-input-box

         #  visstat :: Displays statistical information from a
         MeasurementSet, or from a Multi-MS
         | vis            =     ''            #  Name of MeasurementSet
           or Multi-MS
         | axis           =     'real'        #  Which values to use
         |      datacolumn     =     'data'        #  Which data column
           to use (data, corrected, model, float_data)
         | useflags       =      False        #  Take flagging into
           account?
         | spw            =         ''        # 
           spectral-window/frequency/channel
         | field          =        '1'        #  Field names or field
           index numbers: ''==>all, field='0~2,3C286'
         | selectdata     =       True        #  More data selection
           parameters (antenna, timerange etc)
         |      antenna        =         ''        #  antenna/baselines:
           ''==>all, antenna = '3,VA04'
         |      timerange      =         ''        #  time range:
           ''==>all, timerange='09:14:0~09:54:0'
         |      correlation    =       'RR'        #  Select data based
           on correlation
         |      scan           =         ''        #  scan numbers:
           ''==>all
         |      array          =         ''        #  (sub)array
           numbers: ''==>all
         |      observation    =         ''        #  observation ID
           number(s): '' = all
         |      uvrange        =         ''        #  uv range:
           ''==>all; uvrange = '0~100klambda', default units=meters
         | timeaverage    =      False        #  Average data in time.
         | intent         =         ''        #  Select data by scan
           intent.
         | reportingaxes  =     'ddid'        #  Which reporting axis to
           use (ddid, field, integration)

       

      Running this task returns a record (Python dictionary) with the
      statistics, which can be captured in a Python variable. For
      example,

      .. container:: casa-output-box

         CASA <54>:
         mystat=visstat(vis='data/regression/unittest/setjy/ngc5921.ms',
         axis='amp', datacolumn='data', useflags=False, spw='',
         field='', selectdata=True, correlation='RR', timeaverage=False,
         intent='', reportingaxes='ddid')

         | CASA <55>: mystat
         | Out[55]:
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

         | CASA <56>: mystat['DATA_DESC_ID=0']['stddev']
         | Out[56]: 15.798076313999745

      .. code:: verbatim

         The options for axis are:

      .. container:: casa-input-box

         axis='amplitude' # or ('amp') axis='phase' axis='imag' (or
         'imaginary') axis='real'

      The phase of a complex number is in radians with range (−π, π).

.. container:: section
   :name: viewlet-below-content-body
