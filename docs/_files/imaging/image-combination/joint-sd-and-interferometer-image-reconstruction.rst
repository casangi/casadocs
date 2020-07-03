.. container::
   :name: viewlet-above-content-title

Joint Single Dish and Interferometer Image Reconstruction
=========================================================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   This is a description of the joint single dish and interferometer
   image reconstruction algorithm within CASA 5.7/6.1.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Joint reconstruction of wideband single dish and
         interferometer data in CASA
         is\ `experimental <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/tasks-and-tools>`__\ .
         Please use at own discretion.
         :name: joint-reconstruction-of-wideband-single-dish-and-interferometer-data-in-casa-is-experimental.-please-use-at-own-discretion.

      The scope of parameters that has been tested for CASA 5.7/6.1 can
      be found below.

       

      .. rubric:: Overview
         :name: overview

      The SDINT imaging algorithm allows joint reconstruction of
      wideband single dish and interferometer data. This algorithm is
      available in the
      task\ `sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging>`__
      and described in `Rau, Naik & Braun
      (2019) <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta>`__.

       

      .. rubric:: Algorithm
         :name: algorithm

       

      Interferometer data are gridded into an image cube (and
      corresponding PSF). The single dish image and PSF cubes are
      combined with the interferometer cubes in a feathering step. The
      joint image and PSF cubes then form inputs to any deconvolution
      algorithm (in either cube or mfs/mtmfs modes). Model images from
      the deconvolution algorithm are translated back to model image
      cubes prior to subtraction from both the single dish image cube as
      well as the interferometer data to form a new pair of residual
      image cubes to be feathered in the next iteration. In the case of
      mosaic imaging, primary beam corrections are performed per channel
      of the image cube, followed by a multiplication by a common
      primary beam, prior to deconvolution. Therefore, for mosaic
      imaging, this task always implements conjbeams=True and
      normtype=’flatnoise’.

       

       

      |image1|

       

       

       

      The input single dish data are the single dish image and psf
      cubes. The input interferometer data is a MeasurementSet. In
      addition to imaging and deconvolution parameters from
      interferometric imaging (task tclean), there are controls for a
      feathering step to combine interferometer and single dish cubes
      within the imaging iterations. Note that the above diagram shows
      only the 'mtmfs' variant. Cube deconvolution proceeds directly
      with the cubes in the green box above, without the extra
      conversion back and forth to the multi-term basis. Primary beam
      handling is also not shown in this diagram, but full details (via
      pseudocode) are available in the \ `reference
      publication. <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7>`__\ 

      The parameters used for controlling the joint deconvolution are
      described on
      the\ `sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging>`__\ task
      pages.

       

      .. rubric:: Task Specification : sdintimaging
         :name: task-specification-sdintimaging

       

      The task
      `sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging>`__
      contains the algorithm for joint reconstruction of wideband single
      dish and interferometer data. The sdintimaging task shares a
      significant number of parameters with the tclean task, but also
      contains unique parameters. A detailed overview of these
      parameters, and how to use them, can be found in the CASA
      Docs\ `task pages of
      sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging>`__\ .

       

      .. rubric:: Usage Modes
         :name: usage-modes

      As seen from the diagram above and described on
      the\ `sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging>`__\ task
      pages, there is considerable flexibility in usage modes. One can
      choose between interferometer-only, singledish-only and joint
      interferometer-singledish imaging. Outputs are restored images and
      associated data products (similar to task tclean).

      The following usage modes will be released in the (experimental)
      sdintimaging task for CASA 6.1/5.7 . Modes being tested are all 12
      combinations of :

      -  Cube Imaging :  All 6 combinations of the following options.

         -  *specmode = 'cube' *
         -  *deconvolver = 'multiscale', 'hogbom'
            *
         -  *usedata = 'sdint', 'sd' , 'int'   *
         -  *gridder = 'standard', 'mosaic'   *
         -  *parallel = False*

      -  Wideband Multi-Term Imaging :  All 6 combinations of the
         following options.

         -  *specmode = 'mfs' *
         -  deconvolver = 'mtmfs'  ( nterms=1  for a single-term MFS
            image, and nterms>1 for multi-term MFS image. Tests use
            nterms=2 )
         -  *usedata = 'sdint', 'sd' , 'int'*
         -  *gridder = 'standard', 'mosaic' *
         -  *parallel = False*

      .. container:: info-box

         NOTE: When the INT and/or SD cubes have flagged (and therefore
         empty) channels, only those channels that have non-zero images
         in both the INT and SD cubes are used for the joint
         reconstruction.

      .. container:: info-box

         NOTE: Single-plane joint imaging may be run with
         deconvolver='mtmfs' and nterms=1.

      .. container:: info-box

         NOTE: All other modes allowed by the new sdintimaging task are
         untested as of CASA 6.1. Tests will be added in subsequent
         releases. Please see the Future Work section at the bottom of
         this page.

       

       

      .. rubric:: Test Results
         :name: test-results

       

      The sdintimaging task was run on a pair of simulated test
      datasets. Both contain a flat spectrum extended emission feature
      plus three point sources, two of which have spectral index=-1.0
      and one which is flat-spectrum (rightmost point). The scale of the
      top half of the extended structure was chosen to lie within the
      central hole in the spatial-frequency plane at the middle
      frequency of the band so as to generate a situation where the
      interferometer-only imaging is difficult.

      Please refer to the
      `publication <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta>`__
      for a more detailed analysis of the imaging quality and
      comparisons of images without and with SD data. 

      Images from a run on the ALMA M100 12m+7m+TP Science Verification
      Data suite are also shown below.

      .. rubric::  
         :name: section

      .. rubric:: Single Pointing Simulation :
         :name: single-pointing-simulation

      Wideband Multi-Term Imaging ( deconvolver='mtmfs', specmode='mfs'
      )

      +-----------------------------------+-----------------------------------+
      | SD + INT                          | |image2|                          |
      |  A joint reconstruction           |                                   |
      | accurately reconstructs both      |                                   |
      | intensity and spectral index for  |                                   |
      | the extended emission as well as  |                                   |
      | the compact sources.              |                                   |
      +-----------------------------------+-----------------------------------+
      | INT-only                          | |image3|                          |
      |                                   |                                   |
      | The intensity has negative bowls  |                                   |
      | and the spectral index is overly  |                                   |
      | steep, especially for the top     |                                   |
      | half of the extended component.   |                                   |
      +-----------------------------------+-----------------------------------+
      | SD-only                           | |image4|                          |
      |                                   |                                   |
      | The spectral index of the         |                                   |
      | extended emission is accurate (at |                                   |
      | 0.0) and the point sources are    |                                   |
      | barely visible at this SD angular |                                   |
      | resolution.                       |                                   |
      +-----------------------------------+-----------------------------------+

       

      Cube Imaging ( deconvolver='multiscale', specmode='cube' )

      +-----------------------------------+-----------------------------------+
      | SD + INT                          | |image5|                          |
      |  A joint reconstruction has lower |                                   |
      | artifacts and more accurate       |                                   |
      | intensities in all three          |                                   |
      | channels, compared to the         |                                   |
      | int-only reconstructions below    |                                   |
      +-----------------------------------+-----------------------------------+
      | INT-only                          | |image6|                          |
      |                                   |                                   |
      | The intensity has negative bowls  |                                   |
      | in the lower frequency channels   |                                   |
      | and the extended emission is      |                                   |
      | largely absent at the higher      |                                   |
      | frequencies.                      |                                   |
      +-----------------------------------+-----------------------------------+
      | SD-only                           | |image7|                          |
      |                                   |                                   |
      | A demonstration of single-dish    |                                   |
      | cube imaging with deconvolution   |                                   |
      | of the SD-PSF.                    |                                   |
      |                                   |                                   |
      | In this example, iterations have  |                                   |
      | not been run until full           |                                   |
      | convergence, which is why the     |                                   |
      | sources still contain signatures  |                                   |
      | of the PSF.                       |                                   |
      +-----------------------------------+-----------------------------------+

       

       

      .. rubric:: Mosaic Simulation
         :name: mosaic-simulation

       

      An observation of the same sky brightness was simulated with 25
      pointings.

       

      Wideband Multi-Term Mosaic Imaging ( deconvolver='mtmfs',
      specmode='mfs' , gridder='mosaic' )

      +-----------------------------------+-----------------------------------+
      | SD + INT                          | |image8|                          |
      |  A joint reconstruction           |                                   |
      | accurately reconstructs both      |                                   |
      | intensity and spectral index for  |                                   |
      | the extended emission as well as  |                                   |
      | the compact sources.              |                                   |
      |                                   |                                   |
      | This is a demonstration of joint  |                                   |
      | mosaicing along with wideband     |                                   |
      | single-dish and interferometer    |                                   |
      | combination.                      |                                   |
      +-----------------------------------+-----------------------------------+
      | INT-only                          | |image9|                          |
      |                                   |                                   |
      | The intensity has negative bowls  |                                   |
      | and the spectral index is         |                                   |
      | strongly inaccurate.   Note that  |                                   |
      | the errors are slightly less than |                                   |
      | the situation with the            |                                   |
      | single-pointing example (where    |                                   |
      | there was only one pointing's     |                                   |
      | worth of uv-coverage).            |                                   |
      +-----------------------------------+-----------------------------------+

       

      Cube Mosaic Imaging ( *deconvolver='multiscale', specmode='cube' ,
      gridder='mosaic'* )

      +-----------------------------------+-----------------------------------+
      | SD + INT                          | |image10|                         |
      |  A joint reconstruction produces  |                                   |
      | better per-channel                |                                   |
      | reconstructions compared to the   |                                   |
      | INT-only situation shown below.   |                                   |
      |                                   |                                   |
      | This is a demonstration of cube   |                                   |
      | mosaic imaging along with SD+INT  |                                   |
      | joint reconstruction.             |                                   |
      +-----------------------------------+-----------------------------------+
      | INT-only                          | |image11|                         |
      |                                   |                                   |
      | Cube mosaic imaging with only     |                                   |
      | interferometer data. This clearly |                                   |
      | shows negative bowls and          |                                   |
      | artifacts arising from the        |                                   |
      | missing flux.                     |                                   |
      +-----------------------------------+-----------------------------------+

       

       

      .. rubric:: Other Tests :  ALMA M100  Spectral Cube Imaging : 12m
         + 7m + TP
         :name: other-tests-alma-m100-spectral-cube-imaging-12m-7m-tp

       

      The sdintimaging task was run on the `ALMA M100 Science
      Verification
      Datasets <https://almascience.nrao.edu/alma-data/science-verification>`__.

      (1) The single dish (TP) cube was pre-processed by adding
      per-plane restoringbeam information.

      (2) Cube specification parameters were obtained from the SD Image
      as follows

         from sdint_helper import \*
         sdintlib = SDINT_helper()
         sdintlib.setup_cube_params(sdcube='M100_TmP')

      ..

         Output : Shape of SD cube : [90 90  1 70]
         Coordinate ordering : ['Direction', 'Direction', 'Stokes',
         'Spectral']
         nchan = 70
         start = 114732899312.0Hz
         width = -1922516.74324Hz
         Found 70 per-plane restoring beams#
         (For specmode='mfs' in sdintimaging, please remember to set
         'reffreq' to a value within the freq range of the cube.)
         Returned Dict : {'nchan': 70, 'start': '114732899312.0Hz',
         'width': '-1922516.74324Hz'}

       

      (3) Task sdintimaging was run with automatic SD-PSF generation,
      n-sigma stopping thresholds, a pb-based mask at the 0.3 gain
      level, and no other deconvolution masks (interactive=False).

         sdintimaging(usedata="sdint", sdimage="../M100_TP",
         sdpsf="",sdgain=3.0, dishdia=12.0, vis="../M100_12m_7m",
         imagename="try_sdint_niter5k", imsize=1000, cell="0.5arcsec",
         phasecenter="J2000 12h22m54.936s +15d48m51.848s", stokes="I",
         specmode="cube", reffreq="", nchan=70,
         start="114732899312.0Hz", width="-1922516.74324Hz",
         outframe="LSRK", veltype="radio", restfreq="115.271201800GHz",
         interpolation="linear", chanchunks=1,
         perchanweightdensity=True, gridder="mosaic", mosweight=True,
         pblimit=0.2, deconvolver="multiscale", scales=[0, 5, 10, 15,
         20], smallscalebias=0.0, pbcor=False, weighting="briggs",
         robust=0.5, niter=5000, gain=0.1, threshold=0.0, nsigma=3.0,
         interactive=False, usemask="user", mask="", pbmask=0.3)

       

      **Results from two channels are show below. **

      LEFT : INT only (12m+7m)    and  RIGHT : SD+INT (12m + 7m + TP)

       

      Channel 23

      |image12|

      Channel 43

       

      |image13|

       

      Moment 0 Maps :   LEFT :  INT only.        MIDDLE :   SD + INT
      with sdgain=1.0          RIGHT : SD + INT with sdgain=3.0

       

      |image14|

       

      Moment 1 Maps :   LEFT :  INT only.        MIDDLE :   SD + INT
      with sdgain=1.0          RIGHT : SD + INT with sdgain=3.0

      |image15|

       

      A comparison (shown for one channel) with and without masking is
      shown below.

      |image16|

       

      Notes : 

      -  In the reconstructed cubes, negative bowls have clearly been
         eliminated by using sdintimaging to combine interferometry + SD
         data.  Residual images are close to noise-like too (not
         pictured above) suggesting a well-constrained and steadily
         converging imaging run.  

      -  The source structure is visibly different from the INT-only
         case, with high and low resolution structure appearing more
         well defined.  However, the *high-resolution* peak flux in the
         SDINT image cube is almost a factor of 3 lower than the
         INT-only. While this may simply be because of deconvolution
         uncertainty in the ill-constrained INT-only reconstruction, it
         requires more investigation to evaluate absolute flux
         correctness.  For example, it will be useful to evaluate if the
         INT-only reconstructed flux changes significantly with careful
         hand-masking.

         -  Compare with a Feathered image :
            http://www.astroexplorer.org/details/apjaa60c2f1   : The
            reconstructed structure is consistent.

      -  The middle and right panels compare reconstructions with
         different values of sdgain (1.0 and 3.0).   The sdgain=3.0 run
         has a noticeable emphasis on the SD flux in the reconstructed
         moment maps, while the high resolution structures have the same
         are the same between sdgain=1 and 3.  This is consistent with
         expectations from the algorithm, but requires further
         investigation to evaluate robustness in general.

      -  Except for the last panel, no deconvolution masks were used
         (apart from a *pbmask* at the 0.3 gain level). The
         deconvolution quality even without masking is consistent with
         the expectation that when supplied with better data constraints
         in a joint reconstruction, the native algorithms are capable of
         converging on their own. In this example (same *niter* and
         *sdgain*), iterative cleaning with interactive and auto-masks
         (based mostly on interferometric peaks in the images) resulted
         in more artifacts compared to a run that allowed multi-scale
         clean to proceed on its own.

      -  The results using sdintimaging on these ALMA data can be
         compared with performance results when\ `using
         feather <https://casaguides.nrao.edu/index.php?title=M100_Band3_Combine_5.4>`__\ ,
         and when\ `using
         tp2vis <https://science.nrao.edu/facilities/alma/alma-develop-old-022217/tp2vis_final_report.pdf>`__\ (ALMA
         study by J. Koda and P. Teuben).

       

       

       

      The following is a list of use cases that have simulation-based
      functional verification tests within CASA.

      +-----------------------+-----------------------+-----------------------+
      | 1                     | Wideband mulit-term   | Wideband data single  |
      |                       | imaging (SD+Int)      | field imaging by      |
      |                       |                       | joint-reconstruction  |
      |                       |                       | from single dish and  |
      |                       |                       | interferometric data  |
      |                       |                       | to obtain the high    |
      |                       |                       | resolution of the     |
      |                       |                       | interferometer while  |
      |                       |                       | account for the zero  |
      |                       |                       | spacing information.  |
      |                       |                       | Use multi-term        |
      |                       |                       | multi-frequency       |
      |                       |                       | synthesis (MTMFS)     |
      |                       |                       | algorithm to properly |
      |                       |                       | account for spectral  |
      |                       |                       | information of the    |
      |                       |                       | source.               |
      +-----------------------+-----------------------+-----------------------+
      | 2                     | Wideband multi-term   | The same as #1 except |
      |                       | imaging: Int only     | for using             |
      |                       |                       | interferometric data  |
      |                       |                       | only, which is useful |
      |                       |                       | to make a comparison  |
      |                       |                       | with #1 (i.e. effect  |
      |                       |                       | of missing flux).     |
      |                       |                       | This is equivalent to |
      |                       |                       | running 'mtmfs' with  |
      |                       |                       | specmode='mfs' and    |
      |                       |                       | gridder='standard' in |
      |                       |                       | tclean                |
      +-----------------------+-----------------------+-----------------------+
      | 3                     | Wideband multi-term   | The same as #1 expect |
      |                       | imaging: SD only      | for using single dish |
      |                       |                       | data only which is    |
      |                       |                       | useful to make a      |
      |                       |                       | comparison with #1    |
      |                       |                       | (i.e. to see how much |
      |                       |                       | high resolution       |
      |                       |                       | information is        |
      |                       |                       | missing).  Also,      |
      |                       |                       | sometimes, the SD PSF |
      |                       |                       | has significant       |
      |                       |                       | sidelobes (Airy disk) |
      |                       |                       | and even single dish  |
      |                       |                       | images can benefit    |
      |                       |                       | from deconvolution.   |
      |                       |                       | This is a use case    |
      |                       |                       | where wideband        |
      |                       |                       | multi-term imaging is |
      |                       |                       | applied to SD data    |
      |                       |                       | alone to make images  |
      |                       |                       | at the highest        |
      |                       |                       | possible resolution   |
      |                       |                       | as well as to derive  |
      |                       |                       | spectral index        |
      |                       |                       | information.          |
      +-----------------------+-----------------------+-----------------------+
      | 4                     | Single field cube     | Spectral cube single  |
      |                       | imaging: SD+Int       | field imaging by      |
      |                       |                       | joint reconstruction  |
      |                       |                       | of single dish and    |
      |                       |                       | interferometric data  |
      |                       |                       | to obtain single      |
      |                       |                       | field spectral cube   |
      |                       |                       | image.                |
      |                       |                       |                       |
      |                       |                       | Use multi-scale clean |
      |                       |                       | for deconvolution     |
      +-----------------------+-----------------------+-----------------------+
      | 5                     | Single field cube     | The same as #4 except |
      |                       | imaging: Int only     | for using the         |
      |                       |                       | interferometric data  |
      |                       |                       | only, which is        |
      |                       |                       | useful to make a      |
      |                       |                       | comparison with #4    |
      |                       |                       | (i.e. effect of       |
      |                       |                       | missing flux). This   |
      |                       |                       | is equivalent to      |
      |                       |                       | running 'multiscale'  |
      |                       |                       | with specmode='cube'  |
      |                       |                       | and                   |
      |                       |                       | gridder='standard' in |
      |                       |                       | tclean.               |
      +-----------------------+-----------------------+-----------------------+
      | 6                     | Single field cube     | The same as #4 except |
      |                       | imaging: SD only      | for using the single  |
      |                       |                       | dish data only, which |
      |                       |                       | is useful to make a   |
      |                       |                       | comparison with #4    |
      |                       |                       |                       |
      |                       |                       | (i.e. to see how much |
      |                       |                       | high resolution       |
      |                       |                       | information is        |
      |                       |                       | missing)              |
      |                       |                       |                       |
      |                       |                       | Also, it addresses    |
      |                       |                       | the use case where SD |
      |                       |                       | PSF sidelobes are     |
      |                       |                       | significant and where |
      |                       |                       | the SD images could   |
      |                       |                       | benefit from          |
      |                       |                       | multiscale (or point  |
      |                       |                       | source) deconvolution |
      |                       |                       | per channel.          |
      +-----------------------+-----------------------+-----------------------+
      | 7                     | Wideband multi-term   | Wideband data mosaic  |
      |                       | mosaic Imaging:       | imaging by            |
      |                       | SD+Int                | joint-reconstruction  |
      |                       |                       | from single dish and  |
      |                       |                       | interferometric data  |
      |                       |                       | to obtain the high    |
      |                       |                       | resolution of the     |
      |                       |                       | interferometer while  |
      |                       |                       | account for the zero  |
      |                       |                       | spacing information.  |
      |                       |                       |                       |
      |                       |                       | Use multi-term        |
      |                       |                       | multi-frequency       |
      |                       |                       | synthesis (MTMFS)     |
      |                       |                       | algorithm to properly |
      |                       |                       | account for spectral  |
      |                       |                       | information of the    |
      |                       |                       | source. Implement the |
      |                       |                       | concept of conjbeams  |
      |                       |                       | (i.e. frequency       |
      |                       |                       | dependent primary     |
      |                       |                       | beam correction) for  |
      |                       |                       | wideband mosaicing.   |
      +-----------------------+-----------------------+-----------------------+
      | 8                     | Wideband multi-term   | The same as #7 except |
      |                       | mosaic imaging: Int   | for using             |
      |                       | only                  | interferometric data  |
      |                       |                       | only, which is useful |
      |                       |                       | to make a comparison  |
      |                       |                       | with #7 (i.e. effect  |
      |                       |                       | of missing flux).     |
      |                       |                       | Also, this is an      |
      |                       |                       | alternate             |
      |                       |                       | implementation of the |
      |                       |                       | concept of conjbeams  |
      |                       |                       | ( frequency dependent |
      |                       |                       | primary beam          |
      |                       |                       | correction) available |
      |                       |                       | via tclean, and which |
      |                       |                       | is likely to be more  |
      |                       |                       | robust to uv-coverage |
      |                       |                       | variations  (and      |
      |                       |                       | sumwt) across         |
      |                       |                       | frequency.            |
      +-----------------------+-----------------------+-----------------------+
      | 9                     | Wideband multi-term   | The same as #7 expect |
      |                       | mosaic imaging: SD    | for using single dish |
      |                       | only                  | data only which is    |
      |                       |                       | useful to make a      |
      |                       |                       | comparison with #7    |
      |                       |                       | (i.e. to see how much |
      |                       |                       | high resolution       |
      |                       |                       | information is        |
      |                       |                       | missing).  This is    |
      |                       |                       | the same situation as |
      |                       |                       | (3) , but made on an  |
      |                       |                       | image coordinate      |
      |                       |                       | system that matches   |
      |                       |                       | an interferometer     |
      |                       |                       | mosaic mtmfs image.   |
      +-----------------------+-----------------------+-----------------------+
      | 10                    | Cube mosaic imaging:  | Spectral cube mosaic  |
      |                       | SD+Int                | imaging by joint      |
      |                       |                       | reconstruction of     |
      |                       |                       | single dish and       |
      |                       |                       | interferometric data. |
      |                       |                       |                       |
      |                       |                       | Use multi-scale clean |
      |                       |                       | for deconvolution.    |
      +-----------------------+-----------------------+-----------------------+
      | 11                    | Cube mosaic imaging:  | The same as #10       |
      |                       | Int only              | except for using the  |
      |                       |                       | intererometric data   |
      |                       |                       | only, which is useful |
      |                       |                       | to make a comparison  |
      |                       |                       | with #10 (i.e. effect |
      |                       |                       | of missing flux).     |
      |                       |                       | This is the same use  |
      |                       |                       | case as               |
      |                       |                       | gridder='mosaic' and  |
      |                       |                       | dec                   |
      |                       |                       | onvolver='multiscale' |
      |                       |                       | in tclean for         |
      |                       |                       | specmode='cube'.      |
      +-----------------------+-----------------------+-----------------------+
      | 12                    | Cube mosaic imaging:  | The same as #10       |
      |                       | SD only               | except for using the  |
      |                       |                       | single dish data      |
      |                       |                       | only, which is useful |
      |                       |                       | to make a comparison  |
      |                       |                       | with #10 (i.e. to see |
      |                       |                       | how much high         |
      |                       |                       | resolution            |
      |                       |                       | information is        |
      |                       |                       | missing).  This is    |
      |                       |                       | the same situation as |
      |                       |                       | (6), but made on an   |
      |                       |                       | image coordinate      |
      |                       |                       | system that matches   |
      |                       |                       | an interferometer     |
      |                       |                       | mosaic cube image.    |
      +-----------------------+-----------------------+-----------------------+
      | 13                    | Wideband MTMFS SD+INT | The same as #1, but   |
      |                       | with channel 2        | with partially        |
      |                       | flagged in INT        | flagged data in the   |
      |                       |                       | cubes. This is a      |
      |                       |                       | practical reality     |
      |                       |                       | with real data where  |
      |                       |                       | the INT and SD data   |
      |                       |                       | are likely to have    |
      |                       |                       | gaps in the data due  |
      |                       |                       | to radio frequency    |
      |                       |                       | interferenece or      |
      |                       |                       | other weight          |
      |                       |                       | variations.           |
      +-----------------------+-----------------------+-----------------------+
      |  14                   | Cube SD+INT with      | The same as #4, but   |
      |                       | channel 2 flagged     | with partially        |
      |                       |                       | flagged data in the   |
      |                       |                       | cubes. This is a      |
      |                       |                       | practical reality     |
      |                       |                       | with real data where  |
      |                       |                       | the INT and SD data   |
      |                       |                       | are likely to have    |
      |                       |                       | gaps in the data due  |
      |                       |                       | to radio frequency    |
      |                       |                       | interferenece or      |
      |                       |                       | other weight          |
      |                       |                       | variations.           |
      +-----------------------+-----------------------+-----------------------+
      | 15                    | Wideband MTMFS SD+INT | The same as #1, but   |
      |                       | with sdpsf=""         | with an unspecified   |
      |                       |                       | sdpsf. This triggers  |
      |                       |                       | the auto-calculation  |
      |                       |                       | of the SD PSF cube    |
      |                       |                       | using restoring beam  |
      |                       |                       | information from the  |
      |                       |                       | regridded input       |
      |                       |                       | sdimage.              |
      +-----------------------+-----------------------+-----------------------+

      .. rubric::  
         :name: section-1

      .. rubric:: Future work
         :name: future-work

       

      For future work and a summary of the Code Design, please see the
      `"Developer" <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging/developer>`__
      tab
      ofthe\ `sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging>`__\ \ task.

      |  
      |  

      .. rubric:: References
         :name: references

      Urvashi Rau, Nikhil Naik, and Timothy Braun 2019\ \ `AJ 158,
      1 <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta>`__\ \ .\ 

      https://github.com/urvashirau/WidebandSDINT

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig_algo.png/@@images/38b5adb2-5073-44d7-b7a8-681061cbe225.png
   :class: image-inline
   :width: 599px
   :height: 329px
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_standard_mfs_mtmfs_sdint.png/@@images/bbd9a1df-8307-451e-860f-1a4905a57e0c.png
   :class: image-inline
   :width: 416px
   :height: 160px
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_standard_mfs_mtmfs_int.png/@@images/62cc52d7-e720-45e4-ae6d-8f782189d7e0.png
   :class: image-inline
   :width: 417px
   :height: 160px
