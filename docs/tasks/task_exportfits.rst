

.. _Description:

Description
   

.. _Examples:

Examples
   Write a FITS image file that uses velocity rather than frequency
   as the spectral axis, overwriting an existing file of the same
   name if it already exists.
   
   ::
   
      exportfits(imagename="my.im", fitsimage="my.fits", velocity =
      True, overwrite=True)
   
   Write a FITS image file that uses velocity rather than frequency
   as the spectral axis and where the degenerate Stokes axis is
   dropped (i.e. the product has only one value in the polarisation
   dimension).
   
   ::
   
      exportfits(imagename="my.im", fitsimage="my.fits", dropstokes =
      True, velocity = True)
   
   Note: if the imput image has a synthesized beam specfied, then the
   major and minor axis (BMAJ and BMIN) may be specified in units of
   degrees in the output fits-file.
   

.. _Development:

Development
   