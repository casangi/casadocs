#
# stub function definition file for docstring parsing
#

def tclean(vis, selectdata=True, field='', spw='', timerange='', uvrange='', antenna='', scan='', observation='', intent='', datacolumn='corrected', imagename='', imsize=100, cell='"1arcsec"', phasecenter='', stokes='I', projection='SIN', startmodel='', specmode='mfs', reffreq='', nchan=-1, start='', width='', outframe='LSRK', veltype='radio', restfreq=[''], interpolation='linear', perchanweightdensity=True, gridder='standard', facets=1, psfphasecenter='', chanchunks=1, wprojplanes=1, vptable='', mosweight=True, aterm=True, psterm=False, wbawp=True, conjbeams=False, cfcache='', usepointing=False, computepastep=360.0, rotatepastep=360.0, pointingoffsetsigdev=[''], pblimit=0.2, normtype='flatnoise', deconvolver='hogbom', scales=[''], nterms=2, smallscalebias=0.0, restoration=True, restoringbeam='', pbcor=False, outlierfile='', weighting='natural', robust=0.5, noise='1.0Jy', npixels=0, uvtaper=[''], niter=0, gain=0.1, threshold=0.0, nsigma=0.0, cycleniter=-1, cyclefactor=1.0, minpsffraction=0.05, maxpsffraction=0.8, interactive=False, usemask='user', mask='', pbmask=0.0, sidelobethreshold=3.0, noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=0.0, smoothfactor=1.0, minbeamfrac=0.3, cutthreshold=0.01, growiterations=75, dogrowprune=True, minpercentchange=-1.0, verbose=False, fastnoise=True, restart=True, savemodel='none', calcres=True, calcpsf=True, parallel=False):
    r"""
Radio Interferometric Image Reconstruction

Parameters
   - **vis** ({string, stringArray}) - Name of input visibility file(s)
   - **selectdata** (bool=True) - Enable data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - **field** ({string, stringArray}='') - field(s) to select
      - **spw** ({string, stringArray}='') - spw(s)/channels to select
      - **timerange** ({string, stringArray}='') - Range of time to select from data
      - **uvrange** ({string, stringArray}='') - Select data within uvrange
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **scan** ({string, stringArray}='') - Scan number range
      - **observation** ({string, int}='') - Observation ID range
      - **intent** ({string, stringArray}='') - Scan Intent(s)

      .. raw:: html

         </details>
   - **datacolumn** (string='corrected') - Data column to image(data,corrected)
   - **imagename** ({int, string, stringArray}='') - Pre-name of output images
   - **imsize** ({int, intArray}=100) - Number of pixels
   - **cell** ({int, double, intArray, doubleArray, string, stringArray}='"1arcsec"') - Cell size
   - **phasecenter** ({int, string}='') - Phase center of the image
   - **stokes** (string='I') - Stokes Planes to make
   - **projection** (string='SIN') - Coordinate projection 
   - **startmodel** (string='') - Name of starting model image
   - **specmode** (string='mfs') - Spectral definition mode (mfs,cube,cubedata, cubesource)

      .. raw:: html

         <details><summary><i> specmode = mfs </i></summary>

      - **reffreq** (string='') - Reference frequency

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> specmode = cube </i></summary>

      - **nchan** (int=-1) - Number of channels in the output image
      - **start** (string='') - First channel (e.g. start=3,start=\'1.1GHz\',start=\'15343km/s\')
      - **width** (string='') - Channel width (e.g. width=2,width=\'0.1MHz\',width=\'10km/s\')
      - **outframe** (string='LSRK') - Spectral reference frame in which to interpret \'start\' and \'width\'
      - **veltype** (string='radio') - Velocity type (radio, z, ratio, beta, gamma, optical)
      - **restfreq** (stringArray=['']) - List of rest frequencies
      - **interpolation** (string='linear') - Spectral interpolation (nearest,linear,cubic)
      - **chanchunks** (int=1) - Number of channel chunks
      - **perchanweightdensity** (bool=True) - whether to calculate weight density per channel in Briggs style weighting or not

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> specmode = cubesource </i></summary>

      - **nchan** (int=-1) - Number of channels in the output image
      - **start** (string='') - First channel (e.g. start=3,start=\'1.1GHz\',start=\'15343km/s\')
      - **width** (string='') - Channel width (e.g. width=2,width=\'0.1MHz\',width=\'10km/s\')
      - **outframe** (string='LSRK') - Spectral reference frame in which to interpret \'start\' and \'width\'
      - **veltype** (string='radio') - Velocity type (radio, z, ratio, beta, gamma, optical)
      - **restfreq** (stringArray=['']) - List of rest frequencies
      - **interpolation** (string='linear') - Spectral interpolation (nearest,linear,cubic)
      - **chanchunks** (int=1) - Number of channel chunks
      - **perchanweightdensity** (bool=True) - whether to calculate weight density per channel in Briggs style weighting or not

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> specmode = cubedata </i></summary>

      - **nchan** (int=-1) - Number of channels in the output image
      - **start** (string='') - First channel (e.g. start=3,start=\'1.1GHz\',start=\'15343km/s\')
      - **width** (string='') - Channel width (e.g. width=2,width=\'0.1MHz\',width=\'10km/s\')
      - **veltype** (string='radio') - Velocity type (radio, z, ratio, beta, gamma, optical)
      - **restfreq** (stringArray=['']) - List of rest frequencies
      - **interpolation** (string='linear') - Spectral interpolation (nearest,linear,cubic)
      - **chanchunks** (int=1) - Number of channel chunks
      - **perchanweightdensity** (bool=True) - whether to calculate weight density per channel in Briggs style weighting or not

      .. raw:: html

         </details>
   - **gridder** (string='standard') - Gridding options (standard, wproject, widefield, mosaic, awproject)

      .. raw:: html

         <details><summary><i> gridder = standard </i></summary>

      - **vptable** (string='') - Name of Voltage Pattern table
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = widefield </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **facets** (int=1) - Number of facets on a side
      - **vptable** (string='') - Name of Voltage Pattern table
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = wproject </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **vptable** (string='') - Name of Voltage Pattern table
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = wprojectft </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **vptable** (string='') - Name of Voltage Pattern table
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = mosaic </i></summary>

      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky,pbsquare)
      - **vptable** (string='') - Name of Voltage Pattern table
      - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.
      - **mosweight** (bool=True) - Indepently weight each field in a mosaic
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
      - **conjbeams** (bool=False) - Use conjugate frequency for wideband A-terms
      - **psfphasecenter** ({int, string}='') - optional direction to calculate psf for mosaic (default is image phasecenter)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = mosaicft </i></summary>

      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky,pbsquare)
      - **vptable** (string='') - Name of Voltage Pattern table
      - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
      - **conjbeams** (bool=False) - Use conjugate frequency for wideband A-terms
      - **psfphasecenter** ({int, string}='') - optional direction to calculate psf for mosaic (default is image phasecenter)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = ftmosaic </i></summary>

      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky,pbsquare)
      - **vptable** (string='') - Name of Voltage Pattern table
      - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.
      - **mosweight** (bool=True) - Indepently weight each field in a mosaic
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = imagemosaic </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky,pbsquare)
      - **vptable** (string='') - Name of Voltage Pattern table
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = awproject </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky,pbsquare)
      - **psterm** (bool=False) - Use prolate spheroidal during gridding
      - **aterm** (bool=True) - Use aperture illumination functions during gridding
      - **cfcache** (string='') - Convolution function cache directory name
      - **computepastep** (double=360.0) - Parallactic angle interval after the AIFs are recomputed (deg)
      - **rotatepastep** (double=360.0) - Parallactic angle interval after which the nearest AIF is rotated (deg) 
      - **pointingoffsetsigdev** ({intArray, doubleArray}=['']) -  Pointing offset threshold to determine heterogeneity of pointing corrections for the AWProject gridder
      - **wbawp** (bool=True) - Use wideband A-terms
      - **mosweight** (bool=True) - Indepently weight each field in a mosaic
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
      - **conjbeams** (bool=False) - Use conjugate frequency for wideband A-terms
      - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = awprojectft </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky,pbsquare)
      - **psterm** (bool=False) - Use prolate spheroidal during gridding
      - **aterm** (bool=True) - Use aperture illumination functions during gridding
      - **cfcache** (string='') - Convolution function cache directory name
      - **computepastep** (double=360.0) - Parallactic angle interval after the AIFs are recomputed (deg)
      - **rotatepastep** (double=360.0) - Parallactic angle interval after which the nearest AIF is rotated (deg) 
      - **pointingoffsetsigdev** ({intArray, doubleArray}=['']) -  Pointing offset threshold to determine heterogeneity of pointing corrections for the AWProject gridder
      - **wbawp** (bool=True) - Use wideband A-terms
      - **mosweight** (bool=True) - Indepently weight each field in a mosaic
      - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
      - **conjbeams** (bool=False) - Use conjugate frequency for wideband A-terms
      - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.

      .. raw:: html

         </details>
   - **deconvolver** (string='hogbom') - Minor cycle algorithm (hogbom,clark,multiscale,mtmfs,mem,clarkstokes)

      .. raw:: html

         <details><summary><i> deconvolver = multiscale </i></summary>

      - **scales** ({intArray, doubleArray}=['']) - List of scale sizes (in pixels) for multi-scale algorithms
      - **smallscalebias** (double=0.0) - Biases the scale selection when using multi-scale or mtmfs deconvolvers 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> deconvolver = mtmfs </i></summary>

      - **scales** ({intArray, doubleArray}=['']) - List of scale sizes (in pixels) for multi-scale algorithms
      - **nterms** (int=2) - Number of Taylor coefficients in the spectral model
      - **smallscalebias** (double=0.0) - Biases the scale selection when using multi-scale or mtmfs deconvolvers 

      .. raw:: html

         </details>
   - **restoration** (bool=True) - Do restoration steps (or not)

      .. raw:: html

         <details><summary><i> restoration = True </i></summary>

      - **restoringbeam** ({string, stringArray}='') - Restoring beam shape to use. Default is the PSF main lobe
      - **pbcor** (bool=False) - Apply PB correction on the output restored image

      .. raw:: html

         </details>
   - **outlierfile** (string='') - Name of outlier-field image definitions
   - **weighting** (string='natural') - Weighting scheme (natural,uniform,briggs, briggsabs[experimental])

      .. raw:: html

         <details><summary><i> weighting = natural </i></summary>

      - **uvtaper** (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> weighting = briggs </i></summary>

      - **robust** (double=0.5) - Robustness parameter
      - **npixels** (int=0) - Number of pixels to determine uv-cell size 
      - **uvtaper** (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> weighting = briggsabs </i></summary>

      - **robust** (double=0.5) - Robustness parameter
      - **noise** (variant='1.0Jy') - noise parameter for briggs abs mode weighting
      - **npixels** (int=0) - Number of pixels to determine uv-cell size 
      - **uvtaper** (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>
   - **niter** (int=0) - Maximum number of iterations
   - **usemask** (string='user') - Type of mask(s) for deconvolution:  user, pb, or auto-multithresh

      .. raw:: html

         <details><summary><i> usemask = user </i></summary>

      - **mask** ({string, stringArray}='') - Mask (a list of image name(s) or region file(s) or region string(s) )
      - **pbmask** (double=0.0) - primary beam mask

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> usemask = pb </i></summary>

      - **pbmask** (double=0.0) - primary beam mask

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> usemask = auto-multithresh </i></summary>

      - **pbmask** (double=0.0) - primary beam mask
      - **sidelobethreshold** (double=3.0) - sidelobethreshold *  the max sidelobe level * peak residual
      - **noisethreshold** (double=5.0) - noisethreshold * rms in residual image + location(median) 
      - **lownoisethreshold** (double=1.5) - lownoisethreshold * rms in residual image + location(median) 
      - **negativethreshold** (double=0.0) - negativethreshold * rms in residual image + location(median) 
      - **smoothfactor** (double=1.0) - smoothing factor in a unit of the beam
      - **minbeamfrac** (double=0.3) - minimum beam fraction for pruning
      - **cutthreshold** (double=0.01) - threshold to cut the smoothed mask to create a final mask
      - **growiterations** (int=75) - number of binary dilation iterations for growing the mask
      - **dogrowprune** (bool=True) - Do pruning on the grow mask
      - **minpercentchange** (double=-1.0) - minimum percentage change in mask size (per channel plane) to trigger updating of mask by automask 
      - **verbose** (bool=False) - True: print more automasking information in the logger

      .. raw:: html

         </details>
   - **fastnoise** (bool=True) - True: use the faster (old) noise calculation. False: use the new improved noise calculations
   - **restart** (bool=True) - True : Re-use existing images. False : Increment imagename
   - **savemodel** (string='none') - Options to save model visibilities (none, virtual, modelcolumn)
   - **calcres** (bool=True) - Calculate initial residual image
   - **calcpsf** (bool=True) - Calculate PSF
   - **parallel** (bool=False) - Run major cycles in parallel


Description
   .. rubric:: Overview
      

   The **tclean** task forms images from visibilities and
   reconstructs a sky model.

   tclean handles continuum images and spectral line cubes, full
   Stokes polarization imaging, supports outlier fields, contains
   point-source CLEAN
   based `algorithms <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__ as
   well as options for multi-scale and `wideband image
   reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__ ,
   widefield imaging correcting for the w-term, full primary-beam
   imaging and joint mosaic imaging (with heterogeneous array support
   for ALMA). Parallelization of the major cycle is also available.

   The tclean task as based on the `CLEAN
   algorithm <https://www.cv.nrao.edu/~abridle/deconvol/node7.html>`__ ,
   which is the most popular and widely-studied method for
   reconstructing a model image based on interferometer data. It
   iteratively removes at each step a fraction of the flux in the
   brightest pixel in a defined region of the current “dirty” image,
   and places this in the model image.

   Image reconstruction in CASA typically comprises an outer loop of
   *major cycles* and an inner loop of *minor cycles*. The major
   cycle implements transforms between the data and image domains and
   the minor cycle operates purely in the image domain. Together,
   they implement an iterative weighted :math:`\chi^2` minimization
   that `solves the measurement
   equation <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/imaging-overview>`__.
   Minor cycle algorithms can have their own (different) optimization
   schemes and the imaging framework and task interface allow for
   considerable freedom in choosing options separately for each step
   of the process.

   |image1|

   

   .. rubric:: Operating Modes
      

   The tclean task can be configured to perform either full iterative
   image reconstructions
   (see `synthesis-imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging>`__ )
   or to run each step separately. Parameters for data selection,
   image definition, gridding and deconvolution algorithms,
   restoration and primary beam setup are shared between all
   operational modes.

   The main usage modes of tclean are:

   -  .. rubric:: Imaging and Deconvolution Iterations:
         

   Construct the PSF and Dirty image and apply a deconvolution
   algorithm to reconstruct a Sky model. A series of major and minor
   cycle iterations are usually performed. The output sky model is
   then restored and optionally PB-corrected. The Sky model can
   optionally be saved in the MS during the last major cycle.

   -  .. rubric:: Make PSF and PB:
         

   Make only the Point Spread Function and the Primary Beam, along
   with auxiliary weight images (a single pixel image containing
   sum-of-weight per plane, and (for mosaic and aprojection) a weight
   image containing the weighted sum of PB square).

   -  .. rubric:: Make a Residual/Dirty Image:
         

   Make a dirty image, or a new residual image using an existing or
   specified model image. This step requires the presence of the
   sum-of-weight and weight images (for normalization) constructed
   during the PSF and PB generation step.

   -  .. rubric:: Model Prediction:
         

   Save a sky model in the MeasurementSet for later use in
   calibration (virtual model or by actual prediction into a model
   column).

   .. warning:: **WARNING** *:* While tclean is generally safe to kill at
      almost any time (ctrl-c), the possible exceptions are the brief
      instances in which the data-writes back to the MS are in
      progress. Therefore, when setting the parameter
      *savemodel='modelcolumn’*, ensure that you do not interrupt the
      tclean process (ctrl-c) while the model is being written to the
      MS, as this will likely corrupt the MS. 

   -  .. rubric:: PB-Correction:
         

   Divide out the Primary Beam from the restored Sky image.

   .. rubric:: pblimit
      

   | The pblimit is a parameter used to define the value of the
     antenna primary beam gain, below which wide-field gridding
     algorithms such as *'mosaic'* and *'awproject'* will not apply
     normalization (and will therefore set to zero). For
     *gridder='standard'*, there is no pb-based normalization during
     gridding and so the value of this parameter is ignored.
   | The sign of the pblimit parameter is used for a different
     purpose. If positive, it defines a T/F pixel mask that is
     attached to the output residual and restored images. If
     negative, this T/F pixel mask is not included. Please note that
     this pixel mask is different from the deconvolution mask used to
     control the region where CLEAN based algorithms will search for
     source peaks. In order to set a deconvolution mask based on pb
     level, please use the *'pbmask'* parameter.

   .. warning:: **WARNING** *:* Certain values of pblimit should be avoided!
      These values are 1, -1, and 0. Details can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/data-weighting>`__. *
      *

   .. rubric:: widebandpbcor
      

   `Widebandpbcor <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_widebandpbcor>`__
   is a separate task, and will eventually be implemented as a
   parameter in **tclean**. It allows correction of the primary beam
   as part of `wideband
   imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-band-imaging>`__.
   It computes a set of PBs at the specified frequencies, calculates
   Taylor-coefficient images that represent the PB spectrum, performs
   a polynomial division to PB-correct the output Taylor-coefficient
   images from **tclean** (with *nterms>1* and
   *deconvolver='mtmfs'*), and recomputes the spectral index (and
   curvature) using the PB-corrected Taylor-coefficient images.

   -  .. rubric:: Pointing Corrections:
         

   Heterogeneous Pointing Corrections can optionally be applied with
   the *usepointing* and *pointingoffsetsigdev* parameters. These
   parameters apply corrections based on the pointing errors that are
   present in the POINTING sub-table. This can improve imaging
   performance for observations with high wide-band sensitivity, such
   as is typically observed with the VLA and ALMA telescopes. An
   overview of pointing corrections is given in the CASA Docs page on
   `Widefield
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam>`__.

   -  .. rubric:: Restoration:
         

   Specify a restoring beam and re-restore the model image.

   -  .. rubric:: Auto-masking:
         

   Automatically mask emission during clean; see `Masks for
   Deconvolution <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__
   for more information.

   

   .. rubric:: Output Images
      

   Depending on the operation being run, a subset of the following
   output images will be written to disk.

   imagename = 'try'

   +-----------------------------------+-----------------------------------+
   | try.psf                           | Point Spread Function             |
   +-----------------------------------+-----------------------------------+
   | try.pb                            | Primary Beam                      |
   +-----------------------------------+-----------------------------------+
   | try.residual                      | Residual Image (or initial Dirty  |
   |                                   | Image)                            |
   +-----------------------------------+-----------------------------------+
   | try.model                         | Model Image after deconvolution   |
   +-----------------------------------+-----------------------------------+
   | try.image                         | Restored output image             |
   +-----------------------------------+-----------------------------------+
   | try.image.pbcor                   | Primary Beam corrected image      |
   +-----------------------------------+-----------------------------------+
   | try.mask                          | Deconvolution mask                |
   +-----------------------------------+-----------------------------------+
   | try.sumwt                         | A single pixel image containing   |
   |                                   | sum of weights per plane          |
   +-----------------------------------+-----------------------------------+
   | try.weight                        | Image of un-normalized sum of     |
   |                                   | PB-square (for mosaics and        |
   |                                   | A-Projection)                     |
   +-----------------------------------+-----------------------------------+
   | try.psf.tt0, try.psf.tt1,         | Multi-term images representing    |
   | try.psf.tt2, try.model.tt0,       | Taylor coefficients (of           |
   | try.model.tt1, try.residual.tt0,  | polynomials that model the sky    |
   | try.residual.tt1, try.image.tt0,  | spectrum)                         |
   | try.image.tt1, etc...             |                                   |
   +-----------------------------------+-----------------------------------+
   | try.workdirectory                 | Scratch images written within a   |
   |                                   | 'work directory' for parallel     |
   | ( try.n1.psf, try.n2.psf,         | imaging runs for cube imaging.    |
   | try.n3.psf, try.n1.residual,      | The reference images are          |
   | try.n2.residual, try.n3.residual, | reference-concatenated at the end |
   | try.n1.weight, try.n2.weight,     | to produce single output cubes.   |
   | try.n3.weight, try.n1.gridwt,     | As of CASA 5.7, continuum imaging |
   | try.n2.gridwt, etc... )           | no longer produces a              |
   |                                   | try.workdirectory.                |
   |                                   |                                   |
   |                                   |                                  |
   +-----------------------------------+-----------------------------------+

   

   .. warning:: WARNING: If an image with that name already exists, it will in
      general be overwritten. Beware using names of existing images
      however. If the tclean is run using an imagename where
      <imagename>.residual and <imagename>.model already exist, then
      tclean will continue starting from these (effectively
      restarting from the end of the previous tclean). Thus, if
      multiple runs of tclean are run consecutively with the same
      imagename, then the cleaning is incremental.

   .. rubric:: Stokes polarization products
      

   It is possible to make polarization images of various Stokes
   parameters, based on the R/L circular (e.g., VLA) or the X/Y
   linear (e.g., ALMA) polarization products. When specifying
   multiple values in the 'stokes' parameter, the output image will
   have planes (along the "polarization" axis) corresponding to the
   chosen Stokes parameters.

   The Stokes parameter is specified as a string of up to four
   letters, and can indicate stokes parameters themselves, Right/Left
   hand polarization products, or linear polarization products (X/Y).
   Examples include:

   ::

      | stokes = 'I' # Intensity only (default)
      | stokes = 'IQU' # Intensity and linear polarization
      | stokes = 'IV' # Intensity and circular polarization
      | stokes = 'IQUV' # All Stokes imaging
      | stokes = 'RR' # Right hand polarization only
      | stokes = 'XXYY' # Both linear polarizations
      | stokes = 'pseudoI' # Intensity only, but including data with
        one of the parallel polarizations flagged

   For imaging the total intensity, the stokes='I' option is stricter
   than the stokes='pseudoI' option in the sense that it excludes all
   correlationsfor which any correlation is flagged,even though the
   remaining correlations are valid.On the other hand,
   the'pseudoI'option allows Stokes I images to include data for
   which either of the parallel hand data are unflagged. For example,
   if you have RR and LL dual polarization data and you flagged parts
   of RR but not LL,stokes='I' will ignore both polarizations in the
   time-stamps where RR are flagged, while stokes='pseudoI' will
   include all unflagged data in the total intensity image. See the
   CASA Docs pages on `Types of
   Images <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/image-definition>`__ and `Single
   Dish Imaging
   (tsdimaging) <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tsdimaging>`__ for
   more information. It is also possible to split out a polarization
   product with split and image separately, but you will not be able
   to combine these part-flagged data in the uv-domain.

   

   .. rubric:: Functional Parameter Blocks
      

   The **tclean** parameters are arrangedin the functional blocks
   described below. More details on the individual parameters and
   sub-parameters can be found under the Parameters tab at the top of
   this page.

   As a general rule, sub-parameters will appear (and be used) only
   when a parent parameter has a specific value. This means that for
   a given set of choices (e.g. deconvolution or gridding algorithm)
   only parameters that are relevant to that choice will be visible
   to the user when " inp() " is invoked. It is advised that this
   task interface be used even when constructing tclean scripts that
   call the task as a python call " tclean(....) " to understand
   which parameters are relevant to the run and which are not.

   

   .. rubric:: Data Selection (selectdata)
      

   Selection parameters allow the definition of a subset of the
   supplied MS (or list of MSs) on which the imaging is to operate.
   Details can be found on the `CASA Docs pages of Image
   Selection <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__.

   

   .. rubric:: Image Definition (specmode)
      

   The image coordinate system(s) and shape(s) can be set up to form
   single images (from a single field or from multiple fields forming
   a mosaic),or multiple fields. The different modes for imaging
   include:

   -  'mfs': multi-frequency synthesis, i.e., continuum imaging with
      only one output image channel.
   -  'cube': Spectral line imaging with one or more channels. The
      fixed spectral frame, LSRK, will be used for automatic internal
      software Doppler tracking so that a spectral line observed over
      an extended time range will line up appropriately.
   -  'cubedata': Spectral line imaging with one or more channels
      There is no internal software Doppler tracking so a spectral
      line observed over an extended time range may be smeared out in
      frequency.
   -  'cubesource': Spectral line imaging while tracking moving
      source (near field or solar system `ephemeris
      objects <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/ephemeris-data>`__ ).
      The velocity of the source is accounted and the frequency
      reported is in the source frame.

   Combined use of the parameters 'specmode' and 'gridder' (see
   below) allows to specify smaller outlier fields, facetted images,
   single plane wideband images (with 1 or more Taylor terms to model
   spectra), 3D spectral cubes with multiple channels, 3D images with
   multiple Stokes planes, 4D images with frequency channels and
   Stokes planes. Various combinations of all these options are also
   supported.

   The  `CASA Docs pages on Image
   Types <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/image-definition>`__  provide
   more details.

   

   .. rubric:: Gridding Options (gridder)
      

   Options for convolutional resampling include standard gridding
   using a prolate spheroidal function, the use of FTs of Fresnel
   kernels for W-Projection, the use of baseline aperture
   illumination functions for A-Projection and Mosaicing. These
   include:

   -  'standard': standard gridding using a prolate spheroidal
      function
   -  'wproject': use of FTs of Fresnel kernels to correct for the
      widefield non-coplanar baseline effect (Cornwell et.al 2008)
   -  'widefield': Facetted imaging with or without W-Projection per
      facet.
   -  'mosaic': A-Projection that uses baseline, frequency and time
      dependent primary beams, without sidelobes, beam rotation or
      squint correction.
   -  'awproject': A-Projection from aperture illumination models
      with azimuthally asymmetric beams, including beam rotation,
      squint correction, conjugate frequency beams and W-projection
      (Bhatnagar et.al, 2008).

   Combinations of these options are also available. See the `CASA
   Docs pages on Widefield
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/wide-field-imaging-full-primary-beam>`__ for
   more information.

   For mosaicing and AW-projection, the frequency dependence of the
   primary beam within the data being imaged is included in the
   calculations and can optionally also be corrected for during
   gridding. See the CASA Docs page on `Wideband
   Imaging <https://casa.nrao.edu/casadocs-devel/imaging/synthesis-imaging/wide-band-imaging>`__ for
   details.

   

   .. rubric:: Deconvolution Options (deconvolver)
      

   All our algorithms follow the Cotton-Schwab CLEAN style of major
   and minor cycles with the details of the deconvolution algorithm
   usually contained within the minor cycle and operating in the
   image domain. Options include:

   -  'hogbom': An adapted version of Hogbom Clean (Hogbom, 1974)
   -  'clark': An adapted version of Clark Clean (Clark, 1980)
   -  'clarkstokes': Clark Clean operating separately per Stokes
      plane
   -  'multiscale': MultiScale Clean (Cornwell, 2008).
      Scale-sensitive deconvolution algorithm designed for images
      with complicated spatial structure. It parameterizes the image
      into a collection of inverted tapered paraboloids.
   -  'mtmfs': Multi-term (Multi Scale) Multi-Frequency Synthesis
      (Rau and Cornwell, 2011). Models the wide-band sky brightness
      distribution through the use of multi-term Taylor polynomial
      and wideband primary beam corrections (to be used with
      nterms>1).
   -  'mem': Maximum Entropy Method (Cornwell and Evans, 1985). Note:
      The MEM implementation in CASA is not very robust, improvements
      will be made in the future.

   If as input to tclean the stokes parameter includes polarization
   planes other than I, then choosing deconvolver='hogbom' or
   'clarkstokes' will clean (search for components) each plane
   sequentially, while deconvolver ='clark' will deconvolve jointly.

   For more details, see the `CASA Docs pages on Deconvolution
   Algorithms <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__.

   Several options for `making masks, including
   automasking <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__,
   are also provided.

   

   .. rubric:: Data Weighting (weighting)
      

   Data weighting during imaging allows for the improvement of the
   dynamic range and the ability to adjust the synthesized beam
   associated with the produced image. The weight given to each
   visibility sample can be adjusted to fit the desired output. There
   are several reasons to adjust the weighting, including improving
   sensitivity to extended sources or accounting for noise variation
   between samples. The user can adjust the weighting by changing the
   *weighting* parameter with six options: 'natural', 'uniform',
   'briggs', 'superuniform', 'briggsabs', and 'radial'. Optionally,
   a UV taper can be applied, and various parameters can be set to
   further adjust the weight calculations.

   The most used options for data weighting are 'natural', 'unform'
   and 'briggs'.

   -  'Natural' weighting gives equal weight to all samples,
      resulting in the lowest noise level and largest (poorest)
      resolution, with relatively high sidelobe levels.
   -  'Uniform' weighting gives a weight inversely proportional to
      the sampling density function, which minimizes sidelobe levels
      and provides higher resolution, but at the expense of higher
      noise levels.
   -  'Briggs' weighting provides a compromise between natural and
      uniform weighting, and often optimizes between angular
      resolution, noise, and sidelobe levels. The key parameter for
      briggs weighting is the robust sub-parameter, which takes
      value between -2.0 (close to uniform weighting) to 2.0 (close
      to natural). The scaling of Ris such that robust=0 gives a good
      trade-off between resolution and sensitivity.

   In addition to the weighting scheme specified via the 'weighting'
   parameter, additional weights can be applied:

   -  The 'uvtaper' parameter applies a Gaussian taper on the weights
      of the UV data, in addition to the weighting scheme specified
      via the 'weighting' parameter. It is equivalent to smoothing
      the PSF obtained by other weighting schemes and can be
      specified either as a Gaussian in uv-space (eg. units of lambda
      or klambda) or as a Gaussian in the image domain (eg. angular
      units like arcsec). The effect of uvtaper this is that the
      clean beam becomes larger, and surface brightness sensitivity
      increases for extended emission.
   -  The 'perchanweightdensity' parameter (for briggs and uniform
      weighting of cubes) determines whether to calculate the
      weightdensity for each channel independently(True)or a
      common weight density for all of the selecteddata (False).In
      general, perchanweightdensity=True (default since CASA 5.5)
      provides more uniform sensitivity per channel for cubes, but
      with generally larger PSFs, while perchanweightdensity=False
      results in smaller psfs for the same robustness value, but the
      rms noise as a function of channel varies and increases toward
      the edge channels.
   -  The 'mosweight' sub-parameter of the mosaic gridder determines
      whether to weight each field in a mosaic independently
      (mosweight = True), or to calculate the weight densityfrom the
      average uv distribution of all the fields combined (mosweight =
      False). For ALMA it has been shown that mosweight = True
      (default since CASA 5.4) may give better results in the
      presence of poor uv-coverage or non-uniform sensitivity across
      the mosaic, but the downside is that the major and minor axis
      of the synthesized beam may be ~10% larger than with
      mosweight=False, and it may potentially cause memory issues for
      large VLA mosaics.

   More details on data weighting can be found on the `Image
   Algorithm <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/data-weighting>`__ pages
   of CASA Docs

   

   .. rubric:: Iteration Control (niter)
      

   Iterations are controlled by user parameters (gain, niter, etc..)
   as well as stopping criteria that decide when to exit minor cycle
   iterations and trigger the next major cycle, and also when to
   terminate the major-minor loop. These stopping criteria include
   reaching iteration limits, convergence thresholds, and signs of
   divergence with appropriate messages displayed in the log. For
   more details, see the `CASA Docs pages on Iteration
   Control <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/user-interaction>`__ .

   

   

   .. rubric:: Other Options
      

   .. rubric:: Handling Large Data and Image Sizes
      

   Parallelization of the major cycle is available for continuum
   imaging and of both major and minor cycles for cube imaging. In
   order to run tclean in parallel mode it is necessary to launch
   CASA with mpicasa, and set the tclean parameter parallel=True. The
   parallelization of tclean works in the same way if the input is a
   normal MS or a Multi-MS (MMS), and thus differs from the parallel
   approach used by other tasks in that it does not require a
   partitioned MMS file. Details can be found in the `CASA Docs
   chapter on Parallel
   Processing <https://casa.nrao.edu/casadocs-devel/stable/parallel-processing>`__ .

   For large image cubes, the gridders can run into memory limits as
   they loop over all available image planes for each row of data
   accessed. To prevent this problem, we can grid subsets of channels
   in sequence with the chanchunks parameter, so that at any given
   time only part of the image cube needs to be loaded into memory.
   The chanchunks parameter controls the number of chunks to split
   the cube into.

   .. rubric:: User Interaction
      

   Options for user interaction include `interactive
   masking <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__
   and editing of iteration control parameters. The `output log
   files <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-logger>`__ can
   also be used to diagnose some problems.

   Several convenience features are also available, such as operating
   on the MS in read-only mode (which does not require write
   permissions), the ability to restart and continue imaging runs
   without incuring the unnecessary cost of an inital major cycle or
   PSF construction and the optional return of a python dictionary
   that contains the convergence history of the run.

   .. rubric:: Scripting Controls
      

   Finer control can be achieved using the PySynthesisImager tools to
   run (for example) only image domain deconvolution or to insert
   methods for automatic mask generation (for example) in between the
   existing major/minor cycle loops or to connect external methods or
   algorithms for either the minor or major cycles.

   .. rubric:: Tracking moving sources or sources with ephemeris
      tables
      

   Ifthe phasecenter isa known major solar system object
   ('MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS',
   'NEPTUNE', 'PLUTO', 'SUN', 'MOON') or is an ephemerides table,
   then that source is tracked and the background sources get smeared
   (which is useful especially for long observations or multi epoch
   data). There is a special case, when phasecenter='TRACKFIELD',
   which will use the ephemerides or polynomial phasecenter in the
   FIELD table of theMeasurementSetsas the source center to track.
   When in tracking mode, the image center will be the direction of
   the source at the first time in the user selected data. At all
   other times, the source will be shifted by the amount it has moved
   in the frame of the image to that initial time. Examples of usage
   are presented in the **tclean** examples tab.

   .. note:: **NOTE**: When displaying ephemeris images, it is good practice
      to use relative coordinates to determine the average offset of
      emission from the ephemeris path over the observation, i.e.,
      axis label properties: world coordinate, relative position. The
      use of the absolute grid (default) can be misleading since the
      chosen coordinate frame is associated with the ephemeris path
      location at an unspecified time, although usually near the
      beginning of the experimient.

   More information can be found in the `CASA Docs chapter on
   Ephemeris
   Data <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/ephemeris-data>`__.

.. |image1| image:: ../media/26ad14d4f63ff633dbd5d9e92d40a5059ab46a67.png
    """
    pass
