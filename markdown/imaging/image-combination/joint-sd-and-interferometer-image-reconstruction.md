

# Joint Single Dish and Interferometer Image Reconstruction 

This is a description of the joint single dish and interferometer image reconstruction algorithm within CASA 5.7/6.1.

### Joint reconstruction of wideband single dish and interferometer data in CASA is [experimental](https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/tasks-and-tools). Please use at own discretion.

The scope of parameters that has been tested for CASA 5.7/6.1 can be found below.

 

## Overview

The SDINT imaging algorithm allows joint reconstruction of wideband single dish and interferometer data. This algorithm is available in the task [**sdintimaging**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging) and described in [Rau, Naik & Braun (2019)](https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta).

 

### Algorithm {#algorithm style="margin-bottom: 0in; line-height: 100%;"}

 

Interferometer data are gridded into an image cube (and corresponding PSF). The single dish image and PSF cubes are combined with the interferometer cubes in a feathering step. The joint image and PSF cubes then form inputs to any deconvolution algorithm (in either *cube* or *mfs/mtmfs* modes). Model images from the deconvolution algorithm are translated back to model image cubes prior to subtraction from both the single dish image cube as well as the interferometer data to form a new pair of residual image cubes to be feathered in the next iteration. In the case of mosaic imaging, primary beam corrections are performed per channel of the image cube, followed by a multiplication by a common primary beam, prior to deconvolution. Therefore, for mosaic imaging, this task always implements *conjbeams=True* and *normtype='flatnoise'*.

 

 

![66b05f9d215777360fc1b1ce0147ce542eeb93b5](media/66b05f9d215777360fc1b1ce0147ce542eeb93b5.png)

 

 

 

The input single dish data are the single dish image and psf cubes. The input interferometer data is a MeasurementSet. In addition to imaging and deconvolution parameters from interferometric imaging (task **tclean**), there are controls for a feathering step to combine interferometer and single dish cubes within the imaging iterations. Note that the above diagram shows only the \'mtmfs\' variant. Cube deconvolution proceeds directly with the cubes in the green box above, without the extra conversion back and forth to the multi-term basis. Primary beam handling is also not shown in this diagram, but full details (via pseudocode) are available in the [reference publication.](https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7)

The parameters used for controlling the joint deconvolution are described on the [**sdintimaging**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging) task pages.

 

## Task Specification : sdintimaging {#task-specification-sdintimaging style="margin-bottom: 0in; line-height: 100%;"}

 

The task [**sdintimaging**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging) contains the algorithm for joint reconstruction of wideband single dish and interferometer data. The **sdintimaging** task shares a significant number of parameters with the **tclean** task, but also contains unique parameters. A detailed overview of these parameters, and how to use them, can be found in the CASA Docs [task pages of sdintimaging](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging).

 

## Usage Modes

As seen from the diagram above and described on the [**sdintimaging**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging) task pages, there is considerable flexibility in usage modes. One can choose between interferometer-only, singledish-only and joint interferometer-singledish imaging. Outputs are restored images and associated data products (similar to task tclean).

The following usage modes will be released in the (experimental) sdintimaging task for CASA 6.1/5.7 . Modes being tested are all 12 combinations of :

-   Cube Imaging :  All 6 combinations of the following options.
    -   *specmode = \'cube\' *
    -   *deconvolver = \'multiscale\', \'hogbom\'        *
    -   *usedata = \'sdint\', \'sd\' , \'int\'   *
    -   *gridder = \'standard\', \'mosaic\'   *
    -   *parallel = False*

```{=html}
<!-- -->
```
-   Wideband Multi-Term Imaging :  All 6 combinations of the following options.    -   *specmode = \'mfs\' *
    -   *deconvolver = \'mtmfs\' * ( *nterms=1 * for a single-term MFS image, and *nterms\>1* for multi-term MFS image. Tests use *nterms=2* )
    -   *usedata = \'sdint\', \'sd\' , \'int\'*
    -   *gridder = \'standard\', \'mosaic\' *
    -   *parallel = False*

<div class="alert alert-info">
**NOTE**: When the INT and/or SD cubes have flagged (and therefore empty) channels, only those channels that have non-zero images in both the INT and SD cubes are used for the joint reconstruction.
</div>

<div class="alert alert-info">
**NOTE**: Single-plane joint imaging may be run with deconvolver=\'mtmfs\' and nterms=1.
</div>

