#
# stub function definition file for docstring parsing
#

def accor(vis, caltable='', field='', spw='', intent='', selectdata=True, timerange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='', append=False, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=['']):
    r"""
Normalize visibilities based on auto-correlations

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
      - **antenna** (string='') - Select data based on antenna/baseline
      - **scan** (string='') - Scan number range
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **msselect** (string='') - Optional complex data selection (ignore for now)

      .. raw:: html

         </details>
   - **solint** (variant='inf') - Solution interval: egs. \'inf\', \'60s\' (see help)
   - **combine** (string='') - Data axes which to combine for solve (obs, scan, spw, and/or field)
   - **append** (bool=False) - Append solutions to the (existing) table
   - **docallib** (bool=False) - Use callib or traditional cal apply parameters

      .. raw:: html

         <details><summary><i> docallib = False </i></summary>

      - **gaintable** (stringArray=['']) - Gain calibration table(s) to apply on the fly
      - **gainfield** (stringArray=['']) - Select a subset of calibrators from gaintable(s)
      - **interp** (stringArray=['']) - Interpolation parameters for each gaintable, as a list
      - **spwmap** (intArray=['']) - Spectral windows combinations to form for gaintables(s)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> docallib = True </i></summary>

      - **callib** (string='') - Cal Library filename

      .. raw:: html

         </details>


Description
   .. rubric:: Summary
      

   .. warning:: **WARNING: accor** is currently an experimental task. Use with
      care and report issues back to the CASA team via the `NRAO
      helpdesk <http://help.nrao.edu>`__.

   **accor** determines the amplitude calibration from
   auto-correlations.

   The **accor** task determines the amplitude corrections from the
   apparent normalization of the mean autocorrelation spectra.
   Mis-normalization of the autocorrelations (and thus also the
   cross-correlations) is caused by errors in sampler thresholds
   during an observation. This correction is typically required for
   data correlated with the DiFX correlator (such as VLBA data).
   Other correlators (such as the SFXC correlator, which is used to
   correlate EVN data at JIVE) may already apply this correction at
   the correlator. In these cases, running this task is not necessary
   (but shouldn't hurt).

   The **accor** task should be run with a solution interval
   (*solint*) adequate to track variations in effective sampler level
   optimization (including resets), typically on timescales of
   seconds to minutes.

   See `Solving for
   Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__for
   more information on the task parameters **accor** shares with all
   calibration solving tasks, including data selection, general
   solving properties, and arranging prior calibration
   (i.e.,specifying other caltables to pre-apply before solving). In
   most cases, no prior calibration is required, since the raw
   mis-normalization of the autocorrelations is essentially the
   calibration sought from **accor**.

    """
    pass
