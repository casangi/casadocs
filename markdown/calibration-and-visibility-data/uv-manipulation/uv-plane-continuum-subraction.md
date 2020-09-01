

# UV Continuum Subraction 

Visibility-plane based continuum subtraction.

# Introduction

After general calibration is done and if there is significant continuum emission present in what is intended as a spectral line observation, continuum subtraction may be desirable. You can estimate and subtract continuum emission in the $uv$-plane prior to imaging or wait and subtract an estimate of it in the image-plane. Note that neither method is ideal, and the choice depends primarily upon the distribution and strength of the continuum emission. Subtraction in the $uv$-plane is desirable if continuum emission dominates the source, since deconvolution of the line emission will be more robust if it not subject to the deconvolution errors of the brighter continuum. There is also a performance benefit since the continuum is nearly the same in each channel of the observation, and it is desirable to avoid repeating its deconvolution in each channel. However, doing the continuum estimation in the $uv$-plane has the serious drawback that interpolating visibilities between channels is only a good approximation for emission from near the phase center. Thus, $uv$-plane based continuum subtraction will do an increasingly poor job for emission distributed further from the phase center. If the continuum emission is relatively weak, it is usually adequate to subtract it in the image plane; this is described in the Image Analysis section of this document. Here, we describe how to do continuum subtraction in the $uv$-plane.

# Basic Concept

