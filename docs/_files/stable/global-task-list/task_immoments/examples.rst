.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Example for creating the "moment 1" map, a map of the
      intensity-weighted mean spectral axis value, which is often used
      for finding velocity fields:

      .. container:: casa-input-box

         immoments(axis='spec', imagename='myimage', moment=[1],
         outfile='velocityfields')

       Example for finding the spectral mean, -1 moment, on a specified
      region of the image as defined by the *box* and *stokes*
      parameters:

      .. container:: casa-input-box

         | taskname='immoments'
         | default()
         | imagename = 'myimage'
         | moment = [-1]
         | axis = 'spec'
         | stokes = 'I'
         | box = '55,12,97,32'
         | go

      Example using a box

      .. container:: casa-input-box

         immoments('clean.image', axis='spec', box="40,40,120,120",
         outfile='mom_withmask.im')

      Example using a CRTF elliptical region with specified axis lengths
      and a position angle of 30 degrees.

      .. container:: casa-input-box

         immoments('clean.image', axis='spec',
         region="ellipse[[00:00:13.47460, +000.02.20.3571],
         [10arcsec,15arcsec], 30deg]", outfile='mom_withmask.im')

      Example using a mask created with a second file to select the data
      used to calculate the 0-moments, integrated values. In this case,
      the mask is from the calibrated.im file and all values that have a
      value greater than 0.5 will be positive in the mask:

      .. container:: casa-input-box

         immoments('clean.image', axis='spec',
         mask='"calibrated.im">0.5', outfile='mom_withmask.im')

.. container:: section
   :name: viewlet-below-content-body
