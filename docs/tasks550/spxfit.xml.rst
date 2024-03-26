spxfit -- Fit a 1-dimensional model(s) to an image(s) or region for determination of spectral index. -- analysis task
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
   * - axis
     - :code:`int(-1)`
     - 
   * - mask
     - :code:`''`
     - 
   * - minpts
     - :code:`int(1)`
     - 
   * - multifit
     - :code:`False`
     - 
   * - spxtype
     - :code:`'plp'`
     - 
   * - spxest
     - :code:`numpy.array( [  ] )`
     - 
   * - spxfix
     - :code:`numpy.array( [  ] )`
     - 
   * - div
     - :code:`[ ]`
     - 
   * - spxsol
     - :code:`''`
     - 
   * - spxerr
     - :code:`''`
     - 
   * - model
     - :code:`''`
     - 
   * - residual
     - :code:`''`
     - 
   * - wantreturn
     - :code:`True`
     - 
   * - stretch
     - :code:`False`
     - 
   * - logresults
     - :code:`True`
     - 
   * - logfile
     - :code:`''`
     - 
   * - append
     - :code:`True`
     - 
   * - sigma
     - :code:`''`
     - 
   * - outsigma
     - :code:`''`
     - 


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image(s)


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


axis
---------------------------------------

:code:`int(-1)`

The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).


mask
---------------------------------------

:code:`''`

Mask to use. Default is none.


minpts
---------------------------------------

:code:`int(1)`

Minimum number of unmasked points necessary to attempt fit.


multifit
---------------------------------------

:code:`False`

If true, fit a profile along the desired axis at each pixel in the specified region. If false, average the non-fit axis pixels and do a single fit to that average profile. Default False.


spxtype
---------------------------------------

:code:`'plp'`

Type of function to fit. "plp" = power logarithmic polynomial, "ltp" = logarithmic transformed polynomial.


spxest
---------------------------------------

:code:`numpy.array( [  ] )`

REQUIRED. Initial estimates as array of numerical values for the spectral index function coefficients. eg [1.5, -0.8] if fitting a plp function thought to be close to 1.5*(x/div)**(-0.8) or [0.4055, -0.8] if fitting an lpt function thought to be close to ln(1.5) - 0.8*ln(x/div).


spxfix
---------------------------------------

:code:`numpy.array( [  ] )`

Fix the corresponding spectral index function coefficients during the fit. True means hold fixed.


div
---------------------------------------

:code:`[ ]`

Divisor (numerical value or quantity) to use in the logarithmic terms of the plp or ltp function. 0 means calculate a useful value on the fly.


spxsol
---------------------------------------

:code:`''`

Name of the spectral index function coefficient solution image to write.


spxerr
---------------------------------------

:code:`''`

Name of the spectral index function coefficient error image to write.


model
---------------------------------------

:code:`''`

Name of model image. Default: do not write the model image ("").


residual
---------------------------------------

:code:`''`

Name of residual image. Default: do not write the residual image ("").


wantreturn
---------------------------------------

:code:`True`

Should a record summarizing the results be returned?


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 


logresults
---------------------------------------

:code:`True`

Output results to logger?


logfile
---------------------------------------

:code:`''`

File in which to log results. Default is not to write a logfile.


append
---------------------------------------

:code:`True`

Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.


sigma
---------------------------------------

:code:`''`

Standard deviation array or image name(s).


outsigma
---------------------------------------

:code:`''`

Name of output image used for standard deviation. Ignored if sigma is empty.




