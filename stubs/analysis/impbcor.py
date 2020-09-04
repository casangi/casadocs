#
# stub function definition file for docstring parsing
#

def impbcor(imagename, pbimage='""', outfile='', overwrite=False, box='', region='', chans='', stokes='', mask='', mode='divide', cutoff=-1.0, stretch=False):
    r"""
Construct a primary beam corrected image from an image and a primary beam pattern.

Parameters
   - **imagename** (string) - Name of the input image [1]_
   - **pbimage** (variant='""') - Name of the primary beam image which must exist or array of values for the pb response. [2]_
   - **outfile** (string='') - Output image name. If empty, no image is written. [3]_
   - **box** (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane. [5]_
   - **region** (variant='') - Region selection. [6]_
   - **chans** (string='') - Channels to use. [7]_
   - **stokes** (string='') - Stokes planes to use. [8]_
   - **mask** (string='') - Mask to use. [9]_
   - **mode** (string='divide') - Divide or multiply the image by the primary beam image. Minimal match supported. [10]_
   - **cutoff** (double=-1.0) - PB cutoff. If mode is "d", all values less than this will be masked. If "m", all values greater will be masked. Less than 0, no cutoff. [11]_


Description
   Corrects an image for primary beam attenuation using an image of
   the primary beam pattern. The primary beam pattern can be provided
   as an image, in which case:

   #. it must have the same shape as the input image and its
      coordinate system must be the same, or
   #. it must be a 2-D image in which case its coordinate system must
      consist of a (2-D) direction coordinate which is the same as
      the direction coordinate in the input image and its direction
      plane must be the same shape as that of the input image.

   Alternatively, *pbimage* can be an array of pixel values in which
   case the same dimensionality and shape constraints apply.

   One can choose between dividing the image by the primary beam
   pattern (*mode="divide"*) or multiplying the image by the primary
   beam pattern (*mode="multiply"*). One can also choose to specify a
   cutoff limit for the primary beam pattern. For *mode="divide"*,
   for all pixels below this cutoff in the primary beam pattern, the
   output image will be masked. In the case of *mode="multiply"*, all
   pixels in the output will be masked corresponding to pixels with
   values greater than the cutoff in the primary beam pattern. A
   negative value for cutoff means that no cutoff will be applied,
   which is the default.




Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Name of the input (CASA, FITS, MIRIAD) image
.. [2] 
   **pbimage** (variant='""')
      | Name of the image (CASA, FITS, MIRIAD) of the primary
      | beam pattern or an array of pixel values.
      |                      Default: ''
.. [3] 
   **outfile** (string='')
      | Name of output CASA image. 
      |                      Default: none. Must be specified.
.. [4] 
   **overwrite** (bool=False)
      | If output file is specified, controls if an already
      | existing file by the same name can be overwritten. 
      |                      Default: True
      |                      Options: True|False
      | 
      |                      If true, the user is not prompted, the file if it
      |                      exists is automatically overwritten.
.. [5] 
   **box** (string='')
      | Rectangular region to select in direction plane.
      |                      Default: '' (use the entire direction plane)
.. [6] 
   **region** (variant='')
      | Region selection. 
      |                      Default: '' (use the full image)
.. [7] 
   **chans** (string='')
      | Channels to use. 
      |                      Default: '' (use all channels)
.. [8] 
   **stokes** (string='')
      | Stokes planes to use.
      |                      Default: '' (use all Stokes planes)
.. [9] 
   **mask** (string='')
      | Mask to use.
      |                      Default: none
.. [10] 
   **mode** (string='divide')
      | Divide or multiply the image by the primary beam image. 
      |                      Default: 'divide'
      | 
      |                      Minimal match supported.
.. [11] 
   **cutoff** (double=-1.0)
      | Primary beam cutoff.
      |                      Default: -1.0 (no cutoff)
      | 
      |                      If mode is "d", all values less than this will be
      |                      masked. If "m", all values greater will be
      |                      masked. Less than 0, no cutoff (default)
.. [12] 
   **stretch** (bool=False)
      | Stretch the mask if necessary and possible? 
      |                      Default: False
      |                      Options: False|True

    """
    pass
