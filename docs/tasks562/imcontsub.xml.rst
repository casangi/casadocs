imcontsub -- Estimates and subtracts continuum emission from an image cube -- analysis, imaging task
=======================================

Description
---------------------------------------

Estimates and subtracts continuum emission from an image cube

For each direction pixel (x, y) column in imagename (or a subset
selected by region and/or box), this estimates the continuum by
fitting a polynomial to one or more subsets of the channels.  The
continuum estimate is saved in contfile, and subtracted from imagename
(or its subset) to make a spectral line estimate, which is saved in
linefile.



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
     - Name of the input spectral line image
   * - linefile
     - :code:`''`
     - Output continuum-subtracted image file name
   * - contfile
     - :code:`''`
     - Output continuum image file name
   * - fitorder
     - :code:`int(0)`
     - Polynomial order for the continuum estimation
   * - region
     - :code:`''`
     - Region selection.
   * - box
     - :code:`''`
     - Rectangular region to select in direction plane. Default is to use the entire direction plane.
   * - chans
     - :code:`''`
     - Channels to use.
   * - stokes
     - :code:`''`
     - Stokes planes to use.


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Input image cube.
                     Default: none

                        Example: imagename='ngc5921_task.im'



linefile
---------------------------------------

:code:`''`

Name of continuum-subtracted output spectral line cube
                     Default: none

                        Example: outline='ngc5921_line.im'



contfile
---------------------------------------

:code:`''`

Name of output continuum cube
                     Default: none

                        Example: contfile='ngc5921_cont.im'



fitorder
---------------------------------------

:code:`int(0)`

Polynomial order for the continuum estimation
                     Default: 0

                        Example: fitorder=2



region
---------------------------------------

:code:`''`

Region selection. 
                     Default: '' (use the full image)



box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane.
                     Default: '' (use the entire direction plane)



chans
---------------------------------------

:code:`''`

Channels to use. 
                     Default: '' (use all channels)



stokes
---------------------------------------

:code:`''`

Stokes planes to use.
                     Default: '' (use all Stokes planes)





