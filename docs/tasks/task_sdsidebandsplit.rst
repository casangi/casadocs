

.. _Description:

Description
   .. warning:: **WARNING**: This task is EXPERIMENTAL. Interface and
      capabilities may change frequently.

   The task **sdsidebandsplit** performs a sideband separation
   operation on data collected by double sideband (DSB) receivers.
   The task splits the emission from the signal and image sidebands
   by utilizing the feature that spectral lines in the two sidebands
   shift in different amounts between observations with different LO
   offsets. The algorithm used in the task is analogous to that of
   Emerson, Klein, & Haslam (1979) [1]_ with shifts in the
   frequency domain instead of spatial one as described in the paper.
   The details of algorithm is also discussed in the section \"Brief
   description of the mathematics behind the
   task\",
   below.

   The task takes two or more images as inputs and is able to
   identify and split the contribution from the signal and image
   sidebands. The resulting output are separate image(s). When the
   parameter *getbothside=False* is set, only the signal sideband is
   solved for and stored as an image. When *getbothside=True*, both
   the signal and image sidebands are obtained and stored separately
   as two images. The name of output image(s) is defined by *outfile*
   and suffixed by '.signalband' and '.imageband' for the signal and
   image sidebands, respectively.

   .. rubric:: How to prepare input images

   This task can only be used with spectral line data and not
   continuum. Therefore input images must be appropriately
   calibrated, for example, by using **sdcal** (and **applycal**),
   and any residual bandpass structure and continuum must be
   subtracted from the spectral line emmission using **sdbaseline**.
   Then an image must be created for each LO offset (e.g.,
   **sdimaging**). The spatial and stokes coordinates must coincide
   with each other in the input images. It is recommended to use the
   frequency setting native to the observation when creating images
   to avoid adding complexity in the definition of the parameters,
   *signalshift* and *imageshift*. The default frequency parameters
   in **sdimaging** (*nchan=-1*, *start=0*, and *width=1*) help to
   avoid in adding this complexity.

   .. rubric:: Definition of *signalshift* and *imageshift*

   Since the input images do not have information on how much the
   frequency is offset in the spectral window in each observation,
   **sdsidebandsplit** relies on user to provide it. Currently, the
   offset in each image should be defined in the unit of channel
   numbers of the image. In the future, the task may support other
   units such as frequency (Hz, MHz, GHz) or velocity (km/s).  The
   parameter, *signalshift*, must be a list of offset channels of the
   signal sideband in corresponding elements of imagename, hence the
   number of elements in signalshift must be equal to that of
   imagename.  The parameter *imageshift* is the same as
   *signalshift* but for the image sideband.

   .. note:: *signalshift* and *imageshift* must be defined in the
      unit of channel numbers in the image. The **sdsidebandsplit**
      task relies on these values to shift back the spectra and
      construct a group of spectra whose signal (or image) sideband
      contribution are aligned. ** ** The solution significantly
      degrades if the values are inaccurate. It is the user's
      responsibility to calculate and provide appropriate numbers of
      shifts especially in case the frequency coordinate of input
      images is different from the native observation, for example by
      regridding and/or by converting frequency frame.

   .. rubric:: Solution flag: *otherside*

   There are two ways to obtain a spectrum of a sideband of interest
   in **sdsidebandsplit**. The parameter *otherside* allows a user to
   switch between the image or signal sideband. When solving for the
   signal (image) sideband with *otherside=False*, spectra are
   shifted back to construct a group of spectra in which the signal
   (image) sideband spectra are static in terms of channel and the
   spectrum of the signal (image) sideband is solved. When
   *otherside=True*, the signal (image) sideband spectrum is obtained
   by solving that of the other, image (signal), sideband and by
   subtracting it from the observed spectrum which contains
   contribution from both sidebands.

   Setting *otherside=True* may have an advantage of removing
   residual offsets in a spectrum. This is because the current
   algorithm does not take into account the sideband ratio and the
   offset component is assigned to the sideband which is originally
   solved. Therefore, solving with *otherside=False* doubles the
   offset components by assigning to both sidebands and breaks the
   conservation of flux between the original and derived spectra.
   This is indeed inappropriate but the capability is now exposed for
   testing purposes. In the future, this should be corrected, for
   example, by accepting the sideband ratio as an input. Note,
   setting *otherside=True* may cause over subtraction. If an
   emission line in a sideband is strong and wide, it causes
   significant ghost emission in the solution of the other sideband.
   When this ghost emission in addition to the offset component is
   subtracted from the original spectrum (*otherside=True*), it may
   cause a negative offset in the derived spectrum.

   .. rubric:: Frequency definition of image sideband

   Since the input images do not have information of the frequency
   settings of the output image of the image sideband,
   **sdsidebandsplit** relies on user inputs when solving for the
   image sideband (*getbothside=True*). The frequency information of
   the image consists of the reference channel in the output image
   (*refpix*) and the frequency at the reference channel (*refval*).
   The frequency increment is defined as the same amount as that of
   signal sideband but with the opposite sign. If the frequency
   increment of the signal sideband is 4880kHz, that of image
   sideband is defined as -4880kHz. See the Examples tab for a sample
   use case showing how to specify *refpix* and *refval*.


   .. rubric:: Brief description of the mathematics behind the task

   The algorithm to split signals from two sidebands is based on the
   following criteria:

   -  The sign of the frequency increment for the image sideband is
      opposite to that for the signal sideband (Note that “signal
      sideband” and “image sideband” are the nominal terms that
      physically correspond to either an upper sideband or a lower
      sideband so if the increment for one sideband is positive, the
      other sideband is negative.)
   -  By shifting the LO frequency, the corresponding sky frequency
      for each spectral channel is shifted accordingly. Because of
      the opposite sign of the frequency increment, the amount of
      shifts in terms of channel occur in opposite directions: if the
      corresponding channel shift in the signal sideband is positive,
      the shift for the image sideband is negative.
   -  In the Fourier (time) domain, the frequency shift is
      represented as a modulation, which is a multiplication of a
      sinusoidal wave whose frequency is equal to the amount of the
      frequency shift.

   Suppose that :math:`h` is an output spectrum of DSB system and
   :math:`f`, :math:`g` represent contributions from signal and image
   sidebands, respectively. Then,

   :math:`h_{m k} = f_{m k} + g_{m k}`, :math:`k=0,1,2,...,N-1`,

   where :math:`k` denotes channel index and :math:`N` is a number
   of spectral channels. If LO frequency shift by x causes
   :math:`f_{m k}` and :math:`g_{m k}` to shift by
   :math:`\Delta^{m x}_{m f}` and :math:`\Delta^{m x}_{m g}`
   with respect to its original spectra, respectively, output
   spectrum with shift is wrtten as,

   :math:`h^{m x}_{m k} = f_{m k - \Delta^x_f} + g_{m k - \Delta^x_g}`.

   We can shift :math:`h^{m x}_{m k}` as if the contribution from
   image sideband, :math:`g`, is being unshifted. By
   shifting :math:`h^{m x}_{m k}`
   by :math:`-\Delta^{m x}_{m g}`, we can construct such
   spectrum,

   :math:`h^{m x,imag}_{m k} = f_{m k - \Delta^x} + g_{m k}`,

   where
   :math:`\Delta^{m x} = \Delta^{m x}_{m f} - \Delta^{m x}_{m g}`.
   Channel shift in the signal sideband is represented as a
   modulation in Fourier (time) domain. Thus, Fourier transform of
   the above is written as,

   :math:`H^{m x,imag}_{m t} = F_{m t} \exp(-i \frac{2\pi t \Delta^{m x}}{N}) + G_{m t}`,

   where :math:`H^{m x,imag}_{m t}`, :math:`F_{m t}`, and
   :math:`G_{m t}` are Fourier transform
   of :math:`h^{m x,imag}_{m k}`, :math:`f_{m k}`, and
   :math:`g_{m k}`, respectively. Applying similar procedure for
   the different LO frequency offset, y, we can obtain another
   result:

   :math:`H^{m y,imag}_{m t} = F_{m t} \exp(-i \frac{2\pi t \Delta^{m y}}{N}) + G_{m t}`.

   we can obtain :math:`G_{m t}`, Fourier transform of the
   contribution from image sideband, :math:`g_{m k}`, from the
   above two results,

   :math:`G_{m t} = \frac{1}{2} (H^{m x,imag}_{m t} + H^{m y,imag}_{m t}) + \frac{1}{2} \frac{\cos\theta}{i\sin\theta} (H^{m x,imag}_{m t} - H^{m y,imag}_{m t})`,

   where
   :math:`\theta = 2\pi t (\Delta^{m x} - \Delta^{m y}) / N`.

   There are two ways to obtain the contribution from signal
   sideband. One is to solve signal sideband exactly same procedure
   with the above. By doing that, we obtain,

   :math:`F_{m t} = \frac{1}{2} (H^{m x,sig}_{m t} + H^{m y,sig}_{m t}) - \frac{1}{2} \frac{\cos\theta}{i\sin\theta} (H^{m x,sig}_{m t} - H^{m y,sig}_{m t})`,

   where the quantity with superscript "sig" corresponds to the
   shifted spectrum so that contribution from the signal sideband
   remain fixed. This is what the **sdsidebandsplit** does
   when *otherside=True*. Another way is to subtract the contribution
   of image sideband from the output spectrum. If *otherside=False*,
   contribution from signal sideband is estimated in that way.

   In principle, the task can split contributions from signal and
   image sidebands if only two images with different LO shifts are
   given. However, the task accepts more than two images to obtain
   better result. If :math:`m` images are given and all images are
   based on independent LO shifts, there are :math:`m(m-1)/2`
   combinations to obtain the solution of splitted spectra. In that
   case, the task takes average of those solutions to get a final
   solution.

   Note that, when :math:`\Delta^{m x}` and :math:`\Delta^{m y}`
   are so close that :math:`\theta` becomes almost zero, the above
   solution could diverge. Such a solution must be avoided to obtain
   a finite result. The parameter *threshold* is introduced for this
   purpose. It should range from 0.0 to 1.0.  The solution will be
   excluded from the process if :math:`|\sin(\theta)|` is less than
   *threshold*.


   .. rubric:: Bibliography

   .. [1] Emerson, Klein, & Haslam 1979, A&A, 76, 92 `ADS <http://adsabs.harvard.edu/abs/1979A%26A....76...92E>`__


