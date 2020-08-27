#
# stub function definition file for docstring parsing
#

def visstat(vis, axis='amplitude', datacolumn='data', useflags=True, spw='', field='', selectdata=True, antenna='', uvrange='', timerange='', correlation='', scan='', array='', observation='', timeaverage=False, timebin='0s', timespan='', maxuvwdistance=0.0, disableparallel=False, ddistart=-1, taql='', monolithic_processing=False, intent='', reportingaxes='ddid'):
    """
Displays statistical information from a MeasurementSet, or from a Multi-MS

Parameters
----------
vis : string
   Name of MeasurementSet or Multi-MS
axis : string
   Values on which to compute statistics
useflags : bool
   Take flagging into account?
spw : string
   spectral-window/frequency/channel
field : string
   Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'
selectdata : bool
   More data selection parameters (antenna, timerange etc)
timeaverage : bool
   Average data in time.
intent : string, stringArray, int, intArray
   Select data by scan intent.
reportingaxes : string
   Which reporting axis to use (ddid, field, integration)

Other Parameters
----------
datacolumn : string
   Which data column to use (data, corrected, model, float_data)
antenna : string
   antenna/baselines: \'\'==>all, antenna = \'3,VA04\'
uvrange : string
   uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters
timerange : string
   time range: \'\'==>all, timerange=\'09:14:0~09:54:0\'
correlation : string
   Select data based on correlation
scan : string
   scan numbers: \'\'==>all
array : string
   (sub)array numbers: \'\'==>all
observation : string, int
   observation ID number(s): \'\' = all
timebin : string
   Bin width for time averaging.
timespan : string, stringArray
   Span the timebin across scan, state or both.
maxuvwdistance : double
   Maximum separation of start-to-end baselines that can be included in an average. (meters)
disableparallel : bool
   Hidden parameter for internal use only. Do not change it!
ddistart : int
   Hidden parameter for internal use only. Do not change it!
taql : string
   Table query for nested selections
monolithic_processing : bool
   Hidden parameter for internal use only. Do not change it!

Notes
-----





   display statistical information from a Measurement Set, or from a
   Multi-MS



      This task returns a dictionary with statistical information about
      data in a MeasurementSet or Multi-MS.

      The following statistics are computed and added to the returned
      dictionary: mean value, minimum value, maximum value, sum of
      values, sum of squared values, sum of weights, median, median
      absolute deviation, first and third quartiles, minimum, maximum,
      variance, standard deviation, and root mean square. Two other
      fields indicate whether the data are weighted and whether they are
      masked. The field 'npts' gives the number of data points.

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

    """
    pass
