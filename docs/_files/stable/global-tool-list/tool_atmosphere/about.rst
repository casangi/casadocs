.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   tool atmosphere description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: description

         Tool **atmosphere** returns atmospheric transmission of a given
         atmospheric profile and frequencies. The transmission is
         calculated based on `the Atmospheric Transmission at Microwaves
         model <http://cab.inta-csic.es/users/jrpardo/class_atm.html>`__
         (ATM) using the ATM library developed by the team lead by J.
         Cernicharo and Juan R. Padro and TELCAL subsystem of ALMA. For
         details of ATM, please refer to the citations at the bottom.

      .. container:: description

          

      .. rubric:: Basic Steps to Use atmosphere tool
         :name: basic-steps-to-use-atmosphere-tool
         :class: description

      The basic steps to use **atmosphere** tool are:

      #. Construct atmospheric model profile to calculate transmission
      #. Setup frequencies to calculate transmission
      #. Get atmospheric transmission (the opacities, phase delay, path
         length, absorption coefficients, etc.)

      .. rubric:: Construct atmospheric model profile
         :name: construct-atmospheric-model-profile

      Use **initAtmProfile** method to construct atmospheric model
      profile. The atmospheric model profile is composed of the layer
      thickness, pressure, temperature, and gas density of atmospheric
      component species as a function of the altitude. It can be used to
      calculate absorption and phase coefficients, as well as to perform
      forward and/or retrieval radiative transfer calculations. The
      atmospheric component species used in the calculation
      are H\ :sub:`2`\ O, CO, O\ :sub:`3`, N\ :sub:`2`\ 0,
      NO\ :sub:`2`, O\ :sub:`3`, and SO\ :sub:`2`.

      The atmospheric model profile can be build by defining the
      following values

      -  the altitude of the site
      -  the temperature, pressure and relative humidity at the ground
      -  the top height of atmospheric profile (*maxAltitude*)
      -  the tropospheric temperature lapse rate (*dTem_dh*)
      -  the initial step of pressure (*dP*) and multiplicative factor
         of pressure steps (*dPm*)
      -  the scale height of water vapor (*h0*)
      -  the atmospheric type ID (*atmType*)

      The available atmospheric types are *TROPICAL*, *MIDLATSUMMER*,
      *MIDLATWINTER*, *SUBARTSUMMER*, and *SUBARTWINTER*. It controls
      the profile of upper layers of atmosphere. The map between
      atmospheric types and IDs can be listed by a
      method, **listAtmosphereTypes**.

      Method **initAtmProfile** optionally accepts *layerBoundaries*
      and *layerTemperature* to construct an atmospheric model profile
      using user defined temperature profile of atmosphere.

      It is possible to modify basic atmospheric parameters after
      initialization by **updateAtmProfile** method.

      Method **getBasicAtmParams** prints the current parameters used to
      construct atmospheric model profile. Use **getProfile** to obtain
      the atmospheric model profile constructed.

      .. rubric:: Setup frequencies to calculate transmission
         :name: setup-frequencies-to-calculate-transmission

      Use **initSpectralWindow** method to define frequencies (spectral
      windows) to compute transmission. The building blocks of spectral
      window are the center frequency (*fCenter*), band width
      (*fWidth*), and channel width (*fRes*). The method accepts a list
      of quantities for the frequencies when *nbands* > 1 in the method.

      Use **addSpectralWindow** method to add more spectral windows
      after initialization.

      There are several methods to return spectral window setttings,
      e.g., **getSpectralWindow**, **getBandWidth**, **getChanFreq**,
      **getChanNum**, **getChanSep**, **getNumChan**, **getRefChan**,
      and **getRefFreq**.

      .. rubric:: Get atmospheric transmission
         :name: get-atmospheric-transmission

      There are three setter methods that can be invoked only after
      atmospheric model and spectral windows are defined,
      i.e., **setUserWH2O**, **setAirMass**, and
      **setSkyBackgroundTemperature**, which define the water vapor
      column used for radiative transfer calculations, air mass used for
      the radiative transfer, and balckbody temperature of the sky
      background (default: 2.73K), respectively.

      Now it is ready to invoke getter methods to compute and obtain the
      transmission of the atmospheric model you defined in previous
      steps. Tool **atmosphere** computes,

      -  the integrated opacity along atmospheric path, e.g.,
         **getWetOpacity**, **getCOLinesOpacity**
      -  the integrated path length, e.g., **getN20LinesPathLength**,
         **getDispersivePathLength**
      -  the atmospheric phase delay, e.g.,
         **getNonDispersivePhaseDelay**
      -  the equivalent Black-body or the Rayleigh-Jeans Temperature of
         (a channel in) a spectral window, e.g., **getTebbSky**,
         **getAverageTrjSky**
      -  the absorption coefficient at a layer in the atmospheric
         profile, e.g., **getAbsO3Lines**, **getAbsH2OCont**

      Please refer to descriptions in
      `Methods <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_atmosphere/methods>`__ for
      details of each method.

       

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo et al. 1995, J. Quant. Spectr. and Radiat.  |
      |                 | Transfer, 54, N6, 931                             |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo et al. 1996, Journal of Geophysical         |
      |                 | Research, 101, D22, 28723                         |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 3                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo et al. 1998, Journal of Geophysical         |
      |                 | Research, 103, D6, 6189                           |
      +-----------------+---------------------------------------------------+

      =============== =================================================
      Citation Number 4
      Citation Text   Serabyn et al. 1998, Applied Optics, 37, 12, 2185
      =============== =================================================

      +-----------------+---------------------------------------------------+
      | Citation Number | 5                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo et al. 1998, J. Quant. Spectr. and Radiat.  |
      |                 | Transfer, 60, N4, 559                             |
      +-----------------+---------------------------------------------------+

      =============== ========================================================
      Citation Number 6
      Citation Text   Matsushita et al. 1999, Publ. Astron. Soc. Japan 51, 603
      =============== ========================================================

      +-----------------+---------------------------------------------------+
      | Citation Number | 7                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo et al. 2000, J. Quant. Spectr. and Radiat.  |
      |                 | Transfer, 67, 2, 169                              |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 8                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo, Serabyn and  Cernicharo 2001, J. Quant.    |
      |                 | Spectr. and Radiat. Transfer, 68/4, 419           |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 9                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Garand et al. 2001, Journal of Geophysical        |
      |                 | Research, 106, 24017                              |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 10                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Prigent et al. 2001, Journal of Geophysical       |
      |                 | Research, 106, 28243                              |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 11                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo, Cernicharo, and Serabyn 2001, Canadian     |
      |                 | Journal of Physics, 80(4), 455                    |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 12                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo et al. 2001, Canadian Journal of Physics,   |
      |                 | 80(4), 443                                        |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 13                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Wiedner et al. 2004, Journal of Geophysical       |
      |                 | Research, 109, D6, 06214                          |
      +-----------------+---------------------------------------------------+

      =============== =================================
      Citation Number 14
      Citation Text   Pardo et al. 2004, ApJS, 153, 363
      =============== =================================

      +-----------------+---------------------------------------------------+
      | Citation Number | 15                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Pardo et al. 2005, J. Quant. Spec. and Radiat.    |
      |                 | Transfer 96/3-4, 537                              |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 16                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Prigent et al. 2005, Geophysical Journal Letters  |
      |                 | 42, L04810                                        |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 17                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Rosenkranz et al. 2006, Chapter 2 in "Thermal     |
      |                 | Microwave Radiation - Applications for Remote     |
      |                 | Sensing", IEE Electromagnetic Waves Series        |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 18                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Battaglia et al. 2006, Chapter 3 in "Thermal      |
      |                 | Microwave Radiation - Applications for Remote     |
      |                 | Sensing", IEE Electromagnetic Waves Series        |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 19                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Prigent, J.R. Pardo, W.B. Rossow 2006, Journal of |
      |                 | Applied Meteorology and Climatology, 45, 1622     |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 20                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Meirold-Mautner et al. 2007, Journal of the       |
      |                 | Atmospheric Sciences, 64/5, 1550                  |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 21                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Chaboureau et al. 2007, Journal of Applied        |
      |                 | Meteorology and Climatology, 47/5, 1337           |
      +-----------------+---------------------------------------------------+

.. container:: section
   :name: viewlet-below-content-body
