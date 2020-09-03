#
# stub function definition file for docstring parsing
#

def partition(vis, outputvis='', createmms=True, separationaxis='auto', numsubms='auto', flagbackup=True, datacolumn='all', field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', disableparallel=False, ddistart=-1, taql=''):
    r"""
Task to produce Multi-MSs using parallelism

Parameters
   - **vis** (string) - Name of input measurement set
   - **outputvis** (string='') - Name of output measurement set
   - **createmms** (bool=True) - Should this create a multi-MS output

      .. raw:: html

         <details><summary><i> createmms = True </i></summary>

      - **separationaxis** (string='auto') - Axis to do parallelization across(scan, spw, baseline, auto)
      - **numsubms** ({string, int}='auto') - The number of SubMSs to create (auto or any number)
      - **flagbackup** (bool=True) - Create a backup of the FLAG column in the MMS.
      - **disableparallel** (bool=False) - Create a multi-MS in parallel.
      - **ddistart** (int=-1) - Do not change this parameter. For internal use only.
      - **taql** (string='') - Table query for nested selections

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> createmms = False </i></summary>

      - **separationaxis** (string='auto') - Axis to do parallelization across(scan, spw, baseline, auto)
      - **numsubms** ({string, int}='auto') - The number of SubMSs to create (auto or any number)
      - **flagbackup** (bool=True) - Create a backup of the FLAG column in the MMS.
      - **disableparallel** (bool=False) - Create a multi-MS in parallel.
      - **ddistart** (int=-1) - Do not change this parameter. For internal use only.
      - **taql** (string='') - Table query for nested selections

      .. raw:: html

         </details>
   - **datacolumn** (string='all') - Which data column(s) to process.
   - **field** ({string, stringArray, int, intArray}='') - Select field using ID(s) or name(s).
   - **spw** ({string, stringArray, int, intArray}='') - Select spectral window/channels.
   - **scan** ({string, stringArray, int, intArray}='') - Select data by scan numbers.
   - **antenna** ({string, stringArray, int, intArray}='') - Select data based on antenna/baseline.
   - **correlation** ({string, stringArray}='') - Correlation: '' ==> all, correlation="XX,YY".
   - **timerange** ({string, stringArray, int, intArray}='') - Select data by time range.
   - **intent** ({string, stringArray, int, intArray}='') - Select data by scan intent.
   - **array** ({string, stringArray, int, intArray}='') - Select (sub)array(s) by array ID number.
   - **uvrange** ({string, stringArray, int, intArray}='') - Select data by baseline length.
   - **observation** ({string, stringArray, int, intArray}='') - Select by observation ID(s).
   - **feed** ({string, stringArray, int, intArray}='') - Multi-feed numbers: Not yet implemented.


Description
   partition is a task that creates
   a `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__ out
   of a MeasurementSet. General selectionparameters are included,
   and one or all of the various data columns(DATA, FLAG_DATA and/or
   FLOAT_DATA, and possibly MODEL_DATA and/orCORRECTED_DATA) can be
   selected.

   The partition task creates a Multi-MS in parallelusing the
   Message Passing Interface ( `MPI <http://mpi-forum.org/>`__ ),
   enabled via
   the `mpi4casa <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/casa-parallelization-interface-mpi4casa>`__ framework.

   .. note:: When partition or any other task processes an MMS in parallel,
      each Sub-MS is processed independently in a parallel
      engine.The log messages of the parallel engines are identified
      by the string MPIServer- #, where # gives the numberof the
      engine running that process. When the task runs sequentially,
      it shows the MPIClient textin the origin of the log messages
      or does not show anything.

   

   .. rubric:: Parameter Descriptions
      

   .. rubric:: *vis*
      

   Name of input MeasurementSet.

   .. rubric:: *outputvis*
      

   Name of outputMulti-MS.

   .. rubric:: *createmms*
      

   By default, this parameter is set to True tocreate an output
   Multi-MS, which is the basic step for running CASA in parallel.
   See more about this in the
   `Parallelization <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__
   chapter. The task will obey the settings of the parameters listed
   below if set to True. If set to False, it will work as the
   **split** task and create a normal MS, split according to the
   given data selection parameters.Note that, when this parameter is
   set to False, a clusterwill not be used.

   .. rubric:: *separationaxis*
      

   Axis to do parallelization across. Namely, it is how the MS will
   be partitioned to form separated entities, called Sub-MSs.
   **partition** accepts four axes to do separation across: ’auto’,
   ’scan’, ’spw’ or ’baseline’. The default is set to 'auto',
   whichwill first separate the MS in spws, then in scans. It tries
   to balance the spw and scan contents in each Sub-MS, also taking
   into account the available fields so that the size in disk is also
   balanced. This is the recommended axis to partition an MS.

   -  The 'auto' option will partition the MS per scan and spw to
      obtain optimal load balancing with thefollowing criteria:  
      

   1. Maximize the scan/spw/field distribution across sub-MSs

   2. Generate sub-MSs with similar size

   -  The 'scan' or 'spw' axes will partition the MS based on scans
      or spws. The individual sub-MSs maynot be balanced with
      respect to the number of rows.
   -  The 'baseline' axis is mostly useful for Single-Dish data. This
      axis will partition the MSbased on the available baselines. If
      the user wants only auto-correlations, use theantenna
      selection such as antenna='*&&&' together with this separation
      axis. Note thatif numsubms='auto', partition will try to create
      as many sub-MSs as the number of availableservers in the
      cluster. If the user wants to have one sub-MS for each
      baseline, set the numsubmsparameter to a number higher than
      the number of baselines to achieve this.    

   .. rubric:: *numsubms*
      

   The number of sub-MSs to create in the Multi-MS.The default
   'auto' is to partition the MS using the number of available
   servers in the cluster.If the task is unable to determine the
   number of running servers, or the user did not start CASAusing
   mpicasa, numsubms will be set to8 Sub-MSs as default. The user
   can create any number of Sub-MSs, regardless of the number of
   cores used to create the cluster with mpicasa.

   .. rubric:: *flagbackup*
      

   Make a backup of the FLAG column of the output MMS. When theMMS
   is created, the `flag
   versions <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/managing-flag-versions-flagmanager>`__ (the
   .flagversions file) of the input MS are not transferred;therefore
   it is necessary to re-create it for the new MMS. Notethat
   multiple backups from the input MS will not be preserved.
   Thiswill create a single backup of all the flags present in the
   inputMS at the time the MMS is created.

    """
    pass
