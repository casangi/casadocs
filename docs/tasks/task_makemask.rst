

.. _Description:

Description
   task description
   
   makemask manages Boolean masks in an image, converts and regrids
   Boolean to value-based masks (and vice versa), stretches
   single-plane masks to cubes, and generates masks from CASA region
   files. Detailed background information on masks, and examples on
   how to create them, can be found in the CASA Docs Chapter pages
   on `image
   masks <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/image-masks>`__ (image
   analysis) and `masks for
   deconvolution <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/masks-for-deconvolution>`__ (synthesis
   imaging).
   
    
   
   .. rubric:: Parameter descriptions
      
   
   .. rubric:: *mode*
      
   
   Mask method to use by makemask task. Below are the allowed
   values: 
   
   -  list: list internal Boolean masks in inpimage to the log
      (default value)
   -  copy: copy/merge masks and regrid if necessary to a new or
      existing mask
   -  expand: expand a mask from one range of frequencies to another
      range
   -  delete: delete an internal mask from an image; if the deleted
      mask was a default mask, the task chooses the first one in the
      remaining internal mask list as default (as appears in the log
      when do listing with mode='list')
   -  setdefaultmask: set a specified internal mask as a default
      internal mask
   
   In all cases (for output mask is expected), if the output image
   has a different coordinate system from the result of input and
   processing, the mask will be re-gridded to the output coordinate
   system.
   
   .. rubric:: inpimage
      
   
   Name of input image to use as a reference for the output
   coordinates (if output does not exist). Also used as a reference
   image when regions are specified in inpmask for mode='copy'. If
   output is a new image specified with an internal True/False mask,
   the pixel values in the input image are copied to the output image
   and the regions specified in inpmask are merged (if multiple
   regions specified) and treated as a valid region, therefore will
   be UNMASKED in output.
   
    
   
   .. rubric:: Expandable parameters for mode='copy', 'expand',
      'delete' and 'setdefaultmask':
      
   
   .. rubric:: inpmask
      
   
   Name(s) of input mask(s).The default is set to inpmask='', for
   when no mask is given. To specify an image (zero/non-zero) mask,
   just give a image name (e.g. myimage1.im). To specify an internal
   (True/False) mask, you must give a parent image name and the
   internal mask name separated by a colon. (e.g. myimage1.im:mask0).
   The internal mask names can be found by running the makemask task
   in mode='list'. For mode='expand', use the inpimage values to make
   a mask (zero/non-zero). Non-zero values are normalized to one in
   the process. For mode='copy', a list of strings can be used to
   merge specific image mask(s), True/False mask(s), and region(s).
   The regions can be specified directly in the CASA region format or
   in the text file(s) contains the regions.
   
   .. rubric:: output
      
   
   Name of output image (no default value). Ifthe output is a plain
   image name, the resultant mask is written as an image (zero/one)
   mask. If the output name is the form of 'imagename:maskname', the
   resultant mask is written as an internal (True/False) mask. To
   re-grid a mask to a different coordinate system, give an image
   with the target coordinate system in inpimage, or make a copy of
   an image with the target coordinate system and specified the name
   of the copy in output. If output is specified as a plain image (if
   it exists), it will regrid the mask to the new coordinate system
   and modify output (if overwrite=True). If output is specified as
   an image with an internal mask (if the internal mask exists), it
   will regrid the mask to the new coordinate system and modify the
   internal mask only (if overwrite=True). If output does not exist,
   it will only copy inpimage. If output == inpimage, makemask will
   not regrid but only modify in-place.
   
   .. note:: NOTE: The term 'mask' is used in the image analysis and clean
      tasks in opposite sense. In the image analysis, the masked
      region is a region to be excluded, while clean's input mask
      defines the region to be used as a clean box/region. In the
      makemask task, since the most common use case of output image
      mask is to use as an input mask in clean, when it converts an
      internal mask to the image mask, the 'masked' region (where the
      pixels are masked and have the Boolean value False) of the
      internal mask is translated to the pixels with value of 0 in
      output image mask.
   
   .. rubric:: overwrite
      
   
   Overwrite the mask specified in output (see also the output rules
   above). The default value is False.
   
   .. note:: NOTE: For a cube mask, overwrite=True generally overwrites in
      the specified channel planes only and so any pre-existed masks
      in other channels will be remain untouched.
   
    
   
   .. rubric:: Additional expandable parameters for mode='expand'
      
   
   .. rubric:: inpfreqs
      
   
   Input channel/frequency/velocity range. Specify channels in a list
   of integers. For frequency/velocity, a range is specified in a
   string with '~', e.g. '1.5MHz~1.6MHz', '-8km/s~-14km/s' (for a
   cube with ascending frequencies/velocities). The default is all
   channels.
   
   .. note:: NOTE: The range in frequency or velocity needs to be specified
      as the same order as in the template cube specified in
      inpimage. E.g., if a template cube has descending frequencies,
      then the range will be, e.g. '1.6MHz~1.5MHz' or
      '-14km/s~-8km/s'.
   
   .. rubric:: outfreqs
      
   
   Output channel/frequency/velocity range. Specify same way as
   inpfreqs. The default is all channels.
   

