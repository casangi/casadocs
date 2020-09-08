#
# stub function definition file for docstring parsing
#

def impbcor(imagename, pbimage='""', outfile='', overwrite=False, box='', region='', chans='', stokes='', mask='', mode='divide', cutoff=-1.0, stretch=False):
    r"""
Construct a primary beam corrected image from an image and a primary beam pattern.

Parameters
   - imagename_ (string) - Name of the input image
   - pbimage_ (variant='""') - Name of the primary beam image which must exist or array of values for the pb response.
   - outfile_ (string='') - Output image name. If empty, no image is written.
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - region_ (variant='') - Region selection.
   - chans_ (string='') - Channels to use.
   - stokes_ (string='') - Stokes planes to use.
   - mask_ (string='') - Mask to use.
   - mode_ (string='divide') - Divide or multiply the image by the primary beam image. Minimal match supported.
   - cutoff_ (double=-1.0) - PB cutoff. If mode is "d", all values less than this will be masked. If "m", all values greater will be masked. Less than 0, no cutoff.


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

.. _imagename:

   .. rubric:: imagename

   | Name of the input (CASA, FITS, MIRIAD) image

.. _pbimage:

   .. rubric:: pbimage

   | Name of the image (CASA, FITS, MIRIAD) of the primary
   | beam pattern or an array of pixel values.
   |                      Default: ''

.. _outfile:

   .. rubric:: outfile

   | Name of output CASA image. 
   |                      Default: none. Must be specified.

.. _overwrite:

   .. rubric:: overwrite

   | If output file is specified, controls if an already
   | existing file by the same name can be overwritten. 
   |                      Default: True
   |                      Options: True|False
   | 
   |                      If true, the user is not prompted, the file if it
   |                      exists is automatically overwritten.

.. _box:

   .. rubric:: box

   | Rectangular region to select in direction plane.
   |                      Default: '' (use the entire direction plane)

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
   |                      Default: '' (use all Stokes planes)

.. _mask:

   .. rubric:: mask

   | Mask to use.
   |                      Default: none

.. _mode:

   .. rubric:: mode

   | Divide or multiply the image by the primary beam image. 
   |                      Default: 'divide'
   | 
   |                      Minimal match supported.

.. _cutoff:

   .. rubric:: cutoff

   | Primary beam cutoff.
   |                      Default: -1.0 (no cutoff)
   | 
   |                      If mode is "d", all values less than this will be
   |                      masked. If "m", all values greater will be
   |                      masked. Less than 0, no cutoff (default)

.. _stretch:

   .. rubric:: stretch

   | Stretch the mask if necessary and possible? 
   |                      Default: False
   |                      Options: False|True


    """
    pass
