#
# stub function definition file for docstring parsing
#

def makemask(mode='list', inpimage='', inpmask='', output='', overwrite=False, inpfreqs='', outfreqs=''):
    """
Makes and manipulates image masks

| Construct masks based on various criteria, convert between mask-types, and generate a mask for clean

Parameters
----------
mode : string
   Mask method (list, copy,expand,delete,setdefaultmask)

Other Parameters
----------
inpimage : string, stringArray
   Name of input image.
inpmask : string, stringArray
   mask(s) to be processed: image masks,T/F internal masks(Need to include parent image names),regions(for copy mode)
output : string
   Name of output mask (imagename or imagename:internal_maskname)
overwrite : bool
   overwrite output if exists?
inpfreqs : string, intArray
   List of chans/freqs (in inpmask) to read masks from 
outfreqs : string, intArray
   List of chans/freqs (in output) on which to expand the mask

Notes
-----





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
         :name: parameter-descriptions
         :class: p1

      .. rubric:: *mode*
         :name: mode

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
         :name: inpimage

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
         :name: expandable-parameters-for-modecopy-expand-delete-and-setdefaultmask

      .. rubric:: inpmask
         :name: inpmask
         :class: p1

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
         :name: output

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
         :name: overwrite
         :class: p1

      Overwrite the mask specified in output (see also the output rules
      above). The default value is False.

      .. note:: NOTE: For a cube mask, overwrite=True generally overwrites in
         the specified channel planes only and so any pre-existed masks
         in other channels will be remain untouched.

       

      .. rubric:: Additional expandable parameters for mode='expand'
         :name: additional-expandable-parameters-for-modeexpand
         :class: p1

      .. rubric:: inpfreqs
         :name: inpfreqs
         :class: p1

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
         :name: outfreqs
         :class: p1

      Output channel/frequency/velocity range. Specify same way as
      inpfreqs. The default is all channels.

    """
    pass
