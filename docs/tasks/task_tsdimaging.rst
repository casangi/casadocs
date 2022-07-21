

.. _Description:

Description
   The **tsdimaging** task grids/images total power and spectral data
   according to a specified gridding kernel. The input data should be
   calibrated and bandpass corrected (where necessary), and the
   output is a CASA image format dataset, either 2-D, 3-D, or 4-D
   depending on the input parameters.

   The output image contains up to four axes: two spatial axes,
   frequency, and polarization. By default, the spatial coordinates
   are determined such that the imaged area is covered with a cell
   size equal to 1/3 of the FWHM of the primary beam of antennas in
   the first MS. It is also possible to define the spatial axes of
   the image by specifying the image center direction
   (*phasecenter*), the number of image pixels (*imsize*), and the
   pixel size (*cell*).

   The frequency coordinate of the image is defined by three
   parameters: the number of channels (*nchan*), the channel
   number/frequency/velocity of the first channel (*start*), and the
   channel width (*width*). The *start* and *width* parameters can be
   in units of 'channel' (use channel number), 'frequency' (e.g.,
   'GHz'), or 'velocity' (e.g., 'km/s'). By default, *nchan*,
   *start*, and *width* are set so that all selected spectral windows
   are covered with a channel width equal to the separation of the
   first two channels selected.

   Finally, the polarization axis of the image is determined by the
   *stokes* parameter. For example, *stokes='XXYY'* produces an image
   cube with each plane containing the image of one of the
   polarizations, while *stokes='I'* produces a "total intensity", or
   Stokes I image. There is also another option for Stokes I imaging,
   called 'pseudoI'; the difference between 'I' and 'pseudoI' is how
   the task handles flag information. The *stokes='I'* imaging is
   stricter in the sense that it only takes into account visibilities
   for which all correlations are valid. In other words, it excludes
   all correlations for any data with any correlation flagged, even
   though the remaining correlations are valid. On the other hand,
   the 'pseudoI' option allows Stokes I images to include data for
   which either of the parallel hand data are unflagged.

   .. note:: **NOTE**: Users should set *stokes='pseudoI'* if you want to
      get the equivalent result to the one obtained by setting
      *stokes='I'* for **sdimaging**. Setting *stokes='I'* in
      **sdimaging** is implemented the same way as *stokes='pseudoI'*
      in **tsdimaging**.

   The parameter *gridfunction* sets the gridding function
   (convolution kernel) for imaging. Currently, the task supports
   'BOX' (boxcar), 'SF' (Prolate Spheroidal Wave Function), 'GAUSS'
   (Gaussian), 'GJINC' (Gaussian*Jinc), where Jinc(x) =
   :math:`J_1(π*x/c)/(π*x/c)` with a first order Bessel function J_1,
   and 'PB' (Primary Beam).

   There are four subparameters for *gridfunction*: *convsupport,
   truncate, gwidth*, and *jwidth*. The *convsupport* parameter is an
   integer specifying the cutoff radius for 'SF' in units of pixels.
   By default (*convsupport* =-1), the cutoff radius is 3 pixels.
   The *truncate* parameter is a cutoff radius for 'GAUSS' or
   'GJINC'. It accepts integer, float, and string values, where the
   string would be a number plus unit. Allowed units include 'deg',
   'arcmin', 'arcsec', and 'pixel'. The default is 'pixel'. The
   default value for *truncate*, which is used when a negative radius
   is set, is 3*HWHM for 'GAUSS' and the radius at the first null for
   'GJINC'. The *gwidth* is the HWHM of the Gaussian for 'GAUSS' and
   'GJINC'. The default value is :math:`sqrt(log(2))` pixels for
   'GAUSS' and :math:`2.52*sqrt(log(2))` pixels for 'GJINC'. The
   *jwidth* specifies the width of the jinc function (parameter 'c'
   in the definition above). The default is 1.55 pixels. Both
   *gwidth* and *jwidth* allow integer, float, or string values,
   where the string would be a number plus unit. The default values
   for *gwidth* and *jwidth* are taken from Mangum, et al. 2007
   [1]_. The formula for 'GAUSS' and 'GJINC' are taken
   from Table 1 in the paper, and are written as follows using
   *gwidth* and *jwidth*:

   GAUSS: :math:`\exp[-\log(2)*(|r|/gwidth)^2]`,

   GJINC:
   :math:`J_1(π*|r|/jwidth)/(π*|r|/jwidth)* \exp[-\log(2)*(|r|/gwidth)^2]`,

   where :math:`r` is the radial distance from the origin.

   The *outfile* should be unique. **tsdimaging** will stop with an
   Exception error (e.g., Exception: Unable to open lattice) if
   *outfile* is the same as the *infiles* name.

   The *phasecenter* parameter sets the center direction of the
   image. If the phasecenter is the name known major solar system
   object ('MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS',
   'NEPTUNE', 'PLUTO', 'SUN', 'MOON') or is an ephemerides table then
   that source is tracked and the background sources get smeared. A
   parameter *ephemsrcname* has been deprecated accordingly. There is
   a special case, when phasecenter='TRACKFIELD', which will use the
   ephemerides or polynomial phasecenter in the FIELD table of the
   MeasurementSets as the source center to track.

   The *clipminmax* function can clip minimum and maximum values from
   each pixel. This function makes the computed output slightly more
   robust to noise and spurious data. Note that the benefit of
   clipping is lost when the number of integrations contributing to
   each gridded pixel is small, or where the incidence of spurious
   data points is approximately equal to or greater than the number
   of beams (in area) encompassed by the expected image.

   In addition to the image described above, **tsdimaging** produces 
   weight image (outfile.weight). The weight image is calculated 
   based on the WEIGHT or WEIGHT_SPECTRUM in the MS file. 
   In each pixel in the grid (e.g., in RAD-Dec space), the gridding process 
   searches through the data for measurements taken within some cutoff radius 
   (specified by *convsupport*). Depending on their distance from the grid 
   coordinate, the observation is weighted according to the *gridfunction* 
   and added together in each pixel. Sum of the weight is produced as 
   the weight image. The weight image has same dimensions that image has.

   The *minweight* parameter defines a threshold of weight values to
   mask. The pixels in *outfile* whose weight is smaller than
   *minweight* \*median (*weight*) are masked out. 

   The *projection* parameter allows to specify what kind of map
   projection is applied. The default is SIN (slant orthographic)
   projection. The task also supports CAR (plate carrée), TAN
   (gnomonic), and SFL (Sanson-Flamsteed).

   .. rubric:: Image Definition (specmode)

   The image coordinate system(s) and shape(s) can be set up to form
   single images. The different modes for imaging include:

   -  *'cube'*: Spectral line imaging with one or more channels. The
      fixed spectral frame, LSRK, will be used for automatic internal
      software Doppler tracking so that a spectral line observed over
      an extended time range will line up appropriately. You can
      change the output spectral frame via outframe parameter.
   -  *'cubedata'*: Spectral line imaging with one or more channels
      There is no internal software Doppler tracking so a spectral
      line observed over an extended time range may be smeared out in
      frequency.
   -  *'cubesource'*: Spectral line imaging while tracking moving
      source (near field or solar system `ephemeris
      objects <../../notebooks/ephemeris_data.ipynb>`__).
      The velocity of the source is accounted and the frequency
      reported is in the source frame.

   .. rubric:: Technical Note: sdimaging and tsdimaging

   The **tsdimaging** task is supposed to replace **sdimaging**. The
   initial version of this task was intended to be fully compatible
   with **sdimaging**. Technically speaking, those tasks share
   underlying framework with interferometry imaging
   tasks: **sdimaging** shares with **clean**, while **tsdimaging**
   is based on the framework for **tclean**. As **clean** (and the
   underlying framework) will be deprecated and replaced with
   **tclean** in the future, **sdimaging** will also be made
   obsolete in favor of migrating to **tsdimaging**. This transition
   will have several benefits from the user's point of view in
   future. In terms of functionality, new features implemented in
   **tclean** will also apply to **tsdimaging** if the features are
   useful for single dish imaging. Another possible benefit is a
   performance. Since the framework for **tclean** is designed to
   support parallel processing, it can also be used to speed up
   **tsdimaging**. This should be effective for large datasets, but
   these examples represent future work. Currently, effort is
   underway to make **tsdimaging** compatible with **sdimaging** and
   convert it to a "regular" (non-experimental) task.

   .. rubric:: Bibliography

   .. [1] Mangum, et al. 2007, A&A, 474, 679 `ADS <https://ui.adsabs.harvard.edu/abs/2007A%26A...474..679M/abstract>`__


.. _Examples:

Examples
   To generate a spectral line cube with 500 channels selected from
   channel 200 to 700:

   ::

      spw='0'
      pol='XX'
      src='Moon'

      tsdimaging(infiles='mydata.ms',
                 spw=spw,
                 nchan=500,
                 start='200',
                 width='1',
                 cell=['30.0arcsec','30.0arcsec'],
                 outfile='mydata.ms.im',
                 imsize=[80,80],
                 gridfunction='GAUSS',
                 gwidth='4arcsec',
                 stokes=pol,
                 ephemsrcname=src)


   The *start* parameter can be specified in different units:

   ::

      start=100  # mode='channel'
      start='22.3GHz'  # mode='frequency'
      start='5.0km/s'  # mode='velocity'


   The parameter *phasecenter* sets the center direction of the
   image:

   ::

      phasecenter=6
      phasecenter='J2000 19h30m00 -40d00m00'
      phasecenter='J2000 292.5deg -40.0deg'
      phasecenter='J2000 5.105rad -0.698rad'
      phasecenter='ICRS 13:05:27.2780 -049.28.04.458'
      phasecenter='myComet_ephem.tab'
      phasecenter='MOON'
      phasecenter='TRACKFIELD'


.. _Development:

Development
   No additional development details

