

.. _Description:

Description
   Task **sdsmooth** performs smoothing along the spectral axis using
   a user-specified smoothing kernel. Currently, 'Gaussian' and
   'boxcar' kernels are supported.

   The default Kernel shape is 'Gaussian'. The width of the function
   is specified with the *kwidth* parameter, in number of channels.

   Standard data selection parameters are used: *antenna*, *field*,
   *spw*, *scan*, *timerange*, *pol,* and *intent*.

   Weights are propagated to smoothed spectra following:

   :math:`W^{k}_{m out} = \frac{ (\sum_{i=1}^{n} c_{i})^{2} } { (\sum_{i=1}^{n} c^{2}_{i} / W^{j+i}_{m inp}) }`

   where :math:`W` is the input/output weight, :math:`c` is the
   spectral smoothing kernel originated from a channel
   :math:`k` where the weight is evaluated, and :math:`n` is the
   width of the spectral smoothing kernel in channels. In the case of
   Gaussian, :math:`n` corresponds to FWHM in channels.


.. _Examples:

Examples
   To spectrally smooth part of a data set for both polarizations,
   selecting by frequency and scan with a boxcar kernel having a
   width of 50 channels:

   ::

      sdsmooth(infile='sd_data.ms', spw='116~117GHz', scan='21~23', pol='0,1',
               kernel='boxcar', kwidth='50', antenna='PM03', outfile='sd_data_smoothed.ms',
               overwrite=True)


.. _Development:

Development
   None