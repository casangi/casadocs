exportfits -- Convert a CASA image to a FITS file -- import/export task
=======================================

Description
---------------------------------------

	CASA-produced images can be exported as FITS files for transporting
	to other software packages or publication.  
        No subimaging of the fits image can be made with this task.
        The spectral reference frame can be changed prior to export
        using the task imreframe.




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
     - 
   * - fitsimage
     - :code:`''`
     - 
   * - velocity
     - :code:`False`
     - 
   * - optical
     - :code:`False`
     - 
   * - bitpix
     - :code:`int(-32)`
     - 
   * - minpix
     - :code:`int(0)`
     - 
   * - maxpix
     - :code:`int(-1)`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - dropstokes
     - :code:`False`
     - 
   * - stokeslast
     - :code:`True`
     - 
   * - history
     - :code:`True`
     - 
   * - dropdeg
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of input CASA image


fitsimage
---------------------------------------

:code:`''`

Name of output image FITS file


velocity
---------------------------------------

:code:`False`

Use velocity (rather than frequency) as spectral axis


optical
---------------------------------------

:code:`False`

Use the optical (rather than radio) velocity convention


bitpix
---------------------------------------

:code:`int(-32)`

Bits per pixel


minpix
---------------------------------------

:code:`int(0)`

Minimum pixel value (if minpix > maxpix, value is automatically determined)


maxpix
---------------------------------------

:code:`int(-1)`

Maximum pixel value (if minpix > maxpix, value is automatically determined)


overwrite
---------------------------------------

:code:`False`

Overwrite pre-existing imagename


dropstokes
---------------------------------------

:code:`False`

Drop the Stokes axis?


stokeslast
---------------------------------------

:code:`True`

Put Stokes axis last in header?


history
---------------------------------------

:code:`True`

Write history to the FITS image?


dropdeg
---------------------------------------

:code:`False`

Drop all degenerate axes (e.g. Stokes and/or Frequency)?




