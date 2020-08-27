#
# stub function definition file for docstring parsing
#

def initweights(vis, wtmode='nyq', tsystable='', gainfield='', interp='', spwmap=[''], dowtsp=False):
    """
Initializes weight information in the MS

Parameters
----------
vis : string
   Name of input visibility file (MS)
wtmode : string
   Initialization mode
dowtsp : bool
   Initialize the WEIGHT_SPECTRUM column

Other Parameters
----------
tsystable : string
   Tsys calibration table to apply on the fly
gainfield : string
   Select a subset of calibrators from Tsys table
interp : string
   Interpolation type in time[,freq]. default==\'linear,linear\'
spwmap : intArray
   Spectral windows combinations to form for gaintable(s)

Notes
-----





   task description



      This task provides for initialization of the weight information in
      the MS. An overview on weights in CASA is provided in the `Data
      Weights <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__
      section of CASAdocs. For ALMA interferometry and EVLA data, it
      should not generally be necessary to use this task, as the weight
      information should have been initialized properly at fill time
      (when the import was performed with CASA v4.2.2 and later).

      | Several initialization modes are supported via the *wtmode*
        parameter. If *wtmode='nyq'* (the default), the SIGMA and WEIGHT
        will be initialized according to bandwidth and integration time.
        This is the theoretically correct mode for raw normalized
        visibilities (e.g., ALMA). For the EVLA, this is correct if
        switched-power and bandpass calibration will later be applied.
        If *wtmode='sigma'*, WEIGHT will be initialized according to
        the existing SIGMA column. If *wtmode='weight'*, WEIGHT_SPECTRUM
        will be initialized according to the existing WEIGHT column;
        *dowtspec=True* must be specified in this case. If
        *wtmode='ones'*, SIGMA and WEIGHT will be initialized with
        1.0, globally. This is a traditional means of initializing
        weight information, and is adequate when the integration time
        and bandwidth are uniform. It is not recommended for
        modern instruments (ALMA, EVLA), where variety in observational
        setups is common, and properly initialized and calibrated
        weights will be used for imaging sensitivity estimates.
      | There are two EXPERIMENTAL modes, *wtmode='tsys'* and
        *'tinttsys'*. In the modes, SIGMA and WEIGHT will be initialized
        according to :math:`T_{sys}`, bandwidth :math:`\Delta\nu`, and
        integration time :math:`t_{int}` (used only in
        '*tinttsys*'), i.e.:

      -  *tsys* : :math:`weight=\frac{\Delta\nu}{T_{sys}^2}`
      -  *tinttsys*:
         :math:`weight=\frac{\Delta\nu \, t_{int}}{T_{sys}^2}`

      These modes use Tsys values to calculate weight as is done in Tsys
      calibration. Tsys values are taken from a Tsys calibration table
      given as *tsystable*. Selection of gain field
      (*gainfield*), interpolation method (*interp*), and spectral
      window mapping (*spwmap*) are supported, too.

      Available types of interpolation are:

      -  Time: '*nearest*', '*linear*', the variation of those with
         '*perobs*', e.g., '*linearperobs*' (enforce obsId boundaries in
         interpolation)
      -  Freq: '*nearest*', '*linear*', '*cubic*', '*spline*', and the
         variation of those with '*flag*', e.g., '*linearflag*'
         (with channelized flag).

      See the page of **applycal** for details of interpolations.

      .. note:: **WARNING**: If the weight in an MS is initialized with these
         modes and Tsys calibration table is applied
         with *calwt=True* after that, the weight would be contaminated
         by being divided by the square of Tsys twice. !!! USERS ARE
         ADVISED TO USE THESE EXPERIMENTAL MODES WITH CARE !!!

      For the above *wtmodes*, if *dowtsp=True* (or if the
      WEIGHT_SPECTRUM column already exists), the WEIGHT_SPECTRUM column
      will be initialized (uniformly in channel in *wtmode='nyq',
      'sigma',* '*weight*', and '*ones*'), in a manner consistent with
      the disposition of the WEIGHT column. If the
      WEIGHT_SPECTRUM column does not exist, *dowtsp=True* will force
      its creation. Use of the WEIGHT_SPECTRUM column is only
      meaningful for ALMA data which will be calibrated with
      channelized Tsys information, or if the weights will become
      channelized after calibration, e.g., via averaging over time-
      and channel-dependent flagging (**statwt** is a task for
      channel-dependent weight estimation from the data itself). 

      In non-channelized modes (*wtmode='nyq', 'sigma', 'weight',*
      and '*ones*') or when *dowtsp=False,* the SIGMA_SPECTRUM column
      will be removed from the MS. On the other hand, the SIGMA_SPECTRUM
      column is added and initialized in channelized modes
      (*wtmode='tsys'* and '*tinttsys*') if *dowtsp=True* or if the
      WEIGHT_SPECTRUM already column exists.

      Two additional modes are available for managing the
      spectral weight info columns; these should be used with extreme
      care: If *wtmode='delwtsp'*, the WEIGHT_SPECTRUM column will be
      deleted (if it exists). If *wtmode='delsigsp',* the SIGMA_SPECTRUM
      column will be deleted (if it exists). Note that creation
      of SIGMA_SPECTRUM is not supported via this method.

      .. note:: **NOTE**: This task does not support any prior
         selection. Intialization of the weight information must
         currently be done globally or not at all. This is to maintain
         consistency.

    """
    pass
