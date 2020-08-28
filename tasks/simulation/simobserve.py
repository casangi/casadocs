#
# stub function definition file for docstring parsing
#

def simobserve(project='sim', skymodel='', inbright='', indirection='', incell='', incenter='', inwidth='', complist='', compwidth='"8GHz"', comp_nchan=1, setpointings=True, ptgfile='$project.ptg.txt', integration='10s', direction=[''], mapsize=['', ''], maptype='hexagonal', pointingspacing='', caldirection='', calflux='1Jy', obsmode='int', refdate='2014/01/01', hourangle='transit', totaltime='7200s', antennalist='', sdantlist='aca.tp.cfg', sdant=0, outframe='LSRK', thermalnoise='tsys-atm', user_pwv=0.5, t_ground=270., t_sky=260., tau0=0.1, seed=11111, leakage=0.0, graphics='both', verbose=False, overwrite=True):
    r"""
visibility simulation task

Parameters
   - **project** (string) - Root prefix for output file names
   - **skymodel** (string) - model image to observe
   - **complist** (string) - Componentlist to observe
   - **setpointings** (bool) - Calculate a map of pointings?
   - **obsmode** (string) - Observation mode to simulate [int(interferometer)|sd(singledish)|(none)]
   - **outframe** (string) - Spectral frame of MS to create
   - **thermalnoise** (string) - add thermal noise: [tsys-atm|tsys-manual|(none)]
   - **leakage** (double) - Cross polarization (interferometer only)
   - **graphics** (string) - Display graphics at each stage to [screen|file|both|none]
   - **verbose** (bool) - Print extra information to the logger and terminal
   - **overwrite** (bool) - Overwrite existing files in the project subdirectory

Subparameters
   *skymodel != ''*

   - **inbright** (string='') - Peak brightness to scale the image to in Jy/pixel
   - **indirection** (string='') - Set new direction, e.g. J2000 19h00m00 -40d00m00
   - **incell** (string='') - Set new cell/pixel size, e.g. 0.1arcsec
   - **incenter** (string='') - Set new frequency of center channel e.g. 89GHz (required even for 2D model)
   - **inwidth** (string='') - Set new channel width, e.g. "10MHz" (required even for 2D model)

   *complist != ''*

   - **compwidth** (string=8GHz) - Bandwidth of components
   - **comp_nchan** (int=1) - Channelization of components

   *setpointings = True*

   - **integration** (string=10s) - Integration (sampling) time
   - **direction** (stringArray='') - Mosaic center direction, e.g J2000 19h00m00 -40d00m00
   - **mapsize** (stringArray=
        ) - Angular size of mosaic map to simulate.
   - **maptype** (string=ALMA) - how to calculate the pointings for the mosaic observation: hexagonal, square (raster), ALMA, etc.
   - **pointingspacing** (string='') - Spacing in between pointings e.g. 0.25PB. ALMA default: INT=lambda/D/sqrt(3), SD=lambda/D/3 

   *setpointings = False*

   - **ptgfile** (string=$project.ptg.txt) - List of pointing positions
   - **integration** (string=10s) - Integration (sampling) time

   *obsmode = int*

   - **antennalist** (string=alma.out10.cfg) - Interferometer antenna position file
   - **refdate** (string=2014/05/21) - Date of observation. Not critical unless concatting simulations
   - **hourangle** (string=transit) - Hour angle of observation center, e.g. -3:00:00, 5h
   - **totaltime** (string="7200s") - Total time of observation or number of repetitions
   - **caldirection** (string='') - pt source calibrator [experimental]
   - **calflux** (string=1Jy) - pt source calibrator flux [experimental]

   *obsmode = sd*

   - **sdantlist** (string=aca.tp.cfg) - Single dish antenna position file
   - **sdant** (int=0) - Single dish antenna index in file
   - **refdate** (string=2014/05/21) - Date of observation. Not critical unless concatting simulations
   - **hourangle** (string=transit) - Hour angle of observation center, e.g. -3:00:00, 5h
   - **totaltime** (string="7200s") - Total time of observation or number of repetitions

   *obsmode = ''*

   - **antennalist** (string='') - Interferometer antenna position file
   - **sdantlist** (string='') - Single dish antenna position file
   - **sdant** (int=0) - Single dish antenna index in file

   *thermalnoise = tsys-atm*

   - **user_pwv** (double=0.5) - Precipitable Water Vapor in mm
   - **t_ground** (double=269.) - Ground/spillover ambient temperature in K
   - **seed** (int=11111) - Random number seed

   *thermalnoise = tsys-manual*

   - **t_ground** (double=269.) - Ground/spillover ambient temperature in K
   - **t_sky** (double=263.) - Atmospheric temperatur in K
   - **tau0** (double=0.1) - Zenith opacity
   - **seed** (int=11111) - Random number seed


Description
      .. rubric:: Summary
         :name: summary

      This task simulates interferometric or total power
      MeasurementSets. The general steps for simulation in CASA are
      described on the top
      `Simulation <https://casa.nrao.edu/casadocs-devel/stable/simulation>`__
      page. We describe the first two steps in more detail here.

      #. Make a model image or componentlist representation of the sky
         brightness distribution.
      #. Use the **simobserve** task to create a MeasurementSet (uv
         data).

      .. rubric:: Generating a Model Image
         :name: generating-a-model-image

      A "model image" is a CASA image or FITS file that contains a
      representation of the sky brightness distribution, and it
      represents the object to be "observed" in the simulation. There
      are several ways to generate a model image.

      .. rubric:: Starting from an existing FITS image
         :name: starting-from-an-existing-fits-image

      The simplest option is to begin with an existing FITS image. The
      image can be either a single plane (i.e., one observed frequency
      channel) or a cube. A common simulation exercise is to begin with
      a FITS file representing an observation of a target, then scale
      the spatial axes and the flux to shift the data to what would be
      observed for a similar target at a different distance. The
      **simobserve** task has parameters to set the peak flux density,
      coordinates on the sky, pixel size, frequency of the center
      channel, and channel width.

      .. rubric:: Starting from a component list
         :name: starting-from-a-component-list

      .. note:: **WARNING**: **simobserve** does not currently handle component
         lists correctly for single-dish-only simulations. It is advised
         to convert the component list to an image or FITS file.

      It may be useful to simulate observations of an idealized model
      image consisting, for example, of point sources and Gaussians. The
      CASA component list tool (**cl**) allows the user to specify a set
      of point sources, Gaussians, disks, and limb-darkened disks. One
      can then either use that component list directly
      in **simobserve**, or create a CASA image from the components, or
      both. Details can be found in `this CASA
      guide <http://casaguides.nrao.edu/index.php?title=Simulation_Guide_Component_Lists_%28CASA_4.1%29>`__.

      .. rubric:: Starting from a GIF or JPG image
         :name: starting-from-a-gif-or-jpg-image

      A user may wish to convert a GIF or JPG image to a FITS file for
      simulation in CASA. The image should be converted to a 32-bit FITS
      image for use with the CASA sim tools. See `this
      page <http://casaguides.nrao.edu/index.php?title=Convert_jpg_to_fits>`__
      for an example of using gimp to convert a JPG image to a FITS
      file. Alternatively, you could use ImageMagik from the command
      line, like so:

      .. note:: convert myfile.jpg myfile.fits

      Then proceed to trim and convert the file in CASA like so:

      .. note:: | importfits(fitsimage='myfile.fits',imagename='testimage',overwrite=T)
         | default 'immath'
         | imagename = 'testimage'
         | expr = 'IM0'
         | box = '0,0,299,299'
         | outfile = 'testimage2'
         | immath()

      You can use **imhead** to modify the header parameters of the new
      image, or you can use the parameters in the **simobserve** task to
      modify the peak flux density, coordinates on the sky, pixel size,
      frequency of the center channel, and channel width. See the
      discussion below.

       

      .. rubric:: Generating visibilities with simobserve
         :name: generating-visibilities-with-simobserve

      The task **simobserve** takes several steps to generate observed
      visibilities. The major steps are:

      -  Modify Model: If desired, you can modify the header parameters
         in your data model to mimic different observing targets. For
         example, if you start with a model of M100 you might wish to
         scale the axes to simulate an observation of an M100-like
         galaxy that is 4X more distant.
      -  Set Pointings: If the angular size of your model image is
         comparable or larger than the 12-m primary beam, you can
         simulate observing the target as a mosaic. In this step, the
         individual pointings are determined and saved in a text file.
         You can also generate such a text file yourself.
      -  Generate visibilities: The visibilities are determined based on
         the telescope and configuration specified, and the length in
         time of the observation.
      -  Finally, noise can be added to the visibilities. The
         **simobserve** task uses the
         `aatm <http://www.mrao.cam.ac.uk/%7Ebn204/alma/atmomodel.html>`__
         atmospheric model (based on Juan Pardo's
         `ATM <http://cab.inta-csic.es/users/jrpardo/class_atm.html>`__
         library) to simulate real observing conditions. It can corrupt
         the data with thermal noise and atmospheric attenuation.
         Corruption with an atmospheric phase screen, or adding gain
         fluctuations or drift, can be added subsequently using the
         **simulator** tool **sm** as described in `this CASA
         guide. <https://casaguides.nrao.edu/index.php/Corrupt>`__

      For details, please see the descriptions of the individual
      parameters below.

      .. note:: **WARNING**: It is currently not possible to generate a MS in a
         frame other than J2000 e.g., if you set *indirection* to "ICRS
         19h00m00 -40d00m00" it will silently assume that to actually be
         "J2000 19h00m00 -40d00m00". The reference frame can be set to
         ICRS during the imaging or **simanalyze** process.

      .. note:: **WARNING**: when using a simulated MS in **tclean**, it should
         be considered best practice to declare the *phasecenter*
         parameter using the 'J2000 xx:xx:xx.xxx +xxx.xx.xx.xxx'
         notation to account for possible rounding errors that can
         create an offset in the simulated image.

      .. note:: **NOTE**: **simobserve** calls **sm.predict** with
         **sm.setvp** (*dovp=True*). This means that the vpmanager will
         be queried, and a primary beam pattern will be applied,
         according to the telescope name. One can set the primary beam
         for the given telescope using the **vpmanager**. In most
         circumstances, **simobserve** will use synthesis gridding
         (image-plane primary beam application), unless 1) there are
         more than 1 pointing, AND 2) there are more than one antenna
         diameter in the configuration file. In that case it will
         **sm.setoptions** (*ftmachine="mosaic"*) which enables
         heterogenous array simulation for ALMA, ACA, and OVRO
         telescopes.

         Treatment of the primary beam depends critically on parameters
         set in sm.setvp() and sm.setoptions(ftmachine) - see help
         sm.setvp for details. For componentlists, if sm.setvp() is run
         prior to predict, then the spectral variation of each component
         in the componentlist will include the multiplicative term of
         the beam value for each channel frequency. So a flat spectrum
         component will show the frequency variation of the beam in the
         predicted visibilities.

      .. rubric:: Task output
         :name: task-output

       Below is a list of the products produced by the **simobserve**
      task. Not all of these will necessarily be produced, depending on
      input parameters selected.

      .. note:: **NOTE**: To support different runs with different arrays, the
         names have the configuration name from antenna list appended.

      -  [project].[cfg].skymodel = 4D input sky model image
         (optionally) scaled
      -  [project].[cfg].skymodel.flat.regrid.conv = input sky regridded
         to match the output image, and convolved with the output clean
         beam
      -  [project].[cfg].skymodel.png = diagnostic figure of sky model
         with pointings
      -  [project].[cfg].ptg.txt = list of mosaic pointings
      -  [project].[cfg].quick.psf = psf calculated from uv coverage
      -  [project].[cfg].ms = noise-free MeasurementSet
      -  [project].[cfg].noisy.ms = corrupted MeasurementSet
      -  [project].[cfg].observe.png = diagnostic figure of uv coverage
         and visibilities
      -  [project].[cfg].simobserve.last = saved input parameters for
         **simobserve** task

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *project*
         :name: project

      The root filename for all output files. This parameter should be
      set to the same name as used when running **simanalyze** or
      **simalma** for the directory of results generated.

      .. rubric:: *skymodel*
         :name: skymodel

      The input image (used as a model of the sky). **simobserve** uses
      a CASA or FITS image. If you merely have a grid of numbers, you
      will need to write them out as FITS or write a CASA script to read
      them in and use the **ia** tool to create an image and insert the
      data. **simobserve** does NOT require a coordinate system in the
      header. If the coordinate information is incomplete, missing, or
      you would like to override it, set the appropriate "in"
      parameters.

      .. note:: **NOTE**: Setting those parameters simply changes the header
         values, ignoring any values already in the image. No regridding
         is performed.

      You can also manipulate an image header manually with the
      **imhead** task. If you have a proper Coordinate System,
      **simobserve** will do its best to generate visibilities from
      that.

      .. rubric:: *skymodel* expandable parameters
         :name: skymodel-expandable-parameters

      .. rubric:: *inbright*
         :name: inbright

      Scales the model flux densities by setting the peak brightness of
      the britest pixel in Jy/pixel, or '' for unchanged.

      .. note:: **WARNING**: 'unchanged' will take the numerical values in your
         image and assume they are in Jy/pixel, even if it says some
         other unit in the header.

      .. rubric:: *indirection*
         :name: indirection

      The central direction to place the sky model image, or '' to use
      whatever is in the image already.

      .. rubric:: *incell*
         :name: incell

      The spatial pixel size to scale the skymodel image, or '' to use
      whatever is in the image already.

      .. rubric:: *incenter*
         :name: incenter

      The frequency to use for the center channel (or only channel, if
      the skymodel is 2D). Examples: *incenter='89GHz'*, or '' to use
      what is in the header.

      .. rubric:: *inwidth*
         :name: inwidth

      The width of the channels to use, or '' to use what is in the
      image should be a string representing a quantity with units.
      Examples: *inwidth='10MHz'*

      .. note:: **NOTE**: *inwidth* only works reliably with frequencies, not
         velocities.

      .. note:: **NOTE** **2**: It is not possible to change the number of
         spectral planes of the sky model, only to relabel them with
         different frequencies. That kind of regridding can be
         accomplished with the CASA toolkit.

      .. rubric::  
         :name: section

      .. rubric:: *complist*
         :name: complist

      A component list model of the sky, added to or instead of
      *skymodel*.

      .. note:: **WARNING**: **simobserve** does not currently handle component
         lists correctly for single-dish-only simulations. It is advised
         to convert the component list to an image or FITS file.

      .. rubric:: complist expandable parameters
         :name: complist-expandable-parameters

      .. rubric:: *compwidth*
         :name: compwidth

      The bandwidth of components; if simulating from components only,
      this defines the bandwidth of the MS and output images.

      .. rubric:: *comp_nchan*
         :name: comp_nchan

      The number of channels in the output MS. Validated only for a
      positive integer number of channels, this parameter assumes a flat
      spectrum and equal spacing when setting the channel width in the
      output MS. Since variation in channel width as a function of
      frequency is not currently supported, it is not advised to use
      this parameter to simulate observations with spectral index or
      large fractional bandwidth (use a skymodel image instead).

       

      .. rubric:: *setpointings*
         :name: setpointings

      If True, **simobserve** calculates a map of pointings based on a
      set of sub-parameters and generates a pointing file. If False, it
      will read the pointings from the parameter *ptgfile*.

      .. rubric:: *setpointings=True* expandable parameters
         :name: setpointingstrue-expandable-parameters

      .. rubric:: *integration*
         :name: integration

      Sets the time interval for each integration. Also used with
      *setpointings=False*. Examples: *integration='10s'*

      .. note:: **NOTE**: To simulate a 'scan' longer than one integration, use
         *setpointings* to generate a pointing file, and then edit the
         file to increase the time at each point to be larger than the
         parameter integration time.

      .. rubric:: *direction*
         :name: direction

      The mosaic center direction. If left unset, **simobserve** will
      use the center of the skymodel image. Examples: *direction= 'J2000
      19h00m00 -40d00m00';* can optionally be a list of pointings,
      otherwise **simobserve** will cover a region of size *mapsize*
      according to *maptype*.

      .. rubric:: *mapsize*
         :name: mapsize

      The angular size of mosaic map to simulate. Set to '' to cover the
      model image.

      .. rubric:: *maptype*
         :name: maptype

      How to calculate the pointings for the mosaic observation.
      'hexagonal', 'square' (rectangular raster), 'ALMA' for the same
      hex algorithm as the ALMA Cycle 1 OT or 'ALMA2012' for the
      algorithm used in the Cycle 0 OT.

      .. rubric:: *pointingspacing*
         :name: pointingspacing

      Spacing in between primary beams. "0.25PB" to use 1/4 of the
      primary beam FWHM, "nyquist" will use :math:`\lambda/d/2`, '' will
      use :math:`\lambda/d/\sqrt(3)` for INT, :math:`\lambda/d/3` for
      SD.

      .. rubric:: *setpointings=False* expandable parameters
         :name: setpointingsfalse-expandable-parameters

      .. rubric:: *ptgfile*
         :name: ptgfile

      A text file specifying directions in the following format, with
      optional integration times, e.g.,

      ::

         #Epoch     RA          DEC      TIME(optional)
         J2000 23h59m28.10 -019d52m12.35 10.0

      If the time column is not present in the file, it will use
      'integration' for all pointings.

      .. note:: **NOTE**: At this time the file should contain only science
         pointings: **simobserve** will observe these, then optionally
         the calibrator, then the list of science pointings again, etc,
         until totaltime is used up.

       

      .. rubric:: *obsmode*
         :name: obsmode

      Sets the observation mode to calculate visibilities from a
      skymodel image (which may have been modified above), an optional
      component list, and a pointing file (which also may have been
      generated above). This parameter takes two possible values:

      -  interferometer (or int)
      -  singledish (or sd)

      If simulating from a component list, you should specify
      *compwidth*, the desired bandwidth. There is not currently a way
      to specify the spectrum of a component, so simulations from a
      componentlist only will be continuum (1 chan).

      .. rubric:: *obsmode* expandable parameters ('int' or 'sd')
         :name: obsmode-expandable-parameters-int-or-sd

      .. rubric:: *refdate*
         :name: refdate

      The date of simulated observation. Examples:
      *refdate='2014/05/21'*

      .. rubric:: *hourangle*
         :name: hourangle

      The hour angle of observation, given as a string of various
      possible formats. E.g., "-3:00:00", or "5h". The default setting
      for this parameter is *hourangle='transit'*, which is equivalent
      to 0h.

      .. rubric:: *totaltime*
         :name: totaltime

      The total time of an observation. Examples: *totaltime='7200s'* or
      if a number without units, interpreted as the number of times to
      repeat the mosaic.

      .. rubric:: *obsmode='int' expandable parameters*
         :name: obsmodeint-expandable-parameters

      .. rubric:: *antennalist*
         :name: antennalist

      ASCII file containing antenna positions. Each row has x, y, and z
      coordinates and antenna diameter and name; header lines are
      required to specify the observatory name and coordinate system. If
      the configuration file does not include antenna names, the station
      name will be used instead.

      ::

         #observatory=ALMA
         #COFA=-67.75,-23.02
         #coordsys=LOC (local tangent plane)
         # uid___A002_Xdb6217_X55ec_target.ms
         # x             y               z             diam  station  ant 
         -5.850273514   -125.9985379    -1.590364043   12.   A058     DA41
         -19.90369337    52.82680653    -1.892119601   12.   A023     DA42
         13.45860758    -5.790196849    -2.087805181   12.   A035     DA43
         5.606192499     7.646657746    -2.087775605   12.   A001     DA44
         24.10057423    -25.95933768    -2.08466565    12.   A036     DA45

      Standard array configuration files are found in your CASA data
      repository, os.getenv("CASAPATH").split()[0]+"/data/alma/simmos/".
      A string of the form "alma;0.5arcsec" will be parsed into a full
      12m ALMA configuration. If *antennalist=' '*, **simobserve** will
      not produce an interferometric MS. If simulating total power
      observations, be sure to accurately set the parameter
      *sdantlist*. 

      .. rubric:: *caldirection*
         :name: caldirection

      An unresolved calibrator can be observed interleaved with the
      science pointings. The calibrator is implemented as a point source
      clean component with this specified direction and
      flux= *calflux*.

      .. rubric:: *calflux*
         :name: calflux

      Sets the flux density for the calibrator. Default is set to
      *calflux='1Jy'*.

      .. rubric:: *obsmode='sd' expandable parameters*
         :name: obsmodesd-expandable-parameters

      .. rubric:: *sdantlist*
         :name: sdantlist

      Single-dish antenna position file. If simulating total power
      observations, be sure to accurately set the
      parameter *sdantlist*. If this parameter is left unset,
      **simobserve** assumes the default configuration file for a single
      dish simulation (even if the configuration file is explicitly
      specified in *antennalist*). Default: *sdantlist='aca.tp.cfg'.*

      .. rubric:: *sdant*
         :name: sdant

      The index of the antenna in the list to use for total power.
      Defaults to the first antenna on the list (*sdant=0*).
      Heterogeneous total power "arrays" are not currently supported.

      .. rubric:: 
         *thermalnoise*
         :name: thermalnoise

      Adds thermal noise to the synthesized data. This parameter takes
      two possible values (not including unset ' '):

      -  tsys-atm: J. Pardo's ATM library will be used to construct an
         atmospheric profile for the ALMA site: altitude 5000m, ground
         pressure 650mbar, relhum=20%, a water layer of *user_pwv* at
         altitude of 2km, the sky brightness temperature returned by
         ATM, and internally tabulated receiver temperatures
      -  tsys-manual: instead of using the ATM model, specify the zenith
         sky brightness and opacity manually. Noise is added and then
         the visibility flux scale is referenced above the atmosphere. 

      In either mode, noise is calculated using the following
      assumptions:

      -  an antenna spillover efficiency of 0.96,
      -  taper of 0.86,
      -  surface accuracy of 25 and 300 microns for ALMA and EVLA,
         respectively, using the Ruze formula for surface efficiency,
      -  correlator efficiencies of 0.95 and 0.91 for ALMA and EVLA, and
      -  receiver temperatures:

         -  for ALMA: 25, 30, 40, 42, 50, 50, 72, 135, 105, 230 K
            interpolated between 35, 75, 110, 145, 185, 230, 345, 409,
            675, 867 GHz
         -  for EVLA: 500, 70, 60, 55, 100, 130, 350 K interpolated
            between 0.33, 1.47, 4.89, 8.44, 22.5, 33.5, 43.3 GHz
         -  for SMA: 67, 116, 134, 500 K interpolated between 212, 310,
            383, 660 GHz

      These are only approximate numbers and do not take into account
      performance at edges of receiver bands, nor are they guaranteed to
      reflect the most recent measurements. Caveat emptor. Use the
      **sm** tool to add noise if you want more precise control, and use
      the ALMA exposure time calculator for sensitivity numbers in
      proposals.

      .. rubric:: *thermalnoise* expandable parameters
         :name: thermalnoise-expandable-parameters

      .. rubric:: *t_ground*
         :name: t_ground

      The ambient ground/spillover temperature in K.

      .. rubric:: *seed*
         :name: seed

      Random number seed for noise generation.

      .. rubric:: *thermalnoise='tsys-atm'* expandable parameters
         :name: thermalnoisetsys-atm-expandable-parameters

      .. rubric:: *user_pwv*
         :name: user_pwv

      The precipitable water vapor at zenith if constructing an
      atmospheric model.

      .. rubric:: *thermalnoise='tsys-manual'* expandable parameters
         :name: thermalnoisetsys-manual-expandable-parameters

      .. rubric:: *t_sky*
         :name: t_sky

      The atmospheric temperature in K.

      .. rubric:: *tau0*
         :name: tau0

      The zenith opacity at observing frequency. See
      `here <https://casaguides.nrao.edu/index.php/Corrupt>`__ for more
      information on noise, in particular how to add a phase screen
      using the toolkit.

       

      .. rubric:: *leakage*
         :name: leakage

      Adds cross polarization corruption of this fractional magnitude.

      .. rubric:: *graphics*
         :name: graphics

      View plots on the screen, saved to file, both, or neither.

      .. rubric:: *verbose*
         :name: verbose

      Turns on or off the printing of extra information to the logger
      and terminal.

      .. rubric:: *overwrite*
         :name: overwrite

      Overwrites existing files in the project subdirectory. Default:
      False

    """
    pass
