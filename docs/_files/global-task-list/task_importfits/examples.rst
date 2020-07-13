Examples
========

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      A straightforward implementation of **importfits**:

      .. container:: casa-input-box

         importfits(fitsimage='ngc3256.fits', imagename='ngc3256.im',
         overwrite=True)

      Though the user may wish to explicitly set (or re-set), for
      example, the beam characteristics:

      .. container:: casa-input-box

         importfits(fitsimage='ngc3256.fits', imagename='ngc3256.im',
         overwrite=True, beam=['0.35arcsec', '0.24arcsec', '25deg'])

      Which will force the BMIN, BMAX and BPA parameters to be 0.35",
      0.24" and 25 degrees, respectively.

.. container:: section
   :name: viewlet-below-content-body
