.. container::
   :name: viewlet-above-content-title

Developer
=========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task developer

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   --CASA Developer--

   .. container::
      :name: parent-fieldname-text

      task_tclean.py  contains only calls to various steps and the
      controls for different Operating Modes (LINK).  No other logic is
      present in the top level task script.    task_tclean.py uses
      classes defined in refimagerhelper.py ( PySynthesisImager and its
      parallel derivatives ).

       

      Script writers aiming to replicate tclean in an external script
      and be able to insert their own methods or connect their own
      modules, will be able to simply copy and paste the task tclean
      code (the lines containing  " imager.xxxx " )

       

      The tclean task interface is meant to show (and use) subparameters
      only when their parent options are turned on. This way, at any
      given time, the only parameters a user should see via inp() are
      those that are relevant to the current set of algorithm and
      operational choices. 

       

      Additional examples to be added to the Examples tab (from testing
      suite at
      https://svn.cv.nrao.edu/svn/casa/branches/release-4_7/gcwrap/python/scripts/tests/test_refimager.py):

      Examples are meant to have a consistent set of values for vis,
      imagename, imsize,cell, with a limited number of parameters per
      line, to ensure readability. Note that each multiline command has
      to be edited outside of plone and copied in here, such that the
      spacing is preserved and the reader can copy/paste at the casa
      prompt. 

      .. rubric::  
         :name: section

      .. rubric:: Make PSF and PB : 
         :name: make-psf-and-pb

      Make only the PSF, Weight images, and the PB.

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec, niter=0

      .. rubric:: Make a residual/dirty image :
         :name: make-a-residualdirty-image

      example

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Model Prediction :
         :name: model-prediction

      example

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: PB-correction :
         :name: pb-correction

      example

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      | 
      |  

      .. rubric:: Restoration :
         :name: restoration

      examples

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Restarts : 
         :name: restarts

       ( deconv only,  autonaming, etc )

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

       

      .. rubric:: Data Selection : 
         :name: data-selection

      one MS, a list of MSs.

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Single-Field Image Shapes :
         :name: single-field-image-shapes

       Single Field (mfs, cube (basics), phasecenter, stokes planes ? )

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Defining Spectral Coordinate Systems :
         :name: defining-spectral-coordinate-systems

      LINK to Synthesis Imaging / Spectral Line Imaging

      (examples of all the complicated ways you can do this)

       

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      ::

          

      .. rubric:: Examples of Multi-Field Imaging :
         :name: examples-of-multi-field-imaging

      ( 2 single, multiterm, mfs and cube, etc )

       

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      .. rubric::  
         :name: section-1

      .. rubric:: Examples of Iteration Control :
         :name: examples-of-iteration-control

      niter=0,  using cycleniter,  cyclefactor...

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Using a Starting model :
         :name: using-a-starting-model

      single term, multi-term, with restarts, a single-dish model
      (units, etc).

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Saving model visibilities in preparation for
         self-calibration :
         :name: saving-model-visibilities-in-preparation-for-self-calibration

      use savemodel of various types.

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Making masks for deconvolution :
         :name: making-masks-for-deconvolution

      LINK to Synthesis Imaging / Masks For Deconvolution

      making masks....

       

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      ::

          

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      ::

      .. rubric:: Primary Beam correction :
         :name: primary-beam-correction

      LINK to Synthesis Imaging / Primary Beams

      single term, wideband (connect to wb)

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      using vpmanager to set a PB model for tclean

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Returned dictionary :
         :name: returned-dictionary

      example of what is in it...

       

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      ::

      .. rubric:: Examples of Wide-Band Imaging :
         :name: examples-of-wide-band-imaging

      LINK to Synthesis Imaging / Wide Band Imaging

      Choose nterms, ref-freq.  Re-restore outputs. Apply widebandpbcor

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Examples of Mosaicking :
         :name: examples-of-mosaicking

      LINK to Synthesis Imaging / Mosaicking

      Setting up mosaic imaging, setup vpmanager to supply external PB.

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Examples of Wide-field and Full-Beam Imaging
         :name: examples-of-wide-field-and-full-beam-imaging

      facets, wprojection (and wprojplanes),  A-Projection

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

       

      .. rubric:: Parallelization for Continuum/MFS and Cube.
         :name: parallelization-for-continuummfs-and-cube.

      blah...

      example

      .. container:: casa-input-box

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      .. rubric::  
         :name: section-2

      .. rubric:: Channel chunking for very large Spectral Cubes :
         :name: channel-chunking-for-very-large-spectral-cubes

      blah...

      example

      .. container:: casa-input-box

         .. container:: casa-input-box

            This box is intended for CASA Inputs. Insert your text here.

         tclean(vis='test.ms', imagename='try1', imsize=100,
         cell='10.0arcsec',

      .. rubric::  
         :name: section-3

      .. rubric:: Changes to tclean
         :name: changes-to-tclean

      10/19/2019:

      In the MTMFS deconvolver, the expression used to compute D-Chisq
      can be algebraically reduced. This means that the runtime of the
      minor cycle has been improved ror deconvolver=‘MTMFS’,
      particularly for large imsize, niter, and number of scales for
      multi-scale deconvolution. This `technical
      memo <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean/notes_speedup_tests.pdf>`__
      briefly describes the algorithmic changes and provides examples of
      the speed-up in runtime.

       

      .. container:: page

         .. container:: layoutArea

            .. container:: column

                

       

       

.. container:: section
   :name: viewlet-below-content-body
