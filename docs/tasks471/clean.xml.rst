clean -- Invert and deconvolve images with selected algorithm -- imaging task
=======================================

Description
---------------------------------------
Form images from visibilities. Handles continuum and spectral line cubes.


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
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
     - :code:`True`
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
   * - observation
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - mode
     - :code:`'mfs'`
     - 
   * - resmooth
     - :code:`False`
     - 
   * - gridmode
     - :code:`''`
     - 
   * - wprojplanes
     - :code:`int(-1)`
     - 
   * - facets
     - :code:`int(1)`
     - 
   * - cfcache
     - :code:`'cfcache.dir'`
     - 
   * - rotpainc
     - :code:`float(5.0)`
     - 
   * - painc
     - :code:`float(360.0)`
     - 
   * - aterm
     - :code:`True`
     - 
   * - psterm
     - :code:`False`
     - 
   * - mterm
     - :code:`True`
     - 
   * - wbawp
     - :code:`False`
     - 
   * - conjbeams
     - :code:`True`
     - 
   * - epjtable
     - :code:`''`
     - 
   * - interpolation
     - :code:`'linear'`
     - 
   * - niter
     - :code:`int(500)`
     - 
   * - gain
     - :code:`float(0.1)`
     - 
   * - threshold
     - :code:`{'value': float(0.0), 'unit': 'mJy'}`
     - 
   * - psfmode
     - :code:`'clark'`
     - 
   * - imagermode
     - :code:`'csclean'`
     - 
   * - ftmachine
     - :code:`'mosaic'`
     - 
   * - mosweight
     - :code:`False`
     - 
   * - scaletype
     - :code:`'SAULT'`
     - 
   * - multiscale
     - :code:`numpy.array( [ int(0) ] )`
     - 
   * - negcomponent
     - :code:`int(-1)`
     - 
   * - smallscalebias
     - :code:`float(0.6)`
     - 
   * - interactive
     - :code:`False`
     - 
   * - mask
     - :code:`numpy.array( [  ] )`
     - 
   * - nchan
     - :code:`int(-1)`
     - 
   * - start
     - :code:`int(0)`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - outframe
     - :code:`''`
     - 
   * - veltype
     - :code:`'radio'`
     - 
   * - imsize
     - :code:`numpy.array( [ int(256),int(256) ] )`
     - 
   * - cell
     - :code:`{'value': float(1.0), 'unit': 'arcsec'}`
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
   * - uvtaper
     - :code:`False`
     - 
   * - outertaper
     - :code:`numpy.array( [ '' ] )`
     - 
   * - innertaper
     - :code:`numpy.array( [  ] )`
     - 
   * - modelimage
     - :code:`''`
     - 
   * - restoringbeam
     - :code:`numpy.array( [  ] )`
     - 
   * - pbcor
     - :code:`False`
     - 
   * - minpb
     - :code:`float(0.2)`
     - 
   * - usescratch
     - :code:`False`
     - 
   * - noise
     - :code:`'1.0Jy'`
     - 
   * - npixels
     - :code:`int(0)`
     - 
   * - npercycle
     - :code:`int(100)`
     - 
   * - cyclefactor
     - :code:`float(1.5)`
     - 
   * - cyclespeedup
     - :code:`int(-1)`
     - 
   * - nterms
     - :code:`int(1)`
     - 
   * - reffreq
     - :code:`''`
     - 
   * - chaniter
     - :code:`False`
     - 
   * - flatnoise
     - :code:`True`
     - 
   * - allowchunk
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


imagename
---------------------------------------

:code:`''`

Pre-name of output images


outlierfile
---------------------------------------

:code:`''`

Text file with image names, sizes, centers for outliers


field
---------------------------------------

:code:`''`

Field Name or id


spw
---------------------------------------

:code:`''`

Spectral windows e.g. \'0~3\', \'\' is all


selectdata
---------------------------------------

:code:`True`

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

Scan number range


observation
---------------------------------------

:code:`''`

Observation ID range


intent
---------------------------------------

:code:`''`

Scan Intent(s)


mode
---------------------------------------

:code:`'mfs'`

Spectral gridding type (mfs, channel, velocity, frequency)


resmooth
---------------------------------------

:code:`False`

Re-restore the cube image to a common beam when True


gridmode
---------------------------------------

:code:`''`

Gridding kernel for FFT-based transforms, default=\'\' None


wprojplanes
---------------------------------------

:code:`int(-1)`

Number of w-projection planes for convolution; -1 => automatic determination 


facets
---------------------------------------

:code:`int(1)`

Number of facets along each axis (main image only)


cfcache
---------------------------------------

:code:`'cfcache.dir'`

Convolution function cache directory


rotpainc
---------------------------------------

:code:`float(5.0)`

Parallactic angle increment (degrees) for OTF A-term rotation


painc
---------------------------------------

:code:`float(360.0)`

Parallactic angle increment (degrees) for computing A-term


aterm
---------------------------------------

:code:`True`

Switch-on the A-Term?


psterm
---------------------------------------

:code:`False`

Switch-on the PS-Term?


