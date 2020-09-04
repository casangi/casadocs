#
# stub function definition file for docstring parsing
#

def immoments(imagename, moments=[0], axis='spectral', region='', box='', chans='', stokes='', mask='', includepix=-1, excludepix=-1, outfile='', stretch=False):
    r"""
Compute moments from an image

Parameters
   - **imagename** (string) - Name of the input image [1]_
   - **moments** (intArray=[0]) - List of moments you would like to compute [2]_
   - **axis** ({string, int}='spectral') - The momement axis: ra, dec, lat, long, spectral, or stokes [3]_
   - **region** ({string, stringArray}='') - Region selection. Default is to use the full image. [4]_
   - **box** (string='') - Rectangular region(s) to select in direction plane. Default is to use the entire direction plane. [5]_
   - **chans** (string='') - Channels to use. Default is to use all channels. [6]_
   - **stokes** (string='') - Stokes planes to use. Default is to use all Stokes planes. [7]_
   - **mask** (variant='') - Mask to use. Default is none. [8]_
   - **includepix** ({int, doubleArray, intArray}=-1) - Range of pixel values to include [9]_
   - **excludepix** ({int, doubleArray, intArray}=-1) - Range of pixel values to exclude [10]_
   - **outfile** (string='') - Output image file name (or root for multiple moments)  [11]_


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

.. [1] 
   **imagename** (string)
      | Name of the input image
.. [2] 
   **moments** (intArray=[0])
      | List of moments you would like to compute
.. [3] 
   **axis** ({string, int}='spectral')
      | The momement axis: ra, dec, lat, long, spectral, or stokes
.. [4] 
   **region** ({string, stringArray}='')
      | Region selection. Default is to use the full image.
.. [5] 
   **box** (string='')
      | Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
.. [6] 
   **chans** (string='')
      | Channels to use. Default is to use all channels.
.. [7] 
   **stokes** (string='')
      | Stokes planes to use. Default is to use all Stokes planes.
.. [8] 
   **mask** (variant='')
      | Mask to use. Default is none.
.. [9] 
   **includepix** ({int, doubleArray, intArray}=-1)
      | Range of pixel values to include
.. [10] 
   **excludepix** ({int, doubleArray, intArray}=-1)
      | Range of pixel values to exclude
.. [11] 
   **outfile** (string='')
      | Output image file name (or root for multiple moments)
.. [12] 
   **stretch** (bool=False)
      | Stretch the mask if necessary and possible?

    """
    pass
