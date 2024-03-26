imstat -- Displays statistical information from an image or image region -- analysis, information task
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
     - Name of the input image
   * - axes
     - :code:`[ ]`
     - List of axes to evaluate statistics over. Default is all axes.
   * - region
     - :code:`''`
     - Region selection. Default is to use the full image.
   * - box
     - :code:`''`
     - Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
   * - chans
     - :code:`''`
     - Channels to use. Default is to use all channels.
   * - stokes
     - :code:`''`
     - Stokes planes to use. Default is to use all Stokes planes.
   * - listit
     - :code:`True`
     - Print stats and bounding box to logger?
   * - verbose
     - :code:`True`
     - Print additional messages to logger?
   * - mask
     - :code:`''`
     - Mask to use. Default is none.
   * - stretch
     - :code:`False`
     - Stretch the mask if necessary and possible?
   * - logfile
     - :code:`''`
     - Name of file to write fit results.
   * - append
     - :code:`True`
     - If logfile exists, append to it if True or overwrite it if False
   * - algorithm
     - :code:`'classic'`
     - Algorithm to use. Supported values are "biweight", "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported.
   * - fence
     - :code:`float(-1)`
     - Fence value for hinges-fences. A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if algorithm is not "hinges-fences".
   * - center
     - :code:`'mean'`
     - Center to use for fit-half. Valid choices are "mean", "median", and "zero". Ignored if algorithm is not "fit-half".
   * - lside
     - :code:`True`
     - For fit-half, use values <= center for real data if True? If False, use values >= center as real data. Ignored if algorithm is not "fit-half".
   * - zscore
     - :code:`float(-1)`
     - For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".
   * - maxiter
     - :code:`int(-1)`
     - For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algorithm is not "chauvenet".
   * - clmethod
     - :code:`'auto'`
     - Method to use for calculating classical statistics. Supported methods are "auto", "tiled", and "framework". Ignored if algorithm is not "classic".
   * - niter
     - :code:`int(3)`
     - For biweight, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, do a fast, simple computation (see description). Ignored if the algorithm is not "biweight".


Parameter Explanations
=======================================



imagename
---------------------------------------

:code:`''`

Name of the input image


axes
---------------------------------------

:code:`[ ]`

List of axes to evaluate statistics over. Default is all axes.


region
---------------------------------------

:code:`''`

Region selection. Default is to use the full image.


box
---------------------------------------

:code:`''`

Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.


chans
---------------------------------------

:code:`''`

Channels to use. Default is to use all channels.


stokes
---------------------------------------

:code:`''`

Stokes planes to use. Default is to use all Stokes planes.


listit
---------------------------------------

:code:`True`

Print stats and bounding box to logger?


verbose
---------------------------------------

:code:`True`

Print additional messages to logger?


mask
---------------------------------------

:code:`''`

Mask to use. Default is none.


stretch
---------------------------------------

:code:`False`

Stretch the mask if necessary and possible? 


logfile
---------------------------------------

:code:`''`

Name of file to write fit results.


append
---------------------------------------

:code:`True`

If logfile exists, append to it if True or overwrite it if False


algorithm
---------------------------------------

:code:`'classic'`

Algorithm to use. Supported values are "biweight", "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported.


fence
---------------------------------------

:code:`float(-1)`

Fence value for hinges-fences. A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if algorithm is not "hinges-fences".


center
---------------------------------------

:code:`'mean'`

Center to use for fit-half. Valid choices are "mean", "median", and "zero". Ignored if algorithm is not "fit-half".


lside
---------------------------------------

:code:`True`

For fit-half, use values <= center for real data if True? If False, use values >= center as real data. Ignored if algorithm is not "fit-half".


zscore
---------------------------------------

:code:`float(-1)`

For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".


maxiter
---------------------------------------

:code:`int(-1)`

For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algorithm is not "chauvenet".


clmethod
---------------------------------------

:code:`'auto'`

Method to use for calculating classical statistics. Supported methods are "auto", "tiled", and "framework". Ignored if algorithm is not "classic".


niter
---------------------------------------

:code:`int(3)`

For biweight, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, do a fast, simple computation (see description). Ignored if the algorithm is not "biweight".




