#
# stub function definition file for docstring parsing
#

def visstat(vis, axis='amplitude', datacolumn='data', useflags=True, spw='', field='', selectdata=True, antenna='', uvrange='', timerange='', correlation='', scan='', array='', observation='', timeaverage=False, timebin='0s', timespan='', maxuvwdistance=0.0, disableparallel=False, ddistart=-1, taql='', monolithic_processing=False, intent='', reportingaxes='ddid'):
    r"""
Displays statistical information from a MeasurementSet, or from a Multi-MS

Parameters
   - **vis** (string) - Name of MeasurementSet or Multi-MS [1]_
   - **axis** (string='amplitude') - Values on which to compute statistics [2]_

      .. raw:: html

         <details><summary><i> axis = amp </i></summary>

      - **datacolumn** (string='data') - Which data column to use (data, corrected, model, float_data) [3]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = amplitude </i></summary>

      - **datacolumn** (string='data') - Which data column to use (data, corrected, model, float_data) [3]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = phase </i></summary>

      - **datacolumn** (string='data') - Which data column to use (data, corrected, model, float_data) [3]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = real </i></summary>

      - **datacolumn** (string='data') - Which data column to use (data, corrected, model, float_data) [3]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = imag </i></summary>

      - **datacolumn** (string='data') - Which data column to use (data, corrected, model, float_data) [3]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> axis = imaginary </i></summary>

      - **datacolumn** (string='data') - Which data column to use (data, corrected, model, float_data) [3]_

      .. raw:: html

         </details>
   - **useflags** (bool=True) - Take flagging into account? [4]_
   - **spw** (string='') - spectral-window/frequency/channel [5]_
   - **field** (string='') - Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\' [6]_
   - **selectdata** (bool=True) - More data selection parameters (antenna, timerange etc) [7]_

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - **antenna** (string='') - antenna/baselines: \'\'==>all, antenna = \'3,VA04\' [8]_
      - **timerange** (string='') - time range: \'\'==>all, timerange=\'09:14:0~09:54:0\' [10]_
      - **correlation** (string='') - Select data based on correlation [11]_
      - **scan** (string='') - scan numbers: \'\'==>all [12]_
      - **array** (string='') - (sub)array numbers: \'\'==>all [13]_
      - **observation** ({string, int}='') - observation ID number(s): \'\' = all [14]_
      - **uvrange** (string='') - uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters [9]_

      .. raw:: html

         </details>
   - **timeaverage** (bool=False) - Average data in time. [15]_

      .. raw:: html

         <details><summary><i> timeaverage = True </i></summary>

      - **timebin** (string='0s') - Bin width for time averaging. [16]_
      - **timespan** ({string, stringArray}='') - Span the timebin across scan, state or both. [17]_
      - **maxuvwdistance** (double=0.0) - Maximum separation of start-to-end baselines that can be included in an average. (meters) [18]_

      .. raw:: html

         </details>
   - **intent** ({string, stringArray, int, intArray}='') - Select data by scan intent. [23]_
   - **reportingaxes** (string='ddid') - Which reporting axis to use (ddid, field, integration) [24]_


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




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of MeasurementSet or Multi-MS
.. [2] 
   **axis** (string='amplitude')
      | Values on which to compute statistics
.. [3] 
   **datacolumn** (string='data')
      | Which data column to use (data, corrected, model, float_data)
.. [4] 
   **useflags** (bool=True)
      | Take flagging into account?
.. [5] 
   **spw** (string='')
      | spectral-window/frequency/channel
.. [6] 
   **field** (string='')
      | Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'
.. [7] 
   **selectdata** (bool=True)
      | More data selection parameters (antenna, timerange etc)
.. [8] 
   **antenna** (string='')
      | antenna/baselines: \'\'==>all, antenna = \'3,VA04\'
.. [9] 
   **uvrange** (string='')
      | uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters
.. [10] 
   **timerange** (string='')
      | time range: \'\'==>all, timerange=\'09:14:0~09:54:0\'
.. [11] 
   **correlation** (string='')
      | Select data based on correlation
.. [12] 
   **scan** (string='')
      | scan numbers: \'\'==>all
.. [13] 
   **array** (string='')
      | (sub)array numbers: \'\'==>all
.. [14] 
   **observation** ({string, int}='')
      | observation ID number(s): \'\' = all
.. [15] 
   **timeaverage** (bool=False)
      | Average data in time.
.. [16] 
   **timebin** (string='0s')
      | Bin width for time averaging.
.. [17] 
   **timespan** ({string, stringArray}='')
      | Span the timebin across scan, state or both.
.. [18] 
   **maxuvwdistance** (double=0.0)
      | Maximum separation of start-to-end baselines that can be included in an average. (meters)
.. [19] 
   **disableparallel** (bool=False)
      | Hidden parameter for internal use only. Do not change it!
.. [20] 
   **ddistart** (int=-1)
      | Hidden parameter for internal use only. Do not change it!
.. [21] 
   **taql** (string='')
      | Table query for nested selections
.. [22] 
   **monolithic_processing** (bool=False)
      | Hidden parameter for internal use only. Do not change it!
.. [23] 
   **intent** ({string, stringArray, int, intArray}='')
      | Select data by scan intent.
.. [24] 
   **reportingaxes** (string='ddid')
      | Which reporting axis to use (ddid, field, integration)

    """
    pass
