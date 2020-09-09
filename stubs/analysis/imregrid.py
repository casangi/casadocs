#
# stub function definition file for docstring parsing
#

def imregrid(imagename, template='get', output='', asvelocity=True, axes=[-1], shape=[-1], interpolation='linear', decimate=10, replicate=False, overwrite=False):
    r"""
regrid an image onto a template image

Parameters
   - imagename_ (string) - Name of the source image
   - template_ (variant='get') - A dictionary, refcode, or name of an image that provides the output shape and coordinate system

      .. raw:: html

         <details><summary><i> template != get </i></summary>

      - shape_ (intArray=[-1]) - Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.

      .. raw:: html

         </details>
   - output_ (string='') - Name for the regridded image
   - asvelocity_ (bool=True) - Regrid spectral axis in velocity space rather than frequency space?
   - axes_ (intArray=[-1]) - The pixel axes to regrid. -1 => all.
   - interpolation_ (string='linear') - The interpolation method.  One of "nearest", "linear", "cubic".
   - decimate_ (int=10) - Decimation factor for coordinate grid computation
   - replicate_ (bool=False) - Replicate image rather than regrid?
   - overwrite_ (bool=False) - Overwrite (unprompted) pre-existing output file?





.. _imagename:

imagename (string)
   | Name of the source image

.. _template:

template (variant='get')
   | A dictionary, refcode, or name of an image that provides the output shape and coordinate system

.. _output:

output (string='')
   | Name for the regridded image

.. _asvelocity:

asvelocity (bool=True)
   | Regrid spectral axis in velocity space rather than frequency space?

.. _axes:

axes (intArray=[-1])
   | The pixel axes to regrid. -1 => all.

.. _shape:

shape (intArray=[-1])
   | Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.

.. _interpolation:

interpolation (string='linear')
   | The interpolation method.  One of "nearest", "linear", "cubic".

.. _decimate:

decimate (int=10)
   | Decimation factor for coordinate grid computation

.. _replicate:

replicate (bool=False)
   | Replicate image rather than regrid?

.. _overwrite:

overwrite (bool=False)
   | Overwrite (unprompted) pre-existing output file?


    """
    pass
