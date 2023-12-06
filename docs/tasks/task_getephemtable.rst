.. _Description:

Description
   This task retrieves the ephemeris data of a specific ephemeris object by sending a query to JPL's Horizons system and creates the ephemeris data stored in a CASA table format.

This task is intended to be used as a standalone function for a user who needs to use 
an updated ephemeris data in CASA table format for data processing such as imaging. More informiaton on how one can use the CASA epehemeris table generated with this task is available in `Manipulate Ephemeris Ojbect <../../notebooks/ephemeris_data.ipynb#Manipulate-Ephemeris-Objects>`__ section.


The task calls a query driver function, get_horizonsephem, which does input object name checking to translate into the NAIF ID before calling query_horizons. The query_horizons does an actual query to the database. The query results in json is further converted to a CASA table by get_horizonsephem.

The query code is based on the JPL-Horizons API ver.1.2 (https://ssd.jpl.nasa.gov/api/horizons.api). The JPL-Horizons System provides a large number of the query parameters and we only use a subset of them. The following are the list of the parameters that is used by query_horizons function. For detailed descriptions of the parameters, please refer to the JPL-Horizons documentation (https://ssd-api.jpl.nasa.gov/doc/horizons.html). The italic parameters represent user-defined values. Some of the requested quantities are specifically used for setjy task and for other use cases may not be needed. But the fixed quantity selection is used for uniformity within CASA for generated ephemeris tables.
The query parameters used in this task are the following.

- format json
- EPHEM_TYPE OBSERVER
- OBJ_DATA YES
- COMMAND *Objectname*
- START_TIME *Start time*
- STOP_TIME *Stop time*
- STEP_SIZE *Step size*
- CENTER 500\@399 (= geocentric)
- ANG_FORMAT DEG
- QUANTITIES 1,14,15,17,19,20,24
    1. Astrometric RA, Dec,
    14. Observer sub-longitude & sub-latitude,
    15. Sun sub-longitude & sub-latitude,
    17. North pole PA and distance from disc center,
    19. Heliocentric range and range rate,
    20. Observer range and range rate,
    24. Sun-Target-Observer phase angle

asis 
  By setting asis=False, the task checks objectname for the known object names in CASA and if it matches, it converts to an object ID before sending a query to the JPL-Horizons system. The known objects are a list of the supported ephemeris objects in the setjy task plus a few others as listed below.  

  Sun, Mercury, Venus, Moon, Mars, Jupiter, Io, Europa, Ganymede, Callisto, Saturn, Titan, Uranus, Neptune, Pluto, Ceres, Pallas, Juno, Vesta, and Lutetia. 
  By setting asis=True, objectname will be unmodified before sending the query.

timerange
  For a small time interval (e.g. interval='1min'), specifying timernage by the calendar date and time is recommanded rather than using MJD, which may lead to precision error in converting to the calendar dates and times in the returned ephemeris data from the JPL-Horizons system. 

rawdatafile
  This parameter is useful to set whenever errors occur in the query result content and in consequence, CASA ephemeris table is not generated. While some of the common errors during query are parsed to the logger, the full description of the issues in the query that are reported by the JPL-Horizons system can be found in the raw query data file.

.. _Examples:

Examples
   Get Titan's ephemeris data from September 01, 2023 (20UT) to September 04, 2023 (20UT)
   with time interval of 1 hour

   ::
   
      getephemtable(objectname='Titan', timerange='2023/09/01/20:00~2023/09/04/20:00', interval='1h', outfile='Titan_20230901_20230904ephem.tab')
   
   Same as above but specifying timerange in JD,

   ::

      getephemtable(objectname='Titan', timerange='JD 2460189.416667~2460192.333333', interval='1h', outfile='Titan_20230901_20230904ephem.tab')

   Or in MJD with interval of 5 minutes,

   ::

      getephemtable(objectname='Titan', timerange='MJD 60188.916667~60191.833333', interval='5m', outfile='Titan_20230901_20230904ephem.tab')


   Same as above but also save the raw query results,

   ::

     getephemtable(objectname='Titan', timerange='MJD 60188.916667~60191.833333', interval='5m', outfile='Titan_20230901_20230904ephem.tab', rawdatafile='Titan_raw_query_results.txt')

   Get Comet Nishimura, C/2023 P1 data with 5 min interval (interval parameter is omitted since 5 minutes is default), 

   ::

      getephemtable(objectname='C/2023 P1', asis=True, timerange='MJD 60188.916667~60191.833333', outfile='CometNishimura_20230901_20230904ephem.tab'


.. _Development:

Development
   No additional development details
   
