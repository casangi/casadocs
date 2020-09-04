#
# stub function definition file for docstring parsing
#

def wvrgcal(vis, caltable='', toffset=0, segsource=True, sourceflag=[''], tie=[''], nsol=1, disperse=False, wvrflag=[''], statfield='', statsource='', smooth='', scale=1., spw=[''], wvrspw=[''], reversespw='', cont=False, maxdistm=500., minnumants=2, mingoodfrac=0.8, usefieldtab=False, refant=[''], offsetstable=''):
    r"""
Generate a gain table based on Water Vapour Radiometer data

Parameters
   - **vis** (string) -  [1]_
   - **caltable** (string='') -  [2]_
   - **toffset** (double=0) -  [3]_
   - **segsource** (bool=True) -  [4]_

      .. raw:: html

         <details><summary><i> segsource = True </i></summary>

      - **tie** (stringArray=['']) -  [6]_
      - **sourceflag** (stringArray=['']) -  [5]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> segsource = False </i></summary>

      - **nsol** (int=1) -  [7]_

      .. raw:: html

         </details>
   - **disperse** (bool=False) -  [8]_
   - **wvrflag** (stringArray=['']) -  [9]_
   - **statfield** (string='') -  [10]_
   - **statsource** (string='') -  [11]_
   - **smooth** (string='') -  [12]_
   - **scale** (double=1.) -  [13]_
   - **spw** (intArray=['']) -  [14]_
   - **wvrspw** (intArray=['']) -  [15]_
   - **reversespw** (string='') -  [16]_
   - **cont** (bool=False) -  [17]_
   - **maxdistm** (double=500.) -  [18]_
   - **minnumants** (int=2) -  [19]_
   - **mingoodfrac** (double=0.8) -  [20]_
   - **usefieldtab** (bool=False) -  [21]_
   - **refant** (stringArray=['']) -  [22]_
   - **offsetstable** (string='') -  [23]_


Description
   .. rubric:: Summary
      

   | Information about the observation and the performance of
     **wvrgcal** is written to the CASA logger and also returned in a
     dictionary; see the `Water Vapor Radiometer Gain
     Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/water-vapor-radiometer-gain-calibration-wvrgcal>`__chapter
     in `Synthesis
     Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration>`__for
     a more detailed description of these parameters. The dictionary
     element 'success' is True if no errors occured.
   | Of particular note is the discrepancy statistic (Disc): high
     values (> a few hundred microns) may indicate some levels of
     cloud contamination and the effect of applying the **wvrgcal**
     correction should be checked; values > 1000 :math:`\mu` m in
     all antennas have currently been found to indicate that
     **wvrgcal** correction should not be used.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input visibility file. Default: none. Examples:
   *vis='ngc5921.ms'*

   .. rubric:: *caltable*
      

   Name of output gain calibration table. Default: none. Examples:
   *caltable='ngc5921.wvr'*

   .. rubric:: *toffset*
      

   Time offset (sec) between interferometric and WVR data. Default: 0
   (ALMA default for cycle 1, for cycle 0, i.e. up to Jan 2013 it was
   -1)

   .. rubric:: *segsource*
      

   Do a new coefficient calculation for each source. Default: True

   .. rubric:: *tie*
      

   Prioritise tieing the phase of these sources as well as possible
   (requires *segsource=True*). Default: [ ]. Examples:
   *tie=['3C273,NGC253', 'IC433,3C279']*

   .. rubric:: *sourceflag*
      

   Flag the WVR data for these source(s) as bad and do not produce
   corrections for it (requires *segsource=True*). Default: [ ].
   Examples: *sourceflag=['3C273']*

   .. rubric:: *nsol*
      

   Number of solutions for phase correction coefficients during this
   observation. By default only one set of coefficients is generated
   for the entire observation. If more sets are requested, then they
   will be evenly distributed in time throughout the observation.
   Values > 1 require *segsource=False*. Default: 1

   .. rubric:: *disperse*
      

   Apply correction for dispersion. Default: False

   .. rubric:: *wvrflag*
      

   Regard the WVR data for these antenna(s) as bad and use
   interpolated values instead. Default: [ ]. Examples:
   *wvrflag=['DV03','DA05','PM02']*

   .. rubric:: *statfield*
      

   Compute the statistics (Phase RMS, Disc) on this field only.
   Default: '' (all)

   .. rubric:: *statsource*
      

   Compute the statistics (Phase RMS, Disc) on this source only.
   Default: '' (all)

   .. rubric:: *smooth*
      

   Smooth the calibration solution on the given timescale. Default:
   '' (no smoothing). Examples: *smooth='3s'* smooth on a timescale
   of 3 seconds.

   .. rubric:: *scale*
      

   Scale the entire phase correction by this factor. Default: 1. (no
   scaling)

   .. rubric:: *spw*
      

   List of the spectral window IDs for which solutions should be
   saved into the caltable. Default: [ ] (all spectral windows).
   Examples: *spw=[17,19,21,23]*

   .. rubric:: *wvrspw*
      

   List of the spectral window IDs from which the WVR data should be
   taken. Default: [ ] (all WVR spectral windows). Examples:
   *wvrspw=[0]*

   .. rubric:: *reversespw*
      

   Reverse the sign of the correction for the listed SPWs (only neede
   for early ALMA data before Cycle 0). Default: '' (none). Examples:
   *reversespw='0~2,4'*; spectral windows 0,1,2,4

   .. rubric:: *cont*
      

   Estimate the continuum (e.g., due to clouds). Default: False

   .. rubric:: *maxdistm*
      

   Maximum distance (m) an antenna may have to be considered for
   being part of the antenna set (minnumants to 3 antennas) for the
   interpolation of a solution for a flagged antenna. Default: 500.

   .. rubric:: *minnumants*
      

   Minimum number of near antennas required for interpolation.
   Default: 2

   .. rubric:: *mingoodfrac*
      

   If the fraction of unflagged data for an antenna is below this
   value (0.0 to 1.0), the antenna is flagged. Default: 0.8

   .. rubric:: *usefieldtab*
      

   Derive the antenna AZ/EL values from the FIELD rather than the
   POINTING table. Default: False

   .. rubric:: *refant*
      

   Use the WVR data from this antenna for calculating the dT/dL
   parameters (can give ranked list). Default: '' (use the first good
   or interpolatable antenna), Examples: *refant='DA45'* - use DA45;
   *refant=['DA45','DV51']* - use DA45 and if that is not good, use
   DV51 instead.

   .. rubric:: *offsetstable*
      

   Subtract the temperature offsets in this table from the WVR
   measurements before using them to calculate the phase corrections
   (experimental). Default: '' (do not apply any offsets). Examples:
   *offsetstable='uid___A002_Xabd867_X2277.cloud_offsets'* use the
   given table.




Details
   Explanation of each parameter

.. [1] 
   **vis** (string)
      | Name of input visibility file
.. [2] 
   **caltable** (string='')
      | Name of output gain calibration table
.. [3] 
   **toffset** (double=0)
      | Time offset (sec) between interferometric and WVR data
.. [4] 
   **segsource** (bool=True)
      | Do a new coefficient calculation for each source
.. [5] 
   **sourceflag** (stringArray=[''])
      | Regard the WVR data for these source(s) as bad and do not produce corrections for it (requires segsource=True)
.. [6] 
   **tie** (stringArray=[''])
      | Prioritise tieing the phase of these sources as well as possible (requires segsource=True)
.. [7] 
   **nsol** (int=1)
      | Number of solutions for phase correction coefficients (nsol>1 requires segsource=False)
.. [8] 
   **disperse** (bool=False)
      | Apply correction for dispersion
.. [9] 
   **wvrflag** (stringArray=[''])
      | Regard the WVR data for these antenna(s) as bad and replace its data with interpolated values from neighbouring antennas
.. [10] 
   **statfield** (string='')
      | Compute the statistics (Phase RMS, Disc) on this field only
.. [11] 
   **statsource** (string='')
      | Compute the statistics (Phase RMS, Disc) on this source only
.. [12] 
   **smooth** (string='')
      | Smooth calibration solution on the given timescale
.. [13] 
   **scale** (double=1.)
      | Scale the entire phase correction by this factor
.. [14] 
   **spw** (intArray=[''])
      | List of the spectral window IDs for which solutions should be saved into the caltable
.. [15] 
   **wvrspw** (intArray=[''])
      | List of the spectral window IDs from which the WVR data should be taken
.. [16] 
   **reversespw** (string='')
      | Reverse the sign of the correction for the listed SPWs (only needed for early ALMA data before Cycle 0)
.. [17] 
   **cont** (bool=False)
      | Estimate the continuum (e.g., due to clouds) (experimental)
.. [18] 
   **maxdistm** (double=500.)
      | maximum distance (m) of an antenna used for interpolation for a flagged antenna
.. [19] 
   **minnumants** (int=2)
      | minimum number of near antennas (up to 3) required for interpolation
.. [20] 
   **mingoodfrac** (double=0.8)
      | If the fraction of unflagged data for an antenna is below this value (0. to 1.), the antenna is flagged.
.. [21] 
   **usefieldtab** (bool=False)
      | derive the antenna AZ/EL values from the FIELD rather than the POINTING table
.. [22] 
   **refant** (stringArray=[''])
      | use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)
.. [23] 
   **offsetstable** (string='')
      | (experimental) subtract the temperature offsets in this table from the WVR measurements before calculating the phase corrections

    """
    pass
