.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Examples
========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task examples

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: casa-input-box

         | # boxcar smooth the spectral axis by 3 pixels,
         | # say it's axis 2 and only write every other pixel
         | specsmooth(imagename="mynonsmoothed.im",
           outfile="myboxcarsmoothed.im",
         | axis=2, function="boxcar", dmethod="copy", width=3,
           overwrite=True)

      .. container:: casa-input-box

         | # hanning smooth the spectral axis,
         | # say it's axis 2 and do not perform decimation of image
           planes
         | specsmooth(imagename="mynonsmoothed.im",
           outfile="myhanningsmoothed.im",
         | axis=2, dmethod=""," overwrite=True)

.. container:: section
   :name: viewlet-below-content-body
