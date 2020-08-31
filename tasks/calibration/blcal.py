#
# stub function definition file for docstring parsing
#

def blcal(vis, caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='scan', freqdep=False, calmode='ap', solnorm=False, gaintable=[''], gainfield=[''], interp=[''], spwmap=[''], parang=False):
    r"""
Calculate a baseline-based calibration solution (gain or bandpass)

Parameters
   - **vis** (string) - Name of input visibility file
   - **caltable** (string='') - Name of output gain calibration table
   - **field** (string='') - Select field using field id(s) or field name(s)
   - **spw** (string='') - Select spectral window/channels
   - **intent** (string='') - Select observing intent
   - **selectdata** (bool=True) - Other data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - **timerange** (string='') - Select data based on time range
      - **uvrange** (variant='') - Select data by baseline length.
      - **antenna** (string='') - Select data based on antenna/baseline
      - **scan** (string='') - Scan number range
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **msselect** (string='') - Optional complex data selection (ignore for now)

      .. raw:: html

         </details>
   - **solint** (variant='inf') - Solution interval
   - **combine** (string='scan') - Data axes which to combine for solve (obs, scan, spw, and/or field)
   - **freqdep** (bool=False) - Solve for frequency dependent solutions
   - **calmode** (string='ap') - Type of solution" (\'ap\', \'p\', \'a\')
   - **solnorm** (bool=False) - Normalize average solution amplitudes to 1.0
   - **gaintable** (stringArray=['']) - Gain calibration table(s) to apply on the fly
   - **gainfield** (stringArray=['']) - Select a subset of calibrators from gaintable(s)
   - **interp** (stringArray=['']) - Interpolation parameters for each gaintable, as a list
   - **spwmap** (intArray=['']) - Spectral window mappings to form for gaintable(s)
   - **parang** (bool=False) - Apply parallactic angle correction


Description
      .. rubric:: Summary
         :name: summary

      The **blcal** task determines baseline-based time- and/or
      frequency-dependent gains for all baselines in the data set. Such
      solutions are in contrast to **gaincal** and **bandpass**
      solutions which are antenna-based and better constrained.

      .. note:: In general, solving for and applying baseline-based calibration
         can be a very dangerous thing to do, since such non-closing
         corrections can fundamentally alter the otherwise unique source
         structure information obtained by an interferometer. Use of
         **blcal** should be approached with great care, after all
         antenna-based calibration options have been exhausted, and then
         only on long timescales, to ensure that the solution doesn't
         absorb true---or reinforce false---source structure. You must
         be sure you have an excellent model for the source (better than
         the magnitude of the baseline-dependent errors). In any case,
         **blcal** will, if used, usually mark the endpoint of a
         calibration scheme, reinforcing the current source model, and
         rendering any additional antenna-based calibration (e.g.,
         selfcal) less reliable. As such, it could be viewed as a mostly
         cosmetic last step in calibration.

      .. rubric:: Common calibration solve parameters
         :name: common-calibration-solve-parameters

      The **blcal** task uses all of the same parameters as gaincal and
      bandpass, which the exception of gaintype and bandtype,
      respectively. See `"Solving for
      Calibration" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__
      for general information about calibration solving parameters.

      .. rubric:: Controlling frequency-dependence in blcal: *freqdep*
         :name: controlling-frequency-dependence-in-blcal-freqdep

      The parameter *freqdep* controls whether or not a
      channel-dependent solution should be obtained. If *freqdep=True*,
      a channelized solution (like **bandpass**, but baseline-based)
      will be obtained; otherwise the solution will be unchannelized
      (like **gaincal**, but baseline-based).

    """
    pass
