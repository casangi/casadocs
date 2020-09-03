#
# stub function definition file for docstring parsing
#

def importfits(fitsimage, imagename='', whichrep=0, whichhdu=-1, zeroblanks=True, overwrite=False, defaultaxes=False, defaultaxesvalues='[]', beam='[]'):
    r"""
Convert an image FITS file into a CASA image

Parameters
   - **fitsimage** (string) - Name of input image FITS file
   - **imagename** (string='') - Name of output CASA image
   - **whichrep** (int=0) - If fits image has multiple coordinate reps, choose one.
   - **whichhdu** (int=-1) - If fits file contains multiple images, choose one (0 = first HDU, -1 = first valid image).
   - **zeroblanks** (bool=True) - Set blanked pixels to zero (not NaN)
   - **overwrite** (bool=False) - Overwrite output file if it exists?
   - **defaultaxes** (bool=False) - Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues
   - **defaultaxesvalues** (variant='[]') - List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes)
   - **beam** (variant='[]') - List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords)




    """
    pass
