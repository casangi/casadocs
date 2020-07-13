impv
====

.. container:: documentDescription description

   impv task: Construct a position-velocity image by choosing two points
   in the direction plane.

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Create a position-velocity image. The way the slice is specified
      is controlled by the *mode* parameter. When *mode="coords"*, start
      and end are used to specify the points between which slice is
      taken in the direction coordinate. If *mode="length",* *center, pa
      (position angle),* and *length* are used to specify the slice.
      Note that impv will treat any string starting with "c" as
      *"coords"* and any string starting with "l" as *"length".* The
      spectral extent of the resulting image will be that provided by
      the *region* specification or the entire spectral range of the
      input image if no *region* is specified. One may not specify a
      *region* in direction space; that is accomplished by specifying
      the slice as described previously.

      The parameters *start* and *end* may be specified as two element
      arrays of numerical values, in which case these values will be
      interpreted as pixel locations in the input image. Alternatively,
      they may be expressed as arrays of two strings each representing
      the direction. These strings can either represent quantities (e.g.
      ["40.5deg", "0.5rad") or be sexigesimal format (e.g.
      ["14h20m20.5s","-30d45m25.4s"], ["14:20:20.5s","-30.45.25.4"]). In
      addition, they may be expressed as a single string containing the
      longitude-like and latitude-like values and optionally a reference
      frame value, e.g. "J2000 14:20:20.5s -30.45.25.4".The *center*
      parameter can be specified in the same way. The *length* parameter
      may be specified as a single numerical value, in which case it is
      interpreted as the length in pixels, or a valid quantity, in which
      case it must have units conformant with the direction axes units.
      The *pa* (position angle) parameter must be specified as a valid
      quantity with angular units. The position angle is interpreted in
      the usual astronomical sense; e.g. measured from north through
      east in an equatorial coordinate system. The slice in this case
      starts at the specified position angle and ends on the opposite
      side of the specified center. Thus *pa="45deg"* means start at a
      point at a *pa* of 45 degrees relative to the specified center and
      end at a point at a *pa* of 225 degrees relative to the center.
      Either *start/end* or *center/pa/length* must be specified; if a
      parameter from one of these sets is specified, a parameter from
      the other set may not be specified. In either case, the *end*
      points of the segment must fall within the input image, and they
      both must be at least 2 pixels from the edge of the input image to
      facilite rotation (see below).

      | One may specify a *width*, which represents the number of pixels
        centered along and perpendicular to the direction slice that are
        used for averaging along the slice. The *width* may be specified
        as an integer, in which case it must be positive and odd.
        Alternatively, it may be specified as a valid quantity string
        (e.g., "4arcsec") or quantity record (e.g.
        qa.quantity("4arcsec")). In this case, units must be conformant
        to the direction axes units (usually angular units) and the
        specified quantity will be rounded up, if necessary, to the next
        highest equivalent odd integer number of pixels. The default
        value of 1 represents no averaging. A value of 3 means average
        one pixel on each side of the slice and the pixel on the slice.
        Note that this *width* is applied to pixels in the image after
        it has been rotated (see below for a description of how rotation
        is applied).
      | One may specify the *unit* for the angular offset axis.
      | Internally, the image is first rotated, padding if necessary to
        include relevant pixels that would otherwise be excluded by the
        rotation operation, so that the slice is horizontal, with the
        starting pixel left of the ending pixel. Then, the pixels within
        the specified width of the slice are averaged and the resulting
        image is written and/or returned. The output image has a linear
        coordinate in place of the direction coordinate of the input
        image, and the corresponding axis represents angular offset with
        the center pixel having a value of 0.
      | The equivalent coordinate system, with a (usually) rotated
        direction coordinate (e.g., RA and Dec) is written to the output
        image as a table record. It can be retrieved using the table
        tool (see the examples tab, which is linked from the top of this
        page).

      Note that because the ouput image does not have a direction
      coordinate, other image analysis tasks and tool methods may not be
      able to process it correctly if it is used as an input image. In
      such cases when possible, the task or tool method in question
      should be first run on the input image that would have been used
      in impv, and then impv should be run using as the input image, the
      output image from the task or tool method in question. That is,
      the output image of impv should normally be considered to be the
      end point of any image analysis sequence for tasks/tool methods.

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_impv/parameters
   task_impv/changelog
   task_impv/examples
