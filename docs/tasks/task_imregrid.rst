

.. _Description:

Description

   .. warning:: There are `Known Issues <../../notebooks/introduction.html#Known-Issues>`__ for imregrid.
   
   This task will regrid an input image onto a new coordinate system
   from a template image or to a new directional and spectral
   reference frame. If a template image is used, then the input and
   template images must have the same coordinate structure. The
   **imregrid** task currently finds the nearest input pixel center
   and interpolates to the output pixel center.
   
   .. warning:: No averaging is done in any direction!


   .. warning:: PV images are not supported. Please first regrid as
      desired the image from which the PV image was generated, and
      then create the PV image from that regridded image.


   The new coordinate system is defined by the *template* parameter,
   which can be:
   
   -  a recognized directional reference frame string. Supported
      case-insensitive values are 'J2000', 'B1950', 'B1950_VLA',
      'GALACTIC', 'HADEC', 'AZEL', 'AZELSW', 'AZELNE', 'ECLIPTIC',
      'MECLIPTIC', 'TECLIPTIC', 'SUPERGAL'. Note that the
      conversion between one frame and another in general becomes less accurate as distance from
      the output image's reference pixel increases. After the image
      is regridded, any masked slices remaining along the edges of
      the image in the directional coordinate are cropped, so that
      there are no masked slices in the directional coordinate along
      the edges of the final image. Note that some direction
      coordinate projections, such as SFL often found in GBT images,
      have constraints which do not allow for simple regridding of
      the direction coordinate. The application will throw an
      exception in these cases.
   -  a {'csys':[valid coordinate system dictionary], 'shap':[int
      array describing the output shape]} dictionary. This is
      normally obtained by first running regrid with
      *template='get'*. In this case **imregrid** returns the
      necessary dictionary.
   -  'get', which does not regrid but returns the template
      dictionary for *imagename*, suitable for modification and reuse
      (see the point immediately above), or
   -  the name of an image from which to get the coordinate system
      and shape. The input and template images must have the same
      coordinate structure.
   
   Regridding of complex-valued images is supported. The real and
   imaginary parts are regridded independently and the resulting
   regridded pixel values are combined to form the regridded,
   complex-valued image.
   
   The *replicate* parameter can be used to simply replicate pixels
   rather than regridding them. Normally, *replicate=False*, for
   every output pixel, its world coordinate is computed and the
   corresponding input pixel found (then a little interpolation grid
   is generated). If you set *replicate=True*, then what happens is
   that for every output axis, a vector of regularly sampled input
   pixels is generated (based on the ratio of the output and input
   axis shapes). So this just means the pixels get replicated (by
   whatever interpolation scheme you use) rather than regridded in
   world coordinate space. This process is much faster, but its not a
   true world coordinate-based regrid.
   
   As decribed above, when *replicate* is False, a coordinate is
   computed for each output pixel; this is an expensive operation.
   The *decimate* parameter allows you to decimate the computation of
   that coordinate grid to a sparse grid, which is then filled in via
   fast interpolation. The default for *decimate* is 10. The number
   of pixels per axis in the sparse grid is the number of output
   pixels for that axis divided by the decimation factor. A factor of
   10 does pretty well. You may find that for very non-linear
   coordinate systems (e.g. very close to the pole) that you have to
   reduce the decimation factor. You may also have to reduce the
   decimation factor if the number of pixels in the output image
   along an axis to be regridded is less than about 50, or the output
   image may be completely masked.
   
   If one of the axes to be regridded is a spectral axis and
   *asvelocity=True*, the axis will be regridded to match the
   velocity, not the frequency, coordinate of the template coordinate
   system. Thus the output pixel values will correspond only to the
   velocity, not the frequency, of the output axis.
   
   A variety of `standard interpolation
   schemes <https://en.wikipedia.org/wiki/Interpolation>`__ are
   provided (only the first three characters to be specified). The
   'cubic' interpolation is substantially slower than 'linear', and
   often the improvement is modest. By default 'linear' interpolation
   is used.
   
   If an image has per-plane beams and one attempts to regrid the
   spectral axis, an exception is thrown. One should consider
   convolving all planes to the same resolution in such cases and
   then regridding.

   .. rubric:: Rules Used for Generating Output Images in Specific Cases

   There are numerous rules governing the shape and coordinate system
   of the output image depending on the input image, template image,
   and wheher default values of the axes and shape parameters are
   used. They are enumerated below.
   
   .. note:: **NOTE**: If you want to be certain of what type of output you
      will get, it is highly recommended you specify both axes and
      shape to avoid any ambiguity.
   

   .. rubric:: *1. Rules governing Stokes axes*

   1.1. If the input image has no stokes axis, then the output
   image will have no stokes axis.
   
   1.2. If the input image has a stokes axis, but the template
   image/coordinate system does not, and if the default value of the
   *shape* parameter is used or if *shape* is specified and the
   specified value for the length stokes axis in equal to the length
   of the input image stokes axis, then all stokes in the input image
   will be present in the output image.
   
   1.3. If the input image has a stokes axis, but the template
   image/coordinate system does not, and if the value of the *shape*
   parameter is specified but the length of the resulting stokes axis
   is not equal to the length of the input image's stokes axis, a
   failure will occur.
   
   1.4. If the input image has a stokes axis, if the *template*
   parameter is an image name, and if the template image has a
   degenerate stokes axis, if the *axes* parameter is not specified
   or is specified but does not contain the input stokes axis number,
   and if the *shape* parameter is not specified, then all stokes
   planes in the input image will be present in the output image.
   
   1.5. If the input image has a stokes axis, if the *template*
   parameter is an image name, and if the template image has a
   degenerate stokes axis, if the *axes* parameter is not specified
   or is specified but does not contain the input stokes axis number,
   if the *shape* parameter is specified, and if the specified length
   of the stokes axis is not equal to the length of the input stokes
   axis, then a failure will occur.
   
   1.6. If the input image has a stokes axis, if the *template*
   parameter is an image name, if the template image has a degenerate
   stokes axis, if the *axes* parameter is specified contains the
   input stokes axis number, then use the applicable rule of rules
   1.7. and 1.8. for the template image having a nondegenerate stokes
   axis.
   
   1.7. If the input image has a stokes axis, if the *template*
   parameter is an image name, if the template image has a
   nondegenerate stokes axis, and if *axes* parameter is not
   specified or if it is, it contains the input stokes axis number,
   then only the stokes parameters common to both the input image and
   the template image will be present in the output image. If the
   input image and the template image have no common stokes
   parameters, failure will occur. If shape is specified and the
   length of the specified stokes axis is not equal to the number of
   common stokes parameters in the input image and the template
   image, then failure will result.
   
   1.8. If the input image has a stokes axis, if the *template*
   parameter is an image name, if the template image has a
   nondegenerate stokes axis, and if *axes* parameter is specified
   but does not contain the input image stokes axis number, then all
   stokes present in the input image will be present in the output
   image. If the *shape* parameter is also specified but the length
   of the specified stokes axis does not equal the length of the
   input stokes axis, then failure will result.
   

   .. rubric:: *2. Rules governing spectral axes*

   In all cases, if the shape *parameter* is specified, the spectral
   axis length must be consistent with what one would normally expect
   in the special cases, or a failure will result.
   
   2.1. If the input image does not have a spectral axis, then
   the output image will not have a spectral axis.
   
   2.2. If the input image has a degenerate spectral axis, if the
   *template* parameter is an image name, and if the template image
   has a spectral axis, if the *axes* parameter is not specified or
   if it is and does not contain the input image spectral axis
   number, then the spectral coordinate of the input image is copied
   to the output image and the output image will have a degenerate
   spectral axis.
   
   2.3. If the input image has a degenerate spectral axis, if the
   *template* parameter is an image name, and if the template image
   has a spectral axis, if the *axes* parameter is specified and it
   contains the input image spectral axis number, then the spectral
   coordinate of the template image is copied to the output image. If
   the *shape* parameter is not specified, the output image will have
   the same number of channels as the input image. If the *shape*
   parameter is specified, the output image will have the number of
   channels as specified in shape for the spectral axis. In these
   cases, the pixel and mask values for all spectral hyperplanes will
   be identical; the regridded single spectral plane is simply
   replicated n times, where n is the number of channels in the
   output image.
   
   2.4. If the input image has a spectral axis, if the *template*
   parameter is an image name, and if the template image does not
   have a spectral axis, if the *axes* parameter is not specified or
   if it is and does not contain the input image spectral axis
   number, then the spectral coordinate of the input image is copied
   to the output image and the output image will have the same number
   of channels as the input image.
   
   2.5. If the input image has a spectral axis, if the *template*
   parameter is an image name, if the template image does not have a
   spectral axis, if the *axes* parameter is specified and it
   contains the input image spectral axis number, then failure will
   result.
   
   2.6. If the input image has a spectral axis, if the *template*
   parameter is an image name, if the template image has a degenerate
   spectral axis, and if the *axes* parameter is unspecified or if it
   is but does not contain the spectral axis number of the input
   image, the spectral coordinate of the input image is copied to the
   output image and the output image will have the same number of
   channels as the input image.
   
   2.7. If the input image has a spectral axis, if the *template*
   parameter is an image name, if the template image has a
   nondegenerate spectral axis, and if the *axes* parameter is
   unspecified or if it is and contains the spectral axis number of
   the input image, regrid the spectral axis of the input to match
   the spectral axis of the template.


   .. rubric:: Important Note About Flux Conservation

   In general, regridding is inaccurate for images in which the
   angular resolution is poorly sampled.
   
   The issue is that CASA treats the values in "pixels" as
   measurements of a sky brightness distribution, each at an
   infinitessimally small single point at the location of the "pixel"
   center (to enable the Fourier transforms and gridding that CASA
   deals with regularly). If one has well-sampled the (beam-smoothed)
   sky brightness distribution, then one can resample that
   distribution to a different set of locations, and everything will
   come out correctly. If one has not sampled the distribution well,
   then interpolation to other locations will introduce significant
   errors. Imagine a worst case of a (well-sampled) peak being
   resampled to large "pixel" locations, such that the centers of
   two output pixels fall on either side of the peak. The
   interpolated values at those locations will effectively cause the
   peak to completely disappear.
   
   This is in contrast to software that considers the value in a
   "pixel" to be the sum of the sky brightness subtended by that
   finite-sized pixel. In such software, resampling to other pixels
   requires calculating the overlap of the old and new finite-sized
   pixels, and apportioning the summed flux among output pixels
   accordingly. Such an operation is designed to conserve the total
   flux in the image even if the beam is not well-sampled and is
   common in most optical and infrared imaging and display software.
   Again considering the pathological example of a peak being sampled
   onto a large-pixel grid, explicitly flux-conserving software would
   add up the values from all of the small input pixels, and thus
   although the peak would be coarsely represented in the output
   image, the flux from that peak would not disappear.
   
   In CASA, the different definition of what a "pixel" is requires
   that one have a well-sampled beam, or one will inherently not get
   the right answer. A check is done for such cases and a warning
   message is printed if a beam is present. However, no such check is
   done if there is no beam present. To add a restoring beam to an
   image, use **ia.setrestoringbeam**.
   

   .. rubric:: Task-specific Parameter Summary
   
   *template*
   
   Indicates how the template coordinate system is being specified.
   See above for details.
   
   *shape*

   Shape of the output image. Only used if template is an image. If
   not specified (-1), the output image shape will be the same as the
   template image shape along the axes that are regridded and the
   same as input image shape along the axes which  are not regridded.
   
   *asvelocity*

   Regrid spectral axis in velocity space rather than frequency
   space?
   
   *axes*

   The pixel axes to regrid. -1 => all.
   
   *interpolation*

   The interpolation method. One of "nearest", "linear", "cubic".
   
   *decimate*
   
   Decimation factor for coordinate grid computation. A value of 10
   is sufficient in most cases, except for images in which the length
   of at least one axis to be regridded is less than about 70 or if
   the input or output direction coordinate is close to a pole. In
   these cases, a smaller factor will give signficantly better
   accuracy.
   
   *replicate*

   Replicate image rather than regrid?
   

