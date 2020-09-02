

# Parallelization concept 

Introduction to CASA\'s parallelization concept

 The parallelization approach adopted in CASA is the so-called embarrassingly parallelization. Embarassingly parallel workload or problem is one where little or no effort is needed to separate the problem into a number of parallel tasks. This is often the case where there is little or no dependency or need for communication between those parallel tasks, or for results between them.

In order to run one analysis on multiple processors, one can parallelize the work by dividing the data into several parts ("partitioning") and then run a CASA instance on each part or[ have non-trivially parallelized algorithms, which make use of several processors within a single CASA instance. Non-trivial parallelization is presently only implemented in certain sections of the imaging code of CASA based on [OpenMP](http://www.openmp.org/ "OpenMP"), which is a shared-memory parallel programming library.]{

All other parallelization is achieved by partitioning the MeasurementSet (MS) of interest using the task **partition** or at import time using **importasdm**[. The resulting partitioned MS is called a "Multi-MS" or "MMS". The parallel processing of a Multi-MS is possible using the Message Passing Interface ([MPI](http://mpi-forum.org/ "MPI")). MPI is a standard which addresses primarily the message-passing parallel programming model in a practical, portable, efficient and flexible way.]{

<div class="alert alert-warning">
**WARNING***:* Parallel processing on multi-MSs in CASA is unverified - please use at own discretion. 
</div>

Logically, an MMS has the same structure as an MS but internally it is a group of several MSs which are virtually concatenated. Virtual concatenation of several MSs or MMSs into an MMS can also be achieved via task **virtualconcat**.

Due to the virtual concatenation, the main table of an MMS appears like the union of the main tables of all the member MSs such that when the MMS is accessed like a normal MS, processing can proceed sequentially as usual. Each member MS or "Sub-MS" of an MMS, however, is at the same time a valid MS on its own and can be processed as such. This is what happens when the MMS is accessed by a parallelized task. The partitioning of the MMS is recognized and work is started in parallel on the separate Sub-MSs, provided that the user has started CASA with mpicasa. 

The internal structure of an MMS can be inspected using task **listpartition**.

 

