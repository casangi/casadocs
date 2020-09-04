Description
   Changes the spectral reference frame of an image (cube).

   The spectral values assigned to an object depend on the spectral
   reference frame. This task can change the frame in which the image
   reports its spectral values.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *imagename*
      

   Name of the input image.

   .. rubric:: *output*
      

   Name of the output image. Default (no output) is to modify the
   input image.

   .. rubric:: *outframe*
      

   Spectral frame in which the frequency or velocity values will be
   reported by default. See `Spectral
   Frames <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material/spectral-frames>`__
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

   .. rubric:: *epoch*
      

   Epoch to be associated with this image (only with outframe='geo'
   or 'topo'). For example: '2000/12/25/18:30:00.10'.

   .. rubric:: *restfreq*
      

   Rest-frequency to use for velocity value. For example:
   restfreq='1.420405752GHz' for the HI 21cm line of neutral
   hydrogen. The default is to use the rest-frequency already present
   in the input image.
