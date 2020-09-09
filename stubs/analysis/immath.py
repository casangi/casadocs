#
# stub function definition file for docstring parsing
#

def immath(imagename='', mode='evalexpr', outfile='immath_results.im', expr='IM0', varnames='', sigma='0.0mJy/beam', polithresh='', mask='', region='', box='', chans='', stokes='', stretch=False, imagemd='', prec='float'):
    r"""
Perform math operations on images

Parameters
   - imagename_ (variant='') - a list of input images 
   - mode_ (string='evalexpr') - mode for math operation (evalexpr, spix, pola, poli, lpoli, tpoli)

      .. raw:: html

         <details><summary><i> mode = evalexpr </i></summary>

      - expr_ (string='IM0') - Mathematical expression using images
      - varnames_ (variant='') - a list of variable names to use with the image files

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = poli </i></summary>

      - sigma_ (string='0.0mJy/beam') - standard deviation of noise for debiasing

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = lpoli </i></summary>

      - sigma_ (string='0.0mJy/beam') - standard deviation of noise for debiasing

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = tpoli </i></summary>

      - sigma_ (string='0.0mJy/beam') - standard deviation of noise for debiasing

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = pola </i></summary>

      - polithresh_ (string='') - Threshold in linear polarization intensity image below which to mask pixels.

      .. raw:: html

         </details>
   - outfile_ (string='immath_results.im') - File where the output is saved
   - mask_ (string='') - Mask to use. Default is none.

      .. raw:: html

         <details><summary><i> mask != '' </i></summary>

      - stretch_ (bool=False) - Stretch the mask if necessary and possible? See help stretch.par 

      .. raw:: html

         </details>
   - region_ (string='') - Region selection. Default is to use the full image.
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes.
   - imagemd_ (string='') - An image name from which metadata should be copied. The input can be either an image listed under imagename or any other image on disk. Leaving this parameter unset may copy header metadata from any of the input images, which one is not guaranteed. 
   - prec_ (string='float') - Precision for the output image pixels if mode="evalexpr" or "spix". "float" or "double" (minimum match supported)


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
   Analysis <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis>`__
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

   .. warning:: **WARNING** *:* for a mathematical expression that involves
      multiple images (e.g., subtracting one image from the other),
      it is good to realize that the algorithm is pixel-based. This
      means that it is up to the user to put the images on the same
      dimensions for all relevant axes (e.g., RA and dec). Where
      needed, use **imregrid** before using **immath** to ensure the
      image dimensions on the relevant axes are the same.

   

   .. rubric:: NOTES ON MODES OF OPERATION (`MODE’)
      

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

   Note that thismode is flexible and will fall back to '*tpoli*'
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
   help <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list>`__
   for details).

   When using a multi-Stokes input image, the modes *'tpoli'* and
   *'lpoli'* can be used to control which polarizations are used in
   the calculation:

   The*mode='tpoli'*option will calculate atotal polarization
   intensity image;

   :math:`\sqrt{( Q^2+ U^2+ V^2)}`.

   The task requires all three Stokes image planes to be present.

   The *mode='lpoli'*option will calculate a linear polarization
   intensity image;

   :math:`\sqrt{( Q^2+ U^2)}`.

   Only the Q and U Stokes image planes are required to be present.
   If Stokes Vis present it will be ignored.

   

   .. rubric:: NOTES ON *MODE='SPIX'*
      

   This mode computes the spectral index using two images of
   different frequencies. The spectral index is defined as

   :math:`\alpha = ln(I_0/I_1)/ln(\nu_0/\nu_1)`

   | where the :math:`I`'s are the pixel values and the
     :math:`\nu`'s are the frequencies of the two images.

   | If exactly two images aren't supplied, an exception will result.
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

   

   .. rubric:: NOTES ON PRECPARAMETER
      WITHMODE='EVALEXPR'AND'SPIX'
      

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
   using tool method **ia.setbrightnessunit**or task **imhead** with
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
      

   .. rubric:: *mode*
      

   Mode of operation. Supported values are *'evalexpr'* (evaluate an
   LEL expression), *'spix'* (spectral index computation, although
   see also task **spxfit** for a more robust algorithm), *'pola'*
   (polarization angle), and *'poli'* (total polarization intensity).

   .. rubric:: *expr*
      

   Used when *mode='evalexpr'*. LEL expression to compute.

   .. rubric:: *varnames*
      

   List of normally short strings corresponding to the images given
   in imagename that can alternatively be used for the image names
   given in expr when *mode='evalexpr'*.

   .. rubric:: *sigma*
      

   Used if *mode = 'poli'*. Standard deviation of noise for
   debiasing.

   .. rubric:: *polithresh*
      

   Used if *mode = 'pola'*. Threshold in linear polarization
   intensity image below which to mask pixels.

   .. rubric:: *imagemd*
      

   Name of image from which metadata should be copied to the output
   image. The input can be either an image listed in the imagename
   parameter or any other image on disk. Not specifying this
   parameter may copy header metadata from any of the input images,
   which one is not guaranteed.

   .. rubric:: *prec*
      

   Specifies what the precision type, float or double (minimum match
   supported), should be for the output image. Only used if
   mode='evalexpr' or 'spix'.


.. _imagename:

imagename (variant='')
   | a list of input images

.. _mode:

mode (string='evalexpr')
   | mode for math operation (evalexpr, spix, pola, poli, lpoli, tpoli)

.. _outfile:

outfile (string='immath_results.im')
   | File where the output is saved

.. _expr:

expr (string='IM0')
   | Mathematical expression using images

.. _varnames:

varnames (variant='')
   | a list of variable names to use with the image files

.. _sigma:

sigma (string='0.0mJy/beam')
   | standard deviation of noise for debiasing

.. _polithresh:

polithresh (string='')
   | Threshold in linear polarization intensity image below which to mask pixels.

.. _mask:

mask (string='')
   | Mask to use. Default is none.

.. _region:

region (string='')
   | Region selection. Default is to use the full image.

.. _box:

box (string='')
   | Rectangular region to select in direction plane. Default is to use the entire direction plane.

.. _chans:

chans (string='')
   | Channels to use. Default is to use all channels.

.. _stokes:

stokes (string='')
   | Stokes planes to use. Default is to use all Stokes planes.

.. _stretch:

stretch (bool=False)
   | Stretch the mask if necessary and possible? See help stretch.par

.. _imagemd:

imagemd (string='')
   | An image name from which metadata should be copied. The input can be either an image listed under imagename or any other image on disk. Leaving this parameter unset may copy header metadata from any of the input images, which one is not guaranteed.

.. _prec:

prec (string='float')
   | Precision for the output image pixels if mode="evalexpr" or "spix". "float" or "double" (minimum match supported)


    """
    pass
