#
# stub function definition file for docstring parsing
#

def sdintimaging(vis, usedata='sdint', sdimage='', sdpsf='', sdgain=1.0, dishdia=100.0, selectdata=True, field='', spw='', timerange='', uvrange='', antenna='', scan='', observation='', intent='', datacolumn='corrected', imagename='', imsize=100, cell='"1arcsec"', phasecenter='', stokes='I', projection='SIN', startmodel='', specmode='mfs', reffreq='', nchan=-1, start='', width='', outframe='LSRK', veltype='radio', restfreq=[''], interpolation='linear', chanchunks=1, perchanweightdensity=True, gridder='standard', facets=1, psfphasecenter='', wprojplanes=1, vptable='', mosweight=True, aterm=True, psterm=False, wbawp=True, cfcache='', usepointing=False, computepastep=360.0, rotatepastep=360.0, pointingoffsetsigdev=[''], pblimit=0.2, deconvolver='hogbom', scales=[''], nterms=2, smallscalebias=0.0, restoration=True, restoringbeam='', pbcor=False, weighting='natural', robust=0.5, noise='1.0Jy', npixels=0, uvtaper=[''], niter=0, gain=0.1, threshold=0.0, nsigma=0.0, cycleniter=-1, cyclefactor=1.0, minpsffraction=0.05, maxpsffraction=0.8, interactive=False, usemask='user', mask='', pbmask=0.0, sidelobethreshold=3.0, noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=0.0, smoothfactor=1.0, minbeamfrac=0.3, cutthreshold=0.01, growiterations=75, dogrowprune=True, minpercentchange=-1.0, verbose=False, fastnoise=True, restart=True, savemodel='none', calcres=True, calcpsf=True, parallel=False):
    r"""
Parameters
   - **usedata** (string) - Output image type(int, sd, sdint)
   - **vis** (string, stringArray) - Name of input visibility file(s)
   - **selectdata** (bool) - Enable data selection parameters
   - **datacolumn** (string) - Data column to image(data,corrected)
   - **imagename** (int, string, stringArray) - Pre-name of output images
   - **imsize** (int, intArray) - Number of pixels
   - **cell** (int, double, intArray, doubleArray, string, stringArray) - Cell size
   - **phasecenter** (int, string) - Phase center of the image
   - **stokes** (string) - Stokes Planes to make
   - **projection** (string) - Coordinate projection 
   - **startmodel** (string) - Name of starting model image
   - **specmode** (string) - Spectral definition mode (mfs,cube,cubedata, cubesource)
   - **nchan** (int) - Number of channels in the output image
   - **start** (string) - First channel (e.g. start=3,start=\'1.1GHz\',start=\'15343km/s\')
   - **width** (string) - Channel width (e.g. width=2,width=\'0.1MHz\',width=\'10km/s\')
   - **outframe** (string) - Spectral reference frame in which to interpret \'start\' and \'width\'
   - **veltype** (string) - Velocity type (radio, z, ratio, beta, gamma, optical)
   - **restfreq** (stringArray) - List of rest frequencies
   - **interpolation** (string) - Spectral interpolation (nearest,linear,cubic)
   - **chanchunks** (int) - Number of channel chunks
   - **perchanweightdensity** (bool) - whether to calculate weight density per channel in Briggs style weighting or not
   - **gridder** (string) - Gridding options (standard, wproject, widefield, mosaic, awproject)
   - **deconvolver** (string) - Minor cycle algorithm (hogbom,clark,multiscale,mtmfs,mem,clarkstokes)
   - **restoration** (bool) - Do restoration steps (or not)
   - **weighting** (string) - Weighting scheme (natural,uniform,briggs, briggsabs[experimental])
   - **niter** (int) - Maximum number of iterations
   - **usemask** (string) - Type of mask(s) for deconvolution:  user, pb, or auto-multithresh
   - **fastnoise** (bool) - True: use the faster (old) noise calculation. False: use the new improved noise calculations
   - **restart** (bool) - True : Re-use existing images. False : Increment imagename
   - **savemodel** (string) - Options to save model visibilities (none, virtual, modelcolumn)
   - **calcres** (bool) - Calculate initial residual image
   - **calcpsf** (bool) - Calculate PSF
   - **parallel** (bool) - Run major cycles in parallel

Subparameters
   .. raw:: html

      <details><summary><i> usedata = sd </i></summary>

   - **sdimage** (string="") - Input single dish image
   - **sdpsf** (string="") - Input single dish PSF image
   - **sdgain** (double=1.0) - A factor or gain to adjust single dish flux scale
   - **dishdia** (double=100.0) - Effective dish diameter

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> usedata = sdint </i></summary>

   - **sdimage** (string="") - Input single dish image
   - **sdpsf** (string="") - Input single dish PSF image
   - **sdgain** (double=1.0) - A factor or gain to adjust single dish flux scale
   - **dishdia** (double=100.0) - Effective dish diameter

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> selectdata = True </i></summary>

   - **field** (string="", stringArray) - field(s) to select
   - **spw** (string="", stringArray) - spw(s)/channels to select
   - **timerange** (string="", stringArray) - Range of time to select from data
   - **uvrange** (string="", stringArray) - Select data within uvrange
   - **antenna** (string="", stringArray) - Select data based on antenna/baseline
   - **scan** (string="", stringArray) - Scan number range
   - **observation** (string="", int) - Observation ID range
   - **intent** (string="", stringArray) - Scan Intent(s)

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> specmode = mfs </i></summary>

   - **reffreq** (string="") - Reference frequency

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = standard </i></summary>

   - **vptable** (string="") - Name of Voltage Pattern table
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = widefield </i></summary>

   - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
   - **facets** (int=1) - Number of facets on a side
   - **vptable** (string="") - Name of Voltage Pattern table
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = wproject </i></summary>

   - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
   - **vptable** (string="") - Name of Voltage Pattern table
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = wprojectft </i></summary>

   - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
   - **vptable** (string="") - Name of Voltage Pattern table
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = mosaic </i></summary>

   - **vptable** (string="") - Name of Voltage Pattern table
   - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.
   - **mosweight** (bool=True) - Indepently weight each field in a mosaic
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
   - **psfphasecenter** (int="", string) - optional direction to calculate psf for mosaic (default is image phasecenter)

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = mosaicft </i></summary>

   - **vptable** (string="") - Name of Voltage Pattern table
   - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
   - **psfphasecenter** (int="", string) - optional direction to calculate psf for mosaic (default is image phasecenter)

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = ftmosaic </i></summary>

   - **vptable** (string="") - Name of Voltage Pattern table
   - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.
   - **mosweight** (bool=True) - Indepently weight each field in a mosaic
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = imagemosaic </i></summary>

   - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
   - **vptable** (string="") - Name of Voltage Pattern table
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = awproject </i></summary>

   - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
   - **psterm** (bool=False) - Use prolate spheroidal during gridding
   - **aterm** (bool=True) - Use aperture illumination functions during gridding
   - **cfcache** (string="") - Convolution function cache directory name
   - **computepastep** (double=360.0) - Parallactic angle interval after the AIFs are recomputed (deg)
   - **rotatepastep** (double=360.0) - Parallactic angle interval after which the nearest AIF is rotated (deg) 
   - **pointingoffsetsigdev** (intArray='', doubleArray) -  Pointing offset threshold to determine heterogeneity of pointing corrections for the AWProject gridder
   - **wbawp** (bool=True) - Use wideband A-terms
   - **mosweight** (bool=False) - Indepently weight each field in a mosaic
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
   - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> gridder = awprojectft </i></summary>

   - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
   - **psterm** (bool=False) - Use prolate spheroidal during gridding
   - **aterm** (bool=True) - Use aperture illumination functions during gridding
   - **cfcache** (string="") - Convolution function cache directory name
   - **computepastep** (double=360.0) - Parallactic angle interval after the AIFs are recomputed (deg)
   - **rotatepastep** (double=360.0) - Parallactic angle interval after which the nearest AIF is rotated (deg) 
   - **pointingoffsetsigdev** (intArray='', doubleArray) -  Pointing offset threshold to determine heterogeneity of pointing corrections for the AWProject gridder
   - **wbawp** (bool=True) - Use wideband A-terms
   - **mosweight** (bool=False) - Indepently weight each field in a mosaic
   - **pblimit** (double=0.2) - PB gain level at which to cut off normalizations 
   - **usepointing** (bool=False) - The parameter makes the gridder utilize the pointing table phase directions while computing the residual image.

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> weighting = natural </i></summary>

   - **uvtaper** (stringArray=[]) - uv-taper on outer baselines in uv-plane

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> weighting = briggs </i></summary>

   - **robust** (double=0.5) - Robustness parameter
   - **npixels** (int=0) - Number of pixels to determine uv-cell size 
   - **uvtaper** (stringArray=[]) - uv-taper on outer baselines in uv-plane

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> weighting = briggsabs </i></summary>

   - **robust** (double=0.5) - Robustness parameter
   - **noise** (variant="1.0Jy") - 
   - **npixels** (int=0) - Number of pixels to determine uv-cell size 
   - **uvtaper** (stringArray=[]) - uv-taper on outer baselines in uv-plane

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> deconvolver = multiscale </i></summary>

   - **scales** (intArray='', floatArray) - List of scale sizes (in pixels) for multi-scale algorithms
   - **smallscalebias** (double=0.0) - Biases the scale selection when using multi-scale or mtmfs deconvolvers 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> deconvolver = mtmfs </i></summary>

   - **scales** (intArray='', floatArray) - List of scale sizes (in pixels) for multi-scale algorithms
   - **nterms** (int=2) - Number of Taylor coefficients in the spectral model
   - **smallscalebias** (double=0.0) - Biases the scale selection when using multi-scale or mtmfs deconvolvers 

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> restoration = True </i></summary>

   - **restoringbeam** (string='', stringArray) - Restoring beam shape to use. Default is the PSF main lobe
   - **pbcor** (bool=False) - Apply PB correction on the output restored image

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> niter != 0 </i></summary>

   - **gain** (double=0.1) - Loop gain
   - **threshold** (double=0.0) - Stopping threshold 
   - **nsigma** (double=0.0) - Multiplicative factor for rms-based threshold stopping
   - **cycleniter** (int=-1) - Maximum number of minor-cycle iterations
   - **cyclefactor** (double=1.0) - Scaling on PSF sidelobe level to compute the minor-cycle stopping threshold.
   - **minpsffraction** (double=0.05) - PSF fraction that marks the max depth of cleaning in the minor cycle
   - **maxpsffraction** (double=0.8) - PSF fraction that marks the minimum depth of cleaning in the minor cycle 
   - **interactive** (bool=False, int) - Modify masks and parameters at runtime

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> usemask = user </i></summary>

   - **mask** (string="", stringArray) - Mask (a list of image name(s) or region file(s) or region string(s) )
   - **pbmask** (double=0.0) - primary beam mask

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> usemask = pb </i></summary>

   - **pbmask** (double=0.2) - primary beam mask

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> usemask = auto-multithresh </i></summary>

   - **pbmask** (double=0.2) - primary beam mask
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


Description
      .. rubric:: Joint reconstruction of wideband single dish and
         interferometer data in CASA
         is `experimental <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/tasks-and-tools>`__ .
         Please use at own discretion.
         :name: joint-reconstruction-of-wideband-single-dish-and-interferometer-data-in-casa-is-experimental.-please-use-at-own-discretion.

      The scope of parameters that has been tested for CASA 5.7/6.1 can
      be found on the CASA Docs chapter page on " `Joint Single Dish
      and Interferometer Image
      Reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction>`__ "

       

      The `sdintimaging <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/>`__ task
      allowsjoint reconstruction of wideband single dish and
      interferometer data.

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

       

      A more detailed description of the underlying algorithm, as well
      as results from its testing, can be found on the CASA Docs chapter
      page on "`Joint Single Dish and Interferometer Image
      Reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction>`__". 
      Note that the above diagram shows only the 'mtmfs' variant. Cube
      deconvolution proceeds directly with the cubes in the green box
      above, without the extra conversion back and forth to the
      multi-term basis. Primary beam handling is also not shown in this
      diagram, but full details (via pseudocode) are available in
      the `reference
      publication. <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7>`__

       

      .. rubric:: Task Specification : sdintimaging
         :name: task-specification-sdintimaging

       

      The sdintimaging task shares a significant number of parameters
      with the tclean task. In the description below, parameters that
      are specific to sdintimaging are listed with full details, but all
      others will reference the existing tclean parameter documentation.

       

      .. rubric:: Data Selection
         :name: data-selection

      -  All data selection options allowed for interferometer data.
         This set of parameters is identical to those in task
         **tclean**.

       

      .. rubric:: Image Definition
         :name: image-definition

      -  Spatial dimensions are defined via the parameters : *imsize,
         cell, phasecenter, projection*

      -  Spectral dimensions for the major cycle are defined for cubes
         : *nchan,start, width, outframe, veltype, restfreq,
         interpolation
         *

      -  Spectral dimensions for the minor cycle are chosen based on
         specmode.  For *specmode='cube'* the minor cycle follows the
         same channelization as the major cycle. For *specmode='mfs'*,
         the choice of deconvolver and the setting of *'reffreq'* will
         decide the spectral coordinate system of the wideband image
         that is created after collapsing the cube images from the major
         cycle. For *deconvolver='mtmfs'* the appropriate cube-to-taylor
         (and reverse) conversions are applied.

      .. rubric:: Specifying Both Cube and MFS settings (for
         *specmode='mfs'*) :
         :name: specifying-both-cube-and-mfs-settings-for-specmodemfs

      In **sdintimaging**, with MFS deconvolution, one *needs to specify
      both cube and mfs settings for frequency coordinates because in
      this usage mode the major cycle is done with cubes and the minor
      cycle with mfs*. This detail is different from the tclean task.  A
      few general rules to follow for a MFS (or MTMFS) minor cycle are

      -  The reffreq must lie between the ends of the cube frequency
         range (default based on data selection, or explicitly specified
         using *start, width, nchan*).  If this is not the case, an
         error message will appear.  If left at its default value of
         *reffreq=''*, it will be automatically computed to be the mean
         of the first and last channel frequencies and a log message is
         printed with the new value.

      -  For a wideband imaging run with nterms, at least nterms
         channels must be present in the input cubes. Ideally, in order
         to fully capture spectral variations and also guard against
         missing data, it is recommended that the cube be defined with
         between 5 and 20 channels. More may of course be used,
         especially in order to avoid bandwidth smearing within
         channels, but a larger number of channels will cause the
         feathering step to take longer.  Warnings are printed if the
         nchan of the cube is small (less than 5) or too large (more
         than 50), and the task will exit with an error if nchan <
         nterms.

      -  The sdintimaging task will perform the above checks on the
         input parameters and report problems/warnings as appropriate.  
         The internal automation of some of these settings is on our
         'Future Work' list.

       

      .. rubric:: Single Dish data input 
         :name: single-dish-data-input

       

      -  Image cubes that represent the observed SD image per channel
         and the corresponding SD beam :  *sdimage, sdpsf*

      -  Both the sdimage and sdpsf image cubes must contain per plane
         restoringbeams that represent the effective SD beam.  Per-plane
         restoring beams may be added to an existing image cube using
         ia.open(), a loop over channels with ia.setrestoringbeam(..),
         and ia.close()

      -  Ideally, the imsize, cellsize, and phasecenter of the SD cube
         should match that of the INT cubes specified by imsize,
         cellsize, phasecenter.   However in case of a detected
         mismatch, the *ia.regrid()* method is called internally to
         convert it to the target csys prior to continuing. It is
         expected that such a regrid is possible and in case of error,
         the user should see a warning and suggestion to experiment with
         the imregrid task to reformat their input SD cube.

      -  The frequency axis of the SD cubes must exactly match the INT
         cube spectral axis defined by nchan, start, width.  Note that
         in the internal imregrid call, the frequency axis is not
         regridded. *This means that nchan, start and width specified in
         the task interface must match the frequency coordinates of the
         input SD image.*

         -  Use a helper method (shown in the `ALMA M100
            example <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging/examples>`__ below)
            to extract nchan/start/width parameters from the SD Image
            cube, and supply these as inputs to sdintimaging to exactly
            match the frequency coordinates of the SD and INT cubes.

      -  The order of the direction, stokes, and spectral axes must
         match the INT cubes, typically RA,DEC,Stokes,Channel

      -  Blank channels (sum of pixel amplitudes=0) are internally
         flagged and left out of the joint reconstruction.   So, one way
         to tell the algorithm to ignore some channels in the input SD
         cube is to force all pixel values to zero.

      -  A convenience option has been provided within sdintimaging to
         auto-generate simple SD PSF cubes. If sdpsf='', a PSF cube is
         calculated by evaluating Gaussians based on the restoringbeam
         information per channel read from the input SD Image cube. 
         This option is useful if only an SD Image cube is available as
         the output of the single dish imaging step.

      Please see the `ALMA M100
      example <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_sdintimaging/examples>`__ section
      for sample code and task calls that illustrates the simplest way
      of setting up these inputs. 

       

      To use SD PSFs that represent actual SD beam patterns, please read
      the following details.

      -  The SD PSF must contain a model of the single dish beam at the
         same world-coordinate location as the imaging phasecenter that
         is specified (or assumed via the supplied MS, when
         *phasecenter=’’*), it must be normalized to peak 1, and the PSF
         cube must contain corresponding restoring beams per channel.

      -  It is also expected that the single dish PSF peak is at the
         image center after regridding (same as the interferometer PSF).
         An internal check will look for position shifts (subpixel
         shifts too) and if offsets are 0.001 of a degree or more, it
         will not proceed.  A way around this is to manually re-evaluate
         the SD PSF directly onto the coordinate system of one of the
         intermediate INT images such that the middle pixel contains the
         peak of the PSF. An alternative is to use the *sdpsf=''*
         option, with which one can approximate the SD PSF.

      -  Other ideas to create an SD PSF : Use the SD image cube for
         header information and cube dimensions. Create an empty CASA
         image, fill it with evaluated Gaussians that match the SD beam
         size per channel. A sample script is provided
         `here <https://github.com/urvashirau/WidebandSDINT/blob/master/ScriptForRealData/make_gauss_beam_cube.txt>`__.

      -  The SD PSFs (in this case for the simulated examples/tests) are
         typically generated by calculating disk-shaped aperture
         functions of the appropriate dish diameter, taking a Fourier
         transform and squaring and normalizing the result.

       

      .. rubric:: Data Combination options
         :name: data-combination-options

      The sdintimaging task may be run in three data combination modes
      via the *usedata* parameter. 

      -  **'sdint' :**  Use the interferometer and single dish data in a
         joint reconstruction.  Specification of the ‘sdgain’ and
         ‘ dishdia’ are the same as for the feather task. The method in
         the feather task is called internally to combine image cubes
         and PSF cubes prior to deconvolution.

         -  For *specmode='mfs'*, each channel is pb-corrected to flat
            sky and then a common primary beam (and mask) is applied
            prior to deconvolution. The common PB is computed as a
            weighted average of PBs, using the .sumwt per channel. 
         -  When the INT or the SD cubes contain flagged (i.e. empty)
            channels, they are left out of the joint reconstruction.
            Therefore, only those channels that have both INT and SD
            images, are used.

      -  '**sd**' : Use only the single-dish data and enable
         deconvolution of the single dish image cubes. Both cube and
         wideband multi-term deconvolution of single dish data are
         possible. Note that this mode (currently) still requires an
         interferometer MS to be supplied in order to construct image
         templates. This option is experimental and has passed only the
         tests reported in the publication and the examples shown in
         CASAdocs.

      -  **'int'** : Uses only interferometer data. For
         gridder= *'mosaic'* and *'awproject'*, it implements a
         wideband mosaic scheme similar to those offered via task
         tclean, but with the concept of conjugate-pb correction
         implemented in the image domain. It does so by taking a
         flat-sky normalization per channel, followed by a flat-noise
         rescaling to apply a common primary beam to all channels, and
         subsequently collapsing into taylor images for deconvolution.
         This option is experimental and has passed only the most basic
         tests. Further characterization and comparison to the
         equivalent imaging modes in tclean will be done after the CASA
         6.1 release.  Therefore, please use only with caution.

      .. rubric::  
         :name: section

      .. rubric:: Tuning the sdgain parameter :
         :name: tuning-the-sdgain-parameter

      The *sdgain* parameter acts as an image weighting option by being
      applied both to the data as well as the PSFs during combination.
      Setting values away from 1.0 adjusts the relative weight of the SD
      information to be higher than INT cube, separately for each
      channel. Initial demonstrations have shown promise, but the
      robustness of this algorithm control will become clearer with more
      practical use.

       

      -  A high sdgain value ( > 1.0 ) has been demonstrated to
         emphasize extended emission without changing the high
         resolution structure (see the ALMA M100 example in the "`Joint
         Single Dish and Interferometer Image
         Reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction>`__"
         page).   However, when using a high sdgain, please remember to
         monitor the shape of the joint PSF to look for signs of angular
         resolution loss due to weighting the SD data much too high. 

      -  A low sdgain value ( < 1.0 ) has also been shown to be useful
         in reducing the effect of the usually high SD noise in the
         joint reconstruction while still preserving flux correctness
         (see the `algorithm
         publication <https://iopscience.iop.org/article/10.3847/1538-3881/ab1aa7/meta>`__)
         .  This mode could be useful when the SD image signal-to-noise
         ratio is high enough to match that of the interferometer
         images, even if the rms noise of the SD data is higher than the
         INT image rms (which can happen when the flux of the SD data is
         higher than that of the INT data).

       

       

      .. rubric:: Imaging and Deconvolution Options
         :name: imaging-and-deconvolution-options

      Parameters that control interferometer-gridding/imaging and
      deconvolution options are *specmode, gridder, deconvolver* (and
      associated sub-parameters similar to **tclean**).

      -  **Specmode** : Supported modes include  *specmode='cube' * with
         any single-term deconvolver, and  *specmode='mfs'* with any
         deconvolver (including multi-term). These options represent
         different conversion routines between the feathered cubes and
         the inputs/outputs for deconvolution.

         -  *‘cube’*: the cubes are sent as is to the deconvolver and
            the output model cube is directly passed to the major cycle.
         -  *‘mfs’*: the cubes are averaged to form a continuum image
            and continuum PSF prior to deconvolution and the model image
            is expanded out to an image model cube prior to the next
            major cycle.
         -  *‘mtmfs’*: the cubes are converted to Taylor-weighted
            averages in accordance with the MTMFS algorithm and the
            model Taylor coefficient image output from the deconvolver
            are evaluated back onto a model image cube prior to the
            major cycle. This image reshaping follows the diagram at the
            top of this page.

      All frequency averages in the Cube to Taylor conversions and in
      the calculation of a common Primary Beam use the interferometer
      sum-or-weight spectrum as frequency-dependent weights, multiplied
      by a 1-0 flag to identify channels with valid images in both the
      SD and INT cubes

      -  **Deconvolvers** : Algorithms supported are *‘multiscale',
         'hogbom’* and *'clark'* for *cube* and *mfs(nterms=1)* imaging
         and *‘mtmfs’* for multi-term mfs imaging. However, for use
         cases where single dish data are required along with
         interferometer data, multiscale deconvolution is most
         appropriate to get accurate reconstructions at multiple spatial
         scales. The *‘multiscale’* deconvolver applies to
         *specmode=’cube’* and *'mfs(nterms=1)’* and the *‘mtmfs’*
         deconvolver applies to the *specmode=’mfs(nterms>1)’*. In all
         cases, the *‘scales’* parameter is also relevant as it sets the
         list of scale sizes to use during deconvolution.The *‘hogbom’*
         deconvolver is relevant only when used with *usedata=’sdonly’*
         to deconvolve unresolved sources.

      -  **Gridders** :  Any gridder supported by task tclean may be
         used with **sdintimaging**. Two options that represent
         different normalization schemes are *'standard'* and *'mosaic'*
         (or *'awproject'*). Similar to tclean, the  *‘standard’*
         gridder does not consider primary beams and represents one mode
         of operation that is valid only in the central region of the
         interferometer primary beam. The *‘mosaic’* and *'awproject'*
         gridders account for primary beams and are appropriate for
         full-beam or joint mosaic images.  For these two A-Projection
         gridders, the normtype is always *'flatnoise'* and conjbeams is
         implemented via an image-domain scheme not offered by task
         tclean.  Note also that although the *‘awproject’* gridder may
         be used interchangeably with *‘mosaic’*, this mode will not be
         tested for the initial release of this task (CASA 5.7/6.1).

       

      .. rubric:: Iteration Control  and Automasking
         :name: iteration-control-and-automasking

      Iteration contol and automasking parameters are identical to those
      used in task tclean, with the same rules and conventions applied
      to stopping criteria.

       

      .. rubric:: Output Images
         :name: output-images

      The initial version of the sdintimaging task produces many
      intermediate images which persist after the end of the task.  The
      naming convention of the images is more complex than the tclean
      task.

      +-----------------------------------+-----------------------------------+
      | <imagename>.sd.cube.{image,psf}   | Image cubes onto which the input  |
      |                                   | Single Dish image and psf cubes   |
      | <im                               | are regridded.                    |
      | agename>.sd.cube.{model,residual} |                                   |
      |                                   | Intermediate products containing  |
      |                                   | the model image cube that is      |
      |                                   | subtracted from the SD image to   |
      |                                   | make the SD residual              |
      +-----------------------------------+-----------------------------------+
      | <imagename>.int.cube.{residual,   | Image cubes made from only the    |
      | psf, sumwt,weight,pb)             | interferometer data               |
      |                                   |                                   |
      | <imagename>.int.cube.{model}      | Intermediate product. Cube model  |
      |                                   | image used for model prediction   |
      |                                   | and residual calculation.         |
      +-----------------------------------+-----------------------------------+
      | <imagename>.joint.cube.{residual, | Feathered cubes for the residual  |
      | psf}                              | and psf.   For cube minor cycles, |
      |                                   | these are also the inputs to the  |
      | <imagename>.joint.multite         | deconvolver.                      |
      | rm.{residual,psf}.{tt0,tt1[,tt2]} |                                   |
      |                                   | Multi-term residual images and    |
      |                                   | spectral PSFs constructed from    |
      |                                   | the above feathered cubes. These  |
      |                                   | are inputs to the minor cycle for |
      |                                   | multi-term deconvolution          |
      +-----------------------------------+-----------------------------------+
      | <imagename>.joint.cube.{image,    | For cube minor cycles, all        |
      | sumwt, weight, pb,model,          | standard data products            |
      | mask,pbcor}                       |                                   |
      +-----------------------------------+-----------------------------------+
      | <i                                | For multi-term minor cycles, all  |
      | magename>.joint.multiterm.{image, | standard data products            |
      | sumwt, weight, pb, model, mask,   |                                   |
      | alpha,pbcor}  with  {.tt0, .tt1,  |                                   |
      | .tt2 } extensions as appropriate. |                                   |
      +-----------------------------------+-----------------------------------+

       This long list of output and intermediate images is likely to be
      pruned in a future release.

       

       

      For more information and examples on the functionality of the
      sdintimaging task, see the CASA Docs chapter page on " `Joint
      Single Dish and Interferometer Image
      Reconstruction <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-combination/joint-sd-and-interferometer-image-reconstruction>`__ "

.. |image1| image:: ../../_media/66b05f9d215777360fc1b1ce0147ce542eeb93b5.png
   :class: image-inline
   :width: 599px
   :height: 329px

    """
    pass
