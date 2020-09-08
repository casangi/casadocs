#
# stub function definition file for docstring parsing
#

def imcollapse(imagename, function='', axes='[0]', outfile='', box='', region='', chans='', stokes='', mask='', overwrite=False, stretch=False):
    r"""
Collapse image along one axis, aggregating pixel values along that axis.

Parameters
   - imagename_ (string) - Name of the input image
   - function_ (string='') - Aggregate function to apply. This can be set one of flux, madm, max, mean, median, min, npts, rms, stddev, sum, variance, xmadm. Must be specified.
   - axes_ (variant='[0]') - Zero-based axis number(s) or minimal match strings to collapse.
   - outfile_ (string='') - Name of output CASA image. Must be specified.
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - region_ (string='') - Region selection. Default is to use the full image.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - mask_ (string='') - Mask to use. Default is none.
   - stretch_ (bool=False) - Stretch the mask if necessary and possible?







Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Name of the input image
   |                      Default: none
   | 
   |                         Example: imagename='ngc5921.im'

.. _function:

   .. rubric:: function

   | Function used to compute aggregation of pixel values
   | along the collapsed axis.
   |                      Default: none
   |                      Options: flux, madm, max, mean, median, min,
   |                      npts, rms, stddev, sum, variance, xmadm
   | 
   |                      Minimum match is supported for the function
   |                      parameter (eg, function="r" will compute the rms
   |                      of the pixel values).
   | 
   |                      If one specifies function='flux', the following
   |                      constraints must be true:
   |                      1. The image must have a direction coordinate,
   |                      2. The image must have at least one beam,
   |                      3. The specified axes must be exactly the
   |                      direction coordinate axes,
   |                      4. Only one of the non-directional axes may be
   |                      non-degenerate,
   |                      5. The iamge brightness unit must be conformant
   |                      with x*yJy/beam, where x is an optional unit
   |                      (such as km/s for moments images) and y is an
   |                      optional SI prefix.

.. _axes:

   .. rubric:: axes

   | Zero-based axis number(s) or minimal match strings to
   | collapse.
   |                      Default: [0]
   |                      Axes can be specified as a single integer or
   |                      array of integers indicating the zero-based axes
   |                      along which to collapse the image. Axes may also
   |                      be specified as a single or array of strings
   |                      which minimally and uniquely match (ignoring
   |                      case) world axes names in the image (eg "dec" or
   |                      ["ri, "d"] for collapsing along the declination
   |                      axis or along the right ascension and declination
   |                      axes, respectively).

.. _outfile:

   .. rubric:: outfile

   | Name of output CASA image. Must be specified.
   |                      Default: none
   | 
   |                         Example: outfile='collapsed.im'

.. _box:

   .. rubric:: box

   | Rectangular region to select in direction plane. 
   |                      Default: '' (use the entire direction plane)
   | 
   |                         Example: box="100,100,200,200"

.. _region:

   .. rubric:: region

   | Region selection.
   |                      Default: '' (use the full image)

.. _chans:

   .. rubric:: chans

   | Channels to use. 
   |                      Default: '' (use all channels)

.. _stokes:

   .. rubric:: stokes

   | Stokes planes to use.
   |                      Default: '' (use all stokes planes)

.. _mask:

   .. rubric:: mask

   | Mask to use.
   |                      Default: none

.. _overwrite:

   .. rubric:: overwrite

   | Overwrite output image if it exists?
   |                      Default: False
   |                      Options: False|True

.. _stretch:

   .. rubric:: stretch

   | Stretch the mask if necessary and possible? 
   |                      Default: False
   |                      Options: False|True
   | 
   |                      Stretch the input mask if necessary and
   |                      possible. Only used if a mask is specified.


    """
    pass
