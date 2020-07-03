.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Smooth spectral data

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Task **sdsmooth** performs smoothing along the spectral axis using
      a user-specified smoothing kernel. Currently, 'Gaussian' and
      'boxcar' kernels are supported.

      The default Kernel shape is 'Gaussian'. The width of the function
      is specified with the *kwidth* parameter, in number of channels.

      Standard data selection parameters are used: *antenna*, *field*,
      *spw*, *scan*, *timerange*, *pol,* and *intent*.

       

      Weights are propagated to smoothed spectra following:

      $W^{k}_{\rm out} = \\frac{ (\sum_{i=1}^{n} c_{i})^{2} } {
      (\sum_{i=1}^{n} c^{2}_{i} / W^{j+i}_{\rm inp}) } $    ,

      where $W$ is the input/output weight, $c$ is the spectral
      smoothing kernel originated from a channel $k$ where the weight is
      evaluated, and $n$ is the width of the spectral smoothing kernel
      in channels. In the case of Gaussian, $n$ corresponds to FWHM in
      channels.

      | 
      |  

.. container:: section
   :name: viewlet-below-content-body
