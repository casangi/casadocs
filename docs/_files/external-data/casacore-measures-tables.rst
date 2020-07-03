.. container::
   :name: viewlet-above-content-title

The casacore Measures tables
============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   This chapter describes the casacore Measures tables needed to perform
   accurate conversions of reference frames.

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: plain
      :name: parent-fieldname-text

      The casacore infrastructure includes classes to handle physical
      quantities with a reference frame, so-called "Measures". Each type
      of Measure has its own distinct class in casacore which is derived
      from the Measure base class. One of the main functionalilties
      provided by casacore w.r.t. Measures, is the conversion of
      Measures from one reference frame to another using the MeasConvert
      classes.

      Many of the spectral, spatial, and time reference frames are
      time-dependent and require the knowledge of the outcome of ongoing
      monitoring measurements of properties of the Earth and
      astronomical objects by certain service observatories. This data
      is tabulated in a number of tables (*"Measures Tables"*) which are
      stored in the CASA data repository in the subdirectory
      *"geodetic"*. A snapshot of this repository is included in each
      tarball distribution of CASA and in the casadata module for
      CASA6+. It can be updated to the latest status as described
      `here <https://casa.nrao.edu/casadocs-devel/stable/external-data/casa-data-repository>`__.

      The CASA data repository is updated daily based on the daily
      refinement of the geodetic information from the relevant services
      like the International Earth Rotation and Reference Systems
      Service (IERS). Strictly speaking, the Measures tables are part of
      the casacore infrastructure which is developed by NRAO, ESO, NAOJ,
      CSIRO, and ASTRON. In order to keep the repository consistent
      between the partners, the Measures tables are initially created at
      a single institution (ASTRON) and then copied into the NRAO CASA
      data repository from where all CASA users can retrieve them. As of
      March 2020, the update of the NRAO CASA copy of the Measures
      tables in "geodetic" and the planetary ephemerides in directory
      "ephemerides" takes place every day between 18 h UTC and 19 h UTC
      via two redundant servers at ESO (Garching).

      The following list describes the individual Tables in subdirectory
      "geodetic":

      -  **IERSeop2000:**
         The IERS EOP2000C04_05 Earth Orientation Parameters using the
         precession/nutation model "IAU2000" (files eopc04_IAU2000.xx)
      -  **IERSeop97**:
         The IERS EOPC04_05 Earth Orientation Parameters using the
         precession/nutation model "IAU 1980" (files eopc04.xx)
      -  **IERSpredict:
         **\ IERS Earth Orientation Data predicted from NEOS (from file
         ftp://ftp.iers.org/products/eop/rapid/daily/finals.daily)
      -  **IGRF:**
         International Geomagnetic Reference Field Schmidt
         `semi-normalised spherical harmonic
         coefficients <https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/>`__.
         (Note that this still uses IGRF12. An update to IGRF13 is
         underway.)
      -  IMF (not a Measures Table proper, access not integreated in
         Measures framework):
         Historical interplanetary magnetic field data until MJD 52618
         (December 2002).
      -  KpApF107 (not a Measures Table proper, access not integreated
         in Measures framework)\ **:
         **\ Historical geomagnetic and solar activity indices until MJD
         54921 (April 2009)
      -  **Observatories:
         **\ Table of the official locations of radio observatories.
         Maintained by the CASA consortium.
      -  SCHED_locations (not a Measures Table proper, access not
         integreated in Measures framework)\ **:**
         VLBI station locations
      -  **TAI_UTC:
         **\ TAI_UTC difference (i.e. leap second information) obtained
         from USNO\ **
         **

       

      Measures Tables in the directory "ephemerides":

      -  **DE200**:
         Historical JPL Planetary ephemeris DE200 used for Astronomical
         Almanach from 1984 to 2003 (from
         ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de200)

      -  **DE405**:
         JPL Planetary ephemeris DE405; includes nutations and
         librations; referred to the ICRS(from
         ftp://ssd.jpl.nasa.gov/pub/eph/planets/ascii/de405)

   There are currently no items in this folder.

.. container:: section
   :name: viewlet-below-content-body
