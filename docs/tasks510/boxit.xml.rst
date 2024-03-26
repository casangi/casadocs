boxit -- Box regions in image above given threshold value. -- imaging task
=======================================

Description
---------------------------------------
Returns a list of boxes, one for each contiguous set of pixels
  above the threshold value.  If given "regionfile", outputs boxes in
  regionfile+'.rgn'


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
   * - regionfile
     - :code:`''`
     - 
   * - threshold
     - :code:`{'value': float(0.0), 'unit': 'mJy'}`
     - 
   * - maskname
     - :code:`''`
     - 
   * - chanrange
     - :code:`''`
     - 
   * - polrange
     - :code:`''`
     - 
   * - minsize
     - :code:`int(2)`
     - 
   * - diag
     - :code:`False`
     - 
   * - boxstretch
     - :code:`int(1)`
     - 
   * - overwrite
     - :code:`False`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of image to threshold


regionfile
---------------------------------------

:code:`''`

Output region file


threshold
---------------------------------------

:code:`{'value': float(0.0), 'unit': 'mJy'}`

Threshold value.  Must include units.


maskname
---------------------------------------

:code:`''`

Output mask name (optional).


chanrange
---------------------------------------

:code:`''`

Range of channel ids


polrange
---------------------------------------

:code:`''`

Range of polarization ids


minsize
---------------------------------------

:code:`int(2)`

Minimum number of pixels for a boxable island


diag
---------------------------------------

:code:`False`

Count diagonal connections?


boxstretch
---------------------------------------

:code:`int(1)`

Increase box sizes by this many pixels beyond thresholded pixels.


overwrite
---------------------------------------

:code:`False`

Overwrite existing region file?




