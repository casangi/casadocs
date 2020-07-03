.. container::
   :name: viewlet-above-content-title

Wide-Field Imaging
==================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   W-term, Primary Beams (models, pbcor, A-Projection)

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: **Widefield imaging in CASA
         is\ **\ `experimental <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/tasks-and-tools>`__\ **\ .
         Please use at own discretion.**
         :name: widefield-imaging-in-casa-is-experimental.-please-use-at-own-discretion.

      Imaging modes with A-Projection and mosaics (gridder='mosaic' and
      'awproject') have been validated only for a few usage modes and
      use cases as required by the ALMA and VLASS pipelines. Please use
      these modes at your own discretion, and carefully read the\ `Known
      Issues <https://casa.nrao.edu/casadocs-devel/stable/introduction/known-issues>`__\ for
      CASA 5.6 when using AWproject.

       

      | Wide-field imaging typically refers to fields of view over which
        the basic 2D Fourier transform assumption of interferometric
        imaging does not apply and where standard on-axis calibration
        will not suffice. 
      |  

      .. rubric:: The non-coplanar baseline effect: W-term
         :name: the-non-coplanar-baseline-effect-w-term

      For wide-field imaging, sky curvature and non-coplanar baselines
      result in a non-zero w-term. Standard 2D imaging applied to such
      data will produce artifacts around sources away from the phase
      center. CASA has two methods to correct the w-term effect.

       

      .. rubric:: Faceting
         :name: faceting

      In this method, visibilities are gridded multiple times onto the
      same uv-grid, each time with a different phase-reference center.
      One single dirty/residual image is constructed from the resulting
      grid and deconvolved using a single PSF (picked from the first
      facet). This deconvolution is not affected by emission that
      crosses facet boundaries, unlike in image-domain faceting, which
      is an older approach where small facet images are deconvolved
      separately before being stitched together. `[1] <#cit>`__

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | `Sault et al,                                     |
      |                 | 1999 <https://ui.adsabs.                          |
      |                 | harvard.edu/#abs/1999A&AS..139..387S/abstract>`__ |
      +-----------------+---------------------------------------------------+

      In **tclean**, faceting is available via *gridder='widefield'*
      where you can specify the number of desired facets on a side.  It
      can be used along with W-Projection as well, for very large fields
      of view.

       

      .. rubric:: W-projection
         :name: w-projection

      In this method, visibilities with non-zero w-values are gridded
      using using a gridding convolution function (GCF) given by the
      Fourier transform of the Fresnel EM-wave propagator across a
      distance of w wavelengths. In practice, GCFs are computed for a
      finite set of w-values (wprojplanes) and applied during gridding.
      W-projection is roughly an order of magnitude faster than faceted
      imaging because it grids each visibility only once `[2]. <#cit>`__

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | `Cornwell et al,                                  |
      |                 | 2008 <https://ui.adsabs.                          |
      |                 | harvard.edu/#abs/2008ISTSP...2..647C/abstract>`__ |
      +-----------------+---------------------------------------------------+

      | In **tclean**, w-projection is available via
        *gridder='widefield'* or *'wproject'* or *'awproject'*.  In all
        cases, the '*wprojplanes*' parameter must be set. It represents
        the number of discrete w-values to be used to quantize the range
        of w-values present in the dataset being imaged. An appropriate
        value of wprojplanes depends on whether there is a bright source
        far from the phase center, the desired dynamic range of an image
        in the presence of a bright far out source, the maximum w-value
        in the measurements, and the desired trade off between accuracy
        and computing cost. As a (rough) guide, VLA L-Band D-config may
        require a value of 128 for a source 30arcmin away from the phase
        center. A-config may require 1024 or more. To converge to an
        appropriate value, try starting with 128 and then increasing it
        if artifacts persist. W-term artifacts (for the VLA) typically
        look like arc-shaped smears in a synthesis image or a shift in
        source position between images made at different times. These
        artifacts are more pronounced the further the source is from the
        phase center. There is no harm in simply always choosing a large
        value (say, 1024) but there will be a significant performance
        cost to doing so, especially for *gridder='awproject'* where it
        is combined with A-Projection. *wprojplanes=-1* may be used
        with *gridder='widefield'* or *'wproject'* to automatically
        compute the number of planes.

      The formula that CASA uses to calculate the number of plans when
      *wprojplanes=-1* is:

      $N_\mathrm{wprojplanes} = 0.5\times
      \\frac{W_\mathrm{max}}{\lambda} \\times
      \\frac{\mathrm{imsize}}{\mathrm{(radians)}}$

      where $W_\mathrm{max}$ is the maximum $w$ in your $uvw$ data and
      imsize is the largest linear size of your image. This formula is
      somewhat conservative and it is possible to achieve good results
      by using a smaller number of planes, which can also save on speed
      and memory.

      .. container:: alert-box

         **WARNING**: The algorithm that automatically calculates the
         number of w-bins (wprojplanes = -1) errs on the side of
         numerical accuracy and tends to over-estimate the number of
         w-bins needed. For very wide fields of view, this could result
         in a significant increase in required memory. It is therefore
         useful to point out that it is safe to manually choose a value
         to avoid problems associated with limited memory resources. One
         can do a few tests with different wprojplane values in order to
         find out at which values any shifts in source positions are no
         longer noticeable.

       

      |image1|

       

      .. rubric:: Antenna Voltage/Power Patterns: Primary-Beam
         :name: antenna-voltagepower-patterns-primary-beam

      The aperture-illumination-function (AIF) of each antenna results
      in a direction-dependent complex gain that can vary with time and
      is usually different for each antenna. The resulting antenna power
      pattern is called the primary beam. There are two methods to
      correct for the effect of the primary beam.  

      .. rubric:: Image-domain PB-correction
         :name: image-domain-pb-correction

      A simple method of correcting the effect of the primary beam is a
      post-deconvolution image-domain division of the model image by an
      estimate of the average primary beam or some other model. This
      method ignores primary-beam variations across baselines and time,
      and is therefore approximate, limiting the imaging dynamic-range
      even within the main lobe of the beam.  This approach also cannot
      handle heterogenous arrays.

      In **tclean**, this option is available by setting *pbcor=True*.
       When used with *gridder='standard'* or *'widefield'* or
      *'wproject'* which do not internally use any primary beam models,
      it will compute a model PB at the reference frequency per image
      channel, and divide it out of the output restored image.   If used
      with *gridder='mosaic'* or *'awproject',* it will use a weighted
      average of the primary beam models used by the gridders per
      baseline and timestep.

      Primary Beam correction for wide bandwidth observations is
      discussed in the `Wideband
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__
      section.

      |image2|

       

      .. rubric:: A-Projection
         :name: a-projection

      Time and baseline-dependent corrections are applied during
      gridding, by computing GCFs for each baseline as the convolution
      of the complex conjugates of two antenna aperture illumination
      functions. An additional image-domain normalization step is
      required, and can result in the image being "flat-sky" ( the image
      represents only the sky intensity) or "flat-noise" (the image
      represents the sky multiplied by the primary beam). The advantage
      of this method is that known time and baseline variability can be
      accounted for, both during gridding as well as de-gridding
      `[3] <#cit>`__.

      +-----------------+---------------------------------------------------+
      | Citation Number | 3                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | `Bhatnagar et al,                                 |
      |                 | 2008 <https://ui.adsabs.                          |
      |                 | harvard.edu/#abs/2008A&A...487..419B/abstract>`__ |
      +-----------------+---------------------------------------------------+

      Different primary beam effects cause artifacts at different levels
      in the image `[4] <#cit>`__. Depending on the available
      sensitivity of an observation or desired dynamic range, one can
      choose to leave out some corrections and save on computing time. 
      In general, the varying dish size in a heterogenous array is the
      dominant source of errors causing a dynamic range limit of a few
      100. Next come large pointing offsets (such as beam squint or
      illumination offsets) and at a higher dynamic ranges ($10^4$ and
      beyond) are other factors such as the details about feed leg
      structures. On its own, parallactic angle rotation causes
      artifacts only at a dynamic range of around $10^5$ but if any of
      the other large effects (pointing offset or illumination pattern
      errors) are not azimuthally symmetric, then parallactic angle
      rotation will have an effect at much lower dynamic ranges.

      +-----------------+---------------------------------------------------+
      | Citation Number | 4                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | `Kundert et al                                    |
      |                 | 2016 <http://ieeexplore.ie                        |
      |                 | ee.org/stamp/stamp.jsp?arnumber=7762834&tag=1>`__ |
      +-----------------+---------------------------------------------------+

      .. rubric:: gridder = 'awproject'
         :name: gridder-awproject

      In **tclean**, *gridder='awproject'* applies the full A-Projection
      algorithm and uses baseline, frequency and time dependent primary
      beams. They are azimuthally asymmetric to account for feed leg
      structures. They also include beam squint, which is corrected
      during gridding by applying an appropriate phase gradient across
      the GCFs to cancel out the polarization dependent pointing
      offset.  The frequency dependence of the primary beam within the
      data being imaged is included in the calculations and can
      optionally also be corrected for during gridding (see `Wideband
      Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__
      section for details). 

      The operations of the '*awproject*' gridder are controlled by
      three parameters: *aterm, psterm* and *wprojplanes.*
       *aterm *\ and *psterm *\ controls the inclusion/exclusion of the
      A-term (the antenna aperture function) and the Prolate Spheroidal
      function (the anti-aliasing function) in the convolution functions
      used for gridding. *wprojplanes* controls the inclusion/exclusion
      of the w-term. The following table enumerates the operations for
      the different possible settings of these parameters. PS and PB in
      the table below refers to the Prolate Spheroidal and Primary Beam
      respectivelly and FT() referes to the Fourier transform operation.
      The last column also shows the mathematical content of the .pb
      images, which is one of the image-products on the disk in a
      **tclean** run. For generating a .pb image for image-plane PB
      correction, the gridder needs to be used with *psterm=False* and
      the *cfcache* parameter set to a fresh (non-existant) directory so
      that a fresh cfcache is generated without the PS term in it.  When
      *aterm=False,* the *psterm* parameter needs to be set to *True.*
      It can be set to *False* when *aterm=True. * However with this
      setting the effects of aliasing may be there in the image,
      particularly near the edges.

       

      +-----------+-----------+-----------+-----------+-----------+-----------+
      | Operation | aterm     | psterm    | wp        | GCF       | Contents  |
      |           |           |           | rojplanes |           | of the    |
      |           |           |           |           |           | .pb image |
      +-----------+-----------+-----------+-----------+-----------+-----------+
      | **AW-Pro  | **True**  | **True**  | ** >1**   | *         | **FT(PS)  |
      | jection** |           |           |           | *PS*A*W** | x PB**    |
      |           |           | **False** |           |           |           |
      |           |           |           |           | **A*W**   | **PB**    |
      +-----------+-----------+-----------+-----------+-----------+-----------+
      | **A-Pro   | **True**  | **True**  | **1**     | **PS*A**  | **FT(PS)  |
      | jection** |           |           |           |           | x PB**    |
      |           |           | **False** |           | **A**     |           |
      |           |           |           |           |           | **PB**    |
      +-----------+-----------+-----------+-----------+-----------+-----------+
      | **W-Pro   | **False** | **True**  | **>1**    | **PS*W**  | *         |
      | jection** |           |           |           |           | *FT(PS)** |
      +-----------+-----------+-----------+-----------+-----------+-----------+
      | **S       | **False** | **True**  | **1**     | **PS**    | *         |
      | tandard** |           |           |           |           | *FT(PS)** |
      +-----------+-----------+-----------+-----------+-----------+-----------+

       

       

      Full/Hybrid Mueller matrix support is being added into the system
      for full-polarization widefield imaging.  Currently, heterogenous
      arrays like ALMA are not supported, but it will be suitable for
      VLA widefield imaging. 

       

      .. rubric:: Parallel execution
         :name: parallel-execution

      The computing cost of A-Projection is larger than standard
      imaging, and cost of AW-Projection is higher than A-Projection. 
      However, since the run time scales very well with parallelization,
      these costs can be effectively offset with the use of
      parallelization (using parallel=True; see the `Parallel
      Processing <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__
      section for details about running casa in parallel mode).  The
      runtime scales close to linear with the number of nodes used.  We
      have measured this scaling for up to 200 cores, but the scaling
      may continue further dependening on the data size, data storage
      (e.g., Luster vs. standard file system), image size, algorithms
      used, etc. The plot below shows the measured scaling for a large
      EVLA L-band mosaic imaging experiment. The dark and light blue
      curves (legends "Make PSF + avgPB" and "Make Residual"
      respectively) show the measurement of the steady-state runtime as
      a function of the number of cores used.  The lines in black
      associated with both these curves show the theoratical (ideal)
      linear scaling curves. A memo with the details of the
      characterization of the runtime in parallel mode can be found
      `here <http://www.aoc.nrao.edu/~sbhatnag/misc/Imager_Parallelization.pdf>`__. 
      **Note that parallelization is not restricted to A-Projection and
      can be used with any combination
      of gridder \ and deconolver \ setting.** 

      |image3|

      There are a number of parameters to apply approximations that can
      reduce the computing load.

      Note that current code does not work correctly for non-square
      mosaic images and cube imaging. Fixes for these will be included
      in subsequent releases.   VLA and ALMA data sets often carry the
      POINTING table with antenna pointing information which may not be
      correct.  Since by default the imaging module now uses the
      POINTING table, the POINTING table may need to be disabled (delete
      all rows of the POINTING sub-table in the MS).

       

      |image4|

      .. rubric:: gridder='mosaic'
         :name: griddermosaic

      In **tclean**, *gridder='mosaic'* applies an approximation of the
      A-Projection algorithm where it uses azimuthally symmetric beam
      models that can be different per baseline. It includes the
      diagonal of the Mueller matrix for multi-Stokes images, but
      ignores off-diagonals. The frequency dependence of the primary
      beam is accounted for but is not eliminated during gridding. Since
      time dependence is not supported by default, the computational
      cost is lower than A-Projection.   Since ALMA imaging typically
      involves small fractional bandwidths, includes data with multiple
      dish sizes, and needs to operate on very large cubes with many
      channels, this option is suitable for ALMA.  It is also possible
      to supply external beam models to this gridder, by setting up the
      vpmanager tool, and one can in principle assign beams separately
      for each antenna as a function of time, if needed. Note that
      *gridder='mosaic'* can be used even on a single pointing,
      especially to account for effects due to a heterogenous array. 

       

      .. rubric:: Mosaics
         :name: mosaics

      Data from multiple pointings can be combined during gridding to
      form one single large image. Details are are described in the
      `Mosaicing <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/mosaicing>`__
      page.  In a Linear Mosaic, data from multiple pointings are imaged
      (and optionally deconvolved too) before being stitched together. A
      Joint Mosaic is a simple extension of A-Projection in which phase
      gradients are applied to the gridding convolution functions to map
      data from each pointing to a different position on the sky.  In
      **tclean**, *gridder='mosaic'* and *'awproject'* will both create
      joint mosaics if data from multiple pointings are selected as the
      input.

      .. rubric:: Pointing Offset Corrections
         :name: pointing-offset-corrections

      When the image phase center is chosen to be different from the
      observation phase center, a phase gradient is applied during
      gridding convolution to ensure that the image-domain primary beam
      is centered at the phase-reference direction. This situation is
      encountered for all joint mosaic imaging. By default, it is
      assumed that the antennas point in the same direction as the
      observation phase center specified in the FIELD subtable of the
      MS. However, entries may be supplied in the POINTING subtable of
      the MS and used instead of the FIELD table via the *'usepointing'*
      parameter available to *gridders='mosaic'* and *'awproject'*. The
      VLASS project, for example, has time-dependent and
      antenna-dependent pointing offsets that are not captured in the
      FIELD table and which require an additional POINTING table. Note
      that *'usepointing=True'* has no meaning if there are no entries
      in the POINTING subtable (the default with any MS). Therefore, the
      default is *'usepointing=False'.*

      -  *gridder='mosaic'* reads and uses the pointing offset per
         timestep and baseline, but assumes that both antennas in a
         baseline pair are pointed in the same direction as the ANTENNA1
         listed in the MS for each baseline and timestep. This has not
         been officially validated for CASA 5.6.
      -  *gridder='awproject'* reads and uses the pointing offsets for
         both antennas in the first baseline pair listed in the MS (per
         timestep) and assumes this is constant across all baselines. It
         applies phase gradients per timestep with the assumption that
         all antennas are pointed in the same direction. This has been
         validated on VLASS 1.2 data.

      .. container:: alert-box

         **WARNING**: For CASA 5.6, with *'usepointing=True'*, the
         *gridder='mosaic'* and *'awproject'* implement slightly
         different solutions. For CASA 5.6, only *gridder='awproject'*
         has been validated for *usepointing=True*. A few other features
         are expected to be implemented post 5.6, as described in the
         `Known
         Issues <https://casa.nrao.edu/casadocs-devel/stable/introduction/known-issues>`__.

       

      .. rubric:: Primary Beam Models
         :name: primary-beam-models

      .. rubric:: gridder='standard', 'wproject', 'widefield', 'mosaic'
         :name: gridderstandard-wproject-widefield-mosaic

      Default PB models :

      VLA: PB polynomial fit model (`Napier and Rots,
      1982)  <https://library.nrao.edu/public/memos/vla/test/VLAT_134.pdf>`__\ `[5] <#cit>`__

      +-----------------+---------------------------------------------------+
      | Citation Number | 5                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | `Napier and Rots,                                 |
      |                 | 1982 <https://librar                              |
      |                 | y.nrao.edu/public/memos/vla/test/VLAT_134.pdf>`__ |
      +-----------------+---------------------------------------------------+

      EVLA: New EVLA beam models (`Perley
      2016 <https://library.nrao.edu/public/memos/evla/EVLAM_195.pdf>`__)
      `[6] <#cit>`__

      +-----------------+---------------------------------------------------+
      | Citation Number | 6                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | `Perley                                           |
      |                 | 2016 <https://lib                                 |
      |                 | rary.nrao.edu/public/memos/evla/EVLAM_195.pdf>`__ |
      +-----------------+---------------------------------------------------+

      ALMA : Airy disks for a 10.7m dish (for 12m dishes) and  6.25m
      dish (for 7m dishes) each with 0.75m blockages (Hunter/Brogan
      2011). Joint mosaic imaging supports heterogeneous arrays for
      ALMA  (Hunter/Brogan 2011)

      These are all azimuthally symmetric beams. For EVLA, these models 
      limit the dynamic range to 10^5 due to  beam squint with rotation
      and the presence of feed leg structures.  For ALMA, these models
      accounting only for differences in dish size, but not in any
      feed-leg structural differences between the different types of
      antennas.

       

      .. rubric:: Adding other PB models
         :name: adding-other-pb-models

      Use the vpmanager tool, save its state, and supply as input to
      **tclean**'s *vptable* parameter

      Example : For ALMA and gridder='mosaic', ray-traced (TICRA) beams
      are also available via the vpmanager tool. To use them, call the
      following before the tclean run: 

      .. container:: casa-input-box

         | vp.setpbimage(telescope="ALMA",
           compleximage='/home/casa/data/trunk/alma/responses/ALMA_0_DV__0_0_360_0_45_90_348.5_373_373_GHz_ticra2007_VP.im', 
           antnames=['DV'+'%02d'%k for k in range(25)])
         | vp.saveastable('mypb.tab')

      | 
      | Then, supply vptable='mypb.tab' to tclean.

       

      .. rubric:: gridder = 'awproject'
         :name: gridder-awproject-1

      VLA / EVLA : Uses ray traced models (VLA and EVLA) including feed
      leg and subreflector shadows, off-axis feed location (for beam
      squint and other polarization effects), and a Gaussian fit for the
      feed beams `[7]. <#cit>`__

      The following figure shows an example of the ray-traced PB
      models.  Image on the left shows the instantaneous narrow-band PB
      at the lowest frequency in the band while the image on the right
      shows the wide-band continuum beam.  Sidelobes are at a few
      percent level and highly azimuthally asymmetric.  This asymmetry
      shows up as time-varying gains across the image as the PB rotates
      on the sky with Parallactic Angle.

      |image5|

       

       

      .. rubric:: External Beam models for gridder= 'awproject'
         :name: external-beam-models-for-gridder-awproject

      The beam models used internally in 'awproject' are derived from
      ray-traced aperture illumination functions.  However since the
      'awproject' algorithm uses the disk CF cache mechanism, a simple
      way to use a different beam model is to construct the disk CF
      cache and supply that to 'awproject' during imaging.  The detailed
      documention for construcing the disk CF cache is being developed
      and will be released in subsequent CASA Docs release.  In the
      meantime, if you need to access this route sooner, please contact
      the CASA Helpdesk who will direct you to the related (not yet
      released) documentation or appropriate Algorithms R&D Group (ARDG)
      staff.

      +-----------------+---------------------------------------------------+
      | Citation Number | 7                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | `Brisken                                          |
      |                 | 2009 <https://ui.adsabs.                          |
      |                 | harvard.edu/#abs/2009nsem.confE..21B/abstract>`__ |
      +-----------------+---------------------------------------------------+

      ALMA : Similar ray-traced model as above, but since  the
      correctness of its polarization properties remains un-verified,
      support for ALMA is not yet released for general users.

      The current implementation of AW-Projection does not yet support
      heterogenous arrays (although the version of CASA's AWProjection
      used by LOFAR's LWImager does have fully heterogenous support).
      This, along with Full-polarization support is currently being
      worked on in ARDG branches.

       

      .. rubric:: Heterogeneous Pointing Corrections
         :name: heterogeneous-pointing-corrections

      Due to the high sensitivity of EVLA and ALMA telescopes, imaging
      performance can be limited by the antenna pointing errors. These
      pointing errors in general also vary significantly across the
      array and with time. Corrections to the true antenna pointing
      directions are contained in the POINTING sub-table, and if these
      corrections are present and accurate, they can be used to
      improve imaging of both single-pointing and mosaic fields. These
      heterogeneous pointing corrections are controlled by two
      parameters in **tclean**:

      **usepointing**: When set to *True*, the antenna pointing vectors
      are fetched from the POINTING sub-table. When set to *False* (the
      default), the vectors are determined from the FIELD sub-table,
      effectively disabling correction of antenna pointing errors.

      **pointingoffsetsigdev**: When correcting for pointing errors, the
      first value given in the *pointingoffsetsigdev* task is the size
      in arcsec of the bin used to discover antenna grouping for which
      phase gradients are computed. A compute for a new phase gradient
      is triggered for a bin if the length of the mean pointing vector
      of the antennas in the bin changes by more than the second value.
      The default value of this parameter is [], due a programmatic
      constraint. If run with this value, it will internally pick
      [600,600] and exercise the option of using large tolerances
      (10arcmin) on both axes. Please choose a setting explicitly for
      runs that need to use this parameter.

      .. container:: alert-box

         **WARNING**: Heterogeneous pointing corrections have been
         implemented in support of the VLA Sky Survey. This option is
         available only for *gridder='awproject'* and has been validated
         primarily with VLASS on-the-fly mosaic data where POINTING
         subtables have been modified after the data are recorded. The
         use of pointing corrections is currently unverified for general
         VLA and ALMA data, so users should use these parameters at
         their discretion.

      | A description of the algorithm that handles the antenna pointing
        corrections for the AW-Projection algorithm in CASA can be found
        in `CASA memo
        11 <https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-memos/heterogeneous_pointing_corrections_memo11.pdf>`__.
      | The implementation of heterogeneous antenna pointing corrections
        was driven by requirements for the VLA Sky Survey (VLASS).
        Additional testing of Wideband Mosaic Imaging and Pointing
        Corrections can be found in this `Knowledgebase
        article <https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-knowledgebase/wideband-mosaic-imaging-and-pointing-corrections-for-the-vla-sky-survey>`__.

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig_wterm_compare.png/@@images/1a101041-9992-4609-9d51-c73a29c13553.png
   :class: image-inline
   :width: 513px
   :height: 193px
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig_pbcor.png/@@images/88dfd93d-bb63-443d-8259-0479be666c6f.png
   :class: image-inline
   :width: 522px
   :height: 246px
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/runtime_withcostofselection.png/@@images/26582cc7-58de-435e-bb16-7a01dce1f5a1.png
   :class: image-inline
   :width: 554px
   :height: 388px
.. |image4| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig_aproj_artifact_example-1.png/@@images/86d3af37-15a7-4bfb-ba6d-f29572dd5739.png
   :class: image-inline
   :width: 583px
   :height: 349px
.. |image5| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/nb_wb_pb-2.png/@@images/09b10315-f3ce-415d-a561-f282f76a2052.png
   :class: image-inline
   :width: 676px
   :height: 301px
