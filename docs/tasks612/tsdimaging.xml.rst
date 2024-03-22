tsdimaging -- SD task: imaging for total power and spectral data -- single dish task
=======================================

Description
---------------------------------------

Task sdimaging creates an image from input single-dish data sets.
The input can be either total power and spectral data. 

The coordinate of output image is defined by four axes, i.e., two
spatial axes, frequency and polarization axes.\n
By default, spatial coordinate of image is defined so that the all
pointing directions in POINTING tables of input data sets are covered
with the cell size, 1/3 of FWHM of primary beam of antennas in the
first MS. Therefore, it is often easiest to leave spatial definitions
at the default values. It is also possible to define spatial axes of
the image by specifying the image center direction (phasecenter),
number of image pixel (imsize) and size of the pixel (cell).\n
The frequency coordinate of image is defined by three parameters,
the number of channels (nchan), the channel id/frequency/velocity of
the first channel (start), and channel width (width).There are three
modes available to define unit of start and width, i.e., 'channel' (use
channel indices), 'frequency' (use frequency unit, e.g., 'GHz'),
and 'velocity' (use velocity unit, e.g., 'km/s'). By default, nchan,
start, and width are defined so that all selected spectral windows are
covered with the channel width equal to separation of first two
channels selected.\n
Finally, polarizations of image is defined by stokes parameter or
polarization. For example, stokes='XXYY' produces an image cube with
each plane contains the image of one of the polarizations, while
stokes='I' produces a 'total intensity' or Stokes I image.
The stokes parameter has a special option, 'pseudoI'. The option is 
introduced to support imaging of partially flagged correlations. 
Main difference between 'I' and 'pseudoI' is that the former only takes 
into account the data whose correlations are all valid (this is the 
Stokes I in the strict sense) while the latter accumulates partially 
flagged data in addition. Note that the 'pseudoI' option is compatible 
with 'I' for sdimaging task. 