mterm
---------------------------------------

:code:`True`

Switch-on the M-Term?


wbawp
---------------------------------------

:code:`False`

Trigger the wide-band A-Projection algorithm?


conjbeams
---------------------------------------

:code:`True`

Use frequency conjugate beams in WB A-Projection algorithm?


epjtable
---------------------------------------

:code:`''`

Table of EP-Jones parameters


interpolation
---------------------------------------

:code:`'linear'`

Spectral interpolation (nearest, linear, cubic). 


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

:code:`{'value': float(0.0), 'unit': 'mJy'}`

Flux level to stop cleaning, must include units: \'1.0mJy\'


psfmode
---------------------------------------

:code:`'clark'`

Method of PSF calculation to use during minor cycles


imagermode
---------------------------------------

:code:`'csclean'`

Options: \'csclean\' or \'mosaic\', \'\', uses psfmode


ftmachine
---------------------------------------

:code:`'mosaic'`

Gridding method for the image


mosweight
---------------------------------------

:code:`False`

Individually weight the fields of the mosaic


scaletype
---------------------------------------

:code:`'SAULT'`

Controls scaling of pixels in the image plane. default=\'SAULT\'; example: scaletype=\'PBCOR\' Options: \'PBCOR\',\'SAULT\'


multiscale
---------------------------------------

:code:`numpy.array( [ int(0) ] )`

Deconvolution scales (pixels); [] = standard clean


negcomponent
---------------------------------------

:code:`int(-1)`

Stop cleaning if the largest scale finds this number of neg components


smallscalebias
---------------------------------------

:code:`float(0.6)`

a bias to give more weight toward smaller scales


interactive
---------------------------------------

:code:`False`

Use interactive clean (with GUI viewer)


mask
---------------------------------------

:code:`numpy.array( [  ] )`

Cleanbox(es), mask image(s), region(s), or a level


nchan
---------------------------------------

:code:`int(-1)`

Number of channels (planes) in output image; -1 = all


start
---------------------------------------

:code:`int(0)`

start of output spectral dimension


width
---------------------------------------

:code:`int(1)`

width of output spectral channels


outframe
---------------------------------------

:code:`''`

default spectral frame of output image 


veltype
---------------------------------------

:code:`'radio'`

velocity definition (radio, optical, true) 


imsize
---------------------------------------

:code:`numpy.array( [ int(256),int(256) ] )`

x and y image size in pixels.  Single value: same for both


cell
---------------------------------------

:code:`{'value': float(1.0), 'unit': 'arcsec'}`

x and y cell size(s). Default unit arcsec.


phasecenter
---------------------------------------

:code:`''`

Image center: direction or field index


restfreq
---------------------------------------

:code:`''`

Rest frequency to assign to image (see help)


stokes
---------------------------------------

:code:`'I'`

Stokes params to image (eg I,IV,IQ,IQUV)


weighting
---------------------------------------

:code:`'natural'`

Weighting of uv (natural, uniform, briggs, ...)


robust
---------------------------------------

:code:`float(0.0)`

Briggs robustness parameter


uvtaper
---------------------------------------

:code:`False`

Apply additional uv tapering of visibilities


outertaper
---------------------------------------

:code:`numpy.array( [ '' ] )`

uv-taper on outer baselines in uv-plane


innertaper
---------------------------------------

:code:`numpy.array( [  ] )`

uv-taper in center of uv-plane (not implemented)


modelimage
---------------------------------------

:code:`''`

Name of model image(s) to initialize cleaning


restoringbeam
---------------------------------------

:code:`numpy.array( [  ] )`

Output Gaussian restoring beam for CLEAN image


pbcor
---------------------------------------

:code:`False`

Output primary beam-corrected image


minpb
---------------------------------------

:code:`float(0.2)`

Minimum PB level to use


usescratch
---------------------------------------

:code:`False`

True if to save model visibilities in MODEL_DATA column


noise
---------------------------------------

:code:`'1.0Jy'`

noise parameter for briggs abs mode weighting


npixels
---------------------------------------

:code:`int(0)`

number of pixels for superuniform or briggs weighting


npercycle
---------------------------------------

:code:`int(100)`

Clean iterations before interactive prompt (can be changed)


cyclefactor
---------------------------------------

:code:`float(1.5)`

Controls how often major cycles are done. (e.g. 5 for frequently)


cyclespeedup
---------------------------------------

:code:`int(-1)`

Cycle threshold doubles in this number of iterations


nterms
---------------------------------------

:code:`int(1)`

Number of Taylor coefficients to model the sky frequency dependence 


reffreq
---------------------------------------

:code:`''`

Reference frequency (nterms > 1),\'\' uses central data-frequency


chaniter
---------------------------------------

:code:`False`

Clean each channel to completion (True), or all channels each cycle (False)


flatnoise
---------------------------------------

:code:`True`

Controls whether searching for clean components is done in a constant noise residual image (True) or in an optimal signal-to-noise residual image (False) 


allowchunk
---------------------------------------

:code:`False`

Divide large image cubes into channel chunks for deconvolution 




