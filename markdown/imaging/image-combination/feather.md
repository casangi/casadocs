

# Feather & CASAfeather 

Combining single dish and interferometric images

Feathering is a technique used to combine a Single Dish (SD) image with an interferometric image of the same field.The goal of this process is to reconstruct the source emission on all spatial scales, ranging from the small spatial scales measured by the interferometer to the large-scale structure measured by the single dish.  To do this, feather combines the images in Fourier space, weighting them by the spatial frequency response of each image. This technique assumes that the spatial frequencies of the single dish and interferometric data partially overlap. The subject of interferometric and single dish data combination has a long history. See the introduction of Koda et al 2011 (and references therein) [\[1\]](#Bibliography) for a concise review, and Vogel et al 1984 [\[2\]](#Bibliography), Stanimirovic et al 1999 [\[3\]](#Bibliography), Stanimirovic 2002 [\[4\]](#Bibliography), Helfer et al 2003 [\[5\]](#Bibliography), and Weiss et al 2001 [\[6\]](#Bibliography), among other referenced papers, for other methods and discussions concerning the combination of single dish and interferometric data.The feathering algorithm implemented in CASA is as follows: 

1.  Regrid the single dish image to match the coordinate system, image shape, and pixel size of the high resolution image.    
2.  Transform each image onto uniformly gridded spatial-frequency axes.
3.  Scale the Fourier-transformed low-resolution image by the ratio of the volumes of the two \'clean beams\' (high-res/low-res) to convert the single dish intensity (in Jy/beam) to that corresponding to the high resolution intensity (in Jy/beam). The volume of the beam is calculated as the volume under a two dimensional Gaussian with peak 1 and major and minor axes of the beam corresponding to the major and minor axes of the Gaussian.    
4.  Add the Fourier-transformed data from the  high-resolution image, scaled by []$(1-wt)$ where $wt$ is the Fourier transform of the \'clean beam\' defined in the low-resolution image, to the scaled low resolution image from step 3.5.  Transform back to the image plane.

The input images for feather must have the following characteristics:

1.   Both input images must have a well-defined beam shape for this task to work, which will be a \'clean beam\' for interferometric images and a \'primary-beam\'  for a single-dish image. The beam for each image should be specified in the image header. If a beam is not defined in the header or feather cannot guess the beam based on the telescope parameter in the header, then you will need to add the beam size to the header using **imhead**.    
2.  Both input images must have the same flux density normalization scale. If necessary, the SD image should be converted from temperature units to Jy/beam. Since measuring absolute flux levels is difficult with single dishes, the single dish data is likely to be the one with the most uncertain flux calibration. The SD image flux can be scaled using the parameter *sdfactor* to place it on the same scale as the interferometer data. The casafeather task (see below) can be used to investigate the relative flux scales of the images.*    *

Feather attemps to regrid the single dish image to the interferometric image. Given that the single dish image frequently originates from other data reduction packages, CASA may have trouble performing the necessary regridding steps. If that happens, one may try to regrid the single dish image manually to the interferometric image. CASA has a few tasks to perform individual steps, including **imregrid** for coordinate transformations, **imtrans** to swap and reverse coordinate axes, the tool **ia.adddegaxes()** for adding degenerate axes (e.g. a single Stokes axis). See the \"Image Analysis](https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis)\" chapter for additional options. If you have trouble changing image projections, you can try [the [montage package](http://montage.ipac.caltech.edu/), which also has an [associated python wrapper](http://www.astropy.org/montage-wrapper/).

If you are feathering large images together, set the numbers of pixels along the X and Y axes to composite (non-prime) numbers in order to improve the algorithm speed. In general, FFTs work much faster on even and composite numbers. Then use the subimage task or tool to trim the number of pixels to something desirable.

The inputs for **feather** are: 

```
#feather :: Combine two images using their Fourier transforms
imagename       = ''     # Name of output feathered image
highres         = ''     # Name of high resolution (interferometer) image
lowres          = ''     # Name of low resolution (single dish) image
sdfactor        = 1.0    # Scale factor to apply to Single Dish image
effdishdiam     = -1.0   # New effective SingleDish diameter to use in m
lowpassfiltersd = False  # Filter out the high spatial frequencies of the SD image
```

The SD data cube is specified by the *lowres* parameter and the interferometric data cube by the *highres* parameter. The combined, feathered output cube name is given by the *imagename* parameter. The parameter *sdfactor* can be used to scale the flux calibration of the SD cube. The parameter *effdishdiam* can be used to change the weighting of the single dish image.

The weighting functions for the data are usually the Fourier transform of the Single Dish beam FFT(PB~SD]~) for the Single dish data, and the inverse, 1-FFT(PB~[SD~), for the interferometric data. It is possible, however, to change the weighting functions by pretending that the SD is smaller in size via the *effdishdiam* parameter. This tapers the high spatial frequencies of the SD data and adds more weight to the interferometric data. The *lowpassfiltersd* can take out non-physical artifacts at very high spatial frequencies that are often present in SD data.

Note that the only inputs are for images; **feather** will attempt to regrid the images to a common shape, i.e. pixel size, pixel numbers, and spectral channels. If you are having issues with the regridding inside feather, you may consider regridding using the **imregrid** and **specsmooth** tasks.

The **feather** task does not perform any deconvolution but combines the single dish image with a presumably deconvolved interferometric image. The short spacings of the interferometric image that are extrapolated by the deconvolution process will be those that are down-weighted the most when combined with the single dish data. The single dish image must have a well-defined beam shape and the correct flux units for a model image (Jy/beam instead of Jy/pixel). Use the tasks **imhead** and **immath** first to convert if needed.

Starting with a cleaned synthesis image and a low resolution image from a single dish telescope, the following example shows how they can be feathered: 

```
feather(imagename ='feather.im',       # Create an image called feather.im
        highres   ='synth.im',         # The synthesis image is called synth.im
        lowres    ='single_dish.im')   # The SD image is called single_dish.im
```

### Visual Interface for feather (casafeather) {#sec366 .subsection}

CASA also provides a visual interface to the **feather** task. The interface is run from a command line *outside* CASA by typing casafeather in a shell. An example of the interface is shown below. To start, one needs to specify a high and a low resolution image, typically an interferometric and a single dish map. Note that the single dish map needs to be in units of Jy/beam. The output image name can be specified. The non-deconvolved (dirty) interferometric image can also be specified to use as diagnostic of the relative flux scaling of the single dish and interferometer images. See below for more details. At the top of the display, the parameters *effdshdiameter* and *sdfactor* can be provided in the "Effective Dish Diameter" and "Low Resolution Scale Factor" input boxes. One you have specified the images and parameters, press the "Feather" button in the center of the GUI window to start the feathering process. The feathering process here includes regridding the low resolution image to the high resolution image.

![c0ff299b0bd9c0afa9b65a93c6b02212362645d3](media/c0ff299b0bd9c0afa9b65a93c6b02212362645d3.png)

[]

>Figure 1: ][ The panel shows the "Original Data Slice", which are cuts through the u and v directions of the Fourier-transformed input images. Green is the single dish data (low resolution) and purple the interferometric data (high resolution). To bring them on the same flux scale, the low data were convolved to the high resolution beam and vice versa (selectable in color preferences). In addition, a single dish scaling of 1.2 was applied to adjust calibration differences. The weight functions are shown in yellow (for the low resolution data) and orange (for the high resolution data). The weighting functions were also applied to the green and purple slices. Image slices of the combined, feathered output image are shown in blue. The displays also show the location of the effective dish diameter by the vertical line. This value is kept at the original single dish diameter that is taken from the respective image header.
  

 

------------------------------------------------------------------------

The initial casafeather display shows two rows of plots. The panel shows the "Original Data Slice", which are either cuts through the u and v directions of the Fourier-transformed input images or a radial average. A vertical line shows the location of the effective dish diameter(s). The blue lines are the combined, feathered slices.

 

 ![c57e182275861b522d1e6836eab16a853d7aae7c](media/c57e182275861b522d1e6836eab16a853d7aae7c.png)[

>Figure 3:  The scatter plot in casafeather. The low data, convolved with high beam, weighted and scaled is still somewhat below the equality line (plotted against high data, convolved with low beam, weighted). In this case one can try to adjust the \"low resolution scale factor\" to bring the values closer to the line of equality, ie. to adjust the calibration scales. 
  

Plotting the data as a scatter plot is a useful diagnostic tool for checking for differences in flux scaling between the high and low resolution data sets.The dirty interferometer image contains the actual flux measurements made by the telescope. Therefore, if the single dish scaling is correct, the flux in the dirty image convolved with the low resolution beam and with the appropriate weighting applied should be the same as the flux of the low-resolution data convolved with the high resolution beam once weighted and scaled. If not, the *sdfactor* parameter can be adjusted until they are the same. One may also use the cleaned high resolution image instead of the dirty image, if the latter is not available. However, note that the cleaned high resolution image already contains extrapolations to larger spatial scales that may bias the comparison.

 

 

 

 

# Bibliography

1. Koda\ et\ al\ 2011\ (
2. Vogel\ et\ al\ 1984\ (
3. Stanimirovic\ et\ al\ 1999\ (
4. Stanimirovic\ et\ al\ 2002\ (
5. Helfer\ et\ al\ 2003\ (
6. Weiss\ et\ al\ 2001\ (
^

