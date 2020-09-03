#
# stub function definition file for docstring parsing
#

def imsmooth(imagename, kernel='gauss', major='', minor='', pa='', targetres=False, kimage='', scale=-1.0, region='', box='', chans='', stokes='', mask='', outfile='', stretch=False, overwrite=False, beam=''):
    r"""
Smooth an image or portion of an image

Parameters
   - **imagename** (string) - Name of the input image. Must be specified.
   - **kernel** (string='gauss') - Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel.

      .. raw:: html

         <details><summary><i> kernel = gauss </i></summary>

      - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.
      - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
      - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = gaussian </i></summary>

      - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.
      - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
      - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = g </i></summary>

      - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.
      - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
      - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = box </i></summary>

      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = boxcar </i></summary>

      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = b </i></summary>

      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = image </i></summary>

      - **kimage** (string='') - Kernel image name. Only used if kernel="i" or "image".
      - **scale** (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = i </i></summary>

      - **kimage** (string='') - Kernel image name. Only used if kernel="i" or "image".
      - **scale** (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".

      .. raw:: html

         </details>
   - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
   - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
   - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation.
   - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
   - **kimage** (string='') - Kernel image name. Only used if kernel="i" or "image".
   - **scale** (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".
   - **region** (variant='') - Region selection. Default is to use the full image.
   - **box** (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - **chans** (string='') - Channels to use. Default is to use all channels.
   - **stokes** (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - **mask** (string='') - Mask to use. Default is none.
   - **outfile** (string='') - Output image name. Must be specified.
   - **overwrite** (bool=False) - If true, overwrite (unprompted) pre-existing output file.
   - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.




    """
    pass
