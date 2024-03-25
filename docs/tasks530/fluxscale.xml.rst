fluxscale -- Bootstrap the flux density scale from standard calibrators -- calibration task
=======================================

Description
---------------------------------------


       Bootstrap the flux density scale from standard calibrators:

       After running gaincal on standard flux density calibrators (with or
       without an image model), and other calibrators with unknown flux
       densities (assumed 1 Jy), fluxscale applies the constraint that
       net system gain was, in fact, independent of field, on average,
       and that field-dependent gains in the input caltable are solely
       a result of the unknown flux densities for the calibrators.
       Using time-averaged gain amplitudes, the ratio between 
       each ordinary calibrator and the flux density calibrator(s) is 
       formed for each antenna and polarization (that they have in
       common).  The average of this ratio over antennas and polarizations
       yields a correction factor that is applied to the ordinary 
       calibrators' gains. (See also more detailed discussion in Example section below.)

	


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
   * - caltable
     - :code:`''`
     - 
   * - fluxtable
     - :code:`''`
     - 
   * - reference
     - :code:`numpy.array( [  ] )`
     - 
   * - transfer
     - :code:`numpy.array( [  ] )`
     - 
   * - listfile
     - :code:`''`
     - 
   * - append
     - :code:`False`
     - 
   * - refspwmap
     - :code:`numpy.array( [  ] )`
     - 
   * - gainthreshold
     - :code:`float(-1.0)`
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
   * - incremental
     - :code:`False`
     - 
   * - fitorder
     - :code:`int(1)`
     - 
   * - display
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

Name of input visibility file (MS)


caltable
---------------------------------------

:code:`''`

Name of input calibration table


fluxtable
---------------------------------------

:code:`''`

Name of output, flux-scaled calibration table


reference
---------------------------------------

:code:`numpy.array( [  ] )`

Reference field name(s) (transfer flux scale FROM)


transfer
---------------------------------------

:code:`numpy.array( [  ] )`

Transfer field name(s) (transfer flux scale TO), \'\' -> all


listfile
---------------------------------------

:code:`''`

Name of listfile that contains the fit information.  Default is '' (no file).


append
---------------------------------------

:code:`False`

Append solutions?


refspwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Scale across spectral window boundaries.  See help fluxscale


gainthreshold
---------------------------------------

:code:`float(-1.0)`

Threshold (% deviation from the median) on gain amplitudes to be used in the flux scale calculation


antenna
---------------------------------------

:code:`''`

antennas to include/exclude


timerange
---------------------------------------

:code:`''`

sub selection by timerange


scan
---------------------------------------

:code:`''`

sub selection by scan


incremental
---------------------------------------

:code:`False`

incremental caltable


fitorder
---------------------------------------

:code:`int(1)`

order of spectral fitting


display
---------------------------------------

:code:`False`

display some statistics of flux scaling


fluxd
---------------------------------------

:code:`[ ]`

Dictionary containing the transfer fluxes and their errors.




