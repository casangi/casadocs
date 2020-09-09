Description
   This application reports various metadata related to an MS. The
   listing is sent to the logger or can be saved to a file. Standard
   MS selection parameters can be used to limit the listing (see
   `Visibility Data
   Selections <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
   for details).

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
