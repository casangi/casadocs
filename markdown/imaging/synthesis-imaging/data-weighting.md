

# Imaging Algorithms 

Data weighting, gridding, fft and normalizations

Imaging is the process of converting a list of calibrated visiblities into a raw or \'dirty\' image. There are three stages to inteferometric image-formation: weighting, convolutional resampling, and a Fourier transform.

 

# Data Weighting

During imaging, the visibilities can be weighted in different ways to alter the instrument\'s natural response function in ways that make the image-reconstruction tractable.

Data weighting during imaging allows for the improvement of the dynamic range and the ability to adjust the synthesized beam associated with the produced image. The weight given to each visibility sample can be adjusted to fit the desired output. There are several reasons to adjust the weighting, including improving sensitivity to extended sources or accounting for noise variation between samples. The user can adjust the weighting using **clean** and changing the *weighting* parameter with six options: \'natural\', \'uniform\', \'briggs\',  \'superuniform\', \'briggsabs\', and \'radial\'. Optionally, a UV taper can be applied, and various parameters can be set to further adjust the weight calculations.

 

#### Natural weighting

*Summary:* The natural weighting scheme gives equal weight to all samples. Since usually, lower spatial frequencies are sampled more often than the higher ones, the inner uv-plane will have a significantly higher density of samples and hence signal-to-noise than the outer uv-plane. The resulting \"density-upweighting\" of the inner uv-plane will produce the largest angular resolution and can sometimes result in undesirable structure in the PSF which reduces the accuracy of the minor cycle. However, at the location of a source, this method preserves the natural point-source sensitivity of the instrument.

For *weighting=\'natural\'*, visibilities are weighted only by the data weights, which are calculated during filling and calibration and should be equal to the inverse noise variance on that visibility. Imaging weight $w_i$ of sample []{.cmmi-10x-x-109}$\dot\imath$ is given by:

$w_i = \omega_i = \frac{1}{{\sigma_i}^2}$

where the data weight $\omega_i$ is determined from $\sigma_i$, the rms noise on visibility $\dot\imath$. When data is gridded into the same uv-cell for imaging, the weights are summed, and thus a higher uv density results in higher imaging weights. No sub-parameters are linked to this mode choice. It is the default imaging weight mode, and it should produce "optimum" image with with the lowest noise (highest signal-to-noise ratio).

<div class="alert alert-info">
**NOTE**: This generally produces images with the poorest angular resolution, since the density of visibilities falls radially in the uv-plane.
</div>

####   {#section .nopar}

#### Uniform weighting {#uniform-weighting .nopar}

*Summary:* Uniform weighting gives equal weight to each measured spatial frequency irrespective of sample density. The resulting PSF has the narrowest possible main lobe (i.e. smallest possible angular resolution) and suppressed sidelobes across the entire image and is best suited for sources with high signal-to-noise ratios to minimize sidelobe contamination between sources. However, the peak sensitivity is significantly worse than optimal (typically \~20% worse for reasonably large number of antenna interferometers), since data points in densely sampled regions have been weighted down to make the weights uniform. Also, isolated measurements can get artifically high relative weights and this may introduce further artifacts into the PSF.

For *weighting=\'uniform\'*, the data weights are calculated as in \'natural\' weighting. The data is then gridded to a number of cells in the uv-plane, and after all data is gridded the uv-cells are re-weighted to have "uniform" imaging weights. This pumps up the influence on the image of data with low weights (they are multiplied up to be the same as for the highest weighted data), which sharpens resolution and reduces the sidelobe level in the field-of-view, but increases the rms image noise. No sub-parameters are linked to this mode choice.

For uniform weighting, we first grid the inverse variance $\omega_i$ for all selected data onto a grid with uv cell-size given by 2 ∕ FOV, where FOV is the specified field of view (defaults to the image field of view). This forms the gridded weights $W_k$. The weight of the $\dot\imath$-th sample is then:

$w_i = \frac{\omega_i}{W_k}$

####   {#section-1 .noindent style="text-align: left;"}

#### Briggs weighting {#briggs-weighting .noindent style="text-align: left;"}

