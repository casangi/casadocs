widefield -- Wide-field imaging and deconvolution with selected algorithm -- imaging task
=======================================

Description
---------------------------------------

This is the main wide-field imaging/deconvolution task.  It
uses the wprojection method for a large field of view, can
make many facets, and can include outlier fields.  Several
deconvolution algorithms are supported.  Interactive cleaning
is also supported
  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`numpy.array( [  ] )`
     - 
   * - imagename
     - :code:`''`
     - 
   * - outlierfile
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - selectdata
     - :code:`False`
     - 
   * - timerange
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - mode
     - :code:`'mfs'`
     - 
   * - niter
     - :code:`int(500)`
     - 
   * - gain
     - :code:`float(0.1)`
     - 
   * - threshold
     - :code:`'0.0Jy'`
     - 
   * - psfmode
     - :code:`'clark'`
     - 
   * - ftmachine
     - :code:`''`
     - 
   * - facets
     - :code:`int(3)`
     - 
   * - wprojplanes
     - :code:`int(64)`
     - 
   * - multiscale
     - :code:`numpy.array( [ int() ] )`
     - 
   * - negcomponent
     - :code:`int(0)`
     - 
   * - interactive
     - :code:`False`
     - 
   * - mask
     - :code:`numpy.array( [  ] )`
     - 
   * - nchan
     - :code:`int(1)`
     - 
   * - start
     - :code:`int(0)`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - imsize
     - :code:`numpy.array( [ int(256),int(256) ] )`
     - 
   * - cell
     - :code:`{'value': float(1.01.0), 'unit': 'arcsec'}`
     - 
   * - phasecenter
     - :code:`''`
     - 
   * - restfreq
     - :code:`''`
     - 
   * - stokes
     - :code:`'I'`
     - 
   * - weighting
     - :code:`'natural'`
     - 
   * - robust
     - :code:`float(0.0)`
     - 
   * - npixels
     - :code:`int(0)`
     - 
   * - noise
     - :code:`'1.0Jy'`
     - 
   * - cyclefactor
     - :code:`float(1.5)`
     - 
   * - cyclespeedup
     - :code:`int(-1)`
     - 
   * - npercycle
     - :code:`int(100)`
     - 
   * - uvtaper
     - :code:`False`
     - 
   * - outertaper
     - :code:`numpy.array( [ '' ] )`
     - 
   * - innertaper
     - :code:`numpy.array( [  ] )`
     - 
   * - restoringbeam
     - :code:`numpy.array( [  ] )`
     - 
   * - calready
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`numpy.array( [  ] )`

name of input visibility file


imagename
---------------------------------------

:code:`''`

Pre-name of output images


outlierfile
---------------------------------------

:code:`''`

Text file with image names, sizes, centers


field
---------------------------------------

:code:`''`

Field Name


spw
---------------------------------------

:code:`''`

Spectral windows:channels: \'\' is all 


selectdata
---------------------------------------

:code:`False`

Other data selection parameters


timerange
---------------------------------------

:code:`''`

Range of time to select from data


uvrange
---------------------------------------

:code:`''`

Select data within uvrange 


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


scan
---------------------------------------

:code:`''`

scan number range


mode
---------------------------------------

:code:`'mfs'`

Type of selection (mfs, channel, velocity, frequency)


niter
---------------------------------------

:code:`int(500)`

Maximum number of iterations


gain
---------------------------------------

:code:`float(0.1)`

Loop gain for cleaning


threshold
---------------------------------------

:code:`'0.0Jy'`

Flux level to stop cleaning.  Must include units


psfmode
---------------------------------------

:code:`'clark'`

Algorithm to use (clark, hogbom) 


ftmachine
---------------------------------------

:code:`''`

Gridding method for the image (wproject, ft)


facets
---------------------------------------

:code:`int(3)`

Number of facets along each axis in main image only


wprojplanes
---------------------------------------

:code:`int(64)`

Number of planes to use in wprojection convolutiuon function


multiscale
---------------------------------------

:code:`numpy.array( [ int() ] )`

set deconvolution scales (pixels), default: multiscale=[]


negcomponent
---------------------------------------

:code:`int(0)`

Stop cleaning if the largest scale finds this number of neg components


interactive
---------------------------------------

:code:`False`

use interactive clean (with GUI viewer)


mask
---------------------------------------

:code:`numpy.array( [  ] )`

cleanbox(es), mask image(s), and/or region(s) 


nchan
---------------------------------------

:code:`int(1)`

Number of channels (planes) in output image


start
---------------------------------------

:code:`int(0)`

First channel in input to use


width
---------------------------------------

:code:`int(1)`

Number of input channels to average


imsize
---------------------------------------

:code:`numpy.array( [ int(256),int(256) ] )`

Image size in pixels (nx,ny), single value okay


cell
---------------------------------------

:code:`{'value': float(1.01.0), 'unit': 'arcsec'}`

The image cell size in arcseconds [x,y], single value okay. 


phasecenter
---------------------------------------

:code:`''`

Field Identififier or direction of the image phase center


restfreq
---------------------------------------

:code:`''`

rest frequency to assign to image (see help)


stokes
---------------------------------------

:code:`'I'`

Stokes params to image (I,IV,QU,IQUV,RR,LL,XX,YY,RRLL,XXYY)


weighting
---------------------------------------

:code:`'natural'`

Weighting to apply to visibilities


robust
---------------------------------------

:code:`float(0.0)`

Briggs robustness parameter


npixels
---------------------------------------

:code:`int(0)`

number of pixels to determine cell size for superuniform or briggs weighting


noise
---------------------------------------

:code:`'1.0Jy'`

noise parameter for briggs abs mode weighting


cyclefactor
---------------------------------------

:code:`float(1.5)`

Threshold for minor/major cycles (see pdoc)


cyclespeedup
---------------------------------------

:code:`int(-1)`

Cycle threshold doubles in this number of iterations


npercycle
---------------------------------------

:code:`int(100)`

Number of iterations before interactive masking prompt


uvtaper
---------------------------------------

:code:`False`

Apply additional uv tapering of  visibilities.


outertaper
---------------------------------------

:code:`numpy.array( [ '' ] )`

uv-taper on outer baselines in uv-plane


innertaper
---------------------------------------

:code:`numpy.array( [  ] )`

uv-taper in center of uv-plane


restoringbeam
---------------------------------------

:code:`numpy.array( [  ] )`

Output Gaussian restoring beam for CLEAN image


calready
---------------------------------------

:code:`False`

Create scratch columns and store model visibilities so that selfcal can be run after clean




