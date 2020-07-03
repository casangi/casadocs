.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Developer
=========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   This page gives a brief explanation of the code design.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      This page gives an overview of the code design and future
      development work that needs to be done. Detailed information on
      the algorithm can be found on the chapter page on "`Joint Single
      Dish and Interferometer Image
      Reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction>`__",
      while a description of the **sdintimaging** task and associated
      parameters can be found on the
      `sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging>`__
      task pages.

       

       

      .. rubric:: Code Design
         :name: code-design

       

      The sdintimaging task is implemented using the PySynthesisImager
      module in CASA.

      **Core algorithm implementation**: sdint_imager.py and
      sdint_helper.py

      sdint_imager contains main setup fuctions using PySnthesisImager:
      setup_imager, setup_deconvolver, setup_sdimaging as well as main
      joint imaging alogrithm (do_reconstruct). The sdint_helper
      provides helper functions such as feathering of sd + int, single
      dish residual calculation, primary beam manipulation, checks for
      consistency between SD and INT cube coordinate systems, etc.

      As shown in the diagram at the top of this page, a feathering step
      is inserted in between major and minor cycles to combine SD
      residual and interferometer residual images as well as PSFs before
      deconvolution. Apart from this, standard major/minor cycle
      iterations are performed and most imaging modes of task tclean are
      preserved.  However, only the above documented subset of modes
      have been tested. 

       

       

      .. rubric:: Future work
         :name: future-work

       

      The following is a list of features that are either not available
      yet or untested with the sdintimaging task in CASA 6.1

       

      -  Add the ability to specify only the SD image cube and have the
         interferometer cube coordinate system be generated to match it.
         This is to simplify the interface and not require the user to
         specify interferometer cube settings as well.

         -  Use  sdint_helper:: setup_cube_params() to autogenerate
            nchan/start/width and then remove some parameters from the
            sdintimaging task interface.

      -  Support for parallelization

         -  Enable parallelization of the major and minor cycle via
            PySynthesisImaer after the Cube Refactor work of CAS-9386 is
            complete
         -  Remove the parameter trap in task_sdintimaging, and enable
            functional verification tests for the mpicasa case

      -  Check for validity of the input Single Dish image and PSF cubes
         (some checks already exist regarding coordinate system
         consistency).

         -  If it is not possible to run 'imregrid' provide guidance to
            users on what to do

      -  Make PSFs based on input parameters (already partially
         supported via per-plane restoringbeams)

         -  Allow the user to specify a dish diameter and ask the task
            to generate an Airy Disk SD PSF cube that may be used along
            with the supplied SD image cube. The purpose is to help the
            user in a situation where a SD PSF isn't already available
            or easy to generate.

      -  Connect to tsdimaging internally for ALMA data

         -  Option 1 : A one-step calculation to generate the starting
            SD image and PSF inputs directly from a SD MeasurementSet
            for ALMA.
         -  Option 2 : Implement a 'degrid' equivalent for SD data and
            use sdimaging code within the major/minor cycle loops.

      -  Fully test ‘int-only’ as a  wideband mosaic option.

         -  Test in comparison with gridder='mosaic' and 'awproject'
            with conjbeams=True as offered by tclean.  task_sdintimaging
            implements conjbeams in the image domain. It is expected
            that in situations of widely varying data weights across
            frequency, this version of conjbeams=True will be more
            robust to PSF variation across the face of the mosaic,
            especially for spectral PSFs.  This requires careful testing
            and characterization.

      -  Fix issues in the usage of task_feather

         -  The feather task is used within te major/minor cycle
            iterations.  But, it is incorrect if used as is on a cube
            with per-plane restoring beams. Hence the current code uses
            imsubimage in a loop over channel. This is likely a
            performance bottleneck.  CAS-5883 contains a branch with a
            potential fix to task_feather.
         -  Once task_feather works on cubes with per-plane beams,
            replace the channel loops in task_sdintimaging with single
            task_feather calls.
         -  Understand why the feather step results in NaNs if the
            pblimit is set to a negative value for joint mosaic imaging
            of the INT data.  Check if this is a generic issue (i.e. in
            tclean as well) or just here.   For now, document this.
         -  Feather produces 'imageregrid' warnings for every single
            run, suggesting that the SD cell size and beam size aren't
            compatible, even when they are clearly compatible. 

      -  Manage imageanalysis warning message

         -  Warning from imregrid about being approximate for images
            that are larger than 1 degree on a side.  This needs a
            ticket to change the threshold for this message.

      -  Simplify the output image names

         -  Delete some of the intermediate products and ensure the
            output images follow the standard tclean-like naming scheme

      -  Re-implementation of lower level C++ code will be done only in
         CNGI. i.e. For current CASA, we will continue to use
         PySynthesisImager and Python for cube->mfs conversions.

.. container:: section
   :name: viewlet-below-content-body
