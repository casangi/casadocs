Description
   This application rebins the specified image by the specified
   integer binning factors for each axis. It supports both float
   valued and complex valued images. The corresponding output pixel
   value is the average of the input pixel values. The output pixel
   will be masked False if there were no good input pixels. A
   polarization axis cannot be rebinned.

   | The binning factors array must contain at least one element and
     no more elements than the number of input image axes. If the
     number of elements specified is less than the number of image
     axes, then the remaining axes not specified are not rebinned.
     All specified values must be positive. A value of one indicates
     that no rebinning of the associated axis will occur.
   | Should this array contain any float values, they will be rounded
     to the next lowest integer. Note that in many images with both
     frequency and polarization axes, the polarization axis preceeds
     the frequency axis. If you wish to rebin the frequency axis, it
     is recommended that you inspect your image with **imhead** or
     **ia.summary** to determine the axis ordering.

   Binning starts from the origin pixel of the bounding box of the
   selected region or the origin pixel of the input image if no
   region is specified. The value of crop is used to determine how to
   handle cases where there are pixels at the end of the axis that do
   not form a complete bin. If *crop=True*, extra pixels at the end
   of the axis are discarded. If *crop=False*, the remaining pixels
   are averaged into the final bin along that axis. Should the length
   of the axis to be rebinned be an integral multiple of the
   associated binning factor, the value of crop is irrelevant.

   A value of *dropdeg=True* will result in the output image not
   containing axes that are degenerate in the specified region or in
   the input image if no region is specified. Note that, however, the
   binning factors array must still account for degenerate axes, and
   the binning factor associated with a degenerate axis must always
   be 1.
