#
# stub function definition file for docstring parsing
#

def wvrgcal(vis, caltable='', toffset=0, segsource=True, sourceflag=[''], tie=[''], nsol=1, disperse=False, wvrflag=[''], statfield='', statsource='', smooth='', scale=1., spw=[''], wvrspw=[''], reversespw='', cont=False, maxdistm=500., minnumants=2, mingoodfrac=0.8, usefieldtab=False, refant=[''], offsetstable=''):
    """
Generate a gain table based on Water Vapour Radiometer data

| Information about the observation and the performance of WVRGCAL is written to the CASA logger
|and also returned in a dictionary; see the CASA cookbook for a more detailed description of these parameters.
|The dictionary element 'success' is True if no errors occured.
|
|Of particular note is the discrepancy parameter (Disc): high values (> a few hundred microns) 
|may indicate some levels of cloud contamination and the effect of applying the WVRGCAL correction 
|should be checked; values > 1000 um in all antennas have currently been found to indicate that 
|WVRGCAL correction should not be used.
|
|      
|  vis -- Name of input visibility file
|              default: none; example: vis='ngc5921.ms'
|
|  caltable -- Name of output gain calibration table
|              default: none; example: caltable='ngc5921.wvr'
|
|  toffset -- Time offset (sec) between interferometric and WVR data
|             default: 0 (ALMA default for cycle 1, for cycle 0, i.e. up to Jan 2013 it was -1)
|
|  segsource -- Do a new coefficient calculation for each source
|               default: True
|
|  tie -- Prioritise tieing the phase of these sources as well as possible
|         (requires segsource=True)
|         default: [] example: ['3C273,NGC253', 'IC433,3C279']
|
|  sourceflag -- Flag the WVR data for these source(s) as bad and do not produce corrections for it
|               (requires segsource=True)
|               default: [] (none) example: ['3C273']
|
|  nsol -- Number of solutions for phase correction coefficients during this observation.
|          By default only one set of coefficients is generated for the entire observation. 
|          If more sets are requested, then they will be evenly distributed in time throughout 
|          the observation. Values > 1 require segsource=False.
|          default: 1
|
|  disperse -- Apply correction for dispersion
|             default: False
|
|  wvrflag -- Regard the WVR data for these antenna(s) as bad and use interpolated values instead
|             default: [] (none) example: ['DV03','DA05','PM02']           
|
|  statfield -- Compute the statistics (Phase RMS, Disc) on this field only
|               default: '' (all) 
|
|  statsource -- Compute the statistics (Phase RMS, Disc) on this source only
|                default: '' (all)             
|
|  smooth -- Smooth the calibration solution on the given timescale 
|            default: '' (no smoothing), example: '3s' smooth on a timescale of 3 seconds
|
|  scale -- Scale the entire phase correction by this factor
|           default: 1. (no scaling)
|
|  spw -- List of the spectral window IDs for which solutions should be saved into the caltable
|           default: [] (all spectral windows), example [17,19,21,23]
|
|  wvrspw -- List of the spectral window IDs from which the WVR data should be taken
|           default: [] (all WVR spectral windows), example [0]
|
|  reversespw -- Reverse the sign of the correction for the listed SPWs
|                (only neede for early ALMA data before Cycle 0)
|                default: '' (none), example: reversespw='0~2,4'; spectral windows 0,1,2,4
|
|  cont -- Estimate the continuum (e.g., due to clouds)
|          default: False
|
|  maxdistm -- maximum distance (m) an antenna may have to be considered for being part
|              of the antenna set (minnumants to 3 antennas) for the interpolation of a solution 
|              for a flagged antenna
|              default: 500.
|
|  minnumants -- minimum number of near antennas required for interpolation
|                default: 2
|
|  mingoodfrac -- If the fraction of unflagged data for an antenna is below this value (0. to 1.), 
|                 the antenna is flagged.
|                 default: 0.8
|
|  usefieldtab -- derive the antenna AZ/EL values from the FIELD rather than the POINTING table
|                 default: False
|
|  refant -- use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)
|                default: '' (use the first good or interpolatable antenna), 
|                examples: 'DA45' - use DA45 
|                          ['DA45','DV51'] - use DA45 and if that is not good, use DV51 instead
|
|  offsetstable -- (experimental) subtract the temperature offsets in this table from the WVR measurements before
|             using them to calculate the phase corrections
|                default: '' (do not apply any offsets)
|                examples: 'uid___A002_Xabd867_X2277.cloud_offsets' use the given table

Parameters
----------
vis : string
   
caltable : string
   
toffset : double
   
segsource : bool
   
disperse : bool
   
wvrflag : stringArray
   
statfield : string
   
statsource : string
   
smooth : string
   
scale : double
   
spw : intArray
   
wvrspw : intArray
   
reversespw : string
   
cont : bool
   
maxdistm : double
   
minnumants : int
   
mingoodfrac : double
   
usefieldtab : bool
   
refant : stringArray
   
offsetstable : string
   

Other Parameters
----------
sourceflag : stringArray
   
tie : stringArray
   
nsol : int
   

Notes
-----





   



      .. rubric:: Summary
         :name: summary

      | Information about the observation and the performance of
        **wvrgcal** is written to the CASA logger and also returned in a
        dictionary; see the `Water Vapor Radiometer Gain
        Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration/water-vapor-radiometer-gain-calibration-wvrgcal>`__ chapter
        in `Synthesis
        Calibration <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/synthesis-calibration>`__ for
        a more detailed description of these parameters. The dictionary
        element 'success' is True if no errors occured.
      | Of particular note is the discrepancy statistic (Disc): high
        values (> a few hundred microns) may indicate some levels of
        cloud contamination and the effect of applying the **wvrgcal**
        correction should be checked; values > 1000 :math:`\mu` m in
        all antennas have currently been found to indicate that
        **wvrgcal** correction should not be used.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *vis*
         :name: vis

      Name of input visibility file. Default: none. Examples:
      *vis='ngc5921.ms'*

      .. rubric:: *caltable*
         :name: caltable

      Name of output gain calibration table. Default: none. Examples:
      *caltable='ngc5921.wvr'*

      .. rubric:: *toffset*
         :name: toffset

      Time offset (sec) between interferometric and WVR data. Default: 0
      (ALMA default for cycle 1, for cycle 0, i.e. up to Jan 2013 it was
      -1)

      .. rubric:: *segsource*
         :name: segsource

      Do a new coefficient calculation for each source. Default: True

      .. rubric:: *tie*
         :name: tie

      Prioritise tieing the phase of these sources as well as possible
      (requires *segsource=True*). Default: [ ]. Examples:
      *tie=['3C273,NGC253', 'IC433,3C279']*

      .. rubric:: *sourceflag*
         :name: sourceflag

      Flag the WVR data for these source(s) as bad and do not produce
      corrections for it (requires *segsource=True*). Default: [ ].
      Examples: *sourceflag=['3C273']*

      .. rubric:: *nsol*
         :name: nsol

      Number of solutions for phase correction coefficients during this
      observation. By default only one set of coefficients is generated
      for the entire observation. If more sets are requested, then they
      will be evenly distributed in time throughout the observation.
      Values > 1 require *segsource=False*. Default: 1

      .. rubric:: *disperse*
         :name: disperse

      Apply correction for dispersion. Default: False

      .. rubric:: *wvrflag*
         :name: wvrflag

      Regard the WVR data for these antenna(s) as bad and use
      interpolated values instead. Default: [ ]. Examples:
      *wvrflag=['DV03','DA05','PM02']*

      .. rubric:: *statfield*
         :name: statfield

      Compute the statistics (Phase RMS, Disc) on this field only.
      Default: '' (all)

      .. rubric:: *statsource*
         :name: statsource

      Compute the statistics (Phase RMS, Disc) on this source only.
      Default: '' (all)

      .. rubric:: *smooth*
         :name: smooth

      Smooth the calibration solution on the given timescale. Default:
      '' (no smoothing). Examples: *smooth='3s'* smooth on a timescale
      of 3 seconds.

      .. rubric:: *scale*
         :name: scale

      Scale the entire phase correction by this factor. Default: 1. (no
      scaling)

      .. rubric:: *spw*
         :name: spw

      List of the spectral window IDs for which solutions should be
      saved into the caltable. Default: [ ] (all spectral windows).
      Examples: *spw=[17,19,21,23]*

      .. rubric:: *wvrspw*
         :name: wvrspw

      List of the spectral window IDs from which the WVR data should be
      taken. Default: [ ] (all WVR spectral windows). Examples:
      *wvrspw=[0]*

      .. rubric:: *reversespw*
         :name: reversespw

      Reverse the sign of the correction for the listed SPWs (only neede
      for early ALMA data before Cycle 0). Default: '' (none). Examples:
      *reversespw='0~2,4'*; spectral windows 0,1,2,4

      .. rubric:: *cont*
         :name: cont

      Estimate the continuum (e.g., due to clouds). Default: False

      .. rubric:: *maxdistm*
         :name: maxdistm

      Maximum distance (m) an antenna may have to be considered for
      being part of the antenna set (minnumants to 3 antennas) for the
      interpolation of a solution for a flagged antenna. Default: 500.

      .. rubric:: *minnumants*
         :name: minnumants

      Minimum number of near antennas required for interpolation.
      Default: 2

      .. rubric:: *mingoodfrac*
         :name: mingoodfrac

      If the fraction of unflagged data for an antenna is below this
      value (0.0 to 1.0), the antenna is flagged. Default: 0.8

      .. rubric:: *usefieldtab*
         :name: usefieldtab

      Derive the antenna AZ/EL values from the FIELD rather than the
      POINTING table. Default: False

      .. rubric:: *refant*
         :name: refant

      Use the WVR data from this antenna for calculating the dT/dL
      parameters (can give ranked list). Default: '' (use the first good
      or interpolatable antenna), Examples: *refant='DA45'* - use DA45;
      *refant=['DA45','DV51']* - use DA45 and if that is not good, use
      DV51 instead.

      .. rubric:: *offsetstable*
         :name: offsetstable

      Subtract the temperature offsets in this table from the WVR
      measurements before using them to calculate the phase corrections
      (experimental). Default: '' (do not apply any offsets). Examples:
      *offsetstable='uid___A002_Xabd867_X2277.cloud_offsets'* use the
      given table.

    """
    pass
