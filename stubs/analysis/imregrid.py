#
# stub function definition file for docstring parsing
#

def imregrid(imagename, template='get', output='', asvelocity=True, axes=[-1], shape=[-1], interpolation='linear', decimate=10, replicate=False, overwrite=False):
    r"""
regrid an image onto a template image

Parameters
   - **imagename** (string) - Name of the source image [1]_
   - **template** (variant='get') - A dictionary, refcode, or name of an image that provides the output shape and coordinate system [2]_
   - **output** (string='') - Name for the regridded image [3]_
   - **asvelocity** (bool=True) - Regrid spectral axis in velocity space rather than frequency space? [4]_
   - **axes** (intArray=[-1]) - The pixel axes to regrid. -1 => all. [5]_
   - **interpolation** (string='linear') - The interpolation method.  One of "nearest", "linear", "cubic". [7]_
   - **decimate** (int=10) - Decimation factor for coordinate grid computation [8]_
   - **replicate** (bool=False) - Replicate image rather than regrid? [9]_
   - **overwrite** (bool=False) - Overwrite (unprompted) pre-existing output file? [10]_







Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Name of the source image
.. [2] 
   **template** (variant='get')
      | A dictionary, refcode, or name of an image that provides the output shape and coordinate system
.. [3] 
   **output** (string='')
      | Name for the regridded image
.. [4] 
   **asvelocity** (bool=True)
      | Regrid spectral axis in velocity space rather than frequency space?
.. [5] 
   **axes** (intArray=[-1])
      | The pixel axes to regrid. -1 => all.
.. [6] 
   **shape** (intArray=[-1])
      | Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.
.. [7] 
   **interpolation** (string='linear')
      | The interpolation method.  One of "nearest", "linear", "cubic".
.. [8] 
   **decimate** (int=10)
      | Decimation factor for coordinate grid computation
.. [9] 
   **replicate** (bool=False)
      | Replicate image rather than regrid?
.. [10] 
   **overwrite** (bool=False)
      | Overwrite (unprompted) pre-existing output file?

    """
    pass
