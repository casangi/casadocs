

.. _Description:

Description
   listobs task: List the summary of a data set in the logger or in a
   file
   
   This task reports various metadata related to an MS. The listing
   is sent to the logger or can be saved to a file. Standard MS
   selection parameters can be used to limit the listing (see
   `Visibility Data
   Selections <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
   for details). The task also returns a dictionary with the
   metadata; see Examples for the content and structure of the
   dictionary. Note that the dictionary does not include antenna
   related metadata.
   
   The report begins with information such as the observer, the
   project ID, the number of records, the length of the observation,
   and minimum and maxiumum timestamp of the records included.
   Following this are several tables summarizing metadata. There is a
   table which summarizes scan data (only if verbose = True), a table
   that summarizes field data, a table that summarizes spectral
   window data, a table that summarizes source data (only if verbose
   = True), and a table that summarizes antenna data. If verbose =
   False, the antenna summary will only list antenna and station
   names. If verbose = True, additional information such as the
   diameter, latitude and longitude, position relative to the array
   center, and the ITRF geocentric coordinates for each antenna will
   be listed.
   
   Should the MS have multiple array IDs and/or multiple observation
   IDs, the report will list all of these tables for each array
   ID/observation ID pair.
   
   Note: The 'Average Interval (s)' column in the scan table is the
   average of the MS's *INTERVAL* column for each scan.
   
    
   
   .. rubric:: Description of algorithm to calculate the number of
      unflagged rows
      
   
   The number of unflagged rows is only computed and reported in the
   scan and field table if *listunfl=True*. Computing these
   quantities can have a negative performance impact, especially for
   large datasets. The number of unflagged rows (the *nUnflRows*
   columns in the scans and fields portions of the listing) is
   calculated by summing the fractional unflagged bandwidth for each
   row (and hence why the number of unflagged rows, in general, is
   not an integer). Thus a row which has half of its total bandwidth
   flagged contributes 0.5 rows to the unflagged row count. A row
   with 20 of 32 channels of homogeneous width contributes 20/32 =
   0.625 rows to the unflagged row count. A row with a value of False
   in the *FLAG_ROW* column is not counted in the number of unflagged
   rows.
   
   Parameter Summary
   
   vis
   
   The measurement set to interrogate.
   
   selectdata
   
   Select a subset of data?
   
   field
   
   Field selection. Used only if selectdata = True.
   
   spw
   
   Spectral window selection. Used only if selectdata = True.
   
   antenna
   
   Antenna selection. Used only if selectdata = True.
   
   timerange
   
   Timerange selection. Used only if selectdata = True.
   
   correlation
   
   Correlation selection. Used only if selectdata = True.
   
   scan
   
   Scan selection. Used only if selectdata = True.
   
   intent
   
   Intent selection. Used only if selectdata = True.
   
   feed
   
   Feed selection. Used only if selectdata = True.
   
   array
   
   Array selection. Used only if selectdata = True.
   
   uvrange
   
   The uvrange selection. Used only if selectdata = True.
   
   observation
   
   Observation selection. Used only if selectdata = True.
   
   verbose
   
   Verbosity level. True prints more than false.
   
   listfile
   
   File name to which to save report. No file is produced if set to
   the empty string.
   
   overwrite
   
   Overwrite the specified file if it exists? Only used if listfile
   is not the empty string.
   
   listunfl
   
   Include number of unflagged rows in the field table?
   
   cachesize
   
   Experimental parameter allowing user to control the temporary
   cache size in which data are stored so they do not have to be
   recomputed. 50 MB (the default) appears to be a reasonable value
   for most cases.
   

.. _Examples:

Examples
   task examples
   
   ::
   
      | # generate standard listobs listing
      | listobs(vis="my.ms")
   
   ::
   
      | # generate listobs listing with more detail
      | listobs(vis="my.ms", verbose=True)
   
   ::
   
      | # save the listobs output into a text file
      | listobs(vis="my.ms", verbose=True, listfile="my.listobs.out")
   
   ::
   
      | # Get metadata and print it
      | metadata = listobs(vis="uid__X02_X3d737_X1_01_small.ms")
      | print(metadata)
   
   ::
   
      | {'BeginTime': 55248.126073333326, 'EndTime':
        55248.130800000006, 'IntegrationTime': 408.38400173187256,
      |  'field_0': {'code': 'none',
      |    'direction':
      |       {'m0': {'unit': 'rad', 'value': 1.4433872913993107},
      |        'm1': {'unit': 'rad', 'value': 0.2361430477948328},
      |       'refer': 'J2000', 'type': 'direction'},
      |    'name': 'J0530+135'},
      |  'field_1': {'code': 'none',
      |    'direction':
      |       {'m0': {'unit': 'rad', 'value': 0.0},
      |        'm1': {'unit': 'rad', 'value': 0.0},
      |       'refer': 'J2000', 'type': 'direction'},
      |    'name': 'Mars'},
      |  'nfields': 2, 'numrecords': 1080,
      |  'scan_1': {'0': {'BeginTime': 55248.126073333326, 'EndTime':
        55248.12846666667, 'FieldId': 0, 'FieldName': 'J0530+135',
        'IntegrationTime': 3.0240000000000187, 'SpwIds': np.array([0,
        1], dtype=np.int32), 'StateId': 0, 'nRow': 600, 'scanId':
        1}},
      |  'scan_2': {'0': {'BeginTime': 55248.12877055556, 'EndTime':
        55248.13014111111, 'FieldId': 1, 'FieldName': 'Mars',
        'IntegrationTime': 3.023999999999993, 'SpwIds': np.array([0,
        1], dtype=np.int32), 'StateId': 5, 'nRow': 360, 'scanId':
        2}},
      |  'timeref': 'UTC'}
      | }
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   
