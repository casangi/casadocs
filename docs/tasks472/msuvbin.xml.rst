msuvbin -- grid the visibility data onto a defined uniform grid (in the form of an ms); multiple MS\'s can be done onto the same grid -- ms, averaging task
=======================================

Description
---------------------------------------

	  msuvbin is a uv gridding task. The use is for large volumes
	  of data (from multiple epochs) that needs to be imaged into
	  one image.  One way of proceeding is to image the epochs and
	  average them after wards. Rather than doing this averaging
	  the visibilities on a common uv grid has several convenience
	  advantages like easily doing the proper weighted averaging and imaging.
	  If an output grid already exists and a second ms is gridded on the grid 
	  then the output grid parameters is ignored but the existant grid is used.

	


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
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - taql
     - :code:`''`
     - 
   * - outvis
     - :code:`''`
     - 
   * - phasecenter
     - :code:`''`
     - 
   * - nx
     - :code:`int(1000)`
     - 
   * - ny
     - :code:`int(1000)`
     - 
   * - cell
     - :code:`'1arcsec'`
     - 
   * - ncorr
     - :code:`int(1)`
     - 
   * - nchan
     - :code:`int(1)`
     - 
   * - fstart
     - :code:`'1GHz'`
     - 
   * - fstep
     - :code:`'1kHz'`
     - 
   * - wproject
     - :code:`False`
     - 
   * - memfrac
     - :code:`float(0.5)`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file (MS)


field
---------------------------------------

:code:`''`

Field selection of input ms


spw
---------------------------------------

:code:`''`

Spw selection


taql
---------------------------------------

:code:`''`

TaQl string for data selection


outvis
---------------------------------------

:code:`''`

name of output uvgrid


phasecenter
---------------------------------------

:code:`''`

phase center of uv grid


nx
---------------------------------------

:code:`int(1000)`

Number of pixels of grid along the x-axis


ny
---------------------------------------

:code:`int(1000)`

Number of pixels of grid along the y-axis


cell
---------------------------------------

:code:`'1arcsec'`

pixel cell size defined in sky dimension


ncorr
---------------------------------------

:code:`int(1)`

number of correlations to store in grid


nchan
---------------------------------------

:code:`int(1)`

Number of spectral channels in grid


fstart
---------------------------------------

:code:`'1GHz'`

Frequency of first spectral channel


fstep
---------------------------------------

:code:`'1kHz'`

spectral channel width


wproject
---------------------------------------

:code:`False`

Do wprojection correction while gridding


memfrac
---------------------------------------

:code:`float(0.5)`

Limit how much of memory to use




