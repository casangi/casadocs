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

      To change the spectral reference frame of an image
      ('linecube.image') to the Local Group reference frame using the
      rest-frequency values already stored in the original image, and
      then save the output image into a new image
      ('linecube_new.image'):

      .. container:: casa-input-box

         imreframe(imagename='linecube.image',
         output='linecube_new.image' outframe='lgroup')

      To change the spectral reference frame of an image that contains
      the NH\ 3 (1,1) line into the barycentric values, and overwrite
      the input image:

      .. container:: casa-input-box

         imreframe(imagename='NH3_cube.image', outframe='bary',
         restfreq='23.694496GHz')

       

       

.. container:: section
   :name: viewlet-below-content-body
