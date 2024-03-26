imcollapse -- Collapse image along one axis, aggregating pixel values along that axis. -- analysis task
=======================================

Description
---------------------------------------

This task collapses an image along a specified axis or set of axes of
N pixels to a single pixel on each specified axis. Both float valued
and complex valued images are supported. It computes the specified
aggregate function for pixel values along the specified axes and
places those values in the single remaining plane of those axes in the
output image. 

The reference pixel of the collapsed axis is set to 0 and its
reference value is set to the mean of the the first and last values of
that axis in the specified region of the input image. Convolution to a
common beam is not performed automatically as part of the
preprocessing before the collapse operation occurs. Therefore, if the
input image has per-plane beams, then the user should consider first
smoothing the data to have the same resolution, and use the resulting
image as the input for imcollapse.



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
   * - function
     - :code:`''`
     - Aggregate function to apply. This can be set one of flux, madm, max, mean, median, min, npts, rms, stddev, sum, variance, xmadm. Must be specified.
   * - axes
     - :code:`[ ]`
     - Zero-based axis number(s) or minimal match strings to collapse.
   * - outfile
     - :code:`''`
     - Name of output CASA image. Must be specified.
   * - box
     - :code:`''`
     - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   * - region
     - :code:`''`
     - Region selection. Default is to use the full image.
   * - chans
     - :code:`''`
     - Channels to use. Default is to use all channels.
   * - stokes
     - :code:`''`
     - Stokes planes to use. Default is to use all Stokes planes.
   * - mask
     - :code:`''`
     - Mask to use. Default is none.
   * - overwrite
     - :code:`False`
     - Overwrite output image if it exists?
   * - stretch
     - :code:`False`
     - Stretch the mask if necessary and possible?


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image
                     Default: none

                        Example: imagename='ngc5921.im' 



function
---------------------------------------

:code:`''`

Function used to compute aggregation of pixel values
along the collapsed axis.
                     Default: none
                     Options: flux, madm, max, mean, median, min,
                     npts, rms, stddev, sum, variance, xmadm

                     Minimum match is supported for the function
                     parameter (eg, function="r" will compute the rms
                     of the pixel values).

                     If one specifies function='flux', the following
                     constraints must be true:
                     1. The image must have a direction coordinate,
                     2. The image must have at least one beam,
                     3. The specified axes must be exactly the
                     direction coordinate axes,
                     4. Only one of the non-directional axes may be
                     non-degenerate,
                     5. The iamge brightness unit must be conformant
                     with x*yJy/beam, where x is an optional unit
                     (such as km/s for moments images) and y is an
                     optional SI prefix.



axes
---------------------------------------

:code:`[ ]`

Zero-based axis number(s) or minimal match strings to
collapse.
                     Default: [0]
                     Axes can be specified as a single integer or
                     array of integers indicating the zero-based axes
                     along which to collapse the image. Axes may also
                     be specified as a single or array of strings
                     which minimally and uniquely match (ignoring
                     case) world axes names in the image (eg "dec" or
                     ["ri, "d"] for collapsing along the declination
                     axis or along the right ascension and declination
                     axes, respectively).



outfile
---------------------------------------

:code:`''`

Name of output CASA image. Must be specified.
                     Default: none

                        Example: outfile='collapsed.im'



box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. 
                     Default: '' (use the entire direction plane)

                        Example: box="100,100,200,200"



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
                     Default: '' (use all stokes planes)



mask
---------------------------------------

:code:`''`

Mask to use.
                     Default: none



overwrite
---------------------------------------

:code:`False`

Overwrite output image if it exists?
                     Default: False
                     Options: False|True



stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 
                     Default: False
                     Options: False|True

                     Stretch the input mask if necessary and
                     possible. Only used if a mask is specified.





