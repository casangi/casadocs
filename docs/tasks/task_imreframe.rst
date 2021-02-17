

.. _Description:

Description
   The spectral values assigned to an object depend on the spectral
   reference frame. This task can change the frame in which the image
   reports its spectral values.

   
   .. rubric:: Parameter descriptions

   *imagename*
   
   Name of the input image.
   
   *output*
   
   Name of the output image. Default (no output) is to modify the
   input image.
   
   *outframe*
   
   Spectral frame in which the frequency or velocity values will be
   reported by default. See `Spectral
   Frames <../../notebooks/memo-series.ipynb#Spectral-Frames>`__
   for more information on the frame definitions. 
   
   +-----------------------------------+-----------------------------------+
   | **Abbreviation**                  | **Definition**                    |
   +-----------------------------------+-----------------------------------+
   | lsrk                              | local standard of rest            |
   |                                   | (kinematic) - default             |
   +-----------------------------------+-----------------------------------+
   | lsrd                              | local standard of rest (dynamic)  |
   +-----------------------------------+-----------------------------------+
   | bary                              | barycentric                       |
   +-----------------------------------+-----------------------------------+
   | geo                               | geocentric                        |
   +-----------------------------------+-----------------------------------+
   | topo                              | topocentric                       |
   +-----------------------------------+-----------------------------------+
   | galacto                           | galactocentric                    |
   +-----------------------------------+-----------------------------------+
   | lgroup                            | local group                       |
   +-----------------------------------+-----------------------------------+
   | cmb                               | Cosmic Microwave Background       |
   |                                   | dipole                            |
   +-----------------------------------+-----------------------------------+
   
   *epoch*
   
   Epoch to be associated with this image (only with outframe='geo'
   or 'topo'). For example: '2000/12/25/18:30:00.10'.
   
   *restfreq*
   
   Rest-frequency to use for velocity value. For example:
   restfreq='1.420405752GHz' for the HI 21cm line of neutral
   hydrogen. The default is to use the rest-frequency already present
   in the input image.
   

.. _Examples:

Examples
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
   No additional development details

