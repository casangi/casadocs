.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task clean examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Basic Examples
         :name: basic-examples

      The first example shows the typical parameters used to create a
      'dirty' image and a 'dirty' beam (or PSF). Setting *niter=0*
      results in no cleaning being performed on the image.

      .. container:: casa-input-box

         | clean(vis='example.ms',
         |       imagename='example', #produces images with 'example'
           prefix; .image, .psf, .flux, .flux.pbcoverage (mosaics only),
           .model, .residual, and .mask
         |       field='0~2', #field IDs 0,1,2
         |       spw='0~2,4', #spectral windows 0,1,2,4 (all channels)
         |       mode='mfs', #Multi-frequency synthesis; makes one image
           from all the channels in the selected spws
         |       imsize=[128,128], #created images have sizes of 128 by
           128 pixels
         |       cell='0.1arcsec', #pixels are 0.1 arcsecs each; images
           will be 12.8 arcsecs^2
         |       interactive=False, #turns off interactive cleaning;
           default setting
         |       niter=0) #no iterations performed

      The next example presents the typical parameters used to create a
      multi-frequency continuum image. *mode='mfs'* sets the **clean**
      algorithm for multi-frequency synthesis for wide-band, narrow
      field imaging. Continuum imaging performed on spectral windows
      (spws) containing spectral lines is accomplished with selecting
      the line-free channels using the *spw* parameter.

      .. container:: casa-input-box

         | clean(vis='example.ms',
         |       imagename='example_cont',
         |       field='0',
         |       spw='0:20~53;71~120,1:70~120,2:20~120,3:20~120', #
           selecting the line-free channels
         |       mode='mfs',
         |       threshold='0.4mJy', #sets the cleaning threshold to 0.4
           mJy (where clean will stop, typically the dirty RMS noise);
           units required
         |       niter=500, #sets maximum number of iterations; may be
           less if threshold has been reached
         |       weighting='briggs', #sets the visibility weighting to
           Briggs
         |       robust=0.0, #compromised weighting between sensitiviy
           and resolution
         |       interactive=True, #turns on interactive cleaning;
           casaviewer will be launched
         |       usescratch=False) #the model is saved in the ms header
           and the calculation of the visibilities is done on the fly
           when using calibration or plotms

      The example below presents the typical parameters used for
      cleaning spectral line channels. Using **plotms**, spectral
      featues can be identified and subsequently imaged by cleaning
      around the channel location of the desired feature. The *start*,
      *width*, and *nchan* sub-parameters allow the user to select the
      region and averaging for the output image cube.

      .. container:: casa-input-box

         | clean(vis='example.ms.contsub', #continuum-subtracted MS
         |       imagename='example_line',
         |       field='Source', #field selected by field name found in
           listobs
         |       spw='3',
         |       selectdata=True, #allows for more narrow selection of
           data for cleaning
         |       uvrange='>50km', #limits uv range of selected data from
           baselines greater than 50 km
         |       mode='channel', #clean region selected based on channel
           number
         |       start=500, #starts clean window at channel 500
         |       width=2, #averages each 2 subsequent channels together
         |       nchan=100, #cleans channels 500 to 699, averaged into
           100 channels
         |       imsize=[128,128],
         |       cell='0.1arcsec',
         |       threshold='0.0mJy',
         |       interactive=True,
         |       niter=10000,
         |       npercycle=200, #the number of iterations between each
           interactive update of the mask
         |       mask='myimage.mask') #filename for image mask

      The default *stokes* parameter only images the I polarization. For
      additional Stokes imaging, set the *stokes* parameter to the
      desired polarization (in this example, *stokes='IQUV'* for full
      Stokes imaging).

      .. container:: casa-input-box

         | clean(vis='example.pol.ms',
         |       imagename='example_StokesIQUV',
         |       cell='0.1arcsec',
         |       imsize=[250,250],
         |       psfmode='clarkstokes', #locates clean components
           independently in each stokes image
         |       stokes='IQUV', #Full Stokes
         |       interactive=True,
         |       niter=10000)

      Setting the *imagermode* parameter to 'mosaic' allows the user to
      make mosaic images of several pointings in CASA. This opens up
      several sub-parameters (*mosweight*, *ftmachine*, *scaletype*,
      *cyclefactor*, *cyclespeedup*, and *flatnoise*) associated with
      mosaicking.

      .. container:: casa-input-box

         | clean(vis='example_mosaic.ms',
         |       imagename='example_mosaic',
         |       field='', #selects all fields of the ms
         |       phasecenter='J2000 19h30m00 -40d00m00', #defines the
           phasecenter of the mosaic with J2000 coordinates
         |       mode='mfs',
         |       restfreq='345.79599GHz', #specify rest frequency to use
           for output image; Occasionally it is necessary to set this
           (e.g. some VLA spectral line data)
         |       spw='0:5~28^2', #will produce one image made with
           channels (5,7,9,...,25,27)
         |       interactive=True,
         |       imagermode='mosaic', #make a mosaic of the different
           pointings (uses csclean style too)
         |       ftmachine='ft', #ft used for pooly-sampled or irregular
           mosaics
         |       mosweight=False, #individually weight the fields of
           mosaic; useful if some fields are more sensitive
         |       scaletype='SAULT', #shows the residual with constant
           noise across the mosaic; Can also be achieved by setting
           pbcor=False
         |       cyclefactor=2.0, #controls the threshold at which the
           deconvolution cycle will pause to degrid and subtract the
           model from the visibilities
         |       cyclespeedup=3) #the major cycle threshold doubles in
           this number of iterations; can be used to speed up cleaning

      The next example addresses multi-scale cleaning in CASA, which
      allows imaging on various deconvolution scales. The *multiscale*
      parameter lets the user choose the desired scales and how many to
      include in the imaging. The sub-parameters *negcomponent* and
      *smallscalebias* allow the user to fine-tune the output.

      .. container:: casa-input-box

         | clean(vis=['example1.ms','example2.ms'], #input for multiple
           MSes
         |       imagename=['example_multiscale','outlier1'], #include
           outlier fields
         |       field='0~50',
         |       spw='0',
         |       mode ='mfs',
         |       nterms=3, #runs the MS-MFS algorithm; determined based
           on expected shape and SNR of the spectral structure
         |       reffreq='200GHz', #the reference frequency (for
           nterms>1) about which the Taylor expansion is done
         |       multiscale=[0,6,10,30], #set deconvolution scales
           (pixels); four scales including point sources
         |       negcomponent=-1, #stop cleaning if the largest scale
           finds this number of neg components
         |       smallscalebias=0.6, #a bias to give more weight toward
           smaller scales
         |       interactive=True,
         |       niter=10000)

      When imaging sufficiently large angular regions, the sky can no
      longer be treated as a two-dimensional plane and the use of the
      standard **clean**\ task will produce distortions around sources
      that become increasingly severe with increasing distance from the
      phase center. In this case, one must use a “wide-field” imaging
      algorithm such as w-projection or faceting.

      .. container:: casa-input-box

         | clean(vis='example.ms',
         |       imagename='example_widefield',
         |       outlierfile='outlier.txt', #include outlier fields in a
           text file; see 'Hints on clean with flanking fields' for
           format of file
         |       field='',
         |       spw='',
         |       mode ='mfs',
         |       imsize=[4096,4096],
         |       cell=['0.5arcsec','0.5arcsec'],
         |       gridmode='widefield', #apply corrections for
           non-coplanar effects during imaging using the W-Projection
           algorithm
         |       wprojplanes=64, #number of w-projection planes for
           convolution
         |       facets=1, #number of facets along each axis
         |       interactive=True,
         |       threshold='5e-05Jy/beam',
         |       niter=10000)

      CASA allows for the use of a model image to initialize cleaning,
      in addition to any initial model in the <imagename>.model image
      file. In this example, a single-dish (SD) image is used to help
      constrain the solutions on the short baselines for the
      interferometric data. If the SD data are in FITS file format, you
      will need to run **importfits** to convert it to an image file
      that **clean** can work with.

      .. container:: info-box

         **NOTE**: If the units in the image are Jy/beam as in a SD
         image, then it will be converted to Jy/pixel as in a model
         image, using the restoring beam in the image header and zeroing
         negatives. If the image is in Jy/pixel, then it is taken as is.

      .. container:: casa-input-box

         | clean(vis='example.ms',
         |       imagename='example_startingmodel',
         |       modelimage='example_SD.image',
         |       field='Source',
         |       spw='0',
         |       mode='velocity',
         |       start='0.0km/s',
         |       width='1.0km/s',
         |       imsize=256,
         |       cell='0.1arcsec',
         |       pbcor=True, #outputs primary beam-corrected image
           (masked outside minpb)
         |       threshold='2.0mJy',
         |       interactive=True,
         |       niter=1000)

      This task is often used used in conjunction with **feather** to
      obtain the SD zero-spacing and to conserve the flux. It is
      recommended to use the SD image as a starting model for **clean**
      and then do a feathering afterward. Although that sounds like
      inserting the SD data twice, it usually produces good results, and
      with the the SD flux being conserved. 

      .. container:: casa-input-box

         | feather(imagename='example_combined.image',
         |       highres='example_startingmodel.image',
         |       lowres='example_SD.image')

.. container:: section
   :name: viewlet-below-content-body
