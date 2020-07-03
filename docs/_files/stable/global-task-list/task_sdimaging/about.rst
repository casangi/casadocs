.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   sdimaging task: image total power and spectral data of single dish
   telescopes

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      | This task grids/images total power and spectral data according
        to a specified gridding kernel. The input data should be
        calibrated and bandpass corrected (where necessary), and the
        output is a CASA image format dataset, either 2-d, 3-d, or 4-d
        depending on the input parameters.
      |  

      The output image contains up to four axes: two spatial axes,
      frequency, and polarization. By default, the spatial coordinates
      are determined such that the imaged area is covered with a cell
      size equal to 1/3 of the FWHM of the primary beam of antennas in
      the first MS. It is also possible to define the spatial axes of
      the image by specifying the image center direction
      (*phasecenter*), the number of image pixels (*imsize*), and the
      pixel size (*cell*).

      | 
      | The frequency coordinate of the image is defined by three
        parameters: the number of channels (*nchan*), the channel
        number/frequency/velocity of the first channel (*start*), and
        the channel width (*width*).  The *start* and *width* parameters
        can be in units of 'channel' (use channel number), 'frequency'
        (e.g., 'GHz'), or 'velocity' (e.g., 'km/s'). By default,
        *nchan*, *start*, and *width* are set so that all selected
        spectral windows are covered with a channel width equal to the
        separation of the first two channels selected.
      | Finally, the polarization axis of the image is determined by the
        *stokes* parameter. For example, *stokes*\ ='XXYY' produces an
        image cube with each plane containing the image of one of the
        polarizations, while stokes='I' produces a "total intensity", or
        Stokes I image.

      The parameter *gridfunction* sets the gridding function
      (convolution kernel) for imaging. Currently, the task supports
      'BOX' (boxcar), 'SF' (Prolate Spheroidal Wave Function), 'GAUSS'
      (Gaussian), 'GJINC' (Gaussian*Jinc), where Jinc(x) =
      $J_1(π*x/c)/(π*x/c)$ with a first order Bessel function J_1, and
      'PB' (Primary Beam).

      | There are four subparameters for *gridfunction*: *convsupport,
        truncate, gwidth*, and *jwidth*. The *convsupport* parameter is
        an integer specifying the cutoff radius for 'SF' in units of
        pixels. By default (*convsupport*\ =-1), the cutoff radius is 3
        pixels. The *truncate* parameter is a cutoff radius for 'GAUSS'
        or 'GJINC'. It accepts integer, float, and string values, where
        the string would be a number plus unit. Allowed units include
        'deg', 'arcmin', 'arcsec', and 'pixel'. The default is 'pixel'. 
        The default value for *truncate*, which is used when a negative
        radius is set, is 3*HWHM for 'GAUSS', and the radius at the
        first null for 'GJINC'. The *gwidth* is the HWHM of the Gaussian
        for 'GAUSS' and 'GJINC'. The default value is sqrt(log(2))
        pixels for 'GAUSS' and 2.52*sqrt(log(2)) pixels for 'GJINC'. The
        *jwidth* specifies the width of the jinc function (parameter 'c'
        in the definition above). The default is 1.55 pixels. Both
        *gwidth* and *jwidth* allow integer, float, or string values,
        where the string would be a number plus unit.  The default
        values for *gwidth* and *jwidth* are taken from Mangum, et al.
        2007 `[1] <#cit>`__ . The formula for 'GAUSS' and 'GJINC' are
        taken from Table 1 in the paper, and are written as follows
        using *gwidth* and *jwidth*:
      |    GAUSS: $\exp[-\log(2)*(|r|/gwidth)^2]$
      |    GJINC: $J_1(π*|r|/jwidth)/(π*|r|/jwidth)\*
        \\exp[-\log(2)*(|r|/gwidth)^2]$

      The *imagename* should be unique. Clean will stop with an
      Exception error (e.g. Exception: Unable to open lattice) if
      *imagename* is the same as the *vis* name.   

      | The *ephemsrcname* parameter can be set to specifiy an ephemeris
        for a moving source (solar sytem objects).  If the source name
        in the data matches one of the solar system objects known by
        CASA, the imaging realigns the data by shifting the source, so
        that the source appears to be fixed in the image.
      | The *clipminmax* function can clip minimum and maximum value
        from each pixel. This function makes the computed output
        slightly more robust to noise and spurious data.  Note the
        benefit of clipping is lost when the number of integrations
        contributing to each gridded pixel is small, or where the
        incidence of spurious data points is approximately equal to or
        greater than the number of beams (in area) encompassed by the
        expected image.

      The *minweight* parameter defines a threshold of weight values to
      mask. The pixels in *outfile* whose weight is smaller than
      *minweight*\ \*median (*weight*) are masked out. The task also
      creates a weight image with the name outfile.weight.

      The *projection* parameter allows to specify what kind of map
      projection is applied. The default is SIN (slant orthographic)
      projection. Besides that, the task supports CAR (plate carrée),
      TAN (gnomonic), and SFL (Sanson-Flamsteed). 

      .. rubric:: Bibliography
         :name: bibliography

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Mangum, et al. 2007, A&A, 474, 679-687            |
      |                 | `(A&A) <http://www.aa                             |
      |                 | nda.org/articles/aa/pdf/2007/41/aa7811-07.pdf>`__ |
      +-----------------+---------------------------------------------------+

.. container:: section
   :name: viewlet-below-content-body
