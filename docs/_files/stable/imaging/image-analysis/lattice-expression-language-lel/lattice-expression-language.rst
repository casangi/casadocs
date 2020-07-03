.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Lattice Expression Language
===========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Introduction to LEL

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Lattice Expression Language
         :name: lattice-expression-language-1

      .. rubric:: Introduction
         :name: title0

      The Lattice Expression Language (LEL) makes it possible to do
      arithmetic on lattices (in particular on images [which are just
      lattices plus coordinates]). An expression can be seen as a
      lattice (or image) in itself. It can be used in any operation
      where a normal image is used.

      To summarize, the following functionality is supported:

      -  The common mathematical, comparison, and relational
         `operators <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-expressions>`__.
      -  An extensive list of mathematical and logical
         `functions <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-expressions>`__.
      -  Mixed `data
         type <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-expressions>`__
         arithmetic and automatic data type promotion.
      -  Support of image
         `masks <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks>`__.
      -  `Masking <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks>`__
         using boolean expressions.
      -  Handling of
         `masks <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-masks>`__
         in an expression.
      -  Support of image
         `regions <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-regions>`__.
      -  Interface from both Python and C++.

      The first section explains the syntax. The last sections show the
      interface to LEL using Python or C++. At the end some
      `examples <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel/lel-examples>`__
      are given. If you like, you can go straight to the examples and
      hopefully immediately be able to do some basic things.

      LEL operates on lattices, which are a generalization of arrays. As
      said above a particular type of lattice is an image; they will be
      used most often. Because lattices can be very large and usually
      reside on disk, an expression is only evaluated when a chunk of
      its data is requested. This is similar to reading only the
      requested chunk of data from a disk file.

      LEL is quite efficient and can therefore be used well in C++ and
      Python code. Note however, that it can never be as efficient as
      carefully constructed C++ code.

.. container:: section
   :name: viewlet-below-content-body
