

# Fit Gaussians to Visibilities 

Using uvmodelfit

### UV-Plane Model Fitting (**uvmodelfit**) {#sec291}

It is often desirable to fit simple analytic source component models directly to visibility data. Such fitting has its origins in early interferometry, especially VLBI, where arrays consisted of only a few antennas and the calibration and deconvolution problems were poorly constrained. These methods overcame the calibration uncertainties by fitting the models to calibration-independent closure quantities and the deconvolution problem by drastically limiting the number of free parameters required to describe the visibilities. Today, even with larger and better calibrated arrays, it is still desirable to use visibility model fitting in order to extract geometric properties such as the positions and sizes of discrete components in radio sources. Fits for physically meaningful component shapes such as disks, rings, and optically-thin spheres, though idealized, enable connecting source geometry directly to the physics of the emission regions.

Visibility model fitting is carried out by the **uvmodelfit** task. The inputs are:

```
# uvmodelfit :: Fit a single component source model to the uv data:
vis        =   ''       # Name of input visibility file
field      =   ''       # field name or index
spw        =   ''       # spectral window
selectdata =  False     # Activate data selection details
niter      =    5       # Number of fitting iterations to execute
comptype   =   'P'      # Component type (P=pt source,G=ell. gauss,D=ell. disk)
sourcepar  =  [1, 0, 0] # Starting guess (flux,xoff,yoff,bmajaxrat,bpa)
varypar    =   []       # Which parameters can vary in fit
outfile    =   ''       # Optional output component list table
```

<div class="alert alert-warning">
**ALERT**: This task currently only fits a single component.  For multiple, arbitrary shaped component fitting, we refer to the [uvmultifit](https://launchpad.net/uvmultifit) [\[1\]](#Bibliography) software that was developed by the Nordic [ALMA Regional Center Node](https://www.oso.nordic-alma.se/software-tools.php).  
</div>

The user specifies the number of non-linear solution iterations (*niter*), the component type (*comptype*), an initial guess for the component parameters (*sourcepar*), and optionally, a vector of Booleans selecting which component parameters should be allowed to vary (*varypar*), and a filename in which to store a CASA component list for use in other applications (*outfile*). Allowed comptypes are currently point 'P' or Gaussian 'G'.

The function returns a vector containing the resulting parameter list. This vector can be edited at the command line, and specified as input (*sourcepar*) for another round of fitting.

The *sourcepar* parameter is currently the only way to specify the starting inputs for the fit. For points, there are three inputs: I (total flux density), and relative direction (RA, Dec) offsets (in arcsec) from the observation's phase center. For Gaussians, there are three additional inputs: the Gaussian's semi-major axis width (arcsec), the aspect ratio, and position angle (degrees). It should be understood that the quality of the result is very sensitive to the starting inputs provided by the user. If this first guess is not sufficiently close to the global χ2 minimum, the algorithm will happily converge to an incorrect local minimum. In fact, the χ2 surface, as a function of the component's relative direction inputs, has a shape very much like the inverse of the absolute value of the dirty image of the field. Any peak in this image (positive or negative) corresponds to a local χ2 minimum that could conceivable capture the fit. It is the user's responsibility to ensure that the correct minimum does the capturing.

Currently, **uvmodelfit** relies on the likelihood that the source is very near the phase center (within a beamwidth) and/or the user's savvy in specifying the starting parameters. This fairly serious constraint will soon be relieved somewhat by enabling a rudimentary form of uv-plane weighting to increase the likelihood that the starting guess is on a slope in the correct χ2 valley.

Improvements in the works for visibility model fitting include:

-   User-specifiable uv-plane weighting
-   Additional component shapes, including elliptical disks, rings, and optically thin spheroids.
-   Optional calibration pre-application
-   Multiple components. The handling of more than one component depends mostly on efficient means of managing the list itself (not easy in command line options), which are currently under development.
-   Combined component and calibration fitting.

Example (see Figure 1):

```
# # Note: It's best to channel average the data if many channels # before running a modelfit #
split('ngc5921.ms','1445+099_avg.ms', datacolumn='corrected',field='1445*',width='63')
 

# Initial guess is that it's close to the phase center
# and has a flux of 2.0 (a priori we know it's 2.47)
uvmodelfit('1445+099_avg.ms', # use averaged data
           niter=5, # Do 5 iterations
           comptype='P', # P=Point source, G=Gaussian, D=Disk
           sourcepar=[2.0,.1,.1], # Source parameters for a point source
           spw='0',  
           outfile='gcal.cl') # Output component list file
```

```python
# Output looks like:
 There are 19656 - 3 = 19653 degrees of freedom.
  iter=0: reduced chi2=0.0418509: I=2, dir=[0.1, 0.1] arcsec
  iter=1: reduced chi2=0.003382: I=2.48562, dir=[-0.020069, -0.0268826] arcsec
  iter=2: reduced chi2=0.00338012: I=2.48614, dir=[0.00323428, -0.00232235] arcsec
  iter=3: reduced chi2=0.00338012: I=2.48614, dir=[0.00325324, -0.00228963] arcsec
  iter=4: reduced chi2=0.00338012: I=2.48614, dir=[0.00325324, -0.00228963] arcsec
  iter=5: reduced chi2=0.00338012: I=2.48614, dir=[0.00325324, -0.00228963] arcsec
 If data weights are arbitrarily scaled, the following formal errors
  will be underestimated by at least a factor sqrt(reduced chi2). If
  the fit is systematically poor, the errors are much worse.
 I = 2.48614 +/- 0.0176859
 x = 0.00325324 +/- 0.163019 arcsec
 y = -0.00228963 +/- 0.174458 arcsec
 Writing componentlist to file: /home/sandrock/smyers/Testing/Patch2/N5921/gcal.cl
```

```
# Fourier transform the component list to a model of the MS
ft('1445+099_avg.ms', complist='gcal.cl')

# Plot data versus uv-distance
plotms(vis='1445+099_avg.ms', xaxis='uvdist', datacolumn='corrected')

# Plot model data versus uv-distance
plotms(vis='1445+099_avg.ms', xaxis='uvdist', datacolumn='model')
```

 

<div class="alert alert-info">
The Nordic ALMA ARC node maintains the [UVMULTIFIT](http://www.oso.nordic-alma.se/software-tools.php) package that is based on CASA and which provides  addition, powerful tools for visibility modelling. See the [Nordic ARC software page](http://www.oso.nordic-alma.se/software-tools.php) and Marti-Vidal et al. (2014)  [\[1\]](#Bibliography) for details.

</div>

 

> <div>
>
> ------------------------------------------------------------------------
>
> </div>
>
> <div>
>
> ![](markdown/_media/443dad9cdcbb6b7f6ba2b778b0137baca052e3a2.png)
>
> <div>
>
>  
>
> </div>
>
> <div>
>
>   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------
>   Type                                                                                                                                                                                                         Figure
>   ID                                                                                                                                                                                                           1
>   Plot visualizing the corrected data (red and blue points) and the uv model fit (green circles). This particular plot was made using **plotxy**, which was deprecated in CASA 5.1 - use **plotms** instead.   
>   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------
>
>  
>
>
>
> </div>
>
> </div>

# Bibliography

1. Marti-Vidal,\ I.,\ Vlemmings,\ W.\~H.\~T.,\ Muller,\ S.,\ &\ Casey,\ S.\ 2014,\ A&A,\ 563,\ A136\ (
1. Marti-Vidal\ et\ al.\ 2014,\ A&A\ 563,\ 136\ (
^