The task also supports various grid function (convolution kernel) to
weight spectra as well as an option to remove the most extreme minimum 
and maximum (unweighted) values prior to computing the gridded pixel 
values. See description below for details of gridfunction available.

  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infiles
     - :code:`numpy.array( [  ] )`
     - a list of names of input SD Measurementsets (only MS is allowed for this task)
   * - outfile
     - :code:`''`
     - prefix of output images (.image, .weight, .sumwt, .psf)
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - field
     - :code:`''`
     - select data by field IDs and names, e.g. \'3C2*\' (\'\'=all)
   * - spw
     - :code:`''`
     - select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)
   * - antenna
     - :code:`''`
     - select data by antenna names or IDs, e.g, \'PM03\' (\'\' = all antennas)
   * - scan
     - :code:`''`
     - select data by scan numbers, e.g. \'21~23\' (\'\'=all)
   * - intent
     - :code:`'OBSERVE_TARGET#ON_SOURCE'`
     - select data by observational intent, e.g. \'*ON_SOURCE*\' (\'\'=all)
   * - mode
     - :code:`'channel'`
     - spectral gridding type [\'channel\', \'frequency\', \'velocity\']
   * - nchan
     - :code:`int(-1)`
     - number of channels (planes) in output image (-1=all)
   * - start
     - :code:`int(0)`
     - start of output spectral dimension, e.g. \'0\', \'110GHz\', \'-20km/s\'
   * - width
     - :code:`int(1)`
     - width of output spectral channels
   * - veltype
     - :code:`'radio'`
     - velocity definition [\'radio\', \'optical\', \'true\' or \'relativistic\']
   * - specmode
     - :code:`'cube'`
     - Spectral definition mode (cube, cubedata, cubesource)
   * - outframe
     - :code:`''`
     - velocity frame of output image [\'lsrk\', \'lsrd\', \'bary\', \'geo\', \'topo\', \'galacto\', \'lgroup\', \'cmb\'] (\'\'=current frame or LSRK for multiple-MS inputs)
   * - gridfunction
     - :code:`'BOX'`
     - gridding function for imaging [\'BOX\', \'SF\', \'PB\', \'GAUSS\' or \'GJINC\'] (see description in help)
   * - convsupport
     - :code:`int(-1)`
     - convolution support for gridding
   * - truncate
     - :code:`int(-1)`
     - truncation radius for gridding
   * - gwidth
     - :code:`int(-1)`
     - HWHM for gaussian
   * - jwidth
     - :code:`int(-1)`
     - c-parameter for jinc function
   * - imsize
     - :code:`numpy.array( [  ] )`
     - x and y image size in pixels, e.g., [64,64]. Single value: same for both spatial axes ([] = number of pixels to cover whole pointings in MSes)
   * - cell
     - :code:`''`
     - x and y cell size, (e.g., [\'8arcsec\',\'8arcsec\']. default unit arcmin. ('' = 1/3 of FWHM of primary beam)
   * - phasecenter
     - :code:`''`
     - image center direction: position or field index or ephemeris source info, e.g., \'J2000 17:30:15.0 -25.30.00.0\', \'MARS\'. (\'\' = the center of pointing directions in MSes)
   * - projection
     - :code:`'SIN'`
     - map projection type
   * - pointingcolumn
     - :code:`'direction'`
     - pointing data column to use [\'direction\', \'target\', \'pointing_offset\', \'source_offset\' or \'encoder\']
   * - restfreq
     - :code:`''`
     - rest frequency to assign to image, e.g., \'114.5GHz\'
   * - stokes
     - :code:`'I'`
     - stokes parameters or polarization types to image, e.g. \'I\', \'XX\'
   * - minweight
     - :code:`float(0.1)`
     - Minimum weight ratio to use
   * - brightnessunit
     - :code:`''`
     - Overwrite the brightness unit in image (\'\' = respect the unit in MS) [\'K\' or \'Jy/beam\']
   * - clipminmax
     - :code:`False`
     - Clip minimum and maximum value from each pixel


Parameter Explanations
=======================================



infiles
---------------------------------------

:code:`numpy.array( [  ] )`

a list of names of input SD Measurementsets (only MS is allowed for this task)


outfile
---------------------------------------

:code:`''`

prefix of output images (.image, .weight, .sumwt, .psf)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists [True, False]


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\'=all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g. \'3,5,7\' (\'\'=all)


antenna
---------------------------------------

:code:`''`

select data by antenna names or IDs, e.g, \'PM03\' (\'\' = all antennas)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


intent
---------------------------------------

:code:`'OBSERVE_TARGET#ON_SOURCE'`

select data by observational intent, e.g. \'*ON_SOURCE*\' (\'\'=all)


mode
---------------------------------------

:code:`'channel'`

spectral gridding type


nchan
---------------------------------------

:code:`int(-1)`

 number of channels (planes) in output image (-1=all)


start
---------------------------------------

:code:`int(0)`

start of output spectral dimension, e.g. \'0\', \'110GHz\', \'-20km/s\'


width
---------------------------------------

:code:`int(1)`

width of output spectral channels


veltype
---------------------------------------

:code:`'radio'`

velocity definition


specmode
---------------------------------------

:code:`'cube'`

Spectral definition mode (cube, cubedata, cubesource)


outframe
---------------------------------------

:code:`''`

velocity frame of output image (''=current frame or LSRK for multiple-MS inputs)


gridfunction
---------------------------------------

:code:`'BOX'`

gridding function for imaging (see description in help)


convsupport
---------------------------------------

:code:`int(-1)`

convolution support for gridding


truncate
---------------------------------------

:code:`int(-1)`

truncation radius for gridding


gwidth
---------------------------------------

:code:`int(-1)`

HWHM for gaussian


jwidth
---------------------------------------

:code:`int(-1)`

c-parameter for jinc function


imsize
---------------------------------------

:code:`numpy.array( [  ] )`

x and y image size in pixels, e.g., [64,64]. Single value: same for both spatial axes ([] = number of pixels to cover whole pointings in MSes)


cell
---------------------------------------

:code:`''`

x and y cell size, (e.g., [\'8arcsec\',\'8arcsec\']. default unit arcmin. ('' = 1/3 of FWHM of primary beam)


phasecenter
---------------------------------------

:code:`''`

image center direction: position or field index or ephemeris source info, e.g., \'J2000 17:30:15.0 -25.30.00.0\', \'MARS\'. (\'\' = the center of pointing directions in MSes)


projection
---------------------------------------

:code:`'SIN'`

map projection type


pointingcolumn
---------------------------------------

:code:`'direction'`

pointing data column to use


restfreq
---------------------------------------

:code:`''`

rest frequency to assign to image, e.g., \'114.5GHz\'


stokes
---------------------------------------

:code:`'I'`

stokes parameters or polarization types to image, e.g. \'I\', \'XX\'


minweight
---------------------------------------

:code:`float(0.1)`

Minimum weight ratio to the median of weight used in weight correction and weight beased masking


brightnessunit
---------------------------------------

:code:`''`

Overwrite the brightness unit in image (\'\' = respect the unit in MS) [\'K\' or \'Jy/beam\']


clipminmax
---------------------------------------

:code:`False`

Clip minimum and maximum value from each pixel. Note the benefit of clipping is lost when the number of integrations contributing to each gridded pixel is small, or where the incidence of spurious datapoints is approximately or greater than the number of beams (in area) encompassed by expected image.




