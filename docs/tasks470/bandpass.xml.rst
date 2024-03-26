bandpass -- Calculates a bandpass calibration solution -- calibration task
=======================================

Description
---------------------------------------

Determines the amplitude and phase as a function of frequency for
each spectral window containing more than one channel.  Strong sources
(or many observations of moderately strong sources) are needed to obtain
accurate bandpass functions.  The two solution choices are: Individual
antenna/based channel solutions 'B'; and a polynomial fit over the channels
'BPOLY'.  The 'B' solutions can determined at any specified time interval, and
is recommended in most applications.



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
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - selectdata
     - :code:`True`
     - 
   * - timerange
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - msselect
     - :code:`''`
     - 
   * - solint
     - :code:`'inf'`
     - 
   * - combine
     - :code:`'scan'`
     - 
   * - refant
     - :code:`''`
     - 
   * - minblperant
     - :code:`int(4)`
     - 
   * - minsnr
     - :code:`float(3.0)`
     - 
   * - solnorm
     - :code:`False`
     - 
   * - bandtype
     - :code:`'B'`
     - 
   * - smodel
     - :code:`numpy.array( [  ] )`
     - 
   * - append
     - :code:`False`
     - 
   * - fillgaps
     - :code:`int(0)`
     - 
   * - degamp
     - :code:`int(3)`
     - 
   * - degphase
     - :code:`int(3)`
     - 
   * - visnorm
     - :code:`False`
     - 
   * - maskcenter
     - :code:`int(0)`
     - 
   * - maskedge
     - :code:`int(5)`
     - 
   * - docallib
     - :code:`False`
     - 
   * - callib
     - :code:`''`
     - 
   * - gaintable
     - :code:`numpy.array( [  ] )`
     - 
   * - gainfield
     - :code:`numpy.array( [  ] )`
     - 
   * - interp
     - :code:`numpy.array( [  ] )`
     - 
   * - spwmap
     - :code:`numpy.array( [  ] )`
     - 
   * - parang
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


caltable
---------------------------------------

:code:`''`

Name of output gain calibration table


field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


intent
---------------------------------------

:code:`''`

Select observing intent


selectdata
---------------------------------------

:code:`True`

Other data selection parameters


timerange
---------------------------------------

:code:`''`

Select data based on time range


uvrange
---------------------------------------

:code:`''`

Select data within uvrange (default units meters)


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


scan
---------------------------------------

:code:`''`

Scan number range


observation
---------------------------------------

:code:`''`

Select by observation ID(s)


msselect
---------------------------------------

:code:`''`

Optional complex data selection (ignore for now)


solint
---------------------------------------

:code:`'inf'`

Solution interval in time[,freq]


combine
---------------------------------------

:code:`'scan'`

Data axes which to combine for solve (obs, scan, spw, and/or field)


refant
---------------------------------------

:code:`''`

Reference antenna name(s)


minblperant
---------------------------------------

:code:`int(4)`

Minimum baselines _per antenna_ required for solve


minsnr
---------------------------------------

:code:`float(3.0)`

Reject solutions below this SNR (only applies for bandtype = B)


solnorm
---------------------------------------

:code:`False`

Normalize average solution amplitudes to 1.0 


bandtype
---------------------------------------

:code:`'B'`

Type of bandpass solution (B or BPOLY)


smodel
---------------------------------------

:code:`numpy.array( [  ] )`

Point source Stokes parameters for source model.


append
---------------------------------------

:code:`False`

Append solutions to the (existing) table


fillgaps
---------------------------------------

:code:`int(0)`

Fill flagged solution channels by interpolation


degamp
---------------------------------------

:code:`int(3)`

Polynomial degree for BPOLY amplitude solution


degphase
---------------------------------------

:code:`int(3)`

Polynomial degree for BPOLY phase solution


visnorm
---------------------------------------

:code:`False`

Normalize data prior to BPOLY solution


maskcenter
---------------------------------------

:code:`int(0)`

Number of channels to avoid in center of each band


maskedge
---------------------------------------

:code:`int(5)`

Fraction of channels to avoid at each band edge (in %)


docallib
---------------------------------------

:code:`False`

Use callib or traditional cal apply parameters


callib
---------------------------------------

:code:`''`

Cal Library filename


gaintable
---------------------------------------

:code:`numpy.array( [  ] )`

Gain calibration table(s) to apply on the fly


gainfield
---------------------------------------

:code:`numpy.array( [  ] )`

Select a subset of calibrators from gaintable(s)


interp
---------------------------------------

:code:`numpy.array( [  ] )`

Interpolation mode (in time) to use for each gaintable


spwmap
---------------------------------------

:code:`numpy.array( [  ] )`

Spectral windows combinations to form for gaintables(s)


parang
---------------------------------------

:code:`False`

Apply parallactic angle correction




