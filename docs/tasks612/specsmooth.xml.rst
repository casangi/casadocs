specsmooth -- Smooth an image region in one dimension -- analysis task
=======================================

Description
---------------------------------------




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
   * - outfile
     - :code:`''`
     - Output image name.
   * - box
     - :code:`''`
     - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   * - chans
     - :code:`''`
     - Channels to use. Channels must be contiguous. Default is to use all channels.
   * - stokes
     - :code:`''`
     - Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.
   * - region
     - :code:`''`
     - Region selection. Default is to use the full image.
   * - mask
     - :code:`''`
     - Mask to use. Default is none..
   * - overwrite
     - :code:`False`
     - Overwrite the output if it exists?
   * - stretch
     - :code:`False`
     - Stretch the mask if necessary and possible? Default False
   * - axis
     - :code:`int(-1)`
     - The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).
   * - function
     - :code:`'boxcar'`
     - Convolution function. hanning and boxcar are supported functions. Minimum match is supported.
   * - width
     - :code:`int(2)`
     - Width of boxcar, in pixels.
   * - dmethod
     - :code:`'copy'`
     - Decimation method. "" means no decimation, "copy" and "mean" are also supported (minimum match).


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


outfile
---------------------------------------

:code:`''`

Output image name.


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use. Channels must be contiguous. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.


region
---------------------------------------

:code:`''`

Region selection. Default is to use the full image.


mask
---------------------------------------

:code:`''`

Mask to use. Default is none..


overwrite
---------------------------------------

:code:`False`

Overwrite the output if it exists?


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? Default False


axis
---------------------------------------

:code:`int(-1)`

The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).


function
---------------------------------------

:code:`'boxcar'`

Convolution function. hanning and boxcar are supported functions. Minimum match is supported.


width
---------------------------------------

:code:`int(2)`

Width of boxcar, in pixels.


dmethod
---------------------------------------

:code:`'copy'`

Decimation method. "" means no decimation, "copy" and "mean" are also supported (minimum match).




