

# Known Issues 

Important information concerning this version of CASA

### Summary Most Important Issues (details below)

-   The task **clean** is no longer being actively maintained; instead, **tclean** is now the recommended task for imaging.
-   Wideband and widefield imaging in **tclean** are only partially validated - please use at own risk and read [wideband](https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging) and [widefield](https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam) documentation.
-   When imaging large mosaics with *mosweight* in **tclean**, an error *\"too many open files\"* may occur that may require to increase the limit for open files.
-   **stawt** may fail when the correlator integration time changes within an MS and statwt is run with timebin set to an integer value.
-   CASA is not using *LD_LIBRARY_PATH* anymore but *CASALD_LIBRARY_PATH* to avoid confusion.      
-   **cvel** is calculating the velocity incorrectly for ephemeris objects. We recommend to use **mstransform** or its offspring **cvel2**, although the latter should be used with care as it is not fully commissioned yet.
-   When running CASA with the pipeline option *\'casa \--pipeline\'*, **plotcal** may not show all plots and comes up with an error message. Use CASA without *\'\--pipeline\'* when performing interactive data reduction.
-   **fixvis** uses the small angle approximation and may be incorrect for large phase shifts. Use **tclean** for phase center shifts during imaging when applicable. 
-   With parallel calibration on MMS files, **fixvis** does not write out the the new MMS specified in *outputvis* correctly, hence fixvis solutions are not applied when writing to a new MMS.
-   In **fringefit**, calibration tables created with CASA 5.5 and before cannot be used with CASA 5.6 and later.
-   In **tclean**, defining image cubes in optical velocity in some cases is known not to work.

 

## Installation

### RedHat 6

-   If you use a version of RHEL6 with a kernel version that is older than 2.6 you may encounter an error like:

    
    
    ``` {.code-java}
    E0324 17:24:18.576966686   27444 tcp_server_posix.cc:65]     check for SO_REUSEPORT: 
    {"created":"@1585038258.576951288","description":"OS Error","errno":92,"file":
    "src/core/lib/iomg/socket_utils_common_posix.cc","file_line":168,"os_error":"Protocol 
    not available","syscall":"setsockopt(SO_REUSEPORT)"}
    ```
    
    

    We recommend updating to the latest release of RHEL6.

### NFS mounted disks

-   It is not recommended that you run CASA (e.g. have your data) on disks that are NFS mounted. It can be done, but in some cases the files will be NFS locked and this can crash CASA or its tasks. In this case, you have to restart CASA.
-   If you receive messages like xvfb timeout you may try to clean out your /tmp folder, then restart CASA.

### Ipython: 

-   Due to changes in the new version of IPython, CASA 5.1 no longer includes the current directory in the PYTHONPATH. In the previous versions of CASA, to import a file named \"filename.py\" from the current directory, one would merely type in CASA: *import filename*        That no longer works because the current directory is not searched as a possible location for Python files. So, you must now add the current directory to the PYTHONPATH. This may be done by including in your .casa/init.py file a line calling the sys.path.append() function with two single quote characters (not a double quotation mark) as the argument: *sys.path.append(\'\')*        Alternatively, after starting CASA, one could simply issue a command to update the path by typing    *import sys*    *sys.path = \[\'\'\] + sys.path*    where the characters within the brackets are again two single quotes representing the empty string, which means \"current directory\" to Python.

```{=html}
<!-- -->
```
-   A bug in ipython (v. 5.1.0) can cause error messages like below. This error occassionally happens when using *tget*. This is an ipython issue when the databases are not synchronized in their line numbering and will start a new log file. The next ipython update will likely contain a fix.  
    ```python
    ERROR! Session/line number was not unique in database. History logging moved to new session 318

    CASA <2>:

    ERROR! Session/line number was not unique in database. History logging moved to new session 318
    ```
