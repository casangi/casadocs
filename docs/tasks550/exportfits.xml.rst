exportfits -- Convert a CASA image to a FITS file -- import/export task
=======================================

Description
---------------------------------------

CASA-produced images can be exported as FITS files for transporting to
other software packages or publication.  
No subimaging of the fits image can be made with this task.
The spectral reference frame can be changed prior to export using the
task imreframe.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - imagename
     - :code:`''`
     - Name of input CASA image
   * - fitsimage
     - :code:`''`
     - Name of output image FITS file
   * - velocity
     - :code:`False`
     - Use velocity (rather than frequency) as spectral axis
   * - optical
     - :code:`False`
     - Use the optical (rather than radio) velocity convention
   * - bitpix
     - :code:`int(-32)`
     - Bits per pixel
   * - minpix
     - :code:`int(0)`
     - Minimum pixel value (if minpix > maxpix, value is automatically determined)
   * - maxpix
     - :code:`int(-1)`
     - Maximum pixel value (if minpix > maxpix, value is automatically determined)
   * - overwrite
     - :code:`False`
     - Overwrite output file if it exists?
   * - dropstokes
     - :code:`False`
     - Drop the Stokes axis?
   * - stokeslast
     - :code:`True`
     - Put Stokes axis last in header?
   * - history
     - :code:`True`
     - Write history to the FITS image?
   * - dropdeg
     - :code:`False`
     - Drop all degenerate axes (e.g. Stokes and/or Frequency)?


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of input CASA image
                     Default: none

                        Example: fitsimage='3C273XC1.image'



fitsimage
---------------------------------------

:code:`''`

Name of output image FITS file
                     Default: none

                        Example: fitsimage='3C273XC1.fits'



velocity
---------------------------------------

:code:`False`

Use velocity (rather than frequency) as spectral axis
                     Default: False
                     Options: False|True



optical
---------------------------------------

:code:`False`

Use the optical (rather than radio) velocity convention
                     Default: False
                     Options: False|True



bitpix
---------------------------------------

:code:`int(-32)`

Bits per pixel
                     Default: -32

                        Example: bitpix=16



minpix
---------------------------------------

:code:`int(0)`

Minimum pixel value (if minpix > maxpix, value is automatically determined)


maxpix
---------------------------------------

:code:`int(-1)`

Maximum pixel value (if minpix > maxpix, value is
automatically determined)
                     Default: -1



overwrite
---------------------------------------

:code:`False`

Overwrite output file if it exists?
                     Default: False
                     Options: False|True



dropstokes
---------------------------------------

:code:`False`

Drop the Stokes axis?


stokeslast
---------------------------------------

:code:`True`

Put Stokes axis last in header?
                     Default: True
                     Options: True|False



history
---------------------------------------

:code:`True`

Write history to the FITS image?
                     Default: True
                     Options: True|False



dropdeg
---------------------------------------

:code:`False`

Drop all degenerate axes (e.g. Stokes and/or Frequency)?
                     Default: False
                     Options: False|True





