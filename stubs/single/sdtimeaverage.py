#
# stub function definition file for docstring parsing
#

def sdtimeaverage(infile, datacolumn='float_data', field='', spw='', timerange='', scan='', antenna='', timebin='all', timespan='scan', outfile=''):
    r"""
Average SD data, perform time averaging

Parameters
   - infile_ (string) - name of input SD dataset
   - datacolumn_ (string='float_data') - name of data column to be used ["data", "float_data", or "corrected_data"]
   - field_ (string='') - select data by field IDs and names, e.g. "3C2*" (""=all)
   - spw_ (string='') - select data by spectral windows and channels, e.g. "3,5,7" (""=all)
   - timerange_ (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   - scan_ (string='') - select data by scan numbers, e.g. "21~23" (""=all)
   - antenna_ (string='') - antenna IDs to be averaged over, e.g. "PM03" (""=all)
   - timebin_ (string='all') - bin width for time averaging.
   - timespan_ (string='scan') - span across scan, state or both.
   - outfile_ (string='') - name of output file


Description




         Task **sdtimeaverage**is used for averaging SD spectral
         data over specified time or all the data and export output
         MS. Data selection is available. Please see parameters.

          Task sdtimeaverage is a wrapper task of mstransform.
         sdtimeaveraging provides spectral data averaging in a simple
         way.

          When All the spectra data is to be averaged,
         timebin='all' option is available. This option
         automatically obtains the actual time range, then internally
         executes mstransform.

         

         If the parameter is not specified, sdtimeaverage uses the
         default values. If specified output MS already exist,
         sdtimeaverage does not overwrite.

         

         

         --------------

      Parameter Descriptions
      .. rubric:: timebin(default : ' ' (all))     
         

      The timebin parameter will perform time averaging in the
      specified bin width.

      .. warning:: **Warning:** the timebin parameter works based on wall clock
         time, not integration time. For example, if each scan is 5
         seconds long, and scans are separated by 15 seconds, then
         timebin='25s' is the minimum value needed to combine data
         from 2 consecutive scans. One might assume that
         timebin='10s' should work to combine two 5 second scans, but
         it does not.

      

      .. rubric:: timespan(default : 'scan')
         

      | The timespan parameter will span the timebin across scans,
        states or both.
      | State is equivalent to sub-scans and one scan may have
        several state IDs.

      -  'scan': average data regardless of scan
      -  'state': average data regardless of state
      -  'scan, state':average data regardless of both scan and
         state
      -  ' ':   average dataover each scan and each state
         separately

      .. warning:: | **Warning:** The timespan subparameter = 'scan,scate'
           performs average of the data regardless of scan and state.
           In some cases, data of ON-scan and OFF-scan are to be
           averaged.
         | If the TELESCOPE NAME in specified MS contains 'ALMA',
           then mstransform automatically changes timescan = 'scan
           state'.

      

      .. rubric:: timerange (default : ' ' (all))    
         

      The timerange parameterspecifies thedata based on time
      range.

      .. warning:: **Warning:** timerange is prior than timebin, do not use
         timerange when timebin='all' is desired.

      

      .. rubric:: datacolumn (default : 'float_data')
         

      If 'float_data' does not exist, 'data is used instead.


.. _infile:

infile (string)
   | name of input SD dataset

.. _datacolumn:

datacolumn (string='float_data')
   | name of data column to be used ["data", "float_data", or "corrected_data"]

.. _field:

field (string='')
   | select data by field IDs and names, e.g. "3C2*" (""=all)

.. _spw:

spw (string='')
   | select data by spectral windows and channels, e.g. "3,5,7" (""=all)

.. _timerange:

timerange (string='')
   | select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)

.. _scan:

scan (string='')
   | select data by scan numbers, e.g. "21~23" (""=all)

.. _antenna:

antenna (string='')
   | antenna IDs to be averaged over, e.g. "PM03" (""=all)

.. _timebin:

timebin (string='all')
   | bin width for time averaging.

.. _timespan:

timespan (string='scan')
   | span across scan, state or both.

.. _outfile:

outfile (string='')
   | name of output file


    """
    pass
