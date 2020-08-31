#
# stub function definition file for docstring parsing
#

def simalma(project='sim', dryrun=True, skymodel='', inbright='', indirection='', incell='', incenter='', inwidth='', complist='', compwidth='"8GHz"', setpointings=True, ptgfile='$project.ptg.txt', integration='10s', direction=[''], mapsize=['', ''], antennalist=['alma.cycle1.1.cfg', 'aca.cycle1.cfg'], hourangle='transit', totaltime=['20min', '1h'], tpnant=0, tptime='0s', pwv=0.5, image=True, imsize=[128, 128], imdirection='', cell='', niter=0, threshold='0.1mJy', graphics='both', verbose=False, overwrite=False):
    r"""
Simulation task for ALMA 

Parameters
   - **project** (string) - root prefix for output file names
   - **dryrun** (bool) - dryrun=True will only produce the informative report, not run simobserve/analyze
   - **skymodel** (string) - model image to observe
   - **complist** (string) - componentlist to observe
   - **setpointings** (bool)
   - **antennalist** (stringArray) - antenna position files of ALMA 12m and 7m arrays
   - **hourangle** (string) - hour angle of observation center e.g. -3:00:00, or "transit"
   - **totaltime** (stringArray) - total time of observation; vector corresponding to antennalist
   - **tpnant** (int) - Number of total power antennas to use (0-4)
   - **pwv** (double) - Precipitable Water Vapor in mm. 0 for noise-free simulation
   - **image** (bool) - image simulated data
   - **graphics** (string) - display graphics at each stage to [screen|file|both|none]
   - **verbose** (bool)
   - **overwrite** (bool) - overwrite files starting with $project

Subparameters
   .. raw:: html

      <details><summary><i> skymodel != '' </i></summary>

   - **inbright** (string='') - scale surface brightness of brightest pixel e.g. "1.2Jy/pixel"
   - **indirection** (string='') - set new direction e.g. "J2000 19h00m00 -40d00m00"
   - **incell** (string='') - set new cell/pixel size e.g. "0.1arcsec"
   - **incenter** (string='') - set new frequency of center channel e.g. "89GHz" (required even for 2D model)
   - **inwidth** (string='') - set new channel width e.g. "10MHz" (required even for 2D model)

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> complist != '' </i></summary>

   - **compwidth** (string=8GHz) - bandwidth of components

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> setpointings = True </i></summary>

   - **integration** (string=10s) - integration (sampling) time
   - **direction** (stringArray='') - "J2000 19h00m00 -40d00m00" or "" to center on model
   - **mapsize** (stringArray=
        ) - angular size of map or "" to cover model

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> setpointings = False </i></summary>

   - **ptgfile** (string=$project.ptg.txt) - list of pointing positions
   - **integration** (string=10s) - integration (sampling) time

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> tpnant != 0 </i></summary>

   - **tptime** (string=0s) - total observation time for total power

   .. raw:: html

      </details>

   .. raw:: html

      <details><summary><i> image = True </i></summary>

   - **imsize** (intArray=0) - output image size in pixels (x,y) or 0 to match model
   - **imdirection** (string='') - set output image direction, (otherwise center on the model)
   - **cell** (string='') - cell size with units or "" to equal model
   - **niter** (int=0) - maximum number of iterations (0 for dirty image)
   - **threshold** (string=0.1mJy) - flux level (+units) to stop cleaning

   .. raw:: html

      </details>


Description
      .. rubric:: Summary
         :name: summary

      This task simulates ALMA observation including 12-m, ACA 7-m and
      total power arrays, and images and analyzes simulated data.

      This task makes multiple calls to **simobserve** (to calculate
      visibilities and total power spectra), followed by gridding of
      total power spectra (if total power is requested), concatenation
      of the simulated visibilities, calls to the **simanalyze** task
      for visibility inversion, deconvolution, and calculation of
      difference, and fidelity images, and feathering of single dish and
      interferometric data.

      These steps may not all be familiar to new users, so the
      **simalma** task runs by default in a "dryrun" mode, in which it
      assesses the user's input parameters and sky model, and prints an
      informational report including the required calls to other CASA
      tasks, both to the screen and to a text file in the project
      directory (defined below).

      The user can modify their parameters based on the information,
      then either run with *dryrun=False* to actually call the other
      tasks to create the simulated data, or run the other tasks
      individually one at a time to better understand and control the
      process. More information on running **simalma** can be found
      `here <https://casa.nrao.edu/casadocs-devel/stable/simulation/simalma>`__.

      .. note:: **NOTE**: The ALMA project is refining the optimal method of
         combining the three types of data. If that best practice is
         changed after this release of CASA, the user can control the
         process by modifying the calls to the other CASA tasks.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *project*
         :name: project

      The root filename for all output files. A subdirectory will be
      created, and all created files will be placed in that subdirectory
      including the informational report.

      .. rubric:: *skymodel
         *
         :name: skymodel

      An input image used as a model of the sky. **simalma** requires a
      CASA or FITS image. If you merely have a grid of numbers, you will
      need to write them out as FITS or write a CASA script to read them
      in and use the **image** (**ia**) tool to create an image and
      insert the data. **simalma** does NOT require a coordinate system
      in the header. If the coordinate information is incomplete,
      missing, or you would like to override it, set the appropriate
      "in" parameters.

      .. note:: **NOTE**: Setting those parameters simply changes the header
         values, ignoring any values already in the image. No regridding
         is performed.

      | If you have a proper Coordinate System, **simalma** will do its
        best to generate visibilities from that, and then create a
        synthesis image
      | according to the specified user parameters. You can manipulate
        an image header manually with the **imhead** task.  

      .. rubric:: *inbright
         *
         :name: title1

      The peak brightness to scale the image to in Jy/pixel, or " " to
      keep it unchanged.

      .. note:: **NOTE**: "unchanged" will take the numerical values in your
         image and assume they are in Jy/pixel, even if it says some
         other unit in the header.   

      .. rubric:: *indirection
         *
         :name: indirection

      The central direction to place the sky model image, or " " to use
      whatever is in the image already.

      .. rubric:: *incell
         *
         :name: incell

      The spatial pixel size to scale the skymodel image, or " " to use
      whatever is in the image already.

      .. rubric:: *incenter
         *
         :name: incenter

      The frequency to use for the center channel (or only channel, if
      the skymodel is 2D). E.g., "89GHz", or " " to use what is in the
      header. Required even for a 2D model.

      .. rubric:: *inwidth
         *
         :name: inwidth

      The width of channels to use, or " " to use what is in the image.
      Should be a string representing a quantity with units e.g.,
      "10MHz".

      .. note:: **NOTE**: Only works reliably with frequencies, not velocities.
         It is not possible to change the number of spectral planes of
         the sky model, only to relabel them with different frequencies.
         That kind of regridding can be accomplished with the CASA
         toolkit.

      .. rubric:: *complist
         *
         :name: complist

      A component list model of the sky, added to or instead of
      skymodel. Click
      `here <https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.1)>`__
      for more information.

      .. rubric:: *compwidth
         *
         :name: compwidth

      The bandwidth of components. If simulating from components only,
      this defines the bandwidth of the MS and output images.

      .. rubric:: *setpointings
         *
         :name: setpointings

      If True, calculate a map of pointings and write *ptgfile*. If
      graphics are on, display the pointings shown on the model image.
      Observations with the ALMA 12m and ACA 7m arrays will observe a
      region of size "mapsize" using the same hexagonal algorithm as the
      ALMA OT, with Nyquist sampling. The total power array maps a
      slightly (+1 primary beam) larger area than the 12m array does, to
      improve later image combination. It samples the region with
      lattice grids of spacing 0.33 lambda/D. If *setpointings=False*,
      read pointings from ptgfile.  

      .. rubric:: *ptgfile
         *
         :name: ptgfile

      A text file specifying directions in the same format as the
      example, and optional integration times, e.g.,

      ::

         #Epoch     RA          DEC      TIME(optional)
         J2000 23h59m28.10 -019d52m12.35 10.0

      If the time column is not present in the file, it will use
      "integration" for all pointings.

      .. note:: **NOTE**: At this time the file should contain only science
         pointings. **simalma** will observe these until totaltime is
         used up. 

      .. rubric:: *integration
         *
         :name: integration

      Time interval for each integration e.g., '10s'.

      .. note:: **NOTE**: To simulate a "scan" longer than one integration, use
         *setpointings* to generate a pointing file, and then edit the
         file to increase the time at each point to be larger than the
         parameter integration time. 

      .. rubric:: *direction
         *
         :name: direction

      Mosaic center direction. e.g., 'J2000 19h00m00 -40d00m00'. If
      unset, will use the center of the skymodel image. Can optionally
      be a list of pointings, otherwise **simobserve** will cover a
      region of size *mapsize* according to *maptype*.

      .. rubric:: *mapsize
         *
         :name: mapsize

      Angular size of mosaic map to simulate. Set to " " to cover the
      model image.

      .. rubric:: *antennalist
         *
         :name: antennalist

      A vector of ASCII files containing antenna positions, one for each
      configuration of 7m or 12m dishes.In this task, it should be an
      ALMA configuration. Standard arrays are found in your CASA data
      repository, os.getenv("CASAPATH").split()[0]+"/data/alma/simmos/".
      A string of the form "alma;0.5arcsec" will be parsed into a 12m
      ALMA configuration. Examples:
      ['alma.cycle2.5.cfg','aca.cycle2.i.cfg'],
      ['alma.cycle1;0.3arcsec','alma.cycle1.1.cfg','aca.i.cfg']  

      .. rubric:: *hourangle
         *
         :name: hourangle

      Hour angle of observation e.g., '-3h'.

      .. rubric:: *totaltime
         *
         :name: totaltime

      The total time of observations. This should either be a scalar
      time quantity expressed as a string e.g., '1h', '3600sec',
      '10min', or a vector of such quantities, corresponding to the
      elements of the antennalist vector, e.g., ['5min','20min','3h'].
      If you specify a scalar, that will be used for the highest
      resolution 12m configuration in antennalist, and any lower
      resolution 12m configurations, any 7m configurations, and any TP
      configurations will have observing times relative to totaltime of
      0.5, 2,and 4, respectively.  

      .. rubric:: *tpnant
         *
         :name: tpnant

      The number of total power antennas to use in simulation.  

      .. rubric:: *tptime
         *
         :name: tptime

      If *tpnant>0*, the user must specify the observing time for total
      power as a CASA quantity e.g., '4h'.

      .. note:: **NOTE**: This is not broken up among multiple days - a 20h
         track will include observations below the horizon,  which is
         probably not what is desired.  

      .. rubric:: *pwv
         *
         :name: pwv

      Precipitable water vapor. If constructing an atmospheric model,
      set 0 for noise-free simulation. When *pwv*>0, thermal noise is
      applied to the simulated data. J. Pardo's ATM library will be used
      to construct anatmospheric profile for the ALMA site: altitude
      5000m, ground pressure 650mbar, relhum=20%, a water layer of pwv
      at altitude of 2km, the sky brightness temperature returned by
      ATM, and internally tabulated receiver temperatures. See the
      documentation of **simobserve** for more details.  

      .. rubric:: *image
         *
         :name: image

      An option to invert and deconvolve the simulated MeasurementSet(s)

      .. note:: **NOTE**: Interactive clean or more parameters than the subset
         visible here are available by simply running either **clean**
         or **tclean** tasks directly.

      If graphics turned on, display the clean image and residual image
      uses Cotton-Schwab clean for single fields and Mosaic gridding for
      multiple fields (with Clark PSF calculation in minor cycles).  

      .. rubric:: *imsize
         *
         :name: imsize

      The image size in spatial pixels (x,y). 0 or -1 will use the model
      image size. Examples: imsize=[500,500]

      .. rubric:: *imdirection
         *
         :name: imdirection

      The phase center for synthesized image. Default is to center on
      the sky model.

      .. rubric:: *cell
         *
         :name: title1

      Cell size e.g., "10arcsec". *cell = " "* defaults to the skymodel
      cell.

      .. rubric:: *niter
         *
         :name: niter

      The number of clean/deconvolution iterations, 0 for no cleaning.

      .. rubric:: *threshold
         *
         :name: title1

      The flux level at which to stop cleaning.

      .. rubric:: *graphics
         *
         :name: title1

      View plots on the screen, saved to file, both, or neither.

      .. rubric:: *verbose*
         :name: verbose

      Print extra information to the logger and terminal.

      .. rubric:: *overwrite*
         :name: overwrite

      Overwrite existing files in the project subdirectory. Please see
      the documents of **simobserve** and **simanalyze** for the list of
      outputs produced.

    """
    pass
