

.. _Description:

Description
   tool atmosphere description
   
   Tool **atmosphere** returns atmospheric transmission of a given
   atmospheric profile and frequencies. The transmission is
   calculated based on `the Atmospheric Transmission at Microwaves
   model <http://cab.inta-csic.es/users/jrpardo/class_atm.html>`__
   (ATM) using the ATM library developed by the team lead by J.
   Cernicharo and Juan R. Padro and TELCAL subsystem of ALMA. For
   details of ATM, please refer to the citations at the bottom.
   
    
   
   .. rubric:: Basic Steps to Use atmosphere tool
      
   
   The basic steps to use **atmosphere** tool are:
   
   #. Construct atmospheric model profile to calculate transmission
   #. Setup frequencies to calculate transmission
   #. Get atmospheric transmission (the opacities, phase delay, path
      length, absorption coefficients, etc.)
   
   .. rubric:: Construct atmospheric model profile
      
   
   Use **initAtmProfile** method to construct atmospheric model
   profile. The atmospheric model profile is composed of the layer
   thickness, pressure, temperature, and gas density of atmospheric
   component species as a function of the altitude. It can be used to
   calculate absorption and phase coefficients, as well as to perform
   forward and/or retrieval radiative transfer calculations. The
   atmospheric component species used in the calculation
   are H :sub:`2` O, CO, O :sub:`3`, N :sub:`2` 0,
   NO :sub:`2`, O :sub:`3`, and SO :sub:`2`.
   
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
   *MIDLATWINTER*, *SUBARTSUMMER*, and *SUBARTWINTER*. It controls
   the profile of upper layers of atmosphere. The map between
   atmospheric types and IDs can be listed by a
   method, **listAtmosphereTypes**.
   
   Method **initAtmProfile** optionally accepts *layerBoundaries*
   and *layerTemperature* to construct an atmospheric model profile
   using user defined temperature profile of atmosphere.
   
   It is possible to modify basic atmospheric parameters after
   initialization by **updateAtmProfile** method.
   
   Method **getBasicAtmParams** prints the current parameters used to
   construct atmospheric model profile. Use **getProfile** to obtain
   the atmospheric model profile constructed.
   
   .. rubric:: Setup frequencies to calculate transmission
      
   
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
      
   
   There are three setter methods that can be invoked only after
   atmospheric model and spectral windows are defined,
   i.e., **setUserWH2O**, **setAirMass**, and
   **setSkyBackgroundTemperature**, which define the water vapor
   column used for radiative transfer calculations, air mass used for
   the radiative transfer, and balckbody temperature of the sky
   background (default: 2.73K), respectively.
   
   Now it is ready to invoke getter methods to compute and obtain the
   transmission of the atmospheric model you defined in previous
   steps. Tool **atmosphere** computes,
   
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
   `Methods <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_atmosphere/methods>`__ for
   details of each method.
   
   
   
   
   
   =============== =================================================
   Citation Number 4
   Citation Text   Serabyn et al. 1998, Applied Optics, 37, 12, 2185
   =============== =================================================
   
   =============== ========================================================
   Citation Number 6
   Citation Text   Matsushita et al. 1999, Publ. Astron. Soc. Japan 51, 603
   =============== ========================================================
   
   
   
   
   
   
   
   
   
   
   
   
   
   =============== =================================
   Citation Number 14
   Citation Text   Pardo et al. 2004, ApJS, 153, 363
   =============== =================================
   
   
      Bibliography
   :sup:`1. Pardo et al. 1995, J. Quant. Spectr. and Radiat.
   Transfer, 54, N6, 931` `<#ref-cit1>`__
   
   :sup:`2. Pardo et al. 1996, Journal of Geophysical Research,
   101, D22, 28723` `<#ref-cit2>`__
   
   :sup:`3. Pardo et al. 1998, Journal of Geophysical Research,
   103, D6, 6189` `<#ref-cit3>`__
   
   :sup:`4. Serabyn et al. 1998, Applied Optics, 37, 12,
   2185` `<#ref-cit4>`__
   
   :sup:`5. Pardo et al. 1998, J. Quant. Spectr. and Radiat.
   Transfer, 60, N4, 559` `<#ref-cit5>`__
   
   :sup:`6. Matsushita et al. 1999, Publ. Astron. Soc. Japan 51,
   603` `<#ref-cit6>`__
   
   :sup:`7. Pardo et al. 2000, J. Quant. Spectr. and Radiat.
   Transfer, 67, 2, 169` `<#ref-cit7>`__
   
   :sup:`8. Pardo, Serabyn and  Cernicharo 2001, J. Quant. Spectr.
   and Radiat. Transfer, 68/4, 419` `<#ref-cit8>`__
   
   :sup:`9. Garand et al. 2001, Journal of Geophysical Research,
   106, 24017` `<#ref-cit9>`__
   
   :sup:`10. Prigent et al. 2001, Journal of Geophysical Research,
   106, 28243` `<#ref-cit10>`__
   
   :sup:`11. Pardo, Cernicharo, and Serabyn 2001, Canadian Journal
   of Physics, 80(4), 455` `<#ref-cit11>`__
   
   :sup:`12. Pardo et al. 2001, Canadian Journal of Physics,
   80(4), 443` `<#ref-cit12>`__
   
   :sup:`13. Wiedner et al. 2004, Journal of Geophysical Research,
   109, D6, 06214` `<#ref-cit13>`__
   
   :sup:`14. Pardo et al. 2004, ApJS, 153,
   363` `<#ref-cit14>`__
   
   :sup:`15. Pardo et al. 2005, J. Quant. Spec. and Radiat.
   Transfer 96/3-4, 537` `<#ref-cit15>`__
   
   :sup:`16. Prigent et al. 2005, Geophysical Journal Letters 42,
   L04810` `<#ref-cit16>`__
   
   :sup:`17. Rosenkranz et al. 2006, Chapter 2 in "Thermal
   Microwave Radiation - Applications for Remote Sensing", IEE
   Electromagnetic Waves Series` `<#ref-cit17>`__
   
   :sup:`18. Battaglia et al. 2006, Chapter 3 in "Thermal
   Microwave Radiation - Applications for Remote Sensing", IEE
   Electromagnetic Waves Series` `<#ref-cit18>`__
   
   :sup:`19. Prigent, J.R. Pardo, W.B. Rossow 2006, Journal of
   Applied Meteorology and Climatology, 45,
   1622` `<#ref-cit19>`__
   
   :sup:`20. Meirold-Mautner et al. 2007, Journal of the
   Atmospheric Sciences, 64/5, 1550` `<#ref-cit20>`__
   
   :sup:`21. Chaboureau et al. 2007, Journal of Applied
   Meteorology and Climatology, 47/5, 1337` `<#ref-cit21>`__
   

