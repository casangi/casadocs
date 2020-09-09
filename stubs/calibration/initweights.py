#
# stub function definition file for docstring parsing
#

def initweights(vis, wtmode='nyq', tsystable='', gainfield='', interp='', spwmap=[''], dowtsp=False):
    r"""
Initializes weight information in the MS

Parameters
   - vis_ (string) - Name of input visibility file (MS)
   - wtmode_ (string='nyq') - Initialization mode

      .. raw:: html

         <details><summary><i> wtmode = tsys </i></summary>

      - tsystable_ (string='') - Tsys calibration table to apply on the fly
      - gainfield_ (string='') - Select a subset of calibrators from Tsys table
      - interp_ (string='') - Interpolation type in time[,freq]. default==\'linear,linear\'
      - spwmap_ (intArray=['']) - Spectral windows combinations to form for gaintable(s)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> wtmode = tinttsys </i></summary>

      - tsystable_ (string='') - Tsys calibration table to apply on the fly
      - gainfield_ (string='') - Select a subset of calibrators from Tsys table
      - interp_ (string='') - Interpolation type in time[,freq]. default==\'linear,linear\'
      - spwmap_ (intArray=['']) - Spectral windows combinations to form for gaintable(s)

      .. raw:: html

         </details>
   - dowtsp_ (bool=False) - Initialize the WEIGHT_SPECTRUM column


Description
   This task provides for initialization of the weight information in
   the MS. An overview on weights in CASA is provided in the `Data
   Weights <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__
   section of CASAdocs. For ALMA interferometry and EVLA data, it
   should notgenerally be necessary to use this task, as the weight
   informationshould have been initialized properly at fill time
   (when the import was performed with CASA v4.2.2 and later).

   | Several initialization modes are supported via the *wtmode*
     parameter. If *wtmode='nyq'* (the default), the SIGMA and WEIGHT
     will beinitialized according to bandwidth and integration time.
     Thisis the theoretically correct mode for raw normalized
     visibilities(e.g., ALMA). For the EVLA, this is correct if
     switched-powerand bandpass calibration will later be applied.
     If *wtmode='sigma'*, WEIGHT will be initialized according to
     theexisting SIGMA column. If *wtmode='weight'*, WEIGHT_SPECTRUM
     will be initialized accordingto the existing WEIGHT column;
     *dowtspec=True* must be specified inthis case. If
     *wtmode='ones'*, SIGMA and WEIGHT will be initialized with
     1.0,globally. This is a traditional means of initializing
     weightinformation, and is adequate when the integration time
     andbandwidth are uniform. It is not recommended for
     moderninstruments (ALMA, EVLA), where variety in observational
     setupsis common, and properly initialized and calibrated
     weightswill be used for imaging sensitivity estimates.
   | There are two EXPERIMENTAL modes, *wtmode='tsys'* and
     *'tinttsys'*.In the modes, SIGMA and WEIGHT will be initialized
     according to :math:`T_{sys}`, bandwidth :math:`\Delta\nu`, and
     integration time :math:`t_{int}` (used only in
     '*tinttsys*'),i.e.:

   -  *tsys* : :math:`weight=\frac{\Delta\nu}{T_{sys}^2}`
   -  *tinttsys*:
      :math:`weight=\frac{\Delta\nu \, t_{int}}{T_{sys}^2}`

   These modes use Tsys values to calculate weight as is done inTsys
   calibration. Tsys values are taken from a Tsys calibrationtable
   given as *tsystable*. Selection of gain field
   (*gainfield*),interpolation method (*interp*), and spectral
   window mapping (*spwmap*)are supported, too.

   Available types of interpolation are:

   -  Time: '*nearest*', '*linear*', the variation of those with
      '*perobs*',e.g., '*linearperobs*' (enforce obsId boundaries in
      interpolation)
   -  Freq: '*nearest*', '*linear*', '*cubic*', '*spline*', and the
      variationof those with '*flag*', e.g., '*linearflag*'
      (withchannelized flag).

   See thepageof **applycal** for details of interpolations.

   .. warning:: **WARNING**: If the weight in an MS is initialized with these
      modes andTsys calibration table is applied
      with*calwt=True*after that, theweight would be contaminated
      by being divided by the square of Tsystwice. !!! USERS ARE
      ADVISED TO USE THESE EXPERIMENTAL MODES WITH CARE !!!

   For the above *wtmodes*, if *dowtsp=True* (or if the
   WEIGHT_SPECTRUMcolumn already exists), the WEIGHT_SPECTRUM column
   will beinitialized (uniformly in channel in *wtmode='nyq',
   'sigma',*'*weight*', and '*ones*'), in a manner consistent with
   thedisposition of the WEIGHT column. If the
   WEIGHT_SPECTRUMcolumn does not exist, *dowtsp=True* will force
   its creation.Use of the WEIGHT_SPECTRUM column is only
   meaningfulfor ALMA data which will be calibrated with
   channelizedTsys information, or if the weights will become
   channelizedafter calibration, e.g., via averaging over time-
   andchannel-dependent flagging (**statwt** is a task for
   channel-dependentweight estimation from the data itself).

   In non-channelized modes (*wtmode='nyq', 'sigma', 'weight',*
   and'*ones*') or when *dowtsp=False,*the SIGMA_SPECTRUM column
   will be removedfrom the MS. On the other hand, the SIGMA_SPECTRUM
   column is added andinitialized in channelized modes
   (*wtmode='tsys'* and '*tinttsys*')if *dowtsp=True* or if the
   WEIGHT_SPECTRUM already column exists.

   Two additional modes are available for managing the
   spectralweight info columns; these should be used with extreme
   care: If*wtmode='delwtsp'*, the WEIGHT_SPECTRUM column will be
   deleted (ifit exists). If *wtmode='delsigsp',* the SIGMA_SPECTRUM
   columnwill be deleted (if it exists). Note that creation
   ofSIGMA_SPECTRUM is not supported via this method.

   .. note:: **NOTE**: This task does not support any prior
      selection.Intialization of the weight information must
      currently be done globally or not at all. This is to maintain
      consistency.


.. _vis:

vis (string)
   | Name of input visibility file (MS)

.. _wtmode:

wtmode (string='nyq')
   | Initialization mode

.. _tsystable:

tsystable (string='')
   | Tsys calibration table to apply on the fly

.. _gainfield:

gainfield (string='')
   | Select a subset of calibrators from Tsys table

.. _interp:

interp (string='')
   | Interpolation type in time[,freq]. default==\'linear,linear\'

.. _spwmap:

spwmap (intArray=[''])
   | Spectral windows combinations to form for gaintable(s)

.. _dowtsp:

dowtsp (bool=False)
   | Initialize the WEIGHT_SPECTRUM column


    """
    pass
