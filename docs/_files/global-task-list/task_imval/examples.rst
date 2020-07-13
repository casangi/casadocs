Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: casa-input-box

         | # The value and mask value at a single point (5,17,2,Q)
         | imval( 'myImage', box='5,5,17,17', chans=2, stokes='Q' )
         | # Select and report on two box regions
         | # box 1, bottom-left coord is 2,3 and top-right coord is
           14,15
         | # box 2, bottom-left coord is 30,31 and top-right coord is
           42,43
         | # Note that only the boxes for the
         | imval( 'myImage', box='2,3,14,15;30,31,42,43' )
         | # Select the same two box regions but only channels 4 and 5
         | imval( 'myImage', box='2,3,14,15;30,31,42,43', chan='4~5' )
         | # Select all channels greater the 20 as well as channel 0.
         | # Then the mean and standard deviation are printed
         | # Note that the data returned is a Python numpy array which
         | # has built in operations such as min, max, and means as
         | # demonstrated here.
         | results = imval( 'myImage', chans='>20;0' )
         | imval_data=results['data']
         | mask=results['mask']
         | # holds the absolute coordinates of the associated pixels in
           imval_data
         | coords = results['coords']
         | print "Data max: ", imval_data.max(), " mean is ",
           imval_data.mean()
         | swapped_data=imval_data.swapaxes(0,2)
         | swapped_mask=mask.swapaxes(0,2)
         | print "Data values for 21st channel: \\n", swapped_data[0]
         | print "Mask values for 21st channel: \\n", swapped_mask[0]

.. container:: section
   :name: viewlet-below-content-body
