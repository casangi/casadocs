predictcomp -- Make a component list for a known calibrator -- modeling, calibration task
=======================================

Description
---------------------------------------

	  Writes a component list named clist to disk and returns a dict of
	  {'clist': clist,
	   'objname': objname,
	   'standard': standard,
	   'epoch': epoch,
	   'freqs': pl.array of frequencies, in GHz,
	   'antennalist': a simdata type configuration file,
	   'amps':  pl.array of predicted visibility amplitudes, in Jy,
	   'savedfig': False or, if made, the filename of a plot.}
	  or False on error.
	


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - objname
     - :code:`''`
     - 
   * - standard
     - :code:`'Butler-JPL-Horizons 2010'`
     - 
   * - epoch
     - :code:`''`
     - 
   * - minfreq
     - :code:`''`
     - 
   * - maxfreq
     - :code:`''`
     - 
   * - nfreqs
     - :code:`int(2)`
     - 
   * - prefix
     - :code:`''`
     - 
   * - antennalist
     - :code:`''`
     - 
   * - showplot
     - :code:`False`
     - 
   * - savefig
     - :code:`''`
     - 
   * - symb
     - :code:`'.'`
     - 
   * - include0amp
     - :code:`False`
     - 
   * - include0bl
     - :code:`False`
     - 
   * - blunit
     - :code:`''`
     - 
   * - showbl0flux
     - :code:`False`
     - 


Parameter Explanations
=======================================



objname
---------------------------------------

:code:`''`

Object name


standard
---------------------------------------

:code:`'Butler-JPL-Horizons 2010'`

Flux density standard


epoch
---------------------------------------

:code:`''`

Epoch


minfreq
---------------------------------------

:code:`''`

Minimum frequency


maxfreq
---------------------------------------

:code:`''`

Maximum frequency


nfreqs
---------------------------------------

:code:`int(2)`

Number of frequencies


prefix
---------------------------------------

:code:`''`

Prefix for the component list directory name.


antennalist
---------------------------------------

:code:`''`

Plot for this configuration


showplot
---------------------------------------

:code:`False`

Plot S vs |u| to the screen?


savefig
---------------------------------------

:code:`''`

Save a plot of S vs |u| to this filename


symb
---------------------------------------

:code:`'.'`

A matplotlib plot symbol code


include0amp
---------------------------------------

:code:`False`

Force the amplitude axis to start at 0?


include0bl
---------------------------------------

:code:`False`

Force the baseline axis to start at 0?


blunit
---------------------------------------

:code:`''`

unit of the baseline axis


showbl0flux
---------------------------------------

:code:`False`

Print the zero baseline flux ?




