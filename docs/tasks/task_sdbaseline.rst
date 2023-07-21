

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
   the *blfunc* parameter (e.g. *blfunc = 'poly'*). In general,
   polynomial fitting is stable. Sinusoid fitting is a special mode
   that could be useful for data that clearly shows a standing wave
   in the spectral baseline.

   In addition to fitting with a single function type, users can also
   specify unique baseline fitting parameters for each spectrum by
   setting *blfunc='variable'*. See 'Per-spectrum Fit Parameters'
   section below for details.


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
   updated as :math:`1/(sigmavalue)^2` according to the *sigmavalue*
   parameter ("stddev" or "rms"), where "stddev" calculates the
   standard deviation of the baseline-subtracted spectrum and "rms"
   does the root mean square. The calculation is done with unflagged
   channels only.

   Note that the SIGMA column is not updated; it keeps the values of
   the input MS data. In case the user wants to refer to the
   standard deviation of the output MS data, she or he needs to
   compute it using WEIGHT column values as :math:`1/\sqrt{WEIGHT}`
   - the SIGMA column should not be refered to.


   .. rubric:: Per-spectrum Fit Parameters

   Per-spectrum baseline fitting parameters can be applied when
   *blfunc = 'variable'*.

   The fitting parameters can be defined in a text file and
   specified in the *blparam* parameter. Each line of the text file
   should store baseline fitting parameters for its corresponding
   spectrum in the input MS. It must be a comma-separated text and
   contain values in the following order:

   (1) 'row': row index
   (2) 'pol': polarization index in the specified row
   (3) 'mask': channel range(s) used for the fitting (see examples below).
   (4) 'clipniter': maximum number of times of iterative fitting (identical to the task parameter *clipniter*)
   (5) 'clipthresh': clipping threshold for iterative fitting (identical to the task parameter *clipthresh*)
   (6) 'use_linefinder': "true" or "false". Note that linefinder does not run with per-spectrum fitting now even if setting "true", due to a bug which will be fixed in the future
   (7) 'thresh': S/N threshold for linefinder (identical to the task parameter *thresh*). Blank is accepted when you don't use linefinder
   (8) 'left_edge': channels to drop at beginning of spectrum (identical to the first element of the task parameter *edge*)
   (9) 'right_edge': channels to drop at end of spectrum (identical to the second element of the task parameter *edge*)
   (10) 'avg_limit': channel averaging for broad lines (identical to the task parameter *avg_limit*)
   (11) 'blfunc': baseline model function (identical to the task parameter *blfunc*)
   (12) 'order': order of polynomial function (identical to the task parameter *order*). Needed when (11) is "poly" or "chebyshev". It will be ignored when other values are set for blfunc
   (13) 'npiece': number of the element polynomials of cubic spline curve (identical to the task parameter *npiece*). Needed when (11) is "cspline"
   (14) 'nwave': a list of sinusoidal wave numbers. Needed when (11) is "sinusoid" though, actually, sinusoidal fitting is yet to be available with per-spectrum fitting

   Note that the following task parameters will be ignored/overwritten
   when *blfunc = 'variable'* is specified (i.e., when per-spectrum
   fitting is executed):

   - for iterative clipping: *clipniter*, *clipthresh*
   - for linefinder: *thresh*, *edge*, *avg_limit*
   - for baseline model function: *blfunc*, *order*, *npiece*, *applyfft*, *fftmethod*, *fftthresh*, *addwn*, *rejwn*

   Note also that:

   (1) lines starting with '#' will be ignored and can be used as
       comments
   (2) for MS spectra which have no corresponding line in the text
       file, baseline fitting is not executed

   Examples of text file:

   (1) a simple one:

   ::

      0,0,,2,3,false,,,,,poly,5,,[]
      0,1,1500~7500,0,3.,false,0.,0,0,0,chebyshev,10,0,[]
      1,0,,4,2.5,true,5.,70,80,3,cspline,,6,[]
      1,1,0~4000;6000~8000,0,,false,,,,,sinusoid,,,[0,1,2,3,4,5,6,7]
      #2,0,,0,,false,,,,,poly,10,,[]

   (2) same setting as (1), but with detailed comments:

   ::

      # for row 0, pol 0: no channel mask,
      #                   iterative (twice at maximum) clipping at 3 sigma,
      #                   no linefinder,
      #                   fitting with polynomial of order 5
      0,0,,2,3,false,,,,,poly,5,,[]
      # for row 0, pol 1: use channel range 1500 to 7500,
      #                   no iterative clipping (clipniter=0),
      #                   no linefinder,
      #                   fitting with Chebyshev polynomial of order 10
      0,1,1500~7500,0,3.,false,0.,0,0,0,chebyshev,10,0,[]
      # for row 1, pol 0: no channel mask,
      #                   iterative (4 times at maximum) clipping at 2.5 sigma,
      #                   using linefinder (thresh: 5.0 sigma,
      #                                     left_edge: 70 channels,
      #                                     right_edge: 80 channels,
      #                                     avg_limit: 3),
      #                   fitting with cubic spline with 6 elements
      1,0,,4,2.5,true,5.,70,80,3,cspline,,6,[]
      # for row 1, pol 1: use channel ranges (0 to 4000) and (6000 to 8000),
      #                   no iterative clipping,
      #                   no linefinder,
      #                   fitting with sinusoids with wave numbers up to 7
      1,1,0~4000;6000~8000,0,,false,,,,,sinusoid,,,[0,1,2,3,4,5,6,7]
      # for row 2, pol 0: no baseline fitting as the line is commented out
      #2,0,,0,,false,,,,,poly,10,,[]


.. _Examples:

Examples
   .. rubric::   Example 1

   This is one of the simplest examples. To fit and remove a
   Chebyshev polynomial function (default is of 5th order) from the
   data 'sd_data.ms', using only spectral window 0, and fitting
   channels 100-800 and 1200-2000 (to avoid, for example, band-pass
   roll off at the edges, and perhaps an emission line that might
   occur over channels 800-1200).

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

   .. rubric::  Example 5

   This example shows a polynomial baseline fitting, but without subtraction;
   instead, the fitting results are saved as a text file 'sd_data_blparam.txt'
   and a baseline table 'sd_data_blparam.bltable', which can be used for
   actual baseline subtraction afterwards (see also Example 6).

   ::

      sdbaseline(infile='sd_data.ms', blfunc='poly', dosubtract=False, blformat=['text','table'])

   .. rubric::  Example 6

   This example shows applying a baseline table to a MS to actually subtract
   the best-fit baseline.

   ::

      sdbaseline(infile='sd_data.ms', blmode='apply', bltable='sd_data_blparam.bltable',
                 outfile='sd_data.ms.bl')


.. _Development:

Development
   No additional development details

