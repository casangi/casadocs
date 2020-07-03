.. container::
   :name: viewlet-above-content-title

Image Headers
=============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Viewing and manipulating image headers and histories

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      As summarized in the `CASA
      Images <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/casa-images>`__ page,
      an image header contains information on the observation – e.g. the
      observing date, pointing position, object observed, etc., and the
      resulting image – e.g. the restoring beam size, image intensity
      units, spatial coordinate system, spectral parameters, stokes
      parameters, etc..  Header metadata can also store notes on the
      observation and/or calibration and image processing.  The header
      tells the user what is in the image and is used by the
      CASA **viewer** and other tasks to set the data array on the
      correct spatial and spectral coordinates, assign the intensity
      values correctly, and otherwise properly handle the data cube. 

      FITS image headers can be read in CASA using the **listfits**
      task, whereas CASA image headers can be read and edited using the
      **imhead** task.  Additionally, the **imhistory** task can be used
      to view the history of the image, i.e. what operations or
      processes have been applied to it. These three tasks are described
      and demonstrated below.

       

      .. rubric:: List the Header of a FITS image (**listfits**)
         :name: list-the-header-of-a-fits-image-listfits

      .. container:: info-box

         CASA can frequently read and write image FITS files directly.
         Nevertheless, it is advisable to convert the images to the CASA
         format first with **importfits** for some tasks and
         applications.

      The task **listfits** can be used to display the Header Data Unit
      (HDU) of a FITS image. The input includes only the name of the of
      the FITS file, as follows:

      .. container:: casa-input-box

         | #  listfits :: List the HDU and typical data rows of a fits
           file:
         | fitsfile            =         ''        #  Name of input fits
           file

      The logger will output the full FITS HDU.  The example below shows
      the logger output for a Digital Sky Survey Image, which we have
      truncated somewhat due to the length of the output:

      .. container:: casa-output-box

         .. rubric:: ####################################
            ##### Begin Task: listfits           #####
            listfits(fitsfile="dss.test.fits")
            read fitsfile=dss.test.fits
            d 29: DATE-OBS= '1998-11-24T11:83:00' /Observation:
            Date/Time                         
            time.
            Primary Array HDU ------>>>
            d 156: DATAMIN =                 2701 /GetImage: Minimum
            returned pixel value          
            value has wrong data type.
            erted to type double.
            d 157: DATAMAX =                22189 /GetImage: Maximum
            returned pixel value          
            value has wrong data type.
            erted to type double.
            SIMPLE  =                      T /FITS: Compliance
            BITPIX  =                     16 /FITS: I*2 Data
            NAXIS   =                      2 /FITS: 2-D Image Data
            NAXIS1  =                    891 /FITS: X Dimension
            NAXIS2  =                    893 /FITS: Y Dimension
            EXTEND  =                      T /FITS: File can contain
            extensions
            DATE    = '2016-11-17' /FITS: Creation Date
            ORIGIN  = 'STScI/MAST' /GSSS: STScI Digitized Sky Survey
            SURVEY  = 'POSSII-F' /GSSS: Sky Survey
            REGION  = 'XP061   ' /GSSS: Region Name
            PLATEID = 'A2U4    ' /GSSS: Plate ID
            SCANNUM = '01      ' /GSSS: Scan Number
            DSCNDNUM= '00      ' /GSSS: Descendant Number
            TELESCID=                      3 /GSSS: Telescope ID
            BANDPASS=                     35 /GSSS: Bandpass Code
            COPYRGHT= 'Caltech/Palomar' /GSSS: Copyright Holder
            SITELAT =                 33.356 /Observatory: Latitude
            SITELONG=                116.863 /Observatory: Longitude
            TELESCOP= 'Oschin Schmidt - D' /Observatory: Telescope
            INSTRUME= 'Photographic Plate' /Detector: Photographic Plate
            EMULSION= 'IIIaF   ' /Detector: Emulsion
            FILTER  = 'RG610   ' /Detector: Filter
            PLTSCALE=                   67.2 /Detector: Plate Scale
            arcsec per mm
            PLTSIZEX=                    355 /Detector: Plate X
            Dimension mm
            PLTSIZEY=                    355 /Detector: Plate Y
            Dimension mm
            PLATERA =                144.055 /Observation: Field centre
            RA degrees
            PLATEDEC=                 69.812 /Observation: Field centre
            Dec degrees
            PLTLABEL= 'SF07740 ' /Observation: Plate Label
            DATE-OBS= '1998-11-24T11:83:00' /Observation: Date/Time
            EXPOSURE=                     50 /Observation: Exposure
            Minutes
            PLTGRADE= 'A       ' /Observation: Plate Grade
            OBSHA   =                1.28333 /Observation: Hour Angle
            OBSZD   =                37.9539 /Observation: Zenith
            Distance
            AIRMASS =                1.26743 /Observation: Airmass
            REFBETA =                61.7761 /Observation: Refraction
            Coeff
            REFBETAP=                 -0.082 /Observation: Refraction
            Coeff
            REFK1   =               -48616.4 /Observation: Refraction
            Coeff
            REFK2   =                -148442 /Observation: Refraction
            Coeff
            CNPIX1  =                   4993 /Scan: X Corner
            CNPIX2  =                  10823 /Scan: Y Corner
            XPIXELS =                  23040 /Scan: X Dimension
            YPIXELS =                  23040 /Scan: Y Dimension
            XPIXELSZ=                15.0295 /Scan: Pixel Size microns
            YPIXELSZ=                     15 /Scan: Pixel Size microns
            ASTRMASK= 'xp.mask ' /Astrometry: GSC2 Mask
            WCSAXES =                      2 /GetImage: Number WCS axes
            WCSNAME = 'DSS     ' /GetImage: Local WCS approximation from
            full plat
            RADESYS = 'ICRS    ' /GetImage: GSC-II calibration using
            ICRS system
            CTYPE1  = 'RA---TAN' /GetImage: RA-Gnomic projection
            CRPIX1  =                    446 /GetImage: X reference
            pixel
            CRVAL1  =                 148.97 /GetImage: RA of reference
            pixel
            CUNIT1  = 'deg     ' /GetImage: degrees
            CTYPE2  = 'DEC--TAN' /GetImage: Dec-Gnomic projection
            CRPIX2  =                    447 /GetImage: Y reference
            pixel
            CRVAL2  =                69.6795 /GetImage: Dec of reference
            pixel
            CUNIT2  = 'deg     ' /Getimage: degrees
            CD1_1   =           -0.000279458 /GetImage: rotation matrix
            coefficient
            CD1_2   =            2.15165e-05 /GetImage: rotation matrix
            coefficient
            CD2_1   =            2.14552e-05 /GetImage: rotation matrix
            coefficient
            CD2_2   =             0.00027889 /GetImage: rotation matrix
            coefficient
            OBJECT  = 'data    ' /GetImage: Requested Object Name
            DATAMIN =                   2701 /GetImage: Minimum returned
            pixel value
            DATAMAX =                  22189 /GetImage: Maximum returned
            pixel value
            OBJCTRA = '09 55 52.730' /GetImage: Requested Right
            Ascension (J2000)
            OBJCTDEC= '+69 40 45.80' /GetImage: Requested Declination
            (J2000)
            OBJCTX  =                5438.47 /GetImage: Requested X on
            plate (pixels)
            OBJCTY  =                11269.3 /GetImage: Requested Y on
            plate (pixels)
            END
            (0,0) = 4058
            (0,1) = 4058
            :name: begin-task-listfits-listfitsfitsfiledss.test.fits-read-fitsfiledss.test.fits-d-29-date-obs-1998-11-24t118300-observation-datetime-time.-primary-array-hdu--------d-156-datamin-2701-getimage-minimum-returned-pixel-value-value-has-wrong-data-type.-erted-to-type-double.-d-157-datamax-22189-getimage-maximum-returned-pixel-value-value-has-wrong-data-type.-erted-to-type-double.-simple-t-fits-compliance-bitpix-16-fits-i2-data-naxis-2-fits-2-d-image-data-naxis1-891-fits-x-dimension-naxis2-893-fits-y-dimension-extend-t-fits-file-can-contain-extensions-date-2016-11-17-fits-creation-date-origin-stscimast-gsss-stsci-digitized-sky-survey-survey-possii-f-gsss-sky-survey-region-xp061-gsss-region-name-plateid-a2u4-gsss-plate-id-scannum-01-gsss-scan-number-dscndnum-00-gsss-descendant-number-telescid-3-gsss-telescope-id-bandpass-35-gsss-bandpass-code-copyrght-caltechpalomar-gsss-copyright-holder-sitelat-33.356-observatory-latitude-sitelong-116.863-observatory-longitude-telescop-oschin-schmidt---d-observatory-telescope-instrume-photographic-plate-detector-photographic-plate-emulsion-iiiaf-detector-emulsion-filter-rg610-detector-filter-pltscale-67.2-detector-plate-scale-arcsec-per-mm-pltsizex-355-detector-plate-x-dimension-mm-pltsizey-355-detector-plate-y-dimension-mm-platera-144.055-observation-field-centre-ra-degrees-platedec-69.812-observation-field-centre-dec-degrees-pltlabel-sf07740-observation-plate-label-date-obs-1998-11-24t118300-observation-datetime-exposure-50-observation-exposure-minutes-pltgrade-a-observation-plate-grade-obsha-1.28333-observation-hour-angle-obszd-37.9539-observation-zenith-distance-airmass-1.26743-observation-airmass-refbeta-61.7761-observation-refraction-coeff-refbetap--0.082-observation-refraction-coeff-refk1--48616.4-observation-refraction-coeff-refk2--148442-observation-refraction-coeff-cnpix1-4993-scan-x-corner-cnpix2-10823-scan-y-corner-xpixels-23040-scan-x-dimension-ypixels-23040-scan-y-dimension-xpixelsz-15.0295-scan-pixel-size-microns-ypixelsz-15-scan-pixel-size-microns-astrmask-xp.mask-astrometry-gsc2-mask-wcsaxes-2-getimage-number-wcs-axes-wcsname-dss-getimage-local-wcs-approximation-from-full-plat-radesys-icrs-getimage-gsc-ii-calibration-using-icrs-system-ctype1-ra---tan-getimage-ra-gnomic-projection-crpix1-446-getimage-x-reference-pixel-crval1-148.97-getimage-ra-of-reference-pixel-cunit1-deg-getimage-degrees-ctype2-dec--tan-getimage-dec-gnomic-projection-crpix2-447-getimage-y-reference-pixel-crval2-69.6795-getimage-dec-of-reference-pixel-cunit2-deg-getimage-degrees-cd1_1--0.000279458-getimage-rotation-matrix-coefficient-cd1_2-2.15165e-05-getimage-rotation-matrix-coefficient-cd2_1-2.14552e-05-getimage-rotation-matrix-coefficient-cd2_2-0.00027889-getimage-rotation-matrix-coefficient-object-data-getimage-requested-object-name-datamin-2701-getimage-minimum-returned-pixel-value-datamax-22189-getimage-maximum-returned-pixel-value-objctra-09-55-52.730-getimage-requested-right-ascension-j2000-objctdec-69-40-45.80-getimage-requested-declination-j2000-objctx-5438.47-getimage-requested-x-on-plate-pixels-objcty-11269.3-getimage-requested-y-on-plate-pixels-end-00-4058-01-4058

       

      .. rubric:: Reading and Manipulating CASA Image Headers
         (**imhead**)
         :name: reading-and-manipulating-casa-image-headers-imhead

      CASA image headers can be accessed and edited with the **imhead**
      task. The *imagename* and *mode* are the two primary parameters in
      the **imhead** task. The imhead task can be run with
      *mode='summary'*, *'list'*, *'get'*, *'put'*, *'add'*, *'del'*, or
      *'history'*, and setting the mode opens up mode-specific
      sub-parameters. Many of these modes are described below
      and further documented in the
      `imhead <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_imhead>`__
      page of the Global Task List. 

      The default mode is *mode='summary'*, which prints a summary of
      the image properties to the logger and terminal, and returns a
      dictionary containing header information. With *mode='summary'*,
      **imhead** has the following inputs:  

      .. container:: casa-input-box

         | #  imhead :: List, get and put image header parameters
         | imagename           =         ''        #  Name of the input
           image
         | mode                =  'summary'        #  imhead options:
           add, del,
         |                                         #   get, history,
           list, put, summary
         |      verbose        =      False        #  Give a full
           listing of
         |                                         #   beams or just a
           short summary?
         |                                         #   Only used when
           the image has multiple beams
         |                                         #   and
           mode='summary'.

      Note that to capture the dictionary, it must be assigned as a
      Python variable, e.g. by running: 

      .. container:: casa-input-box

         header_summary =
         imhead('ngc5921.demo.cleanimg.image',mode='summary')

      Setting *mode='list'* prints all header keywords and values to the
      logger and terminal, and returns a dictionary containing the
      keywords and values. This mode does not have any sub-parameters.

      The *mode='get'* setting allows the user to retrieve the value for
      a specified keyword *hdkey*:

      .. container:: casa-input-box

         | #  imhead :: List, get and put image header parameters
         | imagename      =         ''        #  Name of the input image
         | mode           =      'get'   #  imhead options: list,
           summary, get, put
         |    hdkey       =         ''   #  The FITS keyword

      The *mode='put'* setting allows the user to replace the current
      value for a given keyword *hdkey* with that specified in
      *hdvalue*. There are two sub-parameters that are opened by this
      option:

      .. container:: casa-input-box

         | #  imhead :: List, get and put image header parameters
         | imagename      =         ''        #  Name of the input image
         | mode           =      'put'   #  imhead options: list,
           summary, get, put
         |    hdkey       =         ''   #  The FITS keyword
         |    hdvalue     =         ''   #  Value of hdkey

      .. container:: alert-box

         **Alert:** Be careful when using *mode='put'.* This task does
         not check whether the values you specify (e.g. for the axes
         types) are valid, and you can render your image invalid. Make
         sure you know what you are doing when using this option!

      .. rubric:: 
         Examples for **imhead**
         :name: examples-for-imhead

      In the command below, we print the header summary to the logger:

      .. container:: casa-input-box

         CASA <51>: imhead('ngc5921.demo.cleanimg.image',mode='summary')

      The logger output is the following:

      .. container:: casa-output-box

         | ##### Begin Task: imhead             #####
         |   Image name       : ngc5921.demo.cleanimg.image
         |   Object name      : N5921_2
         |   Image type       : PagedImage
         |   Image quantity   : Intensity
         |   Pixel mask(s)    : None
         |   Region(s)        : None
         |   Image units      : Jy/beam
         |   Restoring Beam   : 52.3782 arcsec, 45.7319 arcsec, -165.572
           deg
         |  
         |   Direction reference : J2000
         |   Spectral  reference : LSRK
         |   Velocity  type      : RADIO
         |   Rest frequency      : 1.42041e+09 Hz
         |   Pointing center     :  15:22:00.000000  +05.04.00.000000
         |   Telescope           : VLA
         |   Observer            : TEST
         |   Date observation    : 1995/04/13/00:00:00
         |   Telescope position: [-1.60119e+06m, -5.04198e+06m,
           3.55488e+06m] (ITRF)
         |  
         |   Axis Coord Type      Name             Proj Shape Tile  
           Coord value at pixel    Coord incr Units
         |  
           ------------------------------------------------------------------------------------------------
         |   0    0     Direction Right Ascension   SIN   256   64 
           15:22:00.000   128.00 -1.500000e+01 arcsec
         |   1    0     Direction Declination       SIN   256   64
           +05.04.00.000   128.00  1.500000e+01 arcsec
         |   2    1     Stokes    Stokes                    1   
           1             I
         |   3    2     Spectral  Frequency                46    8  
           1.41279e+09     0.00 2.4414062e+04 Hz
         |                        Velocity                              
           1607.99     0.00 -5.152860e+00 km/s
         | ##### End Task: imhead           

      If the beam size per plane differs (for example, in a spectral
      data cube), the beam information will be displayed for the channel
      with the largest beam (i.e. the lowest frequency channel),
      the chennel with the smallest beam (i.e. the highest frequency
      channel), and the channel closest to the median beam size. If you
      set *verbose=True*, the beam information would be provided for
      each spectral channel (or each plane of the image).  Running
      **imhead** with *mode='summary'* and *verbose=False* for a
      spectral data cube would print information on the restoring beams
      as follows:

      .. container:: casa-output-box

         | Restoring Beams
         | Pol   Type Chan      Freq   Vel
         | I    Max    0 9.680e+08     0   39.59 arcsec x   22.77 arcsec
           pa=-70.57 deg
         | I    Min  511 1.990e+09 -316516   20.36 arcsec x   12.05
           arcsec pa=-65.67 deg
         | I Median  255 1.478e+09 -157949   27.11 arcsec x   15.54
           arcsec pa=-70.36 deg

      Setting mode='list' prints all header keywords and values to the
      logger and terminal, and returns a dictionary containing the
      keywords and values. In the following, we capture the resulting
      dictionary in the variable hlist, and print the variable. 

      .. container:: casa-input-box

         CASA <52>: hlist =
         imhead('ngc5921.demo.cleanimg.image',mode='list')

         | CASA <53>: hlist
         |   Out[53]:
         | {'beammajor': 52.378242492675781,
         |  'beamminor': 45.731891632080078,
         |  'beampa': -165.5721435546875,
         |  'bunit': 'Jy/beam',
         |  'cdelt1': '-7.27220521664e-05',
         |  'cdelt2': '7.27220521664e-05',
         |  'cdelt3': '1.0',
         |  'cdelt4': '24414.0625',
         |  'crpix1': 128.0,
         |  'crpix2': 128.0,
         |  'crpix3': 0.0,
         |  'crpix4': 0.0,
         |  'crval1': '4.02298392585',
         |  'crval2': '0.0884300154344',
         |  'crval3': 'I',
         |  'crval4': '1412787144.08',
         |  'ctype1': 'Right Ascension',
         |  'ctype2': 'Declination',
         |  'ctype3': 'Stokes',
         |  'ctype4': 'Frequency',
         |  'cunit1': 'rad',
         |  'cunit2': 'rad',
         |  'cunit3': '',
         |  'cunit4': 'Hz',
         |  'datamax': ' Not Known ',
         |  'datamin': -0.010392956435680389,
         |  'date-obs': '1995/04/13/00:00:00',
         |  'equinox': 'J2000',
         |  'imtype': 'Intensity',
         |  'masks': ' Not Known ',
         |  'maxpixpos': array([134, 134,   0,  38], dtype=int32),
         |  'maxpos': '15:21:53.976, +05.05.29.998, I, 1.41371e+09Hz',
         |  'minpixpos': array([117,   0,   0,  21], dtype=int32),
         |  'minpos': '15:22:11.035, +04.31.59.966, I, 1.4133e+09Hz',
         |  'object': 'N5921_2',
         |  'observer': 'TEST',
         |  'projection': 'SIN',
         |  'reffreqtype': 'LSRK',
         |  'restfreq': [1420405752.0],
         |  'telescope': 'VLA'}

      The values for these keywords can be queried using
      *mode='get'.* In the following examples, we capture the return
      value:

      .. container:: casa-input-box

         | CASA <53>: mybmaj =
           imhead('ngc5921.demo.cleanimg.image',mode='get',hdkey='beammajor')
         | CASA <54>: mybmaj
         |   Out[54]: {'unit': 'arcsec', 'value': 52.378242492699997}
         | CASA <55>: myobserver =
           imhead('ngc5921.demo.cleanimg.image',mode='get',hdkey='observer')
         | CASA <56>: print myobserver
         | {'value': 'TEST', 'unit': ''}

      You can set the values for keywords using *mode='put'*. For
      example:

      .. container:: casa-input-box

         | CASA <57>:
           imhead('ngc5921.demo.cleanimg.image',mode='put',hdkey='observer',hdvalue='CASA')
         |   Out[57]: 'CASA'
         | CASA <58>:
           imhead('ngc5921.demo.cleanimg.image',mode='get',hdkey='observer')
         |   Out[58]: {'unit': '', 'value': 'CASA'}

       

      .. rubric:: Image History (imhistory)
         :name: image-history-imhistory

      Image headers contain records of the operations applied to them,
      as CASA tasks append the image header with a record of what they
      did. This information can be retrieved via the **imhistory** task,
      and new messages can be appended using the **imhistory** task as
      well. The primary inputs are *imagename* and *mode*, with
      sub-parameters arising from the selected mode. To view the history
      of the image, the inputs are:

      .. container:: casa-input-box

         | #  imhistory :: Retrieve and modify image history
         | imagename           =         ''        #  Name of the input
           image
         | mode                =     'list'        #  Mode to run in,
           'list' to  
         |                                         #   retrieve
           history,'append' 
         |                                         #   to append a
           record to history.
         |      verbose        =       True        #  Write history to
           logger if 
         |                                         #   mode='list'?

      With *verbose=True* (default) the image history is also reported
      in the CASA logger.  The **imhistory** task returns the messages
      in a Python list that can be captured by a variable, e.g.

      .. container:: casa-input-box

         myhistory=imhistory(’image.im’)

      It is also possible to add messages to the image headers via
      *mode='append'*.  See the
      `imhistory <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_imhistory>`__
      page in the Global Task List for an example of appending messages
      to the image history.

       

.. container:: section
   :name: viewlet-below-content-body
