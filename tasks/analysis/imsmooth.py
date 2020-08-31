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


Description
      This task performs a Fourier-based convolution to 'smooth' the
      direction plane of an image. Smoothing is typically performed in
      order to reduce the noise in an image.

      | A deconvolved image :math:`\bf{I}` can be smoothed to a target
        resolution by convolving it with a `Gaussian
        beam <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/definition_synthesized_beam>`__
        :math:`\bf{B}_{\rm tar}`. If the image is already convolved with
        another smaller beam :math:`\bf{B}_{\rm cur}` a correcting beam 
        :math:`\bf{B}_{\rm cor}` can be calculated so that
      | 

        .. math:: \begin{align} \bf{B}_{\rm tar} * \bf{I} = \bf{B}_{\rm cor} * (\bf{B}_{\rm cur} * \bf{I}),  \end{align}
      | where :math:`*` is the convolution operator.  The Fourier
        transform of the above equation is
      | 

        .. math:: \begin{align} \bf{B}_{\rm tar}^f  \bf{I}^f = \bf{B}_{\rm cor}^f  (\bf{B}_{\rm cur}^f  \bf{I}^f), \end{align}
      | where the superscript :math:`f` indicates the Fourier transform.
        The correcting beam can then be obtained by
      | 

        .. math:: \begin{align} \bf{B}_{\rm cor} = \mathcal{F}^{-1} \left( \frac{\bf{B}_{\rm tar}^f}{\bf{B}_{\rm cur}^f} \right). \end{align}

       

      Below we provide details of how the task imsmooth implements this
      concept.

      .. rubric::  
         :name: section

      .. rubric:: Gaussian Kernel
         :name: gaussian-kernel

      The direction pixels must be square. If they are not, use imregrid
      to regrid your image onto a grid of square pixels.

      Under the hood, **ia.convolve2d()** is called with *scale=-1*
      (auto scaling). This means that, when the input image has a
      restoring beam, pixel values in the output image are scaled in
      such a way as to conserve flux density.

      *major* and *minor* are the full width at half maximum (FWHM) of
      the Gaussian. *pa* is the position angle of the Gaussian.

      The beam parameter offers an alternate way of describing the
      convolving Gaussian. If used, neither *major*, *minor*, nor *pa*
      can be specified. The beam parameter must have exactly three
      fields: "*major*", "*minor*", and "*pa*" (or "positionangle");
      this is the record format for the output of
      **ia.restoringbeam()**. For example: 

      beam = {"major": "5arcsec", "minor": "2arcsec", "pa": "20deg"} 

      If both beam and any of *major*, *minor*, and/or *pa* are
      specified for a Gaussian kernel, an exception will be thrown.

      Alternatively, if the input image has multiple beams, setting
      *kernel='commonbeam'* will result in the smallest area beam that
      encloses all beams in the image to be used as the target
      resolution to which to convolve all planes.

      In addition, the *targetres* parameter indicates if the specified
      Gaussian is to be the resolution of the final image (*True*) or if
      it is to be used to convolve the input image (*False*). If *True*,
      the input image must have a restoring beam. Use **imhead()** or
      **ia.restoringbeam()** to check for its existence. If the image
      has multiple beams and *targetres=True* **,** all planes in the
      image will be convolved so that the resulting resolution is that
      specified by the kernel parameters. If the image has multiple
      beams and *targetres=False*, each plane will be convolved with a
      Gaussian specified by beam (and hence, in general, the output
      image will also have multiple beams that vary with spectral
      channel and/or polarization).

      If the units on the original image include Jy/beam, the units on
      the output image will be rescaled by the ratio of the input and
      output beams as well as rescaling by the area of convolution
      kernel in order to conserve flux density.

      If the units on the original image include K, then only the image
      convolution kernel rescaling is done.

      .. rubric:: Boxcar Kernel
         :name: boxcar-kernel

      *major* is the length of the box along the y-axis, and *minor* is
      length of the box along the x-axis. *pa* is not used and beam
      should not be specified. The value of *targetres* is not used.

      .. rubric:: General
         :name: general

      The *major, minor,* and *pa* parameters can be specified in one of
      three ways:

      #. Quantity -- for example *major=qa.quantity(1, 'arcsec')*. Note
         that you can use pixel units, such as *major=qa.quantity(1,
         'pix')*.
      #. String -- for example *minor='1pix'* or *major='0.5arcsec*
         (i.e. a string that the Quanta quantity function accepts).
      #. Numeric -- for example *major=10*. In this case, the units of
         *major* and *minor* are assumed to be in arcsec and units of
         *pa* are assumed to be degrees.

      Note: Using pixel units allows you to convolve axes with different
      units.

      .. rubric:: Image Kernel
         :name: image-kernel

      If *kernel="i"* or *"image"*, the image specified by *kimage* is
      used to convolve the input image. The coordinate system of the
      convolution image is ignored; only the pixel values are
      considered.

      Fourier-based convolution is performed.

      The provided kernel can have fewer dimensions than the image being
      convolved. In this case, it will be padded with degenerate axes.
      An error will result if the kernel has more dimensions than the
      image.

      The scaling of the output image is determined by the *scale*
      parameter. If this is left unset, then the kernel is normalized to
      unit sum. If *scale* is not left unset, then the convolution
      kernel will be scaled (multiplied) by this value.

      Masked pixels will be assigned the value 0.0 before convolution.

      The output mask is the intersection (logical AND) of the default
      input image pixel mask (if any) and the OTF mask. Any other input
      pixel masks will not be copied. The function **ia.maskhandler()**
      should be used if there is a need to copy other masks too.

    """
    pass
