.. container::
   :name: viewlet-above-content-title

Description
===========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   imsubimage task: Create a (sub)image from a region of the image

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      This task copies all or part of the image to a new image specified
      by *outfile*. Both float and complex valued images are supported.

      Sometimes it is useful to drop axes of length one (degenerate
      axes). Set *dropdeg* equal to True if you want to do this.

      The output mask is the union (logical AND) of the default input
      pixel mask (if any) and the OTF mask. Any other input pixel masks
      will not be copied. Use function **ia.maskhandler** if you need to
      copy other masks too.

      If the mask has fewer dimensions than the image and if the shape
      of the dimensions the mask and image have in common are the same,
      the mask will automatically have the missing dimensions added so
      it conforms to the image.

      If *stretch=True* and if the number of mask dimensions is less
      than or equal to the number of image dimensions and some axes in
      the mask are degenerate while the corresponding axes in the image
      are not, the mask will be stretched in the degenerate dimensions.
      For example, if the input image has shape [100, 200, 10] and the
      input mask has shape [100, 200, 1] and *stretch=True*, the mask
      will be stretched along the third dimension to shape [100, 200,
      10]. However if the mask has shape [100, 200, 2], stretching is
      not possible and an error will result.

       

      .. rubric:: Task-specific parameters
         :name: task-specific-parameters

      .. rubric:: *dropdeg*
         :name: dropdeg

      Exclude axes from output image if they would have a length of one
      pixel.

      .. rubric:: *verbose*
         :name: verbose

      Post additional informative, possibly useful, messages to the
      logger?

      .. rubric:: *keepaxes*
         :name: keepaxes

      If dropdeg=True, these are the degenerate axes to keep.
      Nondegenerate axes are implicitly always kept. Ignored if
      dropdeg=False; all axes are kept in that case.

.. container:: section
   :name: viewlet-below-content-body
