uvcontsub -- Continuum fitting and subtraction in the uv plane -- modeling, manipulation task
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
     - Name of input MS.  Output goes to vis + ".contsub" (will be overwritten if already exists)
   * - field
     - :code:`''`
     - Select field(s) using id(s) or name(s)
   * - fitspw
     - :code:`''`
     - Spectral window:channel selection for fitting the continuum
   * - excludechans
     - :code:`False`
     - exclude Spectral window:channel selection in fitspw for fitting
   * - combine
     - :code:`''`
     - Data axes to combine for the continuum estimation (none, or spw and/or scan)
   * - solint
     - :code:`'int'`
     - Continuum fit timescale (int recommended!)
   * - fitorder
     - :code:`int(0)`
     - Polynomial order for the fits
   * - spw
     - :code:`''`
     - Spectral window selection for output
   * - want_cont
     - :code:`False`
     - Create vis + ".cont" to hold the continuum estimate.


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input MS.  Output goes to vis + ".contsub" (will be overwritten if already exists)


field
---------------------------------------

:code:`''`

Select field(s) using id(s) or name(s)


fitspw
---------------------------------------

:code:`''`

Spectral window:channel selection for fitting the continuum


excludechans
---------------------------------------

:code:`False`

exclude Spectral window:channel selection in fitspw for fitting


combine
---------------------------------------

:code:`''`

Data axes to combine for the continuum estimation (none, or spw and/or scan)


solint
---------------------------------------

:code:`'int'`

Continuum fit timescale (int recommended!)


fitorder
---------------------------------------

:code:`int(0)`

Polynomial order for the fits


spw
---------------------------------------

:code:`''`

Spectral window selection for output


want_cont
---------------------------------------

:code:`False`

Create vis + ".cont" to hold the continuum estimate.




