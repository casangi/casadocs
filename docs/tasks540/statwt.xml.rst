statwt -- Compute and set weights based on variance of data. -- misc task
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
   * - vis
     - :code:`''`
     - 
   * - selectdata
     - :code:`True`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - combine
     - :code:`''`
     - 
   * - timebin
     - :code:`int(1)`
     - 
   * - slidetimebin
     - :code:`False`
     - 
   * - chanbin
     - :code:`'spw'`
     - 
   * - minsamp
     - :code:`int(2)`
     - 
   * - statalg
     - :code:`'classic'`
     - 
   * - fence
     - :code:`float(-1)`
     - 
   * - center
     - :code:`'mean'`
     - 
   * - lside
     - :code:`True`
     - 
   * - zscore
     - :code:`float(-1)`
     - 
   * - maxiter
     - :code:`int(-1)`
     - 
   * - excludechans
     - :code:`''`
     - 
   * - wtrange
     - :code:`numpy.array( [  ] )`
     - 
   * - flagbackup
     - :code:`True`
     - 
   * - preview
     - :code:`False`
     - 
   * - datacolumn
     - :code:`'corrected'`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of measurement set


selectdata
---------------------------------------

:code:`True`

Enable data selection parameters


field
---------------------------------------

:code:`''`

Selection based on field names or field index numbers. Default is all.


spw
---------------------------------------

:code:`''`

Selection based on spectral windows:channels. Default is all.


intent
---------------------------------------

:code:`''`

Selection based on intents. Default is all.


array
---------------------------------------

:code:`''`

Selection based on array IDs. Default is all.


observation
---------------------------------------

:code:`''`

Selection based on observation IDs. Default is all.


combine
---------------------------------------

:code:`''`

Ignore changes in these columns (scan, field, and/or state) when aggregating samples to compute weights. The value "corr" is also supported to aggregate samples across correlations.


timebin
---------------------------------------

:code:`int(1)`

Length for binning in time to determine statistics. Can either be integer to be multiplied by the representative integration time, a quantity (string) in time units


slidetimebin
---------------------------------------

:code:`False`

Use a sliding window for time binning, as opposed to time block processing?


chanbin
---------------------------------------

:code:`'spw'`

Channel bin width for computing weights. Can either be integer, in which case it is interpreted as number of channels to include in each bin, or a string "spw" or quantity with frequency units.


minsamp
---------------------------------------

:code:`int(2)`

Minimum number of unflagged visibilities required for computing weights in a sample. Must be >= 2.


statalg
---------------------------------------

:code:`'classic'`

Statistics algorithm to use for computing variances. Supported values are "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported, although the full string must be specified for the subparameters to appear in the inputs list.


fence
---------------------------------------

:code:`float(-1)`

Fence value for statalg="hinges-fences". A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if statalg is not "hinges-fences".


center
---------------------------------------

:code:`'mean'`

Center to use for statalg="fit-half". Valid choices are "mean", "median", and "zero". Ignored if statalg is not "fit-half".


lside
---------------------------------------

:code:`True`

For statalg="fit-half", real data are <=; center? If false, real data are >= center. Ignored if statalg is not "fit-half".


zscore
---------------------------------------

:code:`float(-1)`

For statalg="chauvenet", this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet\'s criterion. Ignored if statalg is not "chauvenet".


maxiter
---------------------------------------

:code:`int(-1)`

For statalg="chauvenet", this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if statalg is not "chauvenet".


excludechans
---------------------------------------

:code:`''`

Channels to exclude from the computation of weights. Specified as an MS select channel selection string.


wtrange
---------------------------------------

:code:`numpy.array( [  ] )`

Range of acceptable weights. Data with weights outside this range will be flagged. Empty array (default) means all weights are good.


flagbackup
---------------------------------------

:code:`True`

Back up the state of flags before the run?


preview
---------------------------------------

:code:`False`

Preview mode. If True, no data is changed, although the amount of data that would have been flagged is reported.


datacolumn
---------------------------------------

:code:`'corrected'`

Data column to use to compute weights. Supported values are "data", "corrected", "residual", and "residual_data" (case insensitive, minimum match supported).




