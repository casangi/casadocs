#
# stub function definition file for docstring parsing
#

def sdfixscan(infiles, mode='fft_mask', numpoly=2, beamsize='0.0', smoothsize='2.0', direction='', maskwidth='1.0', tmax=0.0, tmin=0.0, outfile='', overwrite=False):
    r"""
Task for single-dish image processing

Parameters
   - infiles_ (variant) - list of name of input SD images (FITS or CASA image)
   - mode_ (string='fft_mask') - image processing mode ["fft_mask", "model"]

      .. raw:: html

         <details><summary><i> mode = fft_mask </i></summary>

      - direction_ (variant='') - scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree
      - maskwidth_ (variant='1.0') - mask width for Basket-Weaving (on percentage)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = model </i></summary>

      - numpoly_ (int=2) - order of polynomial fit for Pressed-out method
      - beamsize_ (variant='0.0') - beam size for Pressed-out method
      - smoothsize_ (variant='2.0') - size of smoothing beam for Pressed-out method
      - direction_ (variant='') - scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree

      .. raw:: html

         </details>
   - tmax_ (double=0.0) - maximum threshold value for processing
   - tmin_ (double=0.0) - minimum threshold value for processing
   - outfile_ (string='') - name of output file
   - overwrite_ (bool=False) - overwrite the output file if already exists [True, False]


Description
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
   be specified for each input image.As *direction* parameters, you
   should specify the angles perpendicular to the scan directionsin
   units of degrees.The angle is defined in the counterclockwise
   direction from the x-axis.It removes scan noise by masking wave
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
      processing.And note that 'Basket-Weaving' mode supports
      combining orthogonal scan noise images only (It is possible,
      but,at least, this function has not been tested enough).

   For 'Pressed-out', the scanning must be in a single direction.
   There aretwo ways to specify the size of the smoothing beam used
   for this process. Oneis to specify smoothing size directly. To do
   this, *smoothsize* shouldbe specified as a string of a numerical
   value and a unit(e.g. '10.0arcsec'). The value of *beamsize* will
   be ignored in this case. The other way is to set smoothing size as
   a scale factor of the observed beamsize. In this case, *beamsize*
   is interpreted as the observed beamsize, and *smoothsize* is the
   scale factor. If the *beamsize* isprovided as a float value, its
   unit is assumed to 'arcsec'. It is alsopossible to set the
   *beamsize* as a string consisting of the numericalvalue and the
   unit. The *smoothsize* must be a float value.

   The *infiles* must be an image (CASA or FITS), and doesnot work
   with MS or Scantable. The *direction* is an angle with respectto
   horizontal, in units of degrees. Preferred entries should range
   from 0.0 to 180.0 degrees. The *tmax* and the *tmin* parameters
   are used to specify a threshold thatdefines a range of spectral
   values used for processing. Data values larger than *tmax* or
   smaller than *tmin* will beexcluded from the processing. The
   default (0.0) is to apply no threshold.The *outfile* specifies an
   output CASA image name. If *outfile* isempty, the default name
   ('sdfixscan.out.im') will be used.


   Bibliography
      :sup:`1. Emerson & Grave 1988
      (` `PDF <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1988A%26A...190..353E&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__ :sup:`)` `<#ref-cit1>`__

      :sup:`2. Sofue & Reich 1979
      (` `PDF <http://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1979A%26AS...38..251S&amp;data_type=PDF_HIGH&amp;whole_paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__ :sup:`)` `<#ref-cit2>`__


.. _infiles:

infiles (variant)
   | list of name of input SD images (FITS or CASA image)

.. _mode:

mode (string='fft_mask')
   | image processing mode

.. _numpoly:

numpoly (int=2)
   | order of polynomial fit for Pressed-out method

.. _beamsize:

beamsize (variant='0.0')
   | beam size for Pressed-out method

.. _smoothsize:

smoothsize (variant='2.0')
   | size of smoothing beam for Pressed-out method

.. _direction:

direction (variant='')
   | scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree

.. _maskwidth:

maskwidth (variant='1.0')
   | mask width for Basket-Weaving (on percentage)

.. _tmax:

tmax (double=0.0)
   | maximum threshold value for processing

.. _tmin:

tmin (double=0.0)
   | minimum threshold value for processing

.. _outfile:

outfile (string='')
   | name of output file

.. _overwrite:

overwrite (bool=False)
   | overwrite the output file if already exists


    """
    pass
