#
# stub function definition file for docstring parsing
#

def imsmooth(imagename, kernel='gauss', major='', minor='', pa='', targetres=False, kimage='', scale=-1.0, region='', box='', chans='', stokes='', mask='', outfile='', stretch=False, overwrite=False, beam=''):
    r"""
Smooth an image or portion of an image

Parameters
   - imagename_ (string) - Name of the input image. Must be specified.
   - kernel_ (string='gauss') - Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel.

      .. raw:: html

         <details><summary><i> kernel = gauss </i></summary>

      - beam_ (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.
      - targetres_ (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
      - major_ (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - minor_ (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
      - pa_ (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = gaussian </i></summary>

      - beam_ (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.
      - targetres_ (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
      - major_ (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - minor_ (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
      - pa_ (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = g </i></summary>

      - beam_ (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.
      - targetres_ (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
      - major_ (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - minor_ (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
      - pa_ (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = box </i></summary>

      - major_ (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - minor_ (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = boxcar </i></summary>

      - major_ (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - minor_ (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = b </i></summary>

      - major_ (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - minor_ (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = image </i></summary>

      - kimage_ (string='') - Kernel image name. Only used if kernel="i" or "image".
      - scale_ (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = i </i></summary>

      - kimage_ (string='') - Kernel image name. Only used if kernel="i" or "image".
      - scale_ (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".

      .. raw:: html

         </details>
   - major_ (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
   - minor_ (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
   - pa_ (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.
   - targetres_ (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
   - kimage_ (string='') - Kernel image name. Only used if kernel="i" or "image".
   - scale_ (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".
   - region_ (variant='') - Region selection. Default is to use the full image.
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - mask_ (string='') - Mask to use. Default is none.
   - outfile_ (string='') - Output image name. Must be specified.
   - overwrite_ (bool=False) - If true, overwrite (unprompted) pre-existing output file.
   - beam_ (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.







Details
   Explanation of each parameter

.. _imagename:

   .. rubric:: imagename

   | Name of the input image. Must be specified.

.. _kernel:

   .. rubric:: kernel

   | Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel.

.. _major:

   .. rubric:: major

   | Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".

.. _minor:

   .. rubric:: minor

   | Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".

.. _pa:

   .. rubric:: pa

   | Position angle used only for gaussian kernel. Standard quantity representation.

.. _targetres:

   .. rubric:: targetres

   | If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).

.. _kimage:

   .. rubric:: kimage

   | Kernel image name. Only used if kernel="i" or "image".

.. _scale:

   .. rubric:: scale

   | Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".

.. _region:

   .. rubric:: region

   | Region selection. Default is to use the full image.

.. _box:

   .. rubric:: box

   | Rectangular region to select in direction plane. Default is to use the entire direction plane.

.. _chans:

   .. rubric:: chans

   | Channels to use. Default is to use all channels.

.. _stokes:

   .. rubric:: stokes

   | Stokes planes to use. Default is to use all Stokes planes.

.. _mask:

   .. rubric:: mask

   | Mask to use. Default is none.

.. _outfile:

   .. rubric:: outfile

   | Output image name. Must be specified.

.. _stretch:

   .. rubric:: stretch

   | If true, stretch the mask if necessary and possible.

.. _overwrite:

   .. rubric:: overwrite

   | If true, overwrite (unprompted) pre-existing output file.

.. _beam:

   .. rubric:: beam

   | Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.


    """
    pass