*Summary:* Briggs or Robust weighting [\[1\]](#Bibliography) creates a PSF that smoothly varies between natural and uniform weighting based on the signal-to-noise ratio of the measurements and a tunable parameter that defines a noise threshold. High signal-to-noise samples are weighted by sample density to optimize for PSF shape, and low signal-to-noise data are naturally weighted to optimize for sensitivity.

The *weighting=\'briggs\' *mode is an implementation of the flexible weighting scheme developed by Dan Briggs in his PhD thesis, which can be viewed [here](http://www.aoc.nrao.edu/dissertations/dbriggs/).

This choice brings up the sub-parameters:

```
weighting      =   'briggs'   #   Weighting to apply to visibilities  
     robust    =        0.0   #   Briggs robustness parameter  
     npixels   =          0   #   number of pixels to determine uv-cell size 0=> field of view
```

The actual weighting scheme used is:

$w_i = \frac{\omega_i}{1 + W_k f^2}$

where

$w_i$ is the image weight for a given visibility point $i$;

$\omega_i$ is the visibility weight of baseline $i$;

$W_k = \Sigma_{cell=k}\,\omega_{k}$ is the weight density of a given cell $k$ (with $\omega_{k}$ the weight of a uv point that falls in cell $k$). When using *npixels \> 0* then $\Sigma_{\omega_{k}}$ is over all weights that fall in cells in range *k ± npixels*

$f^2 = \frac{(5 \times 10^{-\text{R}})^2}{\frac{\Sigma_k W_k^2}{\Sigma_i \omega_i}}$;

R is the robust sub-parameter.

The key parameter is the *robust sub-*parameter, which sets R in the Briggs equations. The scaling of R is such that *robust=0* gives a good trade-off between resolution and sensitivity. The robust R takes value between -2.0 (close to uniform weighting) to 2.0 (close to natural).

Superuniform weighting can be combined with Briggs weighting using the *npixels *sub-parameter. This works as in 'superuniform' weighting.

##  

#### Briggsabs weighting

*Summary:* Briggsabs is an experimental weighting scheme that is an adapted version of the Briggs weighting scheme, and is much more aggressive with respect to changes in *npixels*, the uv-cell size.

For *weighting=\'briggsabs\'*, a slightly different Briggs weighting is used, with:

$w_i = \frac{\omega_i}{W_k \text{R}^2 + 2\sigma_\text{i}^2}$

where R is the *robust* parameter and $\sigma_\text{i}$ is the *noise *parameter. In this case, R makes sense for −2.0 ≤ R ≤ 0.0 (R = 1.0 will give the same result as R = −1.0)

This choice brings up the sub-parameters:

```
weighting      = 'briggsabs'  #   Weighting to apply to visibilities  
     robust    =      0.0     #   Briggs robustness parameter  
     noise     =  '0.0Jy'     #   noise parameter for briggs weighting when rmode='abs' 
     npixels   =        0     #   number of pixels to determine uv-cell size 0=> field of view
```

 

<div class="alert alert-warning">
**WARNING:** Briggsabs weighting is experimental - use at own risk!
</div>

 

#### Superuniform weighting {#superuniform-weighting .noindent}

The *weighting=\'superuniform\' *mode is similar to the \'uniform\' weighting mode but there is now an additional *npixels *sub-parameter that specifies a change to the number of cells on a side (with respect to uniform weighting) to define a uv-plane patch for the weighting renormalization. If *npixels=0*, you get uniform weighting.

 

#### Radial weighting

The *weighting=\'radial\' *mode is a seldom-used option that increases the weight by the radius in the uv-plane, i.e.:

$w_i = \omega_i \times \sqrt{u_i^2 + v_i^2}$

Technically, this would be called an inverse uv-taper, since it depends on uv-coordinates and not on the data per-se. Its effect is to reduce the rms sidelobes for an east-west synthesis array. This option has limited utility.

 

#### Perchanweightdensity

When calculating weight density for Briggs style weighting in a cube, the *perchanweightdensity* parameter determines whether to calculate the weight density for each channel independently (the default, True) or a common weight density for all of the selected data. This parameter has no meaning for continuum (*specmode=\'mfs\'*) imaging but for cube imaging *perchanweightdensity=True* is a recommended  alternative option that provides more uniform sensitivity per channel for cubes, but with generally larger psfs than the *perchanweightdensity=False* option (which was also the behavior prior to CASA 5.5). When using *Briggs* style weight with *perchanweightdensity=True*, the imaging weight density calculations use only the weights of data that contribute specifically to that channel. On the other hand, when *perchanweightdensity=False*, the imaging weight density calculations sum all of the weights from all of the data channels selected whose (u,v) falls in a given uv cell on the weight density grid. Since the aggregated weights, in any given uv cell, will change depending on the number of channels included when imaging, the psf calculated for a given frequency channel will also necessarily change, resulting in variability in the psf for a given frequency channel when *perchanweightdensity=False*. In general, *perchanweightdensity=False* results in smaller psfs for the same value of robustness compared to *perchanweightdensity=True*, but the rms noise as a function of channel varies and increases toward the edge channels; *perchanweightdensity=True* provides more uniform sensitivity per channel for cubes. This may make it harder to find estimates of continuum when *perchanweightdensity=False*. If you intend to image a large cube in many smaller subcubes and subsequently concatenate, it is advisable to use *perchanweightdensity=True* to avoid surprisingly varying sensitivity and psfs across the concatenated cube.

<div class="alert alert-info">
**NOTE**: Setting *perchanweightdensity = True* only has effect when using *Briggs* (robust) or *uniform* weighting to make an image cube. It has no meaning for *natural* and *radial* weighting in data cubes, nor does it have any meaning for continuum (*specmode=\'mfs\'*) imaging.
</div>

####   {#section-3 .nopar}

#### Mosweight

When doing Brigg\'s style weighting (including uniform) in **tclean**, the *mosweight* subparameter of the mosaic gridder determines whether to weight each field in a mosaic independently (*mosweight = True*), or to calculate the weight density  from the average uv distribution of all the fields combined (*mosweight = False*). The underlying issue with more uniform robust weighting is how the weight density maps onto the uv-grid, which can give high weight to areas of the uv-plane that are not actually more sensitive. The setting *mosweight = True* has long been known as potentially useful in cases where a mosaic has non-uniform sensitivity, but it was found that it is also very important for more uniform values of robust Briggs weighting in the presence of relatively poor uv-coverage. For example, snap-shot ALMA mosaics with *mosweight = False* typically show an increase in noise in the corners or in the areas furthest away from the phase-center. Therefore, as of CASA 5.4, the *mosweight* sub-parameter has been added to **tclean** with default value *mosweight = True*.

<div class="alert alert-warning">
**WARNING:** the default setting of *mosweight=True* under the mosaic gridder in **tclean** has the following disadvantages: (1) it may potentially cause memory issues for large VLA mosaics; (2) the major and minor axis of the synthesized beam may be \~10% larger than with mosweight=False. Please change to *mosweight=False* to get around these issues.
</div>

####  

#### uvtaper

*Summary:* The effect of uvtaper this is that the clean beam becomes larger, and surface brightness sensitivity increases for extended emission.

uv-tapering applies a Gaussian taper on the weights of your UV data, in addition to the weighting scheme specified via the \'weighting\' parameter. It applies a multiplicative Gaussian taper to the spatial frequency grid, to weight down high spatial-frequency measurements relative to the rest. This means that higher spatial frequencies are weighted down relative to lower spatial frequencies, to suppress artifacts arising from poorely sampled regions near and beyond the maximum spatial frequency in the uv-plane. It is equivalent to smoothing the PSF obtained by other weighting schemes and can be specified either as a Gaussian in uv-space (eg. units of lambda or klambda) or as a Gaussian in the image domain (eg. angular units like arcsec). Because the natural PSF is smoothed out, this tunes the sensitivity of the instrument to scale sizes larger than the angular-resolution of the instrument by increasing the width of the main lobe. There are limits to how much uv-tapering is desirable, however, because the sensitiivty will decrease as more and more data is down-weighted.

<div class="alert alert-info">
**NOTE**: The on-sky FWHM in arcsec is roughly the *uvtaper* / 200 (klambda).
</div>

Examples: uv*taper=\[\'5klambda\'\]* circular taper FWHM=5 kilo-lambda, uv*taper=\[\'5klambda\',\'3klambda\',\'45.0deg\'\]*, *uvtaper=\[\'10arcsec\'\]* on-sky FWHM 10 arcseconds, *uvtaper=\[\'300.0\'\]* default units are lambda in aperture plane, uv*taper=\[\]*; no outer taper applied (default)

 

![6178646282cf25c3d316aa14c3d888e6608a49bd](media/6178646282cf25c3d316aa14c3d888e6608a49bd.png)

#  

# Gridding + FFT

Imaging weights and weighted visibilities are first resampled onto a regular uv-grid (convolutional resampling) using a prolate-spheroidal function as the gridding convolution function (GCF). The result is then Fourier-inverted and grid-corrected to remove the image-domain effect of the GCF. The PSF and residual image are then normalized by the sum-of-weights.

 

![29159db628f096f12291870d788317a84a86e15c](media/29159db628f096f12291870d788317a84a86e15c.png)

 

## Direction-dependent corrections

Basic gridding methods use prolate spheroidals for gridding (*gridder=\'standard\'*) along with image-domain operations to correct for direction-dependent effects. More sophiticated, and computationally-intesitve methods (*gridder=\'wproject\',\'widefield\',\'mosaic\',\'awproject\'*) apply direction-dependent, time-variable and baseline-dependent corrections during gridding in the visibility-domain, by choosing/computing the appropriate gridding convolution kernel to use along with the imaging-weights.

The figure below shows examples of kernels used for the following gridding methods: Standard, W-Projection, and A-Projection.  Combinations of wide-field corrections are done by convolving these kernels together.  For example, AW-Projection will convolve W-kernels with baseline aperture functions and possibly include a prolate spheroidal as well for its anti-aliasing properties.   Mosaicing is implemented as a phase gradient across the gridding convolution kernel calculated at the uv-cell resolution dictated by the full mosaic image size.

In tclean, *gridder=\'mosaic\'* uses Airy disk or polynomial models to construct azimuthally symmetric beams per antenna that are transformed into baseline convolution functions and used for gridding.  *gridder=\'awproject\'* uses ray-traced models of antenna aperture illumination functions to construct GCFs per baseline and time (including azimuthal asymmetry, beam squint, and rotation with time).   More details are given in the [Wide Field Imaging](https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam) page.

 

![1c48e6447847e5f2e25d16da48fb67f74b5e0a70](media/1c48e6447847e5f2e25d16da48fb67f74b5e0a70.png)

 

Computing costs during gridding scale directly with the number of pixels needed to accurately describe each convolution kernel. The standard gridding kernel (prolate spheroid) typically has 3x3 pixels. W-Projection kernels can range from 5x5 to a few hundred pixels on a side.  A-Projection kernels typically range from 8x8 to 50x50 pixels.  When effects are combined by convolving together different kernels (for example A and W Projection), the kernel sizes increase accordingly. 

Memory (and one-time computing costs) also scale with the number of distinct kernels that one must operate with. For example, a large number of different W-Projection kernels, or an array whose antenna illumination patterns are different enough between antennas that they need to be treated separately. In the case of a heterogenous array, each baseline illumination function can be different.  Additionally, if any of these aperture illumination based kernels are rotationally asymmetric, they will need to be rotated (or recomputed at different parallactic angles) as a function of time.  

 

# Normalization

After gridding and the FFT, images must be normalized (by the sum of weights, and optionally by some form of the primary beam weights) to ensure that the flux in the images represents sky-domain flux.

## Sum-Of-Weights and Weight Images

The tclean task produces a number of output images used for normalization. The primary reason these are explicit images on disk (and not just internal temporary files in memory) is that for continuum paralellization, there is the need to accumulate numerators and denominators separately before the normalization step.  For the most part, end users can safely ignore the  output .weight,  .sumwt and .gridwt images.  However, their contents are documented here.

#### .sumwt 

   A single-pixel image containing the sum-of-weights (or, the peak of the PSF). For natural weighting, this is just the sum of the data weights.  For other weighting schemes it contains the effect of the weighting algorithm. For instance, uniform weighting will typically produce a smaller sum-of-weights than natural weighting.    An approximate theoretical sensitivity can be computed as  sqrt( 1/sumwt ). A more accurate calculation requires a different calculation (LINK to some docs from GM on this).   In tclean, facetted imaging will produce one value of sumwt per facet as the normalizations are to be done separately per facet.  Also, for cube imaging, .sumwt will contain one value per image channel and it can be used to visualize the relative weights across the spectrum (and therefore expected image rms). This theoretical sensitivity information is printed to the logger after the PSF generation stage.

#### .weight 

Projection gridders such as \'mosaic\' and \'awproject\' use baseline aperture illumination functions for gridding.  The quantity in the .weight image represents the square of the PB, accumulated over baselines, time and frequency.   For mosaics, it includes a combination across pointing as well (although as can be seen from the equations in the mosaicing section, this is not accurate when weights between pointings differ considerably).

#### .gridwt 

A series of temporary images for cube imaging that are stored within the parallel .workdirectory, and which accumulate binned natural weights before the calculation of imaging weights.  This is not used for normalization anywhere after the initial image weighting stage.

 

## Normalization Steps

#### Standard Imaging

For gridders other than \'mosaic\' and \'awproject\', normalization of the image formed after gridding and the FFT is just the division by the sum of weights (read from the .sumwt image). This suffices to transform the image into units of sky brightness. This is the typical flat-noise normalization (see below).

#### Imaging with primary beams (and mosaics)

For *gridder=\'mosaic\'* and \'awproject\' that use baseline aperture illumination functions during gridding, the result is an additional instance of the PB in the images, which needs to be divided out.  Normalization involves three steps (a) division by the sum-of-weights (b) division by an average PB given by sqrt(weightimage) and (c) a scaling to move the peak of the PB = sqrt(weightimage) to 1.0.   This ensures that fluxes in the dirty image (and therefore those seen by the minor cycle) represent true sky fluxes in regions where the primary beam is at its peak value, or where the mosaic has a relatively constant flat sensitivity pattern.    The reverse operations of (b) and (c) are done before predicting a model image in the major cycle.   ( This description refers to flat-noise normalization, and corresponding changes are done for the other options ).

 

## Types of normalization

There are multiple ways of normalizing the residual image before beginning minor cycle iterations. One is to divide out the primary beam before deconvolution and another is to divide out the primary beam from the deconvolved image. Both approaches are valid, so it is important to clarify the difference between the two. A third option is included for completeness.

For all options, the \'pblimit\' parameter controls regions in the image where PB-correction is actually computed. Regions below the pblimit cannot be normalized and are set to zero. For standard imaging, this refers only to the pb-corrected output image. For *gridder=\'mosaic\'* and *\'awproject\'* it applies to the residual, restored and pb-corrected images.  A small value (e.g. *pblimit=0.01*) can be used to increase the region of the sky actually imaged. For *gridder=\'standard\'*, there is no pb-based normalization during gridding and so the value of this parameter is ignored.The sign of the pblimit parameter is used for a different purpose. If positive, it defines a T/F pixel mask that is attached to the output residual and restored images.  If negative, this T/F pixel mask is not included.  Please note that this pixel mask is different from the deconvolution mask used to control the region where CLEAN based algorithms will search for source peaks.  In order to set a deconvolution mask based on pb level, please use the \'pbmask\' parameter.Based on the above, please note that certain values of pblimit to avoid, are 1, -1, and 0. When the pblimit is set to 1 the entire image is masked as the user is specifying that no normalization or deconvolution happens if the PB gain is lower than 1, which leads to the entire image being masked. Setting the pblimit to -1 also results in no deconvolution as mentioned in the case where pblimit is 1 but there is no masking of the image. Finally a pblimit of zero is not feasible but rather a small value such as 1e-6 is used instead to make a really large wide field image.

### Flat-noise

The dirty image represents $I^{dirty} = I^{psf} \star \left( I^{PB} \cdot I^{sky} \right)$

Primary-beam correction is not done before the minor cycle deconvolution. The dirty image is the instrument\'s response to the product of the sky and the primary beam, and therefore the model image will represent the product of the sky brightness and the average primary beam. The noise in the image is related directly to the measurement noise due to the interferometer, and is the same all across the image. The minor cycle can give equal weight to all flux components that it finds. At the end of deconvolution, the primary beam must be divided out of the restored image. This form of normalization is useful when the primary beam is the dominant direction-dependent effect because the images going into the minor cycle satisfy a convolution equation. It is also more appropriate for single-pointing fields-of-view.

Imaging with the prolate spheroidal gridder will automatically give flat noise images.

### Flat-sky

The dirty image represents $I^{dirty} = \frac{1}{I^{PB}} \cdot \left[I^{psf} \star \left( I^{PB} \cdot I^{sky} \right) \right]$

Approximate Primary-beam correction is done on the dirty image, before the minor cycle iterations. The amplitude of the flux components found during deconvolution will be free of the primary beam, and will represent the true sky. However, the image going into the minor cycle will not satisfy a convolution equation and the noise in the dirty image will be higher in regions where the primary-beam gain is low. Therefore, the minor cycle needs to account for this while searching for flux components (a signal-to-noise dependent CLEAN). This form of normalization is particularly useful for mosaic imaging where the sky brightness can extend across many pointings, or if there is an uneven distribution of weights across pointings. This is because joint mosaics are usually done for sources with spatial scales larger than the field-of-view of each antenna and which are not explicitly present in the measured data. In this situation, allowing the minor cycle to use flux components that span across beams of adjacent pointings is likely to provide a better constraint on the reconstruction of these unmeasured spatial frequencies, and produce smoother large-scale emission.

### PB-square normalization

The dirty image represents $I^{dirty} = I^{PB} \cdot \left[ I^{psf} \star \left( I^{PB} \cdot I^{sky} \right) \right]$

This third option (not currenly available for use, but supported internally) is to not do any PB-based divisions after the gridding and FFT (using *gridder=\'mosaic\'* or \'awproject\', but to let the minor cycle proceed as is.  Advantages of this approach are the elimination of error-inducing divisions by the primary beam (especially in low gain regions and near PB cut-off edges).

 

 

 

# Bibliography

1. 

