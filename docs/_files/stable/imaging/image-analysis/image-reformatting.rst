.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Reformat Images
===============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Resizing, binning, regridding, and collapsing images

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This page contains a description of various tasks that reformat
      images.  These include:

      -  **imsubimage:** enables the user to extract a sub-image from a
         larger cube,
      -  **imtrans:** changes the axis order in an image,
      -  **imregrid:** sets the image onto a different spatial
         coordinate system or spectral grid,
      -  **imreframe:** changes the velocity system of an image
      -  **imrebin:** rebins an image in a spatial or
         spectral dimension 
      -  **imcollapse:** collapses an image along an axis. 

       

      .. rubric:: Extracting sub-images (**imsubimage**)
         :name: extracting-sub-images-imsubimage

      The task **imsubimage** provides a way to extract a smaller data
      cube from a bigger one. The inputs are:

      .. container:: casa-input-box

         | 
         | # imsubimage :: Create a (sub)image from a region of the
           image
         | imagename      =    ''    # Input image name. Default is
           unset.
         | outfile        =    ''    # Output image name. Default is
           unset.
         | box            =    ''    # Rectangular region to select in
         |                           # direction plane. Default is to
           use the
         |                           # entire direction plane.
         | region         =    ''    # Region selection. Default is to
           use the
         |                           # full image.
         | chans          =    ''    # Channels to use. Default is to
           use all
         |                           # channels.
         | stokes         =    ''    # Stokes planes to use. Default is
           to use
         |                           # all Stokes planes.
         | mask           =    ''    # Mask to use. Default is none.
         | dropdeg        =  True    # Drop degenerate axes
         |      keepaxes  =    []    # If dropdeg=True, these are the
         |                           # degenerate axes to keep.
           Nondegenerate
         |                           # axes are implicitly always kept.

         | verbose        =   True   # Post additional informative
           messages to
         |                           # the logger

      The *region* keyword defines the size of the smaller cube and is
      specified via the CASA region CRTF syntax. E.g.

      .. container:: casa-input-box

         region='box [ [ 100pix , 130pix] , [120pix, 150pix ] ]'

      will extract the portion of the image that is between pixel
      coordinates (100,130) and (12,150). *dropdeg=T* with selection via
      *keepaxes* is useful to remove axes in the data cube that are
      degenerate, i.e. axes with a single plane only. A single Stokes I
      axis is a common example.

       

       

      .. rubric:: Reordering the Axes of an Image Cube (**imtrans**)
         :name: reordering-the-axes-of-an-image-cube-imtrans

      Sometimes data cubes can be in axis orders that are not adequate
      for processing. The CASA task **imtrans** can change the ordering
      of the axis:

      .. container:: casa-input-box

         | #  imtrans :: Reorder image axes
         | imagename           =         ''        #  Name of the input
           image
         | outfile             =         ''        #  Name of output
           CASA image.
         | order               =         ''        #  New zero-based
           axes order.
         | wantreturn          =       True        #  Return an image
           tool referencing the
         |                                         #   transposed image

      | The *order* parameter is the most important input here. It is a
        string of numbers that shows how axes 0, 1, 2, 3, ... are mapped
        onto the new cube (note that the first axis has the label 0, as
        typical in python). E.g. *order='1032'* will reorder the input
        axis 0 to be axis 1 in the output, input axis 1 to be output
        axis 0, input axis 2 to output axis 3 (the last axis) and input
        axis 3 to output axis 2. Alternatively, axes can be specified by
        their names. E.g., to reorder an image with right ascension,
        declination, and frequency and reverse the first two,
        *order=[‘‘declination’’, ‘‘right ascension’’, ‘‘frequency’’]*
        will work. The axes names can be found typing
        **ia.coordsys**.\ **names**. Minimum match is supported, so that
        *order=['d', 'f', 'r']* will produce the same results.
      | Axes can simultaneously be transposed and reversed. To reverse
        an axis, precede it by a '-'. For example, *order='-10-32'* will
        reverse the direction of the first and third axis of the input
        image (the zeroth and second axes in the output image).
      | Example (swap the stokes and spectral axes in an
        RA-Dec-Stokes-Frequency image):

      .. container:: casa-input-box

         | imagename = 'myim.im'
         | outfile = 'outim.im'
         | order = '0132'
         | imtrans()

      or

      .. container:: casa-input-box

         | outfile = 'myim_2.im'
         | order = 132
         | imtrans()

      or

      .. container:: casa-input-box

         | outfile = 'myim_3.im'
         | order = ['r', 'd', 'f', 's']
         | imtrans()

      or

      .. container:: casa-input-box

         | outfile = 'myim_4.im'
         | order = ['rig', 'declin', 'frequ', 'stok']
         | imtrans()

      If the *outfile* parameter is empty, only a temporary image is
      created; no output image is written to disk. The temporary image
      can be captured in the returned value (assuming
      *wantreturn*\ =T\ *rue*).

        

      .. rubric:: Regridding an Image (imregrid)
         :name: regridding-an-image-imregrid

      .. container:: info-box

         **Inside the Toolkit:** More complex coordinate system and
         image regridding operation can be carried out in the toolkit.
         The **coordsys** (**cs**) tool and the **ia.regrid** method are
         the relevant components.

      It is occasionally necessary to regrid an image onto a new
      coordinate system. The **imregrid** task will regrid one image
      onto the coordinate system of another, creating an output image.
      In this task, the user need only specify the names of the input,
      template, and output images. The default inputs are:

      .. container:: casa-input-box

         | 
         | #  imregrid :: regrid an image onto a template image
         | imagename           =         ''        #  Name of the source
           image
         | template            =      'get'        #  A dictionary,
           refcode, or name of an
         |                                         #   image that
           provides the output shape
         |                                         #   and coordinate
           system
         | output              =         ''        #  Name for the
           regridded image
         | asvelocity          =       True        #  Regrid spectral
           axis in velocity space
         |                                         #   rather than
           frequency space?
         | axes                =       [-1]        #  The pixel axes to
           regrid. -1 => all.
         | interpolation       =   'linear'        #  The interpolation
           method.  One of
         |                                         #   'nearest',
           'linear', 'cubic'.
         | decimate            =         10        #  Decimation factor
           for coordinate grid
         |                                         #   computation
         | replicate           =      False        #  Replicate image
           rather than regrid?
         | overwrite           =      False        #  Overwrite
           (unprompted) pre-existing
         |                                         #   output file?

      The output image will have the data in *imagename* regridded onto
      the coordinate system provided by the *template* parameter.
      *template* is used universally for a range of ways to define the
      grid of the output image: 

      -  a template image: specify an image name here and the input will
         be regridded to the same 3-dimensional coordinate system as the
         one in template. Values are filled in as blanks if they do not
         exist in the input. Note that the input and template images
         must have the same coordinate structure to begin with (like 3
         or 4 axes, with the same ordering)
      -  a coordinate system (reference code): to convert from one
         coordinate frame to another one, e.g. from B1950 to J2000, the
         template parameter can be used to specify the output coordinate
         system. These following recognized keywords are supported:
         'J2000', 'B1950', 'B1950_VLA', 'GALACTIC', 'HADEC', 'AZEL',
         'AZELSW', 'AZELNE', 'ECLIPTIC', 'MECLIPTIC', 'TECLIPTIC',
         'SUPERGAL'
      -  '*get'*: This option returns a python dictionary in the
         {’csys’: csys_record, ’shap’: shape} format
      -  a python dictionary: In turn, such a dictionary can be used as
         a template to define the final grid

      .. rubric:: 
         Redefining the Velocity System of an Image (**imreframe**)
         :name: redefining-the-velocity-system-of-an-image-imreframe

      **imreframe** can be used to change the velocity system of an
      image. It is not applying a regridding as a change from radio to
      optical conventions would require, but it will change the labels
      of the velocity axes.

      .. container:: casa-input-box

         | #  imreframe :: Change the frame in which the image reports
           its spectral values
         | imagename           =         ''        #  Name of the input
           image
         | output              =         ''        #  Name of the output
           image; '' => modify input image
         | outframe            =     'lsrk'        #  Spectral frame in
           which the frequency or velocity
         |                                         #   values will be
           reported by default
         | restfreq            =         ''        #  restfrequency to
           use for velocity values (e.g.
         |                                         #   '1.420GHz' for
           the HI line)

      *outframe* defines the velocity frame (LSRK, BARY, etc.,) of the
      output image and a rest frequency should be specified to relabel
      the spectral axis in new velocity units.

      .. rubric:: 
         Rebin an Image (**imrebin**)
         :name: rebin-an-image-imrebin

      The task **imrebin** allows one to rebin an image in any spatial
      or spectral direction:

      .. container:: casa-input-box

         | imrebin :: Rebin an image by the specified integer factors
         | imagename           =         ''        #  Name of the input
           image
         | outfile             =         ''        #  Output image name.
         | factor              =         []        #  Binning factors
           for each axis. Use
         |                                         #   imhead or
           ia.summary to determine axis
         |                                         #   ordering.
         | region              =         ''        #  Region selection.
           Default is to use the full
         |                                         #   image.
         | box                 =         ''        #  Rectangular region
           to select in
         |                                         #   direction
           plane. Default is to use the entire
         |                                         #   direction plane.
         | chans               =         ''        #  Channels to use.
           Default is to use all
         |                                         #   channels.
         | stokes              =         ''        #  Stokes planes to
           use. Default is to
         |                                         #   use all Stokes
           planes. Stokes planes
         |                                         #   cannot be
           rebinned.
         | mask                =         ''        #  Mask to use.
           Default is none.
         | dropdeg             =      False        #  Drop degenerate
           axes?
         | crop                =       True        #  Remove pixels from
           the end of an axis to
         |                                         #   be rebinned if
           there are not enough to
         |                                         #   form an integral
           bin?

      | where *factor* is a list of integers that provides the numbers
        of pixels to be binned for each axis. The *crop* parameters
        controls how pixels at the boundaries are treated if the bin
        values are not multiple integers of the image dimensions.
      | Example:

      .. container:: casa-input-box

         imrebin(imagename='my.im', outfile='rebinned.im',
         factor=[1,2,1,4], crop=T)

      This leaves RA untouched, bins DEC by a factor of 2, leaves Stokes
      as is, and bins the spectral axis by a factor of 4. If the input
      image has a spectral axis with a length that is not a multiple of
      4, the *crop=T* setting will discard the remaining 1-3 edge
      pixels.

       

       

      .. rubric:: Collapsing an Image Along an Axis (**imcollapse**)
         :name: collapsing-an-image-along-an-axis-imcollapse

      **imcollapse** allows to apply an aggregation function along one
      or more axes of an image. Functions supported are '*max', 'mean',
      'median', 'min', 'rms', 'stdev', 'sum', 'variance'* (minimum match
      supported). The relevant axes will then collapse to a single value
      or plane (i.e. they will result in a degenerate axis). The
      functions are specified in the *function* parameter of the
      **imcollapse** inputs:

      .. container:: casa-input-box

         | #  imcollapse :: Collapse image along one axis, aggregating
           pixel values along that axis.
         | imagename           =         ''        #  Name of the input
           image
         | function            =         ''        #  Function used to
           compute aggregation
         |                                         #   of pixel values.
         | axes                =        [0]        #  Zero-based axis
           number(s) or minimal
         |                                         #   match strings to
           collapse.
         | outfile             =         ''        #  Name of output
           CASA image.
         | box                 =         ''        #  Optional direction
           plane box ('blcx,
         |                                         #   blcy, trcx
           trcy').
         |      region         =         ''        #  Name of optional
           region file to use.
         | chans               =         ''        #  Optional
           zero-based contiguous
         |                                         #   frequency channel
           specification.
         | stokes              =         ''        #  Optional
           contiguous stokes planes
         |                                         #   specification.
         | mask                =         ''        #  Optional mask to
           use.
         | wantreturn          =       True        #  Should an image
           analysis tool
         |                                         #   referencing the
           collapsed image be
         |                                         #   returned?

      | *wantreturn=True* returns an image analysis tool containing the
        newly created collapsed image.
      | Example (myimage.im is a 512x512x128x4 (ra,dec,freq,stokes; i.e.
        in the 0-based system, frequency is labeled as axis 2) image and
        we want to collapse a subimage of it along its spectral axis
        avoiding the 8 edge channels at each end of the band, computing
        the mean value of the pixels (resulting image is 256x256x1x4 in
        size)):

      .. container:: casa-input-box

         | imcollapse(imagename='myimage.im',
           outfile='collapse_spec_mean.im',
         |            function='mean', axis=2, box='127,127,383,383',
           chans='8~119')

      Note that **imcollapse** will not smooth to a common beam for all
      planes if they differ. If this is desired, run **imsmooth** before
      **imcollapse**.

       

.. container:: section
   :name: viewlet-below-content-body
