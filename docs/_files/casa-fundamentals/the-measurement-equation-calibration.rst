.. container::
   :name: viewlet-above-content-title

Measurement Equation
====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   The synthesis calibration model

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The visibilities measured by an interferometer must be calibrated
      before formation of an image. This is because the wavefronts
      received and processed by the observational hardware have been
      corrupted by a variety of effects. These include (but are not
      exclusive to): the effects of transmission through the atmosphere,
      the imperfect details amplified electronic (digital) signal and
      transmission through the signal processing system, and the effects
      of formation of the cross-power spectra by a correlator.
      Calibration is the process of reversing these effects to arrive at
      corrected visibilities which resemble as closely as possible the
      visibilities that would have been measured in vacuum by a perfect
      system. The subject of this chapter is the determination of these
      effects by using the visibility data itself.

      .. rubric:: The HBS Measurement Equation
         :name: the-hbs-measurement-equation

      The relationship between the observed and ideal (desired)
      visibilities on the baseline between antennas i and j may be
      expressed by the Hamaker-Bregman-Sault *Measurement Equation*
      Hamaker, Bregman, & Sault (1996) `[1] <#cit1>`__ and Sault,
      Hamaker, Bregman (1996) `[2] <#cit2>`__ .

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Hamaker, J.P., Bregman, J.D. & Sault, R.J. 1996,  |
      |                 | A&AS, 117, 137                                    |
      |                 | (`ADS <http://a                                   |
      |                 | dsabs.harvard.edu/abs/1996A%26AS..117..137H>`__). |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Sault, R. J.; Hamaker, J. P.; Bregman, J. D.      |
      |                 | 1996, A&AS, 117, 149                              |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/1996A%26AS..117..149S>`__) |
      +-----------------+---------------------------------------------------+

      →Vij = Jij →V IDEALij\ 

      .. math:: \begin{eqnarray} \vec{V}_{ij}~=~J_{ij}~\vec{V}_{ij}^{\mathrm{~IDEAL}} \end{eqnarray}

      | where→Vij\ :math:`\vec{V}_{ij}` represents the observed
        visibility, a complex number representing the amplitude and
        phase of the correlated data from a pair of antennas in each
        sample time, per spectral channel.
        →V IDEALij\ :math:`\vec{V}_{ij}^{\mathrm{~IDEAL}}` represents
        the corresponding ideal visibilities, and Jij\ :math:`J_{ij}`
        represents the accumulation of all corruptions affecting
        baseline ij\ :math:`ij`. The visibilities are indicated as
        vectors spanning the four correlation combinations which can be
        formed from dual-polarization signals. These four correlations
        are related directly to the Stokes parameters which fully
        describe the radiation. The Jij\ :math:`J_{ij}` term is
        therefore a 4×\ :math:`\times`\ 4 matrix.
      | Most of the effects contained in Jij\ :math:`J_{ij}` (indeed,
        the most important of them) are antenna-based, i.e., they arise
        from measurable physical properties of (or above) individual
        antenna elements in a synthesis array. Thus, adequate
        calibration of an array of Nant\ :math:`N_{ant}` antennas
        forming Nant(Nant−1)/2\ :math:`N_{ant} (N_{ant}-1)/2` baseline
        visibilities is usually achieved through the determination of
        only Nant\ :math:`N_{ant}` factors, such that
        Jij=Ji⊗J∗j\ :math:`J_{ij} = J_i \otimes J_j^{*}`.  For the rest
        of this chapter, we will usually assume that Jij\ :math:`J_{ij}`
        is factorable in this way, unless otherwise noted.

      As implied above, Jij\ :math:`J_{ij}` may also be factored into
      the sequence of specific corrupting effects, each having their own
      particular (relative) importance and physical origin, which
      determines their unique algebra. Including the most commonly
      considered effects, the Measurement Equation can be written:

      →Vij = Mij Bij Gij Dij Eij Pij Tij →V IDEALij\ 

      .. math:: \begin{eqnarray} \vec{V}_{ij}~=~M_{ij}~B_{ij}~G_{ij}~D_{ij}~E_{ij}~P_{ij}~T_{ij}~\vec{V}_{ij}^{\mathrm{~IDEAL}}    \end{eqnarray}

      | 
      | where:

      -  Tij = \ :math:`T_{ij}~=~` Polarization-independent
         multiplicative effects introduced by the troposphere, such as
         opacity and path-length variation.
      -  Pij = \ :math:`P_{ij}~=~` Parallactic angle, which describes
         the orientation of the polarization coordinates on the plane of
         the sky. This term varies according to the type of the antenna
         mount.
      -  Eij = \ :math:`E_{ij}~=~` Effects introduced by properties of
         the optical components of the telescopes, such as the
         collecting area's dependence on elevation.
      -  Dij = \ :math:`D_{ij}~=~` Instrumental polarization response.
         "D-terms" describe the polarization leakage between feeds (e.g.
         how much the R-polarized feed picked up L-polarized emission,
         and vice versa).
      -  Gij = \ :math:`G_{ij}~=~` Electronic gain response due to
         components in the signal path between the feed and the
         correlator. This complex gain term Gij\ :math:`G_{ij}` includes
         the scale factor for absolute flux density calibration, and may
         include phase and amplitude corrections due to changes in the
         atmosphere (in lieu of Tij\ :math:`T_{ij}`). These gains are
         polarization-dependent.
      -  Bij = \ :math:`B_{ij}~=~` Bandpass (frequency-dependent)
         response, such as that introduced by spectral filters in the
         electronic transmission system
      -  Mij = \ :math:`M_{ij}~=~` Baseline-based correlator
         (non-closing) errors. By definition, these are not factorable
         into antenna-based parts.  

      | Note that the terms are listed in the order in which they affect
        the incoming wavefront (G\ :math:`G` and B\ :math:`B` represent
        an arbitrary sequence of such terms depending upon the details
        of the particular electronic system). Note that M\ :math:`M`
        differs from all of the rest in that it is not antenna-based,
        and thus not factorable into terms for each antenna.
      | As written above, the measurement equation is very general; not
        all observations will require treatment of all effects,
        depending upon the desired dynamic range. E.g., instrumental
        polarization calibration can usually be omitted when observing
        (only) total intensity using circular feeds. Ultimately,
        however, each of these effects occurs at some level, and a
        complete treatment will yield the most accurate calibration.
        Modern high-sensitivity instruments such as ALMA and JVLA will
        likely require a more general calibration treatment for similar
        observations with older arrays in order to reach  the advertised
        dynamic ranges on strong sources.
      | In practice, it is usually far too difficult to adequately
        measure most calibration effects absolutely (as if in the
        laboratory) for use in calibration. The effects are usually far
        too changeable. Instead, the calibration is achieved by making
        observations of calibrator sources on the appropriate timescales
        for the relevant effects, and solving the measurement equation
        for them using the fact that we have
        Nant(Nant−1)/2\ :math:`N_{ant}(N_{ant}-1)/2` measurements and
        only Nant\ :math:`N_{ant}` factors to determine (except for
        M\ :math:`M` which is only sparingly used). Note: By
        partitioning the calibration factors into a series of
        consecutive effects, it might appear that the number of free
        parameters is some multiple of Nant\ :math:`N_{ant}`, but the
        relative algebra and timescales of the different effects, as
        well as the  multiplicity of observed polarizations and channels
        compensate, and it can be shown that the problem remains 
        well-determined until, perhaps, the effects are
        direction-dependent within the field of view. Limited solvers
        for such effects are under study; the **calibrater** tool
        currently only handles effects which may be assumed constant
        within the field of view. Corrections for the primary beam are
        handled in the **imager** tool.  Once determined, these terms
        are used to correct the visibilities measured for the scientific
        target. This procedure is known as cross-calibration (when only
        phase is considered, it is called phase-referencing).

      | The best calibrators are point sources at the phase center
        (constant visibility amplitude, zero phase), with sufficient
        flux density to determine the calibration factors with adequate
        SNR on the relevant timescale. The primary gain calibrator must
        be sufficiently close to the target on the sky so that its
        observations sample the same atmospheric effects. A bandpass
        calibrator usually must be sufficiently strong (or observed with
        sufficient duration) to provide adequate per-channel sensitivity
        for a useful calibration. In practice, several calibrators are
        usually observed, each with properties suitable for one or more
        of the required calibrations.
      | Synthesis calibration is inherently a bootstrapping process.
        First, the dominant calibration term is determined, and then,
        using this result, more subtle effects are solved for, until the
        full set of required calibration terms is available for
        application to the target field. The solutions for each
        successive term are relative to the previous terms.
        Occasionally, when the several calibration terms are not
        sufficiently orthogonal, it is useful to re-solve for earlier
        types using the results for later types, in effect, reducing the
        effect of the later terms on the solution for earlier ones, and
        thus better isolating them. This idea is a generalization of the
        traditional concept of self-calibration, where initial imaging
        of the target source supplies the visibility model for a
        re-solve of the gain calibration (G\ :math:`G` or T\ :math:`T`).
        Iteration tends toward convergence to a statistically optimal
        image. In general, the quality of each calibration and of the
        source model are mutually dependent. In principle, as long as
        the solution for any calibration component (or the source model
        itself) is likely to improve substantially through the use of
        new information (provided by other improved solutions), it is
        worthwhile to continue this process.
      | In practice, these concepts motivate certain patterns of
        calibration for different types of observation, and the
        **calibrater** tool in CASA is designed to accommodate these
        patterns in a general and flexible manner. For a spectral line
        total intensity observation, the pattern is usually:

      #. Solve for G\ :math:`G` on the bandpass calibrator
      #. Solve for B\ :math:`B` on the bandpass calibrator, using
         G\ :math:`G`
      #. Solve for G\ :math:`G` on the primary gain (near-target) and
         flux density calibrators, using B\ :math:`B` solutions just
         obtained
      #. Scale G\ :math:`G` solutions for the primary gain calibrator
         according to the flux density calibrator solutions
      #. Apply G\ :math:`G` and B\ :math:`B` solutions to the target
         data
      #. Image the calibrated target data

      If opacity and gain curve information are relevant and available,
      these types are incorporated in each of the steps (in future, an
      actual solve for opacity from appropriate data may be folded into
      this process):

      #. Solve for G\ :math:`G` on the bandpass calibrator, using
         T\ :math:`T` (opacity) and E\ :math:`E` (gain curve) solutions
         already derived.
      #. Solve for B\ :math:`B` on the bandpass calibrator, using
         G\ :math:`G`, T\ :math:`T` (opacity), and E\ :math:`E` (gain
         curve) solutions.
      #. Solve for G\ :math:`G` on primary gain (near-target) and flux
         density calibrators, using B\ :math:`B`, T\ :math:`T`
         (opacity), and E\ :math:`E` (gain curve) solutions.
      #. Scale G\ :math:`G` solutions for the primary gain calibrator
         according to the flux density calibrator solutions
      #. Apply T\ :math:`T` (opacity), E\ :math:`E` (gain curve),
         G\ :math:`G`, and B\ :math:`B` solutions to the target data
      #. Image the calibrated target data

      For continuum polarimetry, the typical pattern is:

      #. Solve for G\ :math:`G` on the polarization calibrator, using
         (analytical) P\ :math:`P` solutions.
      #. Solve for D\ :math:`D` on the polarization calibrator, using
         P\ :math:`P` and G\ :math:`G` solutions.
      #. Solve for G\ :math:`G` on primary gain and flux density
         calibrators, using P\ :math:`P` and D\ :math:`D` solutions.
      #. Scale G\ :math:`G` solutions for the primary gain calibrator
         according to the flux density calibrator solutions.
      #. Apply P\ :math:`P`, D\ :math:`D`, and G\ :math:`G` solutions to
         target data.
      #. Image the calibrated target data.

      | For a spectro-polarimetry observation, these two examples would
        be folded together.
      | In all cases the calibrator model must be adequate at each solve
        step. At high dynamic range and/or high resolution, many
        calibrators which are nominally assumed to be point sources
        become slightly resolved. If this has biased the calibration
        solutions, the offending calibrator may be imaged at any point
        in the process and the resulting model used to improve the
        calibration. Finally, if sufficiently strong, the target may be
        self-calibrated as well.

       

      .. rubric:: General Calibrater Mechanics
         :name: general-calibrater-mechanics

      The **calibrater** tasks/tool are designed to solve and apply
      solutions for all of the solution types listed above (and more are
      in the works). This leads to a single basic sequence of execution
      for all solves, regardless of type:

      #. Set the calibrator model visibilities
      #. Select the visibility data which will be used to solve for a
         calibration type
      #. Arrange to apply any already-known calibration types (the first
         time through, none may yet be available)
      #. Arrange to solve for a specific calibration type, including
         specification of the solution timescale and other specifics
      #. Execute the solve process
      #. Repeat 1-4 for all required types, using each result, as it
         becomes available, in step 3, and perhaps repeating for some
         types to improve the solutions

      By itself, this sequence doesn't guarantee success; the data
      provided for the solve must have sufficient SNR on the appropriate
      timescale, and must provide sufficient leverage for the solution
      (e.g., D solutions require data taken over a sufficient range of
      parallactic angle in order to separate the source polarization
      contribution from the instrumental polarization).

   .. container::
      :name: citation-container

      .. container::
         :name: citation-title

         Bibliography

      .. container::

         :sup:`1. Hamaker, J.P., Bregman, J.D. & Sault, R.J. 1996, A&AS,
         117, 137
         (`\ `ADS <http://adsabs.harvard.edu/abs/1996A%26AS..117..137H>`__\ :sup:`).`\ `↩ <#ref-cit1>`__

      .. container::

         :sup:`2. Sault, R. J.; Hamaker, J. P.; Bregman, J. D. 1996,
         A&AS, 117, 149
         (`\ `ADS <http://adsabs.harvard.edu/abs/1996A%26AS..117..149S>`__\ :sup:`)`\ `↩ <#ref-cit2>`__

.. container:: section
   :name: viewlet-below-content-body
