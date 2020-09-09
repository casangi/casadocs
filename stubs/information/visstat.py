#
# stub function definition file for docstring parsing
#

def visstat(vis, axis='amplitude', datacolumn='data', useflags=True, spw='', field='', selectdata=True, antenna='', uvrange='', timerange='', correlation='', scan='', array='', observation='', timeaverage=False, timebin='0s', timespan='', maxuvwdistance=0.0, disableparallel=False, ddistart=-1, taql='', monolithic_processing=False, intent='', reportingaxes='ddid'):
    r"""
Displays statistical information from a MeasurementSet, or from a Multi-MS

Parameters
   - vis_ (string) - Name of MeasurementSet or Multi-MS
   - axis_ (string='amplitude') - Values on which to compute statistics

      .. raw:: html

         <details><summary><i> axis = amp </i></summary>

      - datacolumn_ (string='data') - Which data column to use (data, corrected, model, float_data)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = amplitude </i></summary>

      - datacolumn_ (string='data') - Which data column to use (data, corrected, model, float_data)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = phase </i></summary>

      - datacolumn_ (string='data') - Which data column to use (data, corrected, model, float_data)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = real </i></summary>

      - datacolumn_ (string='data') - Which data column to use (data, corrected, model, float_data)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = imag </i></summary>

      - datacolumn_ (string='data') - Which data column to use (data, corrected, model, float_data)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = imaginary </i></summary>

      - datacolumn_ (string='data') - Which data column to use (data, corrected, model, float_data)

      .. raw:: html

         </details>
   - useflags_ (bool=True) - Take flagging into account?
   - spw_ (string='') - spectral-window/frequency/channel
   - field_ (string='') - Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'
   - selectdata_ (bool=True) - More data selection parameters (antenna, timerange etc)

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - antenna_ (string='') - antenna/baselines: \'\'==>all, antenna = \'3,VA04\'
      - timerange_ (string='') - time range: \'\'==>all, timerange=\'09:14:0~09:54:0\'
      - correlation_ (string='') - Select data based on correlation
      - scan_ (string='') - scan numbers: \'\'==>all
      - array_ (string='') - (sub)array numbers: \'\'==>all
      - observation_ ({string, int}='') - observation ID number(s): \'\' = all
      - uvrange_ (string='') - uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters

      .. raw:: html

         </details>
   - timeaverage_ (bool=False) - Average data in time.

      .. raw:: html

         <details><summary><i> timeaverage = True </i></summary>

      - timebin_ (string='0s') - Bin width for time averaging.
      - timespan_ ({string, stringArray}='') - Span the timebin across scan, state or both.
      - maxuvwdistance_ (double=0.0) - Maximum separation of start-to-end baselines that can be included in an average. (meters)

      .. raw:: html

         </details>
   - intent_ ({string, stringArray, int, intArray}='') - Select data by scan intent.
   - reportingaxes_ (string='ddid') - Which reporting axis to use (ddid, field, integration)


Description
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
   weight_spectrum, amp, amplitude, phase, real, imag, imaginary,and
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
   on a given subset of theMeasurementSet using selection
   parameters.

   .. note:: Note: If the MS consists of inhomogeneous data, it may be
      necessary to use selection parameters to select a homogeneous
      subset of the MS. For example, if the MS containsseveral
      spectral windows, each having a different number of
      channels,usespw='2' torun visstat onhomogenous data within
      the MS.


.. _vis:

vis (string)
   | Name of MeasurementSet or Multi-MS

.. _axis:

axis (string='amplitude')
   | Values on which to compute statistics

.. _datacolumn:

datacolumn (string='data')
   | Which data column to use (data, corrected, model, float_data)

.. _useflags:

useflags (bool=True)
   | Take flagging into account?

.. _spw:

spw (string='')
   | spectral-window/frequency/channel

.. _field:

field (string='')
   | Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'

.. _selectdata:

selectdata (bool=True)
   | More data selection parameters (antenna, timerange etc)

.. _antenna:

antenna (string='')
   | antenna/baselines: \'\'==>all, antenna = \'3,VA04\'

.. _uvrange:

uvrange (string='')
   | uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters

.. _timerange:

timerange (string='')
   | time range: \'\'==>all, timerange=\'09:14:0~09:54:0\'

.. _correlation:

correlation (string='')
   | Select data based on correlation

.. _scan:

scan (string='')
   | scan numbers: \'\'==>all

.. _array:

array (string='')
   | (sub)array numbers: \'\'==>all

.. _observation:

observation ({string, int}='')
   | observation ID number(s): \'\' = all

.. _timeaverage:

timeaverage (bool=False)
   | Average data in time.

.. _timebin:

timebin (string='0s')
   | Bin width for time averaging.

.. _timespan:

timespan ({string, stringArray}='')
   | Span the timebin across scan, state or both.

.. _maxuvwdistance:

maxuvwdistance (double=0.0)
   | Maximum separation of start-to-end baselines that can be included in an average. (meters)

.. _disableparallel:

disableparallel (bool=False)
   | Hidden parameter for internal use only. Do not change it!

.. _ddistart:

ddistart (int=-1)
   | Hidden parameter for internal use only. Do not change it!

.. _taql:

taql (string='')
   | Table query for nested selections

.. _monolithic_processing:

monolithic_processing (bool=False)
   | Hidden parameter for internal use only. Do not change it!

.. _intent:

intent ({string, stringArray, int, intArray}='')
   | Select data by scan intent.

.. _reportingaxes:

reportingaxes (string='ddid')
   | Which reporting axis to use (ddid, field, integration)


    """
    pass