.. _Examples:

Examples
   Obtain an image of signal sideband (side band supression):

   ::

      sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image',
                      'shift_neg81ch.image'], outfile='separated.image',
                      signalshift=[0.0, +132.0, -81.0],
                      imageshift=[0.0, -132.0, +81.0])

   The output image is 'separated.image.signalband'.

   To solve both signal and image sidebands, set frequency of image
   sideband explicitly in addtion to *getbothside=True*.

   ::

      sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image',
                      'shift_neg81ch.image'], outfile='separated.image',
                      signalshift=[0.0, +132.0, -81.0],
                      imageshift=[0.0, -132.0, +81.0], getbothside=True,
                      refpix=0.0, refval='805.8869GHz')

   The output images are 'separated.image.signalband' and
   'separated.image.imageband' for signal and image sideband,
   respectively.

   To obtain signal sideband image by solving image sideband, set
   *otherside=True*:

   ::

      sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image',
                      'shift_neg81ch.image'], outfile='separated.image',
                      signalshift=[0.0, +132.0, -81.0],
                      imageshift=[0.0, -132.0, +81.0], otherside=True)

   Solution of image sideband is obtained and subtracted from the
   original (double sideband) spectra to derive spectra of signal
   sideband. The output image is 'separated.image.signalband'.


.. _Development:

Development
   No additional development details

