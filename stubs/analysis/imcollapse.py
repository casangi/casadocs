#
# stub function definition file for docstring parsing
#

def imcollapse(imagename, function='', axes='[0]', outfile='', box='', region='', chans='', stokes='', mask='', overwrite=False, stretch=False):
    r"""
Collapse image along one axis, aggregating pixel values along that axis.

Parameters
   - **imagename** (string) - Name of the input image
   - **function** (string='') - Aggregate function to apply. This can be set one of flux, madm, max, mean, median, min, npts, rms, stddev, sum, variance, xmadm. Must be specified.
   - **axes** (variant='[0]') - Zero-based axis number(s) or minimal match strings to collapse.
   - **outfile** (string='') - Name of output CASA image. Must be specified.
   - **box** (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - **region** (string='') - Region selection. Default is to use the full image.
   - **chans** (string='') - Channels to use. Default is to use all channels.
   - **stokes** (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - **mask** (string='') - Mask to use. Default is none.
   - **stretch** (bool=False) - Stretch the mask if necessary and possible?




    """
    pass