<div class="alert alert-info">
**NOTE**: All other modes allowed by the new sdintimaging task are untested as of CASA 6.1. Tests will be added in subsequent releases. Please see the Future Work section at the bottom of this page.
</div>

 

 

## Test Results {#test-results style="margin-bottom: 0in; line-height: 100%;"}

 

The sdintimaging task was run on a pair of simulated test datasets. Both contain a flat spectrum extended emission feature plus three point sources, two of which have spectral index=-1.0 and one which is flat-spectrum (rightmost point). The scale of the top half of the extended structure was chosen to lie within the central hole in the spatial-frequency plane at the middle frequency of the band so as to generate a situation where the interferometer-only imaging is difficult.

Please refer to the [publication](https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta) for a more detailed analysis of the imaging quality and comparisons of images without and with SD data. 

Images from a run on the ALMA M100 12m+7m+TP Science Verification Data suite are also shown below.

###  

### Single Pointing Simulation :

Wideband Multi-Term Imaging ( deconvolver=\'mtmfs\', specmode=\'mfs\' )

<table style="height: 576px;" width="665"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td>SD + INT<br />
<p> A joint reconstruction accurately reconstructs both intensity and spectral index for the extended emission as well as the compact sources.</p></td><td><p><img src="markdown/_media/15c3a0c5553e9880865432e38820c5f165a3aa9d.png" title="fig.try_standard_mfs_mtmfs_sdint.png" class="image-inline" width="416" height="160" /></p></td></tr><tr class="even"><td><p>INT-only</p><p>The intensity has negative bowls and the spectral index is overly steep, especially for the top half of the extended component.</p></td><td><p><img src="markdown/_media/ecab604d0c63ea17708915f25dc865d123f4fb86.png" title="fig.try_standard_mfs_mtmfs_int.png" class="image-inline" width="417" height="160" /></p></td></tr><tr class="odd"><td><p>SD-only</p><p>The spectral index of the extended emission is accurate (at 0.0) and the point sources are barely visible at this SD angular resolution.</p></td><td><p><img src="markdown/_media/2ad31ce78fc986e25620147d69ab1ae858cc33ec.png" title="fig.try_standard_mfs_mtmfs_sd.png" class="image-inline" width="414" height="159" /></p></td></tr></tbody></table>

 

Cube Imaging ( deconvolver=\'multiscale\', specmode=\'cube\' )

<table style="height: 754px;" width="728"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td>SD + INT<br />
<p> A joint reconstruction has lower artifacts and more accurate intensities in all three channels, compared to the int-only reconstructions below</p></td><td><p><img src="markdown/_media/93fb162b2d84a30a1ee671e0176c6eecedb042ee.png" title="fig.try_standard_cube_multiscale_sdint.png" class="image-inline" width="614" height="236" /></p></td></tr><tr class="even"><td><p>INT-only</p><p>The intensity has negative bowls in the lower frequency channels and the extended emission is largely absent at the higher frequencies.</p></td><td><p><img src="markdown/_media/4052cd1ba39e9e48fe52f0aacafaa91fa7c140d3.png" title="fig.try_standard_cube_multiscale_int.png" class="image-inline" width="596" height="229" /></p></td></tr><tr class="odd"><td><p>SD-only</p><p>A demonstration of single-dish cube imaging with deconvolution of the SD-PSF.</p><p>In this example, iterations have not been run until full convergence, which is why the sources still contain signatures of the PSF.</p></td><td><p><img src="markdown/_media/bba19f9a48a3c11588d60f71085d9880004ff3cf.png" title="fig.try_standard_cube_multiscale_sd.png" class="image-inline" width="591" height="227" /></p></td></tr></tbody></table>

 

 

### Mosaic Simulation {#mosaic-simulation style="margin-bottom: 0in; line-height: 100%;"}

 

An observation of the same sky brightness was simulated with 25 pointings.

 

Wideband Multi-Term Mosaic Imaging ( deconvolver=\'mtmfs\', specmode=\'mfs\' , gridder=\'mosaic\' )

<table style="height: 437px;" width="704"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td>SD + INT<br />
<p> A joint reconstruction accurately reconstructs both intensity and spectral index for the extended emission as well as the compact sources.</p><p>This is a demonstration of joint mosaicing along with wideband single-dish and interferometer combination.</p></td><td><p><img src="markdown/_media/21c249a45ca04b60e8285d94b8d4f0d161aebeb6.png" title="fig.try_mosaic_mfs_mtmfs_sdint.png" class="image-inline" width="518" height="199" /></p></td></tr><tr class="even"><td><p>INT-only</p><p>The intensity has negative bowls and the spectral index is strongly inaccurate.   Note that the errors are slightly less than the situation with the single-pointing example (where there was only one pointing's worth of uv-coverage).</p></td><td><p><img src="markdown/_media/3b1edcbf6554f3fb8842b49238e910caba4d9d87.png" title="fig.try_mosaic_mfs_mtmfs_int.png" class="image-inline" width="518" height="199" /></p></td></tr></tbody></table>

 

Cube Mosaic Imaging ( *deconvolver=\'multiscale\', specmode=\'cube\' , gridder=\'mosaic\'* )

<table style="height: 489px;" width="780"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td>SD + INT<br />
<p> A joint reconstruction produces better per-channel reconstructions compared to the INT-only situation shown below.</p><p>This is a demonstration of cube mosaic imaging along with SD+INT joint reconstruction.</p></td><td><p><img src="markdown/_media/43924cabac57bbd4b9c4e6c40686c4bc43ce8306.png" title="fig.try_mosaic_cube_multiscale_sdint.png" class="image-inline" width="631" height="242" /></p></td></tr><tr class="even"><td><p>INT-only</p><p>Cube mosaic imaging with only interferometer data. This clearly shows negative bowls and artifacts arising from the missing flux.</p></td><td><p><img src="markdown/_media/3f9258cd3d4661d3447a9e7b39a96cf8fc62a2c5.png" title="fig.try_mosaic_cube_multiscale_int.png" class="image-inline" width="640" height="246" /></p></td></tr></tbody></table>

 

 

### Other Tests :  ALMA M100  Spectral Cube Imaging : 12m + 7m + TP {#other-tests-alma-m100-spectral-cube-imaging-12m-7m-tp style="margin-bottom: 0in; line-height: 100%;"}

 

The sdintimaging task was run on the [ALMA M100 Science Verification Datasets](https://almascience.nrao.edu/alma-data/science-verification).

\(1\) The single dish (TP) cube was pre-processed by adding per-plane restoringbeam information.[]

\(2\) Cube specification parameters were obtained from the SD Image as follows

> from sdint_helper import \*> sdintlib = SDINT_helper()> sdintlib.setup_cube_params(sdcube=\'M100_TmP\')

> Output : Shape of SD cube : \90 90  1 70\]> [Coordinate ordering : \[\'Direction\', \'Direction\', \'Stokes\', \'Spectral\'\]> nchan = 70> start = 114732899312.0Hz> width = -1922516.74324Hz> Found 70 per-plane restoring beams\#> > (For specmode=\'mfs\' in sdintimaging, please remember to set \'reffreq\' to a value within the freq range of the cube.)> > Returned Dict : {\'nchan\': 70, \'start\': \'114732899312.0Hz\', \'width\': \'-1922516.74324Hz\'}

 

\(3\) Task sdintimaging was run with automatic SD-PSF generation, n-sigma stopping thresholds, a pb-based mask at the 0.3 gain level, and no other deconvolution masks (interactive=False).

> sdintimaging(usedata=\"sdint\", sdimage=\"../M100_TP\", sdpsf=\"\",sdgain=3.0, dishdia=12.0, vis=\"../M100_12m_7m\", imagename=\"try_sdint_niter5k\", imsize=1000, cell=\"0.5arcsec\", phasecenter=\"J2000 12h22m54.936s +15d48m51.848s\", stokes=\"I\", specmode=\"cube\", reffreq=\"\", nchan=70, start=\"114732899312.0Hz\", width=\"-1922516.74324Hz\", outframe=\"LSRK\", veltype=\"radio\", restfreq=\"115.271201800GHz\", interpolation=\"linear\", chanchunks=1, perchanweightdensity=True, gridder=\"mosaic\", mosweight=True, pblimit=0.2, deconvolver=\"multiscale\", scales=\[0, 5, 10, 15, 20\], smallscalebias=0.0, pbcor=False, weighting=\"briggs\", robust=0.5, niter=5000, gain=0.1, threshold=0.0, nsigma=3.0, interactive=False, usemask=\"user\", mask=\"\", pbmask=0.3)

 

**Results from two channels are show below. **

LEFT : INT only (12m+7m)    and  RIGHT : SD+INT (12m + 7m + TP)

 

Channel 23

![18445a5ddbc066530938f1b8712e3a68bf9b8e3a](media/18445a5ddbc066530938f1b8712e3a68bf9b8e3a.png)

Channel 43

 

![f7c37345f62846af242938430ef9287b6b466fd4](media/f7c37345f62846af242938430ef9287b6b466fd4.png)

 

Moment 0 Maps :   LEFT :  INT only.        MIDDLE :   SD + INT with sdgain=1.0          RIGHT : SD + INT with sdgain=3.0

 

![d38c8835a149a2f61fcbeb77ee3d4f3eb04d6962](media/d38c8835a149a2f61fcbeb77ee3d4f3eb04d6962.png)

 

Moment 1 Maps :   LEFT :  INT only.        MIDDLE :   SD + INT with sdgain=1.0          RIGHT : SD + INT with sdgain=3.0

![24348b162f7e4fc3ab4b71d12f80f15f361954c6](media/24348b162f7e4fc3ab4b71d12f80f15f361954c6.png)

 

A comparison (shown for one channel) with and without masking is shown below.

![6e766bca3645b467ecae383e948f7e688aeee11d](media/6e766bca3645b467ecae383e948f7e688aeee11d.png)

 

Notes : 

-   In the reconstructed cubes, negative bowls have clearly been eliminated by using sdintimaging to combine interferometry + SD data.  Residual images are close to noise-like too (not pictured above) suggesting a well-constrained and steadily converging imaging run.  

```{=html}
<!-- -->
```
-   The source structure is visibly different from the INT-only case, with high and low resolution structure appearing more well defined.  However, the *high-resolution* peak flux in the SDINT image cube is almost a factor of 3 lower than the INT-only. While this may simply be because of deconvolution uncertainty in the ill-constrained INT-only reconstruction, it requires more investigation to evaluate absolute flux correctness.  For example, it will be useful to evaluate if the INT-only reconstructed flux changes significantly with careful hand-masking.
    -   Compare with a Feathered image : http://www.astroexplorer.org/details/apjaa60c2f1   : The reconstructed structure is consistent.

```{=html}
<!-- -->
```
-   The middle and right panels compare reconstructions with different values of sdgain (1.0 and 3.0).   The sdgain=3.0 run has a noticeable emphasis on the SD flux in the reconstructed moment maps, while the high resolution structures have the same are the same between sdgain=1 and 3.  This is consistent with expectations from the algorithm, but requires further investigation to evaluate robustness in general.

```{=html}
<!-- -->
```
-   Except for the last panel, no deconvolution masks were used (apart from a *pbmask* at the 0.3 gain level). The deconvolution quality even without masking is consistent with the expectation that when supplied with better data constraints in a joint reconstruction, the native algorithms are capable of converging on their own. In this example (same *niter* and *sdgain*), iterative cleaning with interactive and auto-masks (based mostly on interferometric peaks in the images) resulted in more artifacts compared to a run that allowed multi-scale clean to proceed on its own.

```{=html}
<!-- -->
```
-   The results using sdintimaging on these ALMA data can be compared with performance results when [using feather](https://casaguides.nrao.edu/index.php?title=M100_Band3_Combine_5.4), and when [using tp2vis](https://science.nrao.edu/facilities/alma/alma-develop-old-022217/tp2vis_final_report.pdf) (ALMA study by J. Koda and P. Teuben).

 

 

 

The following is a list of use cases that have simulation-based functional verification tests within CASA.

<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><tbody><tr class="odd"><td>1</td><td>Wideband mulit-term  imaging (SD+Int)</td><td><p>Wideband data single field imaging by joint-reconstruction from single dish and interferometric data to obtain the high resolution of the interferometer while account for the zero spacing information. Use multi-term multi-frequency synthesis (MTMFS) algorithm to properly account for spectral information of the source.</p></td></tr><tr class="even"><td>2</td><td>Wideband multi-term imaging: Int only</td><td>The same as #1 except for using interferometric data only, which is useful to make a comparison with #1 (i.e. effect of missing flux). This is equivalent to running 'mtmfs' with specmode='mfs' and gridder='standard' in tclean</td></tr><tr class="odd"><td>3</td><td>Wideband multi-term imaging: SD only</td><td>The same as #1 expect for using single dish data only which is useful to make a comparison with #1 (i.e. to see how much high resolution information is missing).  Also, sometimes, the SD PSF has significant sidelobes (Airy disk) and even single dish images can benefit from deconvolution. This is a use case where wideband multi-term imaging is applied to SD data alone to make images at the highest possible resolution as well as to derive spectral index information.  </td></tr><tr class="even"><td>4</td><td>Single field cube  imaging: SD+Int</td><td><p>Spectral cube single field imaging by joint reconstruction of single dish and interferometric data to obtain single field spectral cube image.</p><p>Use multi-scale clean for deconvolution</p></td></tr><tr class="odd"><td>5</td><td>Single field cube imaging: Int only</td><td>The same as #4 except for using the interferometric data only, which is  useful to make a comparison with #4 (i.e. effect of missing flux). This is equivalent to running 'multiscale' with specmode='cube' and gridder='standard' in tclean.</td></tr><tr class="even"><td>6</td><td>Single field cube imaging: SD only</td><td><p>The same as #4 except for using the single dish data only, which is useful to make a comparison with #4</p><p>(i.e. to see how much high resolution information is missing)</p><p>Also, it addresses the use case where SD PSF sidelobes are significant and where the SD images could benefit from multiscale (or point source) deconvolution per channel.</p></td></tr><tr class="odd"><td>7</td><td><span title="">Wideband multi-term mosaic Imaging: SD+Int<br />
</span></td><td><p>Wideband data mosaic imaging by joint-reconstruction from single dish and interferometric data to obtain the high resolution of the interferometer while account for the zero spacing information.</p>Use multi-term multi-frequency synthesis (MTMFS) algorithm to properly account for spectral information of the source. Implement the concept of conjbeams (i.e. frequency dependent primary beam correction) for wideband mosaicing.</td></tr><tr class="even"><td>8</td><td><span title="">Wideband multi-term mosaic imaging: Int only<br />
</span></td><td>The same as #7 except for using interferometric data only, which is useful to make a comparison with #7 (i.e. effect of missing flux). Also, this is an alternate implementation of the concept of conjbeams ( frequency dependent primary beam correction) available via tclean, and which is likely to be more robust to uv-coverage variations  (and sumwt) across frequency. </td></tr><tr class="odd"><td>9</td><td>Wideband multi-term mosaic imaging: SD only</td><td>The same as #7 expect for using single dish data only which is useful to make a comparison with #7 (i.e. to see how much high resolution information is missing).  This is the same situation as (3) , but made on an image coordinate system that matches an interferometer mosaic mtmfs image.</td></tr><tr class="even"><td>10</td><td>Cube mosaic imaging: SD+Int</td><td><p>Spectral cube mosaic imaging by joint reconstruction of single dish and interferometric data.</p>Use multi-scale clean for deconvolution. </td></tr><tr class="odd"><td>11</td><td>Cube mosaic imaging: Int only</td><td>The same as #10 except for using the intererometric data only, which is useful to make a comparison with #10 (i.e. effect of missing flux).  This is the same use case as gridder='mosaic' and deconvolver='multiscale' in tclean for specmode='cube'.</td></tr><tr class="even"><td><p>12</p></td><td>Cube mosaic imaging: SD only</td><td><p>The same as #10 except for using the single dish data only, which is useful to make a comparison with #10 (i.e. to see how much high resolution information is missing).  This is the same situation as (6), but made on an image coordinate system that matches an interferometer mosaic cube image.</p></td></tr><tr class="odd"><td><p>13</p></td><td>Wideband MTMFS SD+INT with channel 2 flagged in INT</td><td><p>The same as #1, but with partially flagged data in the cubes. This is a practical reality with real data where the INT and SD data are likely to have gaps in the data due to radio frequency interferenece or other weight variations. </p></td></tr><tr class="even"><td> 14</td><td>Cube SD+INT with channel 2 flagged</td><td><p>The same as #4, but with partially flagged data in the cubes. This is a practical reality with real data where the INT and SD data are likely to have gaps in the data due to radio frequency interferenece or other weight variations.  </p></td></tr><tr class="odd"><td>15</td><td>Wideband MTMFS SD+INT with sdpsf=""</td><td><p>The same as #1, but with an unspecified sdpsf. This triggers the auto-calculation of the SD PSF cube using restoring beam information from the regridded input sdimage.</p></td></tr></tbody></table>

##   {#section-1 style="margin-bottom: 0in; line-height: 100%;"}

## Future work {#future-work style="margin-bottom: 0in; line-height: 100%;"}

 

For future work and a summary of the Code Design, please see the \"Developer\"](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging/developer) tab of the[ [**sdintimaging**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging) task. 

  

## References

 Urvashi Rau, Nikhil Naik, and Timothy Braun 2019 [AJ 158, 1](https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta).^^

https://github.com/urvashirau/WidebandSDINT

