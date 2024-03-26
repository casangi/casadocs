wvrgcal -- Generate a gain table based on Water Vapour Radiometer data -- calibration task
=======================================

Description
---------------------------------------


Information about the observation and the performance of WVRGCAL is written to the CASA logger
and also returned in a dictionary; see the CASA cookbook for a more detailed description of these parameters.
The dictionary element 'success' is True if no errors occured.

Of particular note is the discrepancy parameter (Disc): high values (> a few hundred microns) 
may indicate some levels of cloud contamination and the effect of applying the WVRGCAL correction 
should be checked; values > 1000 um in all antennas have currently been found to indicate that 
WVRGCAL correction should not be used.

      
  vis -- Name of input visibility file
              default: none; example: vis='ngc5921.ms'

  caltable -- Name of output gain calibration table
              default: none; example: caltable='ngc5921.wvr'

  toffset -- Time offset (sec) between interferometric and WVR data
             default: 0 (ALMA default for cycle 1, for cycle 0, i.e. up to Jan 2013 it was -1)

  segsource -- Do a new coefficient calculation for each source
               default: True

  tie -- Prioritise tieing the phase of these sources as well as possible
         (requires segsource=True)
         default: [] example: ['3C273,NGC253', 'IC433,3C279']

  sourceflag -- Flag the WVR data for these source(s) as bad and do not produce corrections for it
               (requires segsource=True)
               default: [] (none) example: ['3C273']

  nsol -- Number of solutions for phase correction coefficients during this observation.
          By default only one set of coefficients is generated for the entire observation. 
          If more sets are requested, then they will be evenly distributed in time throughout 
          the observation. Values > 1 require segsource=False.
          default: 1

  disperse -- Apply correction for dispersion
             default: False

  wvrflag -- Regard the WVR data for these antenna(s) as bad and use interpolated values instead
             default: [] (none) example: ['DV03','DA05','PM02']           

  statfield -- Compute the statistics (Phase RMS, Disc) on this field only
               default: '' (all) 

  statsource -- Compute the statistics (Phase RMS, Disc) on this source only
                default: '' (all)             

  smooth -- Smooth the calibration solution on the given timescale 
	    default: '' (no smoothing), example: '3s' smooth on a timescale of 3 seconds									

  scale -- Scale the entire phase correction by this factor
           default: 1. (no scaling)

  spw -- List of the spectral window IDs for which solutions should be saved into the caltable
	   default: [] (all spectral windows), example [17,19,21,23]

  wvrspw -- List of the spectral window IDs from which the WVR data should be taken
	   default: [] (all WVR spectral windows), example [0]

  reversespw -- Reverse the sign of the correction for the listed SPWs
                (only neede for early ALMA data before Cycle 0)
                default: '' (none), example: reversespw='0~2,4'; spectral windows 0,1,2,4

  cont -- Estimate the continuum (e.g., due to clouds)
          default: False

  maxdistm -- maximum distance (m) an antenna may have to be considered for being part
              of the antenna set (minnumants to 3 antennas) for the interpolation of a solution 
              for a flagged antenna
	      default: 500.

  minnumants -- minimum number of near antennas required for interpolation
	        default: 2

  mingoodfrac -- If the fraction of unflagged data for an antenna is below this value (0. to 1.), 
                 the antenna is flagged.
                 default: 0.8

  usefieldtab -- derive the antenna AZ/EL values from the FIELD rather than the POINTING table
	         default: False

  refant -- use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)
                default: '' (use the first good or interpolatable antenna), 
                examples: 'DA45' - use DA45 
                          ['DA45','DV51'] - use DA45 and if that is not good, use DV51 instead

  offsetstable -- (experimental) subtract the temperature offsets in this table from the WVR measurements before
             using them to calculate the phase corrections
                default: '' (do not apply any offsets)
		examples: 'uid___A002_Xabd867_X2277.cloud_offsets' use the given table

  


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
   * - toffset
     - :code:`float(0)`
     - 
   * - segsource
     - :code:`True`
     - 
   * - sourceflag
     - :code:`numpy.array( [  ] )`
     - 
   * - tie
     - :code:`numpy.array( [  ] )`
     - 
   * - nsol
     - :code:`int(1)`
     - 
   * - disperse
     - :code:`False`
     - 
   * - wvrflag
     - :code:`numpy.array( [  ] )`
     - 
   * - statfield
     - :code:`''`
     - 
   * - statsource
     - :code:`''`
     - 
   * - smooth
     - :code:`''`
     - 
   * - scale
     - :code:`float(1.)`
     - 
   * - spw
     - :code:`numpy.array( [  ] )`
     - 
   * - wvrspw
     - :code:`numpy.array( [  ] )`
     - 
   * - reversespw
     - :code:`''`
     - 
   * - cont
     - :code:`False`
     - 
   * - maxdistm
     - :code:`float(500.)`
     - 
   * - minnumants
     - :code:`int(2)`
     - 
   * - mingoodfrac
     - :code:`float(0.8)`
     - 
   * - usefieldtab
     - :code:`False`
     - 
   * - refant
     - :code:`numpy.array( [  ] )`
     - 
   * - offsetstable
     - :code:`''`
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


