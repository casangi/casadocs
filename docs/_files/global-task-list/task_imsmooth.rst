.. container::
   :name: viewlet-above-content-title

imsmooth
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   imsmooth task: Smooth an image or portion of an image

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This task performs a Fourier-based convolution to 'smooth' the
      direction plane of an image. Smoothing is typically performed in
      order to reduce the noise in an image.

      | A deconvolved image I\ :math:`\bf{I}` can be smoothed to a
        target resolution by convolving it with a `Gaussian
        beam <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/definition_synthesized_beam>`__
        Btar\ :math:`\bf{B}_{\rm tar}`. If the image is already
        convolved with another smaller beam
        Bcur\ :math:`\bf{B}_{\rm cur}` a correcting beam 
        Bcor\ :math:`\bf{B}_{\rm cor}` can be calculated so that
      | Btar∗I=Bcor∗(Bcur∗I),\ 

        .. math:: \begin{align} \bf{B}_{\rm tar} * \bf{I} = \bf{B}_{\rm cor} * (\bf{B}_{\rm cur} * \bf{I}),  \end{align}
      | where ∗\ :math:`*` is the convolution operator.  The Fourier
        transform of the above equation is
      | BftarIf=Bfcor(BfcurIf),\ 

        .. math:: \begin{align} \bf{B}_{\rm tar}^f  \bf{I}^f = \bf{B}_{\rm cor}^f  (\bf{B}_{\rm cur}^f  \bf{I}^f), \end{align}
      | where the superscript f\ :math:`f` indicates the Fourier
        transform. The correcting beam can then be obtained by
      | Bcor=F−1(BftarBfcur).\ 

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

      If both beam and any of *major*, *minor*, and/or *pa* are
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
      has multiple beams and *targetres=True*\ **,** all planes in the
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

       

       

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   task_imsmooth/about
   task_imsmooth/parameters
   task_imsmooth/changelog
   task_imsmooth/examples
   task_imsmooth/developer