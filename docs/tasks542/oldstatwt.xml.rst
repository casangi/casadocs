oldstatwt -- Reweight visibilities according to their scatter (Experimental) -- manipulation task
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
   * - dorms
     - :code:`False`
     - 
   * - byantenna
     - :code:`False`
     - 
   * - sepacs
     - :code:`True`
     - 
   * - fitspw
     - :code:`''`
     - 
   * - fitcorr
     - :code:`''`
     - 
   * - combine
     - :code:`''`
     - 
   * - timebin
     - :code:`'0s'`
     - 
   * - minsamp
     - :code:`int(2)`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - observation
     - :code:`''`
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


dorms
---------------------------------------

:code:`False`

Use rms instead of stddev?


byantenna
---------------------------------------

:code:`False`

Estimate the noise per antenna -not implemented (vs. per baseline)


sepacs
---------------------------------------

:code:`True`

If solving by antenna, treat autocorrs separately (not implemented)


fitspw
---------------------------------------

:code:`''`

The signal-free spectral window:channels to estimate the scatter from


fitcorr
---------------------------------------

:code:`''`

The signal-free correlation(s) to estimate the scatter from (not implemented)


combine
---------------------------------------

:code:`''`

Let estimates span changes in spw, corr, scan and/or state


timebin
---------------------------------------

:code:`'0s'`

Bin length for estimates (not implemented)


minsamp
---------------------------------------

:code:`int(2)`

Minimum number of unflagged visibilities for estimating the scatter


field
---------------------------------------

:code:`''`

Select field using ID(s) or name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


timerange
---------------------------------------

:code:`''`

Select data by time range


scan
---------------------------------------

:code:`''`

Select data by scan numbers


intent
---------------------------------------

:code:`''`

Select data by scan intents


array
---------------------------------------

:code:`''`

Select (sub)array(s) by array ID number


correlation
---------------------------------------

:code:`''`

Select correlations to reweight (DEPRECATED in CASA v4.5)


observation
---------------------------------------

:code:`''`

Select by observation ID(s)


datacolumn
---------------------------------------

:code:`'corrected'`

Which data column to calculate the scatter from




