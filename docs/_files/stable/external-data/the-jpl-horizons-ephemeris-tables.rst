.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

The JPL-Horizons ephemeris tables
=================================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   This chapter describes the ephemeris tables for a selection of the
   solar system objects from JPL-Horizons database.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: plain
      :name: parent-fieldname-text

      The emphemeris data tables for the selected solar system objects
      are generated from the JPL Horizons system's on-line solar system
      data and ephemeris computation service
      (`https://ssd.jpl.nasa.gov/?horizons
      ) <https://ssd.jpl.nasa.gov/?horizons>`__. These are primarily
      used to determine flux models for the solar system objects used in
      **setjy** task.  These tables are stored as CASA tables in the 
      CASA data repository under ephemerides/JPL-Horizons. The current
      ephemeris tables cover ephemerides until December 31, 2030 for
      those objects officially supported in setjy. Available objects,
      which include major planets, satellites, and asteroids, are:
      Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Io,
      Europa, Ganymede, Callisto, Titan, Ceres, Vesta, Pallas, Juno,
      Lutetia, Sun and Moon (the objects in bold are those supported in
      'Butler-JPL-Horizons 2012' standard in setjy.).

      The format of the table name of these tables is
      objectname\ \_\ startMJD\ \_\ endMJD\ \_J2000.tab These tables
      required by setjy task are included in the data directory in the
      CASA distribution. The available tables can be listed by the
      following commands:

       

      .. container:: casa-input-box

         #In CASA6

         CASA <1>: import glob

         CASA <2>: jpldatapath=os.getenv('CASAPATH').split('
         ')[0]+'/data/ephemerides/JPL-Horizons/*J2000.tab'

         CASA <3>: glob.glob(jpldatapath)

       

      The following data are retrieved from the JPL-Horizons system (the
      nubmer in the parentheses indicates the column number listed in
      the JPL-Horizons system). One should refer
      https://ssd.jpl.nasa.gov/?horizons_doc for the detailed
      descreption of each of these quantities.

      +-------------+------------+-------------+-------------+-------------+
      | Quantities  | column no. | Unit/format | Descrition  | column      |
      |             |            |             |             | label       |
      +-------------+------------+-------------+-------------+-------------+
      | Date        | n.a.       | YYYY-MM-DD  |             | Date__      |
      |             |            | HH:MM       |             | (UT)__HR:MN |
      +-------------+------------+-------------+-------------+-------------+
      | Astrometric | 1          | degrees     | Astrometric | R.A.        |
      | RA & DEC    |            |             | RA and Dec  | _(ICRF)_DEC |
      |             |            |             | with        |             |
      |             |            |             | respect to  |             |
      |             |            |             | the         |             |
      |             |            |             | observer's  |             |
      |             |            |             | location    |             |
      |             |            |             | (GEOCETRIC) |             |
      +-------------+------------+-------------+-------------+-------------+
      | Observer    | 14         | degrees     | Apparent    | ob-lon,     |
      | sub-long&   |            |             | p           | ob-lat      |
      | sub-lat     |            |             | lanetodetic |             |
      |             |            |             | (           |             |
      |             |            |             | "geodetic") |             |
      |             |            |             | longitude   |             |
      |             |            |             | and         |             |
      |             |            |             | latitude of |             |
      |             |            |             | the center  |             |
      |             |            |             | of the      |             |
      |             |            |             | target seen |             |
      |             |            |             | by the      |             |
      |             |            |             | OBSERVER at |             |
      |             |            |             | print-time  |             |
      +-------------+------------+-------------+-------------+-------------+
      | Solar       | 15         | degrees     | Apparent    | Sl-lon,     |
      | sub-long &  |            |             | p           | Sl-lat      |
      | sub-lat     |            |             | lanetodetic |             |
      |             |            |             | (           |             |
      |             |            |             | "geodetic") |             |
      |             |            |             | longitude   |             |
      |             |            |             | and         |             |
      |             |            |             | latitude of |             |
      |             |            |             | the Sun     |             |
      |             |            |             | seen by the |             |
      |             |            |             | OBSERVER at |             |
      |             |            |             | print-time  |             |
      +-------------+------------+-------------+-------------+-------------+
      |  North Pole |  17        | degrees and |  Target's   |  NP.ang,    |
      | Pos. ang. & |            | arcseconds  | North Pole  | NP.ds       |
      | dist.       |            |             | position    |             |
      |             |            |             | angle and   |             |
      |             |            |             | angular     |             |
      |             |            |             | distance    |             |
      |             |            |             | from the    |             |
      |             |            |             | "su         |             |
      |             |            |             | b-observer" |             |
      |             |            |             | point       |             |
      +-------------+------------+-------------+-------------+-------------+
      |  Helio      |  19        |  AU, km/s   | H           |  r, rdot    |
      | range &     |            |             | eliocentric |             |
      | range rate  |            |             | range (r)   |             |
      |             |            |             | and         |             |
      |             |            |             | range-rate  |             |
      |             |            |             | (rdot)      |             |
      +-------------+------------+-------------+-------------+-------------+
      |  Observer   |  20        | AU, km/s    |  Range      |  delta,     |
      | range &     |            |             | (delta) and | dedot       |
      | range rate  |            |             | range-rate  |             |
      |             |            |             | (deldot) of |             |
      |             |            |             | the target  |             |
      |             |            |             | center with |             |
      |             |            |             | respect to  |             |
      |             |            |             | the         |             |
      |             |            |             | observer    |             |
      +-------------+------------+-------------+-------------+-------------+
      |  S-T-O      |  24        |  degrees    | Sun-Targ    |  S-T-O      |
      | angle       |            |             | et-Observer |             |
      |             |            |             | angle       |             |
      +-------------+------------+-------------+-------------+-------------+

       The script, request.py (located previously in recipes.ephemerides
      in CASA5, TBD for CASA6) can be used to retrieve the ephemeris
      data from the JPL-Horizons system via e-mail (See also `Manipulate
      Ephemeris Objects
      page <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/ephemeris-data/manipulation-of-ephemeris-objects>`__).
      Further, the saved email text file is converted to a CASA table
      format using JPLephem_reader2.

       

      .. container:: casa-input-box

         #In CASA6

         CASA <5>: from casatasks.private import JPLephem_reader2 as
         jplreader

         | CASA <6>: outdict =
           jplreader.readJPLephem('titan-jpl-horizons-ephem.eml')
         | opened the file=titan-jpl-horizons-ephem.eml

         | CASA <7>:
           jplreader.ephem_dict_to_table(outdict,'Titan_test_ephem.tab')
         | Got nrows = 3653 from MJD

      The converted table contains following columns.

      =========== =========== ==============================================
      Column name unit/format description
      MJD         day         modified Julian date
      RA          degree       atrometric right acension in ICRF/J2000 frame
      DEC         degree       astrometric declination in ICRF/J2000 frame
      Rho         AU          Geocentric distance
      RadVal      AU/d        Geocentric distance rate
      NP_ang      degree      North pole position angle
      NP_dist     degree      North pole angular distance
      DiskLong    degree      Sub-observer longitude
      DiskLat     degree      Sub-observer latitude
      Sl_lon      degree      Sub-Solar longitude
      Sl_lat      degree      Sub-Solar latitude
      r           AU          heliocentric distance
      rdot        km/s        heliocentric distance rate
      phang       degree      phase angle
      =========== =========== ==============================================

       

   There are currently no items in this folder.

.. container:: section
   :name: viewlet-below-content-body
