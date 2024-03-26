imsmooth -- Smooth an image or portion of an image -- analysis task
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
   * - kernel
     - :code:`'gauss'`
     - 
   * - major
     - :code:`''`
     - 
   * - minor
     - :code:`''`
     - 
   * - pa
     - :code:`''`
     - 
   * - targetres
     - :code:`False`
     - 
   * - kimage
     - :code:`''`
     - 
   * - scale
     - :code:`float(-1.0)`
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
   * - outfile
     - :code:`''`
     - 
   * - stretch
     - :code:`False`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - beam
     - :code:`''`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image. Must be specified.


kernel
---------------------------------------

:code:`'gauss'`

Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel.


major
---------------------------------------

:code:`''`

Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". Example: "4arcsec".


minor
---------------------------------------

:code:`''`

Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". Example: "2arcsec".


pa
---------------------------------------

:code:`''`

Position angle used only for gaussian kernel. Standard quantity representation. Example: "40deg".


targetres
---------------------------------------

:code:`False`

If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).


kimage
---------------------------------------

:code:`''`

Kernel image name. Only used if kernel="i" or "image".


scale
---------------------------------------

:code:`float(-1.0)`

Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".


region
---------------------------------------

:code:`''`

Region selection. See "help par.region" for details. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use. See "help par.chans" for details. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. See "help par.stokes" for details. Default is to use all Stokes planes.


mask
---------------------------------------

:code:`''`

Mask to use. See help par.mask. Default is none.


outfile
---------------------------------------

:code:`''`

Output image name. Must be specified.


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? See help par.stretch 


overwrite
---------------------------------------

:code:`False`

Overwrite (unprompted) pre-existing output file?


beam
---------------------------------------

:code:`''`

Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa. Example: Example: {"major": "5arcsec", "minor": "2arcsec", "pa": "20deg"}.




