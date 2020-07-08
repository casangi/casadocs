.. container::
   :name: viewlet-above-content-title

imval
=====

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   imval task: Get the data value(s) and/or mask value in an image.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Get the data value(s) and/or mask value in an image.

      | The data point(s) to be retrieved are those found in the
        specified region, which may be:
      | 1. A region file or text string with the following caveat:

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
      planes being returned.

      Note that if only the pixel and/or mask values are required,
      ia.getchunk() and ia.getregion() also will provide these values.

      For directed output, run as:

      .. container:: casa-input-box

         myoutput = imval()

      The general procedure to obtain data values of an image and
      display them is:

      .. container:: casa-input-box

         #Specify inputs, then
         myoutput = imval()
         #or specify inputs directly in calling sequence to task
         myoutput = imval(imagename='image.im', etc)
         myoutput['KEYS'] #will contain the result associated with any
         of the keys given below

      +-----------------------------------+-----------------------------------+
      | KEYS                              | DESCRIPTION                       |
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

      .. container:: info-box

         NOTE: The data returned is in the same order as it is
         internally stored, typically RA, DEC, spectral, stokes. Also
         both the data and mask values are returned as Python Numpy
         arrays, for information on how to manipulate them see:
         `http:numpy.scipy.org/#array_interface <https://numpy.scipy.org/#array_interface>`__

.. container:: section
   :name: viewlet-below-content-body


.. toctree::
   :hidden:
   :maxdepth: 3

   task_imval/about
   task_imval/parameters
   task_imval/changelog
   task_imval/examples
   task_imval/developer