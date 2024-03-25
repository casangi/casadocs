mosaic -- Create a multi-field deconvolved image with selected algorithm -- imaging task
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
   * - mode
     - :code:`'mfs'`
     - 
   * - alg
     - :code:`'clark'`
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
   * - stokes
     - :code:`'I'`
     - 
   * - niter
     - :code:`int(500)`
     - 
   * - gain
     - :code:`float(0.1)`
     - 
   * - threshold
     - :code:`float(0.0)`
     - 
   * - mask
     - :code:`numpy.array( [  ] )`
     - 
   * - cleanbox
     - :code:`{ }`
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
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - restfreq
     - :code:`''`
     - 
   * - sdimage
     - :code:`''`
     - 
   * - modelimage
     - :code:`''`
     - 
   * - weighting
     - :code:`'natural'`
     - 
   * - mosweight
     - :code:`False`
     - 
   * - rmode
     - :code:`'norm'`
     - 
   * - robust
     - :code:`float(0.0)`
     - 
   * - ftmachine
     - :code:`'mosaic'`
     - 
   * - cyclefactor
     - :code:`float(1.5)`
     - 
   * - cyclespeedup
     - :code:`int(-1)`
     - 
   * - scaletype
     - :code:`'SAULT'`
     - 
   * - minpb
     - :code:`float(0.1)`
     - 
   * - sigma
     - :code:`{'value': float(0.001), 'unit': 'Jy'}`
     - 
   * - targetflux
     - :code:`{'value': float(1.0), 'unit': 'Jy'}`
     - 
   * - constrainflux
     - :code:`False`
     - 
   * - prior
     - :code:`numpy.array( [  ] )`
     - 
   * - negcomponent
     - :code:`int(2)`
     - 
   * - scales
     - :code:`numpy.array( [ int(0),int(3),int(10) ] )`
     - 
   * - npercycle
     - :code:`int(100)`
     - 
   * - npixels
     - :code:`int(0)`
     - 
   * - noise
     - :code:`{'value': float(0.0), 'unit': 'Jy'}`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

name of input visibility file


imagename
---------------------------------------

:code:`''`

Pre-name of output images


mode
---------------------------------------

:code:`'mfs'`

Type of selection (mfs, channel, velocity, frequency)


alg
---------------------------------------

:code:`'clark'`

Algorithm to use (clark, hogbom, multiscale) 


imsize
---------------------------------------

:code:`numpy.array( [ int(256),int(256) ] )`

Image size in pixels (nx,ny), symmetric for single value


cell
---------------------------------------

:code:`{'value': float(1.01.0), 'unit': 'arcsec'}`

The image cell size in arcseconds [x,y]. 


phasecenter
---------------------------------------

:code:`''`

Field Identififier or direction of the image phase center


stokes
---------------------------------------

:code:`'I'`

Stokes params to image (I,IV,QU,IQUV,RR,LL,XX,YY,RRLL,XXYY)


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

:code:`float(0.0)`

Flux level to stop cleaning (unit mJy assumed)


mask
---------------------------------------

:code:`numpy.array( [  ] )`

Set of mask images used in cleaning


cleanbox
---------------------------------------

:code:`{ }`

clean box regions or file name or \'interactive\'


nchan
---------------------------------------

:code:`int(1)`

Number of channels in output image


start
---------------------------------------

:code:`int(0)`

Start channel


width
---------------------------------------

:code:`int(1)`

Channel width (value > 1 indicates channel averaging)


field
---------------------------------------

:code:`''`

Field Name


spw
---------------------------------------

:code:`''`

Spectral windows:channels: \'\' is all 


timerange
---------------------------------------

:code:`''`

Range of time to select from data


restfreq
---------------------------------------

:code:`''`

rest frequency to use in image


sdimage
---------------------------------------

:code:`''`

Input single dish image to use for model


modelimage
---------------------------------------

:code:`''`

Name of output(/input) model image


weighting
---------------------------------------

:code:`'natural'`

Weighting to apply to visibilities


mosweight
---------------------------------------

:code:`False`

Individually weight the fields of the mosaic


rmode
---------------------------------------

:code:`'norm'`

Robustness mode (for Briggs weightting)


robust
---------------------------------------

:code:`float(0.0)`

Briggs robustness parameter


ftmachine
---------------------------------------

:code:`'mosaic'`

Gridding method for the image


cyclefactor
---------------------------------------

:code:`float(1.5)`

Threshold for minor/major cycles (see pdoc)


cyclespeedup
---------------------------------------

:code:`int(-1)`

Cycle threshold doubles in this number of iterations


scaletype
---------------------------------------

:code:`'SAULT'`

Controls scaling of pixels in the image plane


minpb
---------------------------------------

:code:`float(0.1)`

Minimum PB level to use


sigma
---------------------------------------

:code:`{'value': float(0.001), 'unit': 'Jy'}`

Target image sigma


targetflux
---------------------------------------

:code:`{'value': float(1.0), 'unit': 'Jy'}`

Target flux for final image


constrainflux
---------------------------------------

:code:`False`

Constrain image to match target flux 


prior
---------------------------------------

:code:`numpy.array( [  ] )`

Name of MEM prior images


negcomponent
---------------------------------------

:code:`int(2)`

Stop the component search when the largest scale has found this number of negative components


scales
---------------------------------------

:code:`numpy.array( [ int(0),int(3),int(10) ] )`

resolutions in pixel units


npercycle
---------------------------------------

:code:`int(100)`

Number of iterations before interactive masking prompt


npixels
---------------------------------------

:code:`int(0)`

number of pixels to determine cell size for superuniform or briggs weighting


noise
---------------------------------------

:code:`{'value': float(0.0), 'unit': 'Jy'}`

noise parameter for briggs weighting when rmode=\'abs\'




