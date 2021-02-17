

.. _Description:

Description
   This task copies all or part of the image to a new image specified
   by *outfile*. Both float and complex valued images are supported.
   
   Sometimes it is useful to drop axes of length one (degenerate
   axes). Set *dropdeg* equal to True if you want to do this.
   
   The output mask is the union (logical AND) of the default input
   pixel mask (if any) and the OTF mask. Any other input pixel masks
   will not be copied. Use function **ia.maskhandler** if you need to
   copy other masks too.
   
   If the mask has fewer dimensions than the image and if the shape
   of the dimensions the mask and image have in common are the same,
   the mask will automatically have the missing dimensions added so
   it conforms to the image.
   
   If *stretch=True* and if the number of mask dimensions is less
   than or equal to the number of image dimensions and some axes in
   the mask are degenerate while the corresponding axes in the image
   are not, the mask will be stretched in the degenerate dimensions.
   For example, if the input image has shape [100, 200, 10] and the
   input mask has shape [100, 200, 1] and *stretch=True*, the mask
   will be stretched along the third dimension to shape [100, 200,
   10]. However if the mask has shape [100, 200, 2], stretching is
   not possible and an error will result.
   
   .. rubric:: Task-specific parameters
   
   *dropdeg*
   
   Exclude axes from output image if they would have a length of one
   pixel.
   
   *verbose*
   
   Post additional informative, possibly useful, messages to the
   logger?
   
   *keepaxes*
   
   If dropdeg=True, these are the degenerate axes to keep.
   Nondegenerate axes are implicitly always kept. Ignored if
   dropdeg=False; all axes are kept in that case.
   

.. _Examples:

Examples
   ::
   
      # make a subimage containing only channels 4 to 6 of the
      original image,
      imsubimage(imagename="my.im", outfile="first.im", chans="4~6")
   
   ::
   
      # Same as above command, just specifying chans in an alternate, more verbose way
      imsubimage(imagename="my.im", outfile="second.im", chans="range=[4pix,6pix]")
   
   ::
   
      # Same as the above command, but even more verbose way of
      # specifying the spectral selection. Assumes the direction axes
      # are axes numbers 0 and 1.
      ia.open("my.im")
      shape = ia.shape()
      axes = ia.coordsys().names()
      ia.done()
      xmax = shape[axes.index("Right Ascension")] - 1
      ymax = shape[axes.index("Declination")] - 1
      reg = "box[[0pix,0pix],[" + str(xmax) + "pix, " + str(ymax) + "pix]]
      range=[4pix,6pix]"
      imsubimage(imagename="my.im", outfile="third.im", region=reg)
   
   ::
   
      # As an example of the usage of the keepaxes parameter, consider an image
      # that has axes RA, Dec, Stokes, and Freq. The Stokes and Freq axes are both
      # degenerate while the RA and Dec axes are not, and it is desired to make a
      # subimage in which the Stokes axis is discarded. The following command will
      # accomplish that.
      imsubimage(imagename="my.im", outfile="discarded_stokes.im", dropdeg=True, keepaxes=[3])
   

.. _Development:

Development
   No additional development details

