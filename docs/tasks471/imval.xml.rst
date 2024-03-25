imval -- Get the data value(s) and/or mask value in an image. -- analysis, information task
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
   * - region
     - :code:`''`
     - 
   * - box
     - :code:`''`
     - 
   * - chans
     - :code:`''`
     - 
   * - stokes
     - :code:`''`
     - 
   * - blc
     - :code:`[ ]`
     - 
   * - trc
     - :code:`[ ]`
     - 
   * - axes
     - :code:`[ ]`
     - 
   * - unit
     - :code:`[ ]`
     - 
   * - data
     - :code:`[ ]`
     - 
   * - mask
     - :code:`[ ]`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


region
---------------------------------------

:code:`''`

Region selection. See "help par.region" for details. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region(s) to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use. See "help par.chans" for details. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. See "help par.stokes" for details. Planes specified must be contiguous. Default is to use all Stokes planes.


blc
---------------------------------------

:code:`[ ]`

Bottom-left corner of the bounding box that encloses the region being examined..


trc
---------------------------------------

:code:`[ ]`

top-right corner of the bounding box that encloses the region being examined.


axes
---------------------------------------

:code:`[ ]`

A listing of the axis index numbers and the data stored along that axis.


unit
---------------------------------------

:code:`[ ]`

The units the data values are stored and displayed in.


data
---------------------------------------

:code:`[ ]`

The mask values found at the give point(s).


mask
---------------------------------------

:code:`[ ]`

The mask values found at the give point(s).




