

.. _Description:

Description
   This task evaluates mathematical expressions involving existing
   image files. The results of the calculations are stored in the 
   designated output file. The available options are 1) specify a
   mathematical expression directly, 2) use a pre-defined expression
   for calculation of spectral index image, polarization intensity,
   or position angle images. Image file names are specified in
   *imagename*, and by default the variables IM0, IM1, ... are used
   to represent these files in the expression. For option1 (*mode =
   'evalexpr'*) explicit notations of file names in the expression
   are also supported, in which cases the file names must be enclosed
   in double quotes (") and *imagename* is ignored. The image files
   names may be CASA images or FITS images.
   
   .. note:: NOTE: Index values start at 0; use the **imhead** task to see
      the range of index values for each axes.
   
   If the mask has fewer dimensions than the image and if the shape
   of the dimensions the mask and image have in common are the same,
   the mask will automatically have the missing dimensions added so
   it conforms to the image.
   
   For a full description of the allowed syntax and examples, see the
   LEL pages in the `Image
   Analysis <../../notebooks/image_analysis.ipynb>`__
   chapter.
   
   .. note:: NOTE: where indexing and axis numbering are used in the above
      functions they are 1-based, ie. numbering starts at 1.
   
   If *stretch* is true and if the number of mask dimensions is less
   than or equal to the number of image dimensions and some axes in
   the mask are degenerate while the corresponding axes in the image
   are not, the mask will be stetched in the degenerate axis
   dimensions. For example, if the input image has shape [100, 200,
   10] and the input mask has shape [100, 200, 1] and stretch is
   true, the mask will be stretched along the third dimension to
   shape [100, 200, 10]. However if the mask is shape [100, 200, 2],
   stretching is not possible and an error will result.
   
   .. warning:: **WARNING**: for a mathematical expression that involves
      multiple images (e.g., subtracting one image from the other),
      it is good to realize that the algorithm is pixel-based. This
      means that it is up to the user to put the images on the same
      dimensions for all relevant axes (e.g., RA and dec). Where
      needed, use **imregrid** before using **immath** to ensure the
      image dimensions on the relevant axes are the same.

   
   .. rubric:: NOTES ON MODES OF OPERATION ('MODE')

   The supported modes of operation are *mode=‘evalexpr'* (evaluate
   an LEL expression), *'spix'* (spectral index computation, although
   see also task **spxfit** for a more robust algorithm), *'pola'*
   (polarization angle), and *'poli'* (total polarization intensity).
   
   Mode 'evalexpr' supports (mixtures of) images with float, double,
   complex-float, and complex-double precision pixels (although .
   Modes 'pola' and 'poli' only support images with float precision
   pixels. Mode 'spix' only supports images with real valued pixels.

   
   .. rubric:: NOTES ON *MODE='POLA'*
   
   The *mode='pola'* option creates an image of the polarization
   angle;
   
   :math:`\theta = {1\over{2}}\,tan^{-1}(U/Q)`
   
   If *polithresh* is set to a value, e.g. ’30uJy/beam’, a mask
   (’ *mask0* ’) is written to the output image and is False for
   all corresponding linear polarization values below this threshold.
   This parameter overrides the input parameter *mask*. Default (’’)
   means use the value given in *mask*, or no masking if that value
   is empty as well.

   
   .. rubric:: NOTES ON *MODE='POLI', MODE='TPOLI', AND MODE='LPOLI'*
   
   The *mode='poli'* option creates an image of the total polarized
   intensity using all of the linear and circular polarizations
   available in the input image(s);
   
   :math:`\sqrt{( Q^2+ U^2+ V^2)}`.
   
   If the input image(s) contains only Q and U, or only V, then just
   those components contribute to the total polarized intensity. 
   
   Note that this mode is flexible and will fall back to '*tpoli*'
   when Stokes V is provided and '*lpoli*' when Stokes V is not
   available; these modes are described below.
   
   The polarized intensity may optionally be debiased (if *sigma* >
   0). This requires an estimate of the thermal noise level
   (:math:`\sigma`). The resulting image will be computed using
   
   :math:`\sqrt{( Q^2 + U^2 + V^2 - \sigma^2)}`
   
   In the output image, pixels for which the expression inside the
   square root is negative are masked, and their values are set to
   zero. Note that the **imagepol** tool method **po.totpolint** also
   performs this computation (in fact it's what immath calls under
   the hood in this case), with the added feature that an estimate of
   sigma can be computed on the fly (see the relevant `tool method
   help <../../api/casatools.rst>`__
   for details).
   
   When using a multi-Stokes input image, the modes *'tpoli'* and
   *'lpoli'* can be used to control which polarizations are used in
   the calculation:
   
   The *mode='tpoli'* option will calculate a total polarization
   intensity image;
   
   :math:`\sqrt{( Q^2+ U^2+ V^2)}`. 
   
   The task requires all three Stokes image planes to be present. 
   
   The *mode='lpoli'* option will calculate a linear polarization
   intensity image;
   
   :math:`\sqrt{( Q^2+ U^2)}`.
   
   Only the Q and U Stokes image planes are required to be present.
   If Stokes V is present it will be ignored. 
   

   .. rubric:: NOTES ON *MODE='SPIX'*
   
   This mode computes the spectral index using two images of
   different frequencies. The spectral index is defined as
   
   :math:`\alpha = ln(I_0/I_1)/ln(\nu_0/\nu_1)`
   
   where the :math:`I`'s are the pixel values and the
   :math:`\nu`'s are the frequencies of the two images.
   
   If exactly two images aren't supplied, an exception will result.
   This mode is equivalent to specifying mode='evalexpr' and
   expr='spectralindex(IM0, IM1)'. Both images must have spectral
   axes. If both images have multiple channels, they must have the
   same number of channels. In that case, the pixel values of the
   i :math:`^{th}` plane in the output image will be computed
   using the the i :math:`^{th}` plane pixel values and the
   i :math:`^ith` plane frequencies of the input images.
   Alternatively, one image can have :math:`n>1` channels and the
   other can have a single channel, in which case the output image
   will have :math:`n` channels with the i :math:`^{th}` plane
   pixel values being the result of the i :math:`^{th}` plane
   pixel values and i :math:`^{th}` plane frequency of the
   multi-channel image and the pixel values and fequency of the
   single channel image. If corresponding pixels in the two input
   images do not have the same sign, the corresponding output pixel
   will have a value of :math:`nan`.

   
   .. rubric:: NOTES ON PREC PARAMETER WITH MODE='EVALEXPR' AND 'SPIX'
   
   The prec parameter indicates what the precision of the pixel
   values of the output image should be. Float is the default. For
   mode='evalexpr', the domain (real or complex) of the output image
   pixels is determined from the specified lattice expression. For
   mode='spix', only real valued images are supported and the output
   image will also have real valued pixels.
   
   .. rubric:: CAUTIONS REGARDING OUTPUT IMAGE METADATA
   
   EXCEPT IN THE EXAMPLES GIVEN HERE, THIS APPLICATION MAKES NO
   ATTEMPT TO DETERMINE WHAT THE CORRECT BRIGHTNESS UNIT OF THE
   OUTPUT IMAGE SHOULD BE. THIS RESPONSIBILITY LIES SOLELY WITH THE
   USER. The brightness unit of the output image can be modified
   using tool method **ia.setbrightnessunit** or task **imhead** with
   *mode='put'* and *hdkey='bunit'*.
   
   Note that when multiple image are used in the expression, there is
   no strict rule which of those images will be used to create the
   metadata of the output image, unless imagemd is specified. If
   *imagemd* is specified, the following rules of metadata copying
   will be followed:
   
   #. The pixel data type of the image specified by *imagemd* and the
      output image must be the same.
   #. The metadata copied include
   
      -  the coordinate system - thus, the dimensionality of the
         output image must correspond to the coordinate system to be
         copied
      -  the image_info record - which contains information like the
         beam(s)
      -  the misc_info record - if one exists in the image specified
         by *imagemd*
      -  the units.
   
   #. If the output image is a spectral index image, the brightness
      units are set to the empty string.
   #. If the ouptut image is a polarization angle image, the
      brightness unit is set to "deg" and the stokes coordinate is
      set to have a single plane of type of Pangle.

   
   .. rubric:: TEMPORARY IMAGES
   
   It is often necessary for this task to create intermediate,
   temporary disk images. The names of these images start with
   '_immath' and are created in the directory in which the task is
   run. The task makes reasonable attempts to remove these images
   before it exits, but there are conceivably instances where the
   temporary images may not be automatically deleted. If there is no
   immath instance in progress, it is generally safe to delete these
   files manually.

   
   .. rubric:: Task-specific Parameter Summary
   
   *mode*
   
   Mode of operation. Supported values are *'evalexpr'* (evaluate an
   LEL expression), *'spix'* (spectral index computation, although
   see also task **spxfit** for a more robust algorithm), *'pola'*
   (polarization angle), and *'poli'* (total polarization intensity).
   
   *expr*
   
   Used when *mode='evalexpr'*. LEL expression to compute.
   
   *varnames*

   List of normally short strings corresponding to the images given
   in imagename that can alternatively be used for the image names
   given in expr when *mode='evalexpr'*.
   
   *sigma*
   
   Used if *mode = 'poli'*. Standard deviation of noise for
   debiasing.
   
   *polithresh*

   Used if *mode = 'pola'*. Threshold in linear polarization
   intensity image below which to mask pixels.
   
   *imagemd*

   Name of image from which metadata should be copied to the output
   image. The input can be either an image listed in the imagename
   parameter or any other image on disk. Not specifying this
   parameter may copy header metadata from any of the input images,
   which one is not guaranteed.
   
   *prec*
   
   Specifies what the precision type, float or double (minimum match
   supported), should be for the output image. Only used if
   mode='evalexpr' or 'spix'.
   

.. _Examples:

Examples
   **Pre-defined modes:**
   
   ::
   
      mode='evalexpr'; imagename=['image1.im', 'image2.im' ]
      # in the parameter **expr**, the value 'IM0' is replaced by 'image1.im'
      # and 'IM1' is replaced with 'image2.im'
   
      mode='spix'; imagename=['image1.im','image2.im']
      # will calculate an image of log(S1/S2)/log(f1/f2), where S1 and S2 are fluxes and
      # f1 and f2 are frequencies
   
      mode='pola'; imagename='multistokes.im'
          (where that image contains both Q and U stokes planes) or
           imagename=['imageQ.im','imageU.im']

      # will calculate an image of the polarization angle distribution 0.5*arctan(U/Q),
      # where imageQ.im and imageU.im are Stokes Q and U images, respectively.
   
      mode='poli'; imagename=['imageQ.im','imageU.im','imageV.im']
      # will calculate the total polarization intensity image, where imageQ.im, imageU.im,
      # imageV.im are Stokes Q, U, and V images, respectively.
        Alternatively,

      mode='poli'; imagename = ['imageQ.im','imageU.im']
      # will calculate the linear polarization intensity image.
      # In the case where imagename is a single multi-stokes image, the total polarization
      # image will be calculated if all of the Q, U, and V stokes planes are present, and
      # the linear polarization intensity image will be calculated if the Q and U (but not V) planes
      # are present.
   
   **Examples of expressions in mode='evalexpr':**
   
   ::
   
      #Make an image that is image1.im - image2.im
      expr=’ (IM0 - IM1 )’
      #or with an explicit notation,
      expr=’("image1.im" - "image2.im")’
   
   ::
   
      #Double all values in an image.
      immath( imagename='myimage.im', expr='IM0*2',
              outfile='double.im' )
      # or with an explicit notation,
      immath( expr='"myimage.im"*2', outfile='double.im' )
   
   ::
   
      # Taking the sin of an image and adding it to another
      # Note that the images need to be the same size
      immath(imagename=['image1.im', 'image2.im'],
             expr='sin(IM1)+IM0;',outfile='newImage.im')
   
   ::

      # Adding only the plane associated with the 'V' stokes value and
      # the 1st channel together in two images
      immath(imagename=[image1', 'image2'],
             expr='IM0+IM1',chans='1',stokes='V')
   
   ::
   
      # Selecting a single plane (5th channel), of the 3-D cube and
      # adding it to the original image. In this example the 2-D plane
      # gets expanded out and the values are applied to each plane in the
      # 3-D cube. default('immath')
      imagename='ngc7538.image'
      outfile='chanFive.im'
      expr='IM0'
      chans='5'
      go
      default('immath')
      imagename=['ngc7538.image', chanFive.im']
      outfile='ngc7538_chanFive.im'
      expr='IM0+IM1'
      go
   
   ::
   
      # Selecting and saving the inner 3/4 of an image for channels 40,42,44
      # as well as channels less than 10
      default('immath')
      imagename='my_image.im'
      expr='IM0'
      box='25,25,123,123'
      chans='<10;40,42,44'
      outfile='my_image_inner.im' )
      go
   
   ::
   
      # Dividing an image by another, making sure we aren't dividing by zero
      default('immath')
      imagename=['orion.image', 'my.image']
      expr='IM0/iif(IM1==0,1.0,IM1)' #note: iif (a, b, c) a is the boolean expression
      #                                                   b is the value if true
      #                                                   c is the value if false
      outfile='my_orion.image'
      go
   
   ::
   
      # Applying a mask to all of the images in the expression
      default('immath')
      imagename=['ngc7538.image','ngc7538_clean.image']
      expr='(IM0*10)+IM1'
      mask='"ngc7538.mask"'
      outfile='really_noisy_ngc7538.image'
      go
   
   ::
   
      # Applying a pixel mask contained in the image information
      default('immath')
      imagename='ngc5921.image'
      expr='IM0*10'
      mask='mask("ngc5921.mask")'
      outfile='ngc5921.masked.image'
      go
   
   ::
   
      # Creating a total polarization intensity image from an multi-stokes image
      # containing IQUV.
      default('immath')
      outfile='pol_intensity'
      stokes=''
      # in imagename, you can also specify a list containing single
      stokes images
      # of Q and U (for linear polarization intensity) and V (for total
      # polarization intensity)
      imagename='3C138_pcal'
      mode='poli'
      go
   
   ::

      # Creating a polarization position angle image
      default('immath')
      outfile='pol_angle.im'
      mode='pola'
      # you can also do imagename=['Q.im','U.im'] for single stokes images, order of
      # the two Stokes images does not matter
      imagename='3C138_pcal' # multi-stokes image containing at least Q and U stokes
      go
   
   ::
   
      # same as before but write a mask with values of False for pixels for which the
      # corresponding linear polarization ( sqrt(Q*Q+U*U)) is less than 30 microJy/beam
      polithresh='30uJy/beam'
      go
   
   ::
   
      # Creating a spectral index image from the images at two different observing frequencies
      default('immath')
      outfile='mySource_sp.im'
      mode='spix'
      imagename=['mySource_5GHz.im','mySource_8GHz.im']
      go
   

.. _Development:

Development
   No additional development details

