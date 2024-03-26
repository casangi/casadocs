ssoflux -- Fills the model column with the visibilities of a calibrator -- modeling, calibration task
=======================================

Description
---------------------------------------

          *This is an experimental clone of setjy while flux calibration with
           Solar System objects is being tested.  It will eventually be merged
           back into setjy.*

       The task places the model visibility amp and phase associated
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

       ssoflux need only be run on the calibrator sources with a known flux
       density and/or model.
	


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
   * - modimage
     - :code:`''`
     - 
   * - fluxdensity
     - :code:`int(-1)`
     - 
   * - standard
     - :code:`'Perley-Taylor 99'`
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


modimage
---------------------------------------

:code:`''`

File location for field model


fluxdensity
---------------------------------------

:code:`int(-1)`

Specified flux density [I,Q,U,V]; -1 will lookup values


standard
---------------------------------------

:code:`'Perley-Taylor 99'`

Flux density standard




