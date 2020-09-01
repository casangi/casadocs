

# Spectral Analysis 

Moments, Spectral line fitting, Continuum subtraction etc.

#  Continuum Subtraction on an Image Cube (imcontsub)

One method to separate line and continuum emission in an image cube is to specify a number of line-free channels in that cube, make a linear fit to the visibilities in those channels, and subtract the fit from the whole cube. Note that the task **uvcontsub** serves a similar purpose but the subtraction is performed in visibility space (see [UV Continuum Subtraction](resolveuid/2c85a22fd1004fb194cf1890672ad94a)). The **imcontsub** task will perform a polynomial baseline fit to the specified channels from an image cube and subtract it from all channels.The default inputs are:

```
#  imcontsub :: Continuum subtraction on images
imagename  =      ''   #  Name of the input image
linefile   =      ''   #  Output line image file name
contfile   =      ''   #  Output continuum image file name
fitorder   =       0   #  Polynomial order for the continuum estimation
region     =      ''   #  Image region or name to process see viewer
box        =      ''   #  Select one or more box regions
chans      =      ''   #  Select the channel(spectral) range
stokes     =      ''   #  Stokes params to image (I,IV,IQU,IQUV)
```

Area selection using *box* and *region* is detailed in the [box](#region-selection--box-) and [region](#regions--region-) sections. Image cube plane selection using *chans* and *stokes* are described in the [Plane selection](#plane-selection--chans--stokes-) section.

<div class="alert alert-warning">
**ALERT:** **imcontsub** has issues when the image does not contain a spectral or stokes axis. Errors are generated when run on an image missing one or both of these axes. You will need to use the toolkit (e.g. the **ia.adddegaxes** method) to add degenerate missing axes to the image.
</div>

##  Examples for **imcontsub**

For example, we first make a clean image from data in which no uv-plane continuum subtraction has been performed:

```
# Now clean, keeping all the channels except first and last
default('clean')
vis = 'ngc5921.demo.src.split.ms'
imagename = 'ngc5921.demo.nouvcontsub'
mode = 'channel'
nchan = 61
start = 1
width = 1
imsize = [256,256]
psfmode = 'clark'
imagermode = ''
cell = [15.,15.]
niter = 6000
threshold='8.0mJy'
weighting = 'briggs'
robust = 0.5
mask = [108,108,148,148]
interactive=False
clean()

# It will have made the image:
# -----------------------------
# ngc5921.demo.nouvcontsub.image

# You can view this image
viewer('ngc5921.demo.nouvcontsub.image')
```

Channels 0 through 4 and 50 through 60 are line-free. Continuum subtraction is then performed with:

```
default('imcontsub')
imagename = 'ngc5921.demo.nouvcontsub.image'
linefile  = 'ngc5921.demo.nouvcontsub.lineimage'
contfile  = 'ngc5921.demo.nouvcontsub.contimage'
fitorder  = 1
chans      = '0~4,50~60'
stokes    = 'I'
imcontsub()
```

 

# Computing the Moments of an Image Cube (**immoments**)

For spectral line datasets, the output of the imaging process is an image cube, with a frequency or velocity channel axis in addition to the two sky coordinate axes. This can be most easily thought of as a series of image planes stacked along the spectral dimension. A useful product to compute is to collapse the cube into a moment image by taking a linear combination of the individual planes:

$M_m(x_i,y_i) = \sum_k^N w_m(x_i,y_i,v_k)\,I(x_i,y_i,v_k)$

for pixel i and channel k in the cube I. There are a number of choices to form the moment-m, usually approximating some polynomial expansion of the intensity distribution over velocity mean or sum, gradient, dispersion, skew, kurtosis, etc. There are other possibilities (other than a weighted sum) for calculating the image, such as median filtering, finding minima or maxima along the spectral axis, or absolute mean deviations. And the axis along which to do these calculations need not be the spectral axis (i.e. do moments along Dec for a RA-Velocity image). We will treat all of these as generalized instances of a "moment" map.The **immoments** task will compute basic moment images from a cube. The default inputs are:

```
#  immoments :: Compute moments of an image cube:
imagename    =         ''   #   Input image name
moments      =        [0]   #  List of moments you would like to compute
axis         = 'spectral'   #  The moment axis: ra, dec, lat, long, spectral, or stokes
region       =         ''   #  Image Region.  Use viewer
box          =         ''   #  Select one or more box regions
chans        =         ''   #  Select the channel(spectral) range
stokes       =         ''   #  Stokes params to image (I,IV,IQU,IQUV)
mask         =         ''   #  mask used for selecting the area of the
                            #   image to calculate the moments on
includepix   =         -1   #  Range of pixel values to include
excludepix   =         -1   #  Range of pixel values to exclude
outfile      =         ''   #  Output image file name (or root for multiple moments)
```

This task will operate on the input file given by *imagename* and produce a new image or set of images based on the name given in *outfile*.The *moments* parameter chooses which moments are calculated. The choices for the operation mode are:

-   moments=-1  - mean value of the spectrum
-   moments=0   - integrated value of the spectrum
-   moments=1   - intensity weighted coordinate; traditionally used to get \'velocity fields\'
-   moments=2   - intensity weighted dispersion of the coordinate; traditionally used to get \'velocity dispersion\'
-   moments=3   - median of I
-   moments=4   - median coordinate
-   moments=5   - standard deviation about the mean of the spectrum
-   moments=6   - root mean square of the spectrum
-   moments=7   - absolute mean deviation of the spectrum
-   moments=8   - maximum value of the spectrum
-   moments=9   - coordinate of the maximum value of the spectrum
-   moments=10  - minimum value of the spectrum
-   moments=11  - coordinate of the minimum value of the spectrum

The meaning of these is described in the [CASA Toolkit Manual](https://casa.nrao.edu/docs/CasaRef/CasaRef.html), that describes the associated [image.moments](https://casa.nrao.edu/docs/CasaRef/image.moments.html#x62-620001.1.1) tool.The *axis* parameter sets the axis along which the moment is "collapsed" or calculated. Choices are: \'ra\', \'dec\', \'lat\', \'long\', \'spectral\', or \'stokes\'. A standard moment-0 or moment-1 image of a spectral cube would use the default choice 'spectral'. One could make a position-velocity map by setting \'ra\' or \'dec\'.The *includepix* and *excludepix* parameters are used to set ranges for the inclusion and exclusion of pixels based on values. For example, i*ncludepix=\[0.05,100.0\]* will include pixels with values from 50 mJy to 1000 Jy, and *excludepix=\[100.0,1000.0\]* will exclude pixels with values from 100 to 1000 Jy.If a single moment is chosen, the outfile specifies the exact name of the output image. If multiple moments are chosen, then outfile will be used as the root of the output filenames, which will get different suffixes for each moment. For image cubes that contain different beam sizes for each plane, **immoments** will smooth all planes to the largest beam size first, then collapse to the desired moment.

 

## Hints for using **immoments**

In order to make an unbiased moment-0 image, do not put in any thresholding using *includepix* or *excludepix*. This is so that the (presumably) zero-mean noise fluctuations in off-line parts of the image cube will cancel out. If you image has large biases, like a pronounced clean bowl due to missing large-scale flux, then your moment-0 image will be biased also. It will be difficult to alleviate this with a threshold, but you can try.

To make a usable moment-1 (or higher) image, on the other hand, it is critical to set a reasonable threshold to exclude noise from being added to the moment maps. Something like a few times the rms noise level in the usable planes seems to work (put into *includepix* or *excludepix* as needed). Also use *chans* to ignore channels with bad data.

 

## Examples using **immoments**

Below is an example for **immoments**:

```
default('immoments')
imagename = 'ngc5921.demo.cleanimg'
# Do first and second spectral moments
axis  = 'spectral'
chans = ''
moments = [0,1]
# Need to mask out noisy pixels, currently done
# using hard global limits
excludepix = [-100,0.009]
outfile = 'ngc5921.demo.moments'
 
immoments()

# It will have made the images:
# --------------------------------------
# ngc5921.demo.moments.integrated
# ngc5921.demo.moments.weighted_coord
```

Other examples of NGC2403 (a moment-0 image of a VLA line dataset) and NGC4826 (a moment-1 image of a BIMA CO line dataset) are shown in the Figure [below](http://casa.nrao.edu/casadocs/stable/image-analysis/dealing-with-images#figid-analysisfigmoments).

![0d5fd0d2ee99bce18c9c5fcce6f3439c8f9042ce](media/0d5fd0d2ee99bce18c9c5fcce6f3439c8f9042ce.png)

![4e1cdd67ee0996b1a1e19225e04cb383489aabd1](media/4e1cdd67ee0996b1a1e19225e04cb383489aabd1.png)

>NGC2403 VLA moment zero (left) and NGC4826 BIMA moment one (right) images as shown in the viewer.
  

#  Generating Position-Velocity Diagrams (impv)

CASA can generate position-velocity (PV) diagrams via the task **impv** or directly in the **viewer** (see [Image Cube Visualization](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-cube-visualization)**)**.  The viewer application calls the task:

```
#  impv :: Construct a position-velocity image by choosing two points in the direction plane.
imagename           =         ''        #  Name of the input image
outfile             =         ''        #  Output image name. If empty, no image is written.
mode                =   'coords'        #  If 'coords', use start and end values. If 'length', use
                                        #   center, length, and pa values.
width               =          1        #  Width of slice for averaging pixels perpendicular to the
                                        #   slice. Must be an odd positive integer or valid
                                        #   quantity. See help for details.
unit                =   'arcsec'        #  Unit for the offset axis in the resulting image. Must be
                                        #   a unit of angular measure.
chans               =         ''        #  Channels to use. 
                                        #   Channels must be contiguous. Default is to use all
                                        #   channels.
     region         =         ''        #  Region selection. Default is entire image. No selection
                                        #   is permitted in the direction plane. 

stokes              =        'I'        #  Stokes planes to use. Planes must be contiguous. Default
                                        #   is to use all stokes.
mask                =         []        #  Mask to use. Default is none.
     stretch        =      False        #  Stretch the mask if necessary and possible? Default False
```

PV diagrams are generated by "slicing" a datacube through the RA/DEC planes. The "slit" can be defined either by start/end coordinates or by a length, center coordinate, and position angle. Averaged over the width of the 'slit' the image cube values are then stored in a new image with position and velocity as the two axes. The slit position is specified by a start and end pixel in the RA/DEC plane of the data cube. An angular unit can be set to define what is stored in the resulting PV image.

 

# 1-dimensional Smoothing (specsmooth)

To gain higher signal-to-noise of data cubes, one can smooth the data along one dimension (for 2-dimensional smoothing, see **imsmooth** [below](#2-dimensional-smoothing--image-convolution--imsmooth-)**)**. Typically this is the spectral axis. Hanning and Boxcar smoothing kernels are available in the task **specsmooth**:

```
#  specsmooth :: Smooth an image region in one dimension
imagename           =         ''        #  Name of the input image
outfile             =         ''        #  Output image name.
region              =         ''        #  Region selection. Default is to use the full
                                        #   image.
     box            =         ''        #  Rectangular region to select in
                                        #   direction plane. Default is to use the entire
                                        #   direction plane.

mask                =         ''        #  Mask to use. Default is none..
axis                =         -1        #  The profile axis. Default: use the
                                        #   spectral axis if one exists, axis 0
                                        #   otherwise (<0).
function            =  'hanning'        #  Convolution function. hanning and boxcar
                                        #   are supported functions. Minimum match
                                        #   is supported.
dmethod             =     'copy'        #  Decimation method. '' means no
                                        #   decimation, 'copy' and 'mean' are also
                                        #   supported (minimum match).
```

The parameter *dmethod=\'copy\'* allows one to only keep every nth channel, if the smoothing kernel has a width of n. Leaving this parameter empty will return the same size cube as the input and setting it to 'mean' will average planes using the kernel width.

 

 

#    Spectral Line fitting with **specfit**

**specfit** is a powerful task to perform spectral line fits in data cubes. Three types of fitting functions are currently supported, polynomials, Gaussians, and Lorentzians. **specfit** can fit these functions in two ways: over data that were averaged across a region (*multifit=False*) or on a pixel by pixel basis (*multifit=True*).

```
#  specfit :: Fit 1-dimensional Gaussians and/or polynomial models to an image or image region
imagename           =         ''        #  Name of the input image
box                 =         ''        #  Rectangular box in direction coordinate
                                        #   blc, trc. Default: entire image ('').
region              =         ''        #  Region of interest. Default: Do
                                        #   not use a region.
chans               =         ''        #  Channels to use. Channels must be
                                        #   contiguous. Default: all channels ('').
stokes              =         ''        #  Stokes planes to use. Planes must be
                                        #   contiguous. Default: all stokes ('').
axis                =         -1        #  The profile axis. Default: use the
                                        #   spectral axis if one exists, axis 0
                                        #   otherwise (<0).
mask                =         ''        #  Mask to use. Default is
                                        #   none..
poly                =         -1        #  Order of polynomial element.  Default: do
                                        #   not fit a polynomial (<0).
estimates           =         ''        #  Name of file containing initial estimates.
                                        #   Default: No initial estimates ('').
     ngauss         =          1        #  Number of Gaussian elements.  Default: 1.
     pampest        =         ''        #  Initial estimate of PCF profile (gaussian
                                        #   or lorentzian) amplitudes.
     pcenterest     =         ''        #  Initial estimate PCF profile centers, in
                                        #   pixels.
     pfwhmest       =         ''        #  Initial estimate PCF profile FWHMs, in
                                        #   pixels.
     pfix           =         ''        #  PCF profile parameters to fix during fit.
     pfunc          =         ''        #  PCF singlet functions to fit. 'gaussian'
                                        #   or 'lorentzian' (minimal match
                                        #   supported). Unspecified means all
                                        #   gaussians.

minpts              =          0        #  Minimum number of unmasked points
                                        #   necessary to attempt fit.
multifit            =       True        #  If true, fit a profile along the desired
                                        #   axis at each pixel in the specified
                                        #   region. If false, average the non-fit
                                        #   axis pixels and do a single fit to that
                                        #   average profile. Default False.
     amp            =         ''        #  Name of amplitude solution image. Default:
                                        #   do not write the image ('').
     amperr         =         ''        #  Name of amplitude solution error image.
                                        #   Default: do not write the image ('').
     center         =         ''        #  Name of center solution image. Default: do
                                        #   not write the image ('').
     centererr      =         ''        #  Name of center solution error image.
                                        #   Default: do not write the image ('').
     fwhm           =         ''        #  Name of fwhm solution image. Default: do
                                        #   not write the image ('').
     fwhmerr        =         ''        #  Name of fwhm solution error image.
                                        #   Default: do not write the image ('').
     integral       =         ''        #  Prefix of name of integral solution image.
                                        #   Name of image will have gaussian
                                        #   component number appended.  Default: do
                                        #   not write the image ('').
     integralerr    =         ''        #  Prefix of name of integral error solution
                                        #   image. Name of image will have gaussian
                                        #   component number appended.  Default: do
                                        #   not write the image ('').

model               =         ''        #  Name of model image. Default: do not write
                                        #   the model image ('').
residual            =         ''        #  Name of residual image. Default: do not
                                        #   write the residual image ('').
wantreturn          =       True        #  Should a record summarizing the results be
                                        #   returned?
logresults          =       True        #  Output results to logger?
gmncomps            =          0        #  Number of components in each gaussian
                                        #   multiplet to fit
gmampcon            =         ''        #  The amplitude ratio constraints for non-
                                        #   reference components to reference
                                        #   component in gaussian multiplets.
gmcentercon         =         ''        #  The center offset constraints (in pixels)
                                        #   for non-reference components to reference
                                        #   component in gaussian multiplets.
gmfwhmcon           =         ''        #  The FWHM  ratio constraints for non-
                                        #   reference components to reference
                                        #   component in gaussian multiplets.
gmampest            =      [0.0]        #  Initial estimate of individual gaussian
                                        #   amplitudes in gaussian multiplets.
gmcenterest         =      [0.0]        #  Initial estimate of individual gaussian
                                        #   centers in gaussian multiplets, in
                                        #   pixels.
gmfwhmest           =      [0.0]        #  Initial estimate of individual gaussian
                                        #   FWHMss in gaussian multiplets, in pixels.
gmfix               =         ''        #  Parameters of individual gaussians in
                                        #   gaussian multiplets to fix during fit.
logfile             =         ''        #  File in which to log results. Default is
                                        #   not to write a logfile.
goodamprange        =      [0.0]        #  Acceptable amplitude solution range. [0.0]
                                        #   => all amplitude solutions are
                                        #   acceptable.
goodcenterrange     =      [0.0]        #  Acceptable center solution range in pixels
                                        #   relative to region start. [0.0] => all
                                        #   center solutions are acceptable.
goodfwhmrange       =      [0.0]        #  Acceptable FWHM solution range in pixels.
                                        #   [0.0] => all FWHM solutions are
                                        #   acceptable.
sigma               =         ''        #  Standard deviation array or image name.
```

##  Polynomial Fits

Polynomials can be fit by specifying the polynomial order in *poly*. Negative orders will not fit any polynomials.

##  Lorentzian and Gaussian Fits

Gaussian and Lorentzian fits are very similar, they both require amplitude, center, and FWHM to be fully specified. All of the following discussion is thus valid for both functions. The parameter *pfunc* controls whether Gaussian or Lorentzian functions are to be used. Default is all Gaussians. *pfunc=\[\'L\', \'G\', \'G\', \'L\'\]* would use Lorentzian, Gaussian, Gaussian, and Lorentzian components in the order they appear in the estimates file (see below).

###  One or more single Gaussian/Lorentzian

For Gaussian and Lorentzian fits, the task will allow multiple components and **specfit** will try to find the best solution. The parameter *space*, however, is usually not uniform and to avoid local minima in the goodness-of-fit space, one can provide initial start values for the fits. This can be done either through the parameters *pampest*, *pcenterest*, and *pfwhmest* for the amplitudes, center, and FWHM estimates in image coordinates. *pfix* can take parameters that specify fixed fit values. Any combination of the characters \'*p\'* (peak), \'*c\'* (center), and \'*f\'* (fwhm) are permitted, e.g. \'*fc*\' will hold the fwhm and the center constant during the fit. Fixed parameters will have no errors associated with them in the solution. Alternatively, a file with initial values can be supplied by the *estimates* parameter (one Gaussian/Lorentzian parameter set per line). The file has the following format:

    [peak intensity], [center], [fwhm], [optional fixed parameter string]

The first three values are required and must be numerical values. The peak intensity must be expressed in map units, while the center and fwhm must be specified in pixels. The fourth value is optional and if present, represents the parameter(s) that should be held constant during the fit (see above).An example estimates file is:

    # estimates file indicating that two Gaussians should be fit
    # first guassian estimate, peak=40, center at pixel number 10.5, 
    # fwhm = 5.8 pixels, all parameters allowed to vary during
    # fit
    40, 10.5, 5.8
    # second Gaussian, peak = 4, center at pixel number 90.2, 
    # fwhm = 7.2 pixels, hold fwhm constant
    4, 90.2, 7.2, f
    # end file

and the output of a typical execution, e.g.

```python
specfit(imagename='IRC10216_HC3N.cube_r0.5.image',
region='specfit.crtf', multifit=F, estimates='', ngauss=2)

('specfit.crtf' is a CASA regions file, see Section D)
will be

Fit   :
    RA           :   09:47:57.49
    Dec          :   13.16.46.46
    Stokes       : I
    Pixel        : [146.002, 164.499, 0.000,  *]
    Attempted    : YES
    Converged    : YES
    Iterations   : 28
    Results for component 0:
        Type     : GAUSSIAN
        Peak     : 5.76 +/- 0.45 mJy/beam
        Center   : -15.96 +/- 0.32 km/s
                   40.78 +/- 0.31 pixel
        FWHM     : 7.70 +/- 0.77 km/s
                   7.48 +/- 0.74 pixel
        Integral : 47.2 +/- 6.0 mJy/beam.km/s
    Results for component 1:
        Type     : GAUSSIAN
        Peak     : 4.37 +/- 0.33 mJy/beam
        Center   : -33.51 +/- 0.58 km/s
                   23.73 +/- 0.57 pixel
        FWHM     : 15.1 +/- 1.5 km/s
                   14.7 +/- 1.5 pixel
        Integral : 70.2 +/- 8.8 mJy/beam.km/s
```

If *wantreturn=True* (the default value), the task returns a python dictionary (here captured in a variable with the inventive name of \'*fitresults\'*) :

```
fitresults=specfit(imagename='IRC10216_HC3N.cube_r0.5.image', region='specfit.rgn', multifit=F,
        estimates='', ngauss=2)
```

The values can then be used by other python code for further processing.

 

### Gaussian Multiplets

It is possible to fit a number of Gaussians together, as multiplets with restrictions. All restrictions are relative to a reference Gaussian (the zero'th component of each multiplet). *gncomps* specifies the number of Gaussians for each multiplets, and, in fact, a number of these multiplets can be fit simultaneously. *gncomps=\[2,4,3\]*, e.g. fits a 2-component Gaussian, a 4-component Gaussian, and a 3-component Gaussian all at once. The initial parameter estimates can be specified with the *gmampest*, *gmcenterest*, and *gmfwhmest* parameters and the estimates are simply listed in the sequence of *gncomps*. E.g. if *gncomps=\[2,4,3\]* is specified with multiplet G0 consisting of 2 Gaussians a, b, multiplet G1 of 4 Gaussians c, d, e, f, and multiplet G2 of three Gaussians g, h, i, the parameter list in *gm\*est* would be like *gm\*est=\[a,b,c,d,e,f,g,h,i\]*.Restrictions can be specified via the *gmampcon* parameter for the amplitude ratio (non-reference to reference), *gmcentercon* for the offset in pixels (to a reference), and *gmfwhmcon* for the FWHM ratio (non-reference to reference). A value of 0 will not constrain anything. The reference is always the zero'th component in each multiplet, in our example, Gaussians a, c, and g. They cannot be constrained. So *gmncomps=\[2, 4, 3\]*, *gmampcon= \[ 0 , 0.2, 0 , 0.1, 4.5, 0 \]*, *gcentercon=\[24.2, 45.6, 92.7, 0 , -22.8, -33.5\],* and *gfwhmcon=\' \'* would constrain Gaussians b relative to a with a 24.2 pixel offset, Gaussian d to c with a amplitude ratio of 0.2 and a 45.6 pixel offset, Gaussian e to c with a offset of 92.7 pixels, etc. Restrictions will overrule any estimates.The parameters *goodamprange*, *goodcenterrange*, and *goodfwhmrange* can be used to limit the range of amplitude, center, and fwhm solutions for all Gaussians.

###  Pixel-by-pixel fits

As mentioned above, **specfit** can also fit spectral cubes on a pixel by pixel basis. In this case, one can choose to write none, any or all of the solution and error images for Gaussian/Lorentzian fits via the parameters *amp*, *amperr*, *center*, *centererr*, *fwhm*, and *fwhmerr*. Each Gaussian component will produce a set of images *\_0, \_1*, etc. suffixes. Writing analogous images for polynomial coefficients is not yet supported although polynomial fits when *multifit=True* is supported. Best fit coefficients are written to the logger. Pixels for which fits were not attempted or did not converge will be masked as bad.

#  Spatial Spectral Line Properties (**specflux**)

**specflux** calculates the flux as a function of frequency and velocity over a selected spatial region. Flux densities of Jy/beam are being converted to Jy by properly integrating over the selected region.The input parameters of **specflux** are:

```
#  specflux :: Report details of an image spectrum.
imagename           =         ''        #  Name of the input image
box                 =         ''        #  Rectangular region to select in
                                        #   direction plane. Default is to use the entire
                                        #   direction plane.
     region         =         ''        #  Region selection.  Default is to use the full
                                        #   image.

chans               =         ''        #  Channels to use.  Default is to use all
                                        #   channels.
stokes              =         ''        #  Stokes planes to use.  Default is to
                                        #   use all Stokes planes.
mask                =         ''        #  Mask to use.  Default
                                        #   is none.
unit                =     'km/s'        #  Unit to use for the abscissa. Must be
                                        #   conformant with a typical spectral axis
                                        #   unit.
major               =         ''        #  Major axis of overriding restoring beam.
                                        #   If specified, must be a valid quantity.
minor               =         ''        #  Minor axis of overriding restoring beam.
                                        #   If specified, must be a valid quantity
logfile             =         ''        #  File which to write details. Default is
                                        #   to not write to a file.
```

The results can be written into a logfile to be plotted in other packages.

 

# Plot Spectra on a Map (plotprofilemap)

The **profilemap** task enables plotting spectra according to their pointing directions (a.k.a. a profile map) in plots. The input should be CASA image,or FITS format cube. Spectra within the cube are averaged into a bin number specified with the *numpanels* keyword. Absent or masked data are treated according to *plotmasked* keyword setting.

```
plotprofilemap(imagename='interesting_spectralcube_casaimge.im',
figfile = 'grid_map.png',
separatepanel=F,
spectralaxis = 'velocity',
title = 'myprofilemap',
transparent = F,
showaxislabel = True,
showtick = True,
showticklabel = True,
pol=0,
numpanels='8')
```

 

# Calculation of Rotation Measures (**rmfit**)

**rmfit** is an image domain task that accepts an input cube image containing Stokes Q and U axes and will generate the rotation measure by performing a least square fit in the image domain to obtain the best fit to the equation  $\chi = \chi_0 + RM\times \lambda^2$.

The inputs to **rmfit** are:

```
#  rmfit :: Calculate rotation measure.
imagename           =         ''        #  Name(s) of the input image(s). Must be specified.
rm                  =         ''        #  Output rotation measure image name. If not specified, no
                                        #   image is written.
rmerr               =         ''        #  Output rotation measure error image name. If not
                                        #   specified, no image is written.
pa0                 =         ''        #  Output position angle (degrees) at zero wavelength image
                                        #   name. If not specified, no image is written.
pa0err              =         ''        #  Output position angle (degrees) at zero wavelength error
                                        #   image name. If not specified, no image is written.
nturns              =         ''        #  Output number of turns image name. If not specified, no
                                        #   image is written.
chisq               =         ''        #  Output reduced chi squared image name. If not specified,
                                        #   no image is written.
sigma               =         ''        #  Estimate of the thermal noise.  A value less than 0 means
                                        #   auto estimate.
rmfg                =        0.0        #  Foreground rotation measure in rad/m/m to subtract.
rmmax               =        0.0        #  Maximum rotation measure in rad/m/m for which to solve.
                                        #   IMPORTANT TO SPECIFY.
maxpaerr            =      1e+30        #  Maximum input position angle error in degrees to allow in
                                        #   solution determination.
```

This task generates the rotation measure image from stokes Q and U measurements at several different frequencies. You are required to specify the name of at least one image with a polarization axis containing stokes Q and U planes and with a frequency axis containing more than two pixels. The frequencies do not have to be equally spaced (i.e. the frequency coordinate can be a tabular coordinate). It will work out the position angle images for you. You may also specify multiple image names, in which case these images will first be concatenated along the spectral axis using **ia.imageconcat**. The requirements are that for all images, the axis order must be the same and the number of pixels along each axis must be identical, except for the spectral axis which may differ in length between images. The spectral axis need not be contiguous from one image to another. See also the i**magepol.fourierrotationmeasure** function for a new Fourier-based approach.Rotation measure algorithms that work robustly are few. The main problem is in trying to account for the $n- \pi$ ambiguity (see Leahy et al.1986 - Appendix A.1) [\[1\]](#Bibliography) and the [MIRIAD manual](http://www.cfa.harvard.edu/sma/miriad/manuals/SMAuguide/smauserhtml/imrm.html).

But as in all these algorithms, the basic process is that for each spatial pixel, the position angle vs frequency data is fit to determine the rotation measure and the position angle at zero wavelength (and associated errors). An image containing the number of $n- \pi$ turns that were added to the data at each spatial pixel and for which the best fit was found can be written. The reduced $\chi^2$ image for the fits can also be written. Any combination of output images can be written.

<div class="alert alert-info">
**NOTE**: No assessment of curvature (i.e. deviation from the simple linear position angle - $\lambda^2$ functional form) is made.
</div>

The parameter *sigma* gives the thermal noise in Stokes Q and U. By default it is determined automatically using the image data. But if it proves to be inaccurate (maybe not many signal-free pixels), it may be specified. This is used for calculating the error in the position angles (via propagation of Gaussian errors).The argument *maxpaerr* specifies the maximum allowable error in the position angle that is acceptable. The default is an infinite value. From the standard propagation of errors, the error in the linearly polarized position angle is determined from the Stokes Q and U images (at each directional pixel for each frequency). If the position angle error for any pixel exceeds the specified value, the position angle at that pixel is omitted from the fit. The process generates an error for the fit and this is used to compute the errors in the output images.

<div class="alert alert-info">
**NOTE**: *maxpaerr* is not used to mask pixels in the output images.
</div>

The argument *rmfg* is used to specify a foreground RM value. For example, you may know the mean RM in some direction out of the Galaxy, then including this can improve the algorithm by reducing ambiguity. The parameter *rmmax* specifies the maximum absolute RM value that should be solved for. This quite an important parameter. If you leave it at the default, zero, no ambiguity handling will be used. So some a priori information should be supplied; this is the basic problem with rotation measure algorithms.

#  Calculation of Spectral Indices and Higher Order Polynomials (**spxfit**)

This application fits a power logarithmic polynomial or a logarithmic transformed polynomial to pixel values along a specified axis of an image or images. These functions are most often used for fitting the spectral index and higher order terms of a spectrum. A power logarithmic polynomial has the form

$y = \frac{c_0 x}{D^{(c_1 + c_2 \ln(x/D) + c_3 \ln(x/D)^2 + c_n \ln(x/D)^{(n - 1)})}}$

and a logarithmic transformed polynomial is simply the result of this equation after taking the natural log of both sides so that it has the form

$\ln(y) = c_0 + c_1 \ln(x) + c_2 \ln(x/D)^2 +  ... + c_n \ln(x/D)^n$

Because the logarithm of the ordinate values must be taken before fitting a logarithmic transformed polynomial, all non-positive pixel values are effectively masked for the purposes of fitting. The coefficients of the two forms are equal to each other except that c0 in the second equation is equal to $\ln(c_0)$ of the first. In the case of fitting a spectral index, which is traditionally represented as $\alpha$, is equal to $c_1$. In both cases, $D$ is a normalization constant used so that abscissa values are closer to unity when they are sent to the fitter. This generally improves the probability that the fit will converge. This parameter may be specified via the *div* parameter. A value of 0 (the default) indicates that the application should determine a reasonable value for $D$, which is determined via$D = 10^{\int(\log10(\sqrt(\min(x)*\max(x)))}$where *min(x)* and *max(x)* are the minimum and maximum abscissa values, respectively.The inputs are:

```
 #  spxfit :: Fit a 1-dimensional model to an image or image region
for determination of spectral index.
imagename           =                   #  Name of the input image(s)
box                 =         ''        #  Rectangular box in
                                        #   direction coordinate blc, trc.
                                        #   Default: entire image ('').
region              =         ''        #  Region of interest.  Default:
                                        #   Do not use a region.
chans               =         ''        #  Channels to use. Channels
                                        #   must be contiguous.  Default: all channels ('').
stokes              =         ''        #  Stokes planes to
                                        #   use. Planes must be contiguous. Default:
                                        #   all stokes ('').
axis                =         -1        #  The profile axis. Default:
                                        #   use the spectral axis if one
                                        #   exists, axis 0 otherwise (<0).
mask                =         ''        #  Mask to use.  Default is none.
minpts              =          1        #  Minimum number of unmasked
                                        #   points necessary to attempt
                                        #   fit.
multifit            =       True        #  If true, fit a profile
                                        #   along the desired axis at each
                                        #   pixel in the specified
                                        #   region. If false, average the
                                        #   non-fit axis pixels and do
                                        #   a single fit to that average
                                        #   profile. Default False.
     spxsol         =         ''        #  Name of the spectral index
                                        #   function coefficient solution
                                        #   image to write.
     spxerr         =         ''        #  Name of the spectral index
                                        #   function coefficient error
                                        #   image to write.
     model          =         ''        #  Name of model
                                        #   image. Default: do not write the model
                                        #   image ('').
     residual       =         ''        #  Name of residual
                                        #   image. Default: do not write the
                                        #   residual image ('').
spxtype             =      'plp'        #  Type of function to
                                        #   fit. 'plp' => power logarithmic
                                        #   polynomial, 'ltp' =>
                                        #   logarithmic transformed polynomial.
spxest              =         []        #  Initial estimates for the
                                        #   spectral index function
                                        #   coefficients.
spxfix              =         []        #  Fix the corresponding spectral index function
                                        #   coefficients during the fit. True=>hold fixed.
div                 =          0        #  Divisor (numerical value or
                                        #   quantity) to use in the
                                        #   logarithmic terms of the
                                        #   plp or ltp function. 0 =>
                                        #   calculate a useful value on the fly.
wantreturn          =       True        #  Should a record summarizing
                                        #   the results be returned?
logresults          =       True        #  Output results to logger?
logfile             =         ''        #  File in which to log
                                        #   results. Default is not to write a
                                        #   logfile.
sigma               =         -1        #  Standard deviation array or image name(s).
     outsigma       =         ''        #  Name of output image used
                                        #   for standard deviation. Ignored
                                        #   if sigma is empty.
```

For more than a single input image or cube, all images must have the same dimensions along all axes other than the fit axis. *multifit* will perform a per-pixel fit, otherwise there will be a single value over the entire region.

 

# Search for Spectral Line Rest Frequencies (**slsearch**)

The **slsearch** task allows the spectral line enthusiast to find their favorite spectral lines in subset of the [Splatalogue spectral line catalog](http://www.splatalogue.net) which is distributed with CASA. In addition, one can export custom catalogs from Splatalogue and import them to CASA using the task **splattotable** (next section) or tool method **sl.splattotable**. One can even import catalogs with lines not in Splatalogue using the same file format.The inputs to **slsearch** are as follows:

```
#  slsearch :: Search a spectral line table.
tablename           =         ''        #  Input spectral line table name to
                                        #   search. If not specified, use the
                                        #   default table in the system.
outfile             =         ''        #  Results table name. Blank means do not
                                        #   write the table to disk.
freqrange           =   [84, 90]        #  Frequency range in GHz.
species             =       ['']        #  Species to search for.
reconly             =      False        #  List only NRAO recommended
                                        #   frequencies.
chemnames           =       ['']        #  Chemical names to search for.
qns                 =       ['']        #  Resolved quantum numbers to search
                                        #   for.
rrlinclude          =       True        #  Include RRLs in the result set?
rrlonly             =      False        #  Include only RRLs in the result set?
     intensity      =         -1        #  CDMS/JPL intensity range. -1 -> do not
                                        #   use an intensity range.
     smu2           =         -1        #  S*mu*mu range in Debye**2. -1 -> do
                                        #   not use an S*mu*mu range.
     loga           =         -1        #  log(A) (Einstein coefficient) range.
                                        #   -1 -> do not use a loga range.
     eu             =         -1        #  Upper energy state range in Kelvin. -1
                                        #   -> do not use an eu range.
     el             =         -1        #  Lower energy state range in Kelvin. -1
                                        #   -> do not use an el range.

verbose             =       True        #  List result set to logger (and
                                        #   optionally logfile)?
     logfile        =         ''        #  List result set to this logfile (only
                                        #   used if verbose=True).
     append         =       True        #  If true, append to logfile if it
                                        #   already exists, if false overwrite
                                        #   logfile if it exists. Only used if
                                        #   verbose=True and logfile not blank.

wantreturn          =       True        #  If true, return the spectralline tool
                                        #   associated with the result set.
```

The table is provided in the *tablename* parameter but if it is blank (the default), the catalog which is included with CASA will be used. Searches can be made in a parameter space with large dimensionality:

    *freqrange*             Frequency range in GHz.    *species*                Species to search for.    *reconly*                 List only NRAO recommended frequencies.    *chemnames*         Chemical names to search for.    *qns*                      Resolved quantum numbers to search for.    *intensity*               CDMS/JPL intensity range.    *smu2*                   $S\mu^{2}$ range in Debye$^2$.    *loga*                      log(A) (Einstein coefficient) range.    *el*                          Lower energy state range in Kelvin.    *eu*                         Upper energy state range in Kelvin.    *rrlinclude*              Include RRLs in the result set?    *rrlonly*                   Include only RRLs in the result set?

Notation is as found in the Splatalogue catalog.Example:Search for all lines of the species HOCN and HOCO$^+$ in the 200-300GHz range:

```
slsearch(outfile='myresults.tbl', freqrange = [200,300],
         species=['HOCN', 'HOCO+'])
```

The task can also return a python dictionary if assigned a variable like:

```
myLines = slsearch(outfile='myresults.tbl', freqrange = [200,300],
          species=['HOCN', 'HOCO+'])
```

#  Convert Exported Splatalogue Catalogs to CASA Tables (**splattotable**)

In some cases, the internal spectral line catalog may not contain the lines in which one is interested. In that case, one can export a catalog from [Splatalogue](http://www.splatalogue.net) or even create their own \'by hand\' (be careful to get the format exactly right though!). CASA's task **splattotable** can then be used to create a CASA table that contains these lines and can be searched:

```
#  splattotable :: Convert a downloaded Splatalogue spectral line list to a casa table.
filenames           =       ['']        #  Files containing Splatalogue lists.
table               =         ''        #  Output table name.
wantreturn          =       True        #  Do you want the task to return a spectralline tool attached to the results table?
```

A search in Splatalogue will return a catalog that can be saved in a file (look for the \'Export\' section after the results on the search results page). The exported filename(s) should be entered in the *filenames* parameter of **splattotable**. The downloaded files must be in a specific format for this task to succeed. If you use the Splatalogue \'*Export CASA fields*\' feature, you should have no difficulties.

 

 

# Bibliography

1. Leahy,\ J.\~P.,\ Pooley,\ G.\~G.,\ &\ Jagers,\ W.\~J.\ 1986,\ A&A,\ 156,\ 234\ (
^

