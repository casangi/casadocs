

.. _Description:

Description
Antpos retrieves ALMA antenna positions via a web service which runs on an
ALMA-hosted server. The antenna positions are with respect to ITRF. The
user must specify the value of the outfile parameter. This parameter is
the name of the file to which the antenna positions will be written. This
file can then be read by gencal so that it can use the most up to date
antenna positions for the observation.

The input parameters are discussed in detail below.

outfile is required to be specified. It is the name of the file to which to
write antenna positions. If a file with the same name exists it will be
silently overwritten.

asdm is required to be specified. It is the associated ASDM name.
tw is an optional parameter. It is time window in which the antenna positions
are required, specified as a comma separated pair. Times are UTC and are
expressed in YY-MM-DDThh:mm:ss.sss format. The end time must be later than
the begin time.

snr is an optional parameter. It is the signal-to-noise ratio. Antenna
positions which have corrections less than this value will not be written.
If not specified, positions of all antennas will be written.

search is an optional parameter, It is the search algorithm to use.
Supported values are 'both_latest' and 'both_closest'. For 'both_latest',
the last updated position for each antenna within 30 days after the
observation will be returned, taking into account snr if specified. If provided,

tw will override the 30 day default value. For 'both_closest', the position
of each antenna closest in time to the observation, within 30 days (before
or after the observation will be returned, subject to the value of snr if it
is specified. If specified, the value of tw will override the default 30 days.
The default algorithm used is 'both_latest'.

servers is a required parameter. It is a list of servers to query, in order of
priority, to obtain positions. The first server to respond with a valid result is
the only one that is used. That response will be written and no additional
servers will be queried.


.. _Examples:

Examples
   Get antenna positions which have positions with a signal-to-noise ratio
   greater than 5.
   
   ::
   
      antpos(
          outfile='my_ant_pos.json', asdm='valid ASDM name here', snr=5,
          servers=['tbd1.alma.cl', 'tbd2.alma.cl']
     )
   

.. _Development:

Development
   No additional development details


