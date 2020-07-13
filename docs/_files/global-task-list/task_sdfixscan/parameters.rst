Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               infiles : undefined = ''

            list of name of input SD images (FITS or CASA image)

Example

.. container:: param

   .. container:: parameters2

      mode : string = fft_mask

   image processing mode

Allowed Value(s)

fft_mask model

Example

.. container:: param

   .. container:: parameters2

      numpoly : int = 2

   order of polynomial fit for Pressed-out method

Example

.. container:: param

   .. container:: parameters2

      beamsize : double = 0.0

   beam size for Pressed-out method

Example

.. container:: param

   .. container:: parameters2

      smoothsize : undefined = 2.0

   size of smoothing beam for Pressed-out method

Example

.. container:: param

   .. container:: parameters2

      direction : undefined

   scan direction (p.a.) counterclockwise from the horizontal axis in
   unit of degree

Example

.. container:: param

   .. container:: parameters2

      maskwidth : undefined = 1.0

   mask width for Basket-Weaving (on percentage)

Example

.. container:: param

   .. container:: parameters2

      tmax : double = 0.0

   maximum threshold value for processing

Example

.. container:: param

   .. container:: parameters2

      tmin : double = 0.0

   minimum threshold value for processing

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   name of output file

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   overwrite the output file if already exists

Example

.. container:: section
   :name: viewlet-below-content-body
