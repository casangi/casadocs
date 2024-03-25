widebandpbcor -- Wideband PB-correction on the output of the MS-MFS algorithm -- imaging task
=======================================

Description
---------------------------------------
WideBand Primary-beam correction. It computes a set of PBs at the specified frequencies, calculates Taylor-coefficient images that represent the PB spectrum, performs a polynomial division to PB-correct the output Taylor-coefficient images from clean(nterms>1), and recompute spectral index (and curvature) using the PB-corrected Taylor-coefficient images 


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
   * - imagename
     - :code:`''`
     - 
   * - nterms
     - :code:`int(2)`
     - 
   * - threshold
     - :code:`''`
     - 
   * - action
     - :code:`'pbcor'`
     - 
   * - reffreq
     - :code:`''`
     - 
   * - pbmin
     - :code:`float(0.2)`
     - 
   * - field
     - :code:`''`
     - 
   * - spwlist
     - :code:`numpy.array( [ int() ] )`
     - 
   * - chanlist
     - :code:`numpy.array( [ int() ] )`
     - 
   * - weightlist
     - :code:`numpy.array( [ float() ] )`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of measurement set. 


imagename
---------------------------------------

:code:`''`

Name-prefix of multi-termimages to operate on. 


nterms
---------------------------------------

:code:`int(2)`

Number of taylor terms to use


threshold
---------------------------------------

:code:`''`

Intensity above which to re-calculate spectral index 


action
---------------------------------------

:code:`'pbcor'`

PB-correction (pbcor) or only calc spectral-index (calcalpha)


reffreq
---------------------------------------

:code:`''`

Reference frequency (if specified in clean)


pbmin
---------------------------------------

:code:`float(0.2)`

PB threshold below which to not correct


field
---------------------------------------

:code:`''`

Fields to include in the PB calculation


spwlist
---------------------------------------

:code:`numpy.array( [ int() ] )`

List of N spw ids


chanlist
---------------------------------------

:code:`numpy.array( [ int() ] )`

List of N channel ids


weightlist
---------------------------------------

:code:`numpy.array( [ float() ] )`

List of N weights (relative)




