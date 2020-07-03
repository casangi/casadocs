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

      Fit a second order polynomial (fitorder=2) to channels 3-8 and
      54-60 to an RA x Dec x Frequency x Stokes cube, selecting the
      Stokes I plane

      .. container:: casa-input-box

         | ch = '3~8, 54~60'
         | imcontsub(imagename="myimage.im", linefile="mycontsub.im",
           fitorder=2, chans=ch, fitorder=2, stokes="I")

.. container:: section
   :name: viewlet-below-content-body
