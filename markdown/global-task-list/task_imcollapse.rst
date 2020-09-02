Description
   The **imcollapse** task collapses an image along a specified axis
   or set of axes of N pixels into a single pixel on each specified
   axis. Images with float precision and complex-float precision
   pixels are supported. It computes the specifiedaggregate function
   for pixel values along the specified axesand places those values
   in the single remaining plane of those axes in the output image.

   The reference pixels of the collapsed axes are set to 0 and their
   reference values are set to the mean of the the first and last
   values of those axes in the specified region of the input image.

   Convolution to a common beam is not performed automatically as
   part of the preprocessing before the collapse operation occurs.
   Therefore, if the input image has per-plane beams, then the user
   should consider first smoothing the data to have the same
   resolution (e.g., using the tool method ia.convolve2d() or the
   task imsmooth), and use theresulting image as the input for
   collapsing.

   .. rubric:: Parameter descriptions
      

   .. rubric:: *imagename
      *
      

   Name of image on which to perform the operation.

   .. rubric:: *function
      *
      

   Aggregate function to apply to pixel values. Choices are: 'flux'
   (see below for constraints), 'madm' (median absolute deviation
   from the median), 'max', 'mean', 'median', 'min', 'npts', 'rms',
   'stddev', 'sum', 'variance' and 'xmadm' (median absolute deviation
   from the median multipied by x, where x is the reciprocal of
   :math:`\Phi^{-1}` (3/4), where :math:`\Phi^{-1}` is the
   reciprocal of the quantile function. Numerically, x =
   1.482602218505602. See e.g.
   `here <https://en.wikipedia.org/wiki/Median_absolute_deviation#Relation_to_standard_deviation>`__).
   Minimal unique matching is supported for the *function* parameter
   (e.g. *function = 'r'* will compute the rms of the pixel values,
   'med' will compute the median, etc.).

   If one specifies *function='flux'*, the following requirements
   must be met:

   #. The image must have a direction coordinate,
   #. The image must have at least one beam if the brightness unit is
      Jy/beam or derived from that. An image with a brightness unit
      of K (or derivative of that) does not require a beam for this
      calculation,
   #. The specified axes must be exactly the direction coordinate
      axes,
   #. Only one of the non-directional axes may be non-degenerate,
   #. The image brightness unit must be conformant with x*y Jy/beam
      or x*y K, where x is an optional unit (such as km/s for moments
      images)and y is an optional SI prefix.

   .. rubric:: *axes
      *
      

   Image axes along which to perform the aggregation. Axes can be
   specified as a single integer or array of integers indicating the
   zero-based axes alongwhich to collapse the image. Axes may also
   be specified as a single string or an array of strings which
   minimally and uniquely match (ignoring case) world axes names in
   the image (e.g. "dec" or ["ri, "d"] forcollapsing along the
   declination axis or along the right ascension and declination
   axes, respectively).

   .. rubric:: *outfile
      *
      

   Name of image to write the result of the operation.

   .. rubric:: General selection: *box, chans, stokes, region*
      

   Region of interest in which the computation should be performed.
   See `Image Selection
   Parameters <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-selection-parameters>`__
   for details.

   .. rubric:: *mask
      *
      

   On-the-fly mask to use. See section `Image
   Masks <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks>`__
   for details.

   .. rubric:: *overwrite
      *
      

   Automatically overwrite an existing image named *outfile*? If True
   and a file by that name already exists, the application will exit
   with an error. without performing the requested operation.

   .. rubric:: *stretch
      *
      

   Stretch the specified on-the-fly *mask* along degenerate axes if
   possible and necessary to conform to the shape of the input image?
   An error will result if the shape of the specified on-the-fly mask
   is not, or in the case of *stretch* =True, cannot be made to
   conform to the shape of the input image. This parameter is ignored
   if *mask* is not specified.
