imcollapse -- Collapse image along one axis, aggregating pixel values along that axis. -- analysis task
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
   * - function
     - :code:`''`
     - 
   * - axes
     - :code:`[ ]`
     - 
   * - outfile
     - :code:`''`
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
   * - overwrite
     - :code:`False`
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


function
---------------------------------------

:code:`''`

Aggregate function to apply. This can be set one of flux, madm, max, mean, median, min, npts, rms, stddev, sum, variance, xmadm. Must be specified.


axes
---------------------------------------

:code:`[ ]`

Zero-based axis number(s) or minimal match strings to collapse.


outfile
---------------------------------------

:code:`''`

Name of output CASA image. Must be specified.


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. Default is to use the entire direction plane.


region
---------------------------------------

:code:`''`

Region selection. Default is to use the full image.


chans
---------------------------------------

:code:`''`

Channels to use. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. Default is to use all Stokes planes.


mask
---------------------------------------

:code:`''`

Mask to use. Default is none.


overwrite
---------------------------------------

:code:`False`

Overwrite output image if it exists?


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 