.. _Examples:

Examples
   **Basic Examples**
   
   ::
   
      # Regrid an image to the "B1950" or "GALACTIC" coordinate systems
      imregrid(imagename="input.image", output="output.image", template="B1950")
      imregrid(imagename="input.image", output="output.image", template="GALACTIC")
   
   .. note:: When regridding to another coordinate system in the
      manner above, if the input image's direction coordinate is
      already in the frame specified by template, a straight copy of
      the image is made. No regridding is actually done.

   
   ::
   
      # Obtain a template dictionary from an image and then use it to regrid another image
      temp_dict = imregrid(imagename="target.image", template="get")
      imregrid(imagename="input.image", output="output.image", template=temp_dict)
   
   In this example, the *template="get"* option is used in the first
   command in order to characterize the desired shape and coordinate
   system used, and a new dictionary, TEMP_DICT, is generated
   accordingly. This is then used when performing the actual
   regridding of input.image in the second command.

   
   **More Advanced Examples**
   
   It is also possible to directly use a template image for
   regridding with **imregrid**. For this to work reliably and
   predictably, the dimensionality (i.e. which dimensions are present
   in an image) and the axis ordering of the input image must be the
   same. The type and ordering of the axes of both the input and
   template images can (and should) first be examined using the CASA
   **imhead** task. Any necessary reordering of axes can be performed
   using the CASA **imtrans** task. Unless the user explicitly
   specifies which dimensions to regrid using the *axes* parameter
   (see the following example), **imregrid** will also  attempt to
   regrid degenerate axes (i.e. image axes of length one pixel).
   Stokes axes are never regridded. In the case where template is an
   image name and the default value of shape is specified, the output
   image's shape will be the same as the template image's shape along
   the axes which are regridded and the same as the input image's
   shape along the axes which are not regridded. So for example, if
   the input image has a *shape* of [20, 30, 40] and the template
   image has a *shape* of [10, 40, 70] and only *axes=[0, 1]*, the
   output image will have a *shape* of [10, 40, 40]. If *axes=[2]*,
   the output image will have a *shape* of [20, 30, 70].
   
   ::
   
      # Regrid input.image by directly using target.image as a template
      imregrid(imagename="input.image", output="output.image", template="target.image", shape=[500,500,40,1])
   
   In this example, it is assumed that the axis order of the input
   image is of the form (direction_x, direction_y, spectral, Stokes),
   where 'direction_x' and 'direction_y' are the directional
   coordinates on the sky (in some reference frame), 'spectral' is a
   velocity/frequency axis, and 'Stokes' contains polarization
   information. In this example, input.image might typically be a
   data cube of shape [100, 100, 40, 1]. Note that the default value
   of *asvelocity* (True) will be used so that the spectral axis will
   be regridded to the same velocity system as that of the template
   image.
   
   ::
   
      # Regrid only the first two axes of an image
      imregrid(imagename="input.image", output="output.image", template="target.image", axes=[0,1])
   
   In this example, the user should inspect the type and ordering of
   the axes with **imhead**, and then correct with **imtrans** if
   necessary. The above command will regrid only the first two axes
   (normally the directional axes) of input.image and leave all other
   axes unchanged. The output image will have the shape of the
   template image along the regridded axes [0, 1] and the shape of
   the input image along the other axes since the shape parameter was
   not explicitly specified.
   
   ::
   
      # Regrid the third axis, considering velocity rather than frequency units
      imregrid(imagename="input.image", output="output.image", template="target.image", axes=[2], asvelocity=True)
   
   This example regrids the spectral axis (zero-based axis number 2)
   with respect to velocity because the *asvelocity* parameter has
   been set to True. This is useful when e.g., regridding a cube
   containing one spectral line to match the velocity coordinate of
   another cube containing a different spectral line.
   
   ::
   
      # Regrid the third axis, considering velocity rather than frequency units but first set the rest frequency
      imhead("input.image", mode="put", hdkey="restfreq", hdvalue="110GHz")
      imregrid(imagename="input.image", output="output.image", template="target.image", axes=[2], asvelocity=True)
   
   The first command in this example uses the **imhead** task to set
   the value of the image rest frequency to a value of 110GHz in
   input.image. The following **imregrid** command then performs a
   frequency units regridding only of the third axis listed
   (zero-based axis) (2), taking account of the input.image rest
   frequency in the input file.
   

.. _Development:

Development
   No additional development details

