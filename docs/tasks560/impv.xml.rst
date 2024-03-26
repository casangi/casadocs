impv -- Construct a position-velocity image by choosing two points in the direction plane. -- analysis task
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
     - 
   * - outfile
     - :code:`''`
     - 
   * - mode
     - :code:`'coords'`
     - 
   * - start
     - :code:`''`
     - 
   * - end
     - :code:`''`
     - 
   * - center
     - :code:`''`
     - 
   * - length
     - :code:`''`
     - 
   * - pa
     - :code:`''`
     - 
   * - width
     - :code:`int(1)`
     - 
   * - unit
     - :code:`'arcsec'`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - region
     - :code:`[ ]`
     - 
   * - chans
     - :code:`''`
     - 
   * - stokes
     - :code:`''`
     - 
   * - mask
     - :code:`''`
     - 
   * - stretch
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


outfile
---------------------------------------

:code:`''`

Output image name. If empty, no image is written.


mode
---------------------------------------

:code:`'coords'`

If "coords", use start and end values. If "length", use center, length, and pa values.


start
---------------------------------------

:code:`''`

The starting pixel in the direction plane (array of two values).


end
---------------------------------------

:code:`''`

The ending pixel in the direction plane (array of two values).


center
---------------------------------------

:code:`''`

The center point in the direction plane (array of two values). If specified, length and pa must also be specified and neither of start nor end may be specified.


length
---------------------------------------

:code:`''`

The length of the segment in the direction plane. If specified, center and pa must also be specified and neither of start nor end may be specified.


pa
---------------------------------------

:code:`''`

The position angle of the segment in the direction plane, measured from north through east. If specified, center and length must also be specified and neither of start nor end may be specified.


width
---------------------------------------

:code:`int(1)`

Width of slice for averaging pixels perpendicular to the slice. Must be an odd positive integer or valid quantity. See help for details.


unit
---------------------------------------

:code:`'arcsec'`

Unit for the offset axis in the resulting image. Must be a unit of angular measure.


overwrite
---------------------------------------

:code:`False`

Overwrite the output if it exists?


region
---------------------------------------

:code:`[ ]`

Region selection. Default is entire image. No selection is permitted in the direction plane.


chans
---------------------------------------

:code:`''`

Channels to use.  Channels must be contiguous. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. Planes must be contiguous. Default is to use all stokes.


mask
---------------------------------------

:code:`''`

Mask to use. Default is none.


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? Default False




