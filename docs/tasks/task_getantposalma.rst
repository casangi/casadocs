

.. _Description:

Description
This task retrieves ALMA antenna positions via a web service which runs
on an ALMA-hosted server. The antenna positions are with respect to ITRF.
The user must specify the value of the outfile parameter. This parameter
is the name of the file to which the antenna positions will be written.
This file can then be read by gencal so that it can use the most up to
date antenna positions for the observation.

The web service is described by the server development team and can be
found `at this location <https://asw.alma.cl/groups/ASW/-/packages/843>`__. 

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

tw and search are optional parameters and are coupled as follows. search
indicates the search algorithm to use to find the desired antenna positions.
Suppored values of this parameter at the time of writing are 'both_latest'
and 'both_closest'. The default algorithm used is 'both_latest'.
In general, the search is limited in time to the specified value of tw
(time wondow). However, in the case that tw is not specified, the following
rules apply. The task passes the value of the search parameter verbatim to
the web service, meaning that users can take advantage of new search algorithms
as the web service team brings them online. 

For 'both_latest',
the last updated position for each antenna within the specified time window,
or, if tw is not specified, within 30 days after the observation will be
returned, taking into account snr if specified, if provided.

For 'both_closest', if tw is not specified, the position
of each antenna closest in time to the observation, within 30 days (before
or after the observation) will be returned, subject to the value of snr if it
is specified. 

hosts is a required parameter. It is a list of hosts to query, in order of
priority, to obtain positions. The first server to respond with a valid result is
the only one that is used. That response will be written and no additional
hosts will be queried.


.. _Examples:

Examples
   Get antenna positions which have positions with a signal-to-noise ratio
   greater than 5.
   
   ::
   
      getantposalma(
          outfile='my_ant_pos.json', asdm='valid ASDM name here', snr=5,
          hosts=['tbd1.alma.cl', 'tbd2.alma.cl']
     )
   

.. _Development:

Development
   No additional development details


