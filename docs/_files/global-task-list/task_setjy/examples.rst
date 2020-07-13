Examples
========

.. container:: documentDescription description

   task examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Set flux density explictly
         :name: set-flux-density-explictly

      With standard='manual' (and *selectdata=True*), the parameters
      look like this. fluxdensity takes a list of flux densities, [I, Q,
      U, V] at *reffreq*. The same reffreq will be used as a reference
      frequecy for *spix*, *polindex*, and *polange*.

      .. container:: casa-output-box

         #  setjy :: Fills the model column with the visibilities of a
         calibrator
         vis                 =         ''        #  Name of input
         visibility file
         field               =         ''        #  Field name(s)
         spw                 =         ''        #  Spectral window
         identifier (list)
         selectdata          =       True        #  Other data selection
         parameters
              timerange      =         ''        #  Time range to
         operate on (for usescratch=T)
              scan           =         ''        #  Scan number range
         (for usescaratch=T)
              intent         =         ''        #  Observation intent
              observation    =         ''        #  Observation ID range
         (for usescratch=T)
         scalebychan         =       True        #  scale the flux
         density on a per channel basis or else on
                                                 #   a per spw basis
         standard            =   'manual'        #  Flux density
         standard
              fluxdensity    =         -1        #  Specified flux
         density [I,Q,U,V]; (-1 will lookup values)
              spix           =        0.0        #  Spectral index
         (including higher terms) of I fluxdensity
              reffreq        =     '1GHz'        #  Reference frequency
         for spix
              polindex       =         []        #  Coefficients of an
         expansion of frequency-dependent
                                                 #   linear polarization
         fraction expression
              polangle       =         []        #  Coefficients of an
         expansion of frequency-dependent
                                                 #   polarization angle
         expression
              rotmeas        =        0.0        #  Rotation measure (in
         rad/m^2)
         usescratch          =      False        #  Will create if
         necessary and use the MODEL_DATA

      In the simplest form, setting a constant Stokes I flux density for
      a calibrator ( field='0') for all spw can be done as

      .. container:: casa-input-box

         setjy(vis='data.ms', field='0', fluxdensity=[3.5,0.0,0.0,0.0])

      To set Stokes I flux density with spectral index and Stokes Q and
      U using frequency-dependent polarization index and polarization
      angle (in rad) also including rotation measure:

      .. container:: casa-input-box

         setjy(vis=‘data.ms’, standard='manual', field = ‘3C48’,
         fluxdensity=[6.4861, 0, 0, 0], spix=[-0.630458,-0.132252],
         reffreq="3000.0MHz”, polindex=[0.02143,0.0392,0.002349,-0.0230]
         polangle=[-1.7233,1.569,-2.282,1.49], rotmeas=-68.0)

      .. rubric:: Use one of the predefined standards
         :name: use-one-of-the-predefined-standards

       Current default for *standard* is 'Perley-Butler 2017' and the
      parameters look like this (with *selectdata=True*):

      .. container:: casa-output-box

         | #  setjy :: Fills the model column with the visibilities of a
           calibrator
         | vis                 =         ''        #  Name of input
           visibility file
         | field               =         ''        #  Field name(s)
         | spw                 =         ''        #  Spectral window
           identifier (list)
         | selectdata          =       True        #  Other data
           selection parameters
         |      timerange      =         ''        #  Time range to
           operate on (for usescratch=T)
         |      scan           =         ''        #  Scan number range
           (for usescaratch=T)
         |      intent         =         ''        #  Observation intent
         |      observation    =         ''        #  Observation ID
           range (for usescratch=T)
         | scalebychan         =       True        #  scale the flux
           density on a per channel basis or else on a per spw basis
         | standard            = 'Perley-Butler 2017' #  Flux density
           standard
         |      model          =         ''        #  File location for
           field model
         |      listmodels     =      False        #  List the available
           modimages for VLA calibrators or Tb models for Solar System
           objects
         |      interpolation  =  'nearest'        #  method to be used
           to interpolate in time
         | usescratch          =      False        #  Will create if
           necessary and use the MODEL_DATA

      In the most simplest case, using the default stanadard, if
      *field='0'* is one of the known sources as listed in Flux
      Calibrator Models (e.g. 3C286), the following will set appropriate
      channel dependent flux densities for all spws.

      .. container:: casa-input-box

         setjy(vis='data.ms', field='0')

      For selected spws with field specified by the source name:

      .. container:: casa-input-box

         setjy(vis='data.ms', field='3C286', spw='0,2')

      With a model image:

      .. container:: casa-input-box

         setjy(vis='ngc7538_XBAND.ms', field='0', modimage='3C48_X.im')

      Note that if there is no 3C48_X.im in the current directory, setjy
      looks for it in the default model data image directory.

       An example for a Solar System object as a flux calibrator using
      using data from `the M99
      tutorial <http://casaguides.nrao.edu/index.php?title=CARMA_spectral_line_mosaic_M99>`__
      in CASA Guides:

      .. container:: casa-input-box

         setjy(vis=’c0104I’, field=’MARS’, spw=’0~2’,
         standard=’Butler-JPL-Horizons 2012’)

      To list supported models for the relevant standard, set
      l *istmodels=True* and select standard (no need to set *vis*):

      .. container:: casa-input-box

         setjy(listmodels=True)

      This will show a list of the VLA model images along with their
      full paths to the terminal:

      .. container:: casa-output-box

         | No candidate modimages matching '*.im\* \*.mod*' found in .
         | Candidate modimages (*) in
           /users/ttsutsum/casabuilds/data/nrao/VLA/CalModels:
         | 3C138_A.im 3C138_L.im 3C138_U.im 3C147_C.im 3C147_Q.im
           3C147_X.im 3C286_K.im 3C286_S.im 3C48_A.im  3C48_L.im 
           3C48_U.im
         | 3C138_C.im 3C138_Q.im 3C138_X.im 3C147_K.im 3C147_S.im
           3C286_A.im 3C286_L.im 3C286_U.im 3C48_C.im  3C48_Q.im 
           3C48_X.im
         | 3C138_K.im 3C138_S.im 3C147_A.im 3C147_L.im 3C147_U.im
           3C286_C.im 3C286_Q.im 3C286_X.im 3C48_K.im  3C48_S.im  README

      Similarly, for Solar System objects (e.g.
      *standard='Butler-JPL-Horizons 2012'*), Tb models and new time
      asteroid models are listed by:

      .. container:: casa-input-box

         setjy(standard='Butler-JPL-Horizons 2012', listmodels=True)

      This will show a list looks like below in the terminal:

      .. container:: casa-output-box

         | Tb models of solar system objects available for
           Butler-JPL-Horizons 2012 (*Tb*.dat) in
           /users/ttsutsum/casabuilds/data/alma/SolarSystemModels:
         | Callisto_Tb.dat  Europa_Tb.dat    Io_Tb.dat       
           Jupiter_Tb.dat   Mars_Tb_time.dat Pallas_Tb.dat   
           Uranus_Tb.dat    Vesta_Tb.dat
         | Ceres_Tb.dat     Ganymede_Tb.dat  Juno_Tb.dat     
           Mars_Tb.dat      Neptune_Tb.dat   Titan_Tb.dat    
           Venus_Tb.dat
         | Time variable models of asteroids available for
           Butler-JPL-Horizons 2012 [only applicable for the observation
           date 2015.01.01 0UT and beyond] (*fd_time.dat) in
           /users/ttsutsum/casabuilds/data/alma/SolarSystemModels:
         | Ceres_fd_time.dat   Lutetia_fd_time.dat Pallas_fd_time.dat 
           Vesta_fd_time.dat

.. container:: section
   :name: viewlet-below-content-body
