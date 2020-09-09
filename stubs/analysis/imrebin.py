#
# stub function definition file for docstring parsing
#

def imrebin(imagename, outfile='', factor='', region='', box='', chans='', stokes='', mask='', dropdeg=False, overwrite=False, stretch=False, crop=True):
    r"""
Rebin an image by the specified integer factors

Parameters
   - imagename_ (string) - Name of the input image
   - outfile_ (string='') - Output image name.
   - factor_ (intArray='') - Binning factors for each axis. Use imhead or ia.summary to determine axis ordering.
   - region_ (variant='') - Region selection. Default is to use the full image.
   - box_ (string='') - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   - chans_ (string='') - Channels to use. Default is to use all channels.
   - stokes_ (string='') - Stokes planes to use. Default is to use all Stokes planes. Stokes planes cannot be rebinned.
   - mask_ (string='') - Mask to use. Default is none.

      .. raw:: html

         <details><summary><i> mask != '' </i></summary>

      - stretch_ (bool=False) - Stretch the mask if necessary and possible? 

      .. raw:: html

         </details>
   - dropdeg_ (bool=False) - Drop degenerate axes?
   - overwrite_ (bool=False) - Overwrite the output if it exists? Default False
   - crop_ (bool=True) - Remove pixels from the end of an axis to be rebinned if there are not enough to form an integral bin?


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


.. _imagename:

imagename (string)
   | Name of the input image

.. _outfile:

outfile (string='')
   | Output image name.

.. _factor:

factor (intArray='')
   | Binning factors for each axis. Use imhead or ia.summary to determine axis ordering.

.. _region:

region (variant='')
   | Region selection. Default is to use the full image.

.. _box:

box (string='')
   | Rectangular region to select in direction plane. Default is to use the entire direction plane.

.. _chans:

chans (string='')
   | Channels to use. Default is to use all channels.

.. _stokes:

stokes (string='')
   | Stokes planes to use. Default is to use all Stokes planes. Stokes planes cannot be rebinned.

.. _mask:

mask (string='')
   | Mask to use. Default is none.

.. _dropdeg:

dropdeg (bool=False)
   | Drop degenerate axes?

.. _overwrite:

overwrite (bool=False)
   | Overwrite the output if it exists? Default False

.. _stretch:

stretch (bool=False)
   | Stretch the mask if necessary and possible?

.. _crop:

crop (bool=True)
   | Remove pixels from the end of an axis to be rebinned if there are not enough to form an integral bin?


    """
    pass
