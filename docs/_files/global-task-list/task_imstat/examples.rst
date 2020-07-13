Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Select two-box region: box 1 (bottom-left coord is 2,3 and
      top-right coord is 14,15) and box 2 (bottom-left coord is 30,31
      and top-right coord is 42,43)

      .. container:: casa-input-box

         imstat('myImage', box='2,3,14,15;30,31,42,43')

      Select the same two box regions but only channels 4 and 5

      .. container:: casa-input-box

         imstat('myImage', box='2,3,14,15;30,31,42,43', chan='4~5')

      Select all channels greater than 20 as well as channel 0, then the
      mean and standard deviation are printed

      .. container:: casa-input-box

         | results = imstat('myImage', chans='>20;0')
         | print "Mean is: ", results['mean'], " s.d. ",
           results['sigma']

      Find statistical information for the Q stokes value only, then the
      I stokes values only, and printing out the statistical values that
      we are interested in

      .. container:: casa-input-box

         | s1 = imstat('myimage', stokes='Q')
         | s2 = imstat('myimage', stokes='I')
         | print " \| MIN \| MAX \| MEAN"
         | print " Q \| ",s1['min'][0]," \| ",s1['max'][0]," \| ",," \|
           ",s1['mean'][0]
         | print " I \| ",s2['min'][0]," \| ",s2['max'][0]," \| ",," \|
           ",s2['mean'][0]

      Evaluate statistics for each spectral plane in an ra x dec x
      frequency image

      .. container:: casa-input-box

         myim = "noisy.im"

         | # generate an image
         | ia.fromshape(myim, [20,30,40])
         | # give pixels non-zero values
         | ia.addnoise()
         | ia.done()
         | # These are the display axes, the calculation of statistics
           occurs
         | # for each (hyper)plane along axes not listed in the axes
           parameter,
         | # in this case axis 2 (the frequency axis)
         | # display the rms for each frequency plane (your mileage will
           vary with
         | # the values).
         | stats = imstat(imagename=myim, axes=[0,1])

       Printing the produced statistics using the desired KEY

      .. container:: casa-output-box

         | CASA <1>:stats["rms"]
         |   Out[10]:
         | array([ 0.99576014, 1.03813124, 0.97749186, 0.97587883,
           1.04189885,
         |         1.03784776, 1.03371549, 1.03153074, 1.00841606,
           0.947155 ,
         |         0.97335404, 0.94389403, 1.0010221 , 0.97151822,
           1.03942156,
         |         1.01158476, 0.96957082, 1.04212773, 1.00589049,
           0.98696715,
         |         1.00451481, 1.02307892, 1.03102005, 0.97334671,
           0.95209879,
         |         1.02088714, 0.96999902, 0.98661619, 1.01039267,
           0.96842754,
         |         0.99464947, 1.01536798, 1.02466023, 0.96956468,
           0.98090756,
         |         0.9835844 , 0.95698935, 1.05487967, 0.99846411,
           0.99634868])

.. container:: section
   :name: viewlet-below-content-body
