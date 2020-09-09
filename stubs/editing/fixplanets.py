#
# stub function definition file for docstring parsing
#

def fixplanets(vis, field='""', fixuvw=False, direction='', refant='0', reftime='first'):
    r"""
Changes FIELD and SOURCE table entries based on user-provided direction or POINTING table, optionally fixes the UVW coordinates

Parameters
   - vis_ (string) - Name of input visibility file
   - field_ (variant='""') - Select field using field id(s) or field name(s)
   - fixuvw_ (bool=False) - Recalculate Fourier-plane u,v,w coordinates
   - direction_ (variant='') - If set, do not use pointing table but set direction to this value
   - refant_ (variant='0') - Reference antenna name(s)
   - reftime_ (string='first') - If using pointing table information, use it from this timestamp


Description
   The main purpose of this task is to correct observations which
   were performed with correct pointing and correlation but for which
   incorrect direction information was entered in the FIELD and
   SOURCE table of the MS.This may be the case if the data is old
   andthere is no ephemeris table attached to the MS (in which case,
   use**fixplanets** with the parameter *direction* set in order to
   attach one), if improved ephemerides have become available, or
   ifa fixed direction is needed to allow concatenation (using
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

   Alternatively, for most sources, the ephemerisfile can also be
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

   In cases where the source isnot included in
   recipes.ephemerides.request, use the following set of commands to
   get the file in mime format for all sources:

   -  go to the `JPL ephemerides
      webpage <http://ssd.jpl.nasa.gov/horizons.cgi>`__
   -  changethe target body entry to the desired object
   -  click on 'batch-file' data in the special options section
   -  retrieve the command parameter, which is the 'code' for the
      object (i.e., DES=C/2011 L4')
   -  send an email tohorizons@ssd.jpl.nasa.gov, with JOB as
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


.. _vis:

vis (string)
   | Name of input visibility file
   |                      Default: none
   | 
   |                         Example: vis='ngc5921.ms'

.. _field:

field (variant='""')
   | Select field using field id(s) or field name(s)
   |                      Default: '' (all fields)
   |                      
   |                      Use 'go listobs' to obtain the list id's or
   |                      names. If field string is a non-negative integer,
   |                      it is assumed a field index,  otherwise, it is
   |                      assumed a field name.
   | 
   |                         Examples:
   |                         field='0~2'; field ids 0,1,2
   |                         field='0,4,5~7'; field ids 0,4,5,6,7
   |                         field='3C286,3C295'; field named 3C286 and
   |                         3C295
   |                         field = '3,4C*'; field id 3, all names
   |                         starting with 4C

.. _fixuvw:

fixuvw (bool=False)
   | Recalculate Fourier-plane u,v,w coordinates?
   |                      Default: False
   |                      Options: False|True

.. _direction:

direction (variant='')
   | If set, do not use pointing table but set direction to
   | this value
   |                      Default: '' (use pointing table)
   | 
   |                         Example: 'J2000 19h30m00 -40d00m00'
   | 
   |                      The direction can either be given explicitly or
   |                      as the path to a JPL Horizons
   |                      ephemeris. Alternatively, the ephemeris table can
   |                      also be provided as mime format file. For more
   |                      information, see the task pages of fixplanets in
   |                      CASA Docs (https://casa.nrao.edu/casadocs/).

.. _refant:

refant (variant='0')
   | Reference antenna name(s); a prioritized list may be
   | specified
   |                      Default: 0 (antenna ID 0)
   | 
   |                         Examples: 
   |                         refant='4' (antenna with index 4)
   |                         refant='VA04' (VLA antenna #4)
   |                         refant='EA02,EA23,EA13' (EVLA antenna EA02,
   |                         use EA23 and EA13 as alternates if/when EA02
   |                         drops out)
   | 
   |                      Use taskname=listobs for antenna listing

.. _reftime:

reftime (string='first')
   | If using pointing table information, use it from this
   | timestamp
   |                      Default: 'first'
   | 
   |                         Examples: 
   |                         * 'median' will use the median timestamp for
   |                           the given field using only the unflagged
   |                           maintable rows
   |                         * '2012/07/11/08:41:32' will use the given
   |                           timestamp (must be within the observaton
   |                           time)


    """
    pass
