#
# stub function definition file for docstring parsing
#

def importfits(fitsimage, imagename='', whichrep=0, whichhdu=-1, zeroblanks=True, overwrite=False, defaultaxes=False, defaultaxesvalues='[]', beam='[]'):
    r"""
Convert an image FITS file into a CASA image

Parameters
   - **fitsimage** (string) - Name of input image FITS file [1]_
   - **imagename** (string='') - Name of output CASA image [2]_
   - **whichrep** (int=0) - If fits image has multiple coordinate reps, choose one. [3]_
   - **whichhdu** (int=-1) - If fits file contains multiple images, choose one (0 = first HDU, -1 = first valid image). [4]_
   - **zeroblanks** (bool=True) - Set blanked pixels to zero (not NaN) [5]_
   - **overwrite** (bool=False) - Overwrite output file if it exists? [6]_
   - **defaultaxes** (bool=False) - Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues [7]_
   - **defaultaxesvalues** (variant='[]') - List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes) [8]_
   - **beam** (variant='[]') - List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords) [9]_







Details
   Explanation of each parameter

.. [1] 
   **fitsimage** (string)
      | Name of input image FITS file
      |                      Default: none
      | 
      |                         Example: fitsimage='3C273XC1.fits'
.. [2] 
   **imagename** (string='')
      | Name of output CASA image
      |                      Default: none
      | 
      |                         Example: fitsimage='3C273XC1.image'
.. [3] 
   **whichrep** (int=0)
      | If fits image has multiple coordinate reps, choose one.
      |                      Default: 0 (means first)
      | 
      |                         Example: whichrep=1
.. [4] 
   **whichhdu** (int=-1)
      | If fits file contains multiple images, choose one
      |                      Default: -1 (use the first valid one)
      | 
      |                      NOTE: 0 = first HDU, -1 = first valid image
      | 
      |                         Example: whichhdu=1
.. [5] 
   **zeroblanks** (bool=True)
      | Set blanked pixels to zero (not NaN)
      |                      Default: True
      |                      Options: True|False
.. [6] 
   **overwrite** (bool=False)
      | Overwrite output file if it exists?
      |                      Default: False
      |                      Options: False|True
.. [7] 
   **defaultaxes** (bool=False)
      | Add the default 4D coordinate axes where they are
      | missing
      |                      Default: False
      |                      Options: False|True
      | 
      |                      IMPORTANT: value True requires setting defaultaxesvalues
.. [8] 
   **defaultaxesvalues** (variant='[]')
      | List of values to assign to added degenerate axes when
      | defaultaxes==True (ra,dec,freq,stokes)
      |                      Default: []
      | 
      |                      For existing axes, empty strings can be given as
      |                      values. For the directions and spectral values,
      |                      any valid angle/frequency expressions can be
      |                      given.
      | 
      |                         Example: defaultaxesvalues=['19h30m00',
      |                         '-02d30m00', '88.5GHz', 'Q']
.. [9] 
   **beam** (variant='[]')
      | List of values to be used to define the synthesized beam
      | [BMAJ,BMIN,BPA] (as in the FITS keywords)
      |                      Default: [] (i.e.take from FITS file)
      | 
      |                         Example: beam=['0.35arcsec', '0.24arcsec',
      |                         '25deg']

    """
    pass
