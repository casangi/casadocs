sdimaging -- SD task: imaging for total power and spectral data -- single dish task
=======================================

Description
---------------------------------------

Task sdimaging creates an image from input single-dish data sets.\n
The input can be either total power and spectral data. Currently,
this task directly accesses the Measurement Set data because of 
the data access efficiency. So it differs from other single-dish 
tasks that mostly operate on the ASAP scantable data format.\n

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
polarization.For example, stokes='XXYY' produces an image cube with
each plane contains the image of one of the polarizations, while
stokes='I' produces a 'total intensity' or Stokes I image.\n

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
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - intent
     - :code:`'OBSERVE_TARGET#ON_SOURCE'`
     - 
   * - mode
     - :code:`'channel'`
     - spectral gridding type [\'channel\', \'frequency\', \'velocity\']
   * - nchan
     - :code:`int(-1)`
     - 
   * - start
     - :code:`int(0)`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - veltype
     - :code:`'radio'`
     - velocity definition [\'radio\', \'optical\', \'true\' or \'relativistic\']
   * - outframe
     - :code:`''`
     - velocity frame of output image [\'lsrk\', \'lsrd\', \'bary\', \'geo\', \'topo\', \'galacto\', \'lgroup\', \'cmb\'] (\'\'=current frame or LSRK for multiple-MS inputs)
   * - gridfunction
     - :code:`'BOX'`
     - gridding function for imaging [\'BOX\', \'SF\', \'PB\', \'GAUSS\' or \'GJINC\'] (see description in help)
   * - convsupport
     - :code:`int(-1)`
     - 
   * - truncate
     - :code:`int(-1)`
     - 
   * - gwidth
     - :code:`int(-1)`
     - 
   * - jwidth
     - :code:`int(-1)`
     - 
   * - imsize
     - :code:`*UNKNOWN*`
     - 
   * - cell
     - :code:`''`
     - 
   * - phasecenter
     - :code:`''`
     - 
   * - ephemsrcname
     - :code:`''`
     - 
   * - pointingcolumn
     - :code:`'direction'`
     - pointing data column to use [\'direction\', \'target\', \'pointing_offset\', \'source_offset\' or \'encoder\']
   * - restfreq
     - :code:`''`
     - 
   * - stokes
     - :code:`''`
     - 
   * - minweight
     - :code:`float(0.1)`
     - Minimum weight ratio to use
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

name of output image


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

:code:`*UNKNOWN*`

x and y image size in pixels, e.g., [64,64]. Single value: same for both spatial axes ([] = number of pixels to cover whole pointings in MSes)


cell
---------------------------------------

:code:`''`

x and y cell size, (e.g., [\'8arcsec\',\'8arcsec\']. default unit arcmin. ('' = 1/3 of FWHM of primary beam)


phasecenter
---------------------------------------

:code:`''`

image center direction: position or field index, e.g., \'J2000 17:30:15.0 -25.30.00.0\'. ('' = the center of pointing directions in MSes)


ephemsrcname
---------------------------------------

:code:`''`

ephemeris source name, e.g. \'MARS\'


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

:code:`''`

stokes parameters or polarization types to image, e.g. \'I\', \'XX\'


minweight
---------------------------------------

:code:`float(0.1)`

Minimum weight ratio to the median of weight used in weight correction and weight beased masking


clipminmax
---------------------------------------

:code:`False`

Clip minimum and maximum value from each pixel. Note the benefit of clipping is lost when the number of integrations contributing to each gridded pixel is small, or where the incidence of spurious datapoints is approximately or greater than the number of beams (in area) encompassed by expected image.




