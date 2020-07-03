.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Overview
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Chapter overview

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: content

         This section describes imaging single-dish data.

         The data should already be T$_{sys}$ and T$_{sky}$ calibrated
         (at least into antenna temperature units, $T_A^*$ [K]) ,
         according to the process described in the single-dish
         calibration pages.

         The CASA task used for imaging single-dish data is
         `sdimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdimaging>`__. 
         This task will return a four-dimensional array with two
         position axes, one frequency or velocity axis, and one
         polarization axis. The output of
         `sdimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdimaging>`__
         is a CASA image that can be explored, analyzed, and manipulated
         in CASA, or exported into a versatile FITS image format via
         `exportfits <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_exportfits>`__.

         The pages below first describe the general process of gridding
         single-dish data followed by the actual procedures invoked with
         CASA.

.. container:: section
   :name: viewlet-below-content-body
