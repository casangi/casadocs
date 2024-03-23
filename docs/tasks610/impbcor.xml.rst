impbcor -- Construct a primary beam corrected image from an image and a primary beam pattern. -- analysis task
=======================================

Description
---------------------------------------

Correct an image for primary beam attenuation using an image of the
primary beam pattern. The primary beam pattern can be provided as an
image, in which case 1. it must have the same shape as the input image
and its coordinate system must be the same, or 2. it must be a 2-D
image in which case its coordinate system must consist of a (2-D)
direction coordinate which is the same as the direction coordinate in
the input image and its direction plane must be the same shape as that
of the input image. Alternatively, pbimage can be an array of pixel
values in which case the same dimensionality and shape constraints
apply.

One can choose between dividing the image by the primary beam pattern
(mode="divide") or multiplying the image by the primary beam pattern
(mode="multiply"). One can also choose to specify a cutoff limit for
the primary beam pattern. For mode="divide", for all pixels below this
cutoff in the primary beam pattern, the output image will be
masked. In the case of mode="multiply", all pixels in the output will
be masked corresponding to pixels with values greater than the cutoff
in the primary beam pattern. A negative value for cutoff means that no
cutoff will be applied, which is the default.



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
     - Name of the input image
   * - pbimage
     - :code:`[ ]`
     - Name of the primary beam image which must exist or array of values for the pb response.
   * - outfile
     - :code:`''`
     - Output image name. If empty, no image is written.
   * - overwrite
     - :code:`False`
     - Overwrite the output if it exists?
   * - box
     - :code:`''`
     - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   * - region
     - :code:`''`
     - Region selection.
   * - chans
     - :code:`''`
     - Channels to use.
   * - stokes
     - :code:`''`
     - Stokes planes to use.
   * - mask
     - :code:`''`
     - Mask to use.
   * - mode
     - :code:`'divide'`
     - Divide or multiply the image by the primary beam image. Minimal match supported.
   * - cutoff
     - :code:`float(-1.0)`
     - PB cutoff. If mode is "d", all values less than this will be masked. If "m", all values greater will be masked. Less than 0, no cutoff.
   * - stretch
     - :code:`False`
     - Stretch the mask if necessary and possible?


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input (CASA, FITS, MIRIAD) image



pbimage
---------------------------------------

:code:`[ ]`

Name of the image (CASA, FITS, MIRIAD) of the primary
beam pattern or an array of pixel values.
                     Default: ''



outfile
---------------------------------------

:code:`''`

Name of output CASA image. 
                     Default: none. Must be specified.



overwrite
---------------------------------------

:code:`False`

If output file is specified, controls if an already
existing file by the same name can be overwritten. 
                     Default: True
                     Options: True|False

                     If true, the user is not prompted, the file if it
                     exists is automatically overwritten.



box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane.
                     Default: '' (use the entire direction plane)



region
---------------------------------------

:code:`''`

Region selection. 
                     Default: '' (use the full image)



chans
---------------------------------------

:code:`''`

Channels to use. 
                     Default: '' (use all channels)



stokes
---------------------------------------

:code:`''`

Stokes planes to use.
                     Default: '' (use all Stokes planes)



mask
---------------------------------------

:code:`''`

Mask to use.
                     Default: none



mode
---------------------------------------

:code:`'divide'`

Divide or multiply the image by the primary beam image. 
                     Default: 'divide'

                     Minimal match supported.



cutoff
---------------------------------------

:code:`float(-1.0)`

Primary beam cutoff.
                     Default: -1.0 (no cutoff)

                     If mode is "d", all values less than this will be
                     masked. If "m", all values greater will be
                     masked. Less than 0, no cutoff (default)



stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 
                     Default: False
                     Options: False|True





