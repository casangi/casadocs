.. container::
   :name: viewlet-above-content-title

ALMA simulations
================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   How to use simalma to simulate ALMA observations

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary
         :name: summary

      The task **simalma** simulates an ALMA observation by ALMA 12-m,
      ACA-7m and total power arrays. It takes an input model image or a
      list of components, plus configurations of ALMA antennas
      (locations and sizes), and simulates a particular ALMA observation
      (specified by mosaic setup and observing cycles and times). The
      outputs are MeasurementSets. The task optionally generates images
      from the MeasurementSets.

      Technically speaking, **simalma** internally calls **simobserve**
      and **simanalyze** as many times as necessary to simulate and
      analyze an ALMA observation. Some of the simulation and imaging
      parameters are automatically set to values typical of ALMA
      observations. Thus, it has a simpler task interface compared to
      **simobserve** plus **simanalyze** at the cost of limited
      flexibility. If the user wants to have more control of simulation
      setup, it is available by manually running **simobserve** and
      **simanalyze** multiple times or by using the **simulator** (sm)
      tool.

      .. container:: alert-box

         **WARNING**: The task **simalma** is designed to only be
         invoked once for a simulation setup. It always sets up a
         *skymodel* and pointings. That means that **simalma** is not
         supposed to be run multiple times for a project, unlike
         **simobserve** and **simanalyze**. The task **simalma** may
         ignore or overwrite the old results when it is run more than
         once with the same project name.

      There are options in **simalma** to simulate observation of ACA
      7-m and total power arrays, to apply thermal noise, and/or to
      generate images from simulated MeasurementSets. One inputs a
      vector of configurations, and a corresponding vector of total
      times to observe each component. Thermal noise is added to
      visibilities when *pwv* > 0 . The ATM atmospheric model is
      constructed from the characteristics of the ALMA site and a user
      defined Precipitable Water Vapour (*pwv*) value. Set *pwv = 0* to
      omit the thermal noise. Finally, when *image = True*, synthesized
      images are generated from the simulated MeasurementSets.

       

      .. rubric:: Antenna Configuration
         :name: antenna-configuration

      The configurations of the ALMA 12-m and 7-m arrays are defined by
      the *antennalist* parameter, which can be a vector. Each element
      of the vector can be either the name of an antenna configuration
      file or a desired resolution, e.g., *‘alma;cycle1;5arcsec’*. Some
      examples:

      -  *antennalist = [’alma.cycle2.5.cfg’,’aca.cycle2.i.cfg’];
         totaltime = [’20min’,’2h’]’*: Will observe the 12-m array in
         configuration C32-5 for 20 minutes and the ACA 7-m array for 2
         hours.
      -  *antennalist = [’alma;cycle2;0.5arcsec’,’aca.i.cfg’]; totaltime
         = [’20min’,’2h’]’:* Will observe the 12-m array in whatever
         Cycle 2 configuration yields a zenith synthesized beam as close
         as possible to 0.5 arcsec (at the center frequency of your
         skymodel) for 20 minutes and the ACA 7-m array for 2 hours.   
      -  *antennalist = [’alma.cycle1.2.cfg’,’aca.cycle2.i.cfg’];
         totaltime = ’20min’*: Will observe the 12-m array in Cycle 1
         configuration 2 for 20 minutes and the ACA 7-m array for the
         default of 2×(12-m time) = 1h20min. This parameter setting will
         also generate a warning that the user is combining
         configurations from different ALMA Cycles (but the simulation
         will run despite that).

      Total power can either be included along with interferometric
      configurations e.g., *antennalist =
      [’alma.cycle1.2.cfg’,’aca.cycle2.i.cfg’,’aca.tp.cfg’]*, or by
      using the *tpnant* and *tptime* parameters. The latter is
      preferred since it allows greater control (in particular the
      number of total power antennas to use – if more than one is used,
      multiple total power observations will be generated and combined
      in imaging).

      .. rubric:: Field Setup
         :name: field-setup

      | There are two ways to setup pointings, i.e., Rectangle Setup and
        Multi-Pointing.
      | In the Rectangle Setups, pointings are automatically calculated
        from the pointing center (direction) and the map size. A
        rectangular map region is covered by a hexagonal grid (*maptype
        = ‘alma’*) with Nyquist sampling, i.e., 0.48 primary beam (PB)
        spacing (where PB ≡ 1.2 λ / D), in both ALMA 12-m and ACA 7-m
        array simulations. A slightly larger area is mapped in ACA total
        power simulations for later combination with interferometer
        visibilities. The map area is extended by 1 PB in each direction
        and covered by a lattice grid with 0.225 PB spacing.

      In Multi-Pointing, a list of pointings is defined in the
      *direction* parameter or read from a file (when *setpointings =
      False*; note that **simobserve** can read ALMA OT pointing files
      in the old and new format but the latter only when they are saved
      as sexagesimal absolute positions). The ALMA 12-m and ACA 7-m
      arrays observe the specified directions. The ACA total power
      simulations map either (1) square regions of 2 PB extent centered
      at each of the pointings, or (2) a rectangle region that covers
      all the pointings. Either (1) or (2), whichever can be done with
      the smaller number of points, is selected. The pointing spacing in
      total power simulations is, again, 0.225 PB in lattice grids.

      It is advisable that for Total Power Simulations, the field is
      chosen sufficiently large, maybe padding at least 1-2 primary
      beams on each side.

      .. rubric:: Integration time
         :name: integration-time

      The total observation time of each component or configuration is
      defined by the *totaltime* parameter as noted above. A scalar will
      trigger use of the Cycle 2 default time multipliers, 1:0.5:2:4 for
      the first 12-m configuration, any additional 12-m configurations,
      any 7-m configuration, and any total power observation.

      In general, the integration time (dump interval) of simulations is
      defined by the integration parameter with an exception. Since the
      ACA total power array always observes larger areas compared to the
      ALMA 12-m and ACA 7-m arrays, it is possible that the ACA total
      power array cannot cover all pointings in the given observation
      time. In such a case, the integration time in the total power
      simulation is scaled so that the all pointings are observed at
      least once in its observation time, i.e., integration_TP = tptime
      / (the number of total power pointings).

      .. rubric:: Imaging and combination of ALMA with ACA
         :name: imaging-and-combination-of-alma-with-aca

      | The CLEAN algorithm is used in **simalma** to generate images
        from visibilities. The visibilities are weighted to UV-plane
        using Briggs weighting.
      | When ACA observations are simulated, visibilities of ACA 7-m are
        weighted by the relative sensitivities to ALMA 12-m
        visibilities, and both data sets are concatenated before
        imaging. The relative weight of ACA 7-m visibilities is defined
        in proportion to the ratio of beam areas squared, i.e.,
        (7/12)4=0.11\ :math:`(7/12)^{4} = 0.11`. This is because
        **simalma** uses a bandwidth and an integration time common to
        both ALMA 12-m and ACA 7-m simulations.

      The interferometer and total power images are combined using
      **feather** task when total power observations are included. The
      total power image is scaled by the interferometer primary beam
      coverage before combination. The final image product is the
      combined image corrected for the interferometer primary beam
      coverage. The output image of the **feather** task is divided by
      the interferometer primary beam coverage in the final step.

       

.. container:: section
   :name: viewlet-below-content-body
