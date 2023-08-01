.. include:: <isogrk1.txt>

.. _Description:

Description

  This task retrieves calibrator information via telescope-specific web services
  and writes this information as a component list so that it may be used by applications
  downstream.

  The task currently supports only the VLA (since it is the only telescope that has
  such a web service). One of either a calibrator name or direction may be specified.
  The names '3C48', '3C138', '3C147', and '3C286' are supported. A direction is specified
  as 'FRAME LONGITUDE LATITUDE', so for example 'J2000 01:37:41.1 33.09.32' for 3C48. 
  Latitude and longitude may be specified in their familiar sexigesimal forms, or as
  angular quantities which must include units (eg '33.15deg'). If a direction is specified,
  the web service will attempt to find a supported calibrator near that position. If one
  cannot be found, an exception will be thrown.

  The observing band must be specified. For the VLA, supported bands are 'P'. 'L', 'S',
  'C', 'X', 'U', 'K', 'A', and 'Q'.

  The observation date as an MJD must be specified. Specifying an MJD before or around 1980
  will result in an exception being thrown as there are no data for such dates.

  A reference date as an MJD may be specified. It allows older versions of the data
  and/or algorithms should be retrieved, thus allowing historical reproducibility even
  after data and algorithms may have been updated. This input represents the latest date
  for which versioned data and algorithms should be used.

  If successful, the task will write a component list generated from the data returned
  by the web service which represents the brightness distribution for the specified 
  calibrator for the specified band at the specified date (with the reference date applied
  if one is specified). This component list, being a CASA table, will have the table
  keyword 'web_service'. The value of this keyword is a dictionary containing the inputs
  specified in the task, the response of the web service (usually a very long JSON string),
  the URL that was used to make the query, and other possibly useful metadata.  

.. _Examples:

Examples
   .. code-block:: python
        # get the intensity distribution of 3C48 at Q band on MJD 55000
        calmode(
            outfile='3C48.cl', source='3C48', band='Q', obsdate=55000,
            hosts=['http://some-host-that-works.nrao.edu']
        )   

        # the same thing, but do not use any data or algorithms that were
        # created after MJD 56000
        calmode(
            outfile='3C48.cl', source='3C48', band='Q', obsdate=55000,
            refdate=56000, hosts=['http://some-host-that-works.nrao.edu']
        )   

        # get the same information as the first query based on 3C48's direction,
        # not its name
        calmode(
            outfile='3C48.cl', direction='J2000 01h37m41.1s 33.155deg', band='Q',
            obsdate=55000, hosts=['http://some-host-that-works.nrao.edu']
        )   



.. _Development:

Development

 

