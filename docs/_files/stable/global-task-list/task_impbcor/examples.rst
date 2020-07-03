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

      To correct an image for the primary beam response out to a radius
      where the sensitivity drops to 10% of the maximum value in the
      pointing center:

      .. container:: casa-input-box

         impbcor(imagename="attenuated.im", pbimage="mypb.im",
         outfile="pbcorred.im", mode="divide", cutoff=0.1)

.. container:: section
   :name: viewlet-below-content-body
