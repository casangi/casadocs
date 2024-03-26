fixplanets -- Changes FIELD and SOURCE table entries based on user-provided direction or POINTING table, optionally fixes the UVW coordinates -- editing, maninpulation, calibration task
=======================================

Description
---------------------------------------

    This task's main purpose is to correct observations which were performed
    with correct pointing and correlation but for which incorrect direction
    information was entered in the FIELD and SOURCE table of the MS.
    If you actually want to change the phase center of the visibilties in an MS,
    you should use task fixvis.

    Input Parameters
    vis        -- Name of the input visibility set

    field      -- field selection string

    fixuvw     -- recalc uvw coordinates? (default: False)

    direction  -- if set, don't use pointing table but set direction to this value.
                  The direction can either be given explicitly or as the path
                  to a JPL Horizons ephemeris (for an example of the format,
                  see directory data/ephemerides/JPL-Horizons/).
                  Alternatively, the ephemeris table can also be provided as mime format file,
                  i.e. a saved email as obtained via the commands (for example):
                  import recipes.ephemerides.request as jplreq
                  jplreq.request_from_JPL(objnam='Mars',startdate='2012-01-01',enddate='2013-12-31',
                       date_incr='0.1 d', get_axis_orientation=False, get_axis_ang_orientation=True,
                       get_sub_long=True, use_apparent=False, get_sep=False,
                       return_address='YOUR_EMAIL_ADDESS', mailserver='YOUR_MAIL_SERVER_ADDRESS')
                  Note: some mail clients may not save the JPL mail properly.
                        Confirmed to work is Thunderbird.

                  default= '' (use pointing table)

                  example: 'J2000 19h30m00 -40d00m00'

    refant     -- if using pointing table information, use it from this antenna
                  default: 0 (antenna id 0)
                  examples: 'DV06' (antenna with name DV06)
                            3 (antenna id 3)
    reftime    -- if using pointing table information, use it from this timestamp
                  default: 'first'
                  examples: 'median' will use the median timestamp for the given field
		            using only the unflagged maintable rows
                            '2012/07/11/08:41:32' will use the given timestamp (must be
                            within the observaton time)



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
   * - field
     - :code:`[ ]`
     - 
   * - fixuvw
     - :code:`False`
     - 
   * - direction
     - :code:`''`
     - 
   * - refant
     - :code:`[ ]`
     - 
   * - reftime
     - :code:`'first'`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of the input visibility set.


field
---------------------------------------

:code:`[ ]`

Fields to operate on.  Blank = all.


fixuvw
---------------------------------------

:code:`False`

Recalculate Fourier-plane u,v,w coordinates


direction
---------------------------------------

:code:`''`

if set, do not use pointing table but set direction to this value


refant
---------------------------------------

:code:`[ ]`

if using pointing table information, use it from this antenna


reftime
---------------------------------------

:code:`'first'`

if using pointing table information, use it from this timestamp 




