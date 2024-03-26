imdev -- Create an image that can represent the statistical deviations of the input image. -- analysis task
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
   * - region
     - :code:`''`
     - 
   * - box
     - :code:`''`
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
   * - overwrite
     - :code:`False`
     - 
   * - stretch
     - :code:`False`
     - 
   * - grid
     - :code:`numpy.array( [ int(1),int(1) ] )`
     - 
   * - anchor
     - :code:`'ref'`
     - 
   * - xlength
     - :code:`'1pix'`
     - 
   * - ylength
     - :code:`'1pix'`
     - 
   * - interp
     - :code:`'cubic'`
     - 
   * - stattype
     - :code:`'sigma'`
     - 
   * - statalg
     - :code:`'classic'`
     - 
   * - zscore
     - :code:`float(-1)`
     - 
   * - maxiter
     - :code:`int(-1)`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Input image name


outfile
---------------------------------------

:code:`''`

Output image file name. If left blank (the default), no image is written but a new image tool referencing the collapsed image is returned.


region
---------------------------------------

:code:`''`

Region selection. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. Default is to use all Stokes planes.


mask
---------------------------------------

:code:`''`

Mask to use. Default setting is none. 


overwrite
---------------------------------------

:code:`False`

Overwrite (unprompted) pre-existing output file? Ignored if "outfile" is left blank. 


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? Default value is False.


grid
---------------------------------------

:code:`numpy.array( [ int(1),int(1) ] )`

x,y grid spacing. Array of exactly two positive integers.


anchor
---------------------------------------

:code:`'ref'`

x,y anchor pixel location. Either "ref" to use the image reference pixel, or an array of exactly two integers.


xlength
---------------------------------------

:code:`'1pix'`

Either x coordinate length of box, or diameter of circle. Circle is used if ylength is empty string.


ylength
---------------------------------------

:code:`'1pix'`

y coordinate length of box. Use a circle if ylength is empty string.


interp
---------------------------------------

:code:`'cubic'`

Interpolation algorithm to use. One of "nearest", "linear", "cubic", or "lanczos". Minimum match supported.


stattype
---------------------------------------

:code:`'sigma'`

Statistic to compute. See full description for supported statistics.


statalg
---------------------------------------

:code:`'classic'`

Statistics computation algorithm to use. Supported values are "chauvenet" and "classic", Minimum match is supported.


zscore
---------------------------------------

:code:`float(-1)`

For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".


maxiter
---------------------------------------

:code:`int(-1)`

For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algortihm is not "chauvenet".




