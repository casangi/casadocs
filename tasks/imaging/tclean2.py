#
# stub function definition file for docstring parsing
#

def tclean2(vis, selectdata=True, field='', spw='', timerange='', uvrange='', antenna='', scan='', observation='', intent='', datacolumn='corrected', imagename='', imsize=100, cell='"1arcsec"', phasecenter='', stokes='I', projection='SIN', startmodel='', specmode='mfs', reffreq='', nchan=-1, start='', width='', outframe='LSRK', veltype='radio', restfreq=[''], interpolation='linear', gridder='standard', facets=1, chanchunks=1, wprojplanes=1, aterm=True, psterm=False, wbawp=True, conjbeams=True, cfcache='', computepastep=360.0, rotatepastep=360.0, pblimit=0.2, normtype='flatnoise', deconvolver='hogbom', scales=[''], nterms=2, scalebias=0.6, restoringbeam='', outlierfile='', weighting='natural', robust=0.5, npixels=0, uvtaper=[''], niter=0, gain=0.1, threshold=0.0, cycleniter=-1, cyclefactor=1.0, minpsffraction=0.05, maxpsffraction=0.8, interactive=False, usemask='user', mask='', pbmask=0.0, maskthreshold='', maskresolution='', restart=True, savemodel='none', makeimages='auto', calcres=True, calcpsf=True, restoremodel='auto', writepb='auto', ranks=''):
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
   - **projection** (string='SIN') - Coordinate projection (SIN, HPX)
   - **startmodel** (string='') - Name of starting model image
   - **specmode** (string='mfs') - Spectral definition mode (mfs,cube,cubedata)

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

      .. raw:: html

         </details>
   - **gridder** (string='standard') - Gridding options (standard, wproject, widefield, mosaic, awproject)

      .. raw:: html

         <details><summary><i> gridder = widefield </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **facets** (int=1) - Number of facets on a side

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = wproject </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = wprojectft </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = mosaic </i></summary>

      - **pblimit** (double=0.2) - >PB gain level at which to cut off normalizations 
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = mosaicft </i></summary>

      - **pblimit** (double=0.2) - >PB gain level at which to cut off normalizations 
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = ftmosaic </i></summary>

      - **pblimit** (double=0.2) - >PB gain level at which to cut off normalizations 
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = imagemosaic </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **pblimit** (double=0.2) - >PB gain level at which to cut off normalizations 
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = awproject </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **pblimit** (double=0.2) - >PB gain level at which to cut off normalizations 
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky)
      - **psterm** (bool=False) - Use prolate spheroidal during gridding
      - **aterm** (bool=True) - Use aperture illumination functions during gridding
      - **cfcache** (string='') - >Convolution function cache directory name
      - **computepastep** (double=360.0) - At what parallactic angle interval to recompute AIFs (deg)
      - **rotatepastep** (double=360.0) - At what parallactic angle interval to rotate nearest AIF (deg) 
      - **wbawp** (bool=True) - Use wideband A-terms
      - **conjbeams** (bool=True) - Use conjugate frequency for wideband A-terms

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> gridder = awprojectft </i></summary>

      - **wprojplanes** (int=1) - Number of distinct w-values for convolution functions
      - **pblimit** (double=0.2) - >PB gain level at which to cut off normalizations 
      - **normtype** (string='flatnoise') - Normalization type (flatnoise, flatsky)
      - **psterm** (bool=False) - Use prolate spheroidal during gridding
      - **aterm** (bool=True) - Use aperture illumination functions during gridding
      - **cfcache** (string='') - >Convolution function cache directory name
      - **computepastep** (double=360.0) - At what parallactic angle interval to recompute AIFs (deg)
      - **rotatepastep** (double=360.0) - At what parallactic angle interval to rotate nearest AIF (deg) 
      - **wbawp** (bool=True) - Use wideband A-terms
      - **conjbeams** (bool=True) - Use conjugate frequency for wideband A-terms

      .. raw:: html

         </details>
   - **deconvolver** (string='hogbom') - Minor cycle algorithm (hogbom,clark,multiscale,mtmfs,mem,clarkstokes)

      .. raw:: html

         <details><summary><i> deconvolver = hogbom </i></summary>

      - **restoringbeam** ({string, stringArray}='') - Restoring beam shape to use. Default is the PSF main lobe

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> deconvolver = clark </i></summary>

      - **restoringbeam** ({string, stringArray}='') - Restoring beam shape to use. Default is the PSF main lobe

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> deconvolver = multiscale </i></summary>

      - **scales** ({intArray, floatArray}=['']) - List of scale sizes (in pixels) for multi-scale algorithms
      - **restoringbeam** ({string, stringArray}='') - Restoring beam shape to use. Default is the PSF main lobe

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> deconvolver = mtmfs </i></summary>

      - **scales** ({intArray, floatArray}=['']) - List of scale sizes (in pixels) for multi-scale algorithms
      - **nterms** (int=2) - Number of Taylor coefficients in the spectral model
      - **restoringbeam** ({string, stringArray}='') - Restoring beam shape to use. Default is the PSF main lobe

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> deconvolver = aasp </i></summary>

      - **restoringbeam** ({string, stringArray}='') - Restoring beam shape to use. Default is the PSF main lobe

      .. raw:: html

         </details>
   - **outlierfile** (string='') - Name of outlier-field image definitions
   - **weighting** (string='natural') - Weighting scheme (natural,uniform,briggs)

      .. raw:: html

         <details><summary><i> weighting = natural </i></summary>

      - **uvtaper** (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> weighting = briggs </i></summary>

      - **robust** (double=0.5) - Robustness parameter
      - **npixels** (int=0) - Number of pixels to determine uv-cell size (0 : -/+ 3 pixels)
      - **uvtaper** (stringArray=['']) - uv-taper on outer baselines in uv-plane

      .. raw:: html

         </details>
   - **niter** (int=0) - Maximum number of iterations
   - **usemask** (string='user') - Type of mask(s) for deconvolution (user,pb,auto-thresh)

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

         <details><summary><i> usemask = auto-thresh </i></summary>

      - **pbmask** (double=0.0) - primary beam mask
      - **maskthreshold** (string='') - threshold for automasking (string with unit, e.g. "1.0mJy", sigma,  or fraction of peak ,e.g. 0.1)
      - **maskresolution** (string='') - resolution for automasking (string, e.g. "10arcsec")

      .. raw:: html

         </details>
   - **restart** (bool=True) - True : Re-use existing images. False : Increment imagename
   - **savemodel** (string='none') - Options to save model visibilities (none, virtual, modelcolumn)
   - **makeimages** (string='auto') - List of output images (auto,choose)

      .. raw:: html

         <details><summary><i> makeimages = choose </i></summary>

      - **calcres** (bool=True) - Calculate initial residual image
      - **calcpsf** (bool=True) - Calculate PSF
      - **restoremodel** (string='auto') - Restore the model image
      - **writepb** (string='auto') - Make a primary beam image

      .. raw:: html

         </details>
   - **ranks** (intarray='') - List of participating ranks



    """
    pass
