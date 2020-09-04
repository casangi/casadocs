#
# stub function definition file for docstring parsing
#

def blcal(vis, caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='scan', freqdep=False, calmode='ap', solnorm=False, gaintable=[''], gainfield=[''], interp=[''], spwmap=[''], parang=False):
    r"""
Calculate a baseline-based calibration solution (gain or bandpass)

Parameters
   - **vis** (string) - Name of input visibility file [1]_
   - **caltable** (string='') - Name of output gain calibration table [2]_
   - **field** (string='') - Select field using field id(s) or field name(s) [3]_
   - **spw** (string='') - Select spectral window/channels [4]_
   - **intent** (string='') - Select observing intent [5]_
   - **selectdata** (bool=True) - Other data selection parameters [6]_

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - **timerange** (string='') - Select data based on time range [7]_
      - **uvrange** (variant='') - Select data by baseline length. [8]_
      - **antenna** (string='') - Select data based on antenna/baseline [9]_
      - **scan** (string='') - Scan number range [10]_
      - **observation** ({string, int}='') - Select by observation ID(s) [11]_
      - **msselect** (string='') - Optional complex data selection (ignore for now) [12]_

      .. raw:: html

         </details>
   - **solint** (variant='inf') - Solution interval [13]_
   - **combine** (string='scan') - Data axes which to combine for solve (obs, scan, spw, and/or field) [14]_
   - **freqdep** (bool=False) - Solve for frequency dependent solutions [15]_
   - **calmode** (string='ap') - Type of solution" (\'ap\', \'p\', \'a\') [16]_
   - **solnorm** (bool=False) - Normalize average solution amplitudes to 1.0 [17]_
   - **gaintable** (stringArray=['']) - Gain calibration table(s) to apply on the fly [18]_
   - **gainfield** (stringArray=['']) - Select a subset of calibrators from gaintable(s) [19]_
   - **interp** (stringArray=['']) - Interpolation parameters for each gaintable, as a list [20]_
   - **spwmap** (intArray=['']) - Spectral window mappings to form for gaintable(s) [21]_
   - **parang** (bool=False) - Apply parallactic angle correction [22]_


Description
   .. rubric:: Summary
      

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
      

   The **blcal** task uses all of the same parameters as gaincal and
   bandpass, which the exception of gaintype and bandtype,
   respectively. See `"Solving for
   Calibration" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__
   for general information about calibration solving parameters.

   .. rubric:: Controlling frequency-dependence in blcal: *freqdep*
      

   The parameter *freqdep* controls whether or not a
   channel-dependent solution should be obtained. If *freqdep=True*,
   a channelized solution (like **bandpass**, but baseline-based)
   will be obtained; otherwise the solution will be unchannelized
   (like **gaincal**, but baseline-based).




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file
      |                      Default: none
      | 
      |                         Example: vis='ngc5921.ms'
.. [2] 
   **caltable** (string='')
      | Name of output gain calibration table
      |                      Default: none
      | 
      |                         Example: caltable='ngc5921.gcal'
.. [3] 
   **field** (string='')
      | Select field using field id(s) or field name(s)
      |                      Default: '' (all fields)
      |                      
      |                      Use 'go listobs' to obtain the list id's or
      |                      names. If field string is a non-negative integer,
      |                      it is assumed a field index,  otherwise, it is
      |                      assumed a field name.
      | 
      |                         Examples:
      |                         field='0~2'; field ids 0,1,2
      |                         field='0,4,5~7'; field ids 0,4,5,6,7
      |                         field='3C286,3C295'; field named 3C286 and
      |                         3C295
      |                         field = '3,4C*'; field id 3, all names
      |                         starting with 4C
.. [4] 
   **spw** (string='')
      | Select spectral window/channels
      |                      Default: '' (all spectral windows and channels)
      | 
      |                         Examples:
      |                         spw='0~2,4'; spectral windows 0,1,2,4 (all
      |                         channels)
      |                         spw='<2';  spectral windows less than 2
      |                         (i.e. 0,1)
      |                         spw='0:5~61'; spw 0, channels 5 to 61,
      |                         INCLUSIVE
      |                         spw='*:5~61'; all spw with channels 5 to 61
      |                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
      |                         3, channels 3 to 45.
      |                         spw='0~2:2~6'; spw 0,1,2 with channels 2
      |                         through 6 in each.
      |                         spw='0:0~10;15~60'; spectral window 0 with
      |                         channels 0-10,15-60. (NOTE ';' to separate
      |                         channel selections)
      |                         spw='0:0~10^2,1:20~30^5'; spw 0, channels
      |                         0,2,4,6,8,10, spw 1, channels 20,25,30
.. [5] 
   **intent** (string='')
      | Select observing intent
      |                      Default: '' (no selection by intent)
      | 
      |                         Example: intent='*BANDPASS*'  (selects data
      |                         labelled with BANDPASS intent)
.. [6] 
   **selectdata** (bool=True)
      | Other data selection parameters
      |                      Default: True
      |                      Options: True|False
.. [7] 
   **timerange** (string='')
      | Select data based on time range
      |                      Subparameter of selectdata=True
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
.. [8] 
   **uvrange** (variant='')
      | Select data by baseline length.
      |                      Default = '' (all)
      | 
      |                         Examples:
      |                         uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
      |                         uvrange='>4klambda';uvranges greater than 4 kilo-lambda
      |                         uvrange='0~1000km'; uvrange in kilometers
.. [9] 
   **antenna** (string='')
      | Select data based on antenna/baseline
      |                      Subparameter of selectdata=True
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
.. [10] 
   **scan** (string='')
      | Scan number range
      |                      Subparameter of selectdata=True
      |                      Default: '' = all
.. [11] 
   **observation** ({string, int}='')
      | Select by observation ID(s)
      |                      Subparameter of selectdata=True
      |                      Default: '' = all
      | 
      |                          Example: observation='0~2,4'
.. [12] 
   **msselect** (string='')
      | Optional complex data selection (ignore for now)
.. [13] 
   **solint** (variant='inf')
      | Solution interval
      |                      Default: 'inf' (infinite, up to boundaries
      |                      controlled by combine); 
      |                      Options: 'inf' (~infinite), 'int' (per
      |                      integration), any float or integer value with or
      |                      without units
      | 
      |                         Examples: 
      |                         solint='1min'; solint='60s', solint=60 (i.e.,
      |                         1 minute); solint='0s'; solint=0; solint='int'
      |                         (i.e., per integration); solint-'-1s';
      |                         solint='inf' (i.e., ~infinite, up to
      |                         boundaries enforced by combine)
.. [14] 
   **combine** (string='scan')
      | Data axes which to combine for solve
      |                      Default: 'scan' (solutions will break at obs,
      |                      field, and spw boundaries, but may extend over
      |                      multiple scans [per obs, field, and spw] up to
      |                      solint.)
      |                      Options: '','obs','scan','spw',field', or any
      |                      comma-separated combination in a single string
      | 
      |                         Example: combine='scan,spw' - Extend solutions
      |                         over scan boundaries (up to the solint), and
      |                         combine spws for solving
.. [15] 
   **freqdep** (bool=False)
      | Solve for frequency dependent solutions
      |                      Default: False (gain; True=bandpass)
      |                      Options: False|True
.. [16] 
   **calmode** (string='ap')
      | Type of solution" ('ap', 'p', 'a')
      |                      Default: 'ap' (amp and phase)
      |                      Options: 'p' (phase) ,'a' (amplitude), 'ap'
      |                      (amplitude and phase)
      | 
      |                         Example: calmode='p'
.. [17] 
   **solnorm** (bool=False)
      | Normalize average solution amplitudes to 1.0
      |                      Default: False (no normalization)
      | 
      |                      For freqdep=False, this is a global (per-spw)
      |                      normalization of amplitudes (only). For
      |                      freqdep=True, each baseline  solution spectrum is
      |                      separately normalized by its (complex) mean.
.. [18] 
   **gaintable** (stringArray=[''])
      | Gain calibration table(s) to apply on the fly
      |                      Default: '' (none)
      | 
      |                         Examples: 
      |                         gaintable='ngc5921.gcal'
      |                         gaintable=['ngc5921.ampcal','ngc5921.phcal']
.. [19] 
   **gainfield** (stringArray=[''])
      | Select a subset of calibrators from gaintable(s)
      |                      Default: '' (all sources on the sky)
      | 
      |                      'nearest' ==> nearest (on sky) available field in
      |                      table otherwise, same syntax as field
      | 
      |                         Examples: 
      |                         gainfield='0~3'
      |                         gainfield=['0~3','4~6']
.. [20] 
   **interp** (stringArray=[''])
      | Interpolation parmameters (in time[,freq]) for each gaintable, as a list of strings.
      |                      Default: '' --> 'linear,linear' for all gaintable(s)
      |                      Options: Time: 'nearest', 'linear'
      |                               Freq: 'nearest', 'linear', 'cubic',
      |                               'spline'
      |                    Specify a list of strings, aligned with the list of caltable specified
      |                    in gaintable, that contain the required interpolation parameters
      |                    for each caltable.
      |                    * When frequency interpolation is relevant (B, Df,
      |                      Xf), separate time-dependent and freq-dependent
      |                      interp types with a comma (freq_after_ the
      |                      comma). 
      |                    * Specifications for frequency are ignored when the
      |                      calibration table has no channel-dependence. 
      |                    * Time-dependent interp options ending in 'PD'
      |                      enable a "phase delay" correction per spw for
      |                      non-channel-dependent calibration types.
      |                    * For multi-obsId datasets, 'perobs' can be
      |                      appended to the time-dependent interpolation
      |                      specification to enforce obsId boundaries when
      |                      interpolating in time. 
      |                    * Freq-dependent interp options can have 'flag' appended
      |                      to enforce channel-dependent flagging, and/or 'rel' 
      |                      appended to invoke relative frequency interpolation
      | 
      |                         Examples: 
      |                         interp='nearest' (in time, freq-dep will be
      |                         linear, if relevant)
      |                         interp='linear,cubic'  (linear in time, cubic
      |                         in freq)
      |                         interp='linearperobs,splineflag' (linear in
      |                         time per obsId, spline in freq with
      |                         channelized flagging)
      |                         interp='nearest,linearflagrel' (nearest in
      |                         time, linear in freq with with channelized 
      |                         flagging and relative-frequency interpolation)
      |                         interp=',spline'  (spline in freq; linear in
      |                         time by default)
      |                         interp=['nearest,spline','linear']  (for
      |                         multiple gaintables)
.. [21] 
   **spwmap** (intArray=[''])
      | Spectral window mappings to form for gaintable(s)
      |                      default: [] (apply solutions from each calibration spw to
      |                      the same MS spw only)
      |                      Any available calibration spw can be mechanically mapped to any 
      |                       MS spw. 
      |                      Examples:
      |                         spwmap=[0,0,1,1] means apply calibration 
      |                           from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
      |                         spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
      |                           gaintables)
.. [22] 
   **parang** (bool=False)
      | Apply parallactic angle correction
      |                      Default: False
      | 
      |                      If True, apply the parallactic angle correction
      |                      (required for polarization calibration)

    """
    pass
