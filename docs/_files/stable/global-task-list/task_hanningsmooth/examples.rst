.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Apply Hanning smoothing on the CORRECTED column. The output will
      be saved into the DATA column.

      .. container:: casa-input-box

         hanningsmooth(vis='example.ms', outputvis='test.ms',
         datacolumn='corrected')

      Apply Hanning smoothing on all visibility columns of the Multi-MS.
      In this case, if CASA is started with
      `mpicasa <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing/parallelization-control>`__,
      the processing will happen in parallel.

      .. container:: casa-input-box

         hanningsmooth(vis='example.mms', outputvis='test.mms') -->
         default

         hanningsmooth(vis='example.mms', outputvis='test.mms',
         datacolumn='all', keepmms=True) --> set the parameters
         explicitly

       

.. container:: section
   :name: viewlet-below-content-body
