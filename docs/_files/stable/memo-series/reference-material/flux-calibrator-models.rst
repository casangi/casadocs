.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Flux Calibrator Models
======================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Descriptions of flux calibrator models for flux density scaling

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      There are two categories of flux calibrator models available to
      determine flux density scales: compact extra-galactic sources and
      solar system objects. The models for bright extragalactic sources
      are described in the form of polynomial expressions for spectral
      flux densities and clean component images for spatial information.
      The flux density scales based on the solar system objects are
      commonly used to establish flux density scales for mm and sub-mm
      astronomy. These models consist of brightness temperature models
      and their ephemeris data.

      .. rubric:: Compact extragalactic sources
         :name: compact-extragalactic-sources

      For the VLA, the default source models are customarily point
      sources defined by the ’Baars’, ’Perley 90’, ’Perley-Taylor 99’,
      ’Perley-Butler 2010’,  ’Perley-Butler 2013’ (time-variable),
      'Perley-Butler 2017' (time-variable) or ’Scaife-Heald 2012’ flux
      density scales (’Perley-Butler 2017’ is the current standard by
      default), or point sources of unit flux density if the flux
      density is unknown. 'Stevens-Reynolds 2016' currently contains
      only one source, 1934-638, which is primarily used for flux
      calibrator for the ACTA.

      The model images (CLEAN component images) are readily available in
      CASA for the sub set of the sources listed below. The task
      **setjy** provides listing of the available model images included
      in the CASA package's data directory. You can find the path to the
      directory containing your list of VLA Stokes I models by typing
      (inside CASA) print os.getenv('CASAPATH').split(' ')[0] +
      '/data/nrao/VLA/CalModels/'. The `setjy Description
      Page <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_setjy>`__
      in CASA Docs also lists the models that are available in CASA.
      These models can be plotted in plotms.

      Alternatively, the user can provide a model image at the
      appropriate frequency in Jy/pixel units, typically the .model made
      by **clean** (which is a list of components per pixel, as
      required, although the restored .image is in Jy/beam). For unknown
      calibrators, however, the spectral flux distribution has to be
      explicitely specified in **setjy**. If you do not specify the
      correct path to a model (and you have not provided your own
      model), the default model of a point sources of unit flux density
      will be adopted. 

      .. container:: caption

          

      .. container:: center

         +-------------+-------------+-------------+-------------+-------------+
         | 3C/Common   | B1950 Name  | J2000 Name  | Alt. J2000  | Standards   |
         | Name        |             |             | Name        |             |
         +-------------+-------------+-------------+-------------+-------------+
         | –           | –           | –           | J0133-3629  | 9           |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C48        | 0134+329    | 0137+331    | J0137+3309  | 1,2,        |
         |             |             |             |             | 3,4,5,6,7,9 |
         +-------------+-------------+-------------+-------------+-------------+
         | FORNAX X    | –           | –           | J0322-3712  | 9           |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C123       | 0433+295    | 0437+296    | J0437+2940  | 2, 9        |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C138       | 0518+165    | 0521+166    | J0521+1638  | 1,3,4,5,6   |
         +-------------+-------------+-------------+-------------+-------------+
         | PICTOR A    | –           | –           | J0519-4546  | 9           |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C144       | –           | –           | J0534+2200  | 9           |
         | (TAURUS     |             |             |             |             |
         | A/CRAB)     |             |             |             |             |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C147       | 0538+498    | 0542+498    | J0542+4951  | 1,3,4,5,6,  |
         |             |             |             |             | 7, 9        |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C196       | 0809+483    | 0813+482    | J0813+4813  | 1,2,7,9     |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C218(HYDRA | –           | –           | J0918-1205  | 9           |
         | A)          |             |             |             |             |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C274       | –           | –           | J1230+1223  | 9           |
         | (VIRGO A)   |             |             |             |             |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C286       | 1328+307    | 1331+305    | J1331+3030  | 1,2,        |
         |             |             |             |             | 3,4,5,6,7,9 |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C295       | 1409+524    | 1411+522    | J1411+5212  | 1,2,        |
         |             |             |             |             | 3,4,5,6,7,9 |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C438       | –           | –           | J1651+0459  | 9           |
         | (HERCULES   |             |             |             |             |
         | A)          |             |             |             |             |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C353       | –           | –           | J1720-0059  | 9           |
         +-------------+-------------+-------------+-------------+-------------+
         | –           | 1934-638    | –           | J1939-6342  | 1,3,4,5,6,8 |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C380       | 1828+487    | 1829+487    | J1829+4845  | 7,9         |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C405       | –           | –           | J1959+4044  | 9           |
         | (CYGNUS A)  |             |             |             |             |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C444       | –           | –           | J2214-1701  | 9           |
         +-------------+-------------+-------------+-------------+-------------+
         | 3C461       | –           | –           | J2323+5848  | 9           |
         | (CASSIOPEIA |             |             |             |             |
         | A)          |             |             |             |             |
         +-------------+-------------+-------------+-------------+-------------+

      Standards are: (1) `Perley-Butler 2010 <#perley-butler-2010>`__,
      (2) `Perley-Butler 2013 <#perley-butler-2013>`__, (3)
      `Perley-Taylor 99 <#perley-taylor-99>`__, (4) `Perley-Taylor
      95 <#perley-taylor-95>`__, (5) `Perley 90 <#perley-90>`__, (6)
      `Baars <#baars>`__, (7) `Scaife-Heald
      2012 <#scaife-heald-2012>`__, (8) `Stevens-Reynolds
      2016 <#stevens-reynolds-2016>`__ (9) `Perley-Butler 2017
       <#perley-butler-2017>`__

      | 
      | 

      +---------+-----------------------------------------------------------+
      | Type    | Table                                                     |
      +---------+-----------------------------------------------------------+
      | ID      | fluxcalmodels-tab-1                                       |
      +---------+-----------------------------------------------------------+
      | Caption | Known sources and their alternative names recognized by   |
      |         | **setjy** task                                            |
      +---------+-----------------------------------------------------------+

      | 
      | ALMA also uses a few dozen compact QSO as flux standards,
        monitored 2-4 times a month at bands 3, 6 and 7 (90 - 345 GHz).
        Due to rapid variability these data are not packaged with CASA,
        but can be accessed via
        https://almascience.eso.org/alma-data/calibrator-catalogue

       

      .. rubric:: Baars
         :name: baars

      The only standard to not have the year in the name. It is 1977.
      The models are second order polynomials in log(ν), valid between
      408 MHz and 15 GHz.

      Reference: Baars et al. (1977) `[1] <#cit>`__ with a commentary by
      Kellermann, K. I. (1999) `[2] <#cit>`__

      +-----------------+---------------------------------------------------+
      | Citation Number | 1                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Baars, J. W. M. et al. 1977, A&A, 61, 99          |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/1977A%26A....61...99B>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 2                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Kellermann, K. I. 2009\ *,* A&A 500, 143          |
      |                 | (`ADS <http://a                                   |
      |                 | dsabs.harvard.edu/abs/2009A%26A...500..143K>`__)  |
      +-----------------+---------------------------------------------------+

      .. rubric:: 
         Perley 90
         :name: perley-90
         :class: subsubsection

      This standard also includes 1934-638 from Reynolds (7/94) and
      3C138 from Baars et al. (1977) `[1] <#cit>`__ .

      Details can be found at
      http://www.vla.nrao.edu/astro/calib/manual/baars.html\ .

      .. rubric:: Perley-Taylor 95
         :name: sec556
         :class: subsubsection

      Perley and Taylor (1995.2); plus Reynolds (1934-638; 7/94) Details
      can be found at
      http://www.vla.nrao.edu/astro/calib/manual/baars.html\ .

      .. rubric:: Perley-Taylor 99
         :name: perley-taylor-99

      Perley and Taylor (1999.2); plus Reynolds (1934-638; 7/94) Details
      can be found at
      http://www.vla.nrao.edu/astro/calib/manual/baars.html\ .

      .. rubric:: Perley-Butler 2010
         :name: sec558
         :class: subsubsection

      A preliminary version of Perley-Butler 2013. This version also has
      coefficients for sources that showed some degree of variability
      (see Perley & Butler (2013) `[3] <#cit>`__) but they are treated
      as the steady sources (i.e. no time dependent models are used).

      +-----------------+---------------------------------------------------+
      | Citation Number | 3                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Perley, R. A., & Butler, B. J. 2013, ApJS, 204,   |
      |                 | 19                                                |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2013ApJS..204...19P>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Perley-Butler 2013
         :name: perley-butler-2013

      Flux scale for the constant flux sources 3C123, 3C196, 3C286, and
      3C295 as well as variable sources (3C48, 3C138, and 3C147). The
      models for the variable sources are time-dependent.
      Reference: Perley & Butler (2013)  `[3] <#cit>`__ .

      .. rubric:: Scaife-Heald 2012
         :name: scaife-heald-2012

      Low frequency, 30-300MHz, calibrators 3C48, 3C147, 3C196, 3C286,
      3C295, and 3C380.

      Reference: Scaife & Heald (2012)  `[4] <#cit>`__

      +-----------------+---------------------------------------------------+
      | Citation Number | 4                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Scaife, A. M., & Heald, G. H. 2012, MNRAS, 423,   |
      |                 | 30                                                |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2012MNRAS.423L..30S>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Stevens-Reynolds 2016
         :name: stevens-reynolds-2016

      Low frequency (<11GHz) polynomial from Reynolds and updated high
      frequecy polynomial from Stevens.

      Reference: Partridge et al. (2016)  `[5] <#cit>`__

      +-----------------+---------------------------------------------------+
      | Citation Number | 5                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Partridge et al. 2016, ApJ 821,1                  |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2016ApJ...821...61P>`__) |
      +-----------------+---------------------------------------------------+

       

      .. rubric:: Perley-Butler 2017
         :name: perley-butler-2017

      The flux density scale of Perley-Butler 2013 extended downward to
      ~50 MHz. Twenty sources were drawn from the Baar, Perley-Butler
      2013, and Scaife-Heald 2012. Flux scale for the constant flux
      sources Fornax A, 3C123, J0444-2809, Pictor A, 3C144, (Taurus A or
      Crab), 3C196, 3C218 (Hydra A),  3C274 (Virgo A or  M87), 3C286,
      3C295,  3C348 (Hercules A), 3C353, 3C380, 3C405 (Cygnus A), 3C444,
      and 3C461 (Cassiopeia A) as well as variable sources (3C48, 3C138,
      and 3C147). The models for the variable sources are
      time-dependent. The frequency range valid for the model for each
      source is also listed below.

      ============ ============================
      Source       Valid frequency range in GHz
      ============ ============================
      J0133-3649   0.2-4
      3C48         0.05-50
      Fornax X     0.2-0.5
      3C123        0.06-50
      J0444-2809   0.2-2.0
      3C138        0.2-50
      Pictor A     0.2-4.0
      Taurus A     0.05-4.0
      3C147        0.05-50
      3C196        0.050-50
      Hydra A      0.05-12
      Virgo A      0.05-3
      3C286        0.05-50
      3C295        0.05-50
      Hercules A   0.2-12
      3C353        0.2-4
      3C380        0.05-4.0\*
      Cygnus A     0.05-12
      3C444        0.2-12
      Cassiopeia A 0.2-4
      ============ ============================

      \* The corrected frequency range for 3C380 is noted here based on 
      B. J.  Butler 2018, private comunication (CAS-9538)
      Reference: Perley & Butler (2017)  `[7] <#cit>`__

       

       

      +-----------------+---------------------------------------------------+
      | Citation Number | 7                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Perley, R. A. & Butler, B. J. 2017, ApJS,         |
      |                 | 230,7(`ADS <http:                                 |
      |                 | //adsabs.harvard.edu/abs/2017ApJS..230....7P>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Solar System objects
         :name: solar-system-objects

      The usual approach in mm and sub-mm regimes is to use models that
      are, to first order, thermal sources in the Solar System. Their
      apparent brightness varies in time with their distance from the
      Earth (and Sun), and orientation if they are not perfect spheres
      with zero obliquity. However, most of them have almost constant
      surface properties, so once those properties are measured their
      apparent brightness distributions, they can in principle be
      predicted for any time, given an ephemeris. Planets, in
      particular, have more complex spectra and effects such as
      atmospheric lines, magnetic fields, seasons, polar caps and
      surface features that need to be taken into account when they are
      available and significant. In CASA, the Solar System objects
      supported by **setjy** are available through the
      ‘Butler-JPL-Horizons 2010’, and ’Butler-JPL-Horizons 2012’
      standards. It is recommended to use 'Butler-JPL-Horizons 2012' as
      it contains updated models. The 2012 models are described in ALMA
      Memo 594, which is available on
      `https://science.nrao.edu/facilities/alma/~aboutALMA/Technology/ALMA_Memo_Series/alma594/abs594 <https://science.nrao.edu/facilities/alma/aboutALMA/Technology/ALMA_Memo_Series/alma594/abs594>`__
      . Models can be found  by typing (in CASA) print
      os.getenv('CASAPATH').split(' ')[0] +
      '/data/alma/SolarSystemModels'.

      The following objects are supported based on models from
      Butler-JPL-Horizons 2012, updated where necessary as mentioned
      under each object. Please refer ALMA Memo594 for the detailed
      comparisons with the models in Butler-JPL-Horizons-2010.

      .. rubric:: Venus
         :name: venus

      The model spans the frequencies from ~300MHz to 1THz. No
      atmospheric lines such as CO,H\ :sub:`2`\ O\ :sub:`,` HDO, and etc
      are included. Modeled based on Clancy et al. (2012)
       `[6] <#cit>`__.

      +-----------------+---------------------------------------------------+
      | Citation Number | 6                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Clancy, R.T. et al. 2012, Icarus, 217, 779        |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2012Icar..217..779C>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Mars
         :name: mars

      Full implementation of the model of Rudy et al. (1987)
      `[7] <#cit>`__, tabulated as a function of time and frequency
      (30-1000GHz). No atmospheric lines are included.

      +-----------------+---------------------------------------------------+
      | Citation Number | 7                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Rudy, D.J. et al. 1987, Icarus, 71, 159           |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/1987Icar...71..159R>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Jupiter
         :name: jupiter

      Model for 30-1020GHz (from Glenn Orton, private communication),
      does not include synchrotron emission.

      .. rubric:: Uranus
         :name: uranus

      Model for 60-1800GHz (from Glenn Orton and Raphael Moreno, private
      communication), contains no rings or synchrotron.

      .. rubric:: Neptune
         :name: neptune

      Model for 2-2000 GHz (from Glenn Orton and Raphael Moreno, private
      communication), contains no rings or synchrotron.

      .. rubric:: Io
         :name: io

      Spline interpolation of data points from 15 to 29980 GHz
      (references: please refer to the ALMA memo 594 Table 1).  Strongly
      not recommended to use for the primary flux calibrator for ALMA
      observations.

      .. rubric:: Europa
         :name: europa

      Spline interpolation of data points from 15 to 29980 GHz
      (references: please refer to the ALMA memo 594 Table 1).  Strongly
      not recommended to use for the primary flux calibrator for ALMA
      observations.

      .. rubric:: Ganymede
         :name: ganymede

      Spline interpolation of data points from 5 to 29980 GHz
      (references: please refer to the ALMA memo 594 Table 1).

      .. rubric:: Callisto
         :name: callisto

      Spline interpolation of data points from 5 to 29980 GHz
      (references: please refer to the ALMA memo 594 Table 1).

      .. rubric:: Titan
         :name: titan

      Model from Mark Gurwell, from 53.3-­1024.1 GHz. Contains surface
      and atmospheric emission. The atmosphere includes N2-­N2 and
      N2-­CH4 Collision-­Induced Absorption (CIA), and lines from minor
      species CO, :sup:`13`\ CO, C\ :sup:`18`\ O, HCN, H\ :sup:`13`\ CN
      and HC\ :sup:`15`\ N. See, e.g., Gurwell & Muhleman (2000)
      `[8] <#cit>`__; Gurwell (2004) `[9] <#cit>`__.

      +-----------------+---------------------------------------------------+
      | Citation Number | 8                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Gurwell, M.A. & D.O. Muhleman 2000, Icarus, 145,  |
      |                 | 65w                                               |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2000Icar..145..653G>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 9                                                 |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Gurwell, M.A. 2004, ApJ, 616, L7                  |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2004ApJ...616L...7G>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Asteroids
         :name: asteroids

      Some asteroids, namely Ceres, Pallas, Vesta, and Juno are included
      in the Butler-JPL-Horizons 2012. The models consists of the
      constant brightness temperature in frequency. For Ceres, Pallas,
      and Vesta, updated models based on thermophysical models (TPM) (T.
      Mueller, private communication) which are tabulated in time and
      frequency, are available for the observations taken after January
      1st 2015, 0:00 UT. **setjy** task will automatically switch to the
      new models for the observations taken on and after that date. The
      TPM are also available for Lutetia but it is not advised to use
      for the absolute flux calibration for ALMA. Each of the tabulated
      models contains the flux density at 30, 80, 115, 150, 200, 230,
      260, 300, 330, 360, 425, 650, 800, 950, and 1000 GHz. The time
      resolution is 1 hour for Ceres and 15 min for Lutetia, Pallas, and
      Vesta. The cubic interpolation is employed to obtain the flux
      densities at other frequencies.

      .. rubric:: Ceres
         :name: ceres

      Model with a constant $T_b$ = 185K over frequencies (Moullet et
      al. 2010 `[10] <#cit>`__, Muller & Lagerros 2002 `[11] <#cit>`__,
      Redman et al. 1998 `[12] <#cit>`__, Altenhoff et al. 1996
      `[13] <#cit>`__) if time of the observations took place
      ($t_{obs}$) is before 2015.01.01, 0:00 UT, TPM if $t_{obs}$ $\ge$
      2015.01.01, 0:00 UT.

      +-----------------+---------------------------------------------------+
      | Citation Number | 10                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Moullet, A. et al. 2010, A&A, 516, L10            |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/2010A%26A...516L..10M>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 11                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Muller, T.G. & J.S.V. Lagerros 2002, A&A, 381,    |
      |                 | 324                                               |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/2002A%26A...381..324M>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 12                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Redman, R.O. et al. 1998, AJ, 116, 1478           |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/1998AJ....116.1478R>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 13                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Altenhoff, W.J. et al. 1996, A&A, 309, 953        |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/1996A%26A...309..953A>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Pallas
         :name: pallas

      Model with a constant $T_b$ = 189K (Chamberlain et al. 2009
      `[14] <#cit>`__, Altenhoff et al. 1994 `[15] <#cit>`__) for
      $t_{obs}$ $\lt$ 2015.01.01, 0:00 UT, and TPM for $t_{obs}$ $\ge$
      2015.01.01, 0:00 UT

      +-----------------+---------------------------------------------------+
      | Citation Number | 14                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Chamberlain, M.A. et al. 2009, Icarus, 202, 487   |
      |                 | (`ADS <http:                                      |
      |                 | //adsabs.harvard.edu/abs/2009Icar..202..487C>`__) |
      +-----------------+---------------------------------------------------+

      +-----------------+---------------------------------------------------+
      | Citation Number | 15                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Altenhoff, W.J. et al. 1994, A&A, 287, 641        |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/1994A%26A...287..641A>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Vesta
         :name: vesta

      Model with a constant $T_b$ = 155K (Leyrat et al. 2012
      `[16] <#cit>`__, Chamberlain et al. 2009 `[14] <#cit>`__, Redman
      et al. 1998 `[12] <#cit>`__, Altenhoff et al. 1994
      `[15] <#cit>`__) for $t_{obs}$ $\lt$ 2015.01.01, 0:00 UT, and TPM
      for $t_{obs}$ $\ge$ 2015.01.01, 0:00 UT

      +-----------------+---------------------------------------------------+
      | Citation Number | 16                                                |
      +-----------------+---------------------------------------------------+
      | Citation Text   | Leyrat, C. et al. 2012, A&A, 539, A154            |
      |                 | (`ADS <http://                                    |
      |                 | adsabs.harvard.edu/abs/2012A%26A...539A.154L>`__) |
      +-----------------+---------------------------------------------------+

      .. rubric:: Juno
         :name: juno

      Model with a constant $T_b$ = 153K (Chamberlain et al. 2009
      `[14] <#cit>`__, Altenhoff et al. 1994 `[15] <#cit>`__)

       

.. container:: section
   :name: viewlet-below-content-body
