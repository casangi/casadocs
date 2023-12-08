.. _Description:

Description

  This task retrieves VLA-specific calibrator information via a web service
  and writes this information as a component list so that it may be used by applications
  downstream.

  One of either a calibrator name or direction may be specified.
  The names '3C48', '3C138', '3C147', and '3C286' are currently supported by the web
  service. A direction is specified as 'FRAME LONGITUDE LATITUDE', so for example
  "J2000 01:37:41.1 33.09.32" for 3C48. Latitude and longitude may be specified in
  their familiar sexigesimal forms, or as angular quantities which must include
  units (eg '33.15deg'). If a direction is specified, the web service will attempt to
  find a supported calibrator near (as defined by the web service) that position. If
  one cannot be found, the web server will return an error code and the task will
  throw an exception.

  The observing band must be specified. For the VLA, supported bands are 'P'. 'L', 'S',
  'C', 'X', 'U', 'K', 'A', and 'Q'.

  The observation date must be specified as either an MJD (assumed if the value is a number)
  or a date of the form "YYYY-MM-DD" (assumed if the value is specified as a string).

  A reference date may be specified. If so, the specification rules for the observation
  date also hold for this parameter, Specifying this parameter allows older versions of the data
  and/or algorithms to be retrieved, thus allowing historical reproducibility even
  after data and algorithms may have been updated. This input represents the latest date
  for which versioned data and algorithms should be used.

  If successful, the task will write a component list generated from the data returned
  by the web service which represents the brightness distribution for the specified 
  calibrator for the specified band at the specified date (with the reference date applied
  if one is specified). This component list, being a CASA table, will include the table
  keyword "web_service". The value of this keyword will be a dictionary containing the inputs
  specified in the task, the response of the web service (usually a very long JSON string),
  the URL that was used to make the query, and other possibly useful metadata.  


.. _Examples:

Examples
   
    ::

       # get the intensity distribution of 3C48 at Q band on MJD 55000
       calmodevla(
           outfile='3C48.cl', source='3C48', band='Q', obsdate=55000,
           hosts=['http://some-host-that-works.nrao.edu']
       )   

       # the same thing, but do not use any data or algorithms that were
       # created after MJD 56000
       calmodevla(
           outfile='3C48.cl', source='3C48', band='Q', obsdate=55000,
           refdate=56000, hosts=['http://some-host-that-works.nrao.edu']
       )   

       # get the same information as the first query based on 3C48's direction,
       # not its name
       calmodevla(
           outfile='3C48.cl', direction='J2000 01h37m41.1s 33.155deg', band='Q',
           obsdate=55000, hosts=['http://some-host-that-works.nrao.edu']
       )   



.. _Development:

Development

 

