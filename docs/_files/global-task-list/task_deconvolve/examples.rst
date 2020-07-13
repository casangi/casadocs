Examples
========

.. container:: documentDescription description

   task deconvolve examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Deconvolve the dirty image 'mydirtyimage.image' with a dirty beam
      (psf) 'mydirtyimage.psf'. No MS is required as only minor cycles
      are performed. We are using the 'multiscale' clean algorithm with
      scales of 0, 3, and 10 pixels. The stopping criteria are either
      10000 iterations, or an RMS threshold of 10mJy: 

      .. container:: casa-input-box

         deconvolve(imagename='mydirtyimage.image',
         model='mycleanimage.image', psf='mydirtyimage.psf',
         alg='multiscale', scales=[0,3,10], niter=10000, gain=0.1,
         threshold='10mJy')

       

       

.. container:: section
   :name: viewlet-below-content-body
