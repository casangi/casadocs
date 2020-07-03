.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Write a FITS image file that uses velocity rather than frequency
      as the spectral axis, overwriting an existing file of the same
      name if it already exists.

      .. container:: casa-input-box

         exportfits(imagename="my.im", fitsimage="my.fits", velocity =
         True, overwrite=True)

      Write a FITS image file that uses velocity rather than frequency
      as the spectral axis and where the degenerate Stokes axis is
      dropped (i.e. the product has only one value in the polarisation
      dimension).

      .. container:: casa-input-box

         exportfits(imagename="my.im", fitsimage="my.fits", dropstokes =
         True, velocity = True)

      Note: if the imput image has a synthesized beam specfied, then the
      major and minor axis (BMAJ and BMIN) may be specified in units of
      degrees in the output fits-file.

       

       

       

       

.. container:: section
   :name: viewlet-below-content-body
