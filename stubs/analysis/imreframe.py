#
# stub function definition file for docstring parsing
#

def imreframe(imagename, output='', outframe='lsrk', epoch='', restfreq=''):
    r"""
Change the frame in which the image reports its spectral values

Parameters
   - **imagename** (string) - Name of the input image [1]_
   - **output** (string='') - Name of the output image [2]_
   - **outframe** (string='lsrk') - Spectral frame in which the frequency or velocity values will be reported by default [3]_

      .. raw:: html

         <details><summary><i> outframe = topo </i></summary>

      - **epoch** (string='') - Epoch to be associated with this image [4]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> outframe = TOPO </i></summary>

      - **epoch** (string='') - Epoch to be associated with this image [4]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> outframe = geo </i></summary>

      - **epoch** (string='') - Epoch to be associated with this image [4]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> outframe = GEO </i></summary>

      - **epoch** (string='') - Epoch to be associated with this image [4]_

      .. raw:: html

         </details>
   - **restfreq** (string='') - restfrequency to use for velocity values (e.g "1.420GHz" for the HI line) [5]_


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




Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Name of the input image
.. [2] 
   **output** (string='')
      | Name of the output image
.. [3] 
   **outframe** (string='lsrk')
      | Spectral frame in which the frequency or velocity values will be reported by default
.. [4] 
   **epoch** (string='')
      | Epoch to be associated with this image
.. [5] 
   **restfreq** (string='')
      | restfrequency to use for velocity values (e.g "1.420GHz" for the HI line)

    """
    pass
