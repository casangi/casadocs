#
# stub function definition file for docstring parsing
#

def fluxscale(vis, caltable='', fluxtable='', reference=[''], transfer=[''], listfile='', append=False, refspwmap=[-1], gainthreshold=-1.0, antenna='', timerange='', scan='', incremental=False, fitorder=1, display=False):
    r"""
Bootstrap the flux density scale from standard calibrators

Parameters
   - vis_ (string) - Name of input visibility file
   - caltable_ (string='') - Name of input calibration table
   - fluxtable_ (string='') - Name of output, flux-scaled calibration table (required)
   - reference_ (stringArray=['']) - Reference field name(s) (transfer flux scale FROM)
   - transfer_ (stringArray=['']) - Transfer field name(s) (transfer flux scale TO), \'\' -> all
   - listfile_ (string='') - Name of listfile that contains the fit information.  Default is '' (no file).
   - append_ (bool=False) - Append solutions?
   - refspwmap_ (intArray=[-1]) - Scale across spectral window boundaries
   - gainthreshold_ (double=-1.0) - Threshold (fractional deviation from the median) on gain amplitudes to be used in the flux scale calculation
   - antenna_ (string='') - Select data based on antenna/baseline
   - incremental_ (bool=False) - Incremental caltable
   - fitorder_ (int=1) - Order of spectral fitting
   - display_ (bool=False) - Display some statistics of flux scaling


Description
   Summary: The *'G'* or *'T'* solutions obtained by **gaincal** for
   calibrators for which the flux density was unknown and assumed to
   be 1 Jansky are correct in a time- and antenna- relative sense,
   but are mis-scaled by a factor equal to the inverse of the square
   root of the true flux density. This scaling can be corrected by
   enforcing the constraint that mean gain amplitudes determined from
   calibrators of unknown flux density should be the same as
   determined from those with known flux densities. The **fluxscale**
   task exists for this purpose.

   Before running **fluxscale**, one must have first run **setjy**
   for the reference sources and run a **gaincal** that includes
   reference and transfer fields. The reference field(s) should be
   standard flux density calibrators for which an accurate flux
   density (or better, a model image, especially if it is a resolved
   source) is known. The transfer fields are all other calibrators,
   typically point sources (to a good approximation), and for which
   actual flux density is unknown. When running **fluxscale**, the
   input*caltable*will be scaled and written out into the
   output*fluxtable*such that the correct scaling will be applied
   to the transfer sources. The*fluxtable*parameter is required,
   and if it is already present, it will not be overwritten.The user
   can set *append* =True to append the flux-scaled results to the
   existing table. If *incremental=True,* a simple incremental
   calibration table will be generated that contains a single
   antenna-based solution per field embodying the required scale
   factors. If *incremental=False,* a copy of the input caltable is
   generated, with the required scale factors applied to the transfer
   fields.

   **fluxscale** applies the constraint that net system gain was, in
   fact, independent of field, time, and direction, on average, and
   that field-dependent gains in the input caltable are solely a
   result of the unknown flux densities for the calibrators. Using
   time-averaged gain amplitudes, the ratio between each ordinary
   calibrator and the flux density calibrator(s) is formed for each
   antenna and polarization (which they have in common). The average
   of this ratio over antennas and polarizations yields a correction
   factor that is applied to the ordinary calibrators' gains.

   The square of the gain correction factor for each calibrator and
   spw is the presumed flux density of that calibrator (if the
   assumed flux density when solving was 1 Jy), and is reported in
   the logger. The errors reported with this value reflect the
   scatter in gain ratio over antennas and polarizations, divided by
   the square root of the number of antennas and polarizations
   available. If the flux densities for multiple spws exist, fitted
   spectral index and (for nspw>2) curvature are also reported. The
   fit is done for

   :math:`log(S_\nu) = a_o + a_1*(log(\nu/\nu_0)) + a_2*(log(\nu/\nu_0))**2`.

   The reference frequency, :math:`\nu_0` (the mean of
   :math:`log(\nu)`) is reported in the logger along with the flux
   density at that frequency. The fit results are also reported in
   the returned Python dictionary which takes the form:

   ::

      | {fieldIdstr: {spwIdstr: {'fluxd':array([I,Q,U,V]),
      |  'fluxdErr': corresponding errors,
      |  'numSol': corresponding no. of
        solutions}
      |  'fieldName': field name,
      |  'fitFluxd': fitted flux density at the
        reference frequency,
      |  'fitFluxdErr': fitted flux density error,
      |  'fitRefFreq': reference frequency,
      |        'covarMat': covariance matrix for the fit,
      |  'spidx': a_0, a_1, a_2
      |  'spidxerr': errors in a_0,a_1, a_2}
      | 'freq': (center) spw frequencies
      | 'spwID': list of spw IDs,
      | 'spwName': list of spw names}

   where fieldIdstr and spwIdstr are field Id and spw Id in string
   type, respectively. The 'spidx' coefficients, :math:`a_0`,
   :math:`a_1`, and :math:`a_2` are the :math:`log(S_{\nu=\nu0})`,
   the spectral index, and the curvature, respectively. If only a
   single spectral window is present, no fitting is performed but
   fitFluxd and fitRefFreq are filled with the values from fluxd and
   freq, respectively.

   The calibrator models are currently not revised within the MS to
   reflect the flux densities derived by **fluxscale**. Use **setjy**
   to set these, if necessary.

   The constant gain constraint is usually a reasonable assumption
   for the electronic systems on typical antennas. It is important
   that external time- and/or elevation-dependent effects are
   separately accounted for when solving for the gain solution
   supplied to **fluxscale**, e.g., gain curves, opacity, etc. (see
   **gencal**).

   The **fluxscale** results can also be degraded by poor pointing
   during the observation. The parameters, *gainthreshold* and
   *antenna* (and *timerange*/*scan*) can be used to control the data
   to be used in the flux derivation in such cases. Please note that,
   regardless of the antennas that are selected for deriving the
   scaling, the scaling solution is applied to all valid
   (non-flagged) antennas. The *gainthreshold* parameter sets the
   range of the input gain to be used in terms of the fractional
   deviation from their median values (per field, per spectral
   window).

   If the reference and transfer fields were observed in different
   spectral windows, the *refspwmap* parameter may be used to achieve
   the scaling calculation across spectral window boundaries. In
   general, this will yield less accurate flux density calibration.

   The **fluxscale** task can be executed on either *'G'* or *'T'*
   solutions, but it should only be used on one of these types if
   solutions exist for both and one was solved relative to the other
   (use **fluxscale** only on the first of the two).

   .. warning:: **ALERT:** *'GSPLINE'* solutions from **gaincal** are not
      supported in **fluxscale**.

   

   .. rubric:: Using resolved calibrators
      

   If the flux density calibrator is resolved, the assumption that it
   is a point source will cause solutions on outlying antennas to be
   biased in amplitude. In turn, the **fluxscale** step will be
   biased. In general, it is best to use a model for the calibrator,
   but if such a model is not available, it is important to limit the
   solution on the flux density calibrator to only the subset of
   antennas that have baselines short enough that the point-source
   assumption is valid. Such a subset of antennas can be selected for
   the **fluxscale** calculation using the *antenna* parameter, which
   uses standard antenna-selection syntax. Specifying something in
   *antenna* also reveals *timerange* and *scan* selection parameters
   which enable more specific selection on these axes.

   Alternatively, limiting the **fluxscale** calculation to antennas
   on unresolved baselines can be effected by using *antenna* and
   *uvrange* selection when solving for the flux density calibrator
   in **gaincal**. Please see the Examples section.




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _caltable:

   .. rubric:: caltable

   | Name of input calibration table
   |                      Default: none
   | 
   |                         Example: caltable='ngc5921.gcal'. This cal
   |                         table was obtained from task gaincal.=

.. _fluxtable:

   .. rubric:: fluxtable

   | Name of output, flux-scaled calibration table (required)
   |                      Default: none
   | 
   |                         Example: fluxtable='ngc5921.gcal2'
   | 
   |                      The gains in this table have been adjusted by the
   |                      derived flux density each calibrator.  The
   |                      MODEL_DATA column has NOT been updated for the
   |                      flux density of the calibrator.  Use setjy to do
   |                      this if it is a point source.

.. _reference:

   .. rubric:: reference

   | Reference field name(s) (transfer flux scale FROM)
   |                      Default: none
   | 
   |                         Example: reference='1328+307'
   | 
   |                      The names of the fields with a known flux
   |                      densities or visibilities that have been placed
   |                      in the MODEL column by setjy or ft for a model
   |                      not in the CASA system. The syntax is similar to
   |                      field.  Hence field index or names can be used.

.. _transfer:

   .. rubric:: transfer

   | Transfer field name(s) (transfer flux scale TO)
   |                      Default: '' (all sources in caltable that are not
   |                      specified as reference sources.  Do not include
   |                      unknown target sources)
   | 
   |                      The names of the fields with unknown flux
   |                      densities. These should be point-like calibrator
   |                      sources The syntax is similar to field.  Hence
   |                      source index or names can be used.
   | 
   |                         Examples: transfer='1445+099, 3C84'; transfer
   |                         = '0,4'
   | 
   |                      NOTE: All fields in reference and transfer must
   |                      have solutions in the caltable.

.. _listfile:

   .. rubric:: listfile

   | Name of listfile that contains the fit information.
   |                      Default: '' (no fit listfile will be created)
   | 
   |                      The list file contains the flux density, flux
   |                      density error, S/N, and number of solutions (all
   |                      antennas and feeds) for each spectral window.  
   |                      NOTE: The nominal spectral window frequencies
   |                      will be included in the future.

.. _append:

   .. rubric:: append

   | Append fluxscaled solutions to the fluxtable?
   |                      Default: False (the fluxtable must not exist)
   |                      Options: False|True

.. _refspwmap:

   .. rubric:: refspwmap

   | Vector of spectral windows enabling scaling across
   | spectral windows
   |                      Default: [-1] (none)
   | 
   |                         Example with 4 spectral windows:
   |                         If the reference fields were observed only in
   |                         spw=1 and 3, and the transfer fields were
   |                         observed in all 4 spws (0,1,2,3), specify
   |                         refspwmap=[1,1,3,3]. This will ensure that
   |                         transfer fields observed in spws 0,1,2,3 will
   |                         be referenced to reference field solutions
   |                         only in spw 1 or 3.

.. _gainthreshold:

   .. rubric:: gainthreshold

   | Threshold in the input gain solutions to be used in fractional deviation from median values.
   |                      Default: -1 (no threshold)
   | 
   |                         Example: gainthreshold=0.15 (only used the
   |                         gain solutions within 15% (inclusive) of the
   |                         median gain value (per field and per spw).

.. _antenna:

   .. rubric:: antenna

   | Select data based on antenna/baseline
   |                      Subparameter of antenna
   |                      Default: '' (all)
   | 
   |                      If antenna string is a non-negative integer, it
   |                      is assumed an antenna index, otherwise, it is
   |                      assumed as an antenna name
   |   
   |                          Examples: 
   |                          antenna='5&6'; baseline between antenna
   |                          index 5 and index 6.
   |                          antenna='VA05&VA06'; baseline between VLA
   |                          antenna 5 and 6.
   |                          antenna='5&6;7&8'; baselines with
   |                          indices 5-6 and 7-8
   |                          antenna='5'; all baselines with antenna index
   |                          5
   |                          antenna='05'; all baselines with antenna
   |                          number 05 (VLA old name)
   |                          antenna='5,6,10'; all baselines with antennas
   |                          5,6,10 index numbers

.. _timerange:

   .. rubric:: timerange

   | Select data based on time range
   |                      Subparameter of antenna
   |                      Default = '' (all)
   | 
   |                         Examples:
   |                         timerange =
   |                         'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
   |                         (Note: if YYYY/MM/DD is missing date defaults
   |                         to first day in data set.)
   |                         timerange='09:14:0~09:54:0' picks 40 min on
   |                         first day 
   |                         timerange= '25:00:00~27:30:00' picks 1 hr to 3
   |                         hr 30min on NEXT day
   |                         timerange='09:44:00' pick data within one
   |                         integration of time
   |                         timerange='>10:24:00' data after this time

.. _scan:

   .. rubric:: scan

   | Scan number range
   |                      Subparameter of antenna
   |                      Default: '' = all

.. _incremental:

   .. rubric:: incremental

   | Create an incremental caltable containing only gain
   | correction factors ( flux density= 1/(gain correction factor)**2)?
   |                      Default: False
   |                      Options: False|True
   | 
   |                         Example: incremental=True (output a caltable
   |                         containing flux scale factors.)
   | 
   |                      NOTE: If you use the incremental option, note
   |                      that BOTH this incremental fluxscale table AND an
   |                      amplitude vs. time table should be supplied in
   |                      applycal.

.. _fitorder:

   .. rubric:: fitorder

   | Polynomial order of the spectral fitting for valid flux
   | densities
   |                      Default: 1
   | 
   |                      It falls back to a lower fitorder if there are
   |                      not enough solutions to fit with the requested
   |                      fitorder.

.. _display:

   .. rubric:: display

   | Display statistics and/or spectral fitting results.
   |                      Default: False
   |                      Options: False|True
   | 
   |                      Currently only a histogram of the correction
   |                      factors to derive the final flux density for each
   |                      spectral window will be plotted.


    """
    pass
