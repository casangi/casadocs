

.. _Description:

Description
   imtrans task: Reorder image axes
   
   This task reorders (transposes) the axes in the input image to the
   specified order. The associated pixel values and coordinate system
   are transposed.
   
   The *order* parameter describes the mapping of the input axes to
   the output axes. It can be one of three types: a non-negative
   integer, a string, or a list of strings. If a string or
   non-negative integer, it should contain zero-based digits
   describing the new order of the input axes. It must contain the
   same number of (unique) digits as the number of input axes. For
   example, specifying *order="1032"* or *order=1032* for a four axes
   image maps input axes 1, 0, 3, 2 to output axes 0, 1, 2, 3. In the
   case of order being a nonnegative integer and the zeroth axis in
   the input being mapped to zeroth axis in the output, the zeroth
   digit is implicitly understood to be 0, so that to transpose an
   image where one would use a string *order="0321"*, one could
   equivalently specify an int *order=321*. IMPORTANT: When
   specifying a non-negative integer and mapping the zeroth axis of
   the input to the zeroth axis of the output, do **not** explicitly
   specify the leading 0; e.g., specify *order=321* rather than
   *order=0321*. Python interprets an integer with a leading 0 as an
   octal number.
   
   Because of ambiguity for axes numbers greater than nine, using
   string or integer order specifications cannot handle images
   containing more than 10 axes. The order parameter can also be
   specified as a list of strings which uniquely match, ignoring
   case, the first characters of the image axis names
   (ia.coordsys().names()). So to reorder an image with right
   ascension, declination, and frequency axes, one could specify
   *order=["d", "f", "r"]* or equivalently *["decl", "frequ", "right
   a"]*. Note that specifying "ra" for the right ascension axis will
   result in an error because "ra" does not match the first two
   characters of "right ascension". Axes can be simultaneously
   inverted in cases where order is a string or an array of strings
   by specifying negative signs in front of the axis/axes to be
   inverted. So, in a 4-D image, *order="-10-3-2"* maps input axes 1,
   0, 3, 2 to output axes 0, 1, 2, 3 and reverses the direction and
   values of input axes 1, 3, and 2.
   

.. _Examples:

Examples
   task examples
   
   ::
   
         # Swap the stokes and spectral axes in an
         RA-Dec-Stokes-Frequency image
         imagename = "myim.im"
         outfile = "outim.im"
         order = "0132"
         imtrans()
         # or
         outfile = "myim_2.im"
         order = 132
         imtrans()
         # or
         outfile = "myim_3.im"
         order = ["r", "d", "f", "s"]
         imtrans()
         # or
         outfile = "myim_4.im"
         order = ["rig", "declin", "frequ", "stok"]
         imtrans()
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   