.. container::
   :name: viewlet-above-content-title

Math Operations / Statistics
============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Deriving image statistics and performing mathematical operations on
   images

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Mathematical operations on images are typically completed using
      the CASA task
      `immath <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_immath>`__,
      and image statistics may be derived using the CASA tasks
      `imstat <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_imstat>`__
      and
      `imdev <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_imdev>`__.
      Here, we give an overview of how these tasks are used.

      .. rubric:: 
         Mathematical Operations on Images (**immath**)
         :name: mathematical-operations-on-images-immath

      The CASA task **immath** is useful for performing mathematical
      operations on images and on specific channels within images,
      including e.g. addition or subtraction of two cubes, squaring an
      image, computing a spectral index, and determining polarization
      angles and intensities. The inputs are:

      .. container:: casa-input-box

         | #  immath :: Perform math operations on images
         | imagename           =         ''        #  a list of input
           images
         | mode                = 'evalexpr'        #  mode for math
           operation (evalexpr, spix, pola, poli)
         |      expr           =         ''        #  Mathematical
           expression using images
         |      varnames       =         ''        #  a list of variable
           names to use with the image files
         | outfile             = 'immath_results.im' #  File where the
           output is saved
         | mask                =         ''        #  Mask to use.
           Default is none.
         | region              =         ''        #  Region selection. 
         |                                         #   Default is to use
           the full image.
         | box                 =         ''        #  Rectangular region
           to
         |                                         #   select in
           direction plane.
         |                                         #    Default is to
           use the
         |                                         #   entire direction
           plane.
         | chans               =         ''        #  Channels to use. 
         |                                         #   Default is to use
           all channels.
         | stokes              =         ''        #  Stokes planes to
           use. 
         |                                         #   Default is to use
           all Stokes planes.
         | imagemd             =         ''        #  An image name from
           which metadata should be copied. The input
         |                                         #   can be either an
           image listed under imagename or any other
         |                                         #   image on disk.
           Leaving this parameter unset may copy header
         |                                         #   metadata from any
           of the input images, which
         |                                         #   one is not
           guaranteed.

      .. container:: alert-box

         **Alert:** **immath** does not convert any brightness units,
         e.g. from Jy/beam to K or vice versa. The user is responsible
         for making sure the images are consistent with the values in
         the header and the image. It is not advisable to mix input
         images that are in different units or have different beam
         sizes.

      The *imagename* parameter must be given the name of a single image
      as a string (e.g. *imagename='image1.im'*) or the names of
      multiple images in a list of strings
      (e.g. *imagename=['image1.im', 'image2.im']* ). The **immath**
      task outputs an image file, and the name of the output file is
      specified using the *outfile* parameter.

      The *mode* parameter selects what **immath** is to do. The
      default, *mode='evalexpr'*, allows the user to specify a
      mathematical operation to execute on the input images through the
      *expr* sub-parameter. The mathematical expression is specified in
      *expr* as a Lattice Expression Language (LEL) string (see the
      `page on LEL
      strings <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel>`__).
      The standard usage for *mode='evalexpr'* is to input a list of
      images into the *imagename* parameter, and then refer to them in
      the *expr* subparameter in LEL by the names IM0, IM1, ....  For
      example,

      .. container:: casa-input-box

         immath(imagename=['image1.im','image2.im'],expr='IM0-IM1',outfile='ImageDiff.im')

      would subtract the second image given from the first.

      For the special modes '*spix'*, '*pola'*, and '*poli'*, the images
      required for the operation may need to be listed in *imagename* in
      a particular order. See examples of usage for polarization data
      below, paying particular attention to posted alerts.

      The mathematical expression can be computed on the entire image
      cube, or on selected regions and image planes, which can be
      specified through the *mask*, *region*, *box*, *chans*, and
      *stokes* parameters. Mask specification is done using the *mask*
      parameter which can optionally contain an on-the-fly mask
      expression (in
      `LEL <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/lattice-expression-language-lel>`__)
      or point to an image with a pixel mask. In some cases, one may
      like to use a flat image (e.g. a moment image) mask applied to an
      entire cube. The *stretch=True* subparameter in *mask* allows one
      to expand the mask to all planes (i.e. channels or Stokes planes)
      of the cube. Region selection can also be carried out through the
      *region* parameter (see the pages on `Region
      Files <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files>`__
      and `Region File
      Format <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-file-format>`__)
      and *box* parameter, while image plane selection is controlled by
      *chans* and *stokes* parameters.

      The image metadata in the output file is adopted from another
      image, which can be specified through the *imagemd* parameter. In
      *imagemd*, input the name of the image from which the metadata
      should be copied and used for the output image. If left blank, the
      task may pick any of the input image headers, so it is better to
      define this parameter. In fact, the image specified in *imagemd*
      can be any image, even an image that is not part of the
      calculations in **immath**.

      Detailed examples of **immath** usage are given below.

      .. rubric:: 
         Examples for **immath**
         :name: examples-for-immath

      In the following, we show a examples of **immath** usage. Note
      that the image names in the *expr* are assumed to refer to
      existing image files in the current working directory.

       

      .. rubric:: Simple math
         :name: simple-math

      Select a single plane (channel 22) of the 3-D cube:

      .. container:: casa-input-box

         | immath(imagename='ngc5921.demo.cleanimg.image',
         |        expr='IM0',chans='22',
         |        outfile='ngc5921.demo.chan22.image')

      Double all values in our image:

      .. container:: casa-input-box

         | immath(imagename=['ngc5921.demo.chan22.image'],
         |        expr='IM0*2.0',
         |        outfile='ngc5921.demo.chan22double.image' )

      Square all values in our image:

      .. container:: casa-input-box

         | immath(imagename=['ngc5921.demo.chan22.image'],
         |        expr='IM0^2',
         |        outfile='ngc5921.demo.chan22squared.image' )

      .. container:: info-box

         **NOTE**: The units in the output image are still claimed to be
         “Jy/beam”, i.e. **immath** will not correctly scale the units
         in the image for non-linear cases like this. Beware!

      Subtract our image containing channel 22 from the original 3-D
      cube.  Note that in this example, the 2-D plane (channel 22) is
      extended into the third dimension, so that che channel 22 image is
      subtracted from each plane in the 3-D cube:

      .. container:: casa-input-box

         | immath(imagename=['ngc5921.demo.cleanimg.image','ngc5921.demo.chan22.image'],
         |        expr='IM0-IM1',
         |        outfile='ngc5921.demo.sub22.image')

      Divide an image by another, with a threshold on one of the images:

      .. container:: casa-input-box

         | immath(imagename=['ngc5921.demo.cleanimg.image','ngc5921.demo.chan22.image'],
         |        expr='IM0/IM1[IM1>0.008]',
         |        outfile='ngc5921.demo.div22.image')

      You can do other mathematical operations on an image (e.g.
      trigonometric functions), as well as use scalar results from an
      image (e.g. *max, min, median, mean, variance*) in **immath**. You
      also have access to constants such as *e()* and *pi()*. As an
      example, the following expression uses the *sine* function, square
      root (sqrt), a scalar function (max), and the constant *pi* :

      .. container:: casa-input-box

         | immath(imagename=['ngc5921.demo.chan22.image','ngc5921.demo.chan22squared.image'],
         |        expr='sin(float(pi())*IM0/sqrt(max(IM1)))',
         |        outfile='ngc5921.demo.chan22sine.image')

      .. container:: info-box

         **NOTE**: Once again, the units in the output image are still
         claimed to be “Jy/beam”, i.e. **immath** will not correctly
         scale the units in the image for non-linear cases like this.
         Beware!

       

      .. rubric:: Region and Channel Selection
         :name: region-and-channel-selection

      Select and save a region including the inner 1/4 of an image for
      channels 0 through 9 (*chans='<10'*) and channels 40, 42, and 44:

      .. container:: casa-input-box

         | default('immath')
         | imagename=['ngc5921.demo.cleanimg.image']
         | expr='IM0'
         | region='box[[64pix,64pix],[192pix,192pix]]'
         | chans='<10;40,42,44'
         | outfile='ngc5921.demo.inner.image'
         | immath()

      If more than one channel is specified in the *chans* parameter,
      then the output image will contain multiple channels spanning the
      range from the lowest channel specified to the highest. In the
      example above, the output image will span channels 0 through 44,
      for a total of 45 channels. The channels that were not selected
      (in this case, channels 10 through 39 and channels 41 and 43) will
      be masked in the output cube. If we had set *chans='40,42,44'*
      then there would be 5 output channels corresponding to channels
      40, 41, 42, 43, and 44 of the MS with 41 and 43 masked.

      Note that the *chans* syntax allows the operators '<', '<=', '>',
      and '>'. For example, the following two inputs select the same
      channels.

      .. container:: casa-input-box

         | chans = '<17,>79'
         | chans = '<=16,>=80'

      .. rubric::  
         :name: section

      .. rubric:: Polarization manipulation
         :name: polarization-manipulation

      Extract each Stokes plane from a cube into an individual image:

      .. container:: casa-input-box

         | default('immath')
         | imagename = '3C129BC.clean.image'
         | outfile='3C129BC.I'; expr='IM0'; stokes='I'; immath();
         | outfile='3C129BC.Q'; expr='IM0'; stokes='Q'; immath();
         | outfile='3C129BC.U'; expr='IM0'; stokes='U'; immath();
         | outfile='3C129BC.V'; expr='IM0'; stokes='V'; immath();

      Extract linearly polarized intensity and polarization position
      angle images:

      .. container:: casa-input-box

         | immath(stokes='', outfile='3C129BC.P', mode='poli',
         |        imagename=['3C129BC.Q','3C129BC.U'],
           sigma='0.0mJy/beam');
         | immath(stokes='', outfile='3C129BC.X', mode='pola',
         |        imagename=['3C129BC.Q','3C129BC.U'],
           sigma='0.0mJy/beam');

      .. container:: alert-box

         **ALERT:** For *mode=’pola’* you MUST call as a function as in
         this example (giving the parameters as arguments) or **immath**
         will fail.

      Create a fractional linear polarization image:

      .. container:: casa-input-box

         | default( 'immath')
         | imagename = ['3C129BC.I','3C129BC.Q','3C129BC.U']
         | outfile='3C129BC.fractional_linpol'
         | expr='sqrt((IM1^2 + IM2^2)/IM0^2)'
         | stokes=''
         | immath()

      Create a polarized intensity image:

      .. container:: casa-input-box

         | default( 'immath')
         | imagename = ['3C129BC.Q','3C129BC.U','3C129BC.V']
         | outfile='3C129BC.pol_intensity'
         | expr='sqrt(IM0^2 + IM1^2 + IM2^2)'
         | stokes=''
         | immath()

      Toolkit Tricks: The following uses the toolkit. You can make a
      complex linear polarization (Q+iU) image using the **imagepol**
      tool:

      .. container:: casa-input-box

         |   # Make an imagepol tool and open the clean image
         |   potool = casac.homefinder.find_home_by_name('imagepolHome')
         |   po = potool.create()
         |   po.open('3C129BC.clean.image')
         |   # Use complexlinpol to make a Q+iU image
         |   po.complexlinpol('3C129BC.cmplxlinpol')
         |   po.close()

      You can now display this in the **viewer**, in particular overlay
      this over the intensity raster with the intensity contours. When
      you load the image, use the LEL:

      .. container:: casa-input-box

           '3C129BC.cmplxlinpol'['3C129BC.P'>0.0001]

      which is entered into the LEL box at the bottom of the Load Data
      menu.

       

      .. rubric:: Using Masks in **immath**
         :name: using-masks-in-immath

      | The *mask* parameter is used inside **immath** to apply a mask
        to all the images used in *expr* before calculations are done
        (if you are curious, it uses the **ia.subimage** tool method to
        make virtual images that are then input in the LEL to the
        **ia.imagecalc** method).
      | For example, let’s assume that we have made a single channel
        image using **clean:**

      .. container:: casa-input-box

         | default('clean')
         |  
         | vis = 'ngc5921.demo.src.split.ms.contsub'
         | imagename = 'ngc5921.demo.chan22.cleanimg'
         | mode = 'channel'
         | nchan = 1
         | start = 22
         | step = 1
         |  
         | field = ''
         | spw = ''
         | imsize = [256,256]
         | cell = [15.,15.]
         | psfalg = 'clark'
         | gain = 0.1
         | niter = 6000
         | threshold='8.0mJy'
         | weighting = 'briggs'
         | rmode = 'norm'
         | robust = 0.5
         | mask = [108,108,148,148]
         |  
         | clean()

      There is now a file ngc5921.demo.chan22.cleanimg.mask that is an
      image with values 1.0 inside the cleanbox region and 0.0 outside.
      We can use this to mask the clean image:

      .. container:: casa-input-box

         | default('immath')
         | imagename = 'ngc5921.demo.chan22.cleanimg.image'
         | expr='IM0'
         | mask='"ngc5921.demo.chan22.cleanimg.mask">0.5'
         | outfile='ngc5921.demo.chan22.cleanimg.imasked'
         | immath()

      Toolkit Tricks: Note that there are also pixel masks that can be
      contained in each image. These are Boolean masks, and are
      implicitly used in the calculation for each image in *expr*. If
      you want to use the mask in a different image not in *expr*, try
      it in *mask*:

      .. container:: casa-input-box

         | # First make a pixel mask inside
           ngc5921.demo.chan22.cleanimg.mask
         | ia.open('ngc5921.demo.chan22.cleanimg.mask')
         | ia.calcmask('"ngc5921.demo.chan22.cleanimg.mask">0.5')
         | ia.summary()
         | ia.close()
         | # There is now a 'mask0' mask in this image as reported by
           the summary
         | # Now apply this pixel mask in immath
         | default('immath')
         | imagename='ngc5921.demo.chan22.cleanimg.image'
         | expr='IM0'
         | mask='mask(ngc5921.demo.chan22.cleanimg.mask)'
         | outfile='ngc5921.demo.chan22.cleanimg.imasked1'
         | immath()

      Note that nominally the axes of the mask must be congruent to the
      axes of the images in *expr*. However, one exception is that the
      image in mask can have fewer axes (but not axes that exist but are
      of the wrong lengths). In this case, **immath** will extend the
      missing axes to cover the range in the images in *expr*. Thus, you
      can apply a mask made from a single channel to a whole cube.

      .. container:: casa-input-box

         | # drop degenerate stokes and freq axes from mask image
         | ia.open('ngc5921.demo.chan22.cleanimg.mask')
         | im2 =
           ia.subimage(outfile='ngc5921.demo.chan22.cleanimg.mymask',dropdeg=True)
         | im2.summary()
         | im2.close()
         | ia.close()
         | # mymask has only RA and Dec axes
         | # Now apply this mask to the whole cube
         | default('immath')
         | imagename='ngc5921.demo.cleanimg.image'
         | expr='IM0'
         | mask='"ngc5921.demo.chan22.cleanimg.mymask">0.5'
         | outfile='ngc5921.demo.cleanimg.imasked'
         | immath()

      .. rubric::  
         :name: section-1

      .. rubric:: Computing Image Statistics (**imstat**)
         :name: computing-image-statistics-imstat

      The **imstat** task will calculate statistics on a region of an
      image and return the results as a value in a Python dictionary.
      The inputs are:

      .. container:: casa-input-box

         | #  imstat :: Displays statistical information from an image
           or image region
         | imagename           =         ''        #  Name of the input
           image.
         | axes                =         -1        #  List of axes to
           evaluate statistics over. Default is
         |                                         #   all axes.
         | region              =         ''        #  Image Region or
           name. Use Viewer.
         | box                 =         ''        #  Select one or more
           box regions.
         | chans               =         ''        #  Select the
           channel(spectral) range. 
         | stokes              =         ''        #  Stokes params to
           image (I,IV,IQU,IQUV). Default '' =>
         |                                         #   include all
         | listit              =       True        #  Print stats and
           bounding box to logger?
         | verbose             =      False        #  Print additional
           messages to logger?
         | mask                =         ''        #  Mask to use.
           Default is none.
         | logfile             =         ''        #  Name of file to
           write fit results.
         | algorithm           =  'classic'        #  Algorithm to use.
           Supported values are 'chauvenet',
         |                                         #   'classic',
           'fit-half', and 'hinges-fences'. Minimum
         |                                         #   match is
           supported.
         |      clmethod       =     'auto'        #  Method to use for
           calculating classical statistics.
         |                                         #   Supported methods
           are 'auto', 'tiled', and
         |                                         #   'framework'.
           Ignored if algorithm is not 'classic'.

      | Area selection can be done using *region* and *mask* parameters.
        Plane selection is controlled by *chans* and *stokes*. The
        parameter *axes* will select the dimensions that the statistics
        are calculated over. Typical data cubes have axes like: RA axis
        0, DEC axis 1, Velocity axis 2. So, e.g. *axes=[0,1]* would be
        the most common setting to calculate statistics per spectral
        channel.
      | A typical output of **imstat** on a cube with *axes=[0,1]* and
        *algorithm='classic'* (default) looks like:

      .. container:: casa-output-box

         | No region specified. Using full positional plane.
         | Using all spectral channels.
         | Using polarizations ALL
         | Determining stats for image IRC10216_HC3N.cube_r0.5.image
         | Set region from supplied region record
         | Statistics calculated using Classic algorithm
         | Regions ---
         |          -- bottom-left corner (pixel) [blc]:  [0, 0, 0, 0]
         |          -- top-right corner (pixel) [trc]:    [299, 299, 0,
           63]
         |          -- bottom-left corner (world) [blcf]: 09:48:01.492,
           +13.15.40.658, I, 3.63994e+10Hz
         |          -- top-right corner (world) [trcf]:   09:47:53.299,
           +13.17.40.258, I, 3.63915e+10Hz
         | No region specified. Using full positional plane.
         | Using all spectral channels.
         | Using polarizations ALL
         | Selected bounding box :
         |     [0, 0, 0, 0] to [299, 299, 0, 63]  (09:48:01.492,
           +13.15.40.658, I, 3.63994e+10Hz to 09:47:53.299,
           +13.17.40.258, I, 3.63915e+10Hz)
         | #        Frequency  Frequency(Plane) Npts         
           Sum           Mean          Rms           Std dev      
           Minimum       Maximum     
         |   3.63993552e+10                  0  9.000000e+04 
           0.000000e+00  0.000000e+00  0.000000e+00  0.000000e+00 
           0.000000e+00  0.000000e+00
         |   3.63992302e+10                  1  9.000000e+04 
           0.000000e+00  0.000000e+00  0.000000e+00  0.000000e+00 
           0.000000e+00  0.000000e+00
         |   3.63991052e+10                  2  9.000000e+04 
           0.000000e+00  0.000000e+00  0.000000e+00  0.000000e+00 
           0.000000e+00  0.000000e+00
         |   3.63989802e+10                  3  9.000000e+04 
           0.000000e+00  0.000000e+00  0.000000e+00  0.000000e+00 
           0.000000e+00  0.000000e+00
         |   3.63988551e+10                  4  9.000000e+04 
           0.000000e+00  0.000000e+00  0.000000e+00  0.000000e+00 
           0.000000e+00  0.000000e+00
         |   3.63987301e+10                  5  9.000000e+04 
           6.069948e-01  6.744386e-06  1.534640e-03  1.534634e-03
           -6.355108e-03  6.166496e-03
         |   3.63986051e+10                  6  9.000000e+04 
           2.711720e-01  3.013023e-06  1.538071e-03  1.538077e-03
           -6.165663e-03  5.862981e-03
         |   3.63984801e+10                  7  9.000000e+04 
           2.501259e-01  2.779177e-06  1.578049e-03  1.578056e-03
           -6.771976e-03  6.272645e-03
         |   3.63983551e+10                  8  9.000000e+04
           -3.706732e-01 -4.118591e-06  1.607191e-03  1.607194e-03
           -8.871284e-03  6.591001e-03

      | where the header information provides the specifications of the
        data that were selected followed by the table with the frequency
        values of the planes, the plane numbers, Npts (the number of
        pixels per plane), and the Sum, Median, RMS, Standard
        deviations, Minimum, and Maximum of the pixel values for each
        plane. Similar output is provided when the data is averaged over
        different axes. The logger output can also be written into or
        appended to a log file for further processing elsewhere
        (*logfile* parameter).
      | **imstat** has access to different statistics algorithms. Most
        of them represent different ways on how to treat distributions
        that are not Gaussian, in particular to eliminate outlier values
        from the statistics. Available algorithms are CLASSIC, where all
        unmasked pixels are used, FIT-HALF, where one (good) half of the
        distribution is being mirrored across a central value,
        HINGES-FENCES, where the inner quartiles plus a ’fence’ data
        portion is being used, and CHAUVENET, which includes values
        based on the number of standard deviations from the mean. For
        more information, see the inline help of the **imstat** task.

      .. rubric:: 
         Using the task return value
         :name: using-the-task-return-value

      The contents of the return value of **imstat** are in a Python
      dictionary of key-value sets. For example,

      .. container:: casa-input-box

         xstat = imstat()

      | will assign this to the Python variable xstat. The keys for
        xstat are outlined on the **imstat** page.
      | For example, an **imstat** call might be

      .. container:: casa-input-box

         |  default('imstat')
         |  imagename = 'ngc5921.demo.cleanimg.image'  #  The NGC5921
           image cube
         |  box       = '108,108,148,148'              #  20 pixels
           around the center
         |  chans     = '21'                           #  channel 21
         |  xstat = imstat()

      In the terminal window, **imstat** reports:

      .. container:: casa-output-box

         | Statistics on  ngc5921.usecase.clean.image
         | Region ---
         |    -- bottom-left corner (pixel) [blc]: [108, 108, 0, 21]
         |    -- top-right corner (pixel) [trc]:   [148, 148, 0, 21]
         |    -- bottom-left corner (world) [blcf]: 15:22:20.076,
           +04.58.59.981, I, 1.41332e+09Hz
         |    -- top-right corner( world) [trcf]: 15:21:39.919,
           +05.08.59.981, I, 1.41332e+09Hz
         | Values --
         |    -- flux [flux]:              0.111799236126
         |    -- number of points [npts]:  1681.0
         |    -- maximum value [max]:      0.029451508075
         |    -- minimum value [min]:     -0.00612453464419
         |    -- position of max value (pixel) [maxpos]:  [124, 131, 0,
           21]
         |    -- position of min value (pixel) [minpos]:  [142, 110, 0,
           21]
         |    -- position of max value (world) [maxposf]: 15:22:04.016,
           +05.04.44.999, I, 1.41332e+09Hz
         |    -- position of min value (world) [minposf]: 15:21:45.947,
           +04.59.29.990, I, 1.41332e+09Hz
         |    -- Sum of pixel values [sum]: 1.32267159822
         |    -- Sum of squared pixel values [sumsq]: 0.0284534543692
         |    
         | Statistics ---
         |    -- Mean of the pixel values [mean]:      
           0.000786836167885
         |    -- Standard deviation of the Mean [sigma]:
           0.00403944306904
         |    -- Root mean square [rms]:               0.00411418313161
         |    -- Median of the pixel values [median]:    
           0.000137259965413
         |    -- Median of the deviations [medabsdevmed]:      
           0.00152346317191
         |    -- Quartile [quartile]:                      
           0.00305395200849

      The return value in xstat is

      .. container:: casa-output-box

         | CASA <152>: xstat
         |   Out[152]:
         | {'blc': array([108, 108,   0,  21]),
         |  'blcf': '15:22:20.076, +04.58.59.981, I, 1.41332e+09Hz',
         |  'flux': array([ 0.11179924]),
         |  'max': array([ 0.02945151]),
         |  'maxpos': array([124, 131,   0,  21]),
         |  'maxposf': '15:22:04.016, +05.04.44.999, I, 1.41332e+09Hz',
         |  'mean': array([ 0.00078684]),
         |  'medabsdevmed': array([ 0.00152346]),
         |  'median': array([ 0.00013726]),
         |  'min': array([-0.00612453]),
         |  'minpos': array([142, 110,   0,  21]),
         |  'minposf': '15:21:45.947, +04.59.29.990, I, 1.41332e+09Hz',
         |  'npts': array([ 1681.]),
         |  'quartile': array([ 0.00305395]),
         |  'rms': array([ 0.00411418]),
         |  'sigma': array([ 0.00403944]),
         |  'sum': array([ 1.3226716]),
         |  'sumsq': array([ 0.02845345]),
         |  'trc': array([148, 148,   0,  21]),
         |  'trcf': '15:21:39.919, +05.08.59.981, I, 1.41332e+09Hz'}

      .. container:: alert-box

         **ALERT:** The return dictionary currently includes NumPy array
         values, which have to be accessed by an array index to get the
         array value. To access these dictionary elements, use the
         standard Python dictionary syntax, e.g. xstat[<key
         string>][<array index>]

      For example, to extract the standard deviation as a number

      .. container:: casa-input-box

         | mystddev = xstat['sigma'][0]
         | print 'Sigma = '+str(xstat['sigma'][0])

      .. rubric:: 
         Examples for **imstat**
         :name: examples-for-imstat

      To extract statistics for an image:

      .. container:: casa-input-box

         | xstat = imstat('b1608.demo.clean2.image')
         | # Printing out some of these
         |   print 'Max   = '+str(xstat['max'][0])
         |   print 'Sigma = '+str(xstat['sigma'][0])
         | # results:
         | # Max   = 0.016796965152
         | # Sigma = 0.00033631979385

      In a box around the brightest component:

      .. container:: casa-input-box

         | xstat_A =
           imstat('b1608.demo.clean2.image',box='124,125,132,133')
         | # Printing out some of these
         |   print 'Comp A Max Flux = '+str(xstat_A['max'][0])
         |   print 'Comp A Max X,Y  =
           ('+str(xstat_A['maxpos'][0])+','+str(xstat_A['maxpos'][1])+')'
         | # results:
         | # Comp A Max Flux = 0.016796965152
         | # Comp A Max X,Y  = (128,129)

       

      .. rubric:: Computing a *Deviation* Image (**imdev**)
         :name: computing-a-deviation-image-imdev

      The **imdev** task produces an output image whose value in each
      pixel represents the "error" or "deviation" in the input image at
      the corresponding pixel. The output image has the same dimensions
      and coordinate system as the input image, or as the selected
      region of the input image. The inputs are:

      .. container:: casa-input-box

         | # imdev :: Create an image that can represent the statistical
           deviations of the input image.
         | imagename          =          ''        # Input image name
         | outfile            =          ''        # Output image file
           name. If left blank (the default), no
         |                                         #   image is written
           but a new image tool referencing
         |                                         #   the collapsed
           image is returned.
         | region             =          ''        # Region selection.
           Default is to use the full image.
         | box                =          ''        # Rectangular
           region(s) to select in direction plane.
         |                                         #   Default is to use
           the entire direction plane.
         | chans              =          ''        # Channels to use.
           Default is to use all channels.
         | stokes             =          ''        # Stokes planes to
           use. Default is to use all Stokes planes.
         | mask               =          ''        # Mask to use.
           Default setting is none.
         | overwrite          =       False        # Overwrite
           (unprompted) pre-existing output file? Ignored
         |                                         #   if "outfile" is
           left blank.
         | grid               =      [1, 1]        # x,y grid spacing.
           Array of exactly two positive integers.
         | anchor             =       'ref'        # x,y anchor pixel
           location. Either "ref" to use the image
         |                                         # exactly two
           integers.
         | xlength            =      '1pix'        # Either x coordinate
           length of box, or diameter of circle.
         |                                         #   Circle is used if
           ylength is a reference pixel or an
         |                                         #   empty string.
         | ylength            =      '1pix'        # y coordinate length
           of box. Use a circle if ylength is
         |                                         #   an empty string.
         | interp             =     'cubic'        # Interpolation
           algorithm to use. Can be "nearest", "linear",
         |                                         #   "cubic", or
           "lanczos". Minimum match supported.
         | stattype           =     'sigma'        # Statistic to
           compute. See below for the list of supported
         |                                         #   statistics.
         | statalg            =   'classic'        # Statistics
           computation algorithm to use. Supported values
         |                                         #   are "chauvenet"
           and "classic". Minimum match is supported.

      Area selection can be done using the *region* and *mask*
      parameters. Plane selection is controlled by the *chans* and
      *stokes* parameters. Statistics are computed spatially: a
      deviation image is computed independently for each channel/Stokes
      plane. If the *outfile* parameter is left blank, the task returns
      an image tool referencing the resulting image; otherwise the
      resulting image is written to disk.

      The statistic to be computed is selected using the *stattype*
      parameter. Allowed statistics are:

      .. container::

         .. container:: casa-input-box

            | iqr                      inner quartile range (q3 - q1)
            | max                      maximum
            | mean                     mean
            | medabsdevmed, madm       median absolute deviation from
              the median
            | median                   median
            | min                      minimum
            | npts                     number of points
            | q1                       first quartile
            | q3                       third quartile
            | rms                      rms
            | sigma, std               standard deviation
            | sumsq                    sum of squares
            | sum                      sum
            | var                      variance
            | xmadm                    median absolute deviation from
              the median multipied by x, where x is the
            |                          reciprocal of Phi^-1(3/4),where
              Phi^-1 is the reciprocal of the quantile
            |                          function. Numerically, x =
              1.482602218505602. See, eg,
            |                         
              https://en.wikipedia.org/wiki/Median_absolute_deviation#Relation_to_standard_deviation

      The chosen statistic is calculated around a set of grid points
      (pixels) across the input image with grid spacing specified by the
      *grid* parameter. The size and shape of the region used to compute
      the statistic at each grid point is specified by the *xlength* and
      *ylength* parameters. If *ylength* is an empty string, then the
      region used is a circle centered on each grid point with diameter
      provided by *xlength*. Otherwise, a rectangular region with
      dimensions of *xlength* by *ylength* is used. These two parameters
      may be specified as valid quantities with recognized units (e.g.,
      "4arcsec" or "4pix"). They may also be specified as numerical
      values, in which case the unit is assumed to be pixels.

      The chosen statistic is calculated at every grid point in the
      input image, and the result is reflected at the corresponding
      pixel of the output image. Values at all other pixels in the
      output image are determined by interpolating across the grid
      points using the interpolation scheme given by the input parameter
      *interp*. The *statalg* parameter specifies the algorithm for the
      statistics computation. Available algorithms are CLASSIC, where
      all unmasked pixels are used, and CHAUVENET, which includes values
      based on the number of standard deviations from the mean.

      .. rubric:: Examples for **imdev**
         :name: examples-for-imdev

      Compute a "standard deviation" image using grid-spacing of 4
      arcsec in the X direction and 5 arcsec in the Y direction, with
      linear interpolation to compute values at non-grid-pixels. Compute
      the standard deviation in a box of 20 x 25 arcsec.

      .. container::

         .. container:: casa-input-box

            | imdev("my.image", "std.image", grid=[4,5],
              xlength="20arcsec", ylength="25arcsec",
            |        stattype="sigma", interp="linear",
              statalg="classic")

      Compute an image showing median absolute deviation (MAD) across
      the image, with MAD converted to an equivalent RMS value. Anchor
      the grid at a specific pixel [1000,1000] with grid-spacing of 10
      pixels, and use circles of diameter 30 pixels for the statistical
      computation. Calculate the statistic using the z-score/Chauvenet
      algorithm by fixing the maximum z-score to determine outliers to
      5. Use cubic interpolation to determine the value at
      non-grid-pixels. Have the task return a pointer to the output
      image.

      .. container::

         .. container:: casa-input-box

            | myim = imdev("my.image", anchor=[1000,1000], grid=[10,10],
              xlength=30, ylength='',
            |        stattype="xmadm", interp="cubic",
              statalg="chauvenet", zscore=5)

.. container:: section
   :name: viewlet-below-content-body
