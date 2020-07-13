.. container::
   :name: viewlet-above-content-title

specflux
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   specflux task: Report spectral profile and calculate spectral flux
   over a user specified region

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: alert-box

         **Note**: **specflux** is currently an experimental task. 

      **specflux** retrieves details of a multi-channel image spectrum
      which has been integrated over a given region (or the entire image
      by default). One may specify which function to use to combine the
      pixel values within the region using the *function* parameter.
      Supported values are 'flux density', 'mean', 'median', and 'sum'.
      Minimal match is supported. **specflux** also calculates
      spectrally integrated flux (brightness) values. 

      The task uses the brightness units that are specified in the image
      header (e.g., Jy/beam or K). When 'flux density' is calculated,
      the resulting spectra are in units of Jy for cube units of Jy/beam
      and :math:`K*arcsec^2` for cube units of K. 

      The spectral integral that **specflux** calculates is the sum of
      the spectrum multiplied by the channel width. The units are
      updated accordingly. 

      If the units are :math:`K*arcsec^2`, multiply the reported value
      by :math:`2.3504\times10^{-8}\times d^2`, where :math:`d` is in
      pc, to convert from units of :math:`K*arcsec^2` to units of
      :math:`K*pc^2`.

      If provided, *major* and *minor* will be used to compute the beam
      size, and hence the per channel flux densities (if *function="flux
      density"*), overriding the input image beam information (if
      present).

      .. container:: info-box

         **NOTE**: When it is not possible to compute the spectral flux
         (e.g., in the case where the brightness units are Jy/beam but
         the image has no synthesized beam and none is provided to the
         task), then the application will fail.

      The output of **specflux** is written to the CASA logger and an
      ASCII file if *logfile* is specified. 

       

      .. rubric:: Parameter descriptions
         :name: title1

      .. rubric:: *imagename*
         :name: imagename

      Name of the input image (CASA, FITS or MIRIAD images are
      accepted). 

      .. rubric:: *region*
         :name: region

      Region selection, using a `CASA region
      file <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files>`__.
      Default is the entire image. 

      .. rubric:: *box*
         :name: box

      `Rectangular spatial
      selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
      if no region file is supplied. Default is the entire image.

      .. rubric:: *chans*
         :name: chans

      `Spectral/channel
      selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
      if no region file is supplied. Default is the entire channel
      range. 

      .. rubric:: *stokes*
         :name: stokes

      `Stokes
      selection <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__,
      if no region file is supplied. Default are all Stokes planes. 

      .. rubric:: *mask*
         :name: mask

      An `image
      mask <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks>`__
      file. Default is not to use a mask.  

      .. rubric:: *stretch*
         :name: stretch

      If the image mask is a single plane and not a cube of the same
      dimension as the input data cube, *stretch* can by set to True to
      extend the mask to all planes. (Default: False)

      .. rubric:: *function*
         :name: function

      Aggregate function to use for computing per channel values.
      Supported values are 'flux density', 'mean', 'median', 'sum'.
      Minimal match is supported.\ *
      *

      .. rubric:: *unit*
         :name: unit

      Unit to use for the spectral flux calculation. Must be conformant
      with a typical spectral axis unit. Velocity units may only be used
      if the spectral coordinate has a rest frequency and if it is
      :math:`> 0`.

      .. rubric:: *major*
         :name: major

      Major axis of overriding restoring beam. If specified, it must be
      a valid quantity (e.g., "4arcsec").

      .. rubric:: *minor*
         :name: minor

      Minor axis of overriding restoring beam. If specified, it must be
      a valid quantity (e.g., "3arcsec").

      .. rubric:: *logfile*
         :name: logfile

      File which to write details. Default is to not write to a file.

      .. rubric:: *overwrite*
         :name: overwrite

      Overwrite exisitng *logfile* file if it exists. (Default: False) 

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_specflux/about
   task_specflux/examples
