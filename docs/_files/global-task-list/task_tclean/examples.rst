Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container::
         :name: parent-fieldname-text

         The following examples, to be expanded, highlight modes and
         options that the tclean task supports.
         The examples below are written as scripts that may be copied
         and pasted to get started with the basic parameters needed for
         a particular operation. When writing scripts, it is advised
         that the interactive task interface be used to view lists of
         sub-parameters that are relevant only to the operations being
         performed. For example, setting specmode='cube' and running
         inp() will list parameters that are relevant to spectral
         coordinate definition, or setting niter to a number greater
         than zero (niter=100) followed by inp() will list iteration
         control parameters.
         Note that all runs of tclean need the following parameters:
         vis, imagename, imsize, and cell.
         By default, tclean will run with niter=0, making the PSF, a
         primary beam, the initial dirty (or residual) image and a
         restored version of the image.

      .. container::

          

      .. container::

         For examples running tclean on ALMA data, see also the CASA
         Guide `"Tclean and
         ALMA" <https://casaguides.nrao.edu/index.php?title=TCLEAN_and_ALMA>`__.

      .. rubric:: 
         Imaging and Deconvolution Iterations
         :name: imaging-and-deconvolution-iterations

       

      .. rubric:: Using Hogbom CLEAN on a single MFS image
         :name: using-hogbom-clean-on-a-single-mfs-image

      .. container::

         .. container:: casa-input-box

            | tclean(vis='test.ms', imagename='try1', imsize=100,
              cell='10.0arcsec', specmode='mfs',
            |        deconvolver='hogbom', gridder='standard',
              weighting='natural', niter=100 )

      .. rubric:: Using Multi-scale CLEAN on a Cube Mosaic image
         :name: using-multi-scale-clean-on-a-cube-mosaic-image

      .. container::

          

         .. container:: casa-input-box

            .. container::

               tclean(vis='test.ms', imagename='try1', imsize=100,
               cell='10.0arcsec',specmode='cube',

            .. container::

                      nchan=10, start='1.0GHz', width='10MHz',
                      deconvolver='multiscale', scales=[0,3,10,30],
                      gridder='mosaic', pblimit=0.1,
                      weighting='natural', niter=100 )

      .. rubric:: 
         Using W-Projection with Multi-Term MFS wideband imaging
         :name: using-w-projection-with-multi-term-mfs-wideband-imaging

      .. container::

         .. container:: casa-input-box

            | tclean(vis='test.ms', imagename='try1', imsize=100,
              cell='10.0arcsec',
            |        deconvolver='mtmfs', reffreq='1.5GHz', nterms=2,
            |        gridder='wproject', wprojplanes=64,
            |        weighting='natural', niter=100 )

      .. rubric:: 
         Using automasking with any type of image
         :name: using-automasking-with-any-type-of-image

      .. container::

         .. container:: casa-input-box

            tclean(vis='test.ms', imagename='try1', niter=100, ....,
            usemask='auto-multithresh')

      .. container::

         See the `Masks for
         Deconvolution <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__
         section of CASAdocs for more information about the
         auto-multithresh algorithm.

      .. container::

          

      .. rubric:: Scripting using PySynthesisImager
         :name: scripting-using-pysynthesisimager

      .. container::

         PySynthesisImager (LINK) is a python application built on top
         of the synthesis tools (LINK). The operations of the tclean
         task can be replicated using the following python script.
         Subsets of the script can thus be chosen, and extra external
         methods can be inserted in between as desired.  After each
         stage, images are saved on disk. Therefore, any modifications
         done to the images in between steps will be honored. 

      .. container::

          

      .. container::

         .. container:: casa-input-box

            | ## (1) Import the python application layer
            | from imagerhelpers.imager_base import PySynthesisImager
            | from imagerhelpers.input_parameters import
              ImagerParameters
            | ## (2) Set up Input Parameters
            | ## - List all parameters that you need here
            | ## - Defaults will be assumed for unspecified parameters
            | ## - Nearly all parameters are identical to that in the
              task. Please look at the
            | ## list of parameters under \__init_\_ using " help
              ImagerParameters " )
            | paramList = ImagerParameters(
            | msname ='DataTest/point.ms',
            | field='',
            | spw='',
            | imagename='try2',
            | imsize=100,
            | cell='10.0arcsec',
            | specmode='mfs',
            | gridder='standard',
            | weighting='briggs',
            | niter=100,
            | deconvolver='hogbom'
            | )
            | ## (3) Construct the PySynthesisImager object, with all
              input parameters
            | imager = PySynthesisImager(params=paramList)
            | ## (4) Initialize various modules.
            | ## - Pick only the modules you will need later on. For
              example, to only make
            | ## the PSF, there is no need for the deconvolver or
              iteration control modules.
            | ## Initialize modules major cycle modules
            | imager.initializeImagers()
            | imager.initializeNormalizers()
            | imager.setWeighting()
            | ## Init minor cycle modules
            | imager.initializeDeconvolvers()
            | imager.initializeIterationControl()
            | ## (5) Make the initial images
            | imager.makePSF()
            | imager.makePB()
            | imager.runMajorCycle() # Make initial dirty / residual
              image
            | ## (6) Make the initial clean mask
            | imager.hasConverged()
            | imager.updateMask()
            | ## (7) Run the iteration loops
            | while ( not imager.hasConverged() ):
            |     imager.runMinorCycle()
            |     imager.runMajorCycle()
            |     imager.updateMask()
            | ## (8) Finish up
            | retrec=imager.getSummary();
            | imager.restoreImages()
            | imager.pbcorImages()
            | ## (9) Close tools.
            | imager.deleteTools()

      .. container::

          
         For model prediction (i.e. to only save an input model in
         preparation for self-calibration, for example), use the
         following in step (5). The name of the input model is either
         assumed to be <imagename>.model (or its multi-term equivalent)
         or should be specified via the startmodel parameter in step
         (2).
          

         .. container:: casa-input-box

            imager.predictModel()      # Step (5)

         For major cycle parallelization for continuum imaging
         (specmode='mfs'), replace steps (1) and (3) with the following

      .. container::

          

      .. container::

         .. container:: casa-input-box

            | from imagerhelpers.imager_parallel_continuum import
              PyParallelContSynthesisImager      # Step (1)
            | imager =
              PyParallelContSynthesisImager(params=paramList)                                 
              # Step (3)
            |  

      .. container::

         For parallelization of both the major and minor cycles for Cube
         imaging, replace steps (1) and (3) with the following, and
         include a virtual concanenation call at the end. (However, note
         that for parallel Cube imaging, if you would like to replace
         the minor cycle with your own code (for example), you would
         have to go one layer deeper. For this, please contact our team
         for assistance.)

      .. container::

          

      .. container::

         .. container:: casa-input-box

            | 
            | from imagerhelpers.imager_parallel_cube import
              PyParallelCubeSynthesisImager   # Step (1)
            | imager =
              PyParallelCubeSynthesisImager(params=paramList)                        
              # Step (3)
            | imager.concatImages(type='virtualcopy')                                          
              # Step (8)

       

      .. rubric:: Using tclean with ephemerides tables in CASA format
         :name: using-tclean-with-ephemerides-tables-in-casa-format

      .. container::

          

      .. container::

         When you have an ephermeris table that covers the whole
         observation:

      .. container::

         .. container:: casa-input-box

            tclean(vis=['MS1.ms', 'MS2.ms', 'MS3.ms', 'MS4.ms',
            'MS5.ms'],selectdata=True,field="DES_DEEDEE",spw=['17,19,21,23',
            '17,19,21,23', '17,19,21,23', '17,19,21,23',
            '17,19,21,23'],intent="OBSERVE_TARGET#ON_SOURCE",datacolumn="data",imagename="test_track",imsize=[2000,
            2000],cell=['0.037arcsec'],phasecenter="des_deedee_ephem.tab",stokes="I")

         You can check whether the ephermeris table is of the format
         that CASA accepts by using the measures tool me.framecomet
         function:

      .. container::

          

      .. container::

         .. container:: casa-input-box

            me.framecomet('des_deedee.tab')

         If this tool accepts the input without complaint, then the same
         should work in tclean.
         If the source you are tracking is one of the ten sources for
         which the CASA measures tool has the ephemerides from the JPL
         DE200 or DE405, then you can use their names directly:

      .. container::

          

      .. container::

         .. container:: casa-input-box

            tclean(vis=['uid___A002_Xbc74ea_X175c.ms',
            'uid___A002_Xbc74ea_X1af4.ms',
            'uid___A002_Xbc74ea_X1e19.ms',
            'uid___A002_Xbc74ea_X20b7.ms'],selectdata=True,field="Jupiter",spw=['17,19,21,23',
            '17,19,21,23', '17,19,21,23',
            '17,19,21,23'],intent="OBSERVE_TARGET#ON_SOURCE",datacolumn="corrected",imagename="alltogether",imsize=[700,
            700],cell=['0.16arcsec'],phasecenter="JUPITER",stokes="I")

      .. container::

         For ALMA data mainly the correlator may have the ephemerides of
         a moving source already attached to the FIELD tables of the
         MeasurementSets (as it was used to phase track the source). In
         such special cases, you can use the keyword "TRACKFIELD" in the
         phasecenter parameter, and then the internal ephemerides will
         be used to track the source.

      .. container::

          

      .. container::

         .. container:: casa-input-box

            tclean(vis=['MS1.ms', 'MS2.ms', 'MS3.ms', 'MS4.ms',
            'MS5.ms'],selectdata=True,field="DES_DEEDEE",spw=['17,19,21,23',
            '17,19,21,23', '17,19,21,23', '17,19,21,23',
            '17,19,21,23'],intent="OBSERVE_TARGET#ON_SOURCE",datacolumn="data",imagename="test_track",imsize=[2000,
            2000],cell=['0.037arcsec'],phasecenter="TRACKFIELD",stokes="I")

      .. container::

          

.. container:: section
   :name: viewlet-below-content-body
