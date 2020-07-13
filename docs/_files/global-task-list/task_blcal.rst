blcal
=====

.. container:: documentDescription description

   Calculate a baseline-based calibration solution (gain or bandpass)

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary
         :name: summary

      The **blcal** task determines baseline-based time- and/or
      frequency-dependent gains for all baselines in the data set. Such
      solutions are in contrast to **gaincal** and **bandpass**
      solutions which are antenna-based and better constrained.

      .. container:: info-box

         In general, solving for and applying baseline-based calibration
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
         :name: common-calibration-solve-parameters

      The **blcal** task uses all of the same parameters as gaincal and
      bandpass, which the exception of gaintype and bandtype,
      respectively. See `"Solving for
      Calibration" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/solving-for-calibration>`__
      for general information about calibration solving parameters.

      .. rubric:: Controlling frequency-dependence in blcal: *freqdep*
         :name: controlling-frequency-dependence-in-blcal-freqdep

      The parameter *freqdep* controls whether or not a
      channel-dependent solution should be obtained. If *freqdep=True*,
      a channelized solution (like **bandpass**, but baseline-based)
      will be obtained; otherwise the solution will be unchannelized
      (like **gaincal**, but baseline-based).

       

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_blcal/parameters
   task_blcal/changelog
   task_blcal/examples
