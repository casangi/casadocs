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

         # fit c0, c1, and c2 in a power log polynomial using two
         images. Do a pixel by pixel fit. Use initial estimates of
         c0=0.5, c1=2, and c2=0.1. Scale frequencies by dividing them by
         1GHz. Write the solution images.

         res = spxfit(imagename=["im0.im","im1.im"], multifit=True,
         spxtype="plp", spxest=[0.5,2,0.1], div="1GHz",
         spxsol="myplpsolutions.im")

.. container:: section
   :name: viewlet-below-content-body
