

.. _Description:

Description
   Task **sdfixscan** is used to remove a striping pattern generated
   along the scan direction in raster scan data. By default, the
   scanning noise is removed using the FFT-based 'Basket-Weaving'
   method [1]_ that requires multiple images observed over
   exactly the same area with a different scanning direction. When
   doing 'Basket-Weaving', you can mask small structures and protect
   them using the *maskwidth* parameter. If only one image is
   available, the 'Pressed-out' method [2]_ can be used to
   remove the scanning effect.

   For 'Basket-Weaving', scans must have been conducted in at least
   two different directions. Normally, the scanning direction should
   be specified for each input image. As *direction* parameters, you
   should specify the angles perpendicular to the scan directions in
   units of degrees. The angle is defined in the counterclockwise
   direction from the x-axis. It removes scan noise by masking wave
   components perpendicular to the scan direction in the Fourier
   domain. Scan noise and striation structures appear as band-like
   artifacts in the Fourier transformed data. The parameter
   *maskwidth* controls the width of the mask in Fourier space and is
   defined as a percentage in the Fourier domain (*maskwidth = 10*
   means masking a region of 10% width in Fourier space). In the
   perfect case, where scan noise is an ideal striation without
   structure in the direction perpendicular to scan direction, the
   scan noise can be removed by specifying a small value for
   *maskwidth* (ex. *maskwidth = 1*). In the actual case, *maskwidth*
   should be set to some larger number, since scan noise also has
   some structure in the direction perpendicular to the scanning
   direction. Larger *maskwidth* values may also remove the emission
   from the scientific target at the same time, so careful adjustment
   and characterization by the user is necessary.

   .. note:: **NOTE**: Such masks are applied for each input scan image and
      the combined image is returned. If the size of the mask is
      large, the improvements to the noise level by combining images
      becomes small, since a smaller amount of data is subject to the
      processing. And note that 'Basket-Weaving' mode supports
      combining orthogonal scan noise images only (It is possible,
      but, at least, this function has not been tested enough).

   For 'Pressed-out', the scanning must be in a single direction.
   There are two ways to specify the size of the smoothing beam used
   for this process. One is to specify smoothing size directly. To do
   this, *smoothsize* should be specified as a string of a numerical
   value and a unit (e.g. '10.0arcsec'). The value of *beamsize* will
   be ignored in this case. The other way is to set smoothing size as
   a scale factor of the observed beam size. In this case, *beamsize*
   is interpreted as the observed beam size, and *smoothsize* is the
   scale factor. If the *beamsize* is provided as a float value, its
   unit is assumed to 'arcsec'. It is also possible to set the
   *beamsize* as a string consisting of the numerical value and the
   unit. The *smoothsize* must be a float value.

   The *infiles* must be an image (CASA or FITS), and does not work
   with MS or Scantable. The *direction* is an angle with respect to
   horizontal, in units of degrees. Preferred entries should range
   from 0.0 to 180.0 degrees. The *tmax* and the *tmin* parameters
   are used to specify a threshold that defines a range of spectral
   values used for processing. Data values larger than *tmax* or
   smaller than *tmin* will be excluded from the processing. The
   default (0.0) is to apply no threshold. The *outfile* specifies an
   output CASA image name. If *outfile* is empty, the default name
   ('sdfixscan.out.im') will be used.


   .. rubric:: Bibliography

   .. [1] Emerson & Grave 1988, A&A, 190, 353 `ADS <https://ui.adsabs.harvard.edu/abs/1988A%26A...190..353E/abstract>`__

   .. [2] Sofue & Reich 1979, A&AS, 38, 251 `ADS <https://ui.adsabs.harvard.edu/abs/1979A%26AS...38..251S/abstract>`__


.. _Examples:

Examples
   Examples for 'Basket-Weaving'

   ::

      sdfixscan(mode='fft_mask', infiles=['scan_0deg.im', 'scan_90deg.im'], direction=[0., 90.],
                maskwidth=5.0, outfile='basket_0_90.im')

      sdfixscan(mode='fft_mask', infiles=['scan_30deg.im', 'scan_120deg.im'], direction=[30., 120.],
                maskwidth=10.0, outfile='basket_30_120.im')



   Example for  'Pressed-out'

   ::

      sdfixscan(mode='model', infiles='scan_0deg.im', direction=90., smoothsize='100arcsec', outfile='press_0.im')


.. _Development:

Development
   No additional development details

