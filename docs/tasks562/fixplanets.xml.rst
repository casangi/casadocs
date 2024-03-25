fixplanets -- Changes FIELD and SOURCE table entries based on user-provided direction or POINTING table, optionally fixes the UVW coordinates -- editing, maninpulation, calibration task
=======================================

Description
---------------------------------------

This task's main purpose is to correct observations which were
performed with correct pointing and correlation but for which
incorrect direction information was entered in the FIELD and SOURCE
table of the MS. If you actually want to change the phase center of
the visibilties in an MS, you should use task fixvis.



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
     - Name of input visibility file
   * - field
     - :code:`[ ]`
     - Select field using field id(s) or field name(s)
   * - fixuvw
     - :code:`False`
     - Recalculate Fourier-plane u,v,w coordinates
   * - direction
     - :code:`''`
     - If set, do not use pointing table but set direction to this value
   * - refant
     - :code:`int(0)`
     - Reference antenna name(s)
   * - reftime
     - :code:`'first'`
     - If using pointing table information, use it from this timestamp


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'



field
---------------------------------------

:code:`[ ]`

Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative integer,
                     it is assumed a field index,  otherwise, it is
                     assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C



fixuvw
---------------------------------------

:code:`False`

Recalculate Fourier-plane u,v,w coordinates?
                     Default: False
                     Options: False|True



direction
---------------------------------------

:code:`''`

If set, do not use pointing table but set direction to
this value
                     Default: '' (use pointing table)

                        Example: 'J2000 19h30m00 -40d00m00'

                     The direction can either be given explicitly or
                     as the path to a JPL Horizons
                     ephemeris. Alternatively, the ephemeris table can
                     also be provided as mime format file. For more
                     information, see the task pages of fixplanets in
                     CASA Docs (https://casa.nrao.edu/casadocs/).



refant
---------------------------------------

:code:`int(0)`

Reference antenna name(s); a prioritized list may be
specified
                     Default: 0 (antenna ID 0)

                        Examples: 
                        refant='4' (antenna with index 4)
                        refant='VA04' (VLA antenna #4)
                        refant='EA02,EA23,EA13' (EVLA antenna EA02,
                        use EA23 and EA13 as alternates if/when EA02
                        drops out)

                     Use taskname=listobs for antenna listing



reftime
---------------------------------------

:code:`'first'`

If using pointing table information, use it from this
timestamp
                     Default: 'first'

                        Examples: 
                        * 'median' will use the median timestamp for
                          the given field using only the unflagged
                          maintable rows
                        * '2012/07/11/08:41:32' will use the given
                          timestamp (must be within the observaton
                          time)
 




