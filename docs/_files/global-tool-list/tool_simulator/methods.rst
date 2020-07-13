Methods
=======

.. container:: documentDescription description

   task applycal parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-methods

          

         .. container:: param

            constructor **simulator**

            .. container:: collcontent

               .. container:: methoddesc

                  Create a simulator tool.

               .. container:: methodsection

                  Parameters : None

               .. container:: methodsection

                  Example

               .. container:: methodexam

                  # create a simulator tool mysim = smtool();

         .. container:: param

            function **open**

            .. container:: collcontent

               .. container:: methoddesc

                  A simulator tool can either operate on an existing
                  MeasurementSet, predicting and/or corrupting data on
                  the existing uvw coordinates -- to do that open the MS
                  with sm.openfromms(msname). or it can be used to
                  create a new MeasurementSet from descriptions of the
                  array configuration and the observational parameters
                  -- to create a new MS, use this method
                  sm.open(msname). You will also need to run setconfig,
                  setfield, setspw, setspwindow, setfeed, and settimes.
                  Creating the actual (empty) MS is accomplished with
                  sm.observe. Data can be subsequently sm.predict-ed and
                  sm.corrupt-ed. NOTE: sm.predict assumes the model
                  image units are Jy/pixel, and in fact will overwrite
                  the brightness units of the image itself!

               .. container:: methodsection

                  Parameters

               .. container:: parameters2

                  ms : undefined

               .. container:: methodparmtable

                  MeasurementSet to be created

.. container:: methodsection

   Example

