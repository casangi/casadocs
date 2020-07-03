.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      (1) list mode: prints out a list of the internal mask(s) that
      exist in mymask.im to the log

      .. container:: casa-input-box

         makemask(mode='list', inpimage='mymask.im')

       

      (2) copy mode: Regrid a Boolean (True/False) mask from one
      coordinate system to another and save as Boolean mask in the
      output image.   

      .. container:: casa-input-box

         makemask(mode='copy', inpimage='oldmask.im',
         inpmask='oldmask.im:mask0', output='newmask.im:mask0')

       

      (3) copy mode: Same as (2), but save as integer (one/zero) mask in
      the output image.

      .. container:: casa-input-box

         makemask(mode='copy', inpimage='oldmask.im',
         inpmask='oldmask.im:mask0', output='newmask.im')

      mask0 is translated so that pixels in oldmask.im that appears as
      'masked' in the viewer orhas the pixel mask value = False when
      extracted in imval, are to have pixel value of 1 inthe output
      image, newmask.im.

       

      (4) copy mode: Convert a Boolean mask to an integer mask in the
      same image

      .. container:: casa-input-box

         makemask(mode='copy', inpimage='oldmask.im',
         inpmask='oldmask.im:mask0', output='', overwrite=True)

       

      (5) copy mode: Convert an integer mask to a Boolean mask in the
      same image

      .. container:: casa-input-box

         makemask(mode='copy', inpimage='oldmask.im',
         inpmask='oldmask.im', output='oldmask.im:mask0')

       

      (6) copy mode: Copy a CRTF mask defined in mybox.txt to a Boolean
      mask in a new image

      .. container:: casa-input-box

         makemask(mode='copy', inpimage='image1.im',
         inpmask='mybox.txt', output='image2.im:mask0')

      The pixel values of image1.im will be copied to image2.im and the
      region outside mybox.txt will be masked.

       

      (7) copy mode: Apply a region defined in a CRTF file to mask part
      of an image

      .. container:: casa-input-box

         makemask(mode='copy', inpimage='image1.im',
         inpmask='myregion.crtf', output='image1.im:mask0')

      The region is copied as a Boolean mask (mask0) inside the image,
      image1.im. The region outside myregion.crtf will be masked.

       

      (8) copy mode:Merge integer andBoolean masks, using the input
      coordinate-sys of inpimage and saving in a new output file.
      Remember, if the image specified in output already exist and has a
      different coordinate system from inpimage, the mask will be
      regridded to it. All masks to be merged are specified in a list in
      inpmask.

      The name of internal masks must be given in the format,
      'parent_image_name:internal_mask_name', as shown the example
      below.

      In the example below, image1.im (the integer mask), the internal
      masks, mask0 from image1.im and mask1 from image2.im, and a region
      (on image1.im as defined in inpimage) are combined. The output,
      newmask.im is a new mask name which has not yet exist so image
      specified in inpimage, image1.im's coordinates are used as a
      target image coordinates. If image1.im and image2.im has different
      coordinates, image2.im:mask1 is regridded before it is combined to
      the other two masks.

      .. container:: casa-input-box

         makemask(mode='copy', inpimage='image1.im',
         inpmask=['image1.im', image1.im:mask0','image2.mask:mask1',
         'circle[[15pix , 15pix] ,8pix ]'], output='newmask.im)

       

      (9) expand mode: Expand an integer mask from continuum imaging to
      use as an input mask image for spectral line imaging. Use an
      existing spectral line clean image as a template by specified in
      inpimage. The inpfreqs is left out as it uses a default (=[],
      means all channels).

      .. container:: casa-input-box

         makemask(mode='expand', inpimage='spec.clean.image',
         inpmask='cont.clean.mask' outfreqs=[4,5,6,7],
         output='spec.clean.mask')

       

      (10) expand mode: Expand a Boolean mask from one range of channels
      to another range in the same image.

      .. container:: casa-input-box

         makemask(mode='expand', inpimage='oldmask.im',
         inpmask='oldmask.im:mask0', inpfreqs=[5,6],
         outfreqs=[4,5,6,7],output='oldmask.im:mask0', overwrite=True)

       

      (11) expand mode: Expand a Boolean mask from a range of channels
      in the input image to another range of channels in a different
      image with a different spectral-coordinate system. Save the mask
      as ones/zeros so that it can be used as an input mask in the clean
      task. As the inpimage is used as a template for the
      CoordinateSystem of the output cube, it is a prerequisite to have
      the cube image (a dirty image, etc). In this particular example,
      it is assumed that bigmask.im is a working copy made from the cube
      image of a previous clean execution. It is used as an input
      template and the resultant mask is overwritten to the same image.

      Specify the infreqs and outfreqs in frequency (assuming here
      bigmask.im has frequencies in ascending order),

      .. container:: casa-input-box

         makemask(mode='expand', inpimage='bigmask.im',
         inpmask='smallmask.im:mask0', inpfreqs='1.5MHz~1.6MHz',
         outfreqs='1.2MHz~1.8MHz', output='bigmask.im', overwrite=True)

      or to specify the ranges in velocities,

      .. container:: casa-input-box

         makemask(mode='expand', inpimage='bigmask.im',
         inpmask='smallmask.im:mask0', inpfreqs=4.0km/s~0.5km/s',
         outfreqs='6.5km/s~-2.4km/s', output='bigmask.im',
         overwrite=True)

       

      (12) delete mode: Delete an internal mask from an image.

      .. container:: casa-input-box

         makemask(mode='delete', inpmask='newmask.im:mask0')

       

      (13) setdefaultmask mode: Set an internal mask as a default
      internal mask.

      .. container:: casa-input-box

         makemask(mode='setdefaultmask', inpmask='newmask.im:mask1')

       

.. container:: section
   :name: viewlet-below-content-body
