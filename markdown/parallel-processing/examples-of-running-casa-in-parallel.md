

# Examples parallelization 

Examples of running CASA interactively or via a script in parallel

# Parallel processing using Multi-MS (MMS) in CASA is unverified - please use at own discretion. 

### [Please consider [[parallel imaging](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallel-imaging)]{ using normal MS as alternative.]

# Examples of running CASA in parallel

The following is a list of typical examples on how to run CASA in parallel. Once CASA is started with *mpicasa* and the "Multi-MS" is created, there is basically no difference between running CASA in serial and in parallel. You can find an example of a parallelized analysis in the alma-m100-analysis-hpc-regression.py script located in a sub-directory of your CASA distribution. For example, if CASA is untarred in /home/user/casa-release-5.0.0-el6, the alma-m100 script can be found in /home/user/casa-release-5.0.0-el6/lib/python2.7/regressions/

``` {.verbatim}
  alma-m100-analysis-hpc-regression.py
```

Example 1. Run the above regression script in parallel, using 8 cores in parallel and 1 core as the MPI Client.

```
mpicasa -n 9 <path_to_casa>/casa --nogui --log2term -c alma-m100-analysis-hpc-regression.py
```

Example 2. Start CASA as described before for an interactive session, using 5 cores on the local machine.

```
mpicasa -n 5 <path_to_casa>/casa <casa-options>
```

An *xterm* will be open showing in the tile bar *rank0*. Rank 0 is where the MPIClient runs. The other 4 cores have been opened and are idle waiting for any activity to be sent to them. 

Run **importasdm** to create a "Multi-MS" and save the online flags to a file. The output will be automatically named uid\_\_A002_X888a.ms, which is an MMS partitioned across spw and scan. The online flags are saved in the file uid\_\_A002_X888a_cmd.txt.

```
CASA <2>: importasdm('uid__A002_X888a', createmms=True, savecmds=True)
```

List the contents of the MMS using **listobs**. In order to see how the MMS is partitioned, use **listpartition**.

```
CASA <3>: listobs('uid__A002_X888a.ms', listfile='uid__A002_X888a.listobs')
CASA <4>: listpartition('uid__A002_X888a.ms')
```

Apply the online flags produced by **importasdm**, using **flagdata** in list mode. flagdata is parallelized therefore each engine will work on a separated "Sub-MS" to apply the flags from the uid\_\_A002_X888a_cmd.txt file. You will see messages in the terminal (also saved in the casa-\#\#\#.log file), containing the strings MPIServer-1, MPIServer-2, etc., for all the cores that process in parallel.

```
CASA <5>: flagdata('uid__A002_X888a.ms', mode='list', inpfile='uid__A002_X888a_cmd.txt')
```

Flag auto-correlations and the high Tsys antenna also using list mode for optimization.

```
CASA <6>: flagdata('uid__A002_X888a.ms', mode='list',
                   inpfile=["autocorr=True","antenna='DA62'"])
```

Create all calibration tables in the same way as for a normal MS. Task **gaincal** is not parallelized, therefore it will work on the MMS as if it was a normal MS.

```
CASA <7>: gaincal('uid__A002_X888a.ms', caltable='cal-delay_uid__A002_X888a.K',
                  field='*Phase*',spw='1,3,5,7', solint='inf',combine='scan',
                  refant=therefant, gaintable='cal-antpos_uid__A002_X888a',
                  gaintype='K'))
```

Apply all the calibrations to the MMS. **applycal** will work in parallel on each "Sub-MS" using the available cores.

```
CASA <8>: applycal(vis='uid__A002_X888a.ms', field='0', spw='9,11,13,15',
                   gaintable=['uid__A002_X888a.tsys',
                              'uid__A002_X888a.wvr.smooth',
                              'uid__A002_X888a.antpos'],
                   gainfield=['0', '', ''], interp='linear,linear',
                   spwmap=[tsysmap,[],[]], calwt=True, flagbackup=False)
```

Split out science spectral windows. Task **split** is also parallelized, therefore it will recognize that the input is an MMS and will process it in parallel, creating also an output MMS. 

```
CASA <9>: split(vis='uid__A002_X888a.ms', outputvis='uid__A002_X888a.ms.split',
                 datacolumn='corrected', spw='9,11,13,15', keepflags=True)
```

Run **tclean** normally to create your images.

------------------------------------------------------------------------

