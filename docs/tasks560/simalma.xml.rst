simalma -- Simulation task for ALMA -- simulation task
=======================================

Description
---------------------------------------

This task simulates ALMA observation including 12-m, ACA 7-m and total
power arrays, and images and analyzes simulated data.

This task makes multiple calls to simobserve (to calculate
visibilities and total power spectra), followed by gridding of total
power spectra (if total power is requested), concatenation of the
simulated visibilities, calls to the simanalyze task for visibility
inversion and deconvolution and calculation of difference and fidelity
images, and feathering of single dish and interferometric data.

These steps may not all be familiar to new users, so the simalma task
runs by default in a "dryrun" mode, in which it assesses the user's
input parameters and sky model, and prints an informational report
including the required calls to other CASA tasks, both to the screen
and to a text file in the project directory (defined below).

The user can modify their parameters based on the information, then
either run with dryrun=False to actually call the other tasks to
create the simulated data, or run the other tasks individually one at
a time to better understand and control the process.

NOTE The ALMA project is refining the optimal method of combining the
three types of data.  If that best practice is changed after this
release of CASA, the user can control the process by modifying the
calls to the other CASA tasks.



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
   * - dryrun
     - :code:`True`
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
   * - antennalist
     - :code:`numpy.array( [ 'alma.cycle1.1.cfg','aca.cycle1.cfg' ] )`
     - 
   * - hourangle
     - :code:`'transit'`
     - 
   * - totaltime
     - :code:`numpy.array( [ '20min','1h' ] )`
     - 
   * - tpnant
     - :code:`int(0)`
     - 
   * - tptime
     - :code:`'0s'`
     - 
   * - pwv
     - :code:`float(0.5)`
     - 
   * - image
     - :code:`True`
     - 
   * - imsize
     - :code:`numpy.array( [ int(128),int(128) ] )`
     - 
   * - imdirection
     - :code:`''`
     - 
   * - cell
     - :code:`''`
     - 
   * - niter
     - :code:`int(0)`
     - 
   * - threshold
     - :code:`'0.1mJy'`
     - 
   * - graphics
     - :code:`'both'`
     - 
   * - verbose
     - :code:`False`
     - 
   * - overwrite
     - :code:`False`
     - 


Parameter Explanations
=======================================



project
---------------------------------------

:code:`'sim'`

root prefix for output file names


dryrun
---------------------------------------

:code:`True`

dryrun=True will only produce the informative report, not run simobserve/analyze


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


antennalist
---------------------------------------

:code:`numpy.array( [ 'alma.cycle1.1.cfg','aca.cycle1.cfg' ] )`

antenna position files of ALMA 12m and 7m arrays


hourangle
---------------------------------------

:code:`'transit'`

hour angle of observation center e.g. -3:00:00, or "transit"


totaltime
---------------------------------------

:code:`numpy.array( [ '20min','1h' ] )`

total time of observation; vector corresponding to antennalist


tpnant
---------------------------------------

:code:`int(0)`

Number of total power antennas to use (0-4)


tptime
---------------------------------------

:code:`'0s'`

total observation time for total power


pwv
---------------------------------------

:code:`float(0.5)`

Precipitable Water Vapor in mm. 0 for noise-free simulation


image
---------------------------------------

:code:`True`

image simulated data


imsize
---------------------------------------

:code:`numpy.array( [ int(128),int(128) ] )`

output image size in pixels (x,y) or 0 to match model


imdirection
---------------------------------------

:code:`''`

set output image direction, (otherwise center on the model)


cell
---------------------------------------

:code:`''`

cell size with units or "" to equal model


niter
---------------------------------------

:code:`int(0)`

maximum number of iterations (0 for dirty image)


threshold
---------------------------------------

:code:`'0.1mJy'`

flux level (+units) to stop cleaning


graphics
---------------------------------------

:code:`'both'`

display graphics at each stage to [screen|file|both|none]


verbose
---------------------------------------

:code:`False`




overwrite
---------------------------------------

:code:`False`

overwrite files starting with $project




