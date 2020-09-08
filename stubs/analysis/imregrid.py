#
# stub function definition file for docstring parsing
#

def imregrid(imagename, template='get', output='', asvelocity=True, axes=[-1], shape=[-1], interpolation='linear', decimate=10, replicate=False, overwrite=False):
    r"""
regrid an image onto a template image

Parameters
   - imagename_ (string) - Name of the source image
   - template_ (variant='get') - A dictionary, refcode, or name of an image that provides the output shape and coordinate system
   - output_ (string='') - Name for the regridded image
   - asvelocity_ (bool=True) - Regrid spectral axis in velocity space rather than frequency space?
   - axes_ (intArray=[-1]) - The pixel axes to regrid. -1 => all.
   - interpolation_ (string='linear') - The interpolation method.  One of "nearest", "linear", "cubic".
   - decimate_ (int=10) - Decimation factor for coordinate grid computation
   - replicate_ (bool=False) - Replicate image rather than regrid?
   - overwrite_ (bool=False) - Overwrite (unprompted) pre-existing output file?







Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Name of the source image

.. _template:

   .. rubric:: template

   | A dictionary, refcode, or name of an image that provides the output shape and coordinate system

.. _output:

   .. rubric:: output

   | Name for the regridded image

.. _asvelocity:

   .. rubric:: asvelocity

   | Regrid spectral axis in velocity space rather than frequency space?

.. _axes:

   .. rubric:: axes

   | The pixel axes to regrid. -1 => all.

.. _shape:

   .. rubric:: shape

   | Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.

.. _interpolation:

   .. rubric:: interpolation

   | The interpolation method.  One of "nearest", "linear", "cubic".

.. _decimate:

   .. rubric:: decimate

   | Decimation factor for coordinate grid computation

.. _replicate:

   .. rubric:: replicate

   | Replicate image rather than regrid?

.. _overwrite:

   .. rubric:: overwrite

   | Overwrite (unprompted) pre-existing output file?


    """
    pass
