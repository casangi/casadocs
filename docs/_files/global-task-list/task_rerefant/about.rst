.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary:
         :name: summary

      The time-dependent phases for a specified caltable are
      re-referenced to a new antenna by the specified algorithm.

      .. rubric:: Introduction
         :name: introduction

      Fundamentally, the baseline visibility phases measured by a
      synthesis instrument are exclusively differences (between
      antennas), and so no absolute phase reference exists.
      Antenna-based calibration solutions thus have phases which are
      constrained only to satisfy the observed visibility phases;
      further, each solution in time is formally independent of all
      others, though stability (or at least continuity) in time is
      expected. Therefore, to assert phase continuity in time, it is
      conventional practice to assign a reference antenna whose phase
      will be held constant at zero in time. Any actual phase variation
      associated with the reference antenna will be transferred to the
      phase solutions of all others (consistent with satisfying the
      visibility phase differences), and if the time sampling is
      adequate, phase continuity for all antennas—and thus also for all
      visibility baselines—will be assured. Usually, the phase reference
      antenna is applied on the back-end of the calibration solving
      task, e.g., **gaincal** or **bandpass**.

      However, it is sometimes the case that the referencing must be
      reapplied with a different reference antenna choice, or with a
      different algorithm, e.g., due to dropouts (from visibility
      flagging) or other problems in the nominally preferred reference
      antenna. The **rerefant** task provides a convenient mechanism to
      achieve this without having to re-run the calibration solving task
      with only a new *refant* setting.

      .. rubric:: Input/Output parameters
         :name: inputoutput-parameters

      An input MS, input caltable, and output caltable are specified in
      *vis*, *tablein*, and *caltable*, respectively.

      .. rubric:: Reference antenna choice: *refant*
         :name: reference-antenna-choice-refant

      Reference antennas are specified using the *refant* parameter. A
      list of antennas may be specified in decreasing order of
      preference. (See below for the conditions under which alternate
      reference antennas are used.)\ *
      *

       

      .. rubric:: Phase referencing mode: *refantmode*
         :name: phase-referencing-mode-refantmode

      The *refantmode* parameter controls how the refant is applied.
      Currently available choices are 'flex' and 'strict'.

      .. rubric:: *refantmode='flex'*
         :name: refantmodeflex

      If the preferred or current *refant* drops out, switch to another.
      Alternate reference antennas will be chosen from the *refant*
      parameter (if a nontrivial list of antennas is specified), or
      according to proximity to the last-used refant. If and when the
      preferred refant returns, the referencing will switch back to it.
      Note that the preferred reference antenna may no longer be at zero
      at phase with respect to the alternate refant, and so it will
      return at a new phase value that will be kept constant from that
      point. Generally, this mode of referencing should ensure
      continuity at the available phase SNR (signal-to-noise ratio).
      However, under low SNR conditions, the effective cross-hand phase
      may not be assured stable at refant changes, since each hand of
      polarization is referenced independently, and the non-zero noise
      on the cross-hand phase difference will change. When doing
      polarimetry (which depends on stable cross-hand phase), it may be
      preferable to use *refantmode='strict'* (see below).

      .. rubric:: *refantmode='strict'*
         :name: refantmodestrict

      If the preferred or current refant is absent for a solution, flag
      all antennas at that solution. This mode ensures that the
      effective cross-hand phase will be maintained constant and equal
      to that of the chosen refant, and not subject to variation due to
      finite SNR when switching among reference antennas. If a list of
      antennas is specified in *refant*, only the first is used. Note
      that *refantmode='strict'* is not reversible, since the reason for
      flagging solutions is not preserved. Also note that a poor refant
      choice could lead to excessive data flagging when using this mode.

       

.. container:: section
   :name: viewlet-below-content-body
