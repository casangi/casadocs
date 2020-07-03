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

      .. rubric:: Example: Collapse a Subimage Along the Spectral Axis
         :name: example-collapse-a-subimage-along-the-spectral-axis

      For this example, myimage.im is a 512x512x128x4
      (ra,dec,freq,stokes) image.

      .. container:: casa-input-box

         imagename = "myimage.im"

      We want to only collapse the central 256x256 pixel region, so we
      define a box for the subregion.  Similarly, we avoid the 8 edge
      channels at each end of the band. These are often noisy from the
      imaging process.

      .. container:: casa-input-box

         | box="127,127,383,383"
         | chans="8~119"

      We specify to collapse along the spectral axis (zero based
      index),  and to use the "mean" algorithm.

      .. container:: casa-input-box

         | function="mean"
         | axis=2

      And finally we specify the output image name and call the
      **imcollapse** function.

      .. container:: casa-input-box

         | outfile="collapse_spec_mean.im"
         | imcollapse(imagename=imagename, outfile=outfile,
           function=function, axes=axis, box=box, chans=chans)

      The resulting image (collapse_spec_mean.im) is 256x256x1x4 in
      size.

.. container:: section
   :name: viewlet-below-content-body
