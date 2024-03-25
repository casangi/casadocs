simobserve -- visibility simulation task -- simulation task
=======================================

Description
---------------------------------------

    This task simulates interferometric or total power measurment sets 
    It is currently optimized for JVLA and ALMA, although many observatories
    are included, and adding your own is simply a matter of providing an
    antenna location file (see below). 
    
    simobserve is meant to work in conjunction with the simanalyze task - 
    Calling simobserve one more times will produce simulated measurement
    set(s), which are then gridded, inverted and deconvolved into output
    simulated images using simanalyze. 
    
    ALMA users are encouraged to use the simalma task, which provides 
    additional information on the multiple simobserve and simanalyze 
    calls required to simulate an ALMA observation which may consist of 
    12m interferometric, 7m interferometric, and 12m total power data.
    
    More information and examples are availible at 
     http://casaguides.nrao.edu/index.php?title=Simulating_Observations_in_CASA
    Please contact CASA experts with any questions.




Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - project
     - :code:`'sim'`
     - 
   * - skymodel
     - :code:`''`
     - 
   * - inbright
     - :code:`''`
     - 
   * - indirection
     - :code:`''`
     - 
   * - incell
     - :code:`''`
     - 
   * - incenter
     - :code:`''`
     - 
   * - inwidth
     - :code:`''`
     - 
   * - complist
     - :code:`''`
     - 
   * - compwidth
     - :code:`'"8GHz"'`
     - 
   * - setpointings
     - :code:`True`
     - 
   * - ptgfile
     - :code:`'$project.ptg.txt'`
     - 
   * - integration
     - :code:`'10s'`
     - 
   * - direction
     - :code:`numpy.array( [  ] )`
     - 
   * - mapsize
     - :code:`numpy.array( [ '','' ] )`
     - 
   * - maptype
     - :code:`'hexagonal'`
     - 
   * - pointingspacing
     - :code:`''`
     - 
   * - caldirection
     - :code:`''`
     - 
   * - calflux
     - :code:`'1Jy'`
     - 
   * - obsmode
     - :code:`'int'`
     - 
   * - refdate
     - :code:`'2014/01/01'`
     - 
   * - hourangle
     - :code:`'transit'`
     - 
   * - totaltime
     - :code:`'7200s'`
     - 
   * - antennalist
     - :code:`''`
     - 
   * - sdantlist
     - :code:`'aca.tp.cfg'`
     - 
   * - sdant
     - :code:`int(0)`
     - 
   * - thermalnoise
     - :code:`'tsys-atm'`
     - 
   * - user_pwv
     - :code:`float(0.5)`
     - 
   * - t_ground
     - :code:`float(270.)`
     - 
   * - t_sky
     - :code:`float(260.)`
     - 
   * - tau0
     - :code:`float(0.1)`
     - 
   * - seed
     - :code:`int(11111)`
     - 
   * - leakage
     - :code:`float(0.0)`
     - 
   * - graphics
     - :code:`'both'`
     - 
   * - verbose
     - :code:`False`
     - 
   * - overwrite
     - :code:`True`
     - 


Parameter Explanations
=======================================



project
---------------------------------------

:code:`'sim'`

root prefix for output file names


skymodel
---------------------------------------

:code:`''`

model image to observe


inbright
---------------------------------------

:code:`''`

scale surface brightness of brightest pixel e.g. "1.2Jy/pixel"


indirection
---------------------------------------

:code:`''`

set new direction e.g. "J2000 19h00m00 -40d00m00"


incell
---------------------------------------

:code:`''`

set new cell/pixel size e.g. "0.1arcsec"


incenter
---------------------------------------

:code:`''`

set new frequency of center channel e.g. "89GHz" (required even for 2D model)


inwidth
---------------------------------------

:code:`''`

set new channel width e.g. "10MHz" (required even for 2D model)


complist
---------------------------------------

:code:`''`

componentlist to observe


compwidth
---------------------------------------

:code:`'"8GHz"'`

bandwidth of components


setpointings
---------------------------------------

:code:`True`




ptgfile
---------------------------------------

:code:`'$project.ptg.txt'`

list of pointing positions


integration
---------------------------------------

:code:`'10s'`

integration (sampling) time


direction
---------------------------------------

:code:`numpy.array( [  ] )`

"J2000 19h00m00 -40d00m00" or "" to center on model


mapsize
---------------------------------------

:code:`numpy.array( [ '','' ] )`

angular size of map or "" to cover model


maptype
---------------------------------------

:code:`'hexagonal'`

hexagonal, square (raster), ALMA, etc


pointingspacing
---------------------------------------

:code:`''`

spacing in between pointings or "0.25PB" or "" for ALMA default INT=lambda/D/sqrt(3), SD=lambda/D/3 


caldirection
---------------------------------------

:code:`''`

pt source calibrator [experimental]


calflux
---------------------------------------

:code:`'1Jy'`




obsmode
---------------------------------------

:code:`'int'`

observation mode to simulate [int(interferometer)|sd(singledish)|""(none)]


refdate
---------------------------------------

:code:`'2014/01/01'`

date of observation - not critical unless concatting simulations


hourangle
---------------------------------------

:code:`'transit'`

hour angle of observation center e.g. "-3:00:00", "5h", "-4.5" (a number without units will be interpreted as hours), or "transit" 


totaltime
---------------------------------------

:code:`'7200s'`

total time of observation or number of repetitions


antennalist
---------------------------------------

:code:`''`

interferometer antenna position file


sdantlist
---------------------------------------

:code:`'aca.tp.cfg'`

single dish antenna position file


sdant
---------------------------------------

:code:`int(0)`

single dish antenna index in file


thermalnoise
---------------------------------------

:code:`'tsys-atm'`

add thermal noise: [tsys-atm|tsys-manual|""]


user_pwv
---------------------------------------

:code:`float(0.5)`

Precipitable Water Vapor in mm


t_ground
---------------------------------------

:code:`float(270.)`

ambient temperature


t_sky
---------------------------------------

:code:`float(260.)`

atmospheric temperature


tau0
---------------------------------------

:code:`float(0.1)`

zenith opacity


seed
---------------------------------------

:code:`int(11111)`

random number seed


leakage
---------------------------------------

:code:`float(0.0)`

cross polarization (interferometer only)


graphics
---------------------------------------

:code:`'both'`

display graphics at each stage to [screen|file|both|none]


verbose
---------------------------------------

:code:`False`




overwrite
---------------------------------------

:code:`True`

overwrite files starting with $project




