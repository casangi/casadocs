simobserve -- visibility simulation task -- simulation task
=======================================

Description
---------------------------------------

This task simulates interferometric or total power measurment sets. It
is currently optimized for JVLA and ALMA, although many observatories
are included, and adding your own is simply a matter of providing an
antenna location file (see below).
    
simobserve is meant to work in conjunction with the simanalyze
task. Calling simobserve one more times will produce simulated
measurement set(s), which are then gridded, inverted and deconvolved
into output simulated images using simanalyze.
    
ALMA users are encouraged to use the simalma task, which provides
additional information on the multiple simobserve and simanalyze calls
required to simulate an ALMA observation which may consist of 12m
interferometric, 7m interferometric, and 12m total power data.
    
More information and examples are availible at 
http://casaguides.nrao.edu/index.php?title=Simulating_Observations_in_CASA
Please contact the Helpdesk with any questions (see
https://casa.nrao.edu/help_desk_all.shtml)



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
     - Root prefix for output file names
   * - skymodel
     - :code:`''`
     - model image to observe
   * - inbright
     - :code:`''`
     - Peak brightness to scale the image to in Jy/pixel
   * - indirection
     - :code:`''`
     - Set new direction, e.g. J2000 19h00m00 -40d00m00
   * - incell
     - :code:`''`
     - Set new cell/pixel size, e.g. 0.1arcsec
   * - incenter
     - :code:`''`
     - Set new frequency of center channel e.g. 89GHz (required even for 2D model)
   * - inwidth
     - :code:`''`
     - Set new channel width, e.g. "10MHz" (required even for 2D model)
   * - complist
     - :code:`''`
     - Componentlist to observe
   * - compwidth
     - :code:`'"8GHz"'`
     - Bandwidth of components
   * - comp_nchan
     - :code:`int(1)`
     - Channelization of components
   * - setpointings
     - :code:`True`
     - Calculate a map of pointings?
   * - ptgfile
     - :code:`'$project.ptg.txt'`
     - List of pointing positions
   * - integration
     - :code:`'10s'`
     - Integration (sampling) time
   * - direction
     - :code:`numpy.array( [  ] )`
     - Mosaic center direction, e.g J2000 19h00m00 -40d00m00
   * - mapsize
     - :code:`numpy.array( [ '','' ] )`
     - Angular size of mosaic map to simulate.
   * - maptype
     - :code:`'hexagonal'`
     - how to calculate the pointings for the mosaic observation: hexagonal, square (raster), ALMA, etc.
   * - pointingspacing
     - :code:`''`
     - Spacing in between pointings e.g. 0.25PB. ALMA default: INT=lambda/D/sqrt(3), SD=lambda/D/3
   * - caldirection
     - :code:`''`
     - pt source calibrator [experimental]
   * - calflux
     - :code:`'1Jy'`
     - pt source calibrator flux [experimental]
   * - obsmode
     - :code:`'int'`
     - Observation mode to simulate [int(interferometer)|sd(singledish)|(none)]
   * - refdate
     - :code:`'2014/01/01'`
     - Date of observation. Not critical unless concatting simulations
   * - hourangle
     - :code:`'transit'`
     - Hour angle of observation center, e.g. -3:00:00, 5h
   * - totaltime
     - :code:`'7200s'`
     - Total time of observation or number of repetitions
   * - antennalist
     - :code:`''`
     - Interferometer antenna position file
   * - sdantlist
     - :code:`'aca.tp.cfg'`
     - Single dish antenna position file
   * - sdant
     - :code:`int(0)`
     - Single dish antenna index in file
   * - outframe
     - :code:`'LSRK'`
     - Spectral frame of MS to create
   * - thermalnoise
     - :code:`'tsys-atm'`
     - add thermal noise: [tsys-atm|tsys-manual|(none)]
   * - user_pwv
     - :code:`float(0.5)`
     - Precipitable Water Vapor in mm
   * - t_ground
     - :code:`float(270.)`
     - Ground/spillover ambient temperature in K
   * - t_sky
     - :code:`float(260.)`
     - Atmospheric temperatur in K
   * - tau0
     - :code:`float(0.1)`
     - Zenith opacity
   * - seed
     - :code:`int(11111)`
     - Random number seed
   * - leakage
     - :code:`float(0.0)`
     - Cross polarization (interferometer only)
   * - graphics
     - :code:`'both'`
     - Display graphics at each stage to [screen|file|both|none]
   * - verbose
     - :code:`False`
     - Print extra information to the logger and terminal
   * - overwrite
     - :code:`True`
     - Overwrite existing files in the project subdirectory


Parameter Explanations
=======================================



project
---------------------------------------

:code:`'sim'`

root prefix for output file names


skymodel
---------------------------------------

:code:`''`

Model image to observe

                   * simobserve uses a CASA or fits image. If you
                     merely have a grid of numbers, you will need to
                     write them out as fits or write a CASA script to
                     read them in and use the ia tool to create an
                     image and insert the data.

                   * simobserve does NOT require a coordinate system
                     in the header. If the coordinate information is
                     incomplete, missing, or you would like to
                     override it, set the appropriate "in"
                     parameters. NOTE that setting those parameters
                     simply changes the header values, ignoring any
                     values already in the image. No regridding is
                     performed. 

                   * You can also manipulate an image header manually
                     with the "imhead" task. 

                   * If you have a proper Coordinate System,
                     simobserve will do its best to generate
                     visibilities from that. 



inbright
---------------------------------------

:code:`''`

Peak brightness to scale the image to, in Jy/pixel
                     Subparameter of skymodel
                     Default: '' (i.e., unchanged)

                        Example: inbright='1.2Jy/pixel'

                     Note: "unchanged" will take the numerical values
                     in your image and assume they are in Jy/pixel,
                     even if it says some other unit in the header. 



indirection
---------------------------------------

:code:`''`

Central direction to place the sky model image
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)

                        Example: indirection='J2000 19h00m00
                        -40d00m00'



