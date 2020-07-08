.. container::
   :name: viewlet-above-content-title

sdsidebandsplit
===============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Perform sideband separation using FFT

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary
         :name: summary

      .. container:: alert-box

         **WARNING**: This task is EXPERIMENTAL. Interface and
         capabilities may change frequently.

      The task **sdsidebandsplit** performs a sideband separation
      operation on data collected by double sideband (DSB) receivers.
      The task splits the emission from the signal and image sidebands
      by utilizing the feature that spectral lines in the two sidebands
      shift in different amounts between observations with different LO
      offsets. The algorithm used in the task is analogous to that of
      Emerson, Klein, & Haslam (1979) `[1] <#cit1>`__ with shifts in the
      frequency domain instead of spatial one as described in the paper.
      The details of algorithm is also discussed in the section, `Brief
      description of the mathematics behind the
      task <#brief-description-of-the-mathematics-behind-the-task>`__,
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
         :name: how-to-prepare-input-images

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

      .. rubric:: Definition of *signalshift* and *imageshift*
         :name: definition-of-signalshift-and-imageshift

      Since the input images do not have information on how much the
      frequency is offset in the spectral window in each observation,
      **sdsidebandsplit** relies on user to provide it. Currently, the
      offset in each image should be defined in the unit of channel
      numbers of the image. In the future, the task may support other
      units such as frequency (Hz, MHz, GHz) or velocity (km/s).  The
      parameter, *signalshift*, must be a list of offset channels of the
      signal sideband in corresponding elements of imagename, hence the
      number of elements in signalshift must be equal to that of
      imagename.  The parameter *imageshift* is the same as
      *signalshift* but for the image sideband.

      .. container:: info-box

         **NOTE**: *signalshift* and *imageshift* must be defined in the
         unit of channel numbers in the image. The **sdsidebandsplit**
         task relies on these values to shift back the spectra and
         construct a group of spectra whose signal (or image) sideband
         contribution are aligned.\ ** ** The solution significantly
         degrades if the values are inaccurate. It is the user's
         responsibility to calculate and provide appropriate numbers of
         shifts especially in case the frequency coordinate of input
         images is different from the native observation, for example by
         regridding and/or by converting frequency frame.

      .. rubric:: Solution flag: *otherside*
         :name: solution-flag-otherside

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
         :name: frequency-definition-of-image-sideband

      Since the input images do not have information of the frequency
      settings of the output image of the image sideband,
      **sdsidebandsplit** relies on user inputs when solving for the
      image sideband (*getbothside=True*). The frequency information of
      the image consists of the reference channel in the output image
      (*refpix*) and the frequency at the reference channel (*refval*).
      The frequency increment is defined as the same amount as that of
      signal sideband but with the opposite sign. If the frequency
      increment of the signal sideband is 4880kHz, that of image
      sideband is defined as -4880kHz. See the Examples tab for a sample
      use case showing how to specify *refpix* and *refval*.

       

      .. rubric:: Brief description of the mathematics behind the task
         :name: brief-description-of-the-mathematics-behind-the-task

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

      Suppose that h\ :math:`h` is an output spectrum of DSB system and
      f\ :math:`f`, g\ :math:`g` represent contributions from signal and
      image sidebands, respectively. Then, 

      hk=fk+gk\ :math:`h_{\rm k} = f_{\rm k} + g_{\rm k}`,  
       k=0,1,2,...,N−1\ :math:`k=0,1,2,...,N-1`,

      where k\ :math:`k` denotes channel index and N\ :math:`N` is a
      number of spectral channels. If LO frequency shift by x causes
      fk\ :math:`f_{\rm k}` and gk\ :math:`g_{\rm k}` to shift by
      Δxf\ :math:`\Delta^{\rm x}_{\rm f}` and
      Δxg\ :math:`\Delta^{\rm x}_{\rm g}` with respect to its original
      spectra, respectively, output spectrum with shift is wrtten as,

      hxk=fk−Δxf+gk−Δxg\ :math:`h^{\rm x}_{\rm k} = f_{\rm k - \Delta^x_f} + g_{\rm k - \Delta^x_g}`.

      We can shift hxk\ :math:`h^{\rm x}_{\rm k}` as if the contribution
      from image sideband, g\ :math:`g`, is being unshifted. By
      shifting hxk\ :math:`h^{\rm x}_{\rm k}`
      by −Δxg\ :math:`-\Delta^{\rm x}_{\rm g}`, we can construct such
      spectrum,

      hx,imagk=fk−Δx+gk\ :math:`h^{\rm x,imag}_{\rm k} = f_{\rm k - \Delta^x} + g_{\rm k}`,

      where
      Δx=Δxf−Δxg\ :math:`\Delta^{\rm x} = \Delta^{\rm x}_{\rm f} - \Delta^{\rm x}_{\rm g}`.
      Channel shift in the signal sideband is represented as a
      modulation in Fourier (time) domain. Thus, Fourier transform of
      the above is written as,

      Hx,imagt=Ftexp(−i2πtΔxN)+Gt\ :math:`H^{\rm x,imag}_{\rm t} = F_{\rm t} \exp(-i\frac{2\pi t \Delta^{\rm x}}{N}) + G_{\rm t}`,

      where Hx,imagt\ :math:`H^{\rm x,imag}_{\rm t}`,
      Ft\ :math:`F_{\rm t}`, and Gt\ :math:`G_{\rm t}` are Fourier
      transform of hx,imagk\ :math:`h^{\rm x,imag}_{\rm k}`,
      fk\ :math:`f_{\rm k}`, and gk\ :math:`g_{\rm k}`, respectively.
      Applying similar procedure for the different LO frequency offset,
      y, we can obtain another result:

      Hy,imagt=Ftexp(−i2πtΔyN)+Gt\ :math:`H^{\rm y,imag}_{\rm t} = F_{\rm t} \exp(-i\frac{2\pi t \Delta^{\rm y}}{N}) + G_{\rm t}`.

      we can obtain Gt\ :math:`G_{\rm t}`, Fourier transform of the
      contribution from image sideband, gk\ :math:`g_{\rm k}`, from the
      above two results,

      Gt=12(Hx,imagt+Hy,imagt)+12cosθisinθ(Hx,imagt−Hy,imagt)\ :math:`G_{\rm t} = \frac{1}{2} (H^{\rm x,imag}_{\rm t} + H^{\rm y,imag}_{\rm t}) + \frac{1}{2} \frac{\cos\theta}{i\sin\theta} (H^{\rm x,imag}_{\rm t} - H^{\rm y,imag}_{\rm t})`,

      where
      θ=2πt(Δx−Δy)/N\ :math:`\theta = 2\pi t (\Delta^{\rm x} - \Delta^{\rm y}) / N`. 

      There are two ways to obtain the contribution from signal
      sideband. One is to solve signal sideband exactly same procedure
      with the above. By doing that, we obtain,

      Ft=12(Hx,sigt+Hy,sigt)−12cosθisinθ(Hx,sigt−Hy,sigt)\ :math:`F_{\rm t} = \frac{1}{2} (H^{\rm x,sig}_{\rm t} + H^{\rm y,sig}_{\rm t}) - \frac{1}{2} \frac{\cos\theta}{i\sin\theta} (H^{\rm x,sig}_{\rm t} - H^{\rm y,sig}_{\rm t})`,

      where the quantity with superscript "sig" corresponds to the
      shifted spectrum so that contribution from the signal sideband
      remain fixed. This is what the **sdsidebandsplit** does
      when *otherside=True*. Another way is to subtract the contribution
      of image sideband from the output spectrum. If *otherside=False*,
      contribution from signal sideband is estimated in that way. 

      In principle, the task can split contributions from signal and
      image sidebands if only two images with different LO shifts are
      given. However, the task accepts more than two images to obtain
      better result. If m\ :math:`m` images are given and all images are
      based on independent LO shifts, there are
      m(m−1)/2\ :math:`m(m-1)/2` combinations to obtain the solution of
      splitted spectra. In that case, the task takes average of those
      solutions to get a final solution. 

      Note that, when Δx\ :math:`\Delta^{\rm x}` and
      Δy\ :math:`\Delta^{\rm y}` are so close that θ\ :math:`\theta`
      becomes almost zero, the above solution could diverge. Such a
      solution must be avoided to obtain a finite result. The parameter
      *threshold* is introduced for this purpose. It should range from
      0.0 to 1.0.  The solution will be excluded from the process if
      \|sin(θ)\|\ :math:`|\sin(\theta)|` is less than *threshold*. 

       

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Emerson, Klein, & Haslam 1979, A&A, 76, 92        |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/1979A%26A....76...92E>`__) |
      +-----------------+---------------------------------------------------+

   .. container::
      :name: citation-container

      .. container::
         :name: citation-title

         Bibliography

      .. container::

         :sup:`1. Emerson, Klein, & Haslam 1979, A&A, 76, 92
         (`\ `ADS <http://adsabs.harvard.edu/abs/1979A%26A....76...92E>`__\ :sup:`)`\ `↩ <#ref-cit1>`__

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   task_sdsidebandsplit/about
   task_sdsidebandsplit/parameters
   task_sdsidebandsplit/changelog
   task_sdsidebandsplit/examples
   task_sdsidebandsplit/developer