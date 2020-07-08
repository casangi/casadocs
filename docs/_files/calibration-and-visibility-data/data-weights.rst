.. container::
   :name: viewlet-above-content-title

Data Weights
============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   A detailed description of visibility weighting

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Visibility weight initialization and calibration has undergone
      several improvements in CASA 4.2.2 and CASA 4.3. This appendix
      briefly describes the formal weight definitions, and the changes
      occurring in these CASA versions.  If data sets shall be combined
      that were reduced with different CASA versions, the weights may
      need to be adjusted accordingly. This can be achieved, e.g. by
      running the same version of **statwt** on all datasets before
      combination. The best option, however, is to use a single CASA
      version for all reductions, preferrably 4.2.2 or later.

      .. container:: info-box

         **NOTE**: Post-calibration weights, e.g. imaging weights or
         tapers are not covered here.

       

      .. rubric:: The *SIGMA* and *WEIGHT* columns
         :name: the-sigma-and-weight-columns

      Formally, in CASA 4.2.2 and later, the *SIGMA* column in the
      measurement set will reflect the per-channel noise of the *DATA*
      column as it depends on the channel bandwidth
      Δν\ :math:`\Delta \nu` and the length of an integration
      Δt\ :math:`\Delta t`:

      SIGMA=1√2ΔνΔt\ :math:`SIGMA = \frac{1}{\sqrt{2\Delta \nu \Delta t}}`

      The factor of √2\ :math:`\sqrt{2}` is for cross-correlations only
      and auto-correlation data follows:

      SIGMA=1/√ΔνΔt\ :math:`SIGMA = 1/\sqrt{\Delta \nu \Delta t}`.

      *SIGMA* will only be updated if the time and channel widths are
      modified along with any *DATA* column manipulation, e.g. through
      averaging, binning, smoothing, etc. (tasks like **mstransform**,
      **cvel**, **split**, **exportuvfits**, etc).

      The *WEIGHT* column reflects how much weight each *CORRECTED_DATA*
      sample should receive when data are combined (e.g., in averaging).
      To start with, *WEIGHT* is initialized from the *SIGMA* column
      via:

      WEIGHT=1SIGMA2=2ΔνΔt\ :math:`WEIGHT = \frac{1}{{SIGMA}^2} = 2 \Delta \nu \Delta t`

      Data calibration by **applycal** with *calwt=True* will calculate
      and modify the *WEIGHT* values but not *SIGMA*. Calibration
      applies multiplicative factors and the *WEIGHT* of a visibility on
      a baseline between antennas i\ :math:`i` and j\ :math:`j` is
      calculated via:

      WEIGHTij=cicjSIGMA2ij\ :math:`WEIGHT_{ij}=\frac{c_i c_j}{{SIGMA}_{ij}^2}`

      where ci\ :math:`c_i` and cj\ :math:`c_j` are the net
      antenna-based power calibration factors derived by **applycal**
      (ci=cj\ :math:`c_i=c_j` for auto-correlation data). In the table
      below, we list the definitions of antenna-based c\ :math:`c` for
      different calibration procedures and CASA versions. When more than
      one calibration is applied, the product of the relevant weight
      factors is used.

      +----------------+----------------+----------------+----------------+
      |                | <=\ :m         | CASA 4.2.2/4.3 | >=\ :m         |
      |                | ath:`<=`\ CASA |                | ath:`>=`\ CASA |
      |                | 4.2.1          |                | 4.4            |
      |                |                |                | *(WEI          |
      |                |                |                | GHT_SPECTRUM)* |
      +================+================+================+================+
      | Initialization | 1.             | 2ΔνΔt\ :       | 2ΔνΔt\ :       |
      |                | 0\ :math:`1.0` | math:`2 \Delta | math:`2 \Delta |
      |                |                |  \nu \Delta t` |  \nu \Delta t` |
      +----------------+----------------+----------------+----------------+
      | System         | 1<√Tsys        | 1<Tsys         | 1Tsys,k\ :mat  |
      | Temperature    | ,k>2k\ :math:` | ,k>k\ :math:`\ | h:`\frac{1}{T_ |
      |                | \frac{1}{<\sqr | frac{1}{<T_{\r | {\rm sys, k}}` |
      |                | t{T_{\rm sys,  | m sys, k}>_k}` |                |
      |                | k}}>_{k}^{2}}` |                |                |
      +----------------+----------------+----------------+----------------+
      | Gain           | \|\|G\|\|2\ :  | \|\|G\|\|2\ :  | \|\|G\|\|2\ :  |
      |                | math:`||G||^2` | math:`||G||^2` | math:`||G||^2` |
      +----------------+----------------+----------------+----------------+
      | Bandpass       | 1<\|\|B\|\|−1> | <\|\|B\|\|     | <\|\|B\|\|     |
      |                | 2k\ :math:`\fr | 2>k\ :math:`<| | 2>k\ :math:`<| |
      |                | ac{1}{<||B||^{ | |B||^{2}>_{k}` | |B||^{2}>_{k}` |
      |                | -1}>_{k}^{2}}` |                |                |
      +----------------+----------------+----------------+----------------+

      .. rubric::  
         :name: section

      .. rubric:: Weights in CASA 4.2.1 and Earlier
         :name: weights-in-casa-4.2.1-and-earlier

      The *SIGMA* and *WEIGHT* columns are initialized with values of
      1.0\ :math:`1.0`.  Traditionally, this convention was adequate for
      datasets with uniform sampling in time in frequency; a global
      weight scale factor would not affect calibration and imaging
      fidelity. In data manipulation operations (e.g., **split**, etc.),
      *SIGMA* was treated as a per-channel value and *WEIGHT* as a
      per-spw (all channels) weight. Combined with unit initialization,
      this difference in definition could lead to incongruent weight
      scales for different spectral windows, in particular if bandwidth
      and channel count varied. CASA 4.2.1 is therefore not recommended
      for datasets which have variety in spectral window bandwidth and
      channelization and for which spectral windows are to be combined
      in imaging.

      .. rubric:: Weights in CASA 4.2.2
         :name: weights-in-casa-4.2.2

      In CASA 4.2.2 the *SIGMA* and *WEIGHT* columns are properly
      initialized via the definition in the above equations. Both are
      defined as per-channel values. Also, the weight calibration
      factors have been subtly updated to improve robustness, as
      indicated in the Table.

      .. rubric:: Weights in CASA 4.3
         :name: weights-in-casa-4.3

      In CASA 4.3 frequency variations of the *WEIGHT* and *SIGMA*
      values are (optionally) captured in additional *WEIGHT_SPECTRUM*
      and *SIGMA_SPECTRUM* columns. This allows accommodation of
      variations of effective sensitivity on a channel by channel basis
      (e.g. band edges, atmospheric lines, spectral
      Tsys\ :math:`T_{\rm sys}` variation etc.). *WEIGHT_SPECTRUM* will
      be recognized in the **applycal** task as well as in
      **mstransform** and **clean**. Calibration solvers, however, will
      not yet calculate and modify *WEIGHT_SPECTRUM*.

      .. rubric:: Weights in CASA 4.4 and later
         :name: weights-in-casa-4.4-and-later

      Full support of *WEIGHT_SPECTRUM*.  

.. container:: section
   :name: viewlet-below-content-body
