#
# stub function definition file for docstring parsing
#

def setjy(vis='', field='', spw='', selectdata=False, timerange='', scan='', intent='', observation='', scalebychan=True, standard='Perley-Butler 2017', model='', modimage='', listmodels=False, fluxdensity=-1, spix=0.0, reffreq='1GHz', polindex=[''], polangle=[''], rotmeas=0.0, fluxdict='', useephemdir=False, interpolation='nearest', usescratch=False, ismms=False):
    r"""
Fills the model column with the visibilities of a calibrator

Parameters
   - **vis** (string) - Name of input visibility file
   - **field** (string) - Select field using field id(s) or field name(s)
   - **spw** (string) - Select spectral window/channels
   - **selectdata** (bool) - Other data selection parameters
   - **scalebychan** (bool) - Scale the flux density on a per channel basis or else on a per spw basis
   - **standard** (string) - Flux density standard
   - **usescratch** (bool) - Will create if necessary and use the MODEL_DATA 

Subparameters
   .. raw:: html

      <details><summary><i> selectdata = True </i></summary>

   - **timerange** (string='', stringArray) - Select data based on time range
   - **scan** (string='', stringArray) - Scan number range
   - **intent** (string='') - Select observing intent
   - **observation** (string='', int) - Select by observation ID(s)

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> standard = Perley-Butler 2017 </i></summary>

   - **model** (string='') - File location for field model
   - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects
   - **interpolation** (string=nearest) - Method to be used to interpolate in time

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> standard = Perley-Butler 2013 </i></summary>

   - **model** (string='') - File location for field model
   - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects
   - **interpolation** (string=nearest) - Method to be used to interpolate in time

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> standard = Perley-Butler 2010 </i></summary>

   - **model** (string='') - File location for field model
   - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> standard = Butler-JPL-Horizons 2012 </i></summary>

   - **listmodels** (bool=False) - List the available models for VLA calibrators or Tb models for Solar System objects
   - **useephemdir** (bool=False) - Use directions in the ephemeris table

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> standard = manual </i></summary>

   - **fluxdensity** (int=
                           , intArray, doubleArray) - Specified flux density in Jy [I,Q,U,V]; (-1 will lookup values)
   - **spix** (double='', doubleArray) - Spectral index (including higher terms) of I fluxdensity
   - **reffreq** (string=1GHz) - Reference frequency for spix
   - **polindex** (doubleArray='') - Coefficients of an expansion of frequency-dependent linear polarization fraction expression
   - **polangle** (doubleArray='') - Coefficients of an expansion of frequency-dependent polarization angle expression (in radians)
   - **rotmeas** (double=0.0) - Rotation measure (in rad/m^2)

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> standard = fluxscale </i></summary>

   - **fluxdict** (record='') - Output dictionary from fluxscale

   .. raw:: html

      </details>


Description
      The **setjy** task sets the model visibility amplitude and phase
      associated with a flux density scale and a specified clean
      components image into the model column of the MS data set. The
      flux density (I,Q,U,V) for a point source calibrator can be
      entered explicitly.  If no model is specified, then a point source
      at the phase center is assumed.  For sources that are recognized
      flux calibrators (listed in `Flux Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__ ),
      setjy can calculate the flux densities as a function of frequency
      (and time, for some extragalactic sources classified as the
      variable sources and Solar System objects). Otherwise, the flux
      densities should be manually specified ( standard=’manual’).

      .. rubric:: Overview
         :name: overview

      The basic modes of operations are specified by the parameter,
      *standard*. As the name indicates, the bulk of its options are
      different flux density standards available in CASA as listed in
      `Flux Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__.
      In addition, *standard=’manual’* allows flux density scaling to be
      specified directly instead of using one for the flux density
      standards. And finally, *standard=‘fluxscale’* allows the user to
      insert a flux density based on the python dictionary result from
      the fluxscale task, after the initial **setjy** on the primary
      flux calibrator, to insert proper flux density models for
      secondary calibrators in the MS.

      By default the **setjy** task will cycle through all selected
      fields, spectral windows and channels, (one solution per spw with
      *scalebychan = False*) , setting the flux density either to 1 Jy
      (unpolarized), or if the source is recognized as one of the
      calibrators, to the flux density (assumed unpolarized) appropriate
      to the observing frequency.

      | Optionally, the MODEL_DATA column can be filled with the Fourier
        transform of the model image. But for any given MeasurementSet,
        the performance and data storage requirements are less demanding
        without the MODEL_DATA column. If *usescratch=False*, the model
        is stored as a 'virtual' model. The model parameters are saved
        either in the SOURCE_MODEL column in the SOURCE table (if one
        exists) or in the keyword
      | of the main table in the MS and model visibilities are evaluated
        on the fly when processing calibration or plotting in plotms.
      | The result containing flux densities for each spw is returned as
        a Python dictionary when it is executed as the function with
        arguments,

      .. note:: #For Example

         setjy(vis=‘my.ms’…)

      .. rubric:: Manually setting Flux Densities: standard=‘manual’
         :name: manually-setting-flux-densities-standardmanual

      With this mode, the flux densities and other relevant parameters
      necessary to describe the model can be entered manually. The
      following are the subparameters.

      .. note:: | standard       =   'manual'        #  Flux density standard
         |      fluxdensity    = [1, 0, 0, 0]      #  Specified flux
           density in Jy [I,Q,U,V]; (-1 will lookup values)
         |      spix           =         []        #  Spectral index
           (including higher terms) of I fluxdensity
         |      reffreq        =         ''        #  Reference
           frequency for spix
         |      polindex       =         []        #  Coefficients of an
           expansion of frequency-dependent linear polarization fraction
           expression
         |      polangle       =         []        #  Coefficients of an
           expansion of frequency-dependent polarization angle
           expression (in radians)
         |      rotmeas        =        0.0        #  Rotation measure
           (in rad/m^2)

          

      In the simplest version, the flux for Stokes I can be set via the
      *fluxdensity* subparameter as the first entry in a list. In the
      above example [1,0,0,0] **setjy** sets the flux to 1 Jy.
      Additional Stokes specifications can be set in remaining list
      members.  All *fluxdensity* vales **must** be given in units of
      Jy. A spectral index can be provided via the *spix* and *reffreq*
      subparameters. Finally it is also possible to provide coefficients
      for the polarization fraction and angle as well as a rotation
      measure to define the model (*polindex*, *polangle*, *rotmeas*
      subparameters).

      The *spix* subparamter can accept a list of values to include the
      spectral index of Stokes I in higher order terms, using the
      definition of the flux density at a frequency, :math:`\nu`,
      :math:`S(\nu)=fluxdensity[0]*\frac{\nu}{reffreq}^{spix[0]+spix[1]*log(\nu/reffreq)+..}`
      . The *reffreq* is given by a string including the unit (e.g.
      '10GHz', note that there is no space between the value and the
      unit). The *polindex* takes a list of coefficents ([p0, p1,
      p2...]) using the definition of frequency-dependent polarization
      index (PI) , where

      :math:` PI = \frac{\sqrt{Q^2+U^2}}{I} = p0 + p1*\frac{\nu-reffreq}{reffreq} + p2*(\frac{\nu-reffreq}{reffreq})^2 + ...`.

      Similarly, the *polangle* subparameter takes a list of
      coefficients ([a0,a1,a2, ..]) using the definition of polarization
      angle (:math:`\chi`), where

      :math:`\chi = 0.5arctan\frac{U}{Q} = a0 + a1*\frac{\nu-reffreq}{reffreq} + a2*(\frac{freq-reffreq}{reffreq})^2 + ..`.

      .. note:: The note on some logics how these subparameters are used to
         determine flux densities:

         -  When Stokes Q and U flux densities are given in
            *fluxdensity*, the coefficient, p0 is determined from these
            flux densities and the entry for p0 in *polindex* is
            ignored. Also, a0 is determined from these flux density
            values and the entry for a0 in *polangle* is ignored.
         -  If Q and U flux densities in fluxdensity are set to 0.0,
            then *polindex* [0] and *polangle* [0] are used to
            determine Q and U at *reffreq*.
         -  When the frequency-dependent polindex and polangle are used,
            be sure to include all the coefficients for **both**
            *polindex* and *polangle.* Otherwise Q and U flux densities
            are not calculated correctly.
         -  If *rotmeas* is given, the Q and U that are determined from
            above parameters are further corrected for the Faraday
            rotation.

      .. rubric:: Using the Predefined Standards
         :name: using-the-predefined-standards

      For the VLA, the default source models are customarily point
      sources defined by the *’Baars’*, ’ *Perley 90’*, *’Perley-Taylor
      99’*, ’ *Perley-Butler 2010’*, time-variable *’Perley-Butler
      2013’*, 'Perley-Butler 2017', *’Scaife-Heald 2012’*, or
      *’Stevens-Reynolds 2016’* flux density scales (See `Flux
      Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__
      for details; *’Perley-Butler 2017’* is the current standard by
      default), or point sources of unit flux density if the flux
      density is unknown. When 'Perley-Bulter 2017' is used and if any
      part of the frequencies of the relevant visibility data are
      outside the valid frequency range for each individual source as
      listed in `Flux Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__,
      **setjy** issues warning log messages while it still proceeds to
      calcuate the flux densities and set the model visibility.

      Most calibrator sources are based on radio emission from quasars
      and jets. The spectral indices of these sources are such that at
      (sub)mm wavelengths the majority of these sources become too weak
      and variable to reliably set the flux density scale. Alternatives
      are thermal objects such as planets, moons, and asteroids. Being
      Solar System objects, these objects do not move at the sidereal
      rate and may be (strongly) resolved. The
      *standard=’Butler-JPL-Horizons 2010’* and the recommended
      *standard=’Butler-JPL-Horizons 2012’* (for more information on the
      implemented models, see `Flux Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__
      page and also ALMA Memo 594  `[1] <#cit1>`__.) option of **setjy**
      includes flux density calibration using Solar System objects.

      For ’Butler-JPL-Horizons 2012’ CASA currently supports the objects
      listed in `Flux Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__
      to be applied to ALMA data. These names are recognized when they
      are used in the *’field’* parameter in **setjy**. In that case,
      **setjy** will obtain the geocentric distance and angular diameter
      at the time of the observation from a JPL–Horizons ephemeris and
      calculate model visibilities. Currently the objects are modeled as
      uniform temperature disks. Note that this model may oversimplify
      the real structure, in particular asteroids. The supported
      brightness temperature models for Solar System objects can be
      listed by selecting a *standard* and *listmodels=True* without
      setting any other parameters as shown below:

      .. note:: setjy(standard=‘Butler-JPL-Horizons 2012’, listmodels=True)

      Each model contains temperatures at tabulated frequencies except
      for Mars. For Mars, the model temperatures are tabulated in time
      and frequency (see `Flux Calibrator Models - Conventions, Data
      Formats <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-density-calibrator-models-conventions-data-formats>`__
      for more details).

      For selected asteroids, time variable models are available based
      on thermophysical modeling by T. Mueller (private communication)
      for January 1st, 2015 and beyond. Currently, the new models are
      available for Ceres, Pallas, and Vesta. A model is also available
      for Lutetia but using this source for ALMA absolute flux
      calibration is not advised. These new models are automatically
      chosen for the data taken after 2015 January 1, 0 hr UT. These
      models are also listed when the **setjy** task is executed with
      *standard=‘Butler-JPL-Horizons 2012’* and *listmodels=True*. These
      model data files contain flux densities tabulated in time and
      frequency (see `Flux Calibrator Models - Conventions, Data
      Formats <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-density-calibrator-models-conventions-data-formats>`__
      for more details).  

      Flux density calculation with Solar System objects depends on
      ephemerides. The **setjy** task looks for the data in
      *os.getenv('CASAPATH').split()[0] +
      '/data/ephemerides/JPL-Horizons'*.  If no ephemeris for the right
      object at the right time is present, the calculation will fail.
      Ask the `ALMA helpdesk <https://help.almascience.org/>`__ to make
      an ephemeris. The very adventurous and well versed in python
      can try it using CASA's *recipes.ephemerides* package:

      .. note:: | import recipes.ephemerides as eph
         | help eph

      CASA comes with ephemerides for several more objects, but they are
      intended for use with **me.framecomet()**, and are not
      (yet) suitable flux density calibrators. It is up to the observer
      to pick a good flux density calibrator (bright, spherical and
      featureless, on a circular orbit, in the right part of the
      sky, and not too resolved). Even some of the objects listed
      above may prove to require more sophisticated flux density models
      than are currently implemented in CASA. For many objects
      running **casalog.filter('INFO1')** before running **setjy** will
      send more information to the logger.  "`Reference
      Material <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material>`__"  has
      section "`Flux Calibrator
      Models <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/flux-calibrator-models>`__"
      with descriptions of the models used by **setjy** (both
      extragalactic and Solar System).

      .. note:: **Alert**: The apparent brightness of objects in the Solar
         System will vary with time because of the Earth’s varying
         distance to these objects, if nothing else. If the field index
         of a flux calibrator spans several days, **setjy** should be
         run more than once, limiting each run to a suitable timerange
         by using the timerange, scan, and/or observation selection
         parameters. Note that it is the field index that matters, not
         the name. Typically concat assigns moving objects a new field
         index for each observation, so usually it is not necessary to
         select a time range in **setjy**. However, it is worth checking
         with
         `listobs <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_listobs>`__,
         especially for planets.

      .. rubric:: Using Calibration Models for Resolved Sources
         :name: using-calibration-models-for-resolved-sources

      For observations of Solar System objects using the
      *’Butler-JPL-Horizons 2010’* and *’Butler-JPL-Horizons 2012’*
      models, **setjy** will know and apply the flux distribution across
      the extended structure of the calibrators.

      For other sources, namely VLA calibrator sources, a flux density
      calibrator can be resolved at the observing frequency and the
      point source model generated by **setjy** will not be appropriate.
      If available, a model image of the resolved source at the
      observing frequency may be used to generate the appropriate
      visibilities using the *model* subparameter (currently only
      available for *standard='Perley-Butler 2010' ,*
      *standard='Perley-Butler 2013’,* and *standard='Perley-Butler
      2017'*).  To do this, the *model* subparameter must include the
      full path to the model image. If the *model* subparameter is given
      only the file name, **setjy** will first search for the model
      image in the current working directory.  

      Also note that using **setjy** with a model image will only
      operate on that single source.  Therefore, for different sources,
      **setjy** would need to be run multiple times (with different
      field settings). The default model images available are listed by
      *listmodel=True * and are found in the
      .../data/nrao/VLA/CalModels sub-directory of the CASA
      installation.  Note the full path to the flux density calibrators
      may change depending on the installation directory or copies of
      these models can be placed in the current working directory.

      Currently available model images are:

      .. note:: | 3C138_P.im
         | 3C138_L.im
         | 3C138_S.im
         | 3C138_C.im
         | 3C138_X.im
         | 3C138_U.im
         | 3C138_K.im
         | 3C138_A.im
         | 3C138_Q.im

         | 3C286_P.im
         | 3C286_L.im
         | 3C286_S.im
         | 3C286_C.im
         | 3C286_X.im
         | 3C286_U.im
         | 3C286_K.im
         | 3C286_A.im
         | 3C286_Q.im

         | 3C48_P.im
         | 3C48_L.im
         | 3C48_S.im
         | 3C48_C.im
         | 3C48_X.im
         | 3C48_U.im
         | 3C48_K.im
         | 3C48_A.im
         | 3C48_Q.im

         | 3C147_P.im
         | 3C147_L.im
         | 3C147_S.im
         | 3C147_C.im
         | 3C147_X.im
         | 3C147_U.im
         | 3C147_K.im
         | 3C147_A.im
         | 3C147_Q.im

         3C123_P.im

         3C196_P.im

         3C295_P.im

         3C380_P.im

      These are all un-convolved images of AIPS CC lists. It is
      important that the model image not be one convolved with a finite
      beam; it must have units of Jy/pixel (not Jy/beam).

      Note that **setjy** will rescale the flux in the models for known
      sources to match those it would have calculated. It will thus
      extrapolate the flux out of the frequency band of the model image
      to whatever spectral windows in the MS is specified (but will use
      the structure of the source in the model image).

      If no source model is available, the uvrange selection may be
      needed during calibration to exclude the baselines where the
      resolution effect is significant. There is no hard and fast rule
      for this, though should be considered if the calibrator shows a
      drop of more than 10% on the longest baselines (use plotms to look
      at this). The antenna selection may also be needed if the
      calibrator is heavily resolved and there are few good baselines to
      the outer antennas. Note that uvrange may also be needed to
      exclude the short baselines on some calibrators that have extended
      flux not accounted for in the model.

      Note: For the following models, hard-coded radius limits on the
      model images are applied automatically.

      ===== =====
      3C286 3.0"
      3C48  0.95"
      3C147 0.85"
      3C138 0.75"
      ===== =====

      **Note**: the calibrator guides for the specific telescopes
      usually indicate appropriate min and max for uvrange. For example,
      see the VLA Calibration Manual at:
      https://science.nrao.edu/facilities/vla/observing/callist for
      details on the use of standard calibrators for the VLA.


   Bibliography
         :sup:`1. Butler 2012,` `ALMA Memo
         #594 <https://science.nrao.edu/facilities/alma/aboutALMA/Technology/ALMA_Memo_Series/alma594/abs594>`__ `<#ref-cit1>`__

    """
    pass