incell
---------------------------------------

:code:`''`

set new cell/pixel size
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)

                        Example: incell='0.1arcsec'



incenter
---------------------------------------

:code:`''`

Frequency to use for the center channel (or only channel,
if the skymodel is 2D)
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)

                        Example: incenter='89GHz'



inwidth
---------------------------------------

:code:`''`

Set new channel width 
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)
                     
                     Should be a string representing a quantity with
                     units e.g. inwidth='10MHz'

                     NOTES: 
                   * Only works reliably with frequencies, not
                     velocities 
                   * It is not possible to change the number of
                     spectral planes of the sky model, only to relabel
                     them with different frequencies That kind of
                     regridding can be accomplished with the CASA
                     toolkit.



complist
---------------------------------------

:code:`''`

Component list model of the sky, added to or instead of skymodel. See https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.4)



compwidth
---------------------------------------

:code:`'"8GHz"'`

Bandwidth of components
                     Subparameter of complist

                     If simulating from components only, this defines
                     the bandwidth of the MS and output images

                        Example: compwidth='8GHz'



comp_nchan
---------------------------------------

:code:`int(1)`

Channelization of components
                     Subparameter of complist

                     If simulating from components only, this defines
                     the number of channels of the MeasurementSet

                        Example: comp_nchan=256



setpointings
---------------------------------------

:code:`True`

If true, calculate a map of pointings and write ptgfile. If false, read pointings from ptgfile.
                     Default: True

                     If graphics are on, display the pointings shown
                     on the model image



ptgfile
---------------------------------------

:code:`'$project.ptg.txt'`

A text file specifying directions
                     Subparameter of setpointings=False
                     
                     The text file should have the following format,
                     with optional integration times:
                     Epoch     RA          DEC      TIME(optional)
                     J2000 23h59m28.10 -019d52m12.35 10.0

                     If the time column is not present in the file, it
                     will use "integration" for all pointings.

                     NOTE: at this time the file should contain only
                     science pointings: simobserve will observe these,
                     then optionally the calibrator, then the list of
                     science pointings again, etc, until totaltime is
                     used up.
 


