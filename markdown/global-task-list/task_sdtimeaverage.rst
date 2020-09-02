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
