#
# stub function definition file for docstring parsing
#

def partition(vis, outputvis='', createmms=True, separationaxis='auto', numsubms='auto', flagbackup=True, datacolumn='all', field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', disableparallel=False, ddistart=-1, taql=''):
    """
Task to produce Multi-MSs using parallelism

| Partition is a task to create a Multi-MS out of an MS. General selection
|    parameters are included, and one or all of the various data columns
|    (DATA, LAG_DATA and/or FLOAT_DATA, and possibly MODEL_DATA and/or
|    CORRECTED_DATA) can be selected.
|    
|    The partition task creates a Multi-MS in parallel, using the CASA MPI framework.
|    The user should start CASA as follows in order to run it in parallel.
|    
|    1) Start CASA on a single node with 8 engines. The first engine will be used as the
|       MPIClient, where the user will see the CASA prompt. All other engines will be used
|       as MPIServers and will process the data in parallel.
|           mpicasa -n 8 casa --nogui --log2term
|           partition(.....)
|        
|    2) Running on a group of nodes in a cluster.
|           mpicasa -hostfile user_hostfile casa ....
|           partition(.....)
|            
|        where user_hostfile contains the names of the nodes and the number of engines to use 
|        in each one of them. Example:
|            pc001234a, slots=5
|            pc001234b, slots=4
|     
|    If CASA is started without mpicasa, it is still possible to create an MMS, but
|    the processing will be done in sequential.
|
|    A multi-MS is structured to have a reference MS on the top directory and a
|    sub-directory called SUBMSS, which contain each partitioned sub-MS. The
|    reference MS contains links to the sub-tables of the first sub-MS. The other
|    sub-MSs contain a copy of the sub-tables each. A multi-MS looks like this in disk.
|
|    ls ngc5921.mms
|    ANTENNA           FLAG_CMD     POLARIZATION  SPECTRAL_WINDOW  table.dat
|    DATA_DESCRIPTION  HISTORY      PROCESSOR     STATE            table.info
|    FEED              OBSERVATION  SORTED_TABLE  SUBMSS           WEATHER
|    FIELD             POINTING     SOURCE        SYSCAL
|
|    ls ngc5921.mms/SUBMSS/
|    ngc5921.0000.ms/  ngc5921.0002.ms/  ngc5921.0004.ms/  ngc5921.0006.ms/
|    ngc5921.0001.ms/  ngc5921.0003.ms/  ngc5921.0005.ms/
|
|    Inside casapy, one can use the task listpartition to list the information
|    from a multi-MS.
|    
|    When partition processes an MMS in parallel, each sub-MS is processed independently in an engine.
|    The log messages of the engines are identified by the string MPIServer-#, where # gives the number
|    of the engine running that process. When the task runs sequentially, it shows the MPIClient text
|    in the origin of the log messages or does not show anything.

Parameters
----------
vis : string
   Name of input measurement set
outputvis : string
   Name of output measurement set
createmms : bool
   Should this create a multi-MS output
datacolumn : string
   Which data column(s) to process.
field : string, stringArray, int, intArray
   Select field using ID(s) or name(s).
spw : string, stringArray, int, intArray
   Select spectral window/channels.
scan : string, stringArray, int, intArray
   Select data by scan numbers.
antenna : string, stringArray, int, intArray
   Select data based on antenna/baseline.
correlation : string, stringArray
   Correlation: '' ==> all, correlation="XX,YY".
timerange : string, stringArray, int, intArray
   Select data by time range.
intent : string, stringArray, int, intArray
   Select data by scan intent.
array : string, stringArray, int, intArray
   Select (sub)array(s) by array ID number.
uvrange : string, stringArray, int, intArray
   Select data by baseline length.
observation : string, stringArray, int, intArray
   Select by observation ID(s).
feed : string, stringArray, int, intArray
   Multi-feed numbers: Not yet implemented.

Other Parameters
----------
separationaxis : string
   Axis to do parallelization across(scan, spw, baseline, auto)
numsubms : string, int
   The number of SubMSs to create (auto or any number)
flagbackup : bool
   Create a backup of the FLAG column in the MMS.
disableparallel : bool
   Create a multi-MS in parallel.
ddistart : int
   Do not change this parameter. For internal use only.
taql : string
   Table query for nested selections

Notes
-----





   task description



      partition is a task that creates
      a `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__ out
      of a MeasurementSet. General selection parameters are included,
      and one or all of the various data columns (DATA, FLAG_DATA and/or
      FLOAT_DATA, and possibly MODEL_DATA and/or CORRECTED_DATA) can be
      selected.

      The partition task creates a Multi-MS in parallel using the
      Message Passing Interface ( `MPI <http://mpi-forum.org/>`__ ),
      enabled via
      the `mpi4casa <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/casa-parallelization-interface-mpi4casa>`__ framework.

      .. note:: When partition or any other task processes an MMS in parallel,
         each Sub-MS is processed independently in a parallel
         engine. The log messages of the parallel engines are identified
         by the string MPIServer- #, where # gives the number of the
         engine running that process. When the task runs sequentially,
         it shows the MPIClient text in the origin of the log messages
         or does not show anything.

      .. rubric::  
         :name: section
         :class: p1

      .. rubric:: Parameter Descriptions
         :name: parameter-descriptions
         :class: p1

      .. rubric:: *vis*
         :name: vis
         :class: p1

      Name of input MeasurementSet.

      .. rubric:: *outputvis*
         :name: outputvis
         :class: p1

      Name of output Multi-MS.

      .. rubric:: *createmms*
         :name: createmms

      By default, this parameter is set to True to create an output
      Multi-MS, which is the basic step for running CASA in parallel.
      See more about this in the
      `Parallelization <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__
      chapter. The task will obey the settings of the parameters listed
      below if set to True. If set to False, it will work as the
      **split** task and create a normal MS, split according to the
      given data selection parameters. Note that, when this parameter is
      set to False, a cluster will not be used.

      .. rubric:: *separationaxis*
         :name: separationaxis
         :class: p1

      Axis to do parallelization across. Namely, it is how the MS will
      be partitioned to form separated entities, called Sub-MSs.
      **partition** accepts four axes to do separation across: ’auto’,
      ’scan’, ’spw’ or ’baseline’. The default is set to 'auto',
      which will first separate the MS in spws, then in scans. It tries
      to balance the spw and scan contents in each Sub-MS, also taking
      into account the available fields so that the size in disk is also
      balanced. This is the recommended axis to partition an MS.

      -  The 'auto' option will partition the MS per scan and spw to
         obtain optimal load balancing with the following criteria:     
          

      1. Maximize the scan/spw/field distribution across sub-MSs

      2. Generate sub-MSs with similar size

      -  The 'scan' or 'spw' axes will partition the MS based on scans
         or spws. The individual sub-MSs may not be balanced with
         respect to the number of rows.
      -  The 'baseline' axis is mostly useful for Single-Dish data. This
         axis will partition the MS based on the available baselines. If
         the user wants only auto-correlations, use the antenna
         selection such as antenna='*&&&' together with this separation
         axis. Note thatif numsubms='auto', partition will try to create
         as many sub-MSs as the number of available servers in the
         cluster. If the user wants to have one sub-MS for each
         baseline, set the numsubms parameter to a number higher than
         the number of baselines to achieve this.        

      .. rubric:: *numsubms*
         :name: numsubms
         :class: p1

      The number of sub-MSs to create in the Multi-MS. The default
      'auto' is to partition the MS using the number of available
      servers in the cluster. If the task is unable to determine the
      number of running servers, or the user did not start CASA using
      mpicasa, numsubms will be set to 8 Sub-MSs as default. The user
      can create any number of Sub-MSs, regardless of the number of
      cores used to create the cluster with mpicasa.

      .. rubric:: *flagbackup*
         :name: flagbackup
         :class: p1

      Make a backup of the FLAG column of the output MMS. When the MMS
      is created, the `flag
      versions <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/managing-flag-versions-flagmanager>`__  (the
      .flagversions file) of the input MS are not transferred; therefore
      it is necessary to re-create it for the new MMS. Note that
      multiple backups from the input MS will not be preserved.
      This will create a single backup of all the flags present in the
      input MS at the time the MMS is created.

    """
    pass
