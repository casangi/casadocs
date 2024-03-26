csvclean -- This task does an invert of the visibilities and deconvolve in the image plane. -- utilities, imaging task
=======================================

Description
---------------------------------------
This task does an invert of the visibilities and deconvolve in the
			image plane. It does not do a uvdata subtraction (aka Cotton-Schwab
			major cycle) of model visibility as in clean. - For ALMA Commissioning
	


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
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - advise
     - :code:`False`
     - 
   * - mode
     - :code:`'continuum'`
     - 
   * - nchan
     - :code:`int(-1)`
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
   * - niter
     - :code:`int(500)`
     - 
   * - weighting
     - :code:`'natural'`
     - 
   * - restoringbeam
     - :code:`numpy.array( [  ] )`
     - 
   * - interactive
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

Name of image


field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


advise
---------------------------------------

:code:`False`

Boolean to determine if advice on image cell is requested


mode
---------------------------------------

:code:`'continuum'`

 define the mode to operate csvclean: option continuum, cube 


nchan
---------------------------------------

:code:`int(-1)`

Number of channels (planes) in output image; -1 = all


width
---------------------------------------

:code:`int(1)`

width of output spectral channels


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

Image center: direction or field index


niter
---------------------------------------

:code:`int(500)`

Maximum number of iterations


weighting
---------------------------------------

:code:`'natural'`

Type of weighting


restoringbeam
---------------------------------------

:code:`numpy.array( [  ] )`

Output Gaussian restoring beam for CLEAN image


interactive
---------------------------------------

:code:`False`

Create a mask interactively or not.




