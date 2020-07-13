Parameters
==========

.. container:: documentDescription description

   task deconvolve parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               imagename : string

            Input image to deconvolve

Example

.. container:: param

   .. container:: parameters2

      model : string

   Output image containing deconvolved point model

Example

.. container:: param

   .. container:: parameters2

      psf : stringArray

   Point spread function (dirty beam)

Example

.. container:: param

   .. container:: parameters2

      alg : string = clark

   Algorithm to use (clark, hogbom, multiscale, mem)

Allowed Value(s)

clark hogbom mem multiscale

Example

.. container:: param

   .. container:: parameters2

      niter : int = 10

   number of iteration in deconvolution process

Allowed Value(s)

0

Example

.. container:: param

   .. container:: parameters2

      gain : double = 0.1

   CLEAN gain parameter

Allowed Value(s)

01.0

Example

.. container:: param

   .. container:: parameters2

      threshold : double = 0.0

   level below which sources will not be deconvolved

Example

.. container:: param

   .. container:: parameters2

      mask : string

   image mask to limit region of deconvolution

Example

.. container:: param

   .. container:: parameters2

      scales : intArray = 0310

   scale sizes (pixels) to deconvolve

Example

.. container:: param

   .. container:: parameters2

      sigma : double = 0.0

   mem parameter: Expected noise in image

Example

.. container:: param

   .. container:: parameters2

      targetflux : double = 1.0

   mem parameter: Estimated total flux in image

Example

.. container:: param

   .. container:: parameters2

      prior : string

   mem parameter: prior image for mem search

Example

.. container:: section
   :name: viewlet-below-content-body
