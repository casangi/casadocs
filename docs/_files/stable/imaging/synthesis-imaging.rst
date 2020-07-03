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

      This chapter documents CASA's refactored imager. These features
      are visible to the user via the **tclean** task.

      The first five sections give an algorithm-centric view of the
      imager framework and are meant to convey the overall iterative
      reconstruction framework and how various algorithms and usage
      options fit into it. The other sections are more user-centric and
      focus on what one would need to know about specific imaging goals
      such as wideband imaging, mosaicking or details about
      spectral-cube definitions, etc. There is some overlap in content
      between sections, but this is meant to address the needs of
      readers who want to understand how the system works as well as
      those who want to learn how to approach their specific use case.

      .. container:: info-box

         **NOTE**: The older **clean** task also supports most of the
         options described here, with a similar internal structure.
         However, clean will be deprecated in the near future, so we
         strongly encourage to use **tclean** instead. All major
         functionality from clean is now present in tclean via a
         modified interface, along with additional algorithmic options.

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   synthesis-imaging/imaging-overview
   synthesis-imaging/image-definition
   synthesis-imaging/data-weighting
   synthesis-imaging/deconvolution-algorithms
   synthesis-imaging/user-interaction
   synthesis-imaging/masks-for-deconvolution
   synthesis-imaging/spectral-line-imaging
   synthesis-imaging/wide-band-imaging
   synthesis-imaging/wide-field-imaging-full-primary-beam