#
# stub function definition file for docstring parsing
#

def sdbaseline(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, maskmode='list', thresh=5.0, avg_limit=4, minwidth=4, edge=[0, 0], blmode='fit', dosubtract=True, blformat='text', bloutput='', bltable='', blfunc='poly', order=5, npiece=2, applyfft=True, fftmethod='fft', fftthresh=3.0, addwn=[0], rejwn=[''], clipthresh=3.0, clipniter=0, blparam='', verbose=False, showprogress=False, minnrow=1000, outfile='', overwrite=False):
    r"""
Fit/subtract a spectral baseline 

Parameters
   - infile_ (string) - name of input SD dataset
   - datacolumn_ (string='data') - name of data column to be used ["data", "float_data", or "corrected"]
   - antenna_ (string='') - select data by antenna name or ID, e.g. "PM03"
   - field_ (string='') - select data by field IDs and names, e.g. "3C2*" (""=all)
   - spw_ (string='') - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
   - timerange_ (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   - scan_ (string='') - select data by scan numbers, e.g. "21~23" (""=all)
   - pol_ (string='') - select data by polarization IDs, e.g. "XX,YY" (""=all)
   - intent_ (string='') - select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
   - reindex_ (bool=True) - Re-index indices in subtables based on data selection
   - maskmode_ (string='list') - mode of setting additional channel masks

      .. raw:: html

         <details><summary><i> maskmode = auto </i></summary>

      - thresh_ (double=5.0) - S/N threshold for linefinder
      - avg_limit_ (int=4) - channel averaging for broad lines
      - minwidth_ (int=4) - the minimum channel width to detect as a line
      - edge_ (intArray=[0, 0]) - channels to drop at beginning and end of spectrum

      .. raw:: html

         </details>
   - blmode_ (string='fit') - baselining mode ["fit" or "apply"]

      .. raw:: html

         <details><summary><i> blmode = fit </i></summary>

      - dosubtract_ (bool=True) - subtract baseline from input data [True, False] 
      - blformat_ ({string, stringArray}='text') - format(s) of file(s) in which best-fit parameters are written
      - bloutput_ ({string, stringArray}='') - name(s) of file(s) in which best-fit parameters are written

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> blmode = apply </i></summary>

      - bltable_ (string='') - name of baseline table to apply

      .. raw:: html

         </details>
   - blfunc_ (string='poly') - baseline model function

      .. raw:: html

         <details><summary><i> blfunc = poly </i></summary>

      - order_ (int=5) - order of baseline model function
      - clipthresh_ (double=3.0) - clipping threshold for iterative fitting
      - clipniter_ (int=0) - maximum iteration number for iterative fitting

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> blfunc = chebyshev </i></summary>

      - order_ (int=5) - order of baseline model function
      - clipthresh_ (double=3.0) - clipping threshold for iterative fitting
      - clipniter_ (int=0) - maximum iteration number for iterative fitting

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> blfunc = cspline </i></summary>

      - npiece_ (int=2) - number of element polynomials for cubic spline curve
      - clipthresh_ (double=3.0) - clipping threshold for iterative fitting
      - clipniter_ (int=0) - maximum iteration number for iterative fitting

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> blfunc = sinusoid </i></summary>

      - applyfft_ (bool=True) - automatically set wave numbers of sinusoids
      - fftmethod_ (string='fft') - method for automatically set wave numbers of sinusoids ["fft"]
      - fftthresh_ (double=3.0) - threshold to select wave numbers of sinusoids
      - addwn_ (intArray=[0]) - additional wave numbers to use
      - rejwn_ (intArray=['']) - wave numbers NOT to use
      - clipthresh_ (double=3.0) - clipping threshold for iterative fitting
      - clipniter_ (int=0) - maximum iteration number for iterative fitting

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> blfunc = variable </i></summary>

      - blparam_ (string='') - text file that stores per spectrum fit parameters
      - verbose_ (bool=False) - output fitting parameters to logger [True, False]

      .. raw:: html

         </details>
   - showprogress_ (bool=False) - (NOT SUPPORTED YET) show progress status for large data [True, False] (NOT SUPPORTED YET)

      .. raw:: html

         <details><summary><i> showprogress = True </i></summary>

      - minnrow_ (int=1000) - (NOT SUPPORTED YET) minimum number of input spectra to show progress status

      .. raw:: html

         </details>
   - outfile_ (string='') - name of output file
   - overwrite_ (bool=False) - overwrite the output file if already exists [True, False] 


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
   baseline table to MS data. For each spectrum in the MS, the
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
   mask, clipniter, clipthresh, use_linefinder, thresh, left edge,
   right edge, avg_limit, blfunc, order, npiece, nwave. Each row in
   the text file must contain the following keywords and values:

   -  'row': row number after selection
   -  'pol': polarization index in the row
   -  'clipniter': maximum iteration number for iterative fitting
   -  'blfunc': function name. available options are 'poly',
      'chebyshev', 'cspline',and 'sinusoid'
   -  'order': maximum order of the polynomial. Needed when
      blfunc='poly' or 'chebyshev'
   -  'npiece': number of piecewise polynomials. Needed when
      blfunc='cspline'
   -  'nwave': a list of sinusoidal wave numbers. Needed when
      blfunc='sinusoid'

   

   .. rubric:: Output Files
      

   | The task outputs the baseline-subtracted MS data set. Users
     should specify the output data file name with the *outfile*
     keyword.
   | Also, the fit parameters, terms, and rms of the baseline can be
     saved into an ascii text file (in human-readable format or CSV
     format) or a baseline table (a CASA table). By default, a text
     file named <infile name> + '\_ blparam.txt' is output. The
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




Details
   Explanation of each parameter

.. _infile:

   .. rubric:: infile

   | name of input SD dataset

.. _datacolumn:

   .. rubric:: datacolumn

   | name of data column to be used ["data", "float_data", or "corrected"]

.. _antenna:

   .. rubric:: antenna

   | select data by antenna name or ID, e.g. "PM03"

.. _field:

   .. rubric:: field

   | select data by field IDs and names, e.g. "3C2*" (""=all)

.. _spw:

   .. rubric:: spw

   | select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)

.. _timerange:

   .. rubric:: timerange

   | select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)

.. _scan:

   .. rubric:: scan

   | select data by scan numbers, e.g. "21~23" (""=all)

.. _pol:

   .. rubric:: pol

   | select data by polarization IDs, e.g. "XX,YY" (""=all)

.. _intent:

   .. rubric:: intent

   | select data by observational intent, e.g. "*ON_SOURCE*" (""=all)

.. _reindex:

   .. rubric:: reindex

   | Re-index indices in subtables based on data selection. Ignored when blmode='apply'.

.. _maskmode:

   .. rubric:: maskmode

   | mode of setting additional channel masks. "list" and "auto" are available now.

.. _thresh:

   .. rubric:: thresh

   | S/N threshold for linefinder

.. _avg_limit:

   .. rubric:: avg_limit

   | channel averaging for broad lines

.. _minwidth:

   .. rubric:: minwidth

   | the minimum channel width to detect as a line

.. _edge:

   .. rubric:: edge

   | channels to drop at beginning and end of spectrum

.. _blmode:

   .. rubric:: blmode

   | baselining mode ["fit" or "apply"]

.. _dosubtract:

   .. rubric:: dosubtract

   | subtract baseline from input data [True, False]

.. _blformat:

   .. rubric:: blformat

   | format(s) of file(s) in which best-fit parameters are written ["text", "csv", "table" or ""]

.. _bloutput:

   .. rubric:: bloutput

   | name(s) of file(s) in which best-fit parameters are written

.. _bltable:

   .. rubric:: bltable

   | name of baseline table to apply

.. _blfunc:

   .. rubric:: blfunc

   | baseline model function ["poly", "chebyshev", "cspline", "sinusoid", or "variable"(expert mode)]

.. _order:

   .. rubric:: order

   | order of baseline model function

.. _npiece:

   .. rubric:: npiece

   | number of element polynomials for cubic spline curve

.. _applyfft:

   .. rubric:: applyfft

   | automatically set wave numbers of sinusoids

.. _fftmethod:

   .. rubric:: fftmethod

   | method for automatically set wave numbers of sinusoids

.. _fftthresh:

   .. rubric:: fftthresh

   | threshold to select wave numbers of sinusoids

.. _addwn:

   .. rubric:: addwn

   | additional wave numbers to use

.. _rejwn:

   .. rubric:: rejwn

   | wave numbers NOT to use

.. _clipthresh:

   .. rubric:: clipthresh

   | clipping threshold for iterative fitting

.. _clipniter:

   .. rubric:: clipniter

   | maximum iteration number for iterative fitting

.. _blparam:

   .. rubric:: blparam

   | text file that stores per spectrum fit parameters

.. _verbose:

   .. rubric:: verbose

   | output fitting parameters to logger

.. _showprogress:

   .. rubric:: showprogress

   | (NOT SUPPORTED YET) show progress status for large data

.. _minnrow:

   .. rubric:: minnrow

   | (NOT SUPPORTED YET) minimum number of input spectra to show progress status

.. _outfile:

   .. rubric:: outfile

   | name of output file

.. _overwrite:

   .. rubric:: overwrite

   | overwrite the output file if already exists


    """
    pass
