.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Virtual Model Visibilities
==========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Generating and using virtual MODEL_DATA columns in ms.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The tasks that generate model visibilities (**clean**, **tclean**,
      **ft**, and **setjy**) can either (in most cases) save the data in
      a MODEL_DATA column inside of the MeasurementSet (MS) or it can
      save it in a virtual one. In the latter case the model
      visibilities are generated on demand when it is requested and the
      data necessary to generate that is stored (usually the Fourier
      transform of the model images or a component list). More
      detailed descriptions of the structure of an MS can be found on
      the `CASA
      Fundamentals <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals>`__
      pages. 

      The tasks that can read and make use of the virtual model columns
      include calibration tasks, mstransform tasks (including
      **uvsubtraction**), **plotms**.

      Advantages of virtual model column over the real one:

      -  Speed of serving visibilities (in most cases because
         calculating models visibilities is faster than disk IO)
      -  Disk space saving (a full size of the original data size is
         saved)

      When not to use virtual model

      -  model image size is a significant fraction of the visibility
         data size (e.g large cube from a small data set). Virtual model
         column serving might be slower than real one
      -  when the user wants to edit the model physically via the table
         tool for e.g
      -  when using an FTMachine that does not support virtual model
         saving when imaging (AWProjectFT for e.g)

      Additional Information

      -  When both a physical model column exists along with a virtual
         model, then the virtual model is the one that gets served by
         tasks that uses the visbuffer (e.g calibration tasks)
      -  Use **delmod**\ * *\ task to manage your MODEL_DATA column and
         virtual model
      -  If  model data is written for a subset of the MS (say the user
         used *field* , *spw* and/or *intent* selection in **tclean**)
         then the model visibilities will be served properly for the
         subset in question the other part of the MS will have 1 served
         for parallel hand visibilities and 0 for crosshand
         visibilities. So be careful when doing calibration or uvsub
         after writing model visibilities only for a subset of the MS
         (this applies to using the physical scratch column MODEL_DATA
         too)
      -  The virtual model info is written in the SOURCE table of the MS
         usually (and in the main table if the SOURCE table does not
         exist)
      -  FTMachines (or imaging gridding mode) supporting virtual model
         data are:

         -  GridFT: Standard gridder (including mutiterm and multi
            fields or cube),
         -  WProjectFT: widefield wterm  (including mutiterm and multi
            fields or cube),
         -  MosaicFT: mosaic imaging (including mutiterm or cube),
         -  ComponentLists

       

.. container:: section
   :name: viewlet-below-content-body
