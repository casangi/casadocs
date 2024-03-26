imregrid -- regrid an image onto a template image -- analysis task
=======================================

Description
---------------------------------------

Imregrid will regrid an input image onto a new coordinate system from a template image
or to a new directional reference frame. If a template image is used, then the input and
template images must have the same coordinate structure.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - imagename
     - :code:`''`
     - Name of the source image
   * - template
     - :code:`'get'`
     - A dictionary, refcode, or name of an image that provides the output shape and coordinate system
   * - output
     - :code:`''`
     - Name for the regridded image
   * - asvelocity
     - :code:`True`
     - Regrid spectral axis in velocity space rather than frequency space?
   * - axes
     - :code:`numpy.array( [  ] )`
     - The pixel axes to regrid. -1 => all.
   * - shape
     - :code:`numpy.array( [  ] )`
     - Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.
   * - interpolation
     - :code:`'linear'`
     - The interpolation method.  One of "nearest", "linear", "cubic".
   * - decimate
     - :code:`int(10)`
     - Decimation factor for coordinate grid computation
   * - replicate
     - :code:`False`
     - Replicate image rather than regrid?
   * - overwrite
     - :code:`False`
     - Overwrite (unprompted) pre-existing output file?


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the source image


template
---------------------------------------

:code:`'get'`

A dictionary, refcode, or name of an image that provides the output shape and coordinate system


output
---------------------------------------

:code:`''`

Name for the regridded image


asvelocity
---------------------------------------

:code:`True`

Regrid spectral axis in velocity space rather than frequency space?


axes
---------------------------------------

:code:`numpy.array( [  ] )`

The pixel axes to regrid. -1 => all.


shape
---------------------------------------

:code:`numpy.array( [  ] )`

Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.


interpolation
---------------------------------------

:code:`'linear'`

The interpolation method.  One of "nearest", "linear", "cubic".


decimate
---------------------------------------

:code:`int(10)`

Decimation factor for coordinate grid computation


replicate
---------------------------------------

:code:`False`

Replicate image rather than regrid?


overwrite
---------------------------------------

:code:`False`

Overwrite (unprompted) pre-existing output file?




