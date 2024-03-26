immath -- Perform math operations on images -- analysis task
=======================================

Description
---------------------------------------
 math on images



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
   * - mode
     - :code:`'evalexpr'`
     - 
   * - outfile
     - :code:`'immath_results.im'`
     - 
   * - expr
     - :code:`'IM0'`
     - 
   * - varnames
     - :code:`''`
     - 
   * - sigma
     - :code:`'0.0mJy/beam'`
     - 
   * - polithresh
     - :code:`''`
     - 
   * - mask
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
   * - stretch
     - :code:`False`
     - 
   * - imagemd
     - :code:`''`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

a list of input images 


mode
---------------------------------------

:code:`'evalexpr'`

mode for math operation (evalexpr, spix, pola, poli)


outfile
---------------------------------------

:code:`'immath_results.im'`

File where the output is saved


expr
---------------------------------------

:code:`'IM0'`

Mathematical expression using images


varnames
---------------------------------------

:code:`''`

a list of variable names to use with the image files


sigma
---------------------------------------

:code:`'0.0mJy/beam'`

standard deviation of noise for debiasing


polithresh
---------------------------------------

:code:`''`

Threshold in linear polarization intensity image below which to mask pixels.


mask
---------------------------------------

:code:`''`

Mask to use. See help par.mask. Default is none.


region
---------------------------------------

:code:`''`

Region selection. See "help par.region" for details. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use. See "help par.chans" for details. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. See "help par.stokes" for details. Default is to use all Stokes planes.


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? See help stretch.par 


imagemd
---------------------------------------

:code:`''`

An image name from which metadata should be copied. The input can be either an image listed under imagename or any other image on disk. Leaving this parameter unset may copy header metadata from any of the input images, which one is not guaranteed. 




