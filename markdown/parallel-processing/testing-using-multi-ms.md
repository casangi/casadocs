

# Tests with Multi-MS 

How to create and run functional tests using Multi-MSs

\--CASA Developer\--

This document is a quick guide on how to run CASA functional tests using Multi-MSs. The Multi-MS (MMS) data sets are not stored in the data repository as to avoid duplicating space. Each developer can create a reference set of Multi-MSs for their tests and use them when updating the code.

<div class="alert alert-info">
**NOTE**: The user needs to start CASA with *mpicasa* in order to run it in parallel. Note that in most of the functional tests, the execution will not be faster when running on MMS, mostly because the datasets of the tests are small and the overhead of setting up the cluster may dominate.
</div>

## 1. Create Multi-MS for the tests

There are 3 ways to create Multi-MS data sets for the functional tests (those run using the runUnitTest.py tool).

1.  Create MMS automatically for the MSs used in a particular test script.
2.  Create MMS for a given directory containing MSs.
3.  Use the partition task to have full control and create the Multi-MSs manually.

### Create Multi-MSs automatically using a script

Use the make_mmsdata.py script, which uses the **convertToMMS** class (explained in next section) to create MMS. This script will create MMS for all MSs used in a specific test using default parameters of the partition task. The developer can modify some parameters of partition when running the script. The make_mmsdata.py script is installed in \<trunk/gcwrap/scripts/python/regressions/admin\>. The make_mmsdata.py scripts contains the following options:

  ---------------------------------------------------------------------- ----------------------------------------------------------------------------------------
  *no option*     Print this message and exit.
  *\--all*        Create MMS for all tasks in TASKLIST.
  *\--ignore*     From all tasks, do no create MMS for the given \<tasks\>
  *\--list*       Print the list of tasks from TASKLIST and exit.
  *\--axis*       partition *separationaxis* to use (*spw*, *scan*, *auto*); *default=auto*
  *\--numsubms*   Number of subMSs to use when creating MMS; *default=4*
  *\<tasks\>*     Create MMS data for the given tasks. Additional tasks are separated by white spaces.  
  ---------------------------------------------------------------------- ----------------------------------------------------------------------------------------

 

Examples

**\<script-path\>** can be for CASA trunk: \<trunk/gcwrap/scripts/python/regressions/admin/\> or for a tarball: \<casa-prerelease\.../lib/python2.7/\>

 

\> Get the usage information

```
casa --c <script-path>make_mmsdata.py
```

\> List the tasks for which this script can create MMS.

```
mpicasa -n 5 <install-path>casa --c <script-path>make_mmsdata.py --list
```

\> Create MMS data for gaincal tests using the default auto *separationaxis* and 4 Sub-MSs.

```
mpicasa -n 5 <install-path>casa --c <script-path>make_mmsdata.py gaincal
```

\> Create Multi-MS data for all tasks defined in the script, except flagdata and split, and create 8 Sub-MSs.

```
mpicasa -n 5 <install-path>casa --c <script-path>make_mmsdata.py --numsubms=8 --ignore flagdata split
```

 \> Create MMS data for all tasks defined in TASKLIST using the scan *separationaxis*

```
mpicasa -n 5 <install-path>casa --c <script-path>make_mmsdata.py --axis=scan --all
```

### Create Multi-MSs semi-automatically using the convertToMMS() Python class

Use the **convertToMMS** class inside CASA directly to create Multi-MSs. This class will create MMS data for all the MeasurementSets of a given directory. It will ignore any non-MS data such as calibration tables. Start CASA with *mpicasa* and do the following:.

```
mpicasa -n 5 <install-path>casa --nogui --log2term
```

```
CASA>: import partitionhelper as ph
CASA>: ph.convertToMMS()
```

   Options:

   *inpdir* \<*dir*\>

directory with input MS.

   *mmsdir* \<*dir*\>

directory to save output MMS. If not given, it will save the MMS in a directory called mmsdir in the current directory.

   *axis=\'auto\'*

*separationaxis* parameter of partition (*spw*,*scan*,*auto*).

   *numsubms='auto'*

number of subMSs to create in output MMS

   *cleanup=False*

if True it will remove the output directory before starting.

<div class="alert alert-info">
 NOTE: this script will run using the default values of partition. It will try to create an MMS for every MS in the input directory. It will skip non-MS directories such as cal tables. If partition succeeds, the script will create a link to every non-MS file in the output directory. The script will not walk through sub-directories of *inpdir*. It will also skip files or directories that start with a .
</div>

Examples:

\> Create Multi-MSs for all MSs present in the given directory and save them to the default directory "mmsdir".

```
CASA>: ph.convertoToMMS(inpdir='$CASADATA/regressions/unittest/bandpass')
```

### Create Multi-MSs manually using partition

Run task **partition** manually to create Multi-MSs by hand inside CASA and have more control on the parameters of the task. See help **partition** for more details.

Example:

\> Start CASA with *mpicasa* to create an MMS for the Four_ants_3C286.ms test MS and select only the DATA column. Create flag backup and choose the spw *separationaxis*. Use **listpartition** to see the content of the MMS.

```
CASA >: partition('Four_and_3C286.ms', outputvis='mytest.ms', separationaxis='spw', datacolumn='DATA', flagbackup=True)
```

 

## 2. Modify the functional tests to run with Multi-MSs

In order to run the existing functional tests with a different data set, there is an option in runUnitTest.py, which will look for input data in a different location other than that defined in the tests themselves. The script runUnitTest.py will set an environmental variable called TEST_DATADIR when it is called with the option *\--datadir*. This variable can be read by the tests to use a different location for the input data sets.

Add the following lines in the beginning of the test script. See examples in test_flagdata.py.

    # Path for data
    datapath = os.environ.get('CASAPATH').split()[0] + "/data/regression/unittest/flagdata/"
    # Pick up alternative data directory to run tests on MMSs
    testmms = False
    if os.environ.has_key('TEST_DATADIR'):  
       DATADIR = str(os.environ.get('TEST_DATADIR'))+'/flagdata/'
       if os.path.isdir(DATADIR):
           testmms = True
           datapath = DATADIR
           print 'flagdata tests will use data from '+datapath      

This assumes that the MMS data is stored under a sub-directory with the task name. Most of the existing functional tests follow the recommended way of storing MSs in the data repository, under \<CASADATA\>/regression/unittest/\<taskname\>. Tests that read data from other locations need to be adjusted accordingly. One easier option is to create symbolic links to MSes from other locations to the standard place in \<CASADATA\>/regression/unittest/\<taskname\>.

The following tests already support MMS such as described above:

``` {.verbatim}
test_bandpass          test_clearstat 
test_concat            test_conjugatevis 
test_cvel2             test_flagdata 
test_fluxscale         test_gaincal 
test_gencal            test_hanningsmooth
test_listhistory       test_listobs 
test_listvis           test_plotms 
test_split             test_uvcontsub
test_virtualconcat     test_vishead
test_visstat 
```

For these tests, one only needs to create MMS and run the tests with the *\--datadir* option.

 

## 3. Run the tests with Multi-MSs

Run the tests as you normally do to check that they all pass. Create the MMSs as described in Section 1 and run the same tests on the new data sets. If the MMS are created under ./unittest_mms/\<taskname\>, run the script as follows:

```
mpicasa -n 5 <install-path>casa --c <script-path>runUnitTest.py  --datadir=./unittest_mms test_taskname
```

 

## 4. Troubleshooting

Q. The tests pass using normal MSs but fail on Multi-MSs.

A. The first thing to check is if the *separationaxis* used to **partition** the MS is appropriate to the processing done by the task.

