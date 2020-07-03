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

      .. rubric:: Display a MeasurementSet as a raster image
         :name: display-a-measurementset-as-a-raster-image

      .. container:: casa-input-box

         | # In CASA
         | msview(infile='my_MeasurementSet.ms', displaytype='raster')

      This displays the MeasurementSet as a raster image. Settings
      (e.g., axes) can then be manually adjusted using the interactive
      Viewer Display Panel. If no *infile* is specified, the Load Data
      window will appear for selecting data.

      The parameter *displaytype* (optional) gives the method of
      rendering data visually using one of the following settings:
      raster (default), contour, vector or marker. You can also set this
      parameter to 'lel' to provide a `Lattice Expression
      Language <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lattice-expression-language>`__ expression for
      *infile* (advanced).

       

       

.. container:: section
   :name: viewlet-below-content-body
