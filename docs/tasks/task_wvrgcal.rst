
.. _Description:

Description
   Information about the observation and the performance of **wvrgcal** is written to the CASA logger and also returned in a
   dictionary. The dictionary element 'success' is True if no errors occured. Of particular note is the discrepancy statistic
   (Disc), where high values (> a few hundred microns) may indicate some levels of cloud contamination and the effect of
   applying the **wvrgcal** correction should be checked; values > 1000 :math:`\mu` m in all antennas have currently been
   found to indicate that **wvrgcal** correction should not be used.

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
   

.. _Examples:

Examples
   Usage ::

      wvrgcal(vis='uid___A002_X1d54a1_X5.ms',
      caltable='cal-wvr-uid___A002_X1d54a1_X5.W',toffset=-1,
      segsource=True, tie=['Titan,1037-295,NGC3256'],
      statsource='1037-295')
   

.. _Development:

Development
   None
   