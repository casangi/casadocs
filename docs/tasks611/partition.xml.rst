partition -- Task to produce Multi-MSs using parallelism -- manipulation task
=======================================

Description
---------------------------------------

    Partition is a task to create a Multi-MS out of an MS. General selection
    parameters are included, and one or all of the various data columns
    (DATA, LAG_DATA and/or FLOAT_DATA, and possibly MODEL_DATA and/or
    CORRECTED_DATA) can be selected.
    
    The partition task creates a Multi-MS in parallel, using the CASA MPI framework.
    The user should start CASA as follows in order to run it in parallel.
    
    1) Start CASA on a single node with 8 engines. The first engine will be used as the
       MPIClient, where the user will see the CASA prompt. All other engines will be used
       as MPIServers and will process the data in parallel.
           mpicasa -n 8 casa --nogui --log2term
           partition(.....)
        
    2) Running on a group of nodes in a cluster.
           mpicasa -hostfile user_hostfile casa ....
           partition(.....)
            
        where user_hostfile contains the names of the nodes and the number of engines to use 
        in each one of them. Example:
            pc001234a, slots=5
            pc001234b, slots=4
     
    If CASA is started without mpicasa, it is still possible to create an MMS, but
    the processing will be done in sequential.

    A multi-MS is structured to have a reference MS on the top directory and a
    sub-directory called SUBMSS, which contain each partitioned sub-MS. The
    reference MS contains links to the sub-tables of the first sub-MS. The other
    sub-MSs contain a copy of the sub-tables each. A multi-MS looks like this in disk.

    ls ngc5921.mms
    ANTENNA           FLAG_CMD     POLARIZATION  SPECTRAL_WINDOW  table.dat
    DATA_DESCRIPTION  HISTORY      PROCESSOR     STATE            table.info
    FEED              OBSERVATION  SORTED_TABLE  SUBMSS           WEATHER
    FIELD             POINTING     SOURCE        SYSCAL

    ls ngc5921.mms/SUBMSS/
    ngc5921.0000.ms/  ngc5921.0002.ms/  ngc5921.0004.ms/  ngc5921.0006.ms/
    ngc5921.0001.ms/  ngc5921.0003.ms/  ngc5921.0005.ms/

    Inside casapy, one can use the task listpartition to list the information
    from a multi-MS.
    
    When partition processes an MMS in parallel, each sub-MS is processed independently in an engine.
    The log messages of the engines are identified by the string MPIServer-#, where # gives the number
    of the engine running that process. When the task runs sequentially, it shows the MPIClient text
    in the origin of the log messages or does not show anything.
      



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - Name of input measurement set
   * - outputvis
     - :code:`''`
     - Name of output measurement set
   * - createmms
     - :code:`True`
     - Should this create a multi-MS output
   * - separationaxis
     - :code:`'auto'`
     - Axis to do parallelization across(scan, spw, baseline, auto)
   * - numsubms
     - :code:`'auto'`
     - The number of SubMSs to create (auto or any number)
   * - flagbackup
     - :code:`True`
     - Create a backup of the FLAG column in the MMS.
   * - datacolumn
     - :code:`'all'`
     - Which data column(s) to process.
   * - field
     - :code:`''`
     - Select field using ID(s) or name(s).
   * - spw
     - :code:`''`
     - Select spectral window/channels.
   * - scan
     - :code:`''`
     - Select data by scan numbers.
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline.
   * - correlation
     - :code:`''`
     - Correlation: '' ==> all, correlation="XX,YY".
   * - timerange
     - :code:`''`
     - Select data by time range.
   * - intent
     - :code:`''`
     - Select data by scan intent.
   * - array
     - :code:`''`
     - Select (sub)array(s) by array ID number.
   * - uvrange
     - :code:`''`
     - Select data by baseline length.
   * - observation
     - :code:`''`
     - Select by observation ID(s).
   * - feed
     - :code:`''`
     - Multi-feed numbers: Not yet implemented.
   * - disableparallel
     - :code:`False`
     - Create a multi-MS in parallel.
   * - ddistart
     - :code:`int(-1)`
     - Do not change this parameter. For internal use only.
   * - taql
     - :code:`''`
     - Table query for nested selections


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input measurement set


outputvis
---------------------------------------

:code:`''`

Name of output measurement set


createmms
---------------------------------------

:code:`True`

Should this create a multi-MS output


separationaxis
---------------------------------------

:code:`'auto'`

Axis to do parallelization across(scan, spw, baseline, auto)


numsubms
---------------------------------------

:code:`'auto'`

The number of SubMSs to create (auto or any number)


flagbackup
---------------------------------------

:code:`True`

Create a backup of the FLAG column in the MMS.


datacolumn
---------------------------------------

:code:`'all'`

Which data column(s) to process.


field
---------------------------------------

:code:`''`

Select field using ID(s) or name(s).


spw
---------------------------------------

:code:`''`

Select spectral window/channels.


scan
---------------------------------------

:code:`''`

Select data by scan numbers.


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline.


correlation
---------------------------------------

:code:`''`

Correlation: '' ==> all, correlation="XX,YY".


timerange
---------------------------------------

:code:`''`

Select data by time range.


intent
---------------------------------------

:code:`''`

Select data by scan intent.


array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number.


uvrange
---------------------------------------

:code:`''`

Select data by baseline length.


observation
---------------------------------------

:code:`''`

Select by observation ID(s).


feed
---------------------------------------

:code:`''`

Multi-feed numbers: Not yet implemented.


disableparallel
---------------------------------------

:code:`False`

Create a multi-MS in parallel.


ddistart
---------------------------------------

:code:`int(-1)`

Do not change this parameter. For internal use only.


taql
---------------------------------------

:code:`''`

Table query for nested selections




