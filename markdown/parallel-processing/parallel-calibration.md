

# Parallel Calibration 

List of internally parallelized calibration tasks

# Parallel processing using Multi-MS (MMS) in CASA is unverified - please use at own discretion. 

### Please consider [parallel imaging](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallel-imaging) using normal MS as alternative.

 

Some of the calibration tasks are internally parallelized and will run in parallel if the input MS is a Multi-MS. Other tasks are not and will work normally in the presence of an input MMS. A typical calibration cascade will work normally in parallel when it sees an input MMS. In order to do that, the first step is to set *createmms=True* inside **importasdm** to create a Multi-MS. Once that is done, the calibration steps will distribute the processing in parallel if CASA is started with **mpicasa**, or in serial otherwise.

 

Contrary to the MS, the calibration tables created by calibration tasks are not partitioned. For instance, when **gaincal** is run on a Multi-MS, it will create the same output **gaincal** table as if the input was a normal MS.

 

The following calibration tasks are internally parallelised and will work on each Sub-MS in parallel.

flagdata

setjy

applycal

hanningsmooth

cvel2

uvcontsub

mstransform

split

 

# Special considerations when running some tasks in parallel {#special-considerations-when-running-some-tasks-in-parallel style="font-family: 'Helvetica Neue'; font-size: 14px;"}

### uvcontsub {#uvcontsub style="font-family: 'Helvetica Neue'; font-size: 14px;"}

When the input is a [Multi-MS](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/the-multi-ms) and CASA is started in parallel using [mpicasa](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallelization-control), **uvcontsub** will try to process each Sub-MS in parallel. Depending on the parameters of uvcontsub and the separation axis of the partitioned Multi-MS, processing the input in parallel is not possible. This will happen for example when the input MMS is separated using the default axis \'auto\'. The \'auto\' axis will partition the MMS  by the scan and spw axes, in a way to balance the content on each Sub-MS.

 

If **uvcontsub** is called with combine=\'spw\', the task will expect to find all selected spws in each Sub-MS, as each parallel engine will process a Sub-MS independently of the others. In such cases, task uvcontsub will issue some warnings that the process cannot be continued in parallel. The task will internally handle such cases and will continue to process the input in serial, as if the Multi-MS was a normal monolithic MS.

 

The following steps can be informed in order to find out what is the partition axis of the MMS and what is the content of each Sub-MS. First, use task [listpartition](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_listpartition) to obtain information on the MMS.

```
CASA <2>: listpartition('combspw.mms')
INFO listpartition```:\@almahpc05:MPIClientINFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition
INFO listpartition

In the above example, the MMS was partitioned using the default axis \'auto\' (scan,spw). One can see the Sub-MSs do not contain all spws, therefore depending on the selection used in the task, it will not be possible to proceed in parallel. See the following example for the warnings given by the task in this case.

```
CASA <8>: uvcontsub(vis="combspw.mms",fitspw="1~10:5~122,15~22:5~122",excludechans=False,combine="spw",fitorder=0,spw="6~14",want_cont=False)
2018-02-06 15:45:09 INFO uvcontsub```:\@almahpc05:MPIClient2018-02-06 15:45:09 INFO uvcontsub
2018-02-06 15:45:09 INFO uvcontsub
2018-02-06 15:45:09 INFO uvcontsub
2018-02-06 15:45:09 INFO uvcontsub
[2018-02-06 15:45:11 WARN uvcontsub
[2018-02-06 15:45:11 WARN uvcontsub
2018-02-06 15:45:11 INFO uvcontsub
2018-02-06 15:45:11 INFO uvcontsub
2018-02-06 15:45:11 INFO uvcontsub
2018-02-06 15:45:11 INFO uvcontsub
2018-02-06 15:45:11 INFO SubMS::parseColumnNames() Using DATA column.

A few options are possible at this stage. User can let the process continue in serial, which depending on the size of the MS, can take long, and at the end the continuum subtracted output will be a normal MS. Depending on what the user wants to do next, there is the possibility to recreate the MMS using task [partition](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_partition). If user only wants to run tclean and create an image, having either MS or MMS will work in the same way because [tclean](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean) can run in parallel regardless whether the input is MS or MMS.

 

If the users opts to recreate the MMS before running uvcontsub, best recommend axis to do combine=\'spw\' is per scan. Partition will have to be called in the following way:

 

```
partition(vis='myMS.ms', outputvis='myout.ms', createmms=True, separationaxis='scan')
```

###   {#section style="font-family: 'Helvetica Neue'; font-size: 14px;"}

### flagdata (with mode=\'rflag\') {#flagdata-with-moderflag style="font-family: 'Helvetica Neue'; font-size: 14px;"}

The Rflag action=\'calculate\' can be used to produce the frequency and time thresholds in a first pass which can then be applied in a second pass, using action=\'apply\' once or several times. When this is done with the Multi-MS structure the thresholds calculated in the first pass might differ from the thresholds that would be calculated using a single MS structure. This is due to the fact that in the Multi-MS structure the data are partitioned into Sub-MSs. The default is to produce a balanced partition with respect to the SPWs and scans, with the aim to get content from all SPWs and scans into each of the Sub-MSs. For this reason, the statistics calculated by RFlag may differ across Sub-MSs, as they would differ for different data selections. At the moment this issue has not been assessed thoroughly for real-world datasets. A related question that is not understood in detail at the moment, and that can affect both serial and parallel runs of RFlag, is how much the thresholds can differ between the single pass and dual pass modes of RFlag.

 

