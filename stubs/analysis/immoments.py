#
# stub function definition file for docstring parsing
#

def immoments(imagename, moments=[0], axis='spectral', region='', box='', chans='', stokes='', mask='', includepix=-1, excludepix=-1, outfile='', stretch=False):
    r"""
Compute moments from an image

Parameters
   - imagename_ (string) - Name of the input image
   - moments_ (intArray=[0]) - List of moments you would like to compute
   - axis_ ({string, int}='spectral') - The momement axis: ra, dec, lat, long, spectral, or stokes
   - region_ ({string, stringArray}='') - Region selection. Default is to use the full image.
   - box_ (string='') - Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - mask_ (variant='') - Mask to use. Default is none.
   - includepix_ ({int, doubleArray, intArray}=-1) - Range of pixel values to include
   - excludepix_ ({int, doubleArray, intArray}=-1) - Range of pixel values to exclude
   - outfile_ (string='') - Output image file name (or root for multiple moments) 


Description
   The spectral moment distributions at each pixel are
   determined.The main control of the calculation is given by the
   parameter *moments*:

   -  moments = -1 - mean value of the spectrum
   -  moments = 0 - integrated value of the spectrum
   -  moments = 1 - intensity weighted coordinate; traditionally
      used to get "velocity fields"
   -  moments = 2 - intensity weighted dispersion of the coordinate;
      traditionally used to get "velocity dispersion"
   -  moments = 3 - median value of the spectrum
   -  moments = 4 - median coordinate
   -  moments = 5 - standard deviation about the mean of the
      spectrum
   -  moments = 6 - root mean square of the spectrum
   -  moments = 7 - absolute mean deviation of the spectrum
   -  moments = 8 - maximum value of the spectrum
   -  moments = 9 - coordinate of the maximum value of the spectrum
   -  moments = 10 - minimum value of the spectrum
   -  moments = 11 - coordinate of the minimum value of the spectrum

   The default value of *outfile* is the input image name appended by
   an auto-determined suffix.

   If *stretch=True* and if the number of mask dimensions is less
   than or equal to the number of image dimensions and some axes in
   the mask are degenerate while the corresponding axes in the image
   are not, the mask will be stetched in the degenerate axis
   dimensions. For example, if the input image has shape [100, 200,
   10] and the input mask has shape [100, 200, 1] and *stretch=True*,
   the mask will be stretched along the third dimension to shape
   [100, 200, 10]. However if the mask is shape [100, 200, 2],
   stretching is not possible and an error will result.

   If an image has multiple per-channel beams and the moment axis is
   equal to the spectral axis, each channel will be convolved with a
   beam that has a minimum area necessary to contain each of the
   image beams, ie, it is the minimum area common beam to which all
   the beams in the image can be convolved.

   

   .. rubric:: Task-specific parameter summary
      

   .. rubric:: *moments*
      

   List of moments to compute. See above for details.

   .. rubric:: *axis*
      

   Axis along which to compute the specified moments.

   .. rubric:: *includepix*
      

   Range of pixel values to include in the computation. A range can
   only be given for one of includepix or excludepix.

   .. rubric:: *excludepix*
      

   Range of pixel values to exclude in the computation. A range can
   only be given for one of includepix or excludepix.




Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Name of the input image

.. _moments:

   .. rubric:: moments

   | List of moments you would like to compute

.. _axis:

   .. rubric:: axis

   | The momement axis: ra, dec, lat, long, spectral, or stokes

.. _region:

   .. rubric:: region

   | Region selection. Default is to use the full image.

.. _box:

   .. rubric:: box

   | Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.

.. _chans:

   .. rubric:: chans

   | Channels to use. Default is to use all channels.

.. _stokes:

   .. rubric:: stokes

   | Stokes planes to use. Default is to use all Stokes planes.

.. _mask:

   .. rubric:: mask

   | Mask to use. Default is none.

.. _includepix:

   .. rubric:: includepix

   | Range of pixel values to include

.. _excludepix:

   .. rubric:: excludepix

   | Range of pixel values to exclude

.. _outfile:

   .. rubric:: outfile

   | Output image file name (or root for multiple moments)

.. _stretch:

   .. rubric:: stretch

   | Stretch the mask if necessary and possible?


    """
    pass
