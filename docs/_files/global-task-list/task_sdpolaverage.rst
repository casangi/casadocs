.. container::
   :name: viewlet-above-content-title

sdpolaverage
============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Averaging over different polarizations for Single Dish MS data

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Task **sdpolaverage** is used to export Single Dish MS data
      averaged over different polarizations, to obtain Stokes I from
      orthogonal autocorrelation pairs (XXYY/LLRR). 

      .. rubric:: Polarization Average
         :name: polarization-average

      Two modes of polarizaton averaging are available. One is 'stokes'
      which is an average based on a formulation of Stokes parameter. In
      this mode, averaged data is calculated by (XX + YY) / 2 or (RR +
      LL) / 2. The other option is 'geometric', which is a conventional
      way of averaging in the field of single-dish data reduction; the
      output data is given by weighted average of XX and YY, or RR and
      LL.

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_sdpolaverage/about
   task_sdpolaverage/examples
