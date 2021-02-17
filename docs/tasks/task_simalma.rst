

.. _Description:

Description
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
   `here <../../notebooks/simulation.ipynb#ALMA-simulations>`__.
   
   .. note:: **NOTE**: The ALMA project is refining the optimal method of
      combining the three types of data. If that best practice is
      changed after this release of CASA, the user can control the
      process by modifying the calls to the other CASA tasks.

   .. rubric:: Parameter descriptions
   
   *project*
   
   The root filename for all output files. A subdirectory will be
   created, and all created files will be placed in that subdirectory
   including the informational report.

   *skymodel*
   
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
   
   If you have a proper Coordinate System, **simalma** will do its
   best to generate visibilities from that, and then create a
   synthesis image
   according to the specified user parameters. You can manipulate
   an image header manually with the **imhead** task.
   
   *inbright*
   
   The peak brightness to scale the image to in Jy/pixel, or " " to
   keep it unchanged.
   
   .. note:: **NOTE**: "unchanged" will take the numerical values in your
      image and assume they are in Jy/pixel, even if it says some
      other unit in the header.   
   
   *indirection*
   
   The central direction to place the sky model image, or " " to use
   whatever is in the image already.
   
   *incell*
   
   The spatial pixel size to scale the skymodel image, or " " to use
   whatever is in the image already.
   
   *incenter*
   
   The frequency to use for the center channel (or only channel, if
   the skymodel is 2D). E.g., "89GHz", or " " to use what is in the
   header. Required even for a 2D model.
   
   *inwidth*
   
   The width of channels to use, or " " to use what is in the image.
   Should be a string representing a quantity with units e.g.,
   "10MHz".
   
   .. note:: **NOTE**: Only works reliably with frequencies, not velocities.
      It is not possible to change the number of spectral planes of
      the sky model, only to relabel them with different frequencies.
      That kind of regridding can be accomplished with the CASA
      toolkit.
   
   *complist*
   
   A component list model of the sky, added to or instead of
   skymodel. Click
   `here <https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.1)>`__
   for more information.
   
   *compwidth*
   
   The bandwidth of components. If simulating from components only,
   this defines the bandwidth of the MS and output images.
   
   *setpointings*
   
   If True, calculate a map of pointings and write *ptgfile*. If
   graphics are on, display the pointings shown on the model image.
   Observations with the ALMA 12m and ACA 7m arrays will observe a
   region of size "mapsize" using the same hexagonal algorithm as the
   ALMA OT, with Nyquist sampling. The total power array maps a
   slightly (+1 primary beam) larger area than the 12m array does, to
   improve later image combination. It samples the region with
   lattice grids of spacing 0.33 lambda/D. If *setpointings=False*,
   read pointings from ptgfile.  
   
   *ptgfile*
   
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
   
   *integration*
   
   Time interval for each integration e.g., '10s'.
   
   .. note:: **NOTE**: To simulate a "scan" longer than one integration, use
      *setpointings* to generate a pointing file, and then edit the
      file to increase the time at each point to be larger than the
      parameter integration time. 
   
   *direction*
   
   Mosaic center direction. e.g., 'J2000 19h00m00 -40d00m00'. If
   unset, will use the center of the skymodel image. Can optionally
   be a list of pointings, otherwise **simobserve** will cover a
   region of size *mapsize* according to *maptype*.
   
   *mapsize*
   
   Angular size of mosaic map to simulate. Set to " " to cover the
   model image.
   
   *antennalist*
   
   A vector of ASCII files containing antenna positions, one for each
   configuration of 7m or 12m dishes.In this task, it should be an
   ALMA configuration. Standard arrays are found in your CASA data
   repository, os.getenv("CASAPATH").split()[0]+"/data/alma/simmos/".
   A string of the form "alma;0.5arcsec" will be parsed into a 12m
   ALMA configuration. Examples:
   ['alma.cycle2.5.cfg','aca.cycle2.i.cfg'],
   ['alma.cycle1;0.3arcsec','alma.cycle1.1.cfg','aca.i.cfg']  
   
   *hourangle*
   
   Hour angle of observation e.g., '-3h'.
   
   *totaltime*
   
   The total time of observations. This should either be a scalar
   time quantity expressed as a string e.g., '1h', '3600sec',
   '10min', or a vector of such quantities, corresponding to the
   elements of the antennalist vector, e.g., ['5min','20min','3h'].
   If you specify a scalar, that will be used for the highest
   resolution 12m configuration in antennalist, and any lower
   resolution 12m configurations, any 7m configurations, and any TP
   configurations will have observing times relative to totaltime of
   0.5, 2,and 4, respectively.  
   
   *tpnant*
   
   The number of total power antennas to use in simulation.  
   
   *tptime*
   
   If *tpnant>0*, the user must specify the observing time for total
   power as a CASA quantity e.g., '4h'.
   
   .. note:: **NOTE**: This is not broken up among multiple days - a 20h
      track will include observations below the horizon,  which is
      probably not what is desired.  
   
   *pwv*
   
   Precipitable water vapor. If constructing an atmospheric model,
   set 0 for noise-free simulation. When *pwv*>0, thermal noise is
   applied to the simulated data. J. Pardo's ATM library will be used
   to construct anatmospheric profile for the ALMA site: altitude
   5000m, ground pressure 650mbar, relhum=20%, a water layer of pwv
   at altitude of 2km, the sky brightness temperature returned by
   ATM, and internally tabulated receiver temperatures. See the
   documentation of **simobserve** for more details.  
   
   *image*
   
   An option to invert and deconvolve the simulated MeasurementSet(s)
   
   .. note:: **NOTE**: Interactive clean or more parameters than the subset
      visible here are available by simply running either **clean**
      or **tclean** tasks directly.
   
   If graphics turned on, display the clean image and residual image
   uses Cotton-Schwab clean for single fields and Mosaic gridding for
   multiple fields (with Clark PSF calculation in minor cycles).  
   
   *imsize*
   
   The image size in spatial pixels (x,y). 0 or -1 will use the model
   image size. Examples: imsize=[500,500]
   
   *imdirection*
   
   The phase center for synthesized image. Default is to center on
   the sky model.
   
   *cell*
   
   Cell size e.g., "10arcsec". *cell = " "* defaults to the skymodel
   cell.
   
   *niter*
   
   The number of clean/deconvolution iterations, 0 for no cleaning.
   
   *threshold*
   
   The flux level at which to stop cleaning.
   
   *graphics*
   
   View plots on the screen, saved to file, both, or neither.
   
   *verbose*
   
   Print extra information to the logger and terminal.
   
   *overwrite*
   
   Overwrite existing files in the project subdirectory. Please see
   the documents of **simobserve** and **simanalyze** for the list of
   outputs produced.
   

.. _Examples:

Examples
   Example of a **simalma** routine. More information on this can be
   seen
   `here <https://casaguides.nrao.edu/index.php/Simalma_(CASA_5.1)>`__.
   
   ::
   
      # Set simalma to default parameters
      default("simalma")

      # Our project name will be "m51", and all simulation products will be placed in a subdirectory "m51/"
      project="m51"
      overwrite=True

      # Model sky = H_alpha image of M51
      os.system('curl https://casaguides.nrao.edu/images/3/3f/M51ha.fits.txt -f -o M51ha.fits')
      skymodel="M51ha.fits"

      # Set model image parameters:
      indirection="J2000 23h59m59.96s -34d59m59.50s"
      incell="0.1arcsec"
      inbright="0.004"
      incenter="330.076GHz"
      inwidth="50MHz"
      antennalist=["alma.cycle5.3.cfg","aca.cycle5.cfg"]
      totaltime="1800s"
      tpnant = 2
      tptime="7200s"
      pwv=0.6
      mapsize="1arcmin"
      dryrun = False
      simalma()
   

.. _Development:

Development
   No additional development details

