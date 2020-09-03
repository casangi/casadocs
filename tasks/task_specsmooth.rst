Description
   This application performs one dimensional convolution along a
   specified axis of an image or selected region of an image. Hanning
   smoothing and boxcar smoothing are supported. Both float valued
   and complex valued images are supported. Masked pixel values are
   set to zero prior to convolution. All nondefault pixel masks are
   ignored during the calculation. The convolution is done in the
   image domain (i.e., not with an FFT).

   .. rubric:: BOXCAR SMOOTHING
      

   One dimensional boxcar convolution is defined by

   ::

      zi = (yi + yi+1 + ... + yi+w-1)/w

   | where *z* :sub:`i` is the value at pixel *i* in the box car
     smoothed image, *y* :sub:`k` is the pixel value of the input
     image at pixel *k*, and *w* is a postivie integer representing
     the width of the boxcar in pixels. The length of the axis along
     which the convolution is to occur must be at least *w* pixels in
     the selected region, unless decimation using the mean function
     is chosen in which case the axis
   | length must be at least 2 *w* (see below).

   If *dmethod=""* (no decimation), the length of the output axis
   will be equal to *L* - (*w* + 1), where *L* is the length of the
   input axis. The default pixel mask if one exists is ANDed with the
   OTF mask if specified and copied from the selected region of the
   input image to the output image (in other words, the result mask
   for creating the output image is true only for pixels for which
   both the OTF and pixel mask are true). Thus for example, if the
   selected region in the input image has six planes along the
   convolution axis, if the specified boxcar width is 2, and if the
   pixel values, which are all unmasked, on a slice along this axis
   are [1, 2, 5, 10, 17, 26], then the corresponding output slice
   will be of length five pixels and the output pixel values will be
   [1.5, 3.5, 7.5, 13.5, 21.5].

   If *dmethod="copy"*, the output image is the image calculated if
   *dmethod=""*, except that only every *w* th plane is kept. Both
   the pixel and mask values of these planes are copied directly to
   the output image, without further processing. Thus for example, if
   the selected region in the input image has six planes along the
   convolution axis, the boxcar width is chosen to be 2, and if the
   pixel values, which are all unmasked, on a slice along this axis
   are [1, 2, 5, 10, 17, 26], the corresponding output pixel values
   will be [1.5, 7.5, 21.5].

   | If *dmethod="mean"*, first the image described in the
     *dmethod=""* case is calculated. Then, the *i* th plane of the
     output image is calculated by averaging the *i*w* to the
     *(i+1)*w-1* planes of this intermediate image. Thus, for
     example, if the selected region in the input image has six
     planes along the convolution axis, the boxcar width is chosen to
     be 2, and if the pixel values,
   | which are all unmasked, on a slice along this axis are [1, 2, 5,
     10, 17, 26], then the corresponding output pixel values will be
     [2.5, 10.5]. Any pixels at the end of the convolution axis of
     the intermediate image that do not fall into a complete bin of
     width *w* are ignored. Masked values are taken into
     consideration when forming this average, so if one of the values
     is masked, it is not used in the average. If at least one of the
     values in the intermediate image bin is not masked, the
     corresponding output pixel will not be masked.

   .. rubric:: HANNING SMOOTHING
      

   Hanning convolution of one axis of an image is defined by

   ::

      zi = 0.25yi-1 + 0.5yi + 0.25yi+1 (equation 1)

   where *z* :sub:`i` is the value at pixel *i* in the hanning
   smoothed image, and *y i-1*, *y* :sub:`i`, and *y i+1* are the
   values of the input image at pixels *i*-1, *i*, and *i* +1
   respectively. The length of the axis along which the convolution
   is to occur must be at least three pixels in the selected region.

   If *dmethod=""* (no decimation of image planes), the length of the
   output axis will be the same as that of the input axis. The output
   pixel values along the convolution axis will be related to those
   of the input values according to equation 1, except the first and
   last pixels. In that case,

   ::

      z0 = (y0 + y1)/2

   and,

   ::

      zN-1 = (yN-2 + yN-1)/2

   where *N* is the number of pixels along the convolution aixs. The
   default pixel mask, if one exists, is ANDed with the OTF mask if
   specified and is copied from the selected region of the input
   image to the output image. Thus for example, if the selected
   region in the input image has six planes along the convolution
   axis, and if the pixel values, which are all unmasked, on a slice
   along this axis are [1, 2, 5, 10, 17, 26], the corresponding
   output pixel values will be [1.5, 2.5, 5.5, 10.5, 17.5, 21.5].

   If *dmethod="copy"*, the output image is the image calculated if
   *dmethod=""*, except that only the odd-numbered planes are kept.
   Furthermore, if the number of planes along the convolution axis in
   the selected region of the input image is even, the last odd
   number plane is also discarded. Thus, if the selected region has
   *N* pixels along the convolution axis in the input image, along
   the convolution axis the output image will have (*N*-1)/2 planes
   if *N* is odd, or (*N-2*)/2 planes if *N* is even. The pixel and
   mask values are copied directly, without further processing. Thus
   for example, if the selected region in the input image has six
   planes along the convolution axis, and if the pixel values, which
   are all unmasked, on a slice along this axis are [1, 2, 5, 10, 17,
   26], the corresponding output pixel values will be [2.5, 10.5].

   If *dmethod="mean"*, first the image described in the *dmethod=""*
   case is calculated. The first plane and last plane(s) of that
   image are then discarded as described in the *dmethod="copy"*
   case. Then, the ith plane of the output image is calculated by
   averaging the (2 *i*)th and (2 *i* + 1)th planes of the
   intermediate image. Thus for example, if the selected region in
   the input image has six planes along the convolution axis, and if
   the pixel values, which are all unmasked, on a slice along this
   axis are [1, 2, 5, 10, 17, 26], the corresponding output pixel
   values will be [4.0, 14.0]. Masked values are taken into
   consideration when forming this average, so if one of the values
   is masked, it is not used in the average. If at least one of the
   values in the input pair is not masked, the corresponding output
   pixel will not be masked.

   

   .. rubric:: Task specific parameter summary
      

   .. rubric:: *axis*
      

   Zero-based profile axis number. Default (<0): use the spectral
   axis if one exists, axis 0 otherwise.

   .. rubric:: *function*
      

   Convolution function. hanning and boxcar are supported functions.
   Minimum match is supported.

   .. rubric:: *width*
      

   Width of boxcar, in pixels. Ignored for hanning smoothing.

   .. rubric:: *dmethod*
      

   Decimation method. "" means no decimation, "copy" and "mean" are
   also supported (minimum match).
