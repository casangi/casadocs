

.. _Description:

Description
   task fixplanets description
   
   The main purpose of this task is to correct observations which
   were performed with correct pointing and correlation but for which
   incorrect direction information was entered in the FIELD and
   SOURCE table of the MS. This may be the case if the data is old
   and there is no ephemeris table attached to the MS (in which case,
   use **fixplanets** with the parameter *direction* set in order to
   attach one), if improved ephemerides have become available, or
   if a fixed direction is needed to allow concatenation (using
   **fixplanets** as an alternative to **concat**).
   
   If you actually want to change the phase center of the visibilties
   in an MS, you should use task **fixvis**.
   
    
   
   .. rubric:: Parameter descriptions
      
   
   .. rubric:: *vis*
      
   
   Name of the input visibility set.
   
   .. rubric:: *field*
      
   
   Field selection string.
   
   .. rubric:: *fixuvw*
      
   
   Recalculates the uvw coordinates (default: False).
   
   .. rubric:: *direction*
      
   
   If set, **fixplanets** doesn't use the pointing table but sets the
   direction to this value.
   
   default= '' (use pointing table); example: 'J2000 19h30m00
   -40d00m00'.
   
   The direction can either be given explicitly or as the path to a
   JPL Horizons ephemeris text file (for an example of the format,
   see directory data/ephemerides/JPL-Horizons/).
   
   Alternatively, for most sources, the ephemeris file can also be
   provided as mime format file, i.e., a saved email as obtained via
   the following commands:
   
   ::
   
      | import recipes.ephemerides.request as jplreq
      | jplreq.request_from_JPL(objnam='Mars',
        startdate='2012-01-01', enddate='2013-12-31', date_incr='0.1
        d', get_axis_orientation=False, 
        get_axis_ang_orientation=True, get_sub_long=True,
        use_apparent=False, get_sep=False,
        return_address='YOUR_EMAIL_ADDESS', 
        mailserver='YOUR_MAIL_SERVER_ADDRESS')
   
   .. note:: **NOTE**: Some mail clients may not save the JPL mail properly.
      Confirmed to work in Thunderbird.
   
   In cases where the source is not included in
   recipes.ephemerides.request, use the following set of commands to
   get the file in mime format for all sources:
   
   -  go to the `JPL ephemerides
      webpage <http://ssd.jpl.nasa.gov/horizons.cgi>`__ 
   -  change the target body entry to the desired object
   -  click on 'batch-file' data in the special options section
   -  retrieve the command parameter, which is the 'code' for the
      object (i.e., DES=C/2011 L4')
   -  send an email to horizons@ssd.jpl.nasa.gov, with JOB as
      subject, and in the body:
   
   ::
   
      !$$SOF
   
      COMMAND= 'DES=C/2011 L4'
   
      CENTER= '500@399'
   
      MAKE_EPHEM= 'YES'
   
      TABLE_TYPE= 'OBSERVER'
   
      START_TIME= '2014-06-28'
   
      STOP_TIME= '2014-07-01'
   
      STEP_SIZE= '1 m'
   
      CAL_FORMAT= 'CAL'
   
      TIME_DIGITS= 'MINUTES'
   
      ANG_FORMAT= 'DEG'
   
      OUT_UNITS= 'KM-S'
   
      RANGE_UNITS= 'AU'
   
      APPARENT= 'AIRLESS'
   
      SOLAR_ELONG= '0,180'
   
      SUPPRESS_RANGE_RATE= 'NO'
   
      SKIP_DAYLT= 'NO'
   
      EXTRA_PREC= 'NO'
   
      R_T_S_ONLY= 'NO'
   
      REF_SYSTEM= 'J2000'
   
      CSV_FORMAT= 'NO'
   
      OBJ_DATA= 'YES'
   
      EMAIL_ADDR = 'amoullet@nrao.edu'
   
      QUANTITIES= '1,17,19,20,24,14,15'
   
      !$$EOF
   
   where COMMAND, START_TIME, STOP_TIME, STEP_SIZE and EMAIL_ADDR
   must be adapted to the case. See the Examples tab for how to use
   the returned ephemeris. 
   
   .. rubric:: *refant*
      
   
   If using pointing table information, use it from this antenna.
   default: 0 (antenna id 0); examples: 'DV06' (antenna with name
   DV06); 3 (antenna id 3).
   
   .. rubric:: *reftime*
      
   
   If using pointing table information, use it from this timestamp.
   default: 'first'; examples: 'median' will use the median timestamp
   for the given field using only the unflagged maintable rows;
   '2012/07/11/08:41:32' will use the given timestamp (must be within
   the observaton time).
   

.. _Examples:

Examples
   task examples
   
   To look up the pointing direction from antenna 0 for field 'Titan'
   in the POINTING table based on the first timestamp in the main
   table rows for this field, write this direction in the FIELD and
   SOURCE tables, and then recalculate the UVW coordinates for this
   field:
   
   ::
   
      fixplanets(vis='uid___A002_X1c6e54_X223.ms', field='Titan',
      fixuvw=True)
   
   To attach the ephemeris table 'Titan_55438-56292dUTC.tab' to field
   'Titan' and then recalculate the UVW coordinates for this field:
   
   ::
   
      fixplanets(vis='uid___A002_X1c6e54_X223.ms', field='Titan',
      fixuvw=True, direction='Titan_55438-56292dUTC.tab')
   
   To set the directions for field 'Titan' in the FIELD and SOURCE
   table to the given direction and not recalculate the UVW
   coordinates; this can be useful for several purposes, among them
   preparing a concatenation of datasets. (Only fields with the same
   direction will be recognised as identical.):
   
   ::
   
      fixplanets(vis='uid___A002_X1c6e54_X223.ms', field='Titan',
      fixuvw=False, direction='J2000 12h30m15 -02d12m00')
   
   To use an ephemeris file returned from JPL via the email query
   described in the Description tab in the case where the source is
   unavailable via recipes.ephemerides.request, first copy the entire
   email received from JPL into a file with a .eph extension (for
   example, "target.eph"), and then attach the ephemeris using
   **fixplanets**: 
   
   ::
   
      fixplanets(vis='uid___A002_X1c6e54_X223.ms', fixuvw=True,
      direction='target.eph')
   

.. _Development:

Development
   task developer
   
   --CASA Developer--
   
   