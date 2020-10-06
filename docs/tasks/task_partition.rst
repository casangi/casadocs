

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
    
   
   Other examples of running CASA in parallel can be
   found `here <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/examples-of-running-casa-in-parallel>`__ .
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
   
   .. code:: p1
   
      cvpost001, slots=5
      cvpost002, slots=4
   
    
   
   .. rubric:: Create a Multi-MS of selected spws, partitioned per
      spw
      
   
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
   
     
   
   .. rubric:: Create a Multi-MS with only a certain channel range of
      all spws but do not back up the FLAG column
      
   
   ::
   
      partition('uid0001.ms', outputvis='fewchans.mms', spw='*:1~10',
      flagbackup=False)
   
        
   
   .. rubric:: Create a single-dish Multi-MS using the baseline axis
      only for auto-correlations
      
   
   ::
   
      partition('uid0001.ms', outputvis='myuid.ms', createmms=True,
      separationaxis='baseline', antenna='*&&&')
   
     
   
   .. note:: NOTE: If CASA is started without mpicasa, it is still possible
      to create an MMS, but the processing will be done in serial.
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   