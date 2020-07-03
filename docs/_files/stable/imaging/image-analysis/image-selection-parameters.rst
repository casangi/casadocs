.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Image Selection Parameters
==========================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Select parts of an image with the box, chans, and stokes parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Many of the image analysis tasks contain a set of parameters that
      can be used to define a sub-section of an image that the task
      works on. This includes selection in the spatial coordinates,
      typically RA/DEC or GLON/GLAT (or image axes 0,1) which can be
      defined by the *box* parameter. Spectral selection can be achieved
      by the *chans* parameter (typically axis 3) and Stokes selection
      with the *stokes* parameter (typically axis 2). These parameters
      are described below and are a quick way to select sub-images. For
      more complicated selections, we recommend the usage of the `CASA
      region
      file <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-files>`__
      (`CRTF
      file <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/region-file-format>`__).
         

       

      .. rubric:: Region Selection (*box*)
         :name: region-selection-box

      Direction (e.g. RA, Dec) areal selection in the image analysis
      tasks is controlled by the *box* parameter or through the *region*
      parameter. Note that one should either specify a region
      (recommended) or any of *box*/*chans*/*stokes* parameters.
      Specifying both at the same time will give priority to the command
      line inputs in 'chans' and 'stokes' but will keep the region file
      specification for the spatial region selection.

      The *box* parameter selects spatial rectangular areas:

      .. container:: casa-input-box

         box        =      ''   #  Select one or more box regions

      E.g. for right ascension and declination. Boxes are specified by
      their bottom-left corner (blc) and top-right corner (trc) as
      follows: blcx, blcy, trcx, trcy. At the moment, CASA only accepts
      pixel values. The default (empty string) is to select all pixels
      of an image.

      Example:

      .. container:: casa-input-box

         box='0,0,50,50'

      selects a square with 50 pixels on the side starting at 0.

      .. container:: casa-input-box

         box='10,20,30,40,100,100,150,150'

      selects two regions at a time. The first and the last four values
      mark the two boxes, following (blcx1, blcy1, trcx1, trcy1, blcx2,
      blcy2, trcx2, trcy2), with b/t = bottom/top and l/r = left/right.

      .. container:: alert-box

         | **ALERT:** Note that one should either specify a region
           (recommended) or any of *box*/*chans*/*stokes*. If both are
           specified, the following rules apply:
         |           \* If the *region* parameter is specified as a
           python dictionary (e.g. such as various **rg** tool methods
           return), a binary region file, or a region-in-image, it is
           not permissible to specify any of the *box*, *chans*, or
           *stokes* parameters.
         |           \* If the *region* parameter is specified to be a
           CRTF file name, or a CRTF region string, then the resulting
           *region* and *box* selection is the union of the box
           specification with any regions in the CRTF file/string. This
           is the equivalent of translating the box specification into
           the equivalent "box" CRTF specification and prepending that
           specification to the specified CRTF file/string in the
           *region* parameter.

      .. rubric:: Plane Selection (*chans*, *stokes*)
         :name: plane-selection-chans-stokes

      The channel, frequency, or velocity plane(s) of the image is
      chosen using the *chans* parameter:

      .. container:: casa-input-box

         chans      =      ''   #  Select the channel(spectral) range

      Using channel numbers, it is possible to also set ranges, e.g.\ *
      *

      .. container:: casa-input-box

         | chans='0,3,4,8'          # select channels 0, 3, 4, 8
         | chans='3~20;50,51'       # channels 3 to 20 and 50 and 51
         | chans='<10;>=55'         # channels 0 to 9 and 55 and greater
           (inclusively)\ *
           *

      Sometimes, as in the **immoments** task, the channel/plane
      selection is generalized to work on more than one axis type. In
      this case, the *planes* parameter is used. This behaves like
      *chans* in syntax.

      *chans* can also be set in the CASA region format to allow
      settings in frequency and velocity, e.g.

      .. container:: casa-input-box

          chans=('range=[-50km/s,50km/s], restfreq=100GHz, frame=LSRK')

      This example would even define a new velocity system independent
      of the one in the image itself. If the rest frequency and velocity
      frame within the image are being used, the latter two entries are
      not needed. The parentheses are needed when the call is in a
      single command.

      A frequency selection looks like:

      .. container:: casa-input-box

         chans=('range=[100GHz,100.125GHz]')

      The polarization plane(s) of the image is chosen with the *stokes*
      parameter:

      .. container:: casa-input-box

         stokes     =      ''   #  Stokes params to image
         (I,IV,IQU,IQUV)

      *stokes* parameters to image. Best practice is to separate the
      stokes parameters by commas, but this is not essential if no
      ambiguity exists. Options are: 'I','Q','U','V',
      'I','IV','QU','IQUV', 'RR','RL','LR','LL', 'XX','YX','XY','YY',...

      Examples:

      .. container:: casa-input-box

         | stokes='IQUV';  
         | stokes='I,Q'
         | stokes='RR,RL'

      .. container:: alert-box

         | **ALERT:** For image analysis tasks and tool methods which
           also accept the *region* parameter, the following rules apply
           if both the *chans* and *region* parameters are
           simultaneously specified:
         |     \* If the *region* parameter is specified as a python
           dictionary (e.g. such as various **rg** tool methods return),
           a binary region file, or a region-in-image, it is not
           permissable to specify any of the *box*, *chans*, or *stokes*
           parameters.
         |     \* If the *region* parameter is specified to be a CRTF
           file name, or a CRTF region string, it is only permissable to
           specify *chans* if that specification can be represented as a
           single contiguous channel range. In that case, the *chans*
           specification overrides any global or per-region range
           specification in the CRTF file/string, and is used as the
           global spectral range selection for all regions in the CRTF
           file/string.

       

.. container:: section
   :name: viewlet-below-content-body