integration
---------------------------------------

:code:`'10s'`

Time interval for each integration
                     Subparameter of setpointings=False

                        Example: integration='10s'

                     NOTE: to simulate a "scan" longer than one
                     integration, use  setpointings to generate a
                     pointing file, and then edit the file to increase
                     the time at each point to be larger than the
                     parameter integration time.



direction
---------------------------------------

:code:`numpy.array( [  ] )`

Mosaic center direction.
                     Subparameter of setpointings=True

                        Example: "J2000 19h00m00 -40d00m00" or "" to
                        center on model

                     If unset, will use the center of the skymodel
                     image.
                   * can optionally be a list of pointings, otherwise
                   * simobserve will cover a region of size mapsize
                     according to maptype



mapsize
---------------------------------------

:code:`numpy.array( [ '','' ] )`

Angular size of of mosaic map to simulate.
                     Subparameter of setpointings=True

                     Set to "" to cover model



maptype
---------------------------------------

:code:`'hexagonal'`

How to calculate the pointings for the mosaic
observation?
                     Subparameter of setpointings=True
                     Options: hexagonal, square (raster), ALMA, etc

                     "ALMA" for the same hex algorithm as the ALMA
                     Cycle 1 OT or "ALMA2012" for the algorithm used
                     in the Cycle 0 OT



pointingspacing
---------------------------------------

:code:`''`

Spacing in between pointings. 
                     Subparameter of setpointings=True

                        Examples: 
                        pointingspacing="0.25PB" 
                        pointingspacing="" for ALMA default
                        INT=lambda/D/sqrt(3), SD=lambda/D/3 



caldirection
---------------------------------------

:code:`''`

pt source calibrator [experimental]


calflux
---------------------------------------

:code:`'1Jy'`

pt source calibrator flux [experimental]


obsmode
---------------------------------------

:code:`'int'`

Observation mode to simulate
                     Options: int(interferometer)|sd(singledish)|""(none)

                     Observation mode to calculate visibilities from a
                     skymodel image (which may have been modified
                     above), an optional component list, and a
                     pointing file (which also may have been generated
                     above).

                     This parameter takes two possible values:
                     - interferometer (or int)
                     - singledish (or sd)
                   * If graphics are on, this observe step will
                     display the array (similar to plotants), the uv
                     coverage, the synthesized (dirty) beam, and
                     ephemeris information 
                   * If simulating from a component list, you should
                     specify "compwidth", the desired bandwidth; and 
		     specify "comp_nchan", the desired channelization
		     if more than one output channel is desired



refdate
---------------------------------------

:code:`'2014/01/01'`

Date of simulated observation
                     Subparameter of obsmode='int|sd'
                     Not critical unless concatting simulations

                        Example: refdate="2014/05/21"



hourangle
---------------------------------------

:code:`'transit'`

Hour angle of observation center.
                     Subparameter of obsmode='int|sd'

                         Examples:
                         hourangle="-3:00:00", "5h", or "transit"
 


totaltime
---------------------------------------

:code:`'7200s'`

Total time of observation or number of repetitions
                     Subparameter of obsmode='int|sd'

                         Example:
                         totaltime='7200s'
                         If a number without units, interpreted as the
                         number of times to repeat the mosaic.



antennalist
---------------------------------------

:code:`''`

Text file containing antenna positions.
                     Subparameter of obsmode='int|""'

                     Each row has x y z coordinates and antenna diameter
		     with optional station name and antenna name.
		     Header lines are required to specify:
                     # observatory=ALMA
                     # coordsys=UTM

		     If the Universal Transverse Mercator projection is
		     specified, then other keywords are required:
                     # datum=WGS84
                     # zone=19
		     # hemisphere=S

		     If the observatory keyword is not defined, then the
		     COFA keyword should be, using a coordinate pair:
		     #COFA=-67.75,-23.02

                   * Standard array configurations are found in your
		     CASA data repository,
                   * If "", simobserve will not not produce an
                     interferometric MS 
                   * A string of the form "alma;0.5arcsec" will be
                   parsed into a full 12m ALMA configuration.  



