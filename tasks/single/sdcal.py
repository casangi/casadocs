#
# stub function definition file for docstring parsing
#

def sdcal(infile, calmode='ps', fraction='10%', noff=-1, width=0.5, elongated=False, applytable='', interp='', spwmap='', outfile='', overwrite=False, field='', spw='', scan='', intent=''):
    r"""
 MS SD calibration task

Parameters
   - **infile** (string) - name of input SD dataset (must be MS)
   - **calmode** (string) - SD calibration mode ["ps","otfraster","otf","tsys","apply", and allowed combinations]
   - **field** (string) - select data by field IDs and names, e.g. "3C2*" ("" = all)
   - **spw** (string) - select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)
   - **scan** (string) - select data by scan numbers, e.g. "21~23" (""=all)

Subparameters
   *calmode = ps*

   - **outfile** (string='') - name of output file (See a WARNING in help)
   - **overwrite** (bool=False) - overwrite the output file if already exists [True, False]

   *calmode = otfraster*

   - **fraction** (variant=10%) - fraction of the OFF data to mark
   - **noff** (int=-1) - number of the OFF data to mark
   - **outfile** (string='') - name of output file (See a WARNING in help)
   - **overwrite** (bool=False) - overwrite the output file if already exists [True, False]
   - **intent** (string=OBSERVE_TARGET#ON_SOURCE) - select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)

   *calmode = otf*

   - **fraction** (variant=10%) - fraction of the OFF data to mark
   - **outfile** (string='') - name of output file (See a WARNING in help)
   - **overwrite** (bool=False) - overwrite the output file if already exists [True, False]
   - **intent** (string=OBSERVE_TARGET#ON_SOURCE) - select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)

   *calmode = tsys*

   - **outfile** (string='') - name of output file (See a WARNING in help)
   - **overwrite** (bool=False) - overwrite the output file if already exists [True, False]

   *calmode = apply*

   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.

   *calmode = ps,apply*

   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.

   *calmode = tsys,apply*

   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.

   *calmode = ps,tsys,apply*

   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.

   *calmode = otfraster,apply*

   - **fraction** (variant=10%) - fraction of the OFF data to mark
   - **noff** (int=-1) - number of the OFF data to mark
   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.
   - **intent** (string=OBSERVE_TARGET#ON_SOURCE) - select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)

   *calmode = otfraster,tsys,apply*

   - **fraction** (variant=10%) - fraction of the OFF data to mark
   - **noff** (int=-1) - number of the OFF data to mark
   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.

   *calmode = otf,apply*

   - **fraction** (variant=10%) - fraction of the OFF data to mark
   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.
   - **intent** (string=OBSERVE_TARGET#ON_SOURCE) - select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)

   *calmode = otf,tsys,apply*

   - **fraction** (variant=10%) - fraction of the OFF data to mark
   - **applytable** (variant='') - (List of) sky and/or tsys tables
   - **interp** (string='') - Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
   - **spwmap** (variant='') - A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.


Description
      | Task **sdcal** implements a single-dish data calibration scheme
        similar to that of interferometry, i.e., generate calibration
        tables (caltables) and apply them. Available calibration modes
        (*calmode*) are 'ps', 'otfraster', and 'otf' for sky (reference)
        calibration; and 'tsys' for :math:`T_{\rm sys}` calibration.
        Caltables can be applied to the data with *calmode* ='apply'.
        Each mode generates a caltable except for *calmode* ='apply'. A
        combination of mode keywords is also supported, e.g.,
        *calmode* ='ps,tsys,apply' to calibrate sky and
        :math:`T_{\rm sys}` on-the-fly. Calibration is available even
        for fast-moving sources like the Moon (see the note relating to
        the 'otf' mode below).
      | The calibration mode must be set in accordance with the
        observing mode of the data. The modes are as follows: 

      -  'ps': position switching (including OTF) with explicit
         reference (OFF) spectra
      -  'otfraster': raster OTF scan without explicit OFFs
      -  'otf': non-raster OTF scan without explicit OFFs

      | Thus, if the data contains explicit reference spectra, 'ps'
        should be used. Otherwise, 'otfraster' or 'otf' should be used.
      | In 'otfraster' and 'otf' modes, specific edge regions of the
        observation pattern are automatically marked as reference (OFF)
        spectra.
      | These specific regions are:

      -  in 'otfraster' mode: regions near the beginning and end of the
         raster scan lines.
      -  in 'otf' mode: regions near the periphery of the observation
         pattern.

      .. note:: **NOTE**: Although the 'otfraster' mode is designed for OTF
         observations without explicit OFF spectra, it should work even
         if explicit reference spectra exist. In that case, the OFF
         spectra are ignored and spectra identified by an edge marker
         are used as the reference.

      .. note:: **NOTE**: Detection of periphery scans in 'otf' mode is
         available for "ephemeris" sources, e.g., the Sun and Moon.
         Often, antennas will track these ephemeris sources so that the
         target source is always at the map center. For such
         observations, a periphery search is done in the source frame of
         the ephemeris source, so the observing target maintains its
         position in the map. For calibration in the 'otf' mode, higher
         order pointing interpolation has been implemented to get the
         pointing direction for each spectral data more appropriately.

      Apart from the way reference spectra are selected, the procedure
      to derive calibrated spectra is the same for all modes. Selected
      (or preset) OFF integrations contiguous in time are identified,
      averaged in each segment, and then interpolated to timestamps for
      ON integrations. Effectively, it means that OFF integrations are
      averaged by each OFF spectrum for 'ps' mode, and averaged by
      either ends of each raster row for 'otfraster' mode. Spectra are
      calibrated by:

      :math:`T_{\rm sys}  \frac{ ON - OFF } { OFF }`.

      .. note:: **NOTE**: If *outfile* is unset and *calmode* doesn't include
         "apply", a default names of calibration tables are generated
         based on the *infile* and a predefined suffix  ('_sky' for sky,
         '_tsys' for :math:`T_{\rm sys}`).

    """
    pass
