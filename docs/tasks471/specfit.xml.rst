specfit -- Fit 1-dimensional gaussians and/or polynomial models to an image or image region -- analysis task
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
   * - ngauss
     - :code:`int(1)`
     - 
   * - poly
     - :code:`int(-1)`
     - 
   * - estimates
     - :code:`''`
     - 
   * - minpts
     - :code:`int(1)`
     - 
   * - multifit
     - :code:`False`
     - 
   * - model
     - :code:`''`
     - 
   * - residual
     - :code:`''`
     - 
   * - amp
     - :code:`''`
     - 
   * - amperr
     - :code:`''`
     - 
   * - center
     - :code:`''`
     - 
   * - centererr
     - :code:`''`
     - 
   * - fwhm
     - :code:`''`
     - 
   * - fwhmerr
     - :code:`''`
     - 
   * - integral
     - :code:`''`
     - 
   * - integralerr
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
   * - pampest
     - :code:`''`
     - 
   * - pcenterest
     - :code:`''`
     - 
   * - pfwhmest
     - :code:`''`
     - 
   * - pfix
     - :code:`''`
     - 
   * - gmncomps
     - :code:`int(0)`
     - 
   * - gmampcon
     - :code:`''`
     - 
   * - gmcentercon
     - :code:`''`
     - 
   * - gmfwhmcon
     - :code:`''`
     - 
   * - gmampest
     - :code:`numpy.array( [  ] )`
     - 
   * - gmcenterest
     - :code:`numpy.array( [  ] )`
     - 
   * - gmfwhmest
     - :code:`numpy.array( [  ] )`
     - 
   * - gmfix
     - :code:`''`
     - 
   * - logfile
     - :code:`''`
     - 
   * - append
     - :code:`True`
     - 
   * - pfunc
     - :code:`''`
     - 
   * - goodamprange
     - :code:`numpy.array( [  ] )`
     - 
   * - goodcenterrange
     - :code:`numpy.array( [  ] )`
     - 
   * - goodfwhmrange
     - :code:`numpy.array( [  ] )`
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

Name of the input image


box
---------------------------------------

:code:`''`

Rectangular region to select in direction plane. See "help par.box" for details. Default is to use the entire direction plane.


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

Stokes planes to use. See "help par.stokes" for details. Default is to use all Stokes planes.


axis
---------------------------------------

:code:`int(-1)`

The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).


mask
---------------------------------------

:code:`''`

Mask to use. See help par.mask. Default is none..


ngauss
---------------------------------------

:code:`int(1)`

Number of Gaussian elements.  Default: 1.


poly
---------------------------------------

:code:`int(-1)`

Order of polynomial element.  Default: do not fit a polynomial (<0).


estimates
---------------------------------------

:code:`''`

Name of file containing initial estimates.  Default: No initial estimates ("").


minpts
---------------------------------------

:code:`int(1)`

Minimum number of unmasked points necessary to attempt fit.


multifit
---------------------------------------

:code:`False`

If true, fit a profile along the desired axis at each pixel in the specified region. If false, average the non-fit axis pixels and do a single fit to that average profile. Default False.


model
---------------------------------------

:code:`''`

Name of model image. Default: do not write the model image ("").


residual
---------------------------------------

:code:`''`

Name of residual image. Default: do not write the residual image ("").


amp
---------------------------------------

:code:`''`

Name of amplitude solution image. Default: do not write the image ("").


amperr
---------------------------------------

:code:`''`

Name of amplitude solution error image. Default: do not write the image ("").


center
---------------------------------------

:code:`''`

Name of center solution image. Default: do not write the image ("").


centererr
---------------------------------------

:code:`''`

Name of center solution error image. Default: do not write the image ("").


fwhm
---------------------------------------

:code:`''`

Name of fwhm solution image. Default: do not write the image ("").


fwhmerr
---------------------------------------

:code:`''`

Name of fwhm solution error image. Default: do not write the image ("").


integral
---------------------------------------

:code:`''`

Prefix of ame of integral solution image. Name of image will have gaussian component number appended.  Default: do not write the image ("").


integralerr
---------------------------------------

:code:`''`

Prefix of name of integral error solution image. Name of image will have gaussian component number appended.  Default: do not write the image ("").


wantreturn
---------------------------------------

:code:`True`

Should a record summarizing the results be returned?


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? See help par.stretch 


logresults
---------------------------------------

:code:`True`

Output results to logger?


pampest
---------------------------------------

:code:`''`

Initial estimate of PCF profile (gaussian or lorentzian) amplitudes.


pcenterest
---------------------------------------

:code:`''`

Initial estimate PCF profile centers, in pixels.


pfwhmest
---------------------------------------

:code:`''`

Initial estimate PCF profile FWHMs, in pixels.


pfix
---------------------------------------

:code:`''`

PCF profile parameters to fix during fit.


gmncomps
---------------------------------------

:code:`int(0)`

Number of components in each gaussian multiplet to fit


gmampcon
---------------------------------------

:code:`''`

The amplitude ratio constraints for non-reference components to reference component in gaussian multiplets.


gmcentercon
---------------------------------------

:code:`''`

The center offset constraints (in pixels) for non-reference components to reference component in gaussian multiplets.


gmfwhmcon
---------------------------------------

:code:`''`

The FWHM  ratio constraints for non-reference components to reference component in gaussian multiplets.


gmampest
---------------------------------------

:code:`numpy.array( [  ] )`

Initial estimate of individual gaussian amplitudes in gaussian multiplets.


gmcenterest
---------------------------------------

:code:`numpy.array( [  ] )`

Initial estimate of individual gaussian centers in gaussian multiplets, in pixels.


gmfwhmest
---------------------------------------

:code:`numpy.array( [  ] )`

Initial estimate of individual gaussian FWHMss in gaussian multiplets, in pixels.


gmfix
---------------------------------------

:code:`''`

Parameters of individual gaussians in gaussian multiplets to fix during fit.


logfile
---------------------------------------

:code:`''`

File in which to log results. Default is not to write a logfile.


append
---------------------------------------

:code:`True`

Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.


pfunc
---------------------------------------

:code:`''`

PCF singlet functions to fit. "gaussian" or "lorentzian" (minimal match supported). Unspecified means all gaussians.


goodamprange
---------------------------------------

:code:`numpy.array( [  ] )`

Acceptable amplitude solution range. [0.0] => all amplitude solutions are acceptable.


goodcenterrange
---------------------------------------

:code:`numpy.array( [  ] )`

Acceptable center solution range in pixels relative to region start. [0.0] => all center solutions are acceptable.


goodfwhmrange
---------------------------------------

:code:`numpy.array( [  ] )`

Acceptable FWHM solution range in pixels. [0.0] => all FWHM solutions are acceptable.


sigma
---------------------------------------

:code:`''`

Standard deviation array or image name.


outsigma
---------------------------------------

:code:`''`

Name of output image used for standard deviation. Ignored if sigma is empty.




