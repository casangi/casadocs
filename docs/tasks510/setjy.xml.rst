setjy -- Fills the model column with the visibilities of a calibrator -- modeling, calibration task
=======================================

Description
---------------------------------------

       This task places the model visibility amp and phase associated
       with a specified clean components image into the model column
       of the data set.  The flux density (I,Q,U,V) for a point source
       calibrator can be entered explicitly.

       Models are available for 3C48, 3C138, and 3C286 between
       1.4 and 43 GHz.  3C147 is available above 13 GHz.  These models
       are scaled to the precise frequency of the data.  Only I models are
       presently available.

       The location of the models is system dependent:  At the AOC, the
       models are in the directory::/usr/lib/casapy/data/nrao/VLA/CalModels/
       3C286_L.im (egs)

       setjy need only be run on the calibrator sources with a known flux
       density and/or model.

       For Solar System Objects, model determination was updated and it is 
       available via the 'Butler-JPL-Horizons 2012' standard.
       
       Currently they are modeled as uniform
       temperature disks based on their ephemeris at the time of
       observation (note that this may oversimplify objects, in
       particular asteroids). Specify the name of the object in the
       'field' parameter. 

	


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
   * - selectdata
     - :code:`False`
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
   * - observation
     - :code:`''`
     - 
   * - scalebychan
     - :code:`True`
     - 
   * - standard
     - :code:`'Perley-Butler 2013'`
     - 
   * - model
     - :code:`''`
     - 
   * - modimage
     - :code:`''`
     - 
   * - listmodels
     - :code:`False`
     - 
   * - fluxdensity
     - :code:`int(-1)`
     - 
   * - spix
     - :code:`float(0.0)`
     - 
   * - reffreq
     - :code:`'1GHz'`
     - 
   * - polindex
     - :code:`numpy.array( [  ] )`
     - 
   * - polangle
     - :code:`numpy.array( [  ] )`
     - 
   * - rotmeas
     - :code:`float(0.0)`
     - 
   * - fluxdict
     - :code:`{ }`
     - 
   * - useephemdir
     - :code:`False`
     - 
   * - interpolation
     - :code:`'nearest'`
     - 
   * - usescratch
     - :code:`False`
     - 
   * - ismms
     - :code:`False`
     - 
   * - fluxd
     - :code:`[ ]`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


field
---------------------------------------

:code:`''`

Field name(s)


spw
---------------------------------------

:code:`''`

Spectral window identifier (list)


selectdata
---------------------------------------

:code:`False`

Other data selection parameters


timerange
---------------------------------------

:code:`''`

Time range to operate on (for usescratch=T)


scan
---------------------------------------

:code:`''`

Scan number range (for usescaratch=T)


intent
---------------------------------------

:code:`''`

Observation intent


observation
---------------------------------------

:code:`''`

Observation ID range (for usescratch=T)


scalebychan
---------------------------------------

:code:`True`

scale the flux density on a per channel basis or else on a per spw basis


standard
---------------------------------------

:code:`'Perley-Butler 2013'`

Flux density standard


model
---------------------------------------

:code:`''`

File location for field model


modimage
---------------------------------------

:code:`''`

File location for field model


listmodels
---------------------------------------

:code:`False`

List the available models for VLA calibrators or Tb models for Solar System objects


fluxdensity
---------------------------------------

:code:`int(-1)`

Specified flux density in Jy [I,Q,U,V]; (-1 will lookup values)


spix
---------------------------------------

:code:`float(0.0)`

Spectral index (including higher terms) of I fluxdensity


reffreq
---------------------------------------

:code:`'1GHz'`

Reference frequency for spix


polindex
---------------------------------------

:code:`numpy.array( [  ] )`

Coefficients of an expansion of frequency-dependent linear polarization fraction expression


polangle
---------------------------------------

:code:`numpy.array( [  ] )`

Coefficients of an expansion of frequency-dependent polarization angle expression (in radians) 


rotmeas
---------------------------------------

:code:`float(0.0)`

Rotation measure (in rad/m^2)


fluxdict
---------------------------------------

:code:`{ }`

output dictionary from fluxscale


useephemdir
---------------------------------------

:code:`False`

use directions in the ephemeris table


interpolation
---------------------------------------

:code:`'nearest'`

method to be used to interpolate in time


usescratch
---------------------------------------

:code:`False`

Will create if necessary and use the MODEL_DATA 


ismms
---------------------------------------

:code:`False`

to be used internally for MMS


fluxd
---------------------------------------

:code:`[ ]`

Dictionary containing flux densities and their errors.




