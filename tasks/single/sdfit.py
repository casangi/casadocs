#
# stub function definition file for docstring parsing
#

def sdfit(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', timebin='', timespan='', polaverage='', fitfunc='gaussian', fitmode='list', nfit=[0], thresh=5.0, avg_limit=4, minwidth=4, edge=[0, 0], outfile='', overwrite=False):
    r"""
Fit a spectral line

Parameters
   - **infile** (string) - name of input SD dataset
   - **datacolumn** (string) - name of data column to be used ["data", "float_data", or "corrected_data"]
   - **antenna** (string) - select data by antenna name or ID, e.g. "PM03"
   - **field** (string) - select data by field IDs and names, e.g. "3C2*" (""=all)
   - **spw** (string) - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
   - **timerange** (string) - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   - **scan** (string) - select data by scan numbers, e.g. "21~23" (""=all)
   - **pol** (string) - select data by polarization IDs, e.g. "XX,YY" (""=all)
   - **intent** (string) - select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
   - **timebin** (string) - bin width for time averaging
   - **polaverage** (string) - polarization averaging mode ("", "stokes" or "geometric").
   - **fitfunc** (string) - function for fitting ["gaussian", "lorentzian"]
   - **fitmode** (string) - mode for setting additional channel masks. "list" and "auto" are available now.
   - **outfile** (string) - name of output file
   - **overwrite** (bool) - overwrite the output file if already exists [True, False]

Subparameters
   *timebin != ''*

   - **timespan** (string='') - span the timebin across "scan", "state", "field", or a combination of them (e.g., "scan,state")

   *fitmode = list*

   - **nfit** (intArray='') - list of number of lines to fit in maskline region.

   *fitmode = auto*

   - **thresh** (double=5.0) - S/N threshold for linefinder
   - **avg_limit** (int=4) - channel averaging for broad lines
   - **minwidth** (int=4) - the minimum channel width to detect as a line
   - **edge** (intArray='') - channels to drop at beginning and end of spectrum

   *fitmode = interact*

   - **nfit** (intArray='') - list of number of lines to fit in maskline region.


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

      | *thresh* -- [default 5] S/N threshold for linefinder.
      | *avg_limit* -- [default 4] channel averaging for broad lines. A
        number of consecutive channels up to this value will be averaged
        to search for broad lines
      | *minwidth* --[default: 4]  minimum number of consecutive
        channels required to pass threshold
      | *edge* -- [default 0] channels to drop at beginning and end of
        spectrum

      .. note:: **NOTE**: For bad baselines, *thresh* should be increased, and
         *avg_limit* decreased (or even switched off completely by
         setting this parameter to 1) to avoid detecting baseline
         undulations instead of real lines.

      Detailed output is directed to a log file identified by the
      '*outfile*' parameter.

    """
    pass
