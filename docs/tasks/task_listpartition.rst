

.. _Description:

Description
   task description
   
   Lists the contents of a
   `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__
   according to the way it has been partitioned. The list will show
   the following properties: Sub-MS name, scans, spws, number of
   channels per spw, number of rows of each scan within a Sub-MS and
   the size of the Sub-MS on disk. The task will also list the
   separation axis of the Multi-MS.
   
    
   
   .. rubric:: Parameter descriptions
      
   
   .. rubric:: vis
      
   
   Name of Multi-MS or normal MeasurementSet
   
   .. rubric:: createdict
      
   
   Create and return a dictionary listing the content of the Multi-MS
   according to the way it was partitionted. If set to True, the
   returned dictionary will contain information
   from **ms.getscansummary** () and
   **ms.getspectralwindowinfo** (), with the addition of an index as
   the top key and the Sub-MS name. The default is set to False. The
   following is an example of a returned dictionary:
   
   ::
   
      CASA <1> listpartition('ngc5921.ms', createdict=True)
   
      | INFO    listpartition::::+     
        ##########################################
      | INFO    listpartition::::+      ##### Begin Task:
        listpartition      #####
      | INFO    listpartition::::      
        listpartition(vis="ngc5921.mms",createdict=True,listfile="")
   
      | 
      | INFO    listpartition::::       This is a Multi-MS with
        separation axis = scan
      | INFO    listpartition::::       Sub-MS               Scan 
        Spw    Nchan  Nrows   Size
      | INFO    listpartition::::+      ngc5921.mms.0000.ms  1    
        [0]    [63]   4509    25M
      | INFO    listpartition::::       ngc5921.mms.0001.ms  2    
        [0]    [63]   1890    11M
      | INFO    listpartition::::       ##### End Task:
        listpartition        #####
      | INFO    listpartition::::+     
        ##########################################
   
      | 
      | Out[17]:
      | {0: {'MS': 'ngc5921.mms.0000.ms',
      |   'scanId': {1: {'nchans': array([63], dtype=int32),
      |     'nrows': 4509,
      |     'spwIds': array([0], dtype=int32)}},
      |   'size': '25M'},
      |  1: {'MS': 'ngc5921.mms.0001.ms',
      |   'scanId': {2: {'nchans': array([63], dtype=int32),
      |     'nrows': 1890,
      |     'spwIds': array([0], dtype=int32)}},
      |   'size': '11M'}}
   
   .. rubric:: listfile
      
   
   | Name of ASCII file to save the output of the task, as shown in
     the example above. If empty, it will list on the
     logger/terminal.
   |
   

.. _Examples:

Examples
   

.. _Development:

Development
   