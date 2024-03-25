imfit -- Fit one or more elliptical Gaussian components on an image region(s) -- analysis task
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
   * - includepix
     - :code:`numpy.array( [  ] )`
     - 
   * - excludepix
     - :code:`numpy.array( [  ] )`
     - 
   * - residual
     - :code:`''`
     - 
   * - model
     - :code:`''`
     - 
   * - estimates
     - :code:`''`
     - 
   * - logfile
     - :code:`''`
     - 
   * - append
     - :code:`True`
     - 
   * - newestimates
     - :code:`''`
     - 
   * - complist
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - dooff
     - :code:`False`
     - 
   * - offset
     - :code:`float(0.0)`
     - 
   * - fixoffset
     - :code:`False`
     - 
   * - stretch
     - :code:`False`
     - 
   * - rms
     - :code:`[ ]`
     - 
   * - noisefwhm
     - :code:`''`
     - 
   * - summary
     - :code:`''`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


box
---------------------------------------

:code:`''`

Rectangular region(s) to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


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

Stokes planes to use. See "help par.stokes" for details. Default is to use first Stokes plane.


mask
---------------------------------------

:code:`''`

Mask to use. See help par.mask. Default is none.


includepix
---------------------------------------

:code:`numpy.array( [  ] )`

Range of pixel values to include for fitting.


excludepix
---------------------------------------

:code:`numpy.array( [  ] )`

Range of pixel values to exclude for fitting.


residual
---------------------------------------

:code:`''`

Name of output residual image.


model
---------------------------------------

:code:`''`

Name of output model image.


estimates
---------------------------------------

:code:`''`

Name of file containing initial estimates of component parameters.


logfile
---------------------------------------

:code:`''`

Name of file to write fit results.


append
---------------------------------------

:code:`True`

If logfile exists, append to it if True or overwrite it if False


newestimates
---------------------------------------

:code:`''`

File to write fit results which can be used as initial estimates for next run.


complist
---------------------------------------

:code:`''`

Name of output component list table.


overwrite
---------------------------------------

:code:`False`

Overwrite component list table if it exists?


dooff
---------------------------------------

:code:`False`

Also fit a zero level offset? Default is False


offset
---------------------------------------

:code:`float(0.0)`

Initial estimate of zero-level offset. Only used if doff is True. Default is 0.0


fixoffset
---------------------------------------

:code:`False`

Keep the zero level offset fixed during fit? Default is False 


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? See help par.stretch 


rms
---------------------------------------

:code:`[ ]`

RMS to use in calculation of uncertainties. Numeric or valid quantity (record or string). If numeric, it is given units of the input image. If quantity, units must conform to image units. If not positive, the rms of the residual image, in the region of the fit, is used.


noisefwhm
---------------------------------------

:code:`''`

Noise correlation beam FWHM. If numeric value, interpreted as pixel widths. If quantity (dictionary, string), it must have angular units.


summary
---------------------------------------

:code:`''`

File name to which to write table of fit parameters.