.. container:: methodexam

   In this example, we read in the antenna coordinates from an ASCII
   file, and simulate a single-pointing VLA observation with a
   calibrator. Note that no primary beam attenuation will be applied
   (see sm.setvp). tabname = 'VLAC.LOCAL.TAB' asciifile =
   'VLAC.LOCAL.STN' mytab=table.create() mytab.fromascii(tabname,
   asciifile); xx=[]; yy:=[]; zz:=[]; diam:=[]; xx = mytab.getcol('X');
   yy = mytab.getcol('Y'); zz = mytab.getcol('Z'); diam =
   mytab.getcol('DIAM'); # sm.open('NEW1.ms') # do configuration posvla
   = me.observatory('vla'); # me.observatory('ALMA') also works!
   sm.setconfig(telescopename='VLA', x=xx, y=yy, z=zz,
   dishdiameter=diam, mount='alt-az', antname='VLA',
   coordsystem='local', referencelocation=posvla); # Initialize the
   spectral windows sm.setspwindow(spwname='CBand', freq='5GHz',
   deltafreq='50MHz', freqresolution='50MHz', nchannels=1, stokes='RR RL
   LR LL'); sm.setspwindow(spwname='LBand', freq='1.420GHz',
   deltafreq='3.2MHz', freqresolution='3.2MHz', nchannels=32, stokes='RR
   LL'); # Initialize the source and calibrater
   sm.setfield(sourcename='My cal',
   sourcedirection=['J2000','00h0m0.0','+45.0.0.000'], calcode='A');
   sm.setfield(sourcename='My source',
   sourcedirection=['J2000','01h0m0.0','+47.0.0.000']);
   sm.setlimits(shadowlimit=0.001, elevationlimit='8.0deg');
   sm.setauto(autocorrwt=0.0); sm.settimes(integrationtime='10s',
   usehourangle=F, referencetime=me.epoch('utc', 'today'));
   sm.observe('My cal', 'LBand', starttime='0s', stoptime='300s');
   sm.observe('My source', 'LBand', starttime='310s', stoptime='720s');
   sm.observe('My cal', 'CBand', starttime='720s', stoptime='1020s');
   sm.observe('My source', 'CBand', starttime='1030s',
   stoptime='1500s'); sm.setdata(spwid=1, fieldid=1);
   sm.predict(imagename='M31.MOD'); sm.setdata(spwid=2, fieldid=2);
   sm.predict(imagename='BigLBand.MOD'); sm.close();

.. container:: param

   function **openfromms**

   .. container:: collcontent

      .. container:: methoddesc

         A simulator tool can either operate on an existing
         MeasurementSet, predicting and/or corrupting data on the
         existing uvw coordinates - to do that open the MS with
         sm.openfromms(msname) or it can be used to create a new
         MeasurementSet from descriptions of the array configuration and
         the observational parameters. - to create a new MS, use
         sm.open(msname). NOTE: sm.predict assumes the model image units
         are Jy/pixel, and in fact will overwrite the brightness units
         of the image itself!

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         ms : undefined

      .. container:: methodparmtable

         MeasurementSet to be processed

.. container:: methodsection

   Example

.. container:: methodexam

   sm.openfromms('3C273XC1.MS'); sm.predict('3C273XC1.imagename');
   sm.setnoise(simplenoise='10mJy'); sm.setgain(interval='100s',
   amplitude=0.01); sm.corrupt(); sm.close();

.. container:: param

   function **close**

   .. container:: collcontent

      .. container:: methoddesc

         Close tools and write data to disk. This is a synonym for done.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **done**

   .. container:: collcontent

      .. container:: methoddesc

         Close tools and write data to disk. This is a synonym for done.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **name**

   .. container:: collcontent

      .. container:: methoddesc

         Returns the name of the attached MeasurementSet.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **summary**

   .. container:: collcontent

      .. container:: methoddesc

         Writes a summary of the currently set properties to the default
         logger.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **type**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns the string \`Simulator'. It is used so
         that in a script, you can make sure this variable is a
         simulator tool.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **settimes**

   .. container:: collcontent

      .. container:: methoddesc

         This method sets values to be used in sm.observe. If
         usehourangle=False, the start and stop times in sm.observe are
         referenced to referencetime. If usehourangle=True, then in
         sm.observe, starttime/stoptime will be interpreted as
         startha/stopha. In that case, the start and stop times are
         calculated such that the start time is later than the reference
         time, but less than one day later. The hour angles refer to the
         first source observed.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         integrationtime : any = 10s

      .. container:: methodparmtable

         Integration time

.. container:: parameters2

   usehourangle : undefined = true

.. container:: methodparmtable

   Use starttime/stoptime as hour angles - else they are referenced to
   referencetime

.. container:: parameters2

   referencetime : any = 50000.0d

.. container:: methodparmtable

   Reference time for starttime and stoptime. Epoch Measure . E.g
   me.epoch('UTC', '50000.0d')

.. container:: param

   function **observe**

   .. container:: collcontent

      .. container:: methoddesc

         Observe a given source with a given spectral window for the
         specified times, including start, stop, integration, and gap
         times. If usehourangle=False (set with settimes), the start and
         stop times are referenced to referencetime. If
         userhourangle=True, starttime/stoptime are interpreted as
         startha/stopha, the start and stop times are calculated such
         that the start time is later than the reference time, but less
         than one day later, and the hour angles refer to the first
         source observed. setconfig, setspwindow, setfeed, and setfield
         must be run before observe can be run. See also sm.observemany

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         sourcename : undefined

      .. container:: methodparmtable

         Name of source or field (must be specified)

.. container:: parameters2

   spwname : undefined

.. container:: methodparmtable

   Unique user-supplied name for this spectral window

.. container:: parameters2

   starttime : any = 0s

.. container:: methodparmtable

   Start time referenced to referencetime, or start hour angle

.. container:: parameters2

   stoptime : any = 3600s

.. container:: methodparmtable

   Stop time referenced to referencetime, or stop hour angle

.. container:: parameters2

   add_observation : undefined = false

.. container:: methodparmtable

   Add a new line to the OBSERVATION subtable for this call

.. container:: parameters2

   state_sig : undefined = true

.. container:: methodparmtable

   a new line will be added to STATE if the following don't match

.. container:: parameters2

   state_ref : undefined = false

.. container:: methodparmtable

.. container:: parameters2

   state_cal : undefined = 0.0

.. container:: methodparmtable

.. container:: parameters2

   state_load : undefined = 0.0

.. container:: methodparmtable

.. container:: parameters2

   state_sub_scan : undefined = 0

.. container:: methodparmtable

.. container:: parameters2

   state_obs_mode : undefined = OBSERVE_TARGET.ON_SOURCE

.. container:: methodparmtable

.. container:: parameters2

   observer : undefined = CASA simulator

.. container:: methodparmtable

.. container:: parameters2

   project : undefined = CASA simulation

.. container:: methodparmtable

.. container:: param

   function **observemany**

   .. container:: collcontent

      .. container:: methoddesc

         Observe given sources with a given spectral window for the
         specified times, including start, stop, integration, and gap
         times. If usehourangle=False (set with settimes), the start and
         stop times are referenced to referencetime. If
         userhourangle=True, starttime/stoptime are interpreted as
         startha/stopha, the start and stop times are calculated such
         that the start time is later than the reference time, but less
         than one day later, and the hour angles refer to the first
         source observed. See also sm.observe

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         sourcenames : undefined

      .. container:: methodparmtable

         Name of sources

.. container:: parameters2

   spwname : undefined

.. container:: methodparmtable

   Unique user-supplied name for this spectral window

.. container:: parameters2

   starttimes : undefined = 0s

.. container:: methodparmtable

   Start times referenced to referencetime, or start hour angle

.. container:: parameters2

   stoptimes : undefined = 3600s

.. container:: methodparmtable

   Stop time referenced to referencetime, or stop hour angle

.. container:: parameters2

   directions : undefined

.. container:: methodparmtable

.. container:: parameters2

   add_observation : undefined = false

.. container:: methodparmtable

   Add a new line to the OBSERVATION subtable for this call

.. container:: parameters2

   state_sig : undefined = true

.. container:: methodparmtable

   a new line will be added to STATE if the following don't match

.. container:: parameters2

   state_ref : undefined = false

.. container:: methodparmtable

.. container:: parameters2

   state_cal : undefined = 0.0

.. container:: methodparmtable

.. container:: parameters2

   state_load : undefined = 0.0

.. container:: methodparmtable

.. container:: parameters2

   state_sub_scan : undefined = 0

.. container:: methodparmtable

.. container:: parameters2

   state_obs_mode : undefined = OBSERVE\_TARGET#ON\_SOURCE

.. container:: methodparmtable

.. container:: parameters2

   observer : undefined = CASA simulator

.. container:: methodparmtable

.. container:: parameters2

   project : undefined = CASA simulation

.. container:: methodparmtable

.. container:: param

   function **setlimits**

   .. container:: collcontent

      .. container:: methoddesc

         Data are flagged for two conditions: - Below elevation limit:
         If either of the antennas point below the specified elevation
         limit then the data are flagged. The elevation is calculated
         correctly for antennas at different locations (such as occurs
         in VLBI). - Shadowing: If one antenna shadows another such that
         the fractional (geometric) blockage is greater than the
         specified limit then the data are flagged. No correction for
         blockage is made for shadowed but non-flagged points.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         shadowlimit : undefined = 1e-6

      .. container:: methodparmtable

         Maximum fraction of geometrically shadowed area before flagging
         occurs

.. container:: parameters2

   elevationlimit : any = 10deg

.. container:: methodparmtable

   Minimum elevation angle before flagging occurs

.. container:: param

   function **setauto**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         autocorrwt : undefined = 0.0

      .. container:: methodparmtable

         Weight to assign autocorrelations (0=none)

.. container:: param

   function **setconfig**

   .. container:: collcontent

      .. container:: methoddesc

         Set the positions of the antennas. - The name of the telescope
         will control which voltage pattern is applied to the data (see
         sm.setvp for details). - The diameter(s) will be written to the
         antenna subtable but ONLY affect the calculated visibilities in
         sm.predict if telescope=ALMA,ACA,OVRO, \*and\* ftmachine=mosaic
         (see sm.setvp for details). - simutil::readantenna can be used
         to read an antenna config. file which includes many existing
         observatories. see help for the simobserve task, or the example
         below

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         telescopename : undefined = VLA

      .. container:: methodparmtable

         Name of the telescope we are simulating (determines VP)

.. container:: parameters2

   x : undefined = 0

.. container:: methodparmtable

   Vector of x values of all antennas [m]

.. container:: parameters2

   y : undefined = 0

.. container:: methodparmtable

   Vector of y values of all antennas [m]

.. container:: parameters2

   z : undefined = 0

.. container:: methodparmtable

   Vector of z values of all antennas [m]

.. container:: parameters2

   dishdiameter : undefined = 0

.. container:: methodparmtable

   Vector of diameters of all antennas [m]

.. container:: parameters2

   offset : undefined = 0

.. container:: methodparmtable

   Vector of offset of all antennas [m]

.. container:: parameters2

   mount : undefined = ALT-AZ

.. container:: methodparmtable

   Vector of mount types of all antennas (recognized mounts are
   'ALT-AZ', 'EQUATORIAL', 'X-Y', 'ORBITING', 'BIZARRE'

.. container:: parameters2

   antname : undefined = A

.. container:: methodparmtable

   Vector of names of all antennas

.. container:: parameters2

   padname : undefined = P

.. container:: methodparmtable

   Vector of names of pads or stations

.. container:: parameters2

   coordsystem : undefined = global

.. container:: methodparmtable

   Coordinate system of antenna positions [x,y,z], possibilities are
   'global', 'local' , 'longlat'

.. container:: parameters2

   referencelocation : any = ALMA

.. container:: methodparmtable

   Reference location [required for local coords] Position Measure of
   Coordinates of array location. E.g me.position('ITRF', '30.5deg',
   -20.2deg', 6000km') or me.observatory('ALMA')

.. container:: methodsection

   Example

.. container:: methodexam

   # known antenna configurations are stored in the data repository, #
   for historical reasons under "alma" even though this includes all #
   known observatories:
   configdir=casa.values()[0]['data']+"/alma/simmos/" # please look in
   that directory if your observatory is present. # if so, simutil can
   be used to read the file: from simutil import simutil # a simutil
   must be instantiated to use most methods u=simutil()
   x,y,z,d,padnames,telescope,posobs =
   u.readantenna(configdir+"vla.a.cfg") # note that readantenna converts
   the positions to earth-centered # global, from whatever format is in
   the configuration file, so # coordsystem="global" should be used in
   setconfig sm.setconfig(telescopename=telescope, x=x, y=y, z=z,
   dishdiameter=d.tolist(), mount=['alt-az'], antname=padnames,
   coordsystem='global', referencelocation=pospbs);

.. container:: param

   function **setfeed**

   .. container:: collcontent

      .. container:: methoddesc

         Specify feed parameters. At this moment, you only have the
         choice between 'perfect R L' and 'perfect X Y' (i.e., you
         cannot invent your own corrupted feeds yet). Doesn't need to be
         run if you want perfect R and L feeds.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined

      .. container:: methodparmtable

         Mode for specifying feed parameters (currently, perfect only)

.. container:: parameters2

   x : undefined = 0

.. container:: methodparmtable

   Some very secretive feed array parameter x

.. container:: parameters2

   y : undefined = 0

.. container:: methodparmtable

   Some more very secretive feed array parameter y

.. container:: parameters2

   pol : undefined = R

.. container:: methodparmtable

.. container:: param

   function **setfield**

   .. container:: collcontent

      .. container:: methoddesc

         Set one or more observed fields, including name and
         coordinates. Can be invoked multiple times for a complex
         observation. Must be invoked at least once before sm.observe.
         If the distance to the object is set then the phase term
         includes a curvature for the near-field effect at the center of
         the image.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         sourcename : undefined = SOURCE

      .. container:: methodparmtable

         Name of source or field (must be specified)

.. container:: parameters2

   sourcedirection : any

.. container:: methodparmtable

   Direction Measure of Coordinates of source to be observed. E.g
   me.direction('J2000', '30.5deg','-20.2deg').

.. container:: parameters2

   calcode : undefined

.. container:: methodparmtable

   Calibration code

.. container:: parameters2

   distance : any = 0m

.. container:: methodparmtable

   Distance to the object

.. container:: methodsection

   Example

.. container:: methodexam

   sm.setconfig(telescopename=telescope, x=x, y=y, z=z,
   dishdiameter=d.tolist(), mount=['alt-az'], antname=padnames,
   coordsystem='global', referencelocation=pospbs);
   sm.setspwindow(spwname='XBAND', freq='8GHz', deltafreq='50MHz',
   freqresolution='50MHz', nchannels=1, stokes='RR LL'); dir0 =
   me.direction('B1950', '16h00m0.0', '50d0m0.000')
   sm.setfield(sourcename='SIMU1', sourcedirection=dir0);
   sm.settimes(integrationtime="10s", usehourangle=True,
   referencetime=me.epoch('TAI', "2012/01/01/00:00:00"))
   sm.observe(sourcename='SIMU1', spwname='XBAND', starttime='0s',
   stoptime='3600s')

.. container:: param

   function **setmosaicfield**

   .. container:: collcontent

      .. container:: methoddesc

         Set mosaic fields by internally invoking setfield multiple
         times. Currently only handle a rectangular mosaicing pattern.
         Either setfield or setmosaicfield must be invoked at least once
         before observe. If the distance to the object is set then the
         phase term includes a curvature for the near-field effect at
         the center of the image.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         sourcename : undefined = SOURCE

      .. container:: methodparmtable

         Name of source or field (must be specified).

.. container:: parameters2

   calcode : undefined

.. container:: methodparmtable

   Calibration code

.. container:: parameters2

   fieldcenter : any

.. container:: methodparmtable

   Coordinates of mosaic field center

.. container:: parameters2

   xmosp : undefined = 1

.. container:: methodparmtable

   Number of mosaic pointing in horizontal direction

.. container:: parameters2

   ymosp : undefined = 1

.. container:: methodparmtable

   Number of mosaic pointing in vertical direction

.. container:: parameters2

   mosspacing : any = 1arcsec

.. container:: methodparmtable

   Spacing between mosaic pointings

.. container:: parameters2

   distance : any = 0m

.. container:: methodparmtable

   Distance to the object

.. container:: methodsection

   Example

.. container:: methodexam

   sm.setconfig(telescopename='VLA', x=xx, y=yy, z=zz,
   dishdiameter=diam, mount='alt-az', antname='VLA',
   coordsystem='local', referencelocation=dm.observatory('vla'));
   sm.setspwindow(spwname='XBAND', freq='8GHz', deltafreq='50MHz',
   freqresolution='50MHz', nchannels=1, stokes='RR LL'); dir0 =
   me.direction('B1950', '16h00m0.0', '50d0m0.000')
   sm.setmosaicfield(sourcename='SIMU1', fieldcenter=dir0, xmosp=2,
   ymosp=2, mosspacing='154.5arcsec');
   sm.settimes(integrationtime='10s'); sm.observe('SIMU1_1', 'XBAND',
   starttime='0s', stoptime='100s'); sm.observe('SIMU1_2', 'XBAND',
   starttime='110s', stoptime='210s'); sm.observe('SIMU1_3', 'XBAND',
   starttime='220s', stoptime='320s'); sm.observe('SIMU1_4', 'XBAND',
   starttime='330s', stoptime='430s');

.. container:: param

   function **setspwindow**

   .. container:: collcontent

      .. container:: methoddesc

         Set one or more spectral windows for the observations,
         including starting frequency, number of channels, channel
         increment and resolution, and stokes parameters observed. Can
         be invoked multiple times for a complex observation. Must be
         invoked at least once before observe.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spwname : undefined = XBAND

      .. container:: methodparmtable

         Unique user-supplied name for this spectral window

.. container:: parameters2

   freq : any = 8.0e9Hz

.. container:: methodparmtable

   Starting frequency

.. container:: parameters2

   deltafreq : any = 50e6Hz

.. container:: methodparmtable

   Frequency increment per channel

.. container:: parameters2

   freqresolution : any = 50.e6Hz

.. container:: methodparmtable

   Frequency resolution per channel

.. container:: parameters2

   refcode : undefined = TOPO

.. container:: methodparmtable

   Spectral reference code e.g. LSRK, TOPO, BARY

Allowed Value(s)

LSRK LSRD BARY GEO TOPO GALACTO LGROUP CMB

.. container:: parameters2

   nchannels : undefined = 1

.. container:: methodparmtable

   Number of channels

.. container:: parameters2

   stokes : undefined = RR LL

.. container:: methodparmtable

   Stokes types to simulate

.. container:: methodsection

   Example

.. container:: methodexam

   To simulate a two spectral window (or two IF's in VLA jargon) data
   set, use setpwid as follows (here we are simulating 16 channels,
   50MHz wide channel for each spectral window)
   sm.setspwindow(spwname='CBAND', freq='2GHz', deltafreq='50MHz',
   freqresolution='50MHz', nchannels=16, stokes='RR LL');
   sm.setspwindow(spwname='SBAND', freq='5GHz', deltafreq='50MHz',
   freqresolution='50MHz', nchannels=16, stokes='RR LL'); Note that the
   spwname is used in observe to determine which spectral window to use.

.. container:: param

   function **setdata**

   .. container:: collcontent

      .. container:: methoddesc

         This setup tool function selects which data are to be used
         subsequently. After invocation of setdata, only the selected
         data are operated on.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spwid : undefined = 0

      .. container:: methodparmtable

         Spectral Window Ids (0 relative) to select

.. container:: parameters2

   fieldid : undefined = 0

.. container:: methodparmtable

   Field Ids (0 relative) to select

.. container:: parameters2

   msselect : undefined

.. container:: methodparmtable

   TAQL select string applied as a logical "and" with the other
   selections

.. container:: param

   function **predict**

   .. container:: collcontent

      .. container:: methoddesc

         Predict astronomical data from an image. The (u,v) coordinates
         already exist, either from a MeasurementSet we have read in or
         by generating the MeasurementSet coordinates and empty data
         through smobserve. This method calculates visibilities for
         those coordinates. - predict(incremental=False) calculates new
         visibilities and replaces the DATA column, -
         predict(incremental=True) calculates new visibilities, adds
         them to the DATA column - predict for any value of incremental
         then sets CORRECTED_DATA equal to DATA, and MODEL_DATA to 1 \*
         predict assumes model image units are Jy/pixel, and in fact
         will overwrite the brightness units of the image itself! \*
         treatment of primary beam depends critically on parameters set
         in sm.setvp() and sm.setoptions(ftmachine) - see help sm.setvp
         for details. For componentlists, if sm.setvp() is run prior to
         predict, then the spectral variation of each component in the
         componentlist will include the multiplicative term of the beam
         value for each channel frequency. So a flat spectrum component
         will show the frequency variation of the beam in the predicted
         visibilities.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         imagename : undefined

      .. container:: methodparmtable

         Name of image from which to predict visibilities

.. container:: parameters2

   complist : undefined

.. container:: methodparmtable

   Name of component list

.. container:: parameters2

   incremental : undefined = false

.. container:: methodparmtable

   Add this model to the existing Data Visibilities?

.. container:: param

   function **setoptions**

   .. container:: collcontent

      .. container:: methoddesc

         Set options for predict. See also imager help. To simulate
         single dish data, use gridft=SD and gridfunction=PB. To invoke
         primary beam convolution in the uv domain, use
         ftmachine="mosaic". This is the only option that allows
         heterogeneous array simulation - see the example below and help
         sm.setvp for more details.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         ftmachine : undefined = ft

      .. container:: methodparmtable

         Fourier transform machine. Possibilities are 'ft', 'sd',
         'mosaic'

.. container:: parameters2

   cache : undefined = 0

.. container:: methodparmtable

   Size of gridding cache in complex pixels

.. container:: parameters2

   tile : undefined = 16

.. container:: methodparmtable

   Size of a gridding tile in pixels (in 1 dimension)

.. container:: parameters2

   gridfunction : undefined = SF

.. container:: methodparmtable

   Gridding function. String: 'SF'|'BOX'|'PB'

.. container:: parameters2

   location : any = ALMA

.. container:: methodparmtable

   Location used in phase rotations. Position Measure of Coordinates of
   array location. E.g me.position('ITRF', '30.5deg', '-20.2deg',
   '6000km') or me.observatory('ALMA')

.. container:: parameters2

   padding : undefined = 1.3

.. container:: methodparmtable

   Padding factor in image plane (\>=1.0)

.. container:: parameters2

   facets : undefined = 1

.. container:: methodparmtable

   Number of facets

.. container:: parameters2

   maxdata : undefined = 2000.0

.. container:: methodparmtable

   Maximum data to write to a single TSM file (MB)

.. container:: parameters2

   wprojplanes : undefined = 1

.. container:: methodparmtable

   Number of projection planes when using wproject as the ft-machine

.. container:: methodsection

   Example

.. container:: methodexam

   # set some options sm.setoptions(cache=10000000, tile=32,
   gridfunction='BOX', me.location('vla')) # set ftmachine to invoke
   uv-domain primary beam convolution, and use that # to simulate a
   heterogeneous ALMA 7m+12m array. from simutil import simutil
   u=simutil() configdir=casa.values()[0]['data']+"/alma/simmos/"
   x,y,z,d,padnames,telescope,posobs =
   u.readantenna(configdir+"alma.cycle5.1.cfg")
   x2,y2,z2,d2,padnames2,telescope2,posobs2 =
   u.readantenna(configdir+"aca.cycle5.cfg") sm.open("new.het.alma.ms")
   sm.setconfig(telescopename="ALMA",
   x=np.append(x,x2),y=np.append(y,y2),z=np.append(z,z2),
   dishdiameter=np.append(d,d2), mount=['alt-az'],
   padname=np.append(padnames,padnames2).tolist(), coordsystem='global',
   referencelocation=posobs) sm.setspwindow(spwname="band1",
   freq="330GHz",
   deltafreq="1GHz",freqresolution="1GHz",nchannels=1,stokes='XX YY')
   sm.setfeed(mode='perfect X Y',pol=[''])
   sm.setlimits(shadowlimit=0.01, elevationlimit='10deg')
   sm.setauto(0.0) sm.setfield(sourcename="src1", sourcedirection="ICRS
   10:00:00.00 -23.01.22", calcode="OBJ", distance='0m')
   sm.setfield(sourcename="src2", sourcedirection="ICRS 10:00:00.00
   -23.01.32", calcode="OBJ", distance='0m')
   sm.settimes(integrationtime="10s", usehourangle=True,
   referencetime=me.epoch('TAI', "2012/01/01/00:00:00")) etime="600s"
   sm.observe(sourcename="src1", spwname="band1",
   starttime=qa.mul(-1,qa.quantity(etime)),
   stoptime=qa.quantity(0,"s")); sm.observe(sourcename="src2",
   spwname="band1", starttime=qa.quantity(0,"s"),
   stoptime=qa.quantity(etime)); sm.setoptions(ftmachine="mosaic")
   sm.predict(imagename="point.ra10.image") sm.done()

.. container:: param

   function **setvp**

   .. container:: collcontent

      .. container:: methoddesc

         Set the voltage pattern model (and hence, the primary beam)
         used for a Telecope. There are currently two ways to set the
         voltage pattern: by using the extensive list of defaults which
         the system knows about, or by creating a voltage pattern
         description with the vpmanager. If you are simulating a
         telescope which doesn't yet exist, you will need to supply a
         model voltage pattern using the vpmanager. sm.predict behavior
         depends critically on the parameters here, and the ftmachine
         parameter set in sm.setoptions sm.predict will always query the
         vpmanager for a primary beam/VP pattern. if usedefaultvp==True,
         it will reset the vpmanager first, so that the PB obtained will
         be the default for the given telescope name if
         usedefaultvp==False, it will check whether vptable is set, and
         if so, load that table into the vpmanager and use the beams
         therein. if usedefaultvp==False and vptable is not set, it will
         use whatever is already set in the vpmanager (see example below
         for overriding a default telescope beam). What sm.predict does
         with the obtained PB depends on the ftmachine and dovp
         parameters: if ftmachine=="mosaic": - a message "Performing
         Mosaic Gridding" indicates that one is using uv domain
         convolution for simulating from images. - if the primary beam
         returned by the vpmanager is ALMA, ACA, or OVRO, heterogeneous
         gridding will be invoked, and the dish diameter set in
         sm.setconfig, or already in the antenna subtable, will be used
         to convolve sky model images. for ALMA or ACA, dish diameter
         =12m will use a 10.7m Airy pattern, and dish diameter =7m will
         use a 6.25m Airy pattern. see help sm.setoptions for an
         example. - otherwise the PB returned by the vpmanager will be
         used. \* heterogeneous simulation only works at present from a
         sky model image, NOT from sky model components. If you want to
         simulate a heterogeneous array, please add components to an
         image using ia.modify, and don't specify a component list in
         sm.predict. Homogeneous array simulation from component lists
         works fine. - IF dovp=True, the primary beam returned by the
         vpmanager will be used to convolve sky model components. This
         is not automatically invoked by ftmachine="mosaic", but needs
         to be set explicitly with sm.setvp() if you are simulating from
         components in addition to or instead of sky model images. if
         ftmachine=="ft" (the default): - a message "Synthesis Gridding"
         indicates that if requested with dovp==True, image domain PB
         convolution will be used. - if dovp==True, the primary beam
         returned by the vpmanager will be used to convolve sky model
         components and images.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         dovp : undefined = true

      .. container:: methodparmtable

         Multiply by the voltage pattern (ie, primary beam) when
         simulating

.. container:: parameters2

   usedefaultvp : undefined = true

.. container:: methodparmtable

   Look up the default VP for this telescope and frequency?

.. container:: parameters2

   vptable : undefined

.. container:: methodparmtable

   If usedefaultvp is false, provide a VP Table made with vpmanager

.. container:: parameters2

   dosquint : undefined = true

.. container:: methodparmtable

   Activate the beam squint in the VP model

.. container:: parameters2

   parangleinc : any = 360deg

.. container:: methodparmtable

   Parallactice angle increment for squint application

.. container:: parameters2

   skyposthreshold : any = 180deg

.. container:: methodparmtable

   Position threshold on the sky for feed arrays ??

.. container:: parameters2

   pblimit : undefined = 1.0e-2

.. container:: methodparmtable

   Primary beam limit to use in feed arrays ?

.. container:: methodsection

   Example

.. container:: methodexam

   # use the default primary beam in subsequent sm.predict (according to
   # whatever telescope name was set in sm.setconfig)
   sm.setvp(dovp=True, usedefaultvp=True)
   sm.predict(imagename="point.ra10.image",complist="point.cl") # use an
   alternate VP table e.g. of the format created by vpmanager:
   sm.setvp(dovp=True, usedefaultvp=False,
   vptable='MyAlternateVLAPBModel.TAB', dosquint=F);
   sm.predict(imagename="point.ra10.image",complist="point.cl") # set a
   VP and then use it overridding the default # (if telescope="NGVLA"
   was used previously in setconfig, # or if an MS was loaded with
   observatory name = "NGVLA")
   vp.setpbairy(telescope="NGVLA",dishdiam="10m",maxrad="5deg")
   sm.setvp(dovp=True,usedefaultvp=False)
   sm.predict(imagename="point.ra10.image",complist="point.cl")

.. container:: param

   function **corrupt**

   .. container:: collcontent

      .. container:: methoddesc

         Add errors specified by the set\* functions (such as noise,
         gains, polarization leakage, bandpass, etc) to the visibility
         data. The errors are applied to the DATA and CORRECTED_DATA
         columns. Note that corrupt handles only visibility-plane
         effects, not image-plane effects such as pointing errors and
         voltage patterns, which get applied in predict. Note, the
         function applies errors to both cross- and auto-correlation
         data; The auto-correlation data are corrupted properly only for
         the thermalnoise set by setnoise.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         sm,openfromms('3C273XC1.MS');
         sm.predict('3C273XC1.FAKE.IMAGE'); sm.setnoise(
         mode='simplenoise', simplenoise='0.1Jy'); sm.setpa(
         mode='calculate'); sm.corrupt();

.. container:: param

   function **reset**

   .. container:: collcontent

      .. container:: methoddesc

         Reset the visibility corruption terms: this means that corrupt
         introduces no errors.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **setbandpass**

   .. container:: collcontent

      .. container:: methoddesc

         Set the level of bandpass errors. The error distributions are
         normal, mean zero, with the variances as specified. (Not yet
         implemented).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = calculate

      .. container:: methodparmtable

         Mode of operation. String: 'calculate'|'table'

.. container:: parameters2

   table : undefined

.. container:: methodparmtable

   Name of table

.. container:: parameters2

   interval : any = 3600s

.. container:: methodparmtable

   Coherence interval e.g. '1h'

.. container:: parameters2

   amplitude : undefined = 0.0

.. container:: methodparmtable

   Variances errors in amplitude and phase

.. container:: param

   function **setapply**

   .. container:: collcontent

      .. container:: methoddesc

         Arrange for corruption by existing cal tables, in a manner
         exactly analogous to calibrater.setapply.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         table : undefined

      .. container:: methodparmtable

         Calibration table name

.. container:: parameters2

   type : undefined = BBPOLYGGSPLINEDPTTOPACGAINCURVE

.. container:: methodparmtable

   Component type

.. container:: parameters2

   t : undefined = 0.0

.. container:: methodparmtable

   Interpolation interval (seconds)

.. container:: parameters2

   field : any

.. container:: methodparmtable

   Select on field

.. container:: parameters2

   interp : undefined = aipslinnearestlinear

.. container:: methodparmtable

   Interpolation type (in time)

.. container:: parameters2

   calwt : undefined = false

.. container:: methodparmtable

   Calibrate weights?

.. container:: parameters2

   spwmap : undefined = -1

.. container:: methodparmtable

   Spectral windows to apply

.. container:: parameters2

   opacity : undefined = 0.0

.. container:: methodparmtable

   Array-wide zenith opacity (for type='TOPAC')

.. container:: param

   function **setgain**

   .. container:: collcontent

      .. container:: methoddesc

         Set the level of gain errors. Gain drift is implemented as
         fractional brownian motion with rms amplitude as specified.
         Interval is not currently used.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = fbm

      .. container:: methodparmtable

         Mode of operation. String: 'fbm'

.. container:: parameters2

   table : undefined

.. container:: methodparmtable

   Optional name of table to write

.. container:: parameters2

   interval : any = 10s

.. container:: methodparmtable

   timescale for gain variations NOT USED

.. container:: parameters2

   amplitude : undefined = 0.01

.. container:: methodparmtable

   amplitude scale (RMS) for gain variations [real,imag] or scalar

.. container:: param

   function **settrop**

   .. container:: collcontent

      .. container:: methoddesc

         Set up for corruption by the atmosphere - attenuation and
         increase in noise.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = screen

      .. container:: methodparmtable

         Mode of operation - screen or individual antennas

.. container:: parameters2

   table : undefined

.. container:: methodparmtable

   Name of optional cal table to write

.. container:: parameters2

   pwv : undefined = 3.0

.. container:: methodparmtable

   total precipitable water vapour in mm

.. container:: parameters2

   deltapwv : undefined = 0.15

.. container:: methodparmtable

   RMS PWV fluctuations \*as a fraction of PWV parameter\*

.. container:: parameters2

   beta : undefined = 1.1

.. container:: methodparmtable

   exponent of fractional brownian motion

.. container:: parameters2

   windspeed : undefined = 7.

.. container:: methodparmtable

   wind speed for screen type corruption (m/s)

.. container:: param

   function **setpointingerror**

   .. container:: collcontent

      .. container:: methoddesc

         Set the pointing error from a calpointing table

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         epjtablename : undefined

      .. container:: methodparmtable

         Name of a table that has E-Jones errors for Pointing

.. container:: parameters2

   applypointingoffsets : undefined = false

.. container:: methodparmtable

   Apply pointing offsets

.. container:: parameters2

   dopbcorrection : undefined = false

.. container:: methodparmtable

   apply primary beam correction

.. container:: param

   function **setleakage**

   .. container:: collcontent

      .. container:: methoddesc

         Set the level of polarization leakage between feeds. Currently,
         no time dependence is available.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = constant

      .. container:: methodparmtable

         Mode of operation. String: 'constant'

.. container:: parameters2

   table : undefined

.. container:: methodparmtable

   Optional name of table to write

.. container:: parameters2

   amplitude : undefined = 0.01

.. container:: methodparmtable

   Magnitude of pol leakage [real,imag]

.. container:: parameters2

   offset : undefined = 0.

.. container:: methodparmtable

   Meam of pol leakage [real,imag]

.. container:: param

   function **oldsetnoise**

   .. container:: collcontent

      .. container:: methoddesc

         Set various system parameters from which the thermal (ie,
         random additive) noise level will be calculated. For
         mode=simplenoise, one specifies the standard deviation for the
         noise to be added to real and imaginary parts of the
         visibility. For mode=calculate, the noise will vary with dish
         diameter, antenna efficiency, system temperature, opacity, sky
         temperature, etc. The noise will increase with the airmass if
         tau is greater than zero. The noise is calculated according to
         the Brown Equation (ie, R.L. Brown's calculation of MMA
         sensitivity, 3Oct95): dS = 4*sqrt(2) \*( T_rx*exp(-tau_atm) +
         T_atm*( exp(tau_atm) - epsilon_l + T_cmb) ) \*epsilon_q
         \*epsilon_a \*pi \*D^2 \*sqrt(dnu*dt)

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = calculate

      .. container:: methodparmtable

         Mode of operation. String: 'simplenoise'|'calculate'

.. container:: parameters2

   table : undefined

.. container:: methodparmtable

   Name of noise table - not currently implemented

.. container:: parameters2

   simplenoise : any = 0.0Jy

.. container:: methodparmtable

   Level of noise (if mode=simplenoise)

.. container:: parameters2

   antefficiency : undefined = 0.8

.. container:: methodparmtable

   antenna efficiency

.. container:: parameters2

   correfficiency : undefined = 0.85

.. container:: methodparmtable

   Correlation efficiency

.. container:: parameters2

   spillefficiency : undefined = 0.85

.. container:: methodparmtable

   Forward spillover efficiency

.. container:: parameters2

   tau : undefined = 0.1

.. container:: methodparmtable

   Atmospheric Opacity

.. container:: parameters2

   trx : undefined = 50

.. container:: methodparmtable

   Receiver temp (ie, all non-atmospheric Tsys contributions) [K]

.. container:: parameters2

   tatmos : undefined = 230.0

.. container:: methodparmtable

   (Physical, not Brightness) Temperature of atmosphere [K]

.. container:: parameters2

   tcmb : undefined = 2.7

.. container:: methodparmtable

   Temperature of cosmic microwave background [K]

.. container:: param

   function **setnoise**

   .. container:: collcontent

      .. container:: methoddesc

         Set various system parameters from which the thermal (ie,
         random additive) noise level will be calculated. For
         mode=simplenoise, one specifies the standard deviation "sigma"
         for the noise to be added to real and imaginary parts of the
         visibility. The noise in amplitude per visibility is
         approximately "sigma" although it is not Gaussian (see
         Thompson, Moran, and Swenson fig. 6.9) and the point source
         noise in a Stokes I image will be
         ~sigma/sqrt(n_pol)/sqrt(n_baselines)/sqrt(n_integrations),
         where n_pol are the number of polarizations in the MS
         (typically 2), and n_integrations are the number of correlator
         integration times in the MS (~ track time / int. time) For
         mode=tsys-atm or tsys-atm, the noise will vary with dish
         diameter, antenna efficiency, system temperature, opacity, sky
         temperature, etc. The noise will increase with the airmass if
         tau is greater than zero. The noise is calculated according to
         the Brown Equation (ie, R.L. Brown's calculation of MMA
         sensitivity, 3Oct95): dS = 4*sqrt(2) \*( T_rx*exp(-tau_atm) +
         T_atm*( exp(tau_atm) - epsilon_l + T_cmb) ) \*epsilon_q
         \*epsilon_a \*pi \*D^2 \*sqrt(dnu*dt) For mode=tsys-atm, the
         sky brightness temperature is calculated using an atmospheric
         model created for the user-input PWV. For mode=tsys-manual, the
         user specifies the sky brightness temperature manually.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = simplenoise

      .. container:: methodparmtable

         Mode of operation.

.. container:: parameters2

   table : undefined

.. container:: methodparmtable

   Name of optional cal table to write (if OTF=False)

.. container:: parameters2

   simplenoise : any = 0.1Jy

.. container:: methodparmtable

   Level of noise if not calculated by amt

.. container:: parameters2

   pground : any = 560mbar

.. container:: methodparmtable

   Ground pressure for ATM model (if tsys-atm)

.. container:: parameters2

   relhum : undefined = 20.0

.. container:: methodparmtable

   ground relative humidity for ATM model (if tsys-atm)

.. container:: parameters2

   altitude : any = 5000m

.. container:: methodparmtable

   site altitude for ATM model (if tsys-atm)

.. container:: parameters2

   waterheight : any = 200m

.. container:: methodparmtable

   Height of water layer for ATM model (if tsys-atm)

.. container:: parameters2

   pwv : any = 1mm

.. container:: methodparmtable

   Precipitable Water Vapor ATM model (if tsys-atm)

.. container:: parameters2

   tatmos : undefined = 250.0

.. container:: methodparmtable

   Temperature of atmosphere [K] (if tsys-manual)

.. container:: parameters2

   tau : undefined = 0.1

.. container:: methodparmtable

   Zenith Atmospheric Opacity (if tsys-manual)

.. container:: parameters2

   antefficiency : undefined = 0.8

.. container:: methodparmtable

   Antenna efficiency

.. container:: parameters2

   spillefficiency : undefined = 0.85

.. container:: methodparmtable

   Forward spillover efficiency

.. container:: parameters2

   correfficiency : undefined = 0.88

.. container:: methodparmtable

   Correlation efficiency

.. container:: parameters2

   trx : undefined = 50

.. container:: methodparmtable

   Receiver temp (ie, all non-atmospheric Tsys contributions) [K]

.. container:: parameters2

   tground : undefined = 270.0

.. container:: methodparmtable

   Temperature of ground/spill [K]

.. container:: parameters2

   tcmb : undefined = 2.73

.. container:: methodparmtable

   Temperature of cosmic microwave background [K]

.. container:: parameters2

   OTF : undefined = true

.. container:: methodparmtable

   calculate noise on-the-fly (WARNING: only experts with high-RAM
   machines should use False)

.. container:: parameters2

   senscoeff : undefined = 0.

.. container:: methodparmtable

   sensitivity constant (1./sqrt(2) for interferometer [default]; 1. for
   total power)

.. container:: parameters2

   rxtype : undefined = 0

.. container:: methodparmtable

   Receiver type; 0=2SB, 1=DSB e.g. ALMA B9

.. container:: param

   function **setpa**

   .. container:: collcontent

      .. container:: methoddesc

         Corrupt phase by the parallactic angle

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = calculate

      .. container:: methodparmtable

         Mode of operation. String: 'calculate'|'table'

.. container:: parameters2

   table : undefined

.. container:: methodparmtable

   Name of table

.. container:: parameters2

   interval : any = 10s

.. container:: methodparmtable

   Interval for parallactic angle application, e.g. '10s'

.. container:: param

   function **setseed**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         seed : undefined = 185349251

      .. container:: methodparmtable

         Seed

.. container:: section
   :name: viewlet-below-content-body
