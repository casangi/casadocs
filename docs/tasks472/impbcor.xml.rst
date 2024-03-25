impbcor -- Construct a primary beam corrected image from an image and a primary beam pattern. -- analysis task
=======================================

Description
---------------------------------------



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - imagename
     - :code:`''`
     - 
   * - pbimage
     - :code:`[ ]`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - box
     - :code:`''`
     - 
   * - region
     - :code:`''`
     - 
   * - chans
     - :code:`''`
     - 
   * - stokes
     - :code:`''`
     - 
   * - mask
     - :code:`''`
     - 
   * - mode
     - :code:`'divide'`
     - 
   * - cutoff
     - :code:`float(-1.0)`
     - 
   * - stretch
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


pbimage
---------------------------------------

:code:`[ ]`

Name of the primary beam image which must exist or array of values for the pb response. Default ""


outfile
---------------------------------------

:code:`''`

Output image name. If empty, no image is written. Default ""


overwrite
---------------------------------------

:code:`False`

Overwrite the output if it exists? Default False


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


region
---------------------------------------

:code:`''`

Region selection. See "help par.region" for details. Default is to use the full image.


chans
---------------------------------------

:code:`''`

Channels to use. See "help par.chans" for details. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. See "help par.stokes" for details. Default is to use all Stokes planes.


mask
---------------------------------------

:code:`''`

Mask to use. See help par.mask. Default is none.


mode
---------------------------------------

:code:`'divide'`

Divide or multiply the image by the primary beam image. Minimal match supported. Default "divide"


cutoff
---------------------------------------

:code:`float(-1.0)`

PB cutoff. If mode is "d", all values less than this will be masked. If "m", all values greater will be masked. Less than 0, no cutoff. Default no cutoff


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? See help par.stretch 




