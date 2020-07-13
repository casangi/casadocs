Examples
========

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Pre-defined modes:
         :name: pre-defined-modes

      .. container:: casa-input-box

         | mode='evalexpr'; imagename=['image1.im', 'image2.im' ]
         | # in the parameter **expr**, the value 'IM0' is replaced by
           'image1.im'
         | # and 'IM1' is replaced with 'image2.im'

         | mode='spix'; imagename=['image1.im','image2.im']
         | # will calculate an image of log(S1/S2)/log(f1/f2), where S1
           and S2 are fluxes and
         | # f1 and f2 are frequencies

         | mode='pola'; imagename='multistokes.im' (where that image
           contains both Q and U stokes planes) or
           imagename=['imageQ.im','imageU.im']
         | # will calculate an image of the polarization angle
           distribution 0.5*arctan(U/Q),
         | # where imageQ.im and imageU.im are Stokes Q and U images,
           respectively.

         | mode='poli'; imagename=['imageQ.im','imageU.im','imageV.im']
         | # will calculate the total polarization intensity image,
           where imageQ.im, imageU.im,
         | # imageV.im are Stokes Q, U, and V images, respectively.
           Alternatively,
         | mode='poli'; imagename = ['imageQ.im','imageU.im']
         | # will calculate the linear polarization intensity image.
         | # In the case where imagename is a single multi-stokes image,
           the total polarization
         | # image will be calculated if all of the Q, U, and V stokes
           planes are present, and
         | # the linear polarization intensity image will be calculated
           if the Q and U (but not V) planes
         | # are present.

      .. rubric:: Examples of expressions in mode='evalexpr':
         :name: examples-of-expressions-in-modeevalexpr

      .. container:: casa-input-box

         | #Make an image that is image1.im - image2.im
         | expr=’ (IM0 - IM1 )’
         | #or with an explicit notation,
         | expr=’("image1.im" - "image2.im")’

      .. container:: casa-input-box

         | #Double all values in an image.
         | immath( imagename='myimage.im', expr='IM0*2',
           outfile='double.im' )
         | # or with an explicit notation,
         | immath( expr='"myimage.im"*2', outfile='double.im' )

      .. container:: casa-input-box

         | # Taking the sin of an image and adding it to another
         | # Note that the images need to be the same size
         | immath(imagename=['image1.im', 'image2.im'],
           expr='sin(IM1)+IM0;',outfile='newImage.im')

      .. container:: casa-input-box

         | 
         | # Adding only the plane associated with the 'V' stokes value
           and
         | # the 1st channel together in two images
         | immath(imagename=[image1', 'image2'],
           expr='IM0+IM1',chans='1',stokes='V')

      .. container:: casa-input-box

         | # Selecting a single plane (5th channel), of the 3-D cube and
         | # adding it to the original image. In this example the 2-D
           plane
         | # gets expanded out and the values are applied to each plane
           in the
         | # 3-D cube.
         | default('immath')
         | imagename='ngc7538.image'
         | outfile='chanFive.im'
         | expr='IM0'
         | chans='5'
         | go
         | default('immath')
         | imagename=['ngc7538.image', chanFive.im']
         | outfile='ngc7538_chanFive.im'
         | expr='IM0+IM1'
         | go

      .. container:: casa-input-box

         | # Selecting and saving the inner 3/4 of an image for channels
           40,42,44
         | # as well as channels less than 10
         | default('immath')
         | imagename='my_image.im'
         | expr='IM0'
         | box='25,25,123,123'
         | chans='<10;40,42,44'
         | outfile='my_image_inner.im' )
         | go

      .. container:: casa-input-box

         | # Dividing an image by another, making sure we aren't
           dividing by zero
         | default('immath')
         | imagename=['orion.image', 'my.image']
         | expr='IM0/iif(IM1==0,1.0,IM1)' #note: iif (a, b, c) a is the
           boolean expression
         | #                                                   b is the
           value if true
         | #                                                   c is the
           value if false  
         | outfile='my_orion.image'
         | go

      .. container:: casa-input-box

         | # Applying a mask to all of the images in the expression
         | default('immath')
         | imagename=['ngc7538.image','ngc7538_clean.image']
         | expr='(IM0*10)+IM1'
         | mask='"ngc7538.mask"'
         | outfile='really_noisy_ngc7538.image'
         | go

      .. container:: casa-input-box

         | # Applying a pixel mask contained in the image information
         | default('immath')
         | imagename='ngc5921.image'
         | expr='IM0*10'
         | mask='mask("ngc5921.mask")'
         | outfile='ngc5921.masked.image'
         | go

      .. container:: casa-input-box

         | # Creating a total polarization intensity image from an
           multi-stokes image
         | # containing IQUV.
         | default('immath')
         | outfile='pol_intensity'
         | stokes=''
         | # in imagename, you can also specify a list containing single
           stokes images
         | # of Q and U (for linear polarization intensity) and V (for
           total
         | # polarization intensity)
         | imagename='3C138_pcal'
         | mode='poli'
         | go

      .. container:: casa-input-box

         | 
         | # Creating a polarization position angle image
         | default('immath')
         | outfile='pol_angle.im'
         | mode='pola'
         | # you can also do imagename=['Q.im','U.im'] for single stokes
           images, order of
         | # the two Stokes images does not matter
         | imagename='3C138_pcal' # multi-stokes image containing at
           least Q and U stokes
         | go

      .. container:: casa-input-box

         | # same as before but write a mask with values of False for
           pixels for which the
         | # corresponding linear polarization ( sqrt(Q*Q+U*U)) is less
           than 30 microJy/beam
         | polithresh='30uJy/beam'
         | go

      .. container:: casa-input-box

         | # Creating a spectral index image from the images at two
           different observing frequencies
         | default('immath')
         | outfile='mySource_sp.im'
         | mode='spix'
         | imagename=['mySource_5GHz.im','mySource_8GHz.im']
         | go

       

.. container:: section
   :name: viewlet-below-content-body
