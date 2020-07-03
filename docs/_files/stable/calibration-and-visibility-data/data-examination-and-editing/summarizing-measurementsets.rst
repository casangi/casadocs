.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

MeasurementSet Summary
======================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Summarizing MS or MMS data

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The MeasurementSet is the way CASA stores visibility data (the `MS
      definition <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/measurement-set>`__
      can be found in the `Reference
      Material <https://casa.nrao.edu/casadocs-devel/stable/memo-series/reference-material>`__
      section).  This page describes theree tasks to gain access to
      information stored in the MS: **listobs** displays observational
      details such as spatial (field), spectral (spectral window),
      temporal (scans), and polarization setup of an MS;
      **listpartition** provides information on how a MS was subdivided
      by the **partition** task (used for parallelized processing);
      **listvis** prints out the visibility values themselves. 

       

      .. rubric:: Summarizing your MS (**listobs**)
         :name: summarizing-your-ms-listobs

      An observational summary of the MS contents can be displayed
      with the **listobs** task. The inputs are:

      .. container:: casa-input-box

         | vis                 = 'day2_TDEM0003_10s_norx' #  Name of
           input visibility file (MS)
         | selectdata          =       True        #  Data selection
           parameters
         |      field          =         ''        #  Field names or
           field index
         |                                         #  numbers: ''
           ==>all, field='0~2,3C286'
         |      spw            =         ''        # 
           spectral-window/frequency/channel
         |      antenna        =         ''        #  antenna/baselines:
           ''==>all, antenna ='3,VA04'
         |      timerange      =         ''        #  time range:
           ''==>all,timerange='09:14:0~09:54:0'
         |      correlation    =         ''        #  Select data based
           on correlation
         |      scan           =         ''        #  scan numbers:
           ''==>all
         |      intent         =         ''        #  Select data based
           on observation intent: ''==>all
         |      feed           =         ''        #  multi-feed
           numbers: Not yet implemented
         |      array          =         ''        #  (sub)array
           numbers: ''==>all
         |      uvrange        =         ''        #  uv range:
           ''==>all; uvrange
         |                                         #  ='0~100klambda',
           default units=meters
         |      observation    =         ''        #  Select data based
           on observation ID: ''==>all
         | verbose             =       True        
         | listfile            =         ''        #  Name of disk file
           to write output: ''==>to terminal
         | listunfl            =      False        #  List unflagged row
           counts?
         |                                         #  If true, it can
           have significant negative performance
         |                                         #  impact

      The summary (of the selected data) will be written to the logger,
      to the casapy-YYYYMMDD-HHMMSS.log file, and optionally to a file
      specified in the *listfile* parameter. For example,

      .. container:: casa-input-box

         listobs('n5921.ms')

      results in a logger message like the following (also the format if
      a 'listfile' text file is requested):

      .. container:: casa-output-box

         | listobs(vis="day2_TDEM0003_10s_norx",selectdata=True,spw="",field="",
         |        
           antenna="",uvrange="",timerange="",correlation="",scan="",
         |        
           intent="",feed="",array="",observation="",verbose=True,
         |         listfile="",listunfl=False)
         | ================================================================================
         |            MeasurementSet Name: 
           /Users/jott/casa/casatest/casa4.0/irc/day2_TDEM0003_10s_norx     
           MS Version 2
         | ================================================================================
         |    Observer: Mark J. Mark Claussen     Project: T.B.D.  
         | Observation: EVLA
         | Data records: 290218       Total integration time = 10016
           seconds
         |    Observed from   26-Apr-2010/03:21:56.0   to  
           26-Apr-2010/06:08:52.0 (UTC)
         |    
         |    ObservationID = 0         ArrayID = 0
         |   Date        Timerange (UTC)          Scan  FldId
           FieldName             nRows     SpwIds   Average
           Interval(s)    ScanIntent
         |   26-Apr-2010/03:21:51.0 - 03:23:21.0     5      2
           J0954+1743                2720  [0, 1]  [10, 10]
         |               03:23:39.0 - 03:28:25.0     6      3
           IRC+10216                 9918  [0, 1]  [10, 10]
         |               03:28:38.0 - 03:29:54.0     7      2
           J0954+1743                2700  [0, 1]  [10, 10]
         |               03:30:08.0 - 03:34:53.5     8      3
           IRC+10216                 9918  [0, 1]  [10, 10]
         | ...
         |            (nRows = Total number of rows per scan)
         | Fields: 4
         |   ID   Code Name                RA              
           Decl           Epoch   SrcId      nRows
         |   2    D    J0954+1743          09:54:56.823626
           +17.43.31.22243 J2000   2          65326
         |   3    NONE IRC+10216           09:47:57.382000
           +13.16.40.65999 J2000   3         208242
         |   5    F    J1229+0203          12:29:06.699729
           +02.03.08.59820 J2000   5          10836
         |   7    E    J1331+3030          13:31:08.287984
           +30.30.32.95886 J2000   7           5814
         | Spectral Windows:  (2 unique spectral windows and 1 unique
           polarization setups)
         |   SpwID  Name      #Chans   Frame   Ch1(MHz)  ChanWid(kHz) 
           TotBW(kHz)  Corrs          
         |   0      Subband:0     64   TOPO   36387.229      
           125.000      8000.0  RR  RL  LR  LL
         |   1      Subband:0     64   TOPO   36304.542      
           125.000      8000.0  RR  RL  LR  LL
         | Sources: 10
         |   ID   Name                SpwId RestFreq(MHz)  SysVel(km/s)
         |   0    J1008+0730          0     0.03639232     -0.026       
         |   0    J1008+0730          1     0.03639232     -0.026       
         |   2    J0954+1743          0     0.03639232     -0.026       
         |   2    J0954+1743          1     0.03639232     -0.026       
         |   3    IRC+10216           0     0.03639232     -0.026       
         |   3    IRC+10216           1     0.03639232     -0.026       
         |   5    J1229+0203          0     0.03639232     -0.026       
         |   5    J1229+0203          1     0.03639232     -0.026       
         |   7    J1331+3030          0     0.03639232     -0.026       
         |   7    J1331+3030          1     0.03639232     -0.026       
         | Antennas: 19:
         |   ID   Name  Station   Diam.    Long.        
           Lat.                Offset from array center
           (m)                ITRF Geocentric coordinates (m)        
         |                                                                     
           East         North     Elevation              
           x               y               z
         |   0    ea01  W09       25.0 m   -107.37.25.2 
           +33.53.51.0       -521.9407     -332.7782       -1.1977
           -1601710.017000 -5042006.928200  3554602.355600
         |   1    ea02  E02       25.0 m   -107.37.04.4 
           +33.54.01.1          9.8247      -20.4292       -2.7808
           -1601150.059500 -5042000.619800  3554860.729400
         |   2    ea03  E09       25.0 m   -107.36.45.1 
           +33.53.53.6        506.0591     -251.8666       -3.5832
           -1600715.948000 -5042273.187000  3554668.184500
         |   3    ea04  W01       25.0 m   -107.37.05.9 
           +33.54.00.5        -27.3562      -41.3030       -2.7418
           -1601189.030140 -5042000.493300  3554843.425700
         |   4    ea05  W08       25.0 m   -107.37.21.6 
           +33.53.53.0       -432.1158     -272.1493       -1.5032
           -1601614.091000 -5042001.655700  3554652.509300
         |   5    ea07  N06       25.0 m   -107.37.06.9 
           +33.54.10.3        -54.0667      263.8720       -4.2292
           -1601162.593200 -5041829.000000  3555095.890500
         |   6    ea08  N01       25.0 m   -107.37.06.0 
           +33.54.01.8        -30.8810       -1.4664       -2.8597
           -1601185.634945 -5041978.156586  3554876.424700
         |   7    ea09  E06       25.0 m   -107.36.55.6 
           +33.53.57.7        236.9058     -126.3369       -2.4443
           -1600951.588000 -5042125.911000  3554773.012300
         |   8    ea12  E08       25.0 m   -107.36.48.9 
           +33.53.55.1        407.8394     -206.0057       -3.2252
           -1600801.916000 -5042219.371000  3554706.449900
         |   9    ea15  W06       25.0 m   -107.37.15.6 
           +33.53.56.4       -275.8288     -166.7451       -2.0590
           -1601447.198000 -5041992.502500  3554739.687600
         |   10   ea19  W04       25.0 m   -107.37.10.8 
           +33.53.59.1       -152.8599      -83.8054       -2.4614
           -1601315.893000 -5041985.320170  3554808.304600
         |   11   ea20  N05       25.0 m   -107.37.06.7 
           +33.54.08.0        -47.8454      192.6015       -3.8723
           -1601168.786100 -5041869.054000  3555036.936000
         |   12   ea21  E01       25.0 m   -107.37.05.7 
           +33.53.59.2        -23.8638      -81.1510       -2.5851
           -1601192.467800 -5042022.856800  3554810.438800
         |   13   ea22  N04       25.0 m   -107.37.06.5 
           +33.54.06.1        -42.5986      132.8623       -3.5431
           -1601173.953700 -5041902.660400  3554987.536500
         |   14   ea23  E07       25.0 m   -107.36.52.4 
           +33.53.56.5        318.0523     -164.1848       -2.6960
           -1600880.570000 -5042170.388000  3554741.457400
         |   15   ea24  W05       25.0 m   -107.37.13.0 
           +33.53.57.8       -210.0944     -122.3885       -2.2581
           -1601377.008000 -5041988.665500  3554776.393400
         |   16   ea25  N02       25.0 m   -107.37.06.2 
           +33.54.03.5        -35.6245       53.1806       -3.1345
           -1601180.861480 -5041947.453400  3554921.628700
         |   17   ea27  E03       25.0 m   -107.37.02.8 
           +33.54.00.5         50.6647      -39.4832       -2.7249
           -1601114.365500 -5042023.153700  3554844.945600
         |   18   ea28  N08       25.0 m   -107.37.07.5 
           +33.54.15.8        -68.9057      433.1889       -5.0602
           -1601147.940400 -5041733.837000  3555235.956000

      **listobs** shows information on the project itself like project
      code, observer and telescope, followed by the sequence of scans
      with start/stop times, integration times, and scan intents, a list
      of all fields with name and coordinates, available spectral
      windows and their shapes, a list of sources (field/spw
      combination), and finally the location of all antennas that are
      used in the observation. A row is an MS entry for a given time
      stamp and baseline (rows can be accessed e.g. via
      **browsetable**). 

      *verbose=False* would not show the complete list, in particular no
      information on the scans. 

       

       

      .. rubric:: MMS summary (**listpartition**)
         :name: mms-summary-listpartition

      **listobs** can also be used for Multi MeasurementSets (MMSs). In
      addition, the task **listpartition** will provide additional
      information how the data is structured in preparation
      for parallelized processing (e.g. using the **partition** task).
      The inputs are:

       

      .. container:: casa-input-box

         | #  listpartition :: List the summary of a Multi-MS data set
           in the logger or in a file
         | vis                 =         ''        #  Name of Multi-MS
           or normal MS.
         | createdict          =      False        #  Create and return
           a dictionary with
         |                                         #   Sub-MS
           information
         | listfile            =         ''        #  Name of ASCII file
           to save output:
         |                                         #   ''==>to terminal

      For example,

      .. container:: casa-input-box

         listpartition('n5921.mms')

      results in the logger messages:

      .. container:: casa-output-box

         | This is a multi-MS with separation axis = scan,spw
         | Sub-MS               Scan  Spw    Nchan  Nrows   Size  
         | ngc5921.mms.0000.ms  2     [0]    [63]   1890    27M   
         |                      4     [0]    [63]   756           
         |                      5     [0]    [63]   1134          
         |                      6     [0]    [63]   6804          
         | ngc5921.mms.0001.ms  1     [0]    [63]   4509    28M   
         |                      3     [0]    [63]   6048          
         |                      7     [0]    [63]   1512       

      The output can also be redirected to a `python
      dictionary <http://casa.nrao.edu/casadocs/stable/usingcasa/python-and-casa#figid-casapythondictionaries>`__
      through the *createdict* parameter. 

       

      .. rubric:: Listing MS data (**listvis**)
         :name: listing-ms-data-listvis

      The **listvis** prints a list of the visibility data in an MS to
      the terminal or a textfile. The inputs are:

      .. container:: casa-input-box

         | #  listvis :: List MeasurementSet visibilities.
         | vis                 =         ''        #  Name of input
           visibility file
         | options             =       'ap'        #  List options: ap
           only
         | datacolumn          =     'data'        #  Column to list:
           data, float_data, corrected, model,
         |                                         #   residual
         | field               =         ''        #  Field names or
           index to be listed: ''==>all
         | spw                 =        '*'        #  Spectral
           window:channels: '\*'==>all, spw='1:5~57'
         | selectdata          =      False        #  Other data
           selection parameters
         | observation         =         ''        #  Select by
           observation ID(s)
         | average             =         ''        #  Averaging mode:
           ==>none (Not yet implemented)
         | showflags           =      False        #  Show flagged data
           (Not yet implemented)
         | pagerows            =         50        #  Rows per page
         | listfile            =         ''        #  Output file

      For example,

      .. container:: casa-output-box

         | Units of columns are: Date/Time(YYMMDD/HH:MM:SS UT),
           UVDist(wavelength), Phase(deg), UVW(m)
         | WEIGHT: 7
         | FIELD: 2
         | SPW: 0
         | Date/Time:                           RR:                
           RL:                 LR:                
           LL:                                             
         | 2010/04/26/      Intrf UVDist  Chn    Amp     Phs  Wt F  
           Amp     Phs  Wt F   Amp     Phs  Wt F   Amp     Phs  Wt
           F         U         V         W
         | ------------|---------|------|----|--------------------|-------------------|-------------------|-------------------|---------|---------|---------\|
         |   03:21:56.0 ea01-ea02  72363    0: 0.005  -124.5   7  
           0.005    25.7   7   0.001   104.6   7   0.000    23.4   7    
           -501.93   -321.75    157.78
         |   03:21:56.0 ea01-ea02  72363    1: 0.001    -4.7   7  
           0.001  -135.1   7   0.004   -14.6   7   0.001    19.9   7    
           -501.93   -321.75    157.78
         |   03:21:56.0 ea01-ea02  72363    2: 0.002    17.8   7  
           0.002    34.3   7   0.005  -114.3   7   0.005  -149.7   7    
           -501.93   -321.75    157.78
         |   03:21:56.0 ea01-ea02  72363    3: 0.004   -19.4   7  
           0.003   -79.2   7   0.002   -89.0   7   0.004    31.3   7    
           -501.93   -321.75    157.78
         |   03:21:56.0 ea01-ea02  72363    4: 0.001   -16.8   7  
           0.004  -141.5   7   0.005   114.9   7   0.006   105.2   7    
           -501.93   -321.75    157.78
         |   03:21:56.0 ea01-ea02  72363    5: 0.001   -29.8   7  
           0.009   -96.4   7   0.002  -125.0   7   0.002   -64.5   7    
           -501.93   -321.75    157.78
         | ...
         | Type Q to quit, A to toggle long/short list, or RETURN to
           continue [continue]:

      columns are:

      .. container:: info-box

         ::

            COLUMN NAME       DESCRIPTION
            -----------       -----------
            Date/Time     Time stamp of data sample (YYMMDD/HH:MM:SS UT)
            Intrf                Interferometer baseline (antenna names)
            UVDist            uv-distance (units of wavelength)
            Fld                  Field ID (if more than 1)
            SpW               Spectral Window ID (if more than 1)
            Chn                Channel number (if more than 1)
            (Correlated          Correlated polarizations (eg: RR, LL, XY)
              polarization)     Sub-columns are: Amp, Phs, Wt, F
            Amp               Visibility amplitude
            Phs                 Visibility phase (deg)
            Wt                  Weight of visibility measurement
            F                     Flag: 'F' = flagged datum; ' ' = unflagged
            UVW               UVW coordinates (meters)

      Note that MS listings can be very large. Use selectdata=True and
      subselect the data to obtain the desired information as much as
      possible.  

.. container:: section
   :name: viewlet-below-content-body
