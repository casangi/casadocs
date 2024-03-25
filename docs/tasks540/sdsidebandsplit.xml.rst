sdsidebandsplit -- [EXPERIMENTAL] invoke sideband separation using FFT -- single dish task
=======================================

Description
---------------------------------------
[EXPERIMENTAL] SD sideband separation and supression task:
        Invoke sideband separation / supression using FFT



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - imagename
     - :code:`numpy.array( [  ] )`
     - a list of names of input images
   * - outfile
     - :code:`''`
     - Prefix of output image name
   * - overwrite
     - :code:`False`
     - 
   * - signalshift
     - :code:`numpy.array( [  ] )`
     - a list of channel number shifts in signal side band
   * - imageshift
     - :code:`numpy.array( [  ] )`
     - a list of channel number shifts in image side band
   * - getbothside
     - :code:`False`
     - 
   * - refchan
     - :code:`float(0.0)`
     - 
   * - refval
     - :code:`''`
     - 
   * - otherside
     - :code:`False`
     - 
   * - threshold
     - :code:`float(0.2)`
     - Rejection limit of solution


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`numpy.array( [  ] )`

a list of names of input images. At least two valid images are required for processing


outfile
---------------------------------------

:code:`''`

Prefix of output image name.
      A suffix, ".signalband" or ".imageband" is added to 
      output image name depending on the side band side being solved.


overwrite
---------------------------------------

:code:`False`

overwrite option


signalshift
---------------------------------------

:code:`numpy.array( [  ] )`

a list of channel number shifts in signal side band.
      The number of elements must be equal to that of imagename


imageshift
---------------------------------------

:code:`numpy.array( [  ] )`

 a list of channel number shifts in image side band.
      The number of elements must be either zero or equal to that of imagename.
      In case of zero length array, the values are obtained from signalshift
      assuming the shifts are the same magnitude in opposite direction.


getbothside
---------------------------------------

:code:`False`

sideband separation (True) or supression (False)


refchan
---------------------------------------

:code:`float(0.0)`

reference channel of spectral axis in image sideband


refval
---------------------------------------

:code:`''`

frequency at the reference channel of spectral axis in image sideband (e.g., "100GHz")


otherside
---------------------------------------

:code:`False`

solve the solution of the other side band side and subtract the solution


threshold
---------------------------------------

:code:`float(0.2)`

Rejection limit of solution. The value must be greater than 0.0 and less than 1.0.




