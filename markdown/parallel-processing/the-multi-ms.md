

# The Multi-MS 

Describing a Multi-MS and how to create one

# **Parallel processing using Multi-MS (MMS) in CASA is unverified. Please use at own discretion. **

### [Please consider [parallel imaging](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallel-imaging) using normal MS as alternative.]

# Multi-MS Creation 

## **partition** 

The **partition** task is the main task to create a "Multi-MS". It takes an input MeasurementSet and creates an output "Multi-MS" based on the data selection parameters.

The inputs to **partition** are:

```
CASA <1>: inp partition
--------> inp(partition)
#partition :: Task to produce Multi-MSs using parallelism
vis                 =         ''        #Name of input MeasurementSet
outputvis           =         ''        #Name of output MeasurementSet
createmms           =       True        #Should this create a multi-MS output
     separationaxis =     'auto'        #Axis to do parallelization across(scan, spw, baseline, auto)
     numsubms       =     'auto'        #The number of SubMSs to create (auto or any number)
     flagbackup     =       True        #Create a backup of the FLAG column in the MMS.

datacolumn          =      'all'        #Which data column(s) to process.
field               =         ''        #Select field using ID(s) or name(s).
spw                 =         ''        #Select spectral window/channels.
scan                =         ''        #Select data by scan numbers.
antenna             =         ''        #Select data based on antenna/baseline.
correlation         =         ''        #Correlation: '' ==> all, correlation='XX,YY'.
timerange           =         ''        #Select data by time range.
intent              =         ''        #Select data by scan intent.
array               =         ''        #Select (sub)array(s) by array ID number.
uvrange             =         ''        #Select data by baseline length.
observation         =         ''        #Select by observation ID(s).
feed                =         ''        #Multi-feed numbers: Not yet implemented.
```

## The *createmms* parameter 

 The keyword *createmms* is by default set to True to create an output MMS. It contains three sub-parameters, *separationaxis*, *numsubms* and *flagbackup*. Partition accepts four axes to do separation across: 'auto', 'scan' 'spw' or 'baseline'. The default *separationaxis=\'auto\'* will first separate the MS in spws, then in scans. It tries to balance the spw and scan content in each Sub-MS also taking into account the available fields.

The baseline axis is mostly useful for Single-Dish data. This axis will partition the MS based on the available baselines. If the user wants only auto-correlations, she/he should use the antenna selection syntax such as *antenna=\'\*&&&\'* together with the baseline separation axis. Note that if *numsubms=\'auto\'*, the task will try to create as many Sub-MSs as the number of available parallel cores used when starting CASA with *mpicasa*. If the user wants to have one Sub-MS for each baseline, he/she should set the *numsubms* parameter to a number higher than the number of baselines to achieve this.

The user may force the number of "Sub-MSs" in the output MMS by setting the sub-parameter numsubms. The default *\'auto\'* is to create as many Sub-MSs as the number of engines used when starting CASA with *mpicasa*, in an optimized way. 

The *flagbackup* sub-parameter will create a backup of the FLAG column and save it to the .flagversions file.

## **importasdm** 

Task **partition** has been embedded in task **importasdm** so that at import time the user can already create a MMS. Set the parameter createmms to True and the output of **importasdm** will be a MMS created with default parameters. Sub-parameters separationaxis and numsubms are also available in **importasdm**. From this point on in the data reduction chain, tasks that have been parallelized will run automatically in parallel when they see an MMS and tasks that are not parallelized will work in the same way as they normally do on a MS.

 

 

