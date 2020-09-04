#
# stub function definition file for docstring parsing
#

def imcollapse(imagename, function='', axes='[0]', outfile='', box='', region='', chans='', stokes='', mask='', overwrite=False, stretch=False):
    r"""
Collapse image along one axis, aggregating pixel values along that axis.

Parameters
   - **imagename** (string) - Name of the input image [1]_
   - **function** (string='') - Aggregate function to apply. This can be set one of flux, madm, max, mean, median, min, npts, rms, stddev, sum, variance, xmadm. Must be specified. [2]_
   - **axes** (variant='[0]') - Zero-based axis number(s) or minimal match strings to collapse. [3]_
   - **outfile** (string='') - Name of output CASA image. Must be specified. [4]_
   - **box** (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane. [5]_
   - **region** (string='') - Region selection. Default is to use the full image. [6]_
   - **chans** (string='') - Channels to use. Default is to use all channels. [7]_
   - **stokes** (string='') - Stokes planes to use. Default is to use all Stokes planes. [8]_
   - **mask** (string='') - Mask to use. Default is none. [9]_
   - **stretch** (bool=False) - Stretch the mask if necessary and possible? [11]_







Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Name of the input image
      |                      Default: none
      | 
      |                         Example: imagename='ngc5921.im'
.. [2] 
   **function** (string='')
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
.. [3] 
   **axes** (variant='[0]')
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
.. [4] 
   **outfile** (string='')
      | Name of output CASA image. Must be specified.
      |                      Default: none
      | 
      |                         Example: outfile='collapsed.im'
.. [5] 
   **box** (string='')
      | Rectangular region to select in direction plane. 
      |                      Default: '' (use the entire direction plane)
      | 
      |                         Example: box="100,100,200,200"
.. [6] 
   **region** (string='')
      | Region selection.
      |                      Default: '' (use the full image)
.. [7] 
   **chans** (string='')
      | Channels to use. 
      |                      Default: '' (use all channels)
.. [8] 
   **stokes** (string='')
      | Stokes planes to use.
      |                      Default: '' (use all stokes planes)
.. [9] 
   **mask** (string='')
      | Mask to use.
      |                      Default: none
.. [10] 
   **overwrite** (bool=False)
      | Overwrite output image if it exists?
      |                      Default: False
      |                      Options: False|True
.. [11] 
   **stretch** (bool=False)
      | Stretch the mask if necessary and possible? 
      |                      Default: False
      |                      Options: False|True
      | 
      |                      Stretch the input mask if necessary and
      |                      possible. Only used if a mask is specified.

    """
    pass
