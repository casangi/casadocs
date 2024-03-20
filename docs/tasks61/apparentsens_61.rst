apparentsens -- Imaging sensitivity estimataion -- imaging task
=======================================

Description
---------------------------------------
Estimates the expected imaging sensitivity as a function of the
               visibility weights and imaging parameters.




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
     - Name of input visibility file(s)
   * - field
     - :code:`''`
     - field(s) to select
   * - spw
     - :code:`''`
     - spw(s)/channels to select
   * - intent
     - :code:`''`
     - Scan Intent(s)
   * - selectdata
     - :code:`True`
     - Enable data selection parameters
   * - timerange
     - :code:`''`
     - Range of time to select from data
   * - uvrange
     - :code:`''`
     - Select data within uvrange
   * - antenna
     - :code:`''`
     - Select data based on antenna/baseline
   * - scan
     - :code:`''`
     - Scan number range
   * - observation
     - :code:`''`
     - Observation ID range
   * - imsize
     - :code:`numpy.array( [  ] )`
     - Number of pixels
   * - cell
     - :code:`numpy.array( [  ] )`
     - Cell size
   * - stokes
     - :code:`'I'`
     - Stokes Planes to make (I only, for now)
   * - specmode
     - :code:`'mfs'`
     - Spectral definition mode (mfs only, for now)
   * - weighting
     - :code:`'natural'`
     - Weighting scheme (natural,uniform,briggs)
   * - robust
     - :code:`float(0.5)`
     - Robustness parameter
   * - npixels
     - :code:`int(0)`
     - Number of pixels to determine uv-cell size (0 : -/+ 3 pixels)
   * - uvtaper
     - :code:`numpy.array( [ '' ] )`
     - uv-taper on outer baselines in uv-plane



