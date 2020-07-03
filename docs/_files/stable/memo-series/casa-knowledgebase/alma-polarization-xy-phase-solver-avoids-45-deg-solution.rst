.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

ALMA polarization: XY-phase solver avoids +-45 deg solution
===========================================================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   The XY-phase calibration obtained with CASA task gaical
   (gaintype='XYf+QU') avoids to output +/- 45 degree solutions. This is
   a subtle consequence of the algorithm used to solve for the
   cross-hand phase, and should be harmless for the calibration of ALMA
   full-polarization data.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      When using the task **gaincal** with parameter
      *gaintype='XYf+QU'*, the solution to solve is a fit for a slope in
      2D data (imag vs. real) from data that has noise is *both*
      dimensions.  In such cases, it is always better to fit a *shallow*
      (not steep) slope, so if the slope (for imag vs. real) comes out
      >1.0, it flips the axes (to real vs. imag) and re-fits it (and
      inverts the resulting value to account for the swap).  This
      minimizes the effect of the real axis noise on the slope
      calculation. This yields far more accurate solutions when the
      nominal slope is very large (>>1.0, e.g., the data nearly parallel
      to the imag axis == cross-hand phase approaching +/-90 deg). 

      The case of slope = 1.0 (which is cross-hand phase of 45 deg)
      corresponds to the slope at which to pivot the axis swap decision.
      When plotting the cross-hand phase solutions, a gap appears at
      +-45 deg (see figure). This gap is a property of the typical
      spacings between values in the statistical distribution of slope
      values.  I.e., for a sample of N points filling a distribution
      with a finite width, there is a characteristic *minimum* spacing
      between values that is some small *fraction* of the width of the
      distribution.  Of course, smaller spacings are not forbidden, but
      they are rare.  The axis swap reveals this property since all of
      the (nominal) slopes that are >1.0 (cross-hand phases >45.0 deg)
      are fit with swapped data and yield the inverse slope (<1.0), and
      than inverted to be >1.0 again.  The typical slopes mostly do not
      get arbitrarily close to exactly 1.0, so the gap appears.  This is
      essentially an extension of the fact that (for *any* slope), the
      precise exact value need not be realized in any instance in a
      sample of solutions for it.  E.g., in a sample of N
      gaussian-distributed values centered on some specific value the
      likelihood of any sample having that *precise* central value is
      vanishingly small. 

      The gap should become smaller when either the noise decreases, or
      the number of channels (for the same noise) increases.

      This feature should be harmless for the calibration of ALMA
      full-polarization data.

      |image1|

       

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-knowledgebase/spw29_multiplot.png/@@images/f8fd0ec9-5d6a-48d0-856c-63473f11568a.png
   :class: image-inline