toffset
---------------------------------------

:code:`float(0)`

Time offset (sec) between interferometric and WVR data


segsource
---------------------------------------

:code:`True`

Do a new coefficient calculation for each source


sourceflag
---------------------------------------

:code:`numpy.array( [  ] )`

Regard the WVR data for these source(s) as bad and do not produce corrections for it (requires segsource=True)


tie
---------------------------------------

:code:`numpy.array( [  ] )`

Prioritise tieing the phase of these sources as well as possible (requires segsource=True)


nsol
---------------------------------------

:code:`int(1)`

Number of solutions for phase correction coefficients (nsol>1 requires segsource=False)


disperse
---------------------------------------

:code:`False`

Apply correction for dispersion


wvrflag
---------------------------------------

:code:`numpy.array( [  ] )`

Regard the WVR data for these antenna(s) as bad and replace its data with interpolated values from neighbouring antennas


statfield
---------------------------------------

:code:`''`

Compute the statistics (Phase RMS, Disc) on this field only


statsource
---------------------------------------

:code:`''`

Compute the statistics (Phase RMS, Disc) on this source only


smooth
---------------------------------------

:code:`''`

Smooth calibration solution on the given timescale


scale
---------------------------------------

:code:`float(1.)`

Scale the entire phase correction by this factor


spw
---------------------------------------

:code:`numpy.array( [  ] )`

List of the spectral window IDs for which solutions should be saved into the caltable


wvrspw
---------------------------------------

:code:`numpy.array( [  ] )`

List of the spectral window IDs from which the WVR data should be taken


reversespw
---------------------------------------

:code:`''`

Reverse the sign of the correction for the listed SPWs (only needed for early ALMA data before Cycle 0)


cont
---------------------------------------

:code:`False`

Estimate the continuum (e.g., due to clouds) (experimental)


maxdistm
---------------------------------------

:code:`float(500.)`

maximum distance (m) of an antenna used for interpolation for a flagged antenna


minnumants
---------------------------------------

:code:`int(2)`

minimum number of near antennas (up to 3) required for interpolation


mingoodfrac
---------------------------------------

:code:`float(0.8)`

If the fraction of unflagged data for an antenna is below this value (0. to 1.), the antenna is flagged.


usefieldtab
---------------------------------------

:code:`False`

derive the antenna AZ/EL values from the FIELD rather than the POINTING table


refant
---------------------------------------

:code:`numpy.array( [  ] )`

use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)


offsetstable
---------------------------------------

:code:`''`

(experimental) subtract the temperature offsets in this table from the WVR measurements before calculating the phase corrections




