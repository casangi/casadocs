

.. _Returns:

   values (dict) - data and/or mask values in a given region, with
   their units, associated coordinates, bounding box corners, and axes


.. _Description:

Description
   Get the data value(s) and/or mask value in an image.
   
   The data point(s) to be retrieved are those found in the
   specified region, which may be:

   1. A region file or text string with the following caveat:
   
      -  If the specified region is complex (e.g., a union or
         intersection of multiple regions), only the first simple region
         in this set is used
      -  If the region is not rectangular, then the rectangular region
         that circumscribes the specified region (i.e., the bounding
         box) is used to retrieve values, since the returned arrays must
         be rectangular. The resulting mask values in this case are the
         result of "AND"ing the image mask values with the specified
         region mask values, e.g., if a pixel falls outside the
         specified region but within the bounding box, its returned mask
         value will be false even if its image mask value is true.
   
   2. A region specified by a set of rectangular pixel coordinates,
   the channel ranges and/or the Stokes. In this case, box="" will
   result in the details of the direction plane (i.e., RA/Dec or
   Galactic latitude/longitude) reference pixel to be returned in the
   selected frequency and stokes planes, while box="-1" will result
   in details for all pixels in the selected frequency and stokes
   planes being returned. Choosing a single pixel as box parameter will only work in cases where the third image axis (if present) is labelled 'FREQ'.
   
   Note that if only the pixel and/or mask values are required,
   ia.getchunk() and ia.getregion() also will provide these values.
   
   For directed output, run as:
   
   ::
   
      myoutput = imval()
   
   The general procedure to obtain data values of an image and
   display them is:
   
   ::
   
      # Specify inputs, then
      myoutput = imval()

      # or specify inputs directly in calling sequence to task
      myoutput = imval(imagename='image.im', etc)
      myoutput['KEYS'] #will contain the result associated with any
      of the keys given below
   
   +-----------------------------------+-----------------------------------+
   | KEYS                              | DESCRIPTION                       |
   +-----------------------------------+-----------------------------------+
   | blc                               | absolute PIXEL coordinates of the |
   |                                   | bottom left corner of the         |
   |                                   | bounding box surrounding the      |
   |                                   | selected region                   |
   +-----------------------------------+-----------------------------------+
   | trc                               | the absolute PIXEL coordinates of |
   |                                   | the top right corner of the       |
   |                                   | bounding box surrounding the      |
   |                                   | selected region                   |
   +-----------------------------------+-----------------------------------+
   | axes                              | list the data stored in each axis |
   |                                   | of the data block                 |
   +-----------------------------------+-----------------------------------+
   | unit                              | unit of the returned data values  |
   +-----------------------------------+-----------------------------------+
   | data                              | data value(s) found in the given  |
   |                                   | region                            |
   +-----------------------------------+-----------------------------------+
   | mask                              | mask value(s) found in the given  |
   |                                   | region. See important note above  |
   |                                   | regarding returned mask values    |
   |                                   | for non-rectangular regions.      |
   +-----------------------------------+-----------------------------------+
   | coords                            | The numerical values of the       |
   |                                   | coordinates associated with each  |
   |                                   | data value. Each set of           |
   |                                   | coordinate values is ordered      |
   |                                   | according to the coordinate axis  |
   |                                   | ordering.                         |
   +-----------------------------------+-----------------------------------+
   
   .. note:: NOTE: The data returned is in the same order as it is
      internally stored, typically RA, DEC, spectral, stokes. Also
      both the data and mask values are returned as Python Numpy
      arrays, for information on how to manipulate them see:
      `http:numpy.scipy.org/#array_interface <https://numpy.scipy.org/#array_interface>`__
   

.. _Examples:

Examples
   ::
   
      # The value and mask value at a single point (5,17,2,Q)
      imval( 'myImage', box='5,5,17,17', chans=2, stokes='Q' )

      # Select and report on two box regions
      # box 1, bottom-left coord is 2,3 and top-right coord is 14,15
      # box 2, bottom-left coord is 30,31 and top-right coord is 42,43
      # Note that only the boxes for the
      imval( 'myImage', box='2,3,14,15;30,31,42,43' )

      # Select the same two box regions but only channels 4 and 5
      imval( 'myImage', box='2,3,14,15;30,31,42,43', chan='4~5' )

      # Select all channels greater the 20 as well as channel 0.
      # Then the mean and standard deviation are printed
      # Note that the data returned is a Python numpy array which
      # has built in operations such as min, max, and means as
      # demonstrated here.
      results = imval( 'myImage', chans='>20;0' )
      imval_data=results['data']
      mask=results['mask']

      # holds the absolute coordinates of the associated pixels in imval_data
      coords = results['coords']
      print "Data max: ", imval_data.max(), " mean is ",
      imval_data.mean()
      swapped_data=imval_data.swapaxes(0,2)
      swapped_mask=mask.swapaxes(0,2)
      print "Data values for 21st channel: \\n", swapped_data[0]
      print "Mask values for 21st channel: \\n", swapped_mask[0]
   

.. _Development:

Development
   No additional development details