.. _Examples:

Examples
   task examples
   
   (1) list mode: prints out a list of the internal mask(s) that
   exist in mymask.im to the log
   
   ::
   
      makemask(mode='list', inpimage='mymask.im')
   
    
   
   (2) copy mode: Regrid a Boolean (True/False) mask from one
   coordinate system to another and save as Boolean mask in the
   output image.   
   
   ::
   
      makemask(mode='copy', inpimage='oldmask.im',
      inpmask='oldmask.im:mask0', output='newmask.im:mask0')
   
    
   
   (3) copy mode: Same as (2), but save as integer (one/zero) mask in
   the output image.
   
   ::
   
      makemask(mode='copy', inpimage='oldmask.im',
      inpmask='oldmask.im:mask0', output='newmask.im')
   
   mask0 is translated so that pixels in oldmask.im that appears as
   'masked' in the viewer orhas the pixel mask value = False when
   extracted in imval, are to have pixel value of 1 inthe output
   image, newmask.im.
   
    
   
   (4) copy mode: Convert a Boolean mask to an integer mask in the
   same image
   
   ::
   
      makemask(mode='copy', inpimage='oldmask.im',
      inpmask='oldmask.im:mask0', output='', overwrite=True)
   
    
   
   (5) copy mode: Convert an integer mask to a Boolean mask in the
   same image
   
   ::
   
      makemask(mode='copy', inpimage='oldmask.im',
      inpmask='oldmask.im', output='oldmask.im:mask0')
   
    
   
   (6) copy mode: Copy a CRTF mask defined in mybox.txt to a Boolean
   mask in a new image
   
   ::
   
      makemask(mode='copy', inpimage='image1.im',
      inpmask='mybox.txt', output='image2.im:mask0')
   
   The pixel values of image1.im will be copied to image2.im and the
   region outside mybox.txt will be masked.
   
    
   
   (7) copy mode: Apply a region defined in a CRTF file to mask part
   of an image
   
   ::
   
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
   
   ::
   
      makemask(mode='copy', inpimage='image1.im',
      inpmask=['image1.im', image1.im:mask0','image2.mask:mask1',
      'circle[[15pix , 15pix] ,8pix ]'], output='newmask.im)
   
    
   
   (9) expand mode: Expand an integer mask from continuum imaging to
   use as an input mask image for spectral line imaging. Use an
   existing spectral line clean image as a template by specified in
   inpimage. The inpfreqs is left out as it uses a default (=[],
   means all channels).
   
   ::
   
      makemask(mode='expand', inpimage='spec.clean.image',
      inpmask='cont.clean.mask' outfreqs=[4,5,6,7],
      output='spec.clean.mask')
   
    
   
   (10) expand mode: Expand a Boolean mask from one range of channels
   to another range in the same image.
   
   ::
   
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
   
   ::
   
      makemask(mode='expand', inpimage='bigmask.im',
      inpmask='smallmask.im:mask0', inpfreqs='1.5MHz~1.6MHz',
      outfreqs='1.2MHz~1.8MHz', output='bigmask.im', overwrite=True)
   
   or to specify the ranges in velocities,
   
   ::
   
      makemask(mode='expand', inpimage='bigmask.im',
      inpmask='smallmask.im:mask0', inpfreqs=4.0km/s~0.5km/s',
      outfreqs='6.5km/s~-2.4km/s', output='bigmask.im',
      overwrite=True)
   
    
   
   (12) delete mode: Delete an internal mask from an image.
   
   ::
   
      makemask(mode='delete', inpmask='newmask.im:mask0')
   
    
   
   (13) setdefaultmask mode: Set an internal mask as a default
   internal mask.
   
   ::
   
      makemask(mode='setdefaultmask', inpmask='newmask.im:mask1')
   

.. _Development:

Development
   