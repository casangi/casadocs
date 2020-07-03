.. container::
   :name: viewlet-above-content-title

Time Reference Frames
=====================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   CASA supported time reference frames

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      CASA supported time reference frames: 

       

      +-----------------------+-----------------------+-----------------------+
      | Acronym               | Name                  | Description           |
      +=======================+=======================+=======================+
      | ET                    | Ephemeris Time        |  The time scale used  |
      |                       |                       | prior to 1984 as the  |
      |                       |                       | independent variable  |
      |                       |                       | in gravitational      |
      |                       |                       | theories of the solar |
      |                       |                       | system. In 1984, ET   |
      |                       |                       | was replaced by       |
      |                       |                       | dynamical time (see   |
      |                       |                       | TDB, TT).             |
      +-----------------------+-----------------------+-----------------------+
      | GAST                  | Greenwich Apparent    |  The Greenwich hour   |
      |                       | Sidereal Time         | angle of the true     |
      |                       |                       | equinox `[1] <#fn>`__ |
      |                       |                       | of date.              |
      +-----------------------+-----------------------+-----------------------+
      | GMST                  | Greenwich Mean        | The Greenwich hour    |
      |                       | Sidereal Time         | angle of the mean     |
      |                       |                       | equinox `[1] <#fn>`__ |
      |                       |                       | of date, defined as   |
      |                       |                       | the angular distance  |
      |                       |                       | on the celestial      |
      |                       |                       | sphere measured       |
      |                       |                       | westward along the    |
      |                       |                       | celestial equator     |
      |                       |                       | from the Greenwich    |
      |                       |                       | meridian to the hour  |
      |                       |                       | circle that passes    |
      |                       |                       | through a celestial   |
      |                       |                       | object or point.      |
      |                       |                       |                       |
      |                       |                       | | GMST (in seconds at |
      |                       |                       |   UT1=0) =            |
      |                       |                       |   24110.54841 +       |
      |                       |                       |   8640184.812866 \* T |
      |                       |                       | | + 0.093104 \* T$^2$ |
      |                       |                       |   - 0.0000062 \*      |
      |                       |                       |   T$^3$               |
      |                       |                       | | where T is in       |
      |                       |                       |   Julian centuries    |
      |                       |                       |   from 2000 Jan. 1    |
      |                       |                       |   12h UT1:            |
      |                       |                       | | T = d / 36525       |
      |                       |                       | | d = JD - 2451545.0  |
      |                       |                       |                       |
      |                       |                       | (http://www.cv        |
      |                       |                       | .nrao.edu/~rfisher/Ep |
      |                       |                       | hemerides/times.html) |
      +-----------------------+-----------------------+-----------------------+
      | GMST1                 |                       |  GMST calculated      |
      |                       |                       | specifically with     |
      |                       |                       | reference to UT1      |
      +-----------------------+-----------------------+-----------------------+
      | IAT                   | International Atomic  |  The continuous time  |
      |                       | Time (a.k.a. TAI en   | scale resulting from  |
      |                       | Francais):            | analysis by the       |
      |                       |                       | Bureau International  |
      |                       |                       | des Poids et Mesures  |
      |                       |                       | of atomic time        |
      |                       |                       | standards in many     |
      |                       |                       | countries. The        |
      |                       |                       | fundamental unit of   |
      |                       |                       | TAI is the SI second  |
      |                       |                       | `[2] <#fn>`__ on the  |
      |                       |                       | geoid `[3] <#fn>`__ , |
      |                       |                       | and the epoch is 1958 |
      |                       |                       | January 1.            |
      +-----------------------+-----------------------+-----------------------+
      | LAST                  | Local Apparent        | LAST is derived from  |
      |                       | Sidereal Time         | LMST by applying the  |
      |                       |                       | equation of equinoxes |
      |                       |                       | `[1] <#fn>`__ or      |
      |                       |                       | nutation of the mean  |
      |                       |                       | pole of the Earth     |
      |                       |                       | from mean to true     |
      |                       |                       | position yields LAST. |
      |                       |                       |                       |
      |                       |                       | http://tycho.usno.n   |
      |                       |                       | avy.mil/sidereal.html |
      +-----------------------+-----------------------+-----------------------+
      | LMST                  | Local Mean Sidereal   | | Sidereal time is    |
      |                       | Time                  |   the hour angle of   |
      |                       |                       |   the vernal equinox, |
      |                       |                       |   the ascending node  |
      |                       |                       |   of the ecliptic on  |
      |                       |                       |   the celestial       |
      |                       |                       |   equator. The daily  |
      |                       |                       |   motion of this      |
      |                       |                       |   point provides a    |
      |                       |                       |   measure of the      |
      |                       |                       |   rotation of the     |
      |                       |                       |   Earth with respect  |
      |                       |                       |   to the stars,       |
      |                       |                       |   rather than the     |
      |                       |                       |   Sun. It corresponds |
      |                       |                       |   to the coordinate   |
      |                       |                       |   right ascension of  |
      |                       |                       |   a celestial body    |
      |                       |                       |   that is presently   |
      |                       |                       |   on the local        |
      |                       |                       |   meridian.           |
      |                       |                       | | LMST is computed    |
      |                       |                       |   from the current    |
      |                       |                       |   GMST plus the local |
      |                       |                       |   offset in longitude |
      |                       |                       |   measured positive   |
      |                       |                       |   to the east of      |
      |                       |                       |   Greenwich,          |
      |                       |                       |   (converted to a     |
      |                       |                       |   sidereal offset by  |
      |                       |                       |   the ratio           |
      |                       |                       |   1.00273790935 of    |
      |                       |                       |   the mean solar day  |
      |                       |                       |   to the mean         |
      |                       |                       |   sidereal day.)      |
      |                       |                       | | LMST = GMST +       |
      |                       |                       |   (observer's east    |
      |                       |                       |   longitude)          |
      |                       |                       |                       |
      |                       |                       | | http://www.c        |
      |                       |                       | v.nrao.edu/~rfisher/E |
      |                       |                       | phemerides/times.html |
      |                       |                       | | http://tycho.usno.n |
      |                       |                       | avy.mil/sidereal.html |
      +-----------------------+-----------------------+-----------------------+
      | TAI                   | International Atomic  | see IAT               |
      |                       | Time (a.k.a. TAI en   |                       |
      |                       | Francais)             |                       |
      +-----------------------+-----------------------+-----------------------+
      | TCB                   | Barycentric           |  The coordinate time  |
      |                       | Coordinate Time       | of the Barycentric    |
      |                       |                       | Celestial Reference   |
      |                       |                       | System (BCRS), which  |
      |                       |                       | advances by SI        |
      |                       |                       | seconds `[2] <#fn>`__ |
      |                       |                       | within that system.   |
      |                       |                       | TCB is related to TCG |
      |                       |                       | and TT by             |
      |                       |                       | relativistic          |
      |                       |                       | transformations that  |
      |                       |                       | include a secular     |
      |                       |                       | term.                 |
      +-----------------------+-----------------------+-----------------------+
      | TCG                   |                       |                       |
      +-----------------------+-----------------------+-----------------------+
      | TDB                   | Barycentric Dynamical | A time scale defined  |
      |                       | Time                  | by the IAU            |
      |                       |                       | (originally in 1976;  |
      |                       |                       | named in 1979;        |
      |                       |                       | revised in 2006) used |
      |                       |                       | in barycentric        |
      |                       |                       | ephemerides and       |
      |                       |                       | equations of motion.  |
      |                       |                       | TDB is a linear       |
      |                       |                       | function of TCB that  |
      |                       |                       | on average tracks TT  |
      |                       |                       | over long periods of  |
      |                       |                       | time; differences     |
      |                       |                       | between TDB and TT    |
      |                       |                       | evaluated at the      |
      |                       |                       | Earth's surface       |
      |                       |                       | remain under 2 ms for |
      |                       |                       | several thousand      |
      |                       |                       | years around the      |
      |                       |                       | current epoch. TDB is |
      |                       |                       | functionally          |
      |                       |                       | equivalent to Teph,   |
      |                       |                       | the independent       |
      |                       |                       | argument of the JPL   |
      |                       |                       | planetary and lunar   |
      |                       |                       | ephemerides           |
      |                       |                       | DE405/LE405.          |
      +-----------------------+-----------------------+-----------------------+
      | TDT                   | Terrestrial Dynamical |  The time scale for   |
      |                       | Time                  | apparent geocentric   |
      |                       |                       | ephemerides defined   |
      |                       |                       | by a 1979 IAU         |
      |                       |                       | resolution. In 1991   |
      |                       |                       | it was replaced by    |
      |                       |                       | TT.                   |
      +-----------------------+-----------------------+-----------------------+
      | TT                    | Terrestrial Time      |  An idealized form of |
      |                       |                       | International Atomic  |
      |                       |                       | Time (TAI) with an    |
      |                       |                       | epoch offset; in      |
      |                       |                       | practice TT = TAI +   |
      |                       |                       | 32s.184. TT thus      |
      |                       |                       | advances by SI        |
      |                       |                       | seconds on the geoid  |
      |                       |                       | `[3] <#fn>`__         |
      +-----------------------+-----------------------+-----------------------+
      | UT                    | Universal Time        |  Loosely, mean solar  |
      |                       |                       | time on the Greenwich |
      |                       |                       | meridian (previously  |
      |                       |                       | referred to as        |
      |                       |                       | Greenwich Mean Time). |
      |                       |                       | In current usage, UT  |
      |                       |                       | refers either to UT1  |
      |                       |                       | or to UTC.            |
      +-----------------------+-----------------------+-----------------------+
      | UT1                   |                       |  UT1 is formally      |
      |                       |                       | defined by a          |
      |                       |                       | mathematical          |
      |                       |                       | expression that       |
      |                       |                       | relates it to         |
      |                       |                       | sidereal time. Thus,  |
      |                       |                       | UT1 is                |
      |                       |                       | observationally       |
      |                       |                       | determined by the     |
      |                       |                       | apparent diurnal      |
      |                       |                       | motions of celestial  |
      |                       |                       | bodies, and is        |
      |                       |                       | affected by           |
      |                       |                       | irregularities in the |
      |                       |                       | Earth's rate of       |
      |                       |                       | rotation.             |
      +-----------------------+-----------------------+-----------------------+
      | UT2                   |                       |                       |
      |                       |                       | Before 1972 the time  |
      |                       |                       | broadcast services    |
      |                       |                       | kept their time       |
      |                       |                       | signals within 0.1    |
      |                       |                       | seconds `[2] <#fn>`__ |
      |                       |                       | of UT2, which is UT1  |
      |                       |                       | with annual and       |
      |                       |                       | semiannual variations |
      |                       |                       | in the earth's        |
      |                       |                       | rotation removed. The |
      |                       |                       | formal relation       |
      |                       |                       | between UT1 and UT2   |
      |                       |                       | is                    |
      |                       |                       |                       |
      |                       |                       | UT2 = UT1 + 0.022 \*  |
      |                       |                       | sin(2 \* Pi \* t) -   |
      |                       |                       | 0.012 \* cos(2 \* Pi  |
      |                       |                       | \* t)                 |
      |                       |                       |                       |
      |                       |                       | -  0.006 \* sin(4 \*  |
      |                       |                       |    Pi \* t) + 0.007   |
      |                       |                       |    \* cos(4 \* Pi \*  |
      |                       |                       |    t)                 |
      |                       |                       |    where              |
      |                       |                       |    t = 2000.0 + (MJD  |
      |                       |                       |    - 51544.03) /      |
      |                       |                       |    365.2422           |
      |                       |                       |    is the Besselian   |
      |                       |                       |    day fraction, and  |
      |                       |                       |    MJD is the         |
      |                       |                       |    Modified Julian    |
      |                       |                       |    Date (Julian Date  |
      |                       |                       |    - 2400000.5)       |
      |                       |                       |    http://www.c       |
      |                       |                       | v.nrao.edu/~rfisher/E |
      |                       |                       | phemerides/times.html |
      +-----------------------+-----------------------+-----------------------+
      | UTC                   | Coordinated Universal | UTC is based on IAT   |
      |                       | Time                  | but is maintained     |
      |                       |                       | within 0s.9 of UT1 by |
      |                       |                       | the introduction of   |
      |                       |                       | leap seconds when     |
      |                       |                       | necessary.            |
      +-----------------------+-----------------------+-----------------------+

      +-----------------------------------+-----------------------------------+
      | Footnote Number                   | 1                                 |
      +-----------------------------------+-----------------------------------+
      | Footnote Text                     | | mean equator and equinox v.     |
      |                                   |   true equator and equinox: The   |
      |                                   |   mean equator and equinox are    |
      |                                   |   used for the celestial          |
      |                                   |   coordinate system defined by    |
      |                                   |   the orientation of the Earth's  |
      |                                   |   equatorial plane on some        |
      |                                   |   specified date together with    |
      |                                   |   the direction of the dynamical  |
      |                                   |   equinox on that date,           |
      |                                   |   neglecting nutation. Thus, the  |
      |                                   |   mean equator and equinox moves  |
      |                                   |   in response only to precession. |
      |                                   |   Positions in a star catalog     |
      |                                   |   have traditionally been         |
      |                                   |   referred to a catalog equator   |
      |                                   |   and equinox that approximate    |
      |                                   |   the mean equator and equinox of |
      |                                   |   a standard epoch.               |
      |                                   | | The true equator and equinox    |
      |                                   |   are affected by both precession |
      |                                   |   and nutation. The Equation of   |
      |                                   |   the Equinoxes is the difference |
      |                                   |   (apparent sidereal time minus   |
      |                                   |   mean sidereal time).            |
      |                                   |   Equivalently, the difference    |
      |                                   |   between the right ascensions of |
      |                                   |   the true and mean equinoxes,    |
      |                                   |   expressed in time units.        |
      |                                   |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |                                   |                                   |
      +-----------------------------------+-----------------------------------+

      +-----------------------------------+-----------------------------------+
      | FootnoteNumber                    | 2                                 |
      +-----------------------------------+-----------------------------------+
      | Footnote Text                     |  The Systeme International (SI)   |
      |                                   | second is defined as the duration |
      |                                   | of 9,192,631,770 cycles of        |
      |                                   | radiation corresponding to the    |
      |                                   | transition between two hyperfine  |
      |                                   | levels of the ground state of     |
      |                                   | caesium 133.                      |
      |                                   |                                   |
      |                                   |                                   |
      +-----------------------------------+-----------------------------------+

      +-----------------------------------+-----------------------------------+
      | Footnote Number                   | 3                                 |
      +-----------------------------------+-----------------------------------+
      | Footnote Text                     | The geoid is an equipotential     |
      |                                   | surface that coincides with mean  |
      |                                   | sea level in the open ocean. On   |
      |                                   | land it is the level surface that |
      |                                   | would be assumed by water in an   |
      |                                   | imaginary network of frictionless |
      |                                   | channels connected to the ocean.  |
      |                                   |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |                                   |                                   |
      +-----------------------------------+-----------------------------------+

.. container:: section
   :name: viewlet-below-content-body
