Description
   Task **sdsmooth** performs smoothing along the spectral axis using
   a user-specified smoothing kernel. Currently, 'Gaussian' and
   'boxcar' kernels are supported.

   The default Kernel shape is 'Gaussian'. The width of the function
   is specified with the*kwidth* parameter, in number of channels.

   Standard data selection parameters are used: *antenna*, *field*,
   *spw*, *scan*, *timerange*, *pol,* and *intent*.

   

   Weights are propagated to smoothed spectra following:

   :math:`W^{k}_{\rm out} = \frac{ (\sum_{i=1}^{n} c_{i})^{2} } { (\sum_{i=1}^{n} c^{2}_{i} / W^{j+i}_{\rm inp}) }`
    ,

   where :math:`W` is the input/output weight, :math:`c`is the
   spectral smoothing kernel originated from a channel
   :math:`k`where the weight is evaluated, and :math:`n`is the
   width of the spectral smoothing kernel in channels. In the case of
   Gaussian, :math:`n`corresponds to FWHM in channels.

   | 
   |
