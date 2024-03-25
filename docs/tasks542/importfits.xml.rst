importfits -- Convert an image FITS file into a CASA image -- import/export task
=======================================

Description
---------------------------------------

        Convert an image FITS file into a CASA image

	Keyword arguments:
	fitsimage -- Name of input image FITS file
		default: none; example='3C273XC1.fits'
	imagename -- Name of output CASA image
		default: none; example: imagename='3C273XC1.image'
	whichrep -- If fits image has multiple coordinate reps, choose one.
		default: 0 means first; example: whichrep=1
	whichhdu -- If fits file contains multiple images, choose this one (0 == first)
		default=-1 use the first valid one; example: whichhdu=1
	zeroblanks -- Set blanked pixels to zero (not NaN)
		default=True; example: zeroblanks=True
	overwrite -- Overwrite pre-existing imagename
		default=False; example: overwrite=True
	defaultaxes -- Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues
	        default=False, example: defaultaxes=True
	defaultaxesvalues -- List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes)
                For existing axes, empty strings can be given as values.
		For the directions and spectral values, any valid angle/frequency expressions can be given.
	        default = [], example: defaultaxesvalues=['19h30m00', '-02d30m00', '88.5GHz', 'Q'] 
	beam -- List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords)
	        default = [] (i.e.take from FITS file), example: beam=['0.35arcsec', '0.24arcsec', '25deg']


	


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - fitsimage
     - :code:`''`
     - 
   * - imagename
     - :code:`''`
     - 
   * - whichrep
     - :code:`int(0)`
     - 
   * - whichhdu
     - :code:`int(-1)`
     - 
   * - zeroblanks
     - :code:`True`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - defaultaxes
     - :code:`False`
     - 
   * - defaultaxesvalues
     - :code:`[ ]`
     - 
   * - beam
     - :code:`[ ]`
     - 


Parameter Explanations
=======================================



fitsimage
---------------------------------------

:code:`''`

Name of input image FITS file


imagename
---------------------------------------

:code:`''`

Name of output CASA image


whichrep
---------------------------------------

:code:`int(0)`

If fits image has multiple coordinate reps, choose one.


whichhdu
---------------------------------------

:code:`int(-1)`

If its file contains multiple images, choose one (0 = first HDU, -1 = first valid image).


zeroblanks
---------------------------------------

:code:`True`

Set blanked pixels to zero (not NaN)


overwrite
---------------------------------------

:code:`False`

Overwrite pre-existing imagename


defaultaxes
---------------------------------------

:code:`False`

Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues


defaultaxesvalues
---------------------------------------

:code:`[ ]`

List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes)


beam
---------------------------------------

:code:`[ ]`

List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords)