-   Files in the current directory with the same name as ipython files will cause errors like this error that occurs when a *new.py* file exists in the current directory:    ```python
    ``` {.code-java"}
    AttributeError                            Traceback (most recent call last) 
    /lib/python2.7/site-packages/IPython/core/interactiveshell.pyc in enable_matplotlib(self, gui)                                                                                                             
       2945                 gui, backend = pt.find_gui_and_backend(self.pylab_gui_select)                                            
       2946                                                                                                                          
    -> 2947         pt.activate_matplotlib(backend)                                                                                  
       2948         pt.configure_inline_support(self, backend)                                                                       
       2949                                                                                                                          

    /lib/python2.7/site-packages/IPython/core/pylabtools.pyc in activate_matplotlib(backend)                                                                                                                   
        292     matplotlib.rcParams['backend'] = backend                                                                             
        293                                                                                                                          
    --> 294     import matplotlib.pyplot                                                                                             
        295     matplotlib.pyplot.switch_backend(backend)                                                                            
        296                                                                                                                          

    /lib/python2.7/site-packages/matplotlib/pyplot.py in <module>()
         21 from matplotlib.cbook import dedent, silent_list, is_string_like, is_numlike                                  
         22 from matplotlib import docstring                                                                              
    ---> 23 from matplotlib.figure import Figure, figaspect                                                               
         24 from matplotlib.backend_bases import FigureCanvasBase                                                         
         25 from matplotlib.image import imread as _imread                                                                

    /lib/python2.7/site-packages/matplotlib/figure.py in <module>()
         16 import artist                                                                                                 
         17 from artist import Artist, allow_rasterization                                                                
    ---> 18 from axes import Axes, SubplotBase, subplot_class_factory                                                     
         19 from cbook import flatten, allequal, Stack, iterable, is_string_like                                          
         20 import _image                                                                                                 

    /lib/python2.7/site-packages/matplotlib/axes.py in <module>()
       8452                                                                                                             
       8453 # This is provided for backward compatibility                                                               
    -> 8454 Subplot = subplot_class_factory()                                                                           
       8455                                                                                                             
       8456 docstring.interpd.update(Axes=martist.kwdoc(Axes))                                                          
    ```
    ```

### Scripting:

-   Starting CASA 6: For *\"execfile\"* calls within a script which itself is run via *\"execfile\"*, it is necessary to add *globals()* as the second argument to those *\"execfile\"* calls in order for the nested script to know about the global variables of the calling script. For example, within a script *\'mainscript.py\'*, calls to another script *\'myscript.py\'* should be written as follows: *execfile(\'myscript.py\', globals())* .

 

 

## Calibration

#### **statwt **

-   In some circumstances when an MS data selection is specified, *chanbin* is not equal to the default value of *spw*,  and the WEIGHT_SPECTRUM or SIGMA_SPECTRUM columns don\'t exist, the **statwt** task may need to be run twice in order to complete successfully due to a known issue with initializing the WEIGHT_SPECTRUM and/or SIGMA_SPECTRUM columns in the code. In these circumstances, an exception will be raised with instructions to restart the task. If you are using the tool method, first close the ms tool, then reopen it using the same data set, apply the same selection, and then run **ms.statwt()**.

#### **bandpass**

-   Currently, **bandpass** will not find good solutions if any correlation (including cross-correlation) in the data is completely flagged. As an interim solution one may split the unflagged data in a separate file and then perform **bandpass**

#### **polcal**

-   Polarization position angle calibration *poltype=\'X\'* or *\'Xf\'* will be sensitive to any unmodelled position shift in the specified calibrator linear polarization model relative to the centroid location of total intensity (typically the phase center).  Excess phase due to the position shift will introduce a bias in the cross-hand phase calibration (which is the same as position angle calibration in the circular feed basis).   For this reason, it is best to use truly point-like (in all polarizations) calibrators, if possible, or accurate resolved models.

#### **setjy**

-   Sometimes **setjy** does not properly overwrite a current model in the header of the ms (virtual scratch column). It is recommended to use **delmod** if a model exists and shall be overwritten.

#### **plotcal** (also check the matplotlib section for **plotcal** issues)

-   When **plotcal** does not release a calibration table properly but keeps it locked, try to hit the quit button in the plotcal GUI first. Then redisplay the table.
-   If you use **plotcal** on a caltable, it will then be put into the cache of the table system. If you try to re-run a solve (e.g. **gaincal**, **bandpass**, **blcal**, **polcal**) with the same caltable name and *append=F* to overwrite, then when it tries to delete the original caltable it cannot due to the cache. You will see an error like:    ```python
    SEVERE  gaincal::Calibrater::solve
    Caught exception: Invalid Table operation: SetupNewTable
    ngc5921.demo.gcal is already opened
    (is in the table cache)
    ```

    Either use a different output caltable name, or restart your CASA session (exit and start again) to free up the cache. You can use the **rmtables** task to delete tables.           
-   BPOLY solutions from **bandpass** must be plotted versus frequency and not channel. BPOLY and B solutions can only be overlaid if *xaxis = \'freq\'.*
-   GSPLINE and G solutions from **gaincal** can be overlaid, though this has not been extensively tested.
-   Currently, **plotcal** needs to know the MS from which the caltable was derived to get indexing information. It does this using the name stored inside the table, which does not include the full path, but assumes the MS is in the same directory as the cal-table and has the same name it had when the caltable was created.
-   If there are flagged channels at the lower edge of the data, say, 0\~4, and you select a channel and *\'locate\'* it from plotcal, it will give the incorrect channel number (will count from the first unflagged channel, not zero).

#### **uvcontsub**

-   *fitorder* should be kept low (\<= 1) unless the line band is relatively narrow compared to the fit bands. If the image rms markedly rises in the middle line channels after **uvcontsub**, fito*rder* should probably be lowered.
-   *fitorder* \> 0 does not work with *solint* \> \'int\'

#### **mstransform**

-   SPW combination (*combinespws=True*) requires that all the SPWs selected have the same number of channels.

#### **CASA cal library **

-   The CASA cal library (*docallib=True* in **applycal**, **gaincal**, **bandpass**, etc.) may exhibit problems when calibration is unavailable for a subset of MS spectral windows.  Use of *spwmap* to (transparently, harmless) supply nominal calibration for these spectral windows may help avoid this problem.  For antenna position corrections, try *spwmap*=\[0\] to relieve a variety of this problem.

#### **VLA Switched Power**

-   In CASA v4.2.2 and higher, the weight calibration for EVLA switched power/Tsys corrections is still being investigated. Visibility corrections are ok. Since switched power calibration is not used by the EVLA pipeline (except for requantizer gain corrections, for which this problem is irrelevant), and since *calwt=F* remains the general recommendation, users should rely on **statwt** to generate appropriate data weights.

#### **fringefit **

-   Correcting for dispersive atmospheric delays in wideband and low-frequency fringe-fitting is not yet implemented in CASA. An additional column has been added to the FringeJones tables to make this possible in the future, but values are set to zero until the dispersive delay determination is implemented in CASA. As a result fringefit calibration tables created with CASA 5.5 and before cannot be used with CASA 5.6 and later. Attempting to apply old fringefit calibration tables in CASA 5.6 will fail with an error about non-confirming array sizes. Additionally the version of plotcal in CASA 5.6 will not plot calibration tables generated by CASA 5.5 or earlier; older versions of plotcal will also not plot CASA 5.6 fringefit tables correctly.

#### **fixvis**

-   **fixvis** uses the small angle approximation and may be incorrect for large phase shifts. This may result in sources shifting position if large phase shifts are being applied (shifts up to a few beam sizes have been reported). Please use **tclean** for phase center shifts during imaging when applicable. 
-   With parallel calibration on multi-MS (MMS) files, **fixvis** does not write out the *outputvis* correctly, hence fixvis solutions are not applied when writing to a new MMS. The recommended work-around solution is to over-write the input MMS by leaving the *outputvis* parameter empty. This will change the input MMS, so if you are concerned about that, we recommend to make a copy before running fixvis in parallel mode. Writing output MS files in serial mode is not affected by this bug.

#### **cvel**

-   **cvel** is calculating the velocity incorrectly for ephemeris objects. We recommend to use **mstransform** or its offspring **cvel2**, although the latter should be used with care as it is not fully commissioned yet.
-   **cvel** fails on MMS files used for parallel processing. We recommend to use **mstransform** or its offspring **cvel2**, although the latter should be used with care as it is not fully commissioned yet.

 

## Synthesis Imaging

#### **clean**

-   The task **clean** is no longer being actively maintained; instead, **tclean** is now the recommended task for imaging. For Known Issues on **clean**, see [previous CASA Docs versions](https://casa.nrao.edu/../casadocs/casa-5.4.1/introduction/known-issues).

#### **tclean**

-   Generic problems putting multiple MSs into **tclean** that have mismatches in their shape: Recently, generic problems have been found with putting multiple MSs into **tclean** when there are mismatches in shape across the data set. For example, certain data columns may cause a segment fault if they are present in only some of the input data sets. And for mosaics, please specify the phasecenter explicitly, otherwise tclean will select the first pointing from the first MS. Other mismatches in shape across multiple input MSs may cause similar problem in tclean. The CASA team is in the process of coherently addressing these issues for CASA 5.7. Please contact the [Helpdesk](https://casa.nrao.edu/../help_desk_all.shtml) if you experience related issues that you cannot otherwise solve.

```{=html}
<!-- -->
```
-   In **tclean**, if *gridder='awproject'* is run with *psterm=True*, the output Primary Beam currently still includes the Prolate Spheroidal function. In order to do a primary beam correction, a separate PB needs to be made with *psterm=False*. See the CASA pages on [AWproject](https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam) for more information.

```{=html}
<!-- -->
```
-   For widefield imaging in **tclean**, the following features still need to implemented and commissioned (for *usepointing=True*, with full heterogenous pointing support):
    -   *gridder=\'mosaic\'* : Enable accurate pointing corrections for baselines with antennas pointing in different directions
    -   *gridder=\'awproject\'* : Enable a parameter called *\'pointingoffsetsigdev\'* to trigger an antenna clustering algorithm that identifies classes of antennas based on pointing direction and applies accurate heterogeneous pointing corrections for baselines containing antennas pointing in the same direction as well as in two different directions. (This will be the official solution for VLASS 1.1 imaging.)

```{=html}
<!-- -->
```
-   In **tclean**, the gridders *'mosaic\'* and *\'awproject\'* include aperture illumination functions in the gridding convolution functions used for the PSF generation.  Although this strictly follows the math, it has several undesirable features especially in the situation where data are not uniform across all axes across which they are being combined (i.e. if the mosaic pattern is not relatively flat, if the center of the image has no mosaic pointing, if different pointings have drastically different uv-coverages or frequency coverages). All such variations cause the PSFs to be position-dependent and could relate to potential instabilities during deconvolution, either requiring many major cycles to converge or diverging.  For spectral-cube imaging, the effects are lower because PSFs are normalized to peak 1 no matter what their raw peak values are. For multi-term imaging, the ratios between the spectral PSF central values matter and the effect/error is enhanved. When all these uv-coverage variations are avoided (in careful simulations), both algorithms perform as expected for joint wideband mosaics (both with *conjbeams=True* or *False*). For CASA 5.6, the guidelines are:    -   Full-field, single pointing imaging (spectral cube as well as multi-term) will be accurate as long as the image phase center matches the PB pointing center.  
    -   For multi-term wideband joint mosaics, we recommend the use of *gridder=\'awproject\'* with *conjbeams=True* as that is the only combination that has demonstrated accurate wideband pb-correction (at *niter=0*) especially in the presence of position-dependent uv-coverage. All other options will need monitoring and several major cycles to ensure convergence.  The image should ideally be centered on a PB center.
    -   For spectral cube joint mosaics, both gridders are usable. The effects of PSF position dependence are limited to shape differences (i.e. the peak values and fluxes will still be correct). The most validated mode is for ALMA mosaics (via the pipeline) that uses gridder=\'mosaic\' with spectral cubes.

```{=html}
<!-- -->
```
-   In **tclean**, the mosweight parameter for multi-field imaging has a new default value of *mosweight=True* as of CASA 5.4. This new mosweight default is invoked for any multi-field imaging, but currently has the unwanted behavior that it only shows up on the command line when using *gridder='mosaic'*. The new default setting of *mosweight=True* in tclean optimizes noise characteristics for Briggs/uniform weighting, but one should be aware that it has the following disadvantages:
    -   it may potentially cause memory issues for large VLA mosaics
    -   the major and minor axis of the synthesized beam may be up to \~10% larger than with *mosweight=False*

   Please change to *mosweight=False* to get around these issues.

-   In CASA 5.5, when imaging mosaics with a large number of fields and many MSs in **tclean**, an error can occur that specifies *"too many open files"*. This can happen for both manual and pipeline imaging when using the *'mosweight=True'* parameter. The reason is that in CASA 5.5, a trade-off was made to reduce memory demands in tclean when using mosweight, by placing the weights on disk using multiple files. Unfortunately, this memory fix may cause open file problems for data sets consisting of many MSs and fields. The problem has been characterized in CASA 5.5 based on the number of MSs and fields: with respect to earlier CASA releases, the imager code now uses *\"\#MSs x \#fields x 2\"* additional files. As a rule of thumb, if the limit of number of files open is 4096, then the *"too many open files"* error occurs when \#MSs x \#fields \>= 1500.         While the CASA team is working on a permanent solution for a future CASA version, the recommended work-around solution for CASA 5.5 is to manually increase the limit for the number of open files, e.g.:  *ulimit -Sn 8000*. In some cases, increasing the hard-limit on number of open files may be necessary, which requires admin/root permissions.   

          The official ALMA Cycle-6 pipeline version is CASA 5.4.0, which does not have this issue.

-   In **tclean**, setting *conjbeams=True* results in a small offsets in RA and dec compared to correct RA and dec that are obtained when setting *conjbeams=False*. Our initial tests show that the offset in dec is of the order \~50 milli-arcsec, while the offset in RA is a function of declination, but also amounting to \~50mas. This issue is currectly being investigated.

```{=html}
<!-- -->
```
-   When using the parameter *perchanweightdensity = True*, the speed of **tclean** is slower when using Briggs and uniform weighting compared to natural weighting by a factor of \~3.5.

```{=html}
<!-- -->
```
-   Currently the parameter type of *niter* is defined as an integer, therefore the integer value larger than 2147483647 will not be set properly as it causes an overflow.

```{=html}
<!-- -->
```
-   Using *deconvolver=\'mtmfs\'*, *nterms=1* and *specmode=cube* does not yet work in parallel imaging mode.

```{=html}
<!-- -->
```
-   In **tclean**, defining image cubes in optical velocity in some cases is known not to work. This problem is under investigation.

```{=html}
<!-- -->
```
-   The *awproject* gridder in **tclean** does not support the virtual model scheme.

```{=html}
<!-- -->
```
-   When using interactive tclean when running tclean, please do not use the option *\"Zoom Out To Entire Screen\"* in the CASA Viewer. This will close the interactive tclean and will hang your CASA session.

```{=html}
<!-- -->
```
-   Interactive **tclean** only works when a region or mask is selected in the CASA Viewer. There is a known bug that when a region is first selected, and then de-selected to produce an empty mask (filled with zeros), the CASA Viewer that runs interactive tclean will still allow you to proceed, and tclean will detect an empty mask and stop. Please always mark a region/mask to continue interactive tclean (if the entire image should be cleaned, draw a box around the entire image), and do not forget to double-click inside the green contours to select the region.

```{=html}
<!-- -->
```
-   When using interactive **tclean**, hand-edited cyclethresholds do not change back to the auto-calculated values in the GUI until two major cycles later. However, the logger contains the most accurate information about what was used, and the expected behaviour (of hand-edited cyclethresholds applying to only the current minor cycles) is seen and has been tested. Therefore, iteration control and imaging will proceed as expected. This known issue affects CASA versions 5.6 and 5.7/6.1

```{=html}
<!-- -->
```
-   In the **makemask** task, region files using the minus sign ( - ) to create cutouts are known not to work.

#### **imregrid**

-   Position-velocity (PV) images are not supported by **imregrid**, because their coordinate systems are nonstandard, lacking a direction coordinate and having a linear coordinate.

```{=html}
<!-- -->
```
-   When converting from between coordinate system that require rotation (e.g., from celestial to galactic coordinates), CASA is known to introduce deviations in position from other software packages that can be several tenths of an arcsec. This could be because the rotation of the rectangular grid in a non-cartesian coordinate system is imperfect, possibly due to internal inconsistencies in the conversion matrices. The conversion between one frame and another in general becomes less accurate as distance from the output image\'s reference pixel increases. The imregid task and Measures tool suffer from this Known Issue (see [imregrid task page](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_imregrid)).

#### **imstat**

-   The use of the *"centerbox*" parameter when specifying a region in **imstat** has a known issue that under very specific circumstances, less pixels are taken into account for the statistics than what is expected. This only occurs when all of the following are true: (1) values are specified in pixels; (2) the width of the box is an even number of pixels (e.g, 4pix, 16pix, or 100pix); and (3) the box is located away from the image center in Right Ascension (progressively more pixels are dropped when moving away from the image center, but only in RA). The issue is a combination of machine rounding errors (when the boundary of the centerbox is exactly at the center of a pixel), and the fact that centerbox has to converts pixel coordinates to sky coordinates to allow all possible combinations of regions. Note that the "*box*" parameter is not affected by this, because it can be more strict in only using flat pixel coordinates.    As a simple work-around solution, we recommend to always give the width of the centerbox in "odd" number of pixels. Please note that because centerbox places the center of a box in the middle of a pixel and CASA only includes full pixels, the width of a centerbox always has an odd number of pixels anyway. For example, centerbox=\[\[1000pix,4000pix\],\[4pix,4pix\]\] for an 8000x8000 pixel image should give npts=25, but due to the above issue will result in npts\<25. Instead, centerbox=\[\[1000pix,4000pix\],\[5pix,5pix\]\] will always give npts=25.

 

## Visualization

#### **viewer**

-   The CASA **viewer** does not yet support the entire region shapes and parameters at this stage.
-   For equatorial cubes, i.e. data cubes that include dec=0 (exact), the **viewer** only gives spectra for sources at dec \> 0. No spectra are produced for any points with dec \<0. 
-   **Viewer** may not properly open saved region files.
-   With the new *region* panel being used now, It may be advisable to rename the *\$HOME/.casa/viewer/rc* file that stores previous configurations of the **viewer**.          
-   **Viewer** - labels are not shown - this can be caused by a conflict between an installed version of *PGPLOT* and the version of *PGPLOT* that comes with the non-root version of CASA. If you do have *PGPLOT* installed in a standard location (e.g. */usr/lib*), you may try moving it aside and see if it resolves the problems. If you do encounter this problem, please report it to the CASA team.
-   Some *X11* settings can make the viewer unstable. We identified that the line                *Load \"glx\"*                in */etc/X11/xorg.conf*    is such a setting. If you don\'t need this line for aother applications, it would be better to have it removed.
-   The viewer can only load MeasurementSets (MS) for which all spectral windows have the same channel width. If this is not the case, an *ArrayColumn* error will appear. To get around this, use *SPLIT*`` to place the spectral windows of interest in a separate MS, or try the *table browser* tool.
-   When exiting CASA after using the viewer, a message similar to the following may appear: *proc vtool_1EziEss1P2tH0PxJbGHzzQ is being killed*. This is a cosmetic issue and can be ignored.
-   For some OSs and window managers, parts of the display may be eclipsing interactive elements. We recommend to change the window manager styles for these cases. 
-   When multiple animators are open, it can happen that it is not possible to make them active, when the \'Images\' animator is inactive. Active the \'Images\' animator first to enable the other animators. 
-   MeasurementSet with sizes of tens of Gb may not visualize the full data set properly on all machines, which can give the appearance that part of the data is flagged.
-   The line tool in the MAC viewer plots unreadable hex numbers. 

#### **plotms **

-   In RedHat 7 we found that in some circumstances the vertical tab of the viewer appears on the right hand side instead of the left hand side. This eclipses the scrollbar and makes it difficult to use. To fix, add the following to the top of \~/.config/Trolltech.conf

```
[Qt]

style=GTK+
```

-    When plotting pointing axes in **plotms** on RHEL6, the tick-values of minutes and seconds on the axes are not multiples of 5

```{=html}
<!-- -->
```
-   For concatenated data sets, **plotms** can create an output error if certain data columns were present in some of the concat input MSs, but missing in others (making concat inset zero values). A practical workaround is to either handle the MSs separately, or delete those columns using the tb.removecols tool (but in case of the latter one has to take care that the columns are not crucial).

 

## Analysis

#### **uvmodelfit**

-   When running **uvmodelfit**, the output componentlist does not contain the uncertainty in flux that the task calculates (and displays at the end of the fitting process).

##  Simulation

#### **simobserve** / **simanalyze**

-   CASA simulations do not yet fully support all spectral types of components (i.e., ability to include spectral lines or spectral indices)
-   When cleaning with a simulated MS, it should be considered best practice to declare the *phasecenter* parameter using the \'J2000 xx:xx:xx.xxx +xxx.xx.xx.xxx\' notation to account for possible rounding errors that can create an offset in the image.
-   corruption of simulated MS by an atmospheric phase screen is only available from the toolkit. **simobserve** and **sm**: Under some circumstances, running **sm.setnoise** and **sm.corrupt**, or **simobserve** with thermal noise, twice using the same project name, the noise can be applied a second time, doubling the noise level. Be sure to use different project names for creating different simulations with noise. See [casaguides.nrao.edu](https://casaguides.nrao.edu/index.php/Main_Page) for the latest simulation information

 

## Single Dish

#### **general**

-   Difficulty in allocating memory to import/processing of Band 9 (fast-mapped, double-circle) data. Use high-performance machines as workaround.
-   Please avoid using spectral window and channel selection by frequency range. It may occasionally fail. So far, this has only been reported on Mac OS but it may happen on Linux, too.

#### **sdimaging**

-   **sdimaging** task may fail when more than several MSes are chosen as inputs (infiles) to create single output image. It is because the file descriptor opened by the task exceeds the limit defined by OSes. You can relax the limit of the number of open file descriptors by the command, e.g., *ulimit -n 4096* . Note the typical number of file descriptors opened by the task is 35/MS.       

#### **plotprofilemap** {#plotprofilemap .p1}

-   The task intermittently seg faults on Mac OS.

#### **The following issues in the previous releases are fixed**

-   The **sdbaseline** task fails with *blmode = \'apply\'* and selected data contains SPWs with different number of channels.
-   Spectra with only one polarization cannot be calibrated in **sdcal** and **sdgaincal**.
-   The **importnro** task fails when data contains a disabled array.

 