sdantlist
---------------------------------------

:code:`'aca.tp.cfg'`

single dish antenna position file
                     Subparameter of obsmode='sd|""'



sdant
---------------------------------------

:code:`int(0)`

Index of the antenna in the list to use for total power.  
                     Subparameter of obsmode='sd|""'
                     Default: first antenna on the list. 



outframe
---------------------------------------

:code:`'LSRK'`

spectral frame of MS to create
                     Subparameter of obsmode='sd|""'



thermalnoise
---------------------------------------

:code:`'tsys-atm'`

add thermal noise.
                     Options: tsys-atm, tsys-manual, ""

                     This parameter accepts two settings:
                     - tsys-atm: J. Pardo's ATM library will be used
                     to construct an atmospheric profile for the ALMA
                     site: altitude 5000m, ground pressure 650mbar,
                     relhum=20%, a water layer of user_pwv at altitude
                     of 2km, the sky brightness temperature returned
                     by ATM, and internally tabulated receiver
                     temperatures.
                     - tsys-manual: instead of using the ATM model,
                     specify the zenith  sky brightness and opacity
                     manually.  Noise is added and then the visibility
                     flux scale is referenced above the atmosphere.

                     If left unset (empty string) no thermalnoise
                     corruption is performed.
 
                     In either mode, noise is calculated using an
                     antenna spillover efficiency of 0.96, taper of
                     0.86, surface accuracy of 25 and 300 microns for
                     ALMA and EVLA respectively (using the Ruze
                     formula for surface efficiency), correlator
                     efficiencies of 0.95 and 0.91 for ALMA and EVLA,
                     receiver temperatures 
                     for ALMA of 17, 30, 37, 51, 65,
                     83,147,196,175,230 K interpolated between 35,
                     75,110,145,185,230,345,409,675,867 GHz, 
                     for EVLA of 500, 70,  60,  55,  100, 130, 350 K
                     interpolated between
                     0.33,1.47,4.89,8.44,22.5,33.5,43.3 GHz, 
                     for SMA of 67,  116, 134, 500 K interpolated
                     between 212.,310.,383.,660. GHz.

                     Note: These are only approximate numbers and do
                     not take into account performance at edges of
                     receiver bands, neither are they guaranteed to
                     reflect the most recent measurements.  Caveat
                     emptor. Use the sm tool to add noise if you want
                     more precise control, and use the ALMA exposure
                     time calculator for sensitivity numbers in
                     proposals.



user_pwv
---------------------------------------

:code:`float(0.5)`

Precipitable water vapor if constructing an atmospheric
model (in mm)
                      Subparameter of thermalnoise='tsys-atm'



t_ground
---------------------------------------

:code:`float(270.)`

Ground/spillover temperature in K
                      Subparameter of
                      thermalnoise='tsys-atm|tsys-manual'



t_sky
---------------------------------------

:code:`float(260.)`

Atmospheric temperature in K
                      Subparameter of thermalnoise='tsys-manual'



tau0
---------------------------------------

:code:`float(0.1)`

Zenith opacity at observing frequency
                      Subparameter of thermalnoise='tsys-manual'

                      https://casaguides.nrao.edu/index.php/Corrupt
                      for more information on noise, in particular how
                      to add a phase screen using the toolkit



seed
---------------------------------------

:code:`int(11111)`

Random number seed
                      Subparameter of
                      thermalnoise='tsys-atm|tsys-manual'



leakage
---------------------------------------

:code:`float(0.0)`

add cross polarization corruption of this fractional
magnitude (interferometer only)



graphics
---------------------------------------

:code:`'both'`

View plots on the screen, saved to file, both, or neither
                     Options: screen|file|both|none



verbose
---------------------------------------

:code:`False`

Print extra information to the logger and terminal
                     Default: False
                     Options: True|False



overwrite
---------------------------------------

:code:`True`

Overwrite files starting with $project
                     Default: False
                     Options: True|False





