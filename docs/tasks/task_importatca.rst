

.. _Description:

Description
   The data from the ATCA is available from the archive using the
   RPFITS file format. These files can be imported into CASA with the
   **importatca** task. 
   
   ::
   
      #In CASA
      #  importatca :: Import ATCA RPFITS file(s) to a MeasurementSet
      files               =['*.C1234']        #  Name of input ATCA RPFits file(s)
      vis                 = 'c1234.ms'        #  Name of output visibility file
                                              #   (MeasurementSet)
      options             =         ''        #  Processing options: birdie, reweight,
                                              #   noxycorr, fastmosaic, hires, noac
                                              #   (comma separated list)
      spw                 =       [-1]        #  Specify the spectral windows to use,
                                              #   default=all
      nscans              =     [0, 0]        #  Number of scans to skip followed by
                                              #   number of scans to read
      lowfreq             =   '0.1GHz'        #  Lowest reference frequency to select
      highfreq            =   '999GHz'        #  Highest reference frequency to select
      fields              =       ['']        #  List of field names to select
      edge                =          8        #  Percentage of edge channels to flag.
                                              #  For combined zooms, this specifies the
                                              #   percentage for a single zoom window
   
   The *files* parameter can take a string or a list of strings as
   input and also allows the use of wildcards as shown in the
   example above.
   
   For older ATCA continuum data (before the CABB correlator,
   April 2009), use *options='birdie,reweight'* to suppress
   internally generated RFI.
   
   The *options* parameter:
   
   -  *birdie* - (pre-CABB data only) discard edge channels and
      channels affected by internal RFI
   -  *reweight* - (pre-CABB data only) suppress ringing of RFI
      spikes by reweighting of the lag spectrum 
   -  *noxycorr* – do not apply the xy phase correction as derived
      from the switched noise calibration, by default this is applied
      during loading of the data
   -  *fastmosaic* – use this option if you are loading mosaic data
      with many pointings and only one or two integrations per
      pointing; this option changes the tiling of the data to avoid
      excessive I/O
   -  *hires* – use this option if you have data in time binning mode
      (as used for pulsars) but you want to make it look like data
      with very short integration time (no bins)
   -  *noac*  - discard the auto-correlation data
   
   The *spw* parameter takes a list of integers and can be used to
   select one or more of the simultaneous frequencies. With CABB
   there can be up to 34 spectra. The order of the frequency bands
   in the RPFITS file is: the two continuum bands (0 and 1),
   followed by the zoom bands for the first frequency and then the
   zoom bands for the second frequency. Note that this *spw*
   parameter does not take a string with wildcards. Use *spw=-1*
   to get all the data.

   
   The *nscans* parameter can be used to select part of a file,
   e.g., to retrieve a few test scans for a quick look.

   
   The *lowfreq* and *highfreq* parameters select data based on
   the reference frequency.

   
   The *fields* parameter selects data based on the field/source
   name.

   
   The *edge* parameter specifies how many edge channels to
   discard as a percentage of the number of channels in each band,
   e.g., the default value of 8 will discard 82 channels from the
   top and bottom of a 2048 channel spectrum.
   
   Note: For 16cm CABB data with two identical frequency setups you
   need to set either spw=[0] or spw=[1], otherwise duplicate data
   will appear in the MeasurementSet which can cause issues with
   e.g., mstransform operations.
   

.. _Examples:

Examples
   **Reading a pre-CABB ATCA archive file (RPFITS format)**
   
   ::
   
      importatca(['2001-01-02_1*.C999','2001-01-03_0*.C999'],'c999.ms',options='birdie,reweight',edge=10)
   
   Imports a number of ATCA RPFITS-format data sets into a CASA
   measurement set. We are applying birdie flagging and lag spectrum
   re-weighting (as appropriate for old 33 channel continuum data),
   as well as flagging the 10% edge channels.

   
   **Reading an ATCA/CABB archive file (RPFITS format)**
   
   ::
   
      importatca(['2012-10-25_0707.C2728'],'c2728.ms',options='noac',spw=2,edge=5)
   
   Imports a CABB RPFITS file, throwing away the auto-correlations
   and the 5% edge channels and selecting only the second
   simultaneous frequency band.
   

.. _Development:

Development
   No additional development details