.. _Examples:

Examples
   Note **atmosphere** tool is instanciated as '**at**' tool when
   CASA is loaded.
   
   .. rubric:: Minimum execution
      
   
   Default atmospheric profile, obtain opacities of wet and dry
   components in 100GHz.
   
   ::
   
      #In CASA
   
      CASA <1>: out = at.initAtmProfile()
   
      CASA <2>: nchan = at.initSpectralWindow(1, "100GHz", "500kHz",
      "0Hz")
   
      CASA <**3**>: at.getDryOpacity(0, 0)
   
      Out[**3**]: 0.011171237850436442
   
       
   
      CASA <**4**>: at.getWetOpacity(0, 0)
   
      Out[**4**]: {'unit': 'neper', 'value': array([ 0.01109787])}
   
   .. rubric:: Define Atmospheric Profile
      
   
   Atmospheric profile that represents ALMA site.
   
   ::
   
      #In CASA
   
      CASA <**1**>: out = at.initAtmProfile(humidity=20.0,
      temperature="273K", altitude="5059m", pressure="563mbar",
      atmType=3)
   
      CASA <**2**>: **print** (out)
   
      BASIC ATMOSPHERIC PARAMETERS TO GENERATE REFERENCE ATMOSPHERIC
      PROFILE
   
        
   
      Ground temperature T:         273 K
   
      Ground pressure P:            563 mb
   
      Relative humidity rh:         20 %
   
      Scale height h0:              2 km
   
      Pressure step dp:             10 mb
   
      Altitude alti:                5059 m
   
      Attitude top atm profile:     48 km
   
      Pressure step factor:         1.2 
   
      Tropospheric lapse rate:      -5.6 K/km
   
      Atmospheric type:             MIDLATWINTER
   
      User-defined temperature profile: OFF
   
       
   
      Built atmospheric profile with 21 layers.
   
   Now, get atmospheric model profile constructed in **atmosphere**
   tool. 
   
   The method, **getProfile**, returns the thickness, temperature,
   mass and number density of H :sub:`2` O, pressure, number
   dentities of O :sub:`3`, CO, and N :sub:`2` O in each layer of
   atmosphere model. One can use the return values, e.g., to plot the
   atmosphere model used to calculate transmission.
   
   ::
   
      #In CASA
   
      CASA <**3**>: (out, thick, temp, h2o_mass, h2o_num, press, o3,
      co, n2o) = at.getProfile()
   
   **How to construct an atmospheric profile by user defined
   temperature profile**
   
   The method, **initAtmProfile**, optionally accepts user defined
   temperature profile of atmosphere to construct an atmospheric
   profile. Define arrays of the altitude (in unit of meter) and
   temperature (in Kelvin) to specify temperature profile.
   
   ::
   
      #In CASA
   
      CASA <**1**>: atm_altitudes = [5100.0, 6000.0, 8000.0, 11000.0,
      15000.0] #meter
   
      CASA <**2**>: atm_temperature = [266.08, 267.02, 256.32,
      234.54, 213.34] #Kelvin
   
      CASA <**3**>: out = at.initAtmProfile(humidity=20.0,
      temperature="273K", altitude="5059m", pressure="563mbar",
      atmType=3, layerBoundaries=atm_altitudes,
      layerTemperature=atm_temperature)
   
   .. rubric:: Set Up Spectral Windows
      
   
    Define the first spectral window (center=100GHz, band
   width=1.5GHz, channel resolution=15MHz).
   
   ::
   
      #In CASA
   
      CASA <**4**>: nchan0 = at.initSpectralWindow(1,
      fCenter="100GHz", fWidth="1.5GHz", fRes="15MHz")
   
      CASA <**5**>: nchan0
   
      Out[**5**]: 100
   
   Add another spectral window (center=200GHz, band width=50MHz,
   channel resolution=10MHz) .
   
   ::
   
      #In CASA
   
      CASA <**6**>: at.addSpectralWindow(fCenter="200GHz",
      fWidth="50MHz", fRes="10MHz")
   
      Out[**6**]: 5
   
   Obtain channel frequencies of the second spectral window (id=1).
   
   ::
   
      #In CASA
   
      CASA <**7**>: at.getSpectralWindow(1)
   
      Out[**7**]: 
   
      {'unit': 'Hz',
   
       'value': array([  1.99980000e+11,   1.99990000e+11,  
      2.00000000e+11,
   
                2.00010000e+11,   2.00020000e+11])}
   
    
   
   .. rubric:: Get Atmospheric Transmission
      
   
   Set a user defined PWV (1.7mm) to compute atmospheric
   transimission.
   
   ::
   
      #In CASA
   
      CASA <**8**>: at.setUserWH2O("1.7mm")
   
   Obtain the opacities of water vapor and dry species (CO,
   N :sub:`2` O, NO :sub:`2`, O :sub:`2`, O :sub:`3`,
   SO :sub:`2`) of the second spectral window (id=1). The methods
   return channel number of spw and opacity of all channels in the
   spw.
   
   ::
   
      #In CASA
   
      CASA <**9**>: at.getDryOpacitySpec(1)
   
      Out[**9**]: (5, array([ 0.00928229,  0.00928329,  0.00927743, 
      0.00927898,  0.00928082]))
   
       
   
      CASA <**10**>: at.getWetOpacitySpec(1)
   
      Out[**10**]: 
   
      (5, {'unit': 'mm-1', 'value': array([ 0.08272901,  0.08270427, 
      0.08267965,  0.08265512,  0.08263071])})
   
   Compute atmospheric transmission of all channels in the first
   spectral window (id=0) for airmas=1.5.
   
   ::
   
      #In CASA
   
      CASA <**11**>: dry = at.getDryOpacitySpec(0)[1]
   
      CASA <**12**>: wet = at.getWetOpacitySpec(0)[1]['value']
   
      CASA <**13**>: airmass=1.5
   
      CASA <**14**>: transmission = numpy.exp(-airmass*(dry+wet))
   

.. _Development:

Development
   --CASA Developer--
   