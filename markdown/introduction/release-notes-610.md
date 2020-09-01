

# Release Notes CASA 5.7 / 6.1 

Summary of new features in this release of CASA

This is the documentation for CASA 5.7/6.1. Changes compared to the CASA 5.6/6.0 release are listed below.

 

### Highlights (details below)

-   A new task **sdintimaging** is available for jont deconvolution of Single Dish and Interfermeter data.
-   A new task **sdtimeaverage** is available for averaging single-dish spectral data over specified time.    
-   A new single-dish spectral imaging mode, *\'cubesource\'*, is available in the task **tsdimaging**. 
-   A new parameter *corrdepflags* has been added to the **gaincal**, **bandpass**, and **fringefit** tasks to permit more control of flagging subsets of correlations.    
-   The **fringefit** task now includes support for dispersive delays.
-   The CASA simulator now uses **tclean** instead of clean.
-   The ability to correct for heterogeneous antenna pointing offsets stored in the POINTING sub-table of the MS has been added to **tclean** (*gridder=\'awproject\'*).    
-   **statwt** now includes weighting each visibility by its exposure time, and also improved in the way the *timebin* parameter is interpreted when its value is an integer.
-   the **imsmooth** task has been made consistency with the rest of CASA in terms of masking
-   **simobserve** now reads and populates antenna names rather than assigning numbers, which makes comparing simulated and real data easier. 
-   The *fldmap* parameter within the cal library will now support multiple fields
-   [CARTA](https://casa.nrao.edu/casadocs-devel/stable/imaging/carta) v.1.3 with limited features is now available for users who wish to visualize their data outside the CASA Viewer.
-   VLA P-band models have been made available in CASA for several standard calibrators.
-   Ephemeris tables for Solar System objects have been extended in time
-   An *\"execfile\"* python shortcut has been added to the (Python 3 based) CASA 6 environment for backwards compatibility with ALMA scriptForPI.py restore scripts.
-   For continuum imaging (*specmode=\'mfs'*), the \<imagename\>.workdirectory, where all temporary images produced by the parallel runs were placed, has been removed.
-   A large number of bugs have been fixed

 

### Full Release Notes

#### Data Import/Export

-   In **importasdm**, the *\'remove_ref_undef\'* parameter has been removed. This parameter was added after CASA 4.3 so that MeasurementSets created by importasdm after CASA 4.3 could be made compatible with CASA 4.3 (and older versions of CASA). This was intended to be used for a limited time to allow for backwards compatibility of MeasurementSets with version of CASA older than CASA 4.3. That temporary parameter has now been removed. 
-   The SUB_TYPE column in the PROCESSOR table of a MeasurementSet is now filled by **importasdm** using the correlatorName appropriate for that PROCESSOR as found in the ASDM CorrelatorMode table when that PROCESSOR is a correlator. If the processor is not a correlator, or an appropriate row cannot be found in the CorrelatorMode table, the processorSubType is used to fill the SUB_TYPE column (SUB_TYPE is unchanged for non-correlator processors).

#### MS Viewing, Editing, Manipulation

-   N/A    

#### Calibration

-   The statwt application, which consists of both the task **statwt** and tool method **ms.statwt()**, has undergone substantial changes. The algorithm used to compute weights now includes weighting each visibility by its exposure time. There are also significant changes to how the application interprets the *timebin* parameter if it is an integer. For details, please see the complete [statwt documentation](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_statwt)
-   A new parameter *corrdepflags* has been added to the *gaincal, bandpass*, and *fringefit* tasks to permit control of behavior when a subset of correlations is flagged. Previously (and now only by the default: *corrdepflags=False*), such data was ignored, as if all correlations were flagged. Now, if *corrdepflags=True*, solutions will be obtained for the unflagged polarization in such cases. This enables recovery of data for antennas which may have only one available polarization (common in VLBI). 
-   VLA P-band models for the frequency range between 230 - 470 MHz have been made available in CASA for several standard calibrators, following Perley & Butler (2017). These models can be used in the setjy task.    
-   The *fldmap* parameter within the cal library will now support multiple fields specified as a selection string, much as the *gainfield* works in the conventional calibration apply parameters (previously, only selection of a single field was supported).
-   The runtime of **flagdata** is approximately [24-34% shorter than in earlier CASA versions, because the summary mode has been optimized.]    

#### Imaging

-   A new task [**sdintimaging**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging) for the [joint reconstruction of single dish and interferometer data](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction) is being released in CASA 6.1/5.7. The sdintimaging task implements the algorithm published in [Rau et al, 2019](https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7 "Follow link"){.external-link}. It is being released as \'experimental\' and is currently intended for the exploration of the algorithm\'s capabilities and to gather feedback for the further refinement of the interface. It supports joint deconvolution for spectral cube as well as multi-term wideband imaging, operates on single pointings as well as joint mosaics, includes corrections for frequency dependent primary beams, and optionally allows the deconvolution of only SD images in both cube and mtmfs modes. Documentation about the algorithm, usage modes that have been verified and validated prior to release, and some example images, can be found [here](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction) and in the [sdintimaging task pages](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging).    
-   The new CARTA (*Cube Analysis and Rendering Tool for Astronomy*) visualization software version 1.3 is now available for general users who wish to try visualizing image products outside the CASA Viewer. CARTA is a new image visualization and analysis tool designed for ALMA, VLA, and SKA pathfinders, developed by ASIAA, IDIA, NRAO and Univ. Alberta. CARTA is eventually expected to replace the CASA Viewer, but the current version 1.3 offers only limited functionality and does not include all the features that the Viewer has. Nevertheless, CARTA v.1.3 may be the preferred tool for users who are worried about proper display of header information or overall performance of the CASA Viewer, or who wish to try remote display options, Stokes wedges, custimized layouts, or visualizing HDF5 image formats with CARTA.     
-   The ability to correct for heterogeneous antenna pointing offsets has been added to **tclean** (*gridder=\'awproject\'*) and augments the existing ability to apply time-dependent pointing corrections. With a choice of *usepointing=True*, pointing corrections are applied via vectors that are fetched from the POINTING sub-table in the MS. A new parameter, *pointingoffsetsigdev*, is used to define bins for grouping antennas and deciding the degree of time variability to consider when computing the phase gradients (for *usepointing=True*). Demonstrations of this feature on simulated as well as VLASS data are documented in our [VLASS Pointing Correction Report](https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-knowledgebase/wideband-mosaic-imaging-and-pointing-corrections-for-the-vla-sky-survey). CASA acknowledges the ARDG\'s role in providing the C++ implementation as an addition to the existing AWProject gridder.
-   The convolution function used by the *wproject* gridder in **tclean** has been adjusted to ensure that it is calculated on a grid which size is a composite number. Dramatic slowdowns incurred by setting specific imsize settings (leading to grids of prime numbers) are now avoided.
-   For *deconvolver='MTMFS'*, the runtime of the minor cycle has been improved, particularly for large *imsize*, *niter*, and number of scales for multi-scale deconvolution.
-   For continuum imaging with *specmode=\'mfs\'*, the creation of a directory called \<imagename\>.workdirectory, where all temporary images produced by the parallel runs were placed, has been removed. Only the final gathered/concatenated continuum images now appear in the main directory.

#### Analysis

-   **visstat** now handles more gracefully commands where all data are flagged within one of the groups (sub-selections) across the reporting axes.
-   A change in the **imsmooth** task has been made for better consistency with the rest of CASA, such that combining an existing pixel mask with an OTF mask results in an output mask that is only *True* for pixels where both input masks are True. A practical application of this change is an apparent \"bug fix\" for the **immoments** task when used on cubes with per plane beams; before the fix, it was possible for emission outside of the input mask to end up in the output moment maps.

#### Single Dish

-   Averaging SD spectral data over specified time is now available with the new **sdtimeaverage** task. Dedicated tasks for the baseline-subtraction and pol-averaging are already supported. This sdtimeaverage task is a further dedicated time-averaging task for more convenience.
-   A new spectral imaging mode, *\'cubesource\'*, is available in the task **tsdimaging**. The *\'cubesource\'* mode is effective only for moving sources and tracks frequency shift during the observation. With *\'cubesource\'* mode, frequency reference frame of the output image will be REST.
-   In **tsdimaging**, generation of psf image is disabled until correct implementation for single dish psf image is implemented. This is because the psf image currently generated by tsdimaging is useless in terms of single dish data reduction. This makes performance of tsdimaging faster than previous CASA 5 versions. Having said that, tsdimaging is still slower than sdimaging so that it might be better to use **sdimaging** for *non-ephemeris i*maging if performance matters.

#### VLBI

-   The **fringefit** task now includes support for dispersive delays (inversely proportional to the square of frequency), which parameters solved for is controlled by the new *paramactive* keyword. The *paramactive* parameter takes a Python list of Boolean arguments for the delay, rate, and dispersive components. The default settings preserve the previous behavior of the task, which is also expected to be the most common future use case.

#### Simulations

-   **simobserve** now reads and populates antenna names rather than assigning numbers, which makes it easier to compare plots of simulated data with those of real data. The population of antennas names is based on the fifth column of antenna configuration files passed via the *antennalist* parameter. Partial line comments in the header and body of such files are now also supported via the octothorpe (\#) character.

#### Other

-   The task **accum** will be deprecated in the next CASA release, version 5.8/6.2.
-   An *\"execfile\"* python shortcut has been added to the (Python 3 based) CASA 6 environment for backwards compatibility with ALMA scriptForPI.py restore scripts. The \"execfile\" command has been tested and found to work in the same way as in (Python 2 based) CASA 5 with the exception that the treatment of global variables has changed in Python 3. For *\"execfile\"* calls within a script which itself is run via *\"execfile\"*, it is necessary to add *globals()* as the second argument to those *\"execfile\"* calls in order for the nested script to know about the global variables of the calling script. For example, within a script *\'mainscript.py\'*, calls to another script *\'myscript.py\'* should be written as follows: *execfile(\'myscript.py\', globals())*.
-   Solar System objects\' positional ephemeris tables have been extended in time (*Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Io, Europa, Ganymede, Callisto, Titan* and various asteroids). In addition, Mars and four asteroids (*Ceres, Pallas, Vesta, and Lutetia*) have explicit light curves based upon detailed thermo-physical modeling; these light curves have also been extended forward in time. The underlying brightness temperature models of these objects, and their relation to the Bulter-JPL-Horizons 2012 flux scale, have not been altered.

#### Bug-fixes 

-   For **plotms**, a large number of bugs were addressed to improve display options and functionality, and to transition the plotms task from CASA 5 to CASA 6.    
-   A bug was fixed that prevented *uvtaper* from working with Briggs style weighting (*briggs, briggsabs, uniform*) and *perchanweightdensity=True*.
-   A bug in **tclean** which incorrectly summed the imaging weights when using uniform weighting in parallel runs has been fixed.**    **
-   A bug in **tclean** has been fixed that lead to a seg fault when imaging multiple MSes with inconsistent *WEIGHT_SPECTRUM* columns (i.e., the column exists in all MSes but in some has no data).
-   A bug in **tclean** has been fixed, which triggered a sementation fault when chanchunking with *savemodel=\'virtual\'* and tclean ended with only 1 minor cycle.    
-   A bug was fixed for imaging of ephemeris objects in **tclean**, which affected targets for which the field IDs observed are not in time order. This caused a noticeable offset in direction of the source in cases when the source was fast moving.
-   Several bugs that relate to the use of serial and parallel imaging runs in **tclean** have been fixed. They include a *\'latpole\'* coordinate mismatch when attempting to use an output image from a parallel continuum run in a subsequent serial step, missing *miscinfo* image header information information in *mtmfs* parallel continuum runs, and the inability to use a *model* image from a parallel run in a subsequent serial predict-model step. 
-   A bug in **concat** and **importfitsidi** that affected polarization visibility data in concatenated MSs, such that the cross-hands may previously have been spuriously mis-ordered on some baselines in the concatenated MS, has been fixed. The bug could be triggered when the second MS (in time-order) provided to concat had a different antenna table than the first MS. For more information, please see this [CASA Knowledgebase Article](https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-knowledgebase/bug-affecting-polarization-visibility-data-in-concatenated-data). Specifically, ALMA Stokes V and VLA Stokes U, when subject to the condition above, would be affected by this bug.
-   A bug was fixed in the *spwmap* parameter, which could previously cause an exception when a spw pointed to by other spws did not point to itself. E.g., if only spw 1 has calibration available in the caltable and is to be used to calibrate spws 0,2,3, spwmap=\[1,2,1,1\] would fail (even if not selecting spw 1 for processing) since spw 1 points to spw 2 (for which there is no available calibration). Most users would not see this problem, since spws for which calibration is available will generally be calibrated by themselves. This is now fixed, and any permutation of spw specifications should work correctly in spwmap.
-   A bug has been fixed in **gencal**, specifically in the generation of the antenna position tables for VLA data (this bug did not affect ALMA data). Previously, if the highest-numbered antenna involved in a given observation required a position correction, it was not being registered correctly.*    *
-   A segfault in **imstat** when using the ( - ) operator in *region file* has been fixed.
-   A bug was fixed where in certain specific circumstances (calibration absent for antenna id=0), Single Dish calibration tables were previously not being applied.    
-   A bug in **fixvis** was fixed, whereby fixvis was misbehaving when processing Multi-MSs in parallel. Updates to **uvcontsub** and **cvel** were also made to ensure accurate internal copying of MMS directory structures.
-   A bug in **flagdata**, which led to occasional reports of progress values over 100%, has been fixed. 
-   A bug was fixed in *ImageBeamSet::setBeam()* in which, while the beam was being replaced in the \_beams Matrix object, \_maxBeam was not being recalculated. This led to a problem when, in addition, the beam that was being replaced had been the current maximum beam. 
-   In *msmd.scansforfield()*, the parameter name changed from *intent* to *field*, fixing an existing bug in the naming convention.

 

 

