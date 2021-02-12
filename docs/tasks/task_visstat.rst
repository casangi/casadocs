

.. _Description:

Description
   This task returns a dictionary with statistical information about
   data in a MeasurementSet or Multi-MS.
   
   The following statistics are computed and added to the returned
   dictionary: mean value, minimum value, maximum value, sum of
   values, sum of squared values, sum of weights, median, median
   absolute deviation, first and third quartiles, minimum, maximum,
   variance, standard deviation, and root mean square. Two other
   fields indicate whether the data are weighted and whether they are
   masked. The field 'npts' gives the number of data points. The
   parameter 'doquantiles' can be set to False to show the
   statistical output excluding quantiles, which significantly
   decreases the run-time of visstat.
   
   Statistics may be computed on any of the following axes: flag,
   antenna1, antenna2, feed1, feed2, field_id, array_id,
   data_desc_id, flag_row, interval, scan, scan_number, time, weight,
   weight_spectrum, amp, amplitude, phase, real, imag, imaginary, and
   uvrange (weight, amp, imag and scan are aliases for
   weight_spectrum, amplitude, imaginary and scan_number,
   respectively) Note that the statistics are computed on scalar
   values only; for example, the average amplitude is computed as a
   scalar average.
   
   Additionally, statistics for any axis may be computed on subsets
   of the MeasurementSet partitioned by values of data description
   id, field id or integration number. The 'reportingaxes' argument
   is used to partition the sample set along an axis. For example,
   setting its value to 'ddid' will result in the statistics of the
   chosen sample values partitioned by unique values of the data
   description id. Thus setting 'axis' to 'amp' and 'reportingaxes'
   to 'ddid' will report statistics of visibility amplitudes for each
   unique value of data description id in the MeasurementSet.
   
   When the 'reportingaxes' argument is used to partition the data,
   if one of the partitions is completely flagged and useflags=True,
   the returned report for that partition will have the number of
   points set to zero and the statistics set to 'NaN'. For example,
   if partitionaxes ='field', a list of fields is given, and some of
   the fields are completely flagged, the number of points reported
   for those fields will be 0 and their statistics 'NaN'.
   
   Besides returning the statistical information in a dictionary,
   this task prints the statistics to the CASA logger. When no valid
   data is found for some of the 'reportingaxes' selections, it
   prints a warning about it.
   
   Optionally, the statistical information can be computed based only
   on a given subset of the MeasurementSet using selection
   parameters.
   
   .. note:: Note: If the MS consists of inhomogeneous data, it may be
      necessary to use selection parameters to select a homogeneous
      subset of the MS. For example, if the MS contains several
      spectral windows, each having a different number of
      channels, use spw='2' to run visstat on homogenous data within
      the MS.
   

.. _Examples:

Examples
   To create and view a dictionary called 'mystat' containing the
   visibility statistics of ngc5921.ms:
   
   ::
   
      CASA <1>: mystat = visstat(vis='data/regression/unittest/setjy/ngc5921.ms',
                                 axis='amp', datacolumn='data', useflags=False, spw='',
                                 field='', selectdata=True, correlation='RR', timeaverage=False,
                                 intent='', reportingaxes='ddid')
   
      CASA <2>: mystat
   
   ::
   
      Out[2]:
      {'DATA_DESC_ID=0': {'firstquartile': 0.023732144385576248,
        'isMasked': False,
        'isWeighted': False,
        'max': 73.75,
        'maxDatasetIndex': 12,
        'maxIndex': 1204,
        'mean': 4.511831488357214,
        'medabsdevmed': 0.0432449858635664,
        'median': 0.051963627338409424,
        'min': 2.2130521756480448e-05,
        'minDatasetIndex': 54,
        'minIndex': 4346,
        'npts': 1427139.0,
        'rms': 16.42971891790897,
        'stddev': 15.798076313999745,
        'sum': 6439010.678462409,
        'sumOfWeights': 1427139.0,
        'sumsq': 385235713.187832,
        'thirdquartile': 0.3004012107849121,
        'variance': 249.57921522295976}}
   
   To access only the standard deviation statistic:
   
   ::
   
      CASA <3>: mystat['DATA_DESC_ID=0']['stddev']
   
   ::
   
      Out[3]: 15.798076313999745
   

.. _Development:

Development
   No additional development details

