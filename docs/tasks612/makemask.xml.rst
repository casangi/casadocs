makemask -- Makes and manipulates image masks -- information task
=======================================

Description
---------------------------------------
Construct masks based on various criteria, convert between mask-types, and generate a mask for clean


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - mode
     - :code:`'list'`
     - Mask method (list, copy,expand,delete,setdefaultmask)
   * - inpimage
     - :code:`''`
     - Name of input image.
   * - inpmask
     - :code:`''`
     - mask(s) to be processed: image masks,T/F internal masks(Need to include parent image names),regions(for copy mode)
   * - output
     - :code:`''`
     - Name of output mask (imagename or imagename:internal_maskname)
   * - overwrite
     - :code:`False`
     - overwrite output if exists?
   * - inpfreqs
     - :code:`numpy.array( [  ] )`
     - List of chans/freqs (in inpmask) to read masks from
   * - outfreqs
     - :code:`numpy.array( [  ] )`
     - List of chans/freqs (in output) on which to expand the mask


Parameter Explanations
=======================================



mode
---------------------------------------

:code:`'list'`

Mask method (list, copy,expand,delete,setdefaultmask)


inpimage
---------------------------------------

:code:`''`

Name of input image.


inpmask
---------------------------------------

:code:`''`

mask(s) to be processed: image masks,T/F internal masks(Need to include parent image names),regions(for copy mode)


output
---------------------------------------

:code:`''`

Name of output mask (imagename or imagename:internal_maskname)


overwrite
---------------------------------------

:code:`False`

overwrite output if exists?


inpfreqs
---------------------------------------

:code:`numpy.array( [  ] )`

List of chans/freqs (in inpmask) to read masks from 


outfreqs
---------------------------------------

:code:`numpy.array( [  ] )`

List of chans/freqs (in output) on which to expand the mask




