sdfixscan -- Task for single-dish image processing -- single dish task
=======================================

Description
---------------------------------------

Task sdfixscan is used to remove a scanning noise that appears 
as a striped noise pattern along the scan direction in a raster 
scan data. 

By default, the scanning noise is removed by using the 
FFT-based 'Basket-Weaving' method (Emerson \& Grave 1988) that
requires multiple images that observed exactly the same area with
different scanning direction. If only one image is available, the
'Pressed-out' method (Sofue \& Reich 1979) can be used to remove
the scanning effect.
  


Parameters
---------------------------------------
.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   * - Parameter
     - Default
     - Description
   * - infiles
     - :code:`numpy.array( [  ] )`
     - list of name of input SD images (FITS or CASA image)
   * - mode
     - :code:`'fft_mask'`
     - image processing mode ["fft_mask", "model"]
   * - numpoly
     - :code:`int(2)`
     - order of polynomial fit for Pressed-out method
   * - beamsize
     - :code:`float(0.0)`
     - beam size for Pressed-out method
   * - smoothsize
     - :code:`float(2.0)`
     - size of smoothing beam for Pressed-out method
   * - direction
     - :code:`numpy.array( [  ] )`
     - scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree
   * - maskwidth
     - :code:`float(1.0)`
     - mask width for Basket-Weaving (on percentage)
   * - tmax
     - :code:`float(0.0)`
     - maximum threshold value for processing
   * - tmin
     - :code:`float(0.0)`
     - minimum threshold value for processing
   * - outfile
     - :code:`''`
     - name of output file
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]


Parameter Explanations
=======================================



infiles
---------------------------------------

:code:`numpy.array( [  ] )`

list of name of input SD images (FITS or CASA image)


mode
---------------------------------------

:code:`'fft_mask'`

image processing mode


numpoly
---------------------------------------

:code:`int(2)`

order of polynomial fit for Pressed-out method


beamsize
---------------------------------------

:code:`float(0.0)`

beam size for Pressed-out method


smoothsize
---------------------------------------

:code:`float(2.0)`

size of smoothing beam for Pressed-out method


direction
---------------------------------------

:code:`numpy.array( [  ] )`

scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree


maskwidth
---------------------------------------

:code:`float(1.0)`

mask width for Basket-Weaving (on percentage)


tmax
---------------------------------------

:code:`float(0.0)`

maximum threshold value for processing


tmin
---------------------------------------

:code:`float(0.0)`

minimum threshold value for processing


outfile
---------------------------------------

:code:`''`

name of output file


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists




