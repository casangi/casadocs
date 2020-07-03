.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Background SD Calibration
=========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Brief description of calibrating ALMA single-dish observations

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: content5

         Like any single-dish telescope, ALMA's single dish antennas
         (nominally, four 12m antennas) detect and quantify brightness
         temperature ($T_B$, in Kelvin). In the Rayleigh-Jeans
         approximation, the Planck blackbody law reduces to
         $T_B=\frac{B\lambda^2}{2k}$.  

         An ALMA single-dish observation includes contributions from sky
         targets in the beam, the telescope surface and receiver
         equipment, the ground (through reflections), the atmosphere and
         cosmic background, and any other electronics (necessarily
         noisy) following the receiver front end. Observations made with
         a single dish towards a target ($T_{ON}$) are calibrated using
         an additional observation towards blank sky (i.e. sky at a
         similar elevation, absent of any target emission at the
         frequencies of interest to the observer ($T_{OFF}$)).

         To determine the signal from the target, we can compute:

         $\frac{T_{targ}}{T_{sys}}=\frac{T_{ON}-T_{OFF}}{T_{OFF}}$.  
         (In CASA, this is accomplished during the "sky calibration"
         step).

         The position of the OFF is made as close as possible (in az/el)
         to the ON position.  As a practical matter, there may be some
         differences in the two measurements aside from the target being
         in the ON position. In most cases, the differences arise
         chiefly from the atmospheric contribution, though any target
         coincidentally within the beam of the OFF measurement will
         contaminate and affect the accuracy of the OFF measurement, and
         consequently, the measurement of the calibrated brightness
         temperature of the target.

         To calibrate single dish data, we require a measurement of
         $T_{sys}$, which is done though $T_{atm}$ (i.e. "atmosphere")
         measurements at the start of each scheduling block.  (In CASA,
         this is applied through the $T_{sys}$ calibration step.) 
         $T_{sys}$ determination includes separate observations of the
         sky, and two "loads" of different, known temperatures.

         Note that $T_{sys}(\nu)$ measurements are spectral; that is,
         they determine $T_{sys}$ as function of frequency. Since they
         incorporate an observation of the sky, they may include
         atmospheric features such as the water absorption line in Band
         5 at $\sim$183 GHz. So the calibration of the entire band must
         be done in the frequency domain.

         It is policy that ALMA single-dish data must only be observed
         to supplement and be combined with interferometer observations.
         Therefore, the single-dish data needs to be converted from its
         native units of brightness temperature ($T_A^*$) to flux
         density units (Jy/beam) before combination with the
         interferometric data. The conversion from $T_A^*$ to Jy/beam is
         done empirically, and incorporates a factor for forward beam
         efficiency. The empirical conversion (Jy to K) is computed
         through mapping observations (done recently in time) of a
         standard target - either a planet or a quasar - and the scaling
         from $T_A^*$ to Jy/beam is then made simply and directly from
         the calibrator map and applied to the science target map. 

         +-----------------+---------------------------------------------------+
         | Citation Number | 1                                                 |
         +-----------------+---------------------------------------------------+
         | Citation Text   | O'Neil, 2002 in "The NAIC/NRAO School on Single   |
         |                 | Dish Radio Astronomy" C. Salter, et.al eds.       |
         |                 | (`arxiv                                           |
         |                 |  <https://arxiv.org/pdf/astro-ph/0203001.pdf>`__) |
         +-----------------+---------------------------------------------------+

         +-----------------+---------------------------------------------------+
         | Citation Number | 2                                                 |
         +-----------------+---------------------------------------------------+
         | Citation Text   | PdBI mm astro summer school notes (Dutrey, Dutrey |
         |                 | & Neri; Guélin)                                   |
         +-----------------+---------------------------------------------------+

         =============== =========================================
         Citation Number 3
         Citation Text   Unpublished ALMA memo: Robert Lucas, 2005
         =============== =========================================

          

      .. container:: content5

          

.. container:: section
   :name: viewlet-below-content-body
