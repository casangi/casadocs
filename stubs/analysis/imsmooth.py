#
# stub function definition file for docstring parsing
#

def imsmooth(imagename, kernel='gauss', major='', minor='', pa='', targetres=False, kimage='', scale=-1.0, region='', box='', chans='', stokes='', mask='', outfile='', stretch=False, overwrite=False, beam=''):
    r"""
Smooth an image or portion of an image

Parameters
   - **imagename** (string) - Name of the input image. Must be specified. [1]_
   - **kernel** (string='gauss') - Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel. [2]_

      .. raw:: html

         <details><summary><i> kernel = gauss </i></summary>

      - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa. [17]_
      - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False). [6]_
      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". [3]_
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". [4]_
      - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation. [5]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = gaussian </i></summary>

      - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa. [17]_
      - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False). [6]_
      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". [3]_
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". [4]_
      - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation. [5]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = g </i></summary>

      - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa. [17]_
      - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False). [6]_
      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". [3]_
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". [4]_
      - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation. [5]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = box </i></summary>

      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". [3]_
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". [4]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = boxcar </i></summary>

      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". [3]_
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". [4]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = b </i></summary>

      - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". [3]_
      - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". [4]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = image </i></summary>

      - **kimage** (string='') - Kernel image name. Only used if kernel="i" or "image". [7]_
      - **scale** (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image". [8]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> kernel = i </i></summary>

      - **kimage** (string='') - Kernel image name. Only used if kernel="i" or "image". [7]_
      - **scale** (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image". [8]_

      .. raw:: html

         </details>
   - **major** (variant='') - Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar". [3]_
   - **minor** (variant='') - Minor axis. Standard quantity representation. Must be specified for kernel="boxcar". [4]_
   - **pa** (variant='') - Position angle used only for gaussian kernel. Standard quantity representation. [5]_
   - **targetres** (bool=False) - If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False). [6]_
   - **kimage** (string='') - Kernel image name. Only used if kernel="i" or "image". [7]_
   - **scale** (double=-1.0) - Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image". [8]_
   - **region** (variant='') - Region selection. Default is to use the full image. [9]_
   - **box** (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane. [10]_
   - **chans** (string='') - Channels to use. Default is to use all channels. [11]_
   - **stokes** (string='') - Stokes planes to use. Default is to use all Stokes planes. [12]_
   - **mask** (string='') - Mask to use. Default is none. [13]_
   - **outfile** (string='') - Output image name. Must be specified. [14]_
   - **overwrite** (bool=False) - If true, overwrite (unprompted) pre-existing output file. [16]_
   - **beam** (variant='') - Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa. [17]_







Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Name of the input image. Must be specified.
.. [2] 
   **kernel** (string='gauss')
      | Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel.
.. [3] 
   **major** (variant='')
      | Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
.. [4] 
   **minor** (variant='')
      | Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
.. [5] 
   **pa** (variant='')
      | Position angle used only for gaussian kernel. Standard quantity representation.
.. [6] 
   **targetres** (bool=False)
      | If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
.. [7] 
   **kimage** (string='')
      | Kernel image name. Only used if kernel="i" or "image".
.. [8] 
   **scale** (double=-1.0)
      | Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".
.. [9] 
   **region** (variant='')
      | Region selection. Default is to use the full image.
.. [10] 
   **box** (string='')
      | Rectangular region to select in direction plane. Default is to use the entire direction plane.
.. [11] 
   **chans** (string='')
      | Channels to use. Default is to use all channels.
.. [12] 
   **stokes** (string='')
      | Stokes planes to use. Default is to use all Stokes planes.
.. [13] 
   **mask** (string='')
      | Mask to use. Default is none.
.. [14] 
   **outfile** (string='')
      | Output image name. Must be specified.
.. [15] 
   **stretch** (bool=False)
      | If true, stretch the mask if necessary and possible.
.. [16] 
   **overwrite** (bool=False)
      | If true, overwrite (unprompted) pre-existing output file.
.. [17] 
   **beam** (variant='')
      | Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.

    """
    pass
