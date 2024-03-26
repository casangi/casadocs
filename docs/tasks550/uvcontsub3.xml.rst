uvcontsub3 -- An experimental clone of uvcontsub -- modeling, manipulation task
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
   * - fitspw
     - :code:`''`
     - 
   * - combine
     - :code:`''`
     - 
   * - fitorder
     - :code:`int(0)`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input MS.  Output goes to vis + ".contsub"


fitspw
---------------------------------------

:code:`''`

Spectral window:channel selection for fitting the continuum


combine
---------------------------------------

:code:`''`

Data axes to combine for the continuum estimation (none ('') or spw)


fitorder
---------------------------------------

:code:`int(0)`

Polynomial order for the fits


field
---------------------------------------

:code:`''`

Select field(s) using id(s) or name(s)


spw
---------------------------------------

:code:`''`

Spectral window selection for output


scan
---------------------------------------

:code:`''`

Select data by scan numbers


intent
---------------------------------------

:code:`''`

Select data by scan intents


correlation
---------------------------------------

:code:`''`

Select correlations


observation
---------------------------------------

:code:`''`

Select by observation ID(s)




