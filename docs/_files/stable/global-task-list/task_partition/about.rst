.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      partition is a task that creates
      a\ `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__\ out
      of a MeasurementSet. General selection parameters are included,
      and one or all of the various data columns (DATA, FLAG_DATA and/or
      FLOAT_DATA, and possibly MODEL_DATA and/or CORRECTED_DATA) can be
      selected.

      The partition task creates a Multi-MS in parallel using the
      Message Passing Interface (\ `MPI <http://mpi-forum.org/>`__\ ),
      enabled via
      the\ `mpi4casa <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/casa-parallelization-interface-mpi4casa>`__\ framework.

      .. container:: info-box

         When partition or any other task processes an MMS in parallel,
         each Sub-MS is processed independently in a parallel
         engine. The log messages of the parallel engines are identified
         by the string MPIServer-\ #, where # gives the number of the
         engine running that process. When the task runs sequentially,
         it shows the MPIClient text in the origin of the log messages
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

      Name of output Multi-MS.

      .. rubric:: *createmms*
         :name: createmms

      By default, this parameter is set to True to create an output
      Multi-MS, which is the basic step for running CASA in parallel.
      See more about this in the
      `Parallelization <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__
      chapter. The task will obey the settings of the parameters listed
      below if set to True. If set to False, it will work as the
      **split** task and create a normal MS, split according to the
      given data selection parameters. Note that, when this parameter is
      set to False, a cluster will not be used.

      .. rubric:: *separationaxis*
         :name: separationaxis
         :class: p1

      Axis to do parallelization across. Namely, it is how the MS will
      be partitioned to form separated entities, called Sub-MSs.
      **partition** accepts four axes to do separation across: ’auto’,
      ’scan’, ’spw’ or ’baseline’. The default is set to 'auto',
      which will first separate the MS in spws, then in scans. It tries
      to balance the spw and scan contents in each Sub-MS, also taking
      into account the available fields so that the size in disk is also
      balanced. This is the recommended axis to partition an MS.

      -  The 'auto' option will partition the MS per scan and spw to
         obtain optimal load balancing with the following criteria:     
          

      1. Maximize the scan/spw/field distribution across sub-MSs

      2. Generate sub-MSs with similar size

      -  The 'scan' or 'spw' axes will partition the MS based on scans
         or spws. The individual sub-MSs may not be balanced with
         respect to the number of rows.
      -  The 'baseline' axis is mostly useful for Single-Dish data. This
         axis will partition the MS based on the available baselines. If
         the user wants only auto-correlations, use the antenna
         selection such as antenna='*&&&' together with this separation
         axis. Note thatif numsubms='auto', partition will try to create
         as many sub-MSs as the number of available servers in the
         cluster. If the user wants to have one sub-MS for each
         baseline, set the numsubms parameter to a number higher than
         the number of baselines to achieve this.        

      .. rubric:: *numsubms*
         :name: numsubms
         :class: p1

      The number of sub-MSs to create in the Multi-MS. The default
      'auto' is to partition the MS using the number of available
      servers in the cluster. If the task is unable to determine the
      number of running servers, or the user did not start CASA using
      mpicasa, numsubms will be set to 8 Sub-MSs as default. The user
      can create any number of Sub-MSs, regardless of the number of
      cores used to create the cluster with mpicasa.

      .. rubric:: *flagbackup*
         :name: flagbackup
         :class: p1

      Make a backup of the FLAG column of the output MMS. When the MMS
      is created, the\ `flag
      versions <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/managing-flag-versions-flagmanager>`__\  (the
      .flagversions file) of the input MS are not transferred; therefore
      it is necessary to re-create it for the new MMS. Note that
      multiple backups from the input MS will not be preserved.
      This will create a single backup of all the flags present in the
      input MS at the time the MMS is created. 

       

.. container:: section
   :name: viewlet-below-content-body
