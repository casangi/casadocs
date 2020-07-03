.. container::
   :name: viewlet-above-content-title

Parallel Calibration
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   List of internally parallelized calibration tasks

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container::

         .. rubric:: Parallel processing using Multi-MS (MMS) in CASA is
            unverified - please use at own discretion.
            :name: parallel-processing-using-multi-ms-mms-in-casa-is-unverified---please-use-at-own-discretion.

         .. rubric:: Please consider\ `parallel
            imaging <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallel-imaging>`__\ using
            normal MS as alternative.
            :name: please-consider-parallel-imaging-using-normal-ms-as-alternative.

      .. container::

          

      .. container::

         Some of the calibration tasks are internally parallelized and
         will run in parallel if the input MS is a Multi-MS. Other tasks
         are not and will work normally in the presence of an input MMS.
         A typical calibration cascade will work normally in parallel
         when it sees an input MMS. In order to do that, the first step
         is to set *createmms=True* inside **importasdm** to create a
         Multi-MS. Once that is done, the calibration steps will
         distribute the processing in parallel if CASA is started with
         **mpicasa**, or in serial otherwise.

      .. container::

          

      .. container::

         Contrary to the MS, the calibration tables created by
         calibration tasks are not partitioned. For instance, when
         **gaincal** is run on a Multi-MS, it will create the same
         output **gaincal** table as if the input was a normal MS.

      .. container::

          

      .. container::

         The following calibration tasks are internally parallelised and
         will work on each Sub-MS in parallel.

      .. container::

         .. container::

            flagdata

         .. container::

            setjy

         .. container::

            applycal

         .. container::

            hanningsmooth

         .. container::

            cvel2

         .. container::

            uvcontsub

         .. container::

            mstransform

         .. container::

            split

         .. container::

             

         .. rubric:: Special considerations when running some tasks in
            parallel
            :name: special-considerations-when-running-some-tasks-in-parallel

         .. rubric:: uvcontsub
            :name: uvcontsub

         .. container::

            When the input is a
            `Multi-MS <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms>`__
            and CASA is started in parallel using
            `mpicasa <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallelization-control>`__,
            **uvcontsub** will try to process each Sub-MS in parallel.
            Depending on the parameters of uvcontsub and the separation
            axis of the partitioned Multi-MS, processing the input in
            parallel is not possible. This will happen for example when
            the input MMS is separated using the default axis 'auto'.
            The 'auto' axis will partition the MMS  by the scan and spw
            axes, in a way to balance the content on each Sub-MS.

         .. container::

             

         .. container::

            If **uvcontsub** is called with combine='spw', the task will
            expect to find all selected spws in each Sub-MS, as each
            parallel engine will process a Sub-MS independently of the
            others. In such cases, task uvcontsub will issue some
            warnings that the process cannot be continued in parallel.
            The task will internally handle such cases and will continue
            to process the input in serial, as if the Multi-MS was a
            normal monolithic MS.

         .. container::

             

         .. container::

            The following steps can be informed in order to find out
            what is the partition axis of the MMS and what is the
            content of each Sub-MS. First, use task
            `listpartition <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_listpartition>`__
            to obtain information on the MMS.

         .. container::

            .. container:: casa-input-box

               | CASA <2>: listpartition('combspw.mms')
               | INFO listpartition::::@almahpc05:MPIClient
               | INFO listpartition::::@almahpc05:MPIClient+
                 ##########################################
               | INFO listpartition::::@almahpc05:MPIClient+ ##### Begin
                 Task: listpartition #####
               | INFO listpartition::::@almahpc05:MPIClient
                 listpartition(vis="combspw.ms",createdict=False,listfile="")
               | INFO listpartition::::@almahpc05:MPIClient This is a
                 Multi-MS with separation axis = scan,spw
               | INFO listpartition::::@almahpc05:MPIClient
                 Sub-MS              Scan Spw                
                 Nchan                     Nrows Size
               | INFO
                 listpartition::::@almahpc05:MPIClient+combspw.ms.0000.ms 
                 1    [ 1 5 6 9 12 16]    [128 128 128 128 128 128]
                 252   4.9M
               | INFO
                 listpartition::::@almahpc05:MPIClient                    
                 2    [ 0 3 13 17 18 21]  [128 128 128 128 128 128] 378
               | INFO listpartition::::@almahpc05:MPIClient
                 combspw.ms.0001.ms  1    [ 0 4 8 13 17 21]   [128 128
                 128 128 128 128] 252   4.5M
               | INFO
                 listpartition::::@almahpc05:MPIClient                    
                 2    [ 2 6 7 10 14 22]   [128 128 128 128 128 128] 378
               | INFO listpartition::::@almahpc05:MPIClient
                 combspw.ms.0002.ms  1    [ 3 7 10 14 20 22]  [128 128
                 128 128 128 128] 252   4.5M
               | INFO
                 listpartition::::@almahpc05:MPIClient                    
                 2    [ 5 11 12 15 19 23] [128 128 128 128 128 128] 378
               | INFO listpartition::::@almahpc05:MPIClient
                 combspw.ms.0003.ms  1    [ 2 11 15 18 19 23] [128 128
                 128 128 128 128] 252   4.5M
               | INFO
                 listpartition::::@almahpc05:MPIClient                    
                 2    [ 1 4 8 9 16 20]    [128 128 128 128 128 128] 378
               | INFO listpartition::::@almahpc05:MPIClient ##### End
                 Task: listpartition #####
               | INFO listpartition::::@almahpc05:MPIClient+
                 ##########################################

         .. container::

            In the above example, the MMS was partitioned using the
            default axis 'auto' (scan,spw). One can see the Sub-MSs do
            not contain all spws, therefore depending on the selection
            used in the task, it will not be possible to proceed in
            parallel. See the following example for the warnings given
            by the task in this case.

         .. container::

            .. container:: casa-input-box

               | CASA <8>:
                 uvcontsub(vis="combspw.mms",fitspw="1~10:5~122,15~22:5~122",excludechans=False,combine="spw",fitorder=0,spw="6~14",want_cont=False)
               | 2018-02-06 15:45:09 INFO
                 uvcontsub::::@almahpc05:MPIClient
               | 2018-02-06 15:45:09 INFO
                 uvcontsub::::@almahpc05:MPIClient+
                 ##########################################
               | 2018-02-06 15:45:09 INFO
                 uvcontsub::::@almahpc05:MPIClient+ ##### Begin Task:
                 uvcontsub #####
               | 2018-02-06 15:45:09 INFO
                 uvcontsub::::@almahpc05:MPIClient
                 uvcontsub(vis="combspw.mms",field="",fitspw="1~10:5~122,15~22:5~122",excludechans=False,combine="spw",
               | 2018-02-06 15:45:09 INFO
                 uvcontsub::::@almahpc05:MPIClient+
                 solint="int",fitorder=0,spw="6~14",want_cont=False)
               | 2018-02-06 15:45:11 WARN
                 uvcontsub::::@almahpc05:MPIClient Cannot run with
                 combine='spw' in parallel because the Sub-MSs do not
                 contain all the selected spws
               | 2018-02-06 15:45:11 WARN
                 uvcontsub::::@almahpc05:MPIClient The Multi-MS will be
                 processed in serial and will create an output MS
               | 2018-02-06 15:45:11 INFO
                 uvcontsub::::@almahpc05:MPIClient split is being run
                 internally, and the selected spws
               | 2018-02-06 15:45:11 INFO
                 uvcontsub::::@almahpc05:MPIClient will be renumbered to
                 start from 0 in the output!
               | 2018-02-06 15:45:11 INFO
                 uvcontsub::::@almahpc05:MPIClient Preparing to add
                 scratch columns.
               | 2018-02-06 15:45:11 INFO
                 uvcontsub::::@almahpc05:MPIClient splitting to
                 /data/users/scastro/work/CAS-10697/combspw.mms.contsubId4wzP
                 with spw="1~5,6~14,15~22"
               | 2018-02-06 15:45:11 INFO SubMS::parseColumnNames()
                 Using DATA column.

         .. container::

            A few options are possible at this stage. User can let the
            process continue in serial, which depending on the size of
            the MS, can take long, and at the end the continuum
            subtracted output will be a normal MS. Depending on what the
            user wants to do next, there is the possibility to recreate
            the MMS using task
            `partition <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_partition>`__.
            If user only wants to run tclean and create an image, having
            either MS or MMS will work in the same way because
            `tclean <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean>`__
            can run in parallel regardless whether the input is MS or
            MMS.

         .. container::

             

         .. container::

            If the users opts to recreate the MMS before running
            uvcontsub, best recommend axis to do combine='spw' is per
            scan. Partition will have to be called in the following way:

         .. container::

             

         .. container::

            .. container:: casa-input-box

               partition(vis='myMS.ms', outputvis='myout.ms',
               createmms=True, separationaxis='scan')

         .. container::

            .. rubric::  
               :name: section

            .. rubric:: flagdata (with mode='rflag')
               :name: flagdata-with-moderflag

            .. container::

               The Rflag action='calculate' can be used to produce the
               frequency and time thresholds in a first pass which can
               then be applied in a second pass, using action='apply'
               once or several times. When this is done with the
               Multi-MS structure the thresholds calculated in the first
               pass might differ from the thresholds that would be
               calculated using a single MS structure. This is due to
               the fact that in the Multi-MS structure the data are
               partitioned into Sub-MSs. The default is to produce a
               balanced partition with respect to the SPWs and scans,
               with the aim to get content from all SPWs and scans into
               each of the Sub-MSs. For this reason, the statistics
               calculated by RFlag may differ across Sub-MSs, as they
               would differ for different data selections. At the moment
               this issue has not been assessed thoroughly for
               real-world datasets. A related question that is not
               understood in detail at the moment, and that can affect
               both serial and parallel runs of RFlag, is how much the
               thresholds can differ between the single pass and dual
               pass modes of RFlag.

            .. container::

                

.. container:: section
   :name: viewlet-below-content-body
