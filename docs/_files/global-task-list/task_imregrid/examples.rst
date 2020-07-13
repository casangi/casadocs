Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Basic Examples
         :name: basic-examples

      .. container:: casa-input-box

         | # Regrid an image to the "B1950" or "GALACTIC" coordinate
           systems
         |  imregrid(imagename="input.image", output="output.image",
           template="B1950")
         |  imregrid(imagename="input.image", output="output.image",
           template="GALACTIC")

      .. container:: info-box

         **NOTE**: When regridding to another coordinate system in the
         manner above, if the input image's direction coordinate is
         already in the frame specified by template, a straight copy of
         the image is made. No regridding is actually done.

       

      .. container:: casa-input-box

         | # Obtain a template dictionary from an image and then use it
           to regrid another image
         | temp_dict = imregrid(imagename="target.image",
           template="get")
         | imregrid(imagename="input.image", output="output.image",
           template=temp_dict)

      In this example, the *template="get"* option is used in the first
      command in order to characterize the desired shape and coordinate
      system used, and a new dictionary, TEMP_DICT, is generated
      accordingly. This is then used when performing the actual
      regridding of input.image in the second command.

       

      .. rubric:: More Advanced Examples
         :name: more-advanced-examples

      It is also possible to directly use a template image for
      regridding with **imregrid**. For this to work reliably and
      predictably, the dimensionality (i.e. which dimensions are present
      in an image) and the axis ordering of the input image must be the
      same. The type and ordering of the axes of both the input and
      template images can (and should) first be examined using the CASA
      **imhead** task. Any necessary reordering of axes can be performed
      using the CASA **imtrans** task. Unless the user explicitly
      specifies which dimensions to regrid using the *axes* parameter
      (see the following example), **imregrid** will also  attempt to
      regrid degenerate axes (i.e. image axes of length one pixel).
      Stokes axes are never regridded. In the case where template is an
      image name and the default value of shape is specified, the output
      image's shape will be the same as the template image's shape along
      the axes which are regridded and the same as the input image's
      shape along the axes which are not regridded. So for example, if
      the input image has a *shape* of [20, 30, 40] and the template
      image has a *shape* of [10, 40, 70] and only *axes=[0, 1]*, the
      output image will have a *shape* of [10, 40, 40]. If *axes=[2]*,
      the output image will have a *shape* of [20, 30, 70].

      .. container:: casa-input-box

         | # Regrid input.image by directly using target.image as a
           template
         | imregrid(imagename="input.image", output="output.image",
           template="target.image", shape=[500,500,40,1])

      In this example, it is assumed that the axis order of the input
      image is of the form (direction_x, direction_y, spectral, Stokes),
      where 'direction_x' and 'direction_y' are the directional
      coordinates on the sky (in some reference frame), 'spectral' is a
      velocity/frequency axis, and 'Stokes' contains polarization
      information. In this example, input.image might typically be a
      data cube of shape [100, 100, 40, 1]. Note that the default value
      of *asvelocity* (True) will be used so that the spectral axis will
      be regridded to the same velocity system as that of the template
      image.

      .. container:: casa-input-box

         | # Regrid only the first two axes of an image
         | imregrid(imagename="input.image", output="output.image",
           template="target.image", axes=[0,1])

      In this example, the user should inspect the type and ordering of
      the axes with **imhead**, and then correct with **imtrans** if
      necessary. The above command will regrid only the first two axes
      (normally the directional axes) of input.image and leave all other
      axes unchanged. The output image will have the shape of the
      template image along the regridded axes [0, 1] and the shape of
      the input image along the other axes since the shape parameter was
      not explicitly specified.

      .. container:: casa-input-box

         | # Regrid the third axis, considering velocity rather than
           frequency units
         | imregrid(imagename="input.image", output="output.image",
           template="target.image", axes=[2], asvelocity=True)

      This example regrids the spectral axis (zero-based axis number 2)
      with respect to velocity because the *asvelocity* parameter has
      been set to True. This is useful when e.g., regridding a cube
      containing one spectral line to match the velocity coordinate of
      another cube containing a different spectral line.

      .. container:: casa-input-box

         | # Regrid the third axis, considering velocity rather than
           frequency units but first set the rest frequency
         | imhead("input.image", mode="put", hdkey="restfreq",
           hdvalue="110GHz")
         | imregrid(imagename="input.image", output="output.image",
           template="target.image", axes=[2], asvelocity=True)

      The first command in this example uses the **imhead** task to set
      the value of the image rest frequency to a value of 110GHz in
      input.image. The following **imregrid** command then performs a
      frequency units regridding only of the third axis listed
      (zero-based axis) (2), taking account of the input.image rest
      frequency in the input file.

.. container:: section
   :name: viewlet-below-content-body
