#
# stub function definition file for docstring parsing
#

def imregrid(imagename, template='get', output='', asvelocity=True, axes=[-1], shape=[-1], interpolation='linear', decimate=10, replicate=False, overwrite=False):
    r"""
regrid an image onto a template image

Parameters
   - **imagename** (string) - Name of the source image
   - **template** (variant='get') - A dictionary, refcode, or name of an image that provides the output shape and coordinate system
   - **output** (string='') - Name for the regridded image
   - **asvelocity** (bool=True) - Regrid spectral axis in velocity space rather than frequency space?
   - **axes** (intArray=[-1]) - The pixel axes to regrid. -1 => all.
   - **interpolation** (string='linear') - The interpolation method.  One of "nearest", "linear", "cubic".
   - **decimate** (int=10) - Decimation factor for coordinate grid computation
   - **replicate** (bool=False) - Replicate image rather than regrid?
   - **overwrite** (bool=False) - Overwrite (unprompted) pre-existing output file?




    """
    pass