.. |image4| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_standard_mfs_mtmfs_sd.png/@@images/1ad3d419-8fd9-40e7-a348-9f6b1b2df8c6.png
   :class: image-inline
   :width: 414px
   :height: 159px
.. |image5| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_standard_cube_multiscale_sdint.png/@@images/246193bd-a11e-4179-88be-ce86edc778ea.png
   :class: image-inline
   :width: 614px
   :height: 236px
.. |image6| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_standard_cube_multiscale_int.png/@@images/3d45174e-67f7-4159-ad72-be67ff3c396e.png
   :class: image-inline
   :width: 596px
   :height: 229px
.. |image7| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_standard_cube_multiscale_sd.png/@@images/bc98e892-dca1-4e0a-892f-e5a22e2dd2a6.png
   :class: image-inline
   :width: 591px
   :height: 227px
.. |image8| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_mosaic_mfs_mtmfs_sdint.png/@@images/ae742ca7-bf5c-43b4-bf30-28c26bd51b50.png
   :class: image-inline
   :width: 518px
   :height: 199px
.. |image9| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_mosaic_mfs_mtmfs_int.png/@@images/c583bb0c-0fb1-495d-bc9c-a281bf72789a.png
   :class: image-inline
   :width: 518px
   :height: 199px
.. |image10| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_mosaic_cube_multiscale_sdint.png/@@images/f49f24e8-c3df-4a48-8290-c8d9ad620010.png
   :class: image-inline
   :width: 631px
   :height: 242px
.. |image11| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/fig-try_mosaic_cube_multiscale_int.png/@@images/cead63c1-af84-47b4-b7f2-91f8368b3e9c.png
   :class: image-inline
   :width: 640px
   :height: 246px
.. |image12| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/pic_compare_5k_chan23.png/@@images/6f0d5d45-98c8-4ba1-810b-057e0bdf4951.png
   :class: image-inline
   :width: 435px
   :height: 253px
.. |image13| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/pic_compare_5k_chan43.png/@@images/62b8758b-f050-4ede-a34a-5b9271388c43.png
   :class: image-inline
   :width: 428px
   :height: 249px
.. |image14| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/pic_mom0_int_sdgain1_and_3.png/@@images/12ffefb9-346a-4383-9222-99fe3380bb56.png
   :class: image-inline
.. |image15| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/pic_mom1_int_sdgain1_and_3.png/@@images/1d5f83ae-ab42-4d2e-97f0-4c0360248f75.png
   :class: image-inline
.. |image16| image:: https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/pic_compare_3mask_chan43.png/@@images/e1925d56-a88c-445c-8b48-1753e9002ce0.png
   :class: image-inline
