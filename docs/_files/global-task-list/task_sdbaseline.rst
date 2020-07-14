sdbaseline
==========

.. container:: documentDescription description

   task description

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

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
      baseline table to MS data.  For each spectrum in the MS, the
      best-fit baseline is reproduced from baseline parameters stored in
      the specified baseline table, and subtracted. Putting the "fit"
      and "subtract" into separate processes can be useful for pipeline
      processing of huge datasets.

       

      .. rubric:: Baseline Model Functions 
         :name: baseline-model-functions

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
      mask, clipniter, clipthresh, use_linefinder,  thresh, left edge,
      right edge, avg_limit, blfunc, order, npiece, nwave. Each row in
      the text file must contain the following keywords and values:

      -  'row': row number after selection
      -  'pol': polarization index in the row
      -  'clipniter': maximum iteration number for iterative fitting
      -  'blfunc': function name.  available options are 'poly',
         'chebyshev', 'cspline',and 'sinusoid'
      -  'order': maximum order of the polynomial. Needed when
         blfunc='poly' or 'chebyshev'
      -  'npiece': number of piecewise polynomials. Needed when
         blfunc='cspline'
      -  'nwave': a list of sinusoidal wave numbers. Needed when
         blfunc='sinusoid'

       

      .. rubric:: Output Files 
         :name: output-files

      | The task outputs the baseline-subtracted MS data set.  Users
        should specify the output data file name with the *outfile*
        keyword. 
      | Also, the fit parameters, terms, and rms of the baseline can be
        saved into an ascii text file (in human-readable format or CSV
        format) or a baseline table (a CASA table). By default, a text
        file named  <infile name> + '\_ blparam.txt' is output. The
        saved baseline table can be used later to subtract the baselines
        from an MS.

       

      .. rubric:: Fitting and Clipping
         :name: fitting-and-clipping

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

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_sdbaseline/changelog
   task_sdbaseline/examples
