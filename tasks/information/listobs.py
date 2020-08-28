#
# stub function definition file for docstring parsing
#

def listobs(vis, selectdata=True, spw='', field='', antenna='', uvrange='', timerange='', correlation='', scan='', intent='', feed='', array='', observation='', verbose=True, listfile='', listunfl=False, cachesize=50, overwrite=False):
    r"""
List the summary of a data set in the logger or in a file

Parameters
   - **vis** (string) - Name of input visibility file (MS)
   - **selectdata** (bool) - Data selection parameters
   - **verbose** (bool) - Controls level of information detail reported. True reports more than False.
   - **listfile** (string) - Name of disk file to write output. Default is none (output is written to logger only).
   - **listunfl** (bool) - List unflagged row counts? If true, it can have significant negative performance impact.
   - **cachesize** (double) - EXPERIMENTAL. Maximum size in megabytes of cache in which data structures can be held.

Subparameters
   *selectdata = True*

   - **field** (string='', stringArray) - Selection based on field names or field index numbers. Default is all.
   - **spw** (string='', stringArray) - Selection based on spectral-window/frequency/channel.
   - **antenna** (string='', stringArray) - Selection based on antenna/baselines. Default is all.
   - **timerange** (string='', stringArray) - Selection based on time range. Default is entire range.
   - **correlation** (string='', stringArray) - Selection based on correlation. Default is all.
   - **scan** (string='', stringArray) - Selection based on scan numbers. Default is all.
   - **intent** (string='', stringArray) - Selection based on observation intent. Default is all.
   - **feed** (string='', stringArray) - Selection based on multi-feed numbers: Not yet implemented
   - **array** (string='', stringArray) - Selection based on (sub)array numbers. Default is all.
   - **uvrange** (string='', stringArray) - Selection based on uv range. Default: entire range. Default units: meters.
   - **observation** (string='', int) - Selection based on observation ID. Default is all.

   *listfile != ''*

   - **overwrite** (bool=False) - If True, tacitly overwrite listfile if it exists.


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
         :name: description-of-algorithm-to-calculate-the-number-of-unflagged-rows

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

    """
    pass
