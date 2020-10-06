

.. _Description:

Description
   

.. _Examples:

Examples
   task examples
   
   To change the spectral reference frame of an image
   ('linecube.image') to the Local Group reference frame using the
   rest-frequency values already stored in the original image, and
   then save the output image into a new image
   ('linecube_new.image'):
   
   ::
   
      imreframe(imagename='linecube.image',
      output='linecube_new.image' outframe='lgroup')
   
   To change the spectral reference frame of an image that contains
   the NH 3 (1,1) line into the barycentric values, and overwrite
   the input image:
   
   ::
   
      imreframe(imagename='NH3_cube.image', outframe='bary',
      restfreq='23.694496GHz')
   

.. _Development:

Development
   