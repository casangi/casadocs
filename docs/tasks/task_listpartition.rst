

.. _Returns:

   partition (dict) - description of how the contents of a Multi-MS
   have been partitioned, with sub-MS names, scans, spws, size, etc.


.. _Description:

Description
   Returns and lists to the logger the contents of a `Multi-MS
   <../../notebooks/parallel-processing.ipynb#The-Multi-MS>`__
   according to the way it has been partitioned. The list will show
   the following properties: Sub-MS name, scans, spws, number of
   channels per spw, number of rows of each scan within a Sub-MS and
   the size of the Sub-MS on disk. The task will also list the
   separation axis of the Multi-MS.

   
   .. rubric:: Parameter descriptions
   
   *vis*
   
   Name of Multi-MS or normal MeasurementSet
   
   *createdict*
   
   Create and return a dictionary listing the content of the Multi-MS
   according to the way it was partitionted. If set to True, the
   returned dictionary will contain information
   from **ms.getscansummary** () and
   **ms.getspectralwindowinfo** (), with the addition of an index as
   the top key and the Sub-MS name. The default is set to False. The
   following is an example of a returned dictionary:
   
   ::
   
      CASA <1> listpartition('ngc5921.ms', createdict=True)
   
      INFO    listpartition::::+
      ##########################################
      INFO    listpartition::::+      ##### Begin Task: listpartition      #####
      INFO    listpartition::::
      listpartition(vis="ngc5921.mms",createdict=True,listfile="")

      INFO    listpartition::::       This is a Multi-MS with separation axis = scan
      INFO    listpartition::::       Sub-MS               Scan Spw    Nchan  Nrows   Size
      INFO    listpartition::::+      ngc5921.mms.0000.ms  1 [0]    [63]   4509    25M
      INFO    listpartition::::       ngc5921.mms.0001.ms  2 [0]    [63]   1890    11M
      INFO    listpartition::::       ##### End Task: listpartition        #####
      INFO    listpartition::::+ ##########################################
   

      Out[17]:
      {0: {'MS': 'ngc5921.mms.0000.ms',
        'scanId': {1: {'nchans': array([63], dtype=int32),
          'nrows': 4509,
          'spwIds': array([0], dtype=int32)}},
        'size': '25M'},
       1: {'MS': 'ngc5921.mms.0001.ms',
        'scanId': {2: {'nchans': array([63], dtype=int32),
          'nrows': 1890,
          'spwIds': array([0], dtype=int32)}},
        'size': '11M'}}


   *listfile*
   
   Name of ASCII file to save the output of the task, as shown in
   the example above. If empty, it will list on the
   logger/terminal.


.. _Examples:

Examples
   A multi-measurement set (MMS) is an MS that has been split into
   sub-MSs. An MMS contains a reference MS in the top directory and
   the sub-MSes are located in a directory called SUBMSS inside the
   MMS directory.
   
   Example of a MS that was partitioned in the 'scan' axis using the
   task **partition**:
   
   ::
   
      > ls ngc5921.mms
      ANTENNA           FLAG_CMD     POLARIZATION  SPECTRAL_WINDOW  table.dat
      DATA_DESCRIPTION  HISTORY      PROCESSOR     STATE            table.info
      FEED              OBSERVATION  SORTED_TABLE  SUBMSS           WEATHER
      FIELD             POINTING     SOURCE        SYSCAL
   
   ::
   
      > ls ngc5921.mms/SUBMSS/
      ngc5921.0000.ms/  ngc5921.0002.ms/  ngc5921.0004.ms/ ngc5921.0006.ms/
      ngc5921.0001.ms/  ngc5921.0003.ms/  ngc5921.0005.ms/
   
   The task lists the following properties of a multi-MS or MS:
   sub-MS name, scan, spw list, list of number of channels per spw,
   number of rows for each scan and the size on disk.
   
   **listpartition** task example:
   
   ::
   
      CASA <1> listpartition('ngc5921.ms', createdict=True)
   
      INFO    listpartition::::+ ##########################################
      INFO    listpartition::::+      ##### Begin Task: listpartition      #####
      INFO    listpartition:::: listpartition(vis="ngc5921.mms",createdict=True,listfile="")

      INFO    listpartition::::       This is a Multi-MS with separation axis = scan
      INFO    listpartition::::       Sub-MS               Scan   Spw    Nchan  Nrows   Size
      INFO    listpartition::::+      ngc5921.mms.0000.ms  1 [0]    [63]   4509    25M
      INFO    listpartition::::       ngc5921.mms.0001.ms  2 [0]    [63]   1890    11M
      INFO    listpartition::::       ##### End Task: listpartition        #####
      INFO    listpartition::::+      ##########################################

      Out[17]:
      {0: {'MS': 'ngc5921.mms.0000.ms',
        'scanId': {1: {'nchans': array([63], dtype=int32),
          'nrows': 4509,
          'spwIds': array([0], dtype=int32)}},
        'size': '25M'},
       1: {'MS': 'ngc5921.mms.0001.ms',
        'scanId': {2: {'nchans': array([63], dtype=int32),
          'nrows': 1890,
          'spwIds': array([0], dtype=int32)}},
        'size': '11M'}}
   
   Example of logger output:
   
   ::
   
      Sub-MS          Scan  Spw      Nchan    Nrows   Size
      ngc5921.0000.ms  1    [0]      [63]     4509    11M
      ngc5921.0001.ms  2    [0]      [63]     1890    6.4M
      ngc5921.0002.ms  3    [0]      [63]     6048    13M
      ngc5921.0003.ms  4    [0]      [63]     756     4.9M
      ngc5921.0004.ms  5    [0]      [63]     1134    6.4M
      ngc5921.0005.ms  6    [0]      [63]     6804    15M
      ngc5921.0006.ms  7    [0]      [63]     1512    6.4M

   

.. _Development:

Development
   No additional development details

