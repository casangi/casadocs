

.. _Description:

Description
   Task **sdbaseline** fits and/or subtracts a baseline from
   single-dish spectra in MS format. Given parameters that define the
   baseline to be fit (function type, order or the polynomial, etc.),
   **sdbaseline** computes the best-fit baseline for each spectrum
   using the least-squares fitting method and, if you want, subtracts
   it. The best-fit baseline parameters (including baseline type,
   coefficients of basis functions, etc.) and other values such as
   residual rms can be saved in various formats including ascii text
   (in human-readable format or CSV format) or a baseline table (a
   CASA table). Task **sdbaseline** also has a mode to 'apply' a
   baseline table to MS data.  For each spectrum in the MS, the
   best-fit baseline is reproduced from baseline parameters stored in
   the specified baseline table, and subtracted. Putting the "fit"
   and "subtract" into separate processes can be useful for pipeline
   processing of huge datasets.


   .. rubric:: Baseline Model Functions

   The user can specify the function to be used for the baseline with
   the *blfunc* keyword (e.g. *blfunc = 'poly'*). In general,
   polynomial fitting is stable. Sinusoid fitting is a special mode
   that could be useful for data that clearly shows a standing wave
   in the spectral baseline.

   The **sdbaseline** procedure gives the user the opportunity to
   specify unique baseline fitting parameters for each spectrum,
   using the setting *blfunc='variable'*. Note this is an expert
   mode! The fitting parameters should be defined in a text file for
   each spectrum in the input MS. The text file should store comma
   separated values in the following order: row ID, polarization,
   mask, clipniter, clipthresh, use_linefinder,  thresh, left edge,
   right edge, avg_limit, blfunc, order, npiece, nwave. Each row in
   the text file must contain the following keywords and values:

   -  'row': row number after selection
   -  'pol': polarization index in the row
   -  'clipniter': maximum iteration number for iterative fitting
   -  'blfunc': function name.  available options are 'poly',
      'chebyshev', 'cspline',and 'sinusoid'
   -  'order': maximum order of the polynomial. Needed when
      blfunc='poly' or 'chebyshev'
   -  'npiece': number of piecewise polynomials. Needed when
      blfunc='cspline'
   -  'nwave': a list of sinusoidal wave numbers. Needed when
      blfunc='sinusoid'


   .. rubric:: Output Files

   The task outputs the baseline-subtracted MS data set.  Users
   should specify the output data file name with the *outfile*
   keyword.

   Also, the fit parameters, terms, and rms of the baseline can be
   saved into an ascii text file (in human-readable format or CSV
   format) or a baseline table (a CASA table). By default, a text
   file named  <infile name> + '\_ blparam.txt' is output. The
   saved baseline table can be used later to subtract the baselines
   from an MS.


   .. rubric:: Fitting and Clipping

   In general, least-squares fitting is strongly affected by extreme
   data points, making the resulting fit poor. Sigma clipping is an
   iterative baseline fitting method that clips data based on a
   certain threshold. The threshold is set as a certain factor times
   the rms of the resulting (baseline-subtracted) spectra. If sigma
   clipping is on, baseline fit/removal is performed several times,
   iteratively. After each baseline subtraction, data whose absolute
   value is above the threshold are excluded from the next round of
   fitting. By using sigma clipping, extreme data are excluded from
   the fit so the resulting fit is more robust.

   The user can control the rms multiplication factor using the
   parameter *clipthresh,* for the clipping threshold. The actual
   threshold for sigma clipping will then be (clipthresh) x (rms of
   spectra). Also, the user can specify the maximum number of
   iterations with the parameter *clipniter*.

   In general, sigma clipping will make the procedure slower since it
   increases the number of fits per spectra. However, it is strongly
   recommended to turn on sigma clipping unless you are sure that the
   data is free from any kind of extreme values that may affect the
   fit.


   .. rubric:: Update Weight

   Setting the parameter *updateweight = True*, the WEIGHT column is
   updated as :math:`1/stddev^2` or :math:`1/RMS^2` of each
   baseline-subtracted spectrum, depending on the parameter
   *sigmavalue*. The calculation is done with unflagged channels only.

   Note that the SIGMA column is not updated; it keeps the values of
   the input MS data. In case the user wants to refer to the
   standard deviation of the output MS data, she or he needs to
   compute it using WEIGHT column values as :math:`1/\sqrt{WEIGHT}`
   - the SIGMA column should not be refered to.


.. _Examples:

Examples
   .. rubric::   Example 1

   This is one of the simplest examples. To fit and remove a
   Chebyshev polynomial function (default is 5th order) from the data
   'sd_data.ms', using only spectral window 0, and fitting channels
   100-800 and 1200-2000 (to avoid, for example, band-pass roll off
   at the edges, and perhaps an emission line that might occur over
   channels 800-1200).

   ::

      sdbaseline(infile='sd_data.ms', spw='0:100~800;1200~2000', blfunc='chebyshev',
                 outfile='sd_data.ms.bl', overwrite=True)

   .. rubric::  Example 2

   This example shows fitting and subtracting a sinusoidal baseline.
   To fit and remove a sinusoid from the data 'sd_data.ms', using
   spectral window 0 and scan number 0. Wave numbers of sinusoids are
   set autmatically in the fft method.

   ::

      sdbaseline(infile='sd_data.ms', spw='0', scan='0', blfunc='sinusoid', applyfft=True,
                 fftmethod='fft', outfile='sd_data.ms.bl', overwrite=True)

   .. rubric::  Example 3

   In this example, the user specifies different fitting parameters
   per spectrum, using blfunc='variable' and specifying the fit
   parameters using a text file.

   ::

      sdbaseline(infile='sd_data.ms', blfunc='variable', blparam='blparam.txt',
                 outfile='sd_data.ms.bl', overwrite=True)


   Here is the text file "blparam.txt" used in the above example.

   ::

      #row,pol,mask,clipniter,clipthresh,use_linefinder,thresh,Ledge,Redge,avg_limit,blfunc,order,npiece,nwave
      0,0,100~750;1250~1900,0,3.,false,0.,0,0,0,chebyshev,2,0,[]
      0,1,,0,3.,false,0.,0,0,0,chebyshev,0,0,[]
      1,0,0~500;1500~2000,0,3.,false,0.,0,0,0,poly,1,0,[]

   .. rubric::   Example 4

   This is an example of fitting and subtracting a polynomial
   baseline, and also updating the WEIGHT column of the output MS
   'sd_data.ms.bl' as :math:`1/RMS^2` .

   ::

      sdbaseline(infile='sd_data.ms', blfunc='poly', updateweight=True, sigmavalue='rms',
                 outfile='sd_data.ms.bl', overwrite=True)


.. _Development:

Development
   No additional development details

