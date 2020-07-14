impbcor
=======

.. container:: documentDescription description

   impbcor task: Construct a primary beam corrected image from an image
   and a primary beam pattern.

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      Corrects an image for primary beam attenuation using an image of
      the primary beam pattern. The primary beam pattern can be provided
      as an image, in which case:

      #. it must have the same shape as the input image and its
         coordinate system must be the same, or
      #. it must be a 2-D image in which case its coordinate system must
         consist of a (2-D) direction coordinate which is the same as
         the direction coordinate in the input image and its direction
         plane must be the same shape as that of the input image.

      Alternatively, *pbimage* can be an array of pixel values in which
      case the same dimensionality and shape constraints apply.

      One can choose between dividing the image by the primary beam
      pattern (*mode="divide"*) or multiplying the image by the primary
      beam pattern (*mode="multiply"*). One can also choose to specify a
      cutoff limit for the primary beam pattern. For *mode="divide"*,
      for all pixels below this cutoff in the primary beam pattern, the
      output image will be masked. In the case of *mode="multiply"*, all
      pixels in the output will be masked corresponding to pixels with
      values greater than the cutoff in the primary beam pattern. A
      negative value for cutoff means that no cutoff will be applied,
      which is the default.

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_impbcor/changelog
   task_impbcor/examples
