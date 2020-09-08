#
# stub function definition file for docstring parsing
#

def wvrgcal(vis, caltable='', toffset=0, segsource=True, sourceflag=[''], tie=[''], nsol=1, disperse=False, wvrflag=[''], statfield='', statsource='', smooth='', scale=1., spw=[''], wvrspw=[''], reversespw='', cont=False, maxdistm=500., minnumants=2, mingoodfrac=0.8, usefieldtab=False, refant=[''], offsetstable=''):
    r"""
Generate a gain table based on Water Vapour Radiometer data

Parameters
   - vis_ (string) - 
   - caltable_ (string='') - 
   - toffset_ (double=0) - 
   - segsource_ (bool=True) - 

      .. raw:: html

         <details><summary><i> segsource = True </i></summary>

      - tie_ (stringArray=['']) - 
      - sourceflag_ (stringArray=['']) - 

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> segsource = False </i></summary>

      - nsol_ (int=1) - 

      .. raw:: html

         </details>
   - disperse_ (bool=False) - 
   - wvrflag_ (stringArray=['']) - 
   - statfield_ (string='') - 
   - statsource_ (string='') - 
   - smooth_ (string='') - 
   - scale_ (double=1.) - 
   - spw_ (intArray=['']) - 
   - wvrspw_ (intArray=['']) - 
   - reversespw_ (string='') - 
   - cont_ (bool=False) - 
   - maxdistm_ (double=500.) - 
   - minnumants_ (int=2) - 
   - mingoodfrac_ (double=0.8) - 
   - usefieldtab_ (bool=False) - 
   - refant_ (stringArray=['']) - 
   - offsetstable_ (string='') - 


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

.. _vis:

   .. rubric:: vis

   | Name of input visibility file

.. _caltable:

   .. rubric:: caltable

   | Name of output gain calibration table

.. _toffset:

   .. rubric:: toffset

   | Time offset (sec) between interferometric and WVR data

.. _segsource:

   .. rubric:: segsource

   | Do a new coefficient calculation for each source

.. _sourceflag:

   .. rubric:: sourceflag

   | Regard the WVR data for these source(s) as bad and do not produce corrections for it (requires segsource=True)

.. _tie:

   .. rubric:: tie

   | Prioritise tieing the phase of these sources as well as possible (requires segsource=True)

.. _nsol:

   .. rubric:: nsol

   | Number of solutions for phase correction coefficients (nsol>1 requires segsource=False)

.. _disperse:

   .. rubric:: disperse

   | Apply correction for dispersion

.. _wvrflag:

   .. rubric:: wvrflag

   | Regard the WVR data for these antenna(s) as bad and replace its data with interpolated values from neighbouring antennas

.. _statfield:

   .. rubric:: statfield

   | Compute the statistics (Phase RMS, Disc) on this field only

.. _statsource:

   .. rubric:: statsource

   | Compute the statistics (Phase RMS, Disc) on this source only

.. _smooth:

   .. rubric:: smooth

   | Smooth calibration solution on the given timescale

.. _scale:

   .. rubric:: scale

   | Scale the entire phase correction by this factor

.. _spw:

   .. rubric:: spw

   | List of the spectral window IDs for which solutions should be saved into the caltable

.. _wvrspw:

   .. rubric:: wvrspw

   | List of the spectral window IDs from which the WVR data should be taken

.. _reversespw:

   .. rubric:: reversespw

   | Reverse the sign of the correction for the listed SPWs (only needed for early ALMA data before Cycle 0)

.. _cont:

   .. rubric:: cont

   | Estimate the continuum (e.g., due to clouds) (experimental)

.. _maxdistm:

   .. rubric:: maxdistm

   | maximum distance (m) of an antenna used for interpolation for a flagged antenna

.. _minnumants:

   .. rubric:: minnumants

   | minimum number of near antennas (up to 3) required for interpolation

.. _mingoodfrac:

   .. rubric:: mingoodfrac

   | If the fraction of unflagged data for an antenna is below this value (0. to 1.), the antenna is flagged.

.. _usefieldtab:

   .. rubric:: usefieldtab

   | derive the antenna AZ/EL values from the FIELD rather than the POINTING table

.. _refant:

   .. rubric:: refant

   | use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)

.. _offsetstable:

   .. rubric:: offsetstable

   | (experimental) subtract the temperature offsets in this table from the WVR measurements before calculating the phase corrections


    """
    pass
