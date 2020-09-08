#
# stub function definition file for docstring parsing
#

def importfits(fitsimage, imagename='', whichrep=0, whichhdu=-1, zeroblanks=True, overwrite=False, defaultaxes=False, defaultaxesvalues='[]', beam='[]'):
    r"""
Convert an image FITS file into a CASA image

Parameters
   - fitsimage_ (string) - Name of input image FITS file
   - imagename_ (string='') - Name of output CASA image
   - whichrep_ (int=0) - If fits image has multiple coordinate reps, choose one.
   - whichhdu_ (int=-1) - If fits file contains multiple images, choose one (0 = first HDU, -1 = first valid image).
   - zeroblanks_ (bool=True) - Set blanked pixels to zero (not NaN)
   - overwrite_ (bool=False) - Overwrite output file if it exists?
   - defaultaxes_ (bool=False) - Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues
   - defaultaxesvalues_ (variant='[]') - List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes)
   - beam_ (variant='[]') - List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords)







Details
   Explanation of each parameter

.. _fitsimage:

   .. rubric:: fitsimage

   | Name of input image FITS file
   |                      Default: none
   | 
   |                         Example: fitsimage='3C273XC1.fits'

.. _imagename:

   .. rubric:: imagename

   | Name of output CASA image
   |                      Default: none
   | 
   |                         Example: fitsimage='3C273XC1.image'

.. _whichrep:

   .. rubric:: whichrep

   | If fits image has multiple coordinate reps, choose one.
   |                      Default: 0 (means first)
   | 
   |                         Example: whichrep=1

.. _whichhdu:

   .. rubric:: whichhdu

   | If fits file contains multiple images, choose one
   |                      Default: -1 (use the first valid one)
   | 
   |                      NOTE: 0 = first HDU, -1 = first valid image
   | 
   |                         Example: whichhdu=1

.. _zeroblanks:

   .. rubric:: zeroblanks

   | Set blanked pixels to zero (not NaN)
   |                      Default: True
   |                      Options: True|False

.. _overwrite:

   .. rubric:: overwrite

   | Overwrite output file if it exists?
   |                      Default: False
   |                      Options: False|True

.. _defaultaxes:

   .. rubric:: defaultaxes

   | Add the default 4D coordinate axes where they are
   | missing
   |                      Default: False
   |                      Options: False|True
   | 
   |                      IMPORTANT: value True requires setting defaultaxesvalues

.. _defaultaxesvalues:

   .. rubric:: defaultaxesvalues

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

.. _beam:

   .. rubric:: beam

   | List of values to be used to define the synthesized beam
   | [BMAJ,BMIN,BPA] (as in the FITS keywords)
   |                      Default: [] (i.e.take from FITS file)
   | 
   |                         Example: beam=['0.35arcsec', '0.24arcsec',
   |                         '25deg']


    """
    pass
