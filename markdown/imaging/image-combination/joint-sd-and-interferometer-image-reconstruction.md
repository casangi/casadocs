

# Joint Single Dish and Interferometer Image Reconstruction 

This is a description of the joint single dish and interferometer image reconstruction algorithm within CASA 5.7/6.1.

### Joint reconstruction of wideband single dish and interferometer data in CASA is [[experimental](https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/tasks-and-tools). Please use at own discretion.]

 

 

 

[The input single dish data are the single dish image and psf cubes. The input interferometer data is a MeasurementSet. In addition to imaging and deconvolution parameters from interferometric imaging (task **tclean**), there are controls for a feathering step to combine interferometer and single dish cubes within the imaging iterations. Note that the above diagram shows only the \'mtmfs\' variant. Cube deconvolution proceeds directly with the cubes in the green box above, without the extra conversion back and forth to the multi-term basis. Primary beam handling is also not shown in this diagram, but full details (via pseudocode) are available in the [reference publication.](https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7)]{

[The parameters used for controlling the joint deconvolution are described on the [**sdintimaging**](https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging) task pages.]{

 

## Task Specification : sdintimaging 
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
**NOTE**: Single-plane joint imaging may be run with deconvolver='mtmfs' and nterms=1.
</div>

<div class="alert alert-info">
**NOTE**: All other modes allowed by the new sdintimaging task are untested as of CASA 6.1. Tests will be added in subsequent releases. Please see the Future Work section at the bottom of this page.
</div>

 

 

## Test Results 

 

\(3\) Task sdintimaging was run with automatic SD-PSF generation, n-sigma stopping thresholds, a pb-based mask at the 0.3 gain level, and no other deconvolution masks (interactive=False).

> sdintimaging(usedata=\"sdint\", sdimage=\"../M100_TP\", sdpsf=\"\",sdgain=3.0, dishdia=12.0, vis=\"../M100_12m_7m\", imagename=\"try_sdint_niter5k\", imsize=1000, cell=\"0.5arcsec\", phasecenter=\"J2000 12h22m54.936s +15d48m51.848s\", stokes=\"I\", specmode=\"cube\", reffreq=\"\", nchan=70, start=\"114732899312.0Hz\", width=\"-1922516.74324Hz\", outframe=\"LSRK\", veltype=\"radio\", restfreq=\"115.271201800GHz\", interpolation=\"linear\", chanchunks=1, perchanweightdensity=True, gridder=\"mosaic\", mosweight=True, pblimit=0.2, deconvolver=\"multiscale\", scales=\[0, 5, 10, 15, 20\], smallscalebias=0.0, pbcor=False, weighting=\"briggs\", robust=0.5, niter=5000, gain=0.1, threshold=0.0, nsigma=3.0, interactive=False, usemask=\"user\", mask=\"\", pbmask=0.3)

 

**Results from two channels are show below. **

LEFT : INT only (12m+7m)    and  RIGHT : SD+INT (12m + 7m + TP)

 

Channel 23

![18445a5ddbc066530938f1b8712e3a68bf9b8e3a](media/18445a5ddbc066530938f1b8712e3a68bf9b8e3a.png){.image-inline width="435" height="253"}

Channel 43

 

![f7c37345f62846af242938430ef9287b6b466fd4](media/f7c37345f62846af242938430ef9287b6b466fd4.png){.image-inline width="428" height="249"}

 

Moment 0 Maps :   LEFT :  INT only.        MIDDLE :   SD + INT with sdgain=1.0          RIGHT : SD + INT with sdgain=3.0

 

![d38c8835a149a2f61fcbeb77ee3d4f3eb04d6962](media/d38c8835a149a2f61fcbeb77ee3d4f3eb04d6962.png){.image-inline}

 

Moment 1 Maps :   LEFT :  INT only.        MIDDLE :   SD + INT with sdgain=1.0          RIGHT : SD + INT with sdgain=3.0

![24348b162f7e4fc3ab4b71d12f80f15f361954c6](media/24348b162f7e4fc3ab4b71d12f80f15f361954c6.png){.image-inline}

 

A comparison (shown for one channel) with and without masking is shown below.

![6e766bca3645b467ecae383e948f7e688aeee11d](media/6e766bca3645b467ecae383e948f7e688aeee11d.png){.image-inline}

 

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

<table><colgroup><col 

## Future work ]{authors=""}

https://github.com/urvashirau/WidebandSDINT

