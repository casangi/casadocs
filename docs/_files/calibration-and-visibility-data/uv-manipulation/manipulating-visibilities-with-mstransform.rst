.. container::
   :name: viewlet-above-content-title

Modify UV-data: mstransform
===========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Regridding visibilities with the task mstransform

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **mstransform** is a multipurpose task that provides all the
      functionality of **split**, **partition**, **cvel**,
      **hanningsmooth**, **uvcontsub** and **applycal** with the
      possibility of applying each of these transformations separately
      or together in an in-memory pipeline, thus avoiding unnecessary
      I/O steps. The list of transformations that **mstransform** can
      apply is as follows:

      1.  Data selection and re-indexing
      2.  Data partitioning (create output Multi-MS)
      3.  On-the-fly calibration (via “Cal Library”)
      4.  Time averaging (weighted and baseline dependent)
      5.  UV continuum subtraction
      6.  Combination of spectral windows
      7.  Channel averaging (weighted)
      8.  Hanning smoothing
      9.  Spectral regridding and reference frame transformation
      10. Separation of spectral windows

      Notice that the order in the above list is not arbitrary. When
      various transformations are applied on the data using
      **mstransform**, the order in which the transformations are piped
      one after the other is the one shown in the above list. These
      operations are described in the sections that follow.

      Besides **mstransform** in itself, there are a series of tasks
      which perform only the individual operations: **split**,
      **hanningsmooth** and **cvel2**. Under the hood these are all
      based on the mstransform framework; they are provided to
      facilitate back compatibility, and for simplicity in cases where
      only the simpler operations are needed.  Notice that as of CASA
      4.6, the **mstransform** based versions of **split** and
      **hanningsmooth** are the default ones, whereas **cvel** still is
      based on the old implementation by default, and the **cvel2**
      interface points to the **mstransform** implementation.

.. container:: section
   :name: viewlet-below-content-body
