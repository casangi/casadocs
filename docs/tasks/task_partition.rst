

.. _Description:

Description
   partition is a task that creates
   a `Multi-MS <../../notebooks/parallel-processing.ipynb#The-Multi-MS>`__ out
   of a MeasurementSet. General selection parameters are included,
   and one or all of the various data columns (DATA, FLAG_DATA and/or
   FLOAT_DATA, and possibly MODEL_DATA and/or CORRECTED_DATA) can be
   selected.
   
   The partition task creates a Multi-MS in parallel using the
   Message Passing Interface ( `MPI <http://mpi-forum.org/>`__ ),
   enabled via
   the `mpi4casa <../../notebooks/parallel-processing.ipynb#Advanced:-Interface-Framework>`__ framework.
   
   .. note:: When partition or any other task processes an MMS in parallel,
      each Sub-MS is processed independently in a parallel
      engine. The log messages of the parallel engines are identified
      by the string MPIServer- #, where # gives the number of the
      engine running that process. When the task runs sequentially,
      it shows the MPIClient text in the origin of the log messages
      or does not show anything.

   
   .. rubric:: Parameter Descriptions
   
   *vis*
   
   Name of input MeasurementSet.
   
   *outputvis*
   
   Name of output Multi-MS.
   
   *createmms*
   
   By default, this parameter is set to True to create an output
   Multi-MS, which is the basic step for running CASA in parallel.
   See more about this in the
   `Parallelization <../../notebooks/parallel-processing.ipynb>`__
   chapter. The task will obey the settings of the parameters listed
   below if set to True. If set to False, it will work as the
   **split** task and create a normal MS, split according to the
   given data selection parameters. Note that, when this parameter is
   set to False, a cluster will not be used.
   
   *separationaxis*
   
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
   
   *numsubms*
   
   The number of sub-MSs to create in the Multi-MS. The default
   'auto' is to partition the MS using the number of available
   servers in the cluster. If the task is unable to determine the
   number of running servers, or the user did not start CASA using
   mpicasa, numsubms will be set to 8 Sub-MSs as default. The user
   can create any number of Sub-MSs, regardless of the number of
   cores used to create the cluster with mpicasa.
   
   *flagbackup*

   Make a backup of the FLAG column of the output MMS. When the MMS
   is created, the `flag
   versions <../../notebooks/data_examination.ipynb#Manage-flag-versions>`__  (the
   .flagversions file) of the input MS are not transferred; therefore
   it is necessary to re-create it for the new MMS. Note that
   multiple backups from the input MS will not be preserved.
   This will create a single backup of all the flags present in the
   input MS at the time the MMS is created.
   

.. _Examples:

Examples
   Other examples of running CASA in parallel can be
   found `here <../../notebooks/parallel-processing.ipynb#Examples-parallelization>`__ .
   Use task listpartition to see the content of the Multi-MS.

   
   .. rubric:: Start CASA on a single node with 16 engines
   
   The first engine will be used as the MPIClient, where the user
   will see the CASA prompt. All other engines will be used as
   MPIServers and will process the MS in parallel.
   
   ::
   
      mpicasa -n 16 casa --nogui --log2term
   
      partition(vis='uid__A1__X33993.ms', outputvis='test.mms')

   
   .. rubric:: Run CASA on a group of nodes in a cluster
   
   ::
   
      mpicasa -hostfile user_hostfile casa ....
   
      partition(.....)
   
   where user_hostfile contains the names of the nodes and the number
   of engines to use in each one of them. Example:
   
   .. code::
   
      cvpost001, slots=5
      cvpost002, slots=4

   
   .. rubric:: Create a Multi-MS of selected spws, partitioned per spw
   
   The first example will create 4 Sub-MSs by default, if CASA is
   started with 5 engines. In the second example, use the numsubms
   parameter to force the creation of 8 Sub-MSs, with one spw per
   Sub-MS.
   
   ::
   
      mpicasa -n 5 casa ...
   
      # Ex 1: The following example will create 4 Sub-MSs by default
   
      partition('uid001.ms', outpuvis='source.mms',
                spw='1,3,5,7,9,11,13,15', separationaxis='spw')
   
      # *Ex 2: force the creation of one spw per Sub-MS*
   
      partition('uid001.ms', outpuvis='source.mms',
                spw='1,3,5,7,9,11,13,15', separationaxis='spw', numsubms=8)
   
     
   
   .. rubric:: Create a Multi-MS with only a certain channel range of all spws but do not back up the FLAG column
   
   ::
   
      partition('uid0001.ms', outputvis='fewchans.mms', spw='*:1~10',
                flagbackup=False)

   
   .. rubric:: Create a single-dish Multi-MS using the baseline axis only for auto-correlations
   
   ::
   
      partition('uid0001.ms', outputvis='myuid.ms', createmms=True,
                separationaxis='baseline', antenna='*&&&')

   
   .. note:: NOTE: If CASA is started without mpicasa, it is still possible to create an MMS, but the processing will be done in serial.
   

.. _Development:

Development
   No additional development details

