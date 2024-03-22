importfits -- Convert an image FITS file into a CASA image -- import/export task
=======================================

Description
---------------------------------------

Convert an image FITS file into a CASA image



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
     - Name of input image FITS file
   * - imagename
     - :code:`''`
     - Name of output CASA image
   * - whichrep
     - :code:`int(0)`
     - If fits image has multiple coordinate reps, choose one.
   * - whichhdu
     - :code:`int(-1)`
     - If fits file contains multiple images, choose one (0 = first HDU, -1 = first valid image).
   * - zeroblanks
     - :code:`True`
     - Set blanked pixels to zero (not NaN)
   * - overwrite
     - :code:`False`
     - Overwrite output file if it exists?
   * - defaultaxes
     - :code:`False`
     - Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues
   * - defaultaxesvalues
     - :code:`[ ]`
     - List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes)
   * - beam
     - :code:`[ ]`
     - List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords)


Parameter Explanations
=======================================



fitsimage
---------------------------------------

:code:`''`

Name of input image FITS file
                     Default: none

                        Example: fitsimage='3C273XC1.fits'



imagename
---------------------------------------

:code:`''`

Name of output CASA image
                     Default: none

                        Example: fitsimage='3C273XC1.image'



whichrep
---------------------------------------

:code:`int(0)`

If fits image has multiple coordinate reps, choose one.
                     Default: 0 (means first)

                        Example: whichrep=1



whichhdu
---------------------------------------

:code:`int(-1)`

If fits file contains multiple images, choose one
                     Default: -1 (use the first valid one)

                     NOTE: 0 = first HDU, -1 = first valid image

                        Example: whichhdu=1



zeroblanks
---------------------------------------

:code:`True`

Set blanked pixels to zero (not NaN)
                     Default: True
                     Options: True|False



overwrite
---------------------------------------

:code:`False`

Overwrite output file if it exists?
                     Default: False
                     Options: False|True



defaultaxes
---------------------------------------

:code:`False`

Add the default 4D coordinate axes where they are
missing
                     Default: False
                     Options: False|True

                     IMPORTANT: value True requires setting defaultaxesvalues



defaultaxesvalues
---------------------------------------

:code:`[ ]`

List of values to assign to added degenerate axes when
defaultaxes==True (ra,dec,freq,stokes)
                     Default: []

                     For existing axes, empty strings can be given as
                     values. For the directions and spectral values,
                     any valid angle/frequency expressions can be
                     given.

                        Example: defaultaxesvalues=['19h30m00',
                        '-02d30m00', '88.5GHz', 'Q'] 



beam
---------------------------------------

:code:`[ ]`

List of values to be used to define the synthesized beam
[BMAJ,BMIN,BPA] (as in the FITS keywords)
                     Default: [] (i.e.take from FITS file)

                        Example: beam=['0.35arcsec', '0.24arcsec',
                        '25deg']





