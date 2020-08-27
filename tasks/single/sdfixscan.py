#
# stub function definition file for docstring parsing
#

def sdfixscan(infiles, mode='fft_mask', numpoly=2, beamsize='0.0', smoothsize='2.0', direction='', maskwidth='1.0', tmax=0.0, tmin=0.0, outfile='', overwrite=False):
    """
Task for single-dish image processing

| Task sdfixscan is used to remove a scanning noise that appears 
|as a striped noise pattern along the scan direction in a raster 
|scan data. 
|
|By default, the scanning noise is removed by using the 
|FFT-based 'Basket-Weaving' method (Emerson \& Grave 1988) that
|requires multiple images that observed exactly the same area with
|different scanning direction. If only one image is available, the
|'Pressed-out' method (Sofue \& Reich 1979) can be used to remove
|the scanning effect.

Parameters
----------
infiles : variant
   list of name of input SD images (FITS or CASA image)
mode : string
   image processing mode ["fft_mask", "model"]
tmax : double
   maximum threshold value for processing
tmin : double
   minimum threshold value for processing
outfile : string
   name of output file
overwrite : bool
   overwrite the output file if already exists [True, False]

Other Parameters
----------
numpoly : int
   order of polynomial fit for Pressed-out method
beamsize : variant
   beam size for Pressed-out method
smoothsize : variant
   size of smoothing beam for Pressed-out method
direction : variant
   scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree
maskwidth : variant
   mask width for Basket-Weaving (on percentage)

Notes
-----





   remove artefacts in raster-scanned SD images



      Task **sdfixscan** is used to remove a striping pattern generated
      along the scan direction in raster scan data. By default, the
      scanning noise is removed using the FFT-based 'Basket-Weaving'
      method `[1] <#cit1>`__ that requires multiple images observed over
      exactly the same area with a different scanning direction. When
      doing 'Basket-Weaving', you can mask small structures and protect
      them using the *maskwidth* parameter. If only one image is
      available, the 'Pressed-out' method `[2] <#cit2>`__ can be used to
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

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   |  Emerson & Grave 1988                             |
      |                 | (`PDF <http://articles.ads                        |
      |                 | abs.harvard.edu/cgi-bin/nph-iarticle_query?1988A% |
      |                 | 26A...190..353E&amp;data_type=PDF_HIGH&amp;whole_ |
      |                 | paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Sofue & Reich 1979                                |
      |                 | (`PDF <http://articles.ads                        |
      |                 | abs.harvard.edu/cgi-bin/nph-iarticle_query?1979A% |
      |                 | 26AS...38..251S&amp;data_type=PDF_HIGH&amp;whole_ |
      |                 | paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__) |
      +-----------------+---------------------------------------------------+


         Bibliography

         :sup:`1.  Emerson & Grave 1988
         (` `PDF <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1988A%26A...190..353E&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__ :sup:`)` `↩ <#ref-cit1>`__

         :sup:`2. Sofue & Reich 1979
         (` `PDF <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26AS...38..251S&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__ :sup:`)` `↩ <#ref-cit2>`__

    """
    pass
