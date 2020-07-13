Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. container:: casa-input-box

         | # rebin the first two axes (normally the direction axes)
         | imrebin(imagename="my.im", outfile="rebinned.im",
           factor=[2,3])
         | # rebin the frequency axis, which is the fourth axis in this
           image
         | imrebin(imagename="my2.im", outfile="rebinned2.im",
           factor=[1,1,1,4])

.. container:: section
   :name: viewlet-below-content-body
