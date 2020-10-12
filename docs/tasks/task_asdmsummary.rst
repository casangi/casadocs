

.. _Description:

Description
   summarized description of an ASDM dataset
   
   .. rubric:: Summary
      
   
   Given an ASDM directory, this task will print information about
   the content of the dataset contained in that directory (down to
   the level of a subscan) in the CASA log.
   
    
   
   .. rubric:: Parameter descriptions
      
   
   .. rubric:: *asdm*
      
   
   Name of input ASDM directory. Examples:
   *asdm='10C-119_sb3070258_1.55628.42186299768'*
   

.. _Examples:

Examples
   task asdmsummary examples
   
   The **asdmsummary** task prints to the CASA log a description of
   the content of a Science Data Model (SDM and ASDM are synonymous;
   the A in ASDM stands for "ALMA"). For example, to summarize an SDM
   from the EVLA:
   
   ::
   
      asdmsummary(asdm='10C-119_sb3070258_1.55628.42186299768')
   
   Prints the following information to the CASA logger. Note that the
   output from **asdmsummary** may be quite long, depending on the
   SDM, and this has been edited for space. Edits are indicated using
   "...".
   
   ::
   
      | Input ASDM dataset : 10C-119_sb3070258_1.55628.42186299768
      | ========================================================================================
      | ASDM dataset :10C-119_sb3070258_1.55628.42186299768
      | ========================================================================================
      | Exec Block : ExecBlock_0
      | Telescope : EVLA
      | Configuration name : B
      | Observer name : ...
      | The exec block started on 2011-03-08T10:07:30.550000640 and
        ended on 2011-03-08T13:06:59.950000128
      | 27 antennas have been used in this exec block.
      |         Id     Name         Make Station    Diameter        
        X              Y             Z
      |      Antenna_0  ea01    UNDEFINED   W36        25   
        -1606841.96   -5042279.689    3551913.017
      |      Antenna_1  ea02    UNDEFINED   E20        25    
        -1599340.8   -5043150.965    3554065.219
      |      Antenna_2  ea03    UNDEFINED   E36        25  
        -1596127.728   -5045193.751    3552652.421
      |      Antenna_3  ea04    UNDEFINED   W28        25  
        -1604865.649    -5042190.04    3552962.365
      | ...
      | Number of scans in this exec Block : 13
      | scan #1 from 2011-03-08T10:07:30.550000640 to
        2011-03-08T10:17:27.800000512
      |     Intents : OBSERVE_TARGET
      |     Sources : J1438+6211
      |     Subscan #1 from 2011-03-08T10:07:30.550000640 to
        2011-03-08T10:17:27.800000512
      |         Intent : UNSPECIFIED
      |         Number of integrations : 597
      |          Binary data in uid:///evla/bdf/1299578850271
      |          Number of integrations : 597
      |          Time sampling : INTEGRATION
      |          Correlation Mode : CROSS_AND_AUTO
      |          Spectral resolution type : FULL_RESOLUTION
      |          Atmospheric phase correction : AP_UNCORRECTED
      |          SpectralWindow_0 : numChan = 64, frame = TOPO,
        firstChan = 1247000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_1 : numChan = 64, frame = TOPO,
        firstChan = 1263000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_2 : numChan = 64, frame = TOPO,
        firstChan = 1279000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_3 : numChan = 64, frame = TOPO,
        firstChan = 1295000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      | ...
      | scan #2 from 2011-03-08T10:17:27.800000512 to
        2011-03-08T10:22:26.999999488
      |     Intents : CALIBRATE_PHASE,OBSERVE_TARGET
      |     Sources : J1438+6211
      |     Subscan #1 from 2011-03-08T10:17:27.800000512 to
        2011-03-08T10:22:26.999999488
      |         Intent : UNSPECIFIED
      |         Number of integrations : 300
      |          Binary data in uid:///evla/bdf/1299578850644
      |          Number of integrations : 300
      |          Time sampling : INTEGRATION
      |          Correlation Mode : CROSS_AND_AUTO
      |          Spectral resolution type : FULL_RESOLUTION
      |          Atmospheric phase correction : AP_UNCORRECTED
      |          SpectralWindow_0 : numChan = 64, frame = TOPO,
        firstChan = 1247000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_1 : numChan = 64, frame = TOPO,
        firstChan = 1263000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_2 : numChan = 64, frame = TOPO,
        firstChan = 1279000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_3 : numChan = 64, frame = TOPO,
        firstChan = 1295000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      | ....
      | scan #3 from 2011-03-08T10:22:26.999999488 to
        2011-03-08T10:52:07.150000128
      |          Intents : OBSERVE_TARGET
      |     Sources : N5907
      |     Subscan #1 from 2011-03-08T10:22:26.999999488 to
        2011-03-08T10:52:07.150000128
      |         Intent : UNSPECIFIED
      |         Number of integrations : 1780
      |     
      |          Binary data in uid:///evla/bdf/1299579448131
      |          Number of integrations : 1780
      |          Time sampling : INTEGRATION
      |          Correlation Mode : CROSS_AND_AUTO
      |          Spectral resolution type : FULL_RESOLUTION
      |          Atmospheric phase correction : AP_UNCORRECTED
      |          SpectralWindow_0 : numChan = 64, frame = TOPO,
        firstChan = 1247000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_1 : numChan = 64, frame = TOPO,
        firstChan = 1263000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_2 : numChan = 64, frame = TOPO,
        firstChan = 1279000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      |          SpectralWindow_3 : numChan = 64, frame = TOPO,
        firstChan = 1295000000, chandWidth = 250000 x Polarization_0
        : corr = RR,RL,LR,LL
      | ...
   

.. _Development:

Development
   task asdmsummary developer
   
   --CASA Developer--
   
   