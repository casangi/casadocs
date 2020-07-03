.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Spectral Frames
===============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Spectral Frames supported in CASA

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Spectral Frames
         :name: spectral-frames-1

      CASA supported spectral frames:

      +----------------+-------------------------+-------------------------+
      | Frame          | Description             | Definition              |
      +================+=========================+=========================+
      | REST           | rest frequency          | Lab frame or source     |
      |                |                         | frame; cannot be        |
      |                |                         | converted to any other  |
      |                |                         | frame                   |
      +----------------+-------------------------+-------------------------+
      | LSRK           | LSR as a kinematic      | 20km/s in direction of  |
      |                | (radio) definition      | RA, Dec - [270,+30] deg |
      |                | (J2000) based on        | (B1900.0) (Gordon 1975  |
      |                | average velocity of     | `[1] <#cit>`__ )        |
      |                | stars in the Solar      |                         |
      |                | neighborhood            |                         |
      +----------------+-------------------------+-------------------------+
      | LSRD           | Local Standard of Rest  | U$\odot$=9kms/s,        |
      |                | (J2000), dynamical, IAU | V$\odot$                |
      |                | definition. Solar       | =12km/s,W$\odot$=7km/s. |
      |                | peculiar velocity in    | Or 16.552945km/s        |
      |                | the reference frame of  | towards l,b = 53.13,    |
      |                | a circular orbit about  | +25.02 deg (Delhaye     |
      |                | the Galactic            | 1965 `[2] <#cit>`__)    |
      |                | Center, based on        |                         |
      |                | average velocity of     |                         |
      |                | stars in the Solar      |                         |
      |                | neighborhood and solar  |                         |
      |                | peculiar motion         |                         |
      +----------------+-------------------------+-------------------------+
      | BARY           | Solar System            |                         |
      |                | Baryceneter (J2000)     |                         |
      +----------------+-------------------------+-------------------------+
      | GEO            | Geocentric, referenced  |                         |
      |                | to the Earth's center   |                         |
      +----------------+-------------------------+-------------------------+
      | TOPO           | Topocentric             | Local observatory       |
      |                |                         | frame, fixed in         |
      |                |                         | observing frequency, no |
      |                |                         | doppler tracking        |
      +----------------+-------------------------+-------------------------+
      | GALACTO        | Galactocentric (J2000), | 220 km/s in the         |
      |                | referenced to dynamical | direction l,b = 270, +0 |
      |                | center of the Galaxy    | deg.  (Kerr and         |
      |                |                         | Lynden-Bell 1986        |
      |                |                         | `[3] <#cit>`__)         |
      +----------------+-------------------------+-------------------------+
      | LGROUP         | Mean motion of Local    | 308km/s towards l,b =   |
      |                | Group Galaxies with     | 105,-7                  |
      |                | respect to its bary     |                         |
      |                | center                  |                         |
      +----------------+-------------------------+-------------------------+
      | CMB            | Cosmic Microwave        | 369.5km/s towards l,b = |
      |                | Background, COBE        | 264.4,48.4. (Kogut et   |
      |                | measurements of dipole  | al. 1993                |
      |                | anisotropy              | `[4] <#cit>`__)         |
      +----------------+-------------------------+-------------------------+
      | Undefined      |                         |                         |
      +----------------+-------------------------+-------------------------+

       

      .. container:: center

          

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Gordon 1975: "**Methods of Experimental Physics:  |
      |                 | Volume 12:** Astrophysics, Part C: Radio          |
      |                 | Observations", ed. M.L.Meeks, Academic Press 1976 |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Delhaye 1965                                      |
      |                 | (`ADS <http://articles.a                          |
      |                 | dsabs.harvard.edu/cgi-bin/nph-iarticle_query?1965 |
      |                 | gast.book...61D&amp;data_type=PDF_HIGH&amp;whole_ |
      |                 | paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__) |
      +-----------------+---------------------------------------------------+

       

      +-----------------+---------------------------------------------------+
      | Citation Number | 3                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Kerr F. J. & Lynden-Bell D. 1986 MNRAS, 221, 1023 |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/1986MNRAS.221.1023K>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 4                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Kogut A. et al. 1993                              |
      |                 | (`ADS <http://articles.a                          |
      |                 | dsabs.harvard.edu/cgi-bin/nph-iarticle_query?1993 |
      |                 | ApJ...419....1K&amp;data_type=PDF_HIGH&amp;whole_ |
      |                 | paper=YES&amp;type=PRINTER&amp;filetype=.pdf>`__) |
      +-----------------+---------------------------------------------------+

       

      .. rubric::  Doppler Types
         :name: sec587
         :class: subsection

      CASA supported Doppler types (velocity conventions) where $f_v$ is
      the observed frequency and $f_0$ is the rest frame frequency of a
      given lineand positive velocity V is increasing away from the
      observer:

      .. container:: center

         +--------------+------------------------------------------------------+
         | Name         | Description                                          |
         +==============+======================================================+
         | RADIO        | $$V = c \\frac{(f_0 - f_v)}{f_0}$$                   |
         +--------------+------------------------------------------------------+
         | Z            | $$V=cz$$  $$z = \\frac{(f_0 - f_v)}{f_v}$$           |
         +--------------+------------------------------------------------------+
         | RATIO        | $$V=c(\frac{f_v}{f_o})$$                             |
         +--------------+------------------------------------------------------+
         | BETA         | $$V=c\frac                                           |
         |              | {(1-(\frac{f_v}{f_0})^2)}{(1+(\frac{f_v}{f_0})^2)}$$ |
         +--------------+------------------------------------------------------+
         | GAMMA        | $$ V=c\frac{(1 +                                     |
         |              | (\frac{f_v}{f_0})^2)}{2\frac{f_v}{f_0}}$$            |
         +--------------+------------------------------------------------------+
         | OPTICAL      | $$V= c\frac{(f_0 - f_v)}{f_v}$$                      |
         +--------------+------------------------------------------------------+
         | TRUE         | $$V=c\frac                                           |
         |              | {(1-(\frac{f_v}{f_0})^2)}{(1+(\frac{f_v}{f_0})^2)}$$ |
         +--------------+------------------------------------------------------+
         | RELATIVISTIC | $$V=c\frac                                           |
         |              | {(1-(\frac{f_v}{f_0})^2)}{(1+(\frac{f_v}{f_0})^2)}$$ |
         +--------------+------------------------------------------------------+

          

.. container:: section
   :name: viewlet-below-content-body