A good review of different approaches to the subtraction of the continuum emission is found in Cornwell, Uson & Haddad (1992) [\[1\].](#Bibliography)

Sault (1994) [\[2\]](#Bibliography) gives the detailed analysis of the $uv$-plane based algorithms. We assume here that the sky brightness $I_\nu$ at a sky position $(l,m)$ is composed of the continuum (C) and line (L) emission such that $I_\nu(l,m)=C_\nu(l,m)+L_\nu(l,m)$. The continuum is estimated from fitting a polynomial selecting only \"line-free\" channels. The fitting of the visibiity spectrum is generally done for each sampling and separately for real and imaginary parts to make it a  linear process. Then the polynomial continuum model is subtracted from all channels.

This technique is known to work well when the dominant continuum source is at or near phase center. Its effectiveness tends to decline as distance to the source location with respect to the phase center increases and thus residual continuum left in the subtracted data increases. The effectiveness which has the same expression as in bandwidth smearing, can be parameterized as $\eta=\frac{\Delta\nu}{\nu}\frac{l_{0}}{\theta_{synth}}$ in terms of the the distance in the synthesized beam ($l_{0}/\theta_{synth}$) from the phase center,  where $\nu$ and 2$\Delta\nu$ are the observing frequency and the bandwidth, respectively. In order to the method to work well, $\eta<<1$ must be met. If the brightest continuum emission lies beyond $\frac{\nu}{\Delta\nu}$ beams from the phase center the source need to be shifted before fitting.

# CASA implementations

Currently tasks to do $uv$-plane continuum subtraction are available in uvcontsub, uvcontsub3 and mstransform. All of these tasks are based on the same basic concept described above and achieve essentially the same output but are based on different C++ implementations. uvcontsub has been used as the standard task to do this job and it is based on calibrator tool (\'cb\') to solve for continuum by fitting a polynomial. It creates \'A\'-type (\'additive noise\') caltable which will be deleted before the task exit ) and this solution is applied to correct (or subtract) the rest of the data.uvconstub3 is an experimental task  built with C++ methods outside the calibrator tool in order to eliminate some of extra IOs involve in use of the cb tool. More recently mstransform has been developed to consolidate all visibility data manipulation functions to one task. A new parameter (douvcontsub) in mstransform is available in CASA 4.7 or higher. The current plan is for mstransform to eventually replace uvcontsub and uvcontsub3.

In terms of parallelisation, only uvcontsub and the mstransform implementation (parameter douvcontsub) can process the input in parallel using the [mpi4casa framework](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing). See some notes here on how to handle [special cases in parallel](https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallel-calibration) using uvcontsub.

# The recommended procedures

The general recommended procuedures are described below.  For detailed examples on how to use the $uv$-plane continuum subtraction tasks, please refer  to the sections for each individual task. 

-   Finish general calibration.
-   Use clean/tclean task on the calibrated MS to form an exploratory cube that is useful for determining the line-free channels.
-   Use one of uv-plane continuum subutraction tasks with as low fit order as possible to estimate and subtruct the continuum from the input MS and write the continuum-subtracted MS.
-   Use clean/tclean with the continuum subtracted data to make an image cube of the line emission; inspect for residual continuum, tweak and repeat if needed. Computing image moments in nominally line-free channels may be a useful diagnostic if your imaging requirements are stringent.

 

## Using uvcontsub

The inputs to **uvcontsub** are:

```

#  uvcontsub :: Continuum fitting and subtraction in the uv plane
vis                 =         ''        #  Name of input MS.  Output goes to vis + ".contsub"
                                        #   (will be overwritten if already exists)
field               =         ''        #  Select field(s) using id(s) or name(s)
fitspw              =         ''        #  Spectral window:channel selection for fitting the
                                        #   continuum
combine             =         ''        #  Data axes to combine for the continuum estimation
                                        #   (none, or spw and/or scan)
solint              =      'int'        #  Continuum fit timescale (int recommended!)
fitorder            =          0        #  Polynomial order for the fits
spw                 =         ''        #  Spectral window selection for output
want_cont           =      False        #  Create vis + ".cont" to hold the continuum estimate.
```

For each baseline, and over the timescale specified in *solint*, **uvcontsub** will provide a polynomial fit to the real and imaginary parts of the (continuum-only) channels specified in *fitspw* (using the standard *spw* selection syntax), and then subtract this model from all channels specified in *spw*, or from all channels in spectral windows of *fitspw* if *spw=''*. By setting the subparameter *excludechannels=True*, the channel selection in *fitspw* will be inverted. In that case one can select the line channels themselves and/or corrupted channels that are not used in the continuum fit to the data. *fitspw* can also take frequency ranges, e.g.
```
fitspw='*:113.767~114.528GHz;114.744~115.447GHz'
```

where '*\**' indicates to go across all spws.Typically, low orders for the polynomial work best, like 0th (a constant), or 1st order (a linear fit). Use higher orders with caution and check your results carefully.Usually, one should set *solint='int'* which does no averaging and fits each integration. However, if the continuum emission comes from a small region around the phase center and fitorder = 0, then you can set *solint* larger (as long as it is shorter than the timescale for changes in the visibility function of the continuum). If your scans are short enough you can also use scan averaging with *combine='scan'* and *solint='inf'.* Be warned, setting solint too large will introduce "time smearing" in the estimated continuum and thus not properly subtract emission not at the phase center. Increasing *solint* speeds up the calculation but it does not improve the overall result quality of **uvcontsub** - although the continuum estimates of each baseline may be noisy (just like each visibility in a continuum MS may be noisy), it is better to use the ensemble of individual fits than to average the ensemble before fitting. Note that plotms can do time and baseline averaging on the fly to help you examine noisy data.

uvcontsub will append \".contsub\" for the continuum subtracted MS and \".cont\" if *want_cont=True*. Although the continuum model is available with the latter parameter, we recommend to use line-free channels for creating continuum images. The interpolation across the line channels will not gain better signal-to-noise but may introduce noise or model residuals.

 

## Using mstranform

**mstransform** has gotten support to subtract the continuum in the UV-plane using a polynomial fit along the spectral channels. This transformation can be stacked with the rest of the transformations supported by **mstransform**. To activate continum subtraction the option *douvcontsub* must be set:

```
douvcontsub = True # Enable continuum subtraction as in task **uvcontsub**
```

The most relevant parameter to fit the continuum is *fitspw*, which allows to select which channels are supposedly free of lines and therefore represent with better fidelity the continuum. The syntax of this parameter is similar to the usual syntax for the selection of spw\'s. For instance

```
fitspw='19:5~50;100~220,20:1~100'
```

will use channels 5 to 5 and 100 to 220 when computing the continuum of spw 19. For spw 20 it will use channels 1 to 100.

<div class="alert alert-warning">
There is currently no support to fit the continuum over several spw\'s at the same time. You can use **uvcontsub3** task if you need that functionality.
</div>

The output MS will contain the continuum subtracted signal. If one, on the other hand, is interested in the fitted continuum itself, then the parameter *want_cont* should be set to True. Note that in this case, if there are other transformations enabled in mstransform, the subsequent transformations will work on the fitted continuum data.

The algorithm implemented by **mstransform** allows to reject some outliers in the fit by doing an iterative fit. After the first fit has been obtained, the absolute residuals of each point with respect to the fit are computed and are used as weights for the next iteration. In this way outliers are usually given less and less weight in each iteration. To enable this feature, set the parameter *niter* to a value larger than 1.

```
  niter = 1 # Number of iterations for re-weighted linear fit
```

Additionally one can control the order of the polynomial fit using parameter *fitorder*

```
fitorder = 0 # Polynomial order for the fits
```

In the long term, it is foreseen that the current **uvcontusb** and **uvcontsub3** tasks are deprecated and are substituted by a new **uvcontusb** task that uses **mstransform** under the hood.

 

# Bibliography

1. Cornwell,\ T.\ J.,\ Uson,\ J.\ M.,\ &\ Haddad,\ N.\ 1992,\ A&A,\ 258,\ 583\ (
2. Sault,\ R.\ J.\ 1994,\ A&AS,\ 107,\ 55\ (
^

