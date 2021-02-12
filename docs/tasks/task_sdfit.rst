

.. _Description:

Description
   Task **sdfit** is a basic line fitter for single-dish spectra.
   While it's possible to run **sdfit** on uncalibrated data, the
   structure of the raw bandpass is likely to return complicated
   results that are difficult to parse meaningfully. It's therefore
   recommended to run **sdfit** on calibrated data. The task can fit
   Gaussian or Lorentzian functions.

   The masks for fitting (i.e. selection of the fitting ranges) can
   be computed automatically, or provided specifically by the user.

   .. note:: **NOTE**: Multiple scans, IFs, and polarizations can in
      principle be handled, but it is recommended to use *scan*,
      *field*, *spw*, and *pol* to give a single selection for each
      fit. The task produces a Python dictionary of line statistics
      as output, with keys: 'peak', 'cent', 'fwhm', and 'nfit'.   See
      examples on referencing the keys, below.

   Configurable inputs enable control over data selection,
   averaging/binning behavior, specific handling of polarizations,
   fitting types, and restrictions and output control.

   Selection is by spectral window/channels, field IDs, and antennas
   through the *spw*, *field*, *pol, intent * and *antenna*
   selection parameters. Defaults are that all data are considered in
   fitting.

   Averaging can be computed over time intervals, with the *timebin*
   parameter.  Leaving it unset (the default) indicates no time
   averaging. The *timespan* parameter determines which axes will be
   averaged, in terms of 'scan', 'state' or 'field'.  So multiple
   scans or fields can be averaged together with this parameter.

   Two modes of polarization averaging are available via
   *polaverage*, though the difference is subtle;  the options are
   "Stokes" (the default) and "Geometric". The differences manifest
   in the way the weightings are incorporated in the computation.

   "Stokes" mode computes Stokes I as:

   :math:`I = (XX + YY) / 2.`

   and the associated weight as:

   :math:`w_I = 4 / ( 1/w_{XX} + 1/w_{YY} )`

   "Geometric" mode implements the computation of Stokes I by folding
   in weights for XX and YY as follows:

   :math:`I = (XX * w_{XX} + YY * w_{YY}) / (w_{XX} + w_{YY})`

   And the associated weight as:

   :math:`w_I = w_{XX} + w_{YY}`

   "Geometric" mode is consistent with the historical implementation
   of computing Stokes I, though it is not formally correct since it
   assumes the weightings for XX and YY are equal, generally not the
   case. It is provided for users requiring backward compatibility.

   *fitmode* in **sdfit** enables fitting modes 'list' and 'auto' at
   this point. The 'list' mode allows users to set initial parameters
   (line region and number of lines per region) for the fit. In
   'list' mode, users must give line region via the *spw* parameter
   by using MS selection syntax, while the number of lines per region
   can be specified via the *nfit* parameter.

   In 'auto' mode, the line finder detects channel ranges of spectral
   lines based on median absolute deviation (MAD) of the spectra
   using user defined criteria with the sub-parameters *thresh*,
   *avg_limit*, *minwidth*, and *edge*. The number of channels at
   both edges of spectra defined by the *edge* parameter are ignored
   in line detection.

   The median of the lower 80% of MAD values in a spectrum is
   multiplied by the *thresh* parameter value to define a threshold
   of line detection. All channels with MAD above the threshold are
   identified as spectral line candidates and accepted as spectral
   lines only if the channel width of the line exceeds the value of
   *minwidth* parameter. The line detection is iteratively invoked
   for channel-averaged spectra up to *avg_limit*.

   *thresh* -- [default 5] S/N threshold for linefinder.
   *avg_limit* -- [default 4] channel averaging for broad lines. A
   number of consecutive channels up to this value will be averaged
   to search for broad lines
   *minwidth* --[default: 4]  minimum number of consecutive
   channels required to pass threshold
   *edge* -- [default 0] channels to drop at beginning and end of
   spectrum

   .. note:: **NOTE**: For bad baselines, *thresh* should be increased, and
      *avg_limit* decreased (or even switched off completely by
      setting this parameter to 1) to avoid detecting baseline
      undulations instead of real lines.

   Detailed output is directed to a log file identified by the
   '*outfile*' parameter.


.. _Examples:

Examples
   This example is to fit two Gaussian (default) components to all
   integrations in scan 4, polarization 'XX' only, and write the
   output to a file.  The output (sdfitout) is a python dictionary.

   ::

      sdfitout = sdfit(infile=mymeasurement_set, datacolumn='data', scan='4', outfile='sdfit.log',
                       overwrite=T, nfit=[2], pol='XX')

   An Example of output file:

   ::

      #SCAN  TIME             ANT  BEAM  SPW  POL  Function  P0           P1           P2
      4      4873839081.0780  2    0     6    0    gauss0    2.58050537   15.00975037  3.89437151
      4      4873839081.0780  2    0     6    0    gauss1    0.72443587   61.37811279  8.87286472

   In this example, only a spectrum is selected in an MS. Each row of
   the output file stores the results of fitting a line in the
   spectrum. The columns P0, P1, and P2, store the peak, channel
   index of line center, and full-width-half-maximum (FWHM,
   in channels), respectively.

   The task returns a dictionary of fit results which stores the
   number of lines, 'nfit', and the fit of each line, i.e., the line
   center, 'cent', the full-width-half-maximum, 'fwhm', and peak,
   'peak'. Each value except for 'nfit' is a list of 2 entries [fit
   value, error].

   ::

      sdfitout

      Out[1]:

      {'cent': [[[15.00975037, 0.04713312], [61.37811279, 0.25342196]]],
       'fwhm': [[[3.89437151, 0.11099002], [8.87286472, 0.59676313]]],
       'nfit': [2],
       'peak': [[[2.58050537, 0.06369157], [0.72443587, 0.04219575]]]}

   To obtain the peak of the second line in the first spectrum from
   the dictionary,

   ::

      sdfitout['peak'][0][1]

      Out[2]: [0.72443587, 0.04219575]

   The first entry is the fitted value and the second one is the
   error on the fitted value.

   To fit three lines in a region:

   ::

       sdfitout = sdfit(infile=mymeasurement_set, fitmode='list', nfit=[3])

   To fit two lines in two regions:

   ::

       sdfitout = sdfit(infile=mymeasurement_set, fitmode='list', nfit=[2,2])

   To automatically fit any lines with S/N > 2, averaging over four
   channels (i.e. smoothing), and requiring lines to be at least 10
   channels wide, while excluding channels 0:1000 from beginning and
   500:end from the end of the spectrum:

   ::

      sdfitout = sdfit(infile=mymeasurement_set, fitmode='auto', edge=[1000,500],
                       avg_limit='4', thresh='2', minwidth='10')

   This example directs the output to a file, mysd.fit :

   ::

      sdfitout = sdfit(infile=mymeasurement_set, outfile='mysd.fit')


.. _Development:

Development
   No additional development details

