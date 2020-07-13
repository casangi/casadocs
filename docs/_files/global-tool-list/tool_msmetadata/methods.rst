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

            constructor **msmetadata**

            .. container:: collcontent

               .. container:: methoddesc

               .. container:: methodsection

                  Parameters : None

         .. container:: param

            function **almaspws**

            .. container:: collcontent

               .. container:: methoddesc

                  Get spectral window IDs based on ALMA-specific
                  criteria. The inputs are or'ed together to form the
                  returned list. If complement=True, then the complement
                  of the selection is returned. The following algorithm
                  is used to identify WVR spwectral windows: 1. check
                  for water vapor radiometer (WVR) spectral windows
                  using the spectral window name "WVR#NOMINAL" and
                  report these. 2. If no SPWs match that string, then
                  the names are checked for "WVR" and are reported
                  instead.

               .. container:: methodsection

                  Parameters

               .. container:: parameters2

                  chavg : undefined = false

               .. container:: methodparmtable

                  Get channel average spectral windows?

.. container:: parameters2

   fdm : undefined = false

.. container:: methodparmtable

   Get FDM spectral windows?

.. container:: parameters2

   sqld : undefined = false

.. container:: methodparmtable

   Get square law (i.e. total power) detector spectral windows?

.. container:: parameters2

   tdm : undefined = false

.. container:: methodparmtable

   Get TDM spectral windows?

.. container:: parameters2

   wvr : undefined = false

.. container:: methodparmtable

   Get WVR spectral windows?

.. container:: parameters2

   complement : undefined = false

.. container:: methodparmtable

   Return the complement of the selected set?

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get all square law detector spectral window IDs
   msmd.almaspws(sqld=True) # get all spectral window IDs other than
   those associated with square law detectors msmd.almaspws(sqld=True,
   complement=True)

.. container:: param

   function **antennadiameter**

   .. container:: collcontent

      .. container:: methoddesc

         Get the diameter for the specified antenna. The antenna can be
         specified either by its zero-based ID from the ANTENNA table or
         by its name in that table. The returned dictionary is a valid
         quantity. If a negative integer is provided for the antenna,
         then all atenna diameters will be returned in a dictionary that
         has keys that are the antenna IDs and values that are
         dictionaries, each being a valid quantity representing the
         diameter for that antenna ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         antenna : any = -1

      .. container:: methodparmtable

         Zero-based antenna in the ANTENNA table, or antenna name. A
         negative integer will cause all antenna diameters to be
         returned.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # Get the diameter of the antenna named "VB2"
   diameter = msmd.antennadiameter("VB2") msmd.done()

.. container:: param

   function **antennaids**

   .. container:: collcontent

      .. container:: methoddesc

         Get the zero-based antenna IDs for the specfied antenna names
         and the specified diameter range for the specified observation
         ID. An array of unique IDs in order of the specified names is
         returned. Note that if a specified name is listed mulitple
         times in the ANTENNA table, the largest ID is returned, unless
         the observation ID is specified to be non-negative, in which
         case, the returned IDs are filtered based on the specified
         observation ID. If no names and no diameter range is specified,
         all IDs are returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         name : any

      .. container:: methodparmtable

         Antenna names (string or string array) for which to get the
         corresponding IDs. Note that \* matches any number of
         characters of all character classes.

.. container:: parameters2

   mindiameter : any = 0m

.. container:: methodparmtable

   Minimum antenna diameter, expressed as a quantity.

.. container:: parameters2

   maxdiameter : any = 1pc

.. container:: methodparmtable

   Maximum antenna diameter, expressed as a quantity.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. If negative, all observation IDs are considered.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the zero-based antenna IDs for the antenna
   named "VB2" antenna_id = msmd.antennaids("VB2")[0] # get the
   zero-based antenna IDs for all antennas with diameters between 9m and
   11m antenna_ids = msmd.antennaids(mindiameter="9m",
   maxdiameter=qa.quantity("11m")) msmd.done()

.. container:: param

   function **antennanames**

   .. container:: collcontent

      .. container:: methoddesc

         Get the name of the antenna for the specfied zero-based antenna
         ID. If antennaids is not specified, all antenna names are
         returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         antennaids : any = -1-1

      .. container:: methodparmtable

         Zero-based antenna IDs (int or int array) for which to get the
         antenna names.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the name associated with antenna ID 31
   antenna_name = msmd.antennanames(31)[0] msmd.done()

.. container:: param

   function **antennaoffset**

   .. container:: collcontent

      .. container:: methoddesc

         Get the offset position of the specified antenna relative to
         the array reference position. Antenna may be specified as a
         zero-based integer (row number in the ANTENNA table) or a
         string representing a valid antenna name. The returned record
         contains the longitude, latitude, and elevation offsets as
         quantity records. The reported longitude and latitude offsets
         are measured along the surface of a sphere whose center is
         coincident with the center of the earth and whose surface
         contains the observatory reference position.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         which : any = 0

      .. container:: methodparmtable

         Zero-based antenna in the ANTENNA table, or antenna name.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the offset of the (zero-based) 3rd antenna
   in the ANTENNA table antennna_offset = msmd.antennaoffset(3) # get
   the offset of antenna DV02 antennna_offset =
   msmd.antennaoffset('DV02') msmd.done()

.. container:: param

   function **antennaposition**

   .. container:: collcontent

      .. container:: methoddesc

         Get the position of the specified antenna. The returned record
         represents a position measure, and can be used as such by the
         measures (me) tool.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         which : any = 0

      .. container:: methodparmtable

         Zero-based antenna ID in the ANTENNA table or antenna name.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the position of the (zero-based) 3rd antenna
   in the ANTENNA table antennna_position = msmd.antennaposition(3) #
   get the position of the antenna named DV07 antennna_position =
   msmd.antennaposition("DV07") msmd.done()

.. container:: param

   function **antennastations**

   .. container:: collcontent

      .. container:: methoddesc

         Get the station names of the specified antennas. If a specified
         antenna name is listed multiple times in the ANTENNA table,
         obsid is negative, and which is specified as an array of names,
         then the station associated with the largest ID for that
         antenna is returned. If obsid is nonnegative, returned stations
         are filtered based on that. If which is specified as a string
         (antenna name), then all the stations associated with that
         antenna are returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         which : any = -1

      .. container:: methodparmtable

         Zero-based antenna ID(s) in the ANTENNA table or antenna
         name(s). Single numeric id less than zero retrieves all station
         names.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. If negative, all observation IDs are considered.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get all station names stations =
   msmd.antennastations(-1) # get the stations of the antennas named
   DV07 and DV01 stations = msmd.antennaposition(["DV07", "DV01"])
   msmd.done()

.. container:: param

   function **antennasforscan**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique antennaIDs for the specified scan,
         observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scan : undefined = -1

      .. container:: methodparmtable

         Scan number for which to return the intents.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. If less than 0, all observation IDs are used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. If less than 0, all array IDs are used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the antennas associated with scan 4 (all
   observation IDs, all array IDs) antennas = msmd.antennasforscan(4)
   msmd.done()

.. container:: param

   function **bandwidths**

   .. container:: collcontent

      .. container:: methoddesc

         Get the bandwidths in Hz for the specified spectral windows. If
         spw less than zero, return bandwidths for all spectral windows.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : any = -1

      .. container:: methodparmtable

         Spectral window IDs, if integer less than zero, return
         bandwidths for all spectral windows.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get bandwdith for spectral window 2. baseband =
   msmd.bandwidth(2) msmd.done()

.. container:: param

   function **baseband**

   .. container:: collcontent

      .. container:: methoddesc

         Get the baseband for the specified spectral window.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Spectral window ID.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get baseband for spectral window 2. baseband =
   msmd.baseband(2) msmd.done()

.. container:: param

   function **baselines**

   .. container:: collcontent

      .. container:: methoddesc

         Get a two dimensional boolean array representing baselines for
         data recorded in the MS. A value of True means there is at
         least one row in the MS main table for that baseline, False
         means no rows for that baseline. Autocorrelation "baseline"
         information is also present via the values along the diagonal.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the baseline matrix for this data set
         baselines = msmd.baselines() msmd.done()

.. container:: param

   function **chanavgspws**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of spectral window IDs used for channel averages.
         These are windows that do have 1 channel.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the spectral window IDs used for
         channel averages. chan_avg_spws = msmd.chanavgspws()
         msmd.done()

.. container:: param

   function **chaneffbws**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of channel effective bandwidths for the specified
         spectral window. The parameter asvel indicates if velocity
         widths (True) or frequency widths (False) should be returned.
         The unit parameter specifies the units that the returned values
         should have. If empty (default), "Hz" will be used if
         asvel=False, or "km/s" will be used if asvel=True.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Spectral window ID.

.. container:: parameters2

   unit : undefined

.. container:: methodparmtable

   Desired unit of returned quantities. Empty means "Hz" if asvel=False,
   "km/s" if asvel=True.

.. container:: parameters2

   asvel : undefined = false

.. container:: methodparmtable

   Should return values be equivalent velocity widths?

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the channel effective bandwidths for
   spectral window 2, in m/s chan_ebw = msmd.chaneffbws(2, "m/s", True)
   msmd.done()

.. container:: param

   function **chanfreqs**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of channel frequencies for the specified spectral
         window.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Spectral window ID.

.. container:: parameters2

   unit : undefined = Hz

.. container:: methodparmtable

   Convert frequencies to this unit.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the channel frequencies for spectral window
   2. chan_freqs = msmd.chanfreqs(2) msmd.done()

.. container:: param

   function **chanres**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of channel resolutions for the specified spectral
         window. The parameter asvel indicates if velocity widths (True)
         or frequency widths (False) should be returned. The unit
         parameter specifies the units that the returned values should
         have. If empty (default), "Hz" will be used if asvel=False, or
         "km/s" will be used if asvel=True.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Spectral window ID.

.. container:: parameters2

   unit : undefined

.. container:: methodparmtable

   Desired unit of returned quantities. Empty means "Hz" if asvel=False,
   "km/s" if asvel=True.

.. container:: parameters2

   asvel : undefined = false

.. container:: methodparmtable

   Should return values be equivalent velocity resolutions?

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the channel resolutions for spectral window
   2, in m/s chan_res = msmd.chanres(2, "m/s", True) msmd.done()

.. container:: param

   function **chanwidths**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of channel widths for the specified spectral
         window.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Spectral window ID.

.. container:: parameters2

   unit : undefined = Hz

.. container:: methodparmtable

   Convert frequencies to this unit.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the channel widths for spectral window 2.
   chan_freqs = msmd.chanwidths(2) msmd.done()

.. container:: param

   function **close**

   .. container:: collcontent

      .. container:: methoddesc

         This method will close the tool and reclaim system resources it
         has been using. Returns true if successful.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # do things with tool # finish, close tool
         and free up resources. msmd.close()

.. container:: param

   function **corrprodsforpol**

   .. container:: collcontent

      .. container:: methoddesc

         Get the correlation products associated with the specified
         polarization ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         pol : undefined = -1

      .. container:: methodparmtable

         Polarization ID. Must be nonnegative.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get correlation products for polarization ID 3
   corrprods = msmd.corrprodsforpol(3) msmd.done()

.. container:: param

   function **corrtypesforpol**

   .. container:: collcontent

      .. container:: methoddesc

         Get the correlation types associated with the specified
         polarization ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         pol : undefined = -1

      .. container:: methodparmtable

         Polarization ID. Must be nonnegative.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get correlation types for polarization ID 3
   corrtypes = msmd.corrtypesforpol(3) msmd.done()

.. container:: param

   function **datadescids**

   .. container:: collcontent

      .. container:: methoddesc

         Get a list of data description IDs associated with the
         specified spectral window ID and/or polarization ID. Values of
         less than zero for either means all IDs should be used in the
         selection.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined = -1

      .. container:: methodparmtable

         Spectral window ID. Less than zero implies any,

.. container:: parameters2

   pol : undefined = -1

.. container:: methodparmtable

   Polarization ID. Less than zero implies any.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get all data description IDs associated with spw
   2. msmd.datadescids(spw=2) # same as before but limit the IDs
   returned to those associated with # polarization ID 3
   msmd.datadescids(spw=2, pol=3) msmd.done()

.. container:: param

   function **done**

   .. container:: collcontent

      .. container:: methoddesc

         This method will close the tool and reclaim system resources it
         has been using. Returns true if successful.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # do things with tool # finish, close tool
         and free up resources. msmd.done()

.. container:: param

   function **effexposuretime**

   .. container:: collcontent

      .. container:: methoddesc

         Get the effective exposure time (equivalent to what might be
         more commonly known as total integration time or total sample
         time) is calculated by summing over all rows in the main MS
         table, excluding autocorrelations or rows where FLAG\_ROW is
         false, thusly: sum[over i] (exposure[i]*sum[over j](UFBW[i,
         j])/ncorrelations[i] )/ nmaxbaselines where exposure[i] is the
         value of EXPOSURE for the ith row, the inner sum is performed
         over each correlation for that row, UFBW is the unflagged
         fractional bandwidth is determined by summing all the widths of
         the unflagged channels for that correlation and dividing by the
         total bandwidth of all spectral windows observed at the
         timestamp of row i, ncorrelations is the number of correlations
         determined by the number of rows in the FLAG matrix for MS row
         i, and nmaxbaselines is the maximum number of antenna pairs,
         nantennas*(nantennas-1)/2, where nantennas is the number of
         antennas in the ANTENNA table. This method returns a quantity
         (a dictionary having a numerical value and a string unit).

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the effective exposure time.
         exposure_time = msmd.effexposuretime() msmd.done()

.. container:: param

   function **exposuretime**

   .. container:: collcontent

      .. container:: methoddesc

         Get the exposure time for the specified scan, spwid,
         polarization ID, array ID, and observation ID. This is the
         exposure time of the record with the lowest time stamp of the
         records associated with these parameters. Returns a quantity
         dictionary. If polid is not specified (or specified and
         negative) and there is only one polarization ID in for the
         specified combination of scan, spwid, obsID, and arrayID, then
         that polarization ID is used. If there are multiple
         polarization IDs for the combination of other parameters, a
         list of these is logged and an empty dictionary is returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scan : undefined = 0

      .. container:: methodparmtable

         Scan number.

.. container:: parameters2

   spwid : undefined = 0

.. container:: methodparmtable

   Spectral window ID.

.. container:: parameters2

   polid : undefined = -1

.. container:: methodparmtable

   Polarization ID.

.. container:: parameters2

   obsid : undefined = 0

.. container:: methodparmtable

   Observation ID.

.. container:: parameters2

   arrayid : undefined = 0

.. container:: methodparmtable

   Array ID.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the exposure time for scan 1, spwid 2, and
   polid 3 # for obsid=0 and arrayid=0 integration_time =
   msmd.exposuretime(scan=1, spwid=2, polid=3) msmd.done()

.. container:: param

   function **fdmspws**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of spectral window IDs used for FDM. These are
         windows that do not have 64, 128, or 256 channels.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the spectral window IDs used for FDM.
         fdm_spws = msmd.fdmspws() msmd.done()

.. container:: param

   function **fieldnames**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of field names as they appear in the FIELD table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get list of field names in the ms
         fieldnames = msmd.fieldnames() msmd.done()

.. container:: param

   function **fieldsforintent**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique fields for the specified intent.
         Note that \* matches any number of characters of all character
         classes.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         intent : undefined

      .. container:: methodparmtable

         Intent (case sensitive) for which to return the fields.

.. container:: parameters2

   asnames : undefined = false

.. container:: methodparmtable

   If true, return the field names. If false, return the zero-based
   field IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field names for intent "observe target"
   field_names = msmd.fieldsforintent("observe target", True,
   regex=False) # get the field IDs for intent "observe target"
   field_IDs = msmd.fieldsforintent("observe target", False,
   regex=False) # get all field IDs for all intents which contain 'WVR'
   field_IDs = msmd.fieldsforIntent("*WVR*") msmd.done()

.. container:: param

   function **fieldsforname**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique, zero-based field IDs for the
         specified field name. If the field name is the empty string
         (the default), a list of all unique field IDs in the main table
         of the MS will be returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         name : undefined

      .. container:: methodparmtable

         Field name (case sensitive) for which to return the fields.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field IDs for field name "Enceladus"
   fields = msmd.fieldsforname("Enceladus") msmd.done()

.. container:: param

   function **fieldsforscan**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique fields for the specified scan
         number, observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scan : undefined = -1

      .. container:: methodparmtable

         Scan number for which to return the fields.

.. container:: parameters2

   asnames : undefined = false

.. container:: methodparmtable

   If true, return the field names. If false, return the zero-based
   field IDs.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value means use all observation IDs.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value means use all array IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field names for scan number 5 (for all
   array IDs and all observation IDs). field_names =
   msmd.fieldsforscan(5, True) # get the field IDs for scan number 5
   (for all array IDs and all observation IDs) field_IDs =
   msmd.fieldsforscan(5, False) msmd.done()

.. container:: param

   function **fieldsforscans**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array or dictionary of the unique fields for the
         specified scan numbers, observation ID, and array ID. If
         asnames=True, the values returned will be the field names, if
         False, they will be field IDs. If asmap=True, the structure
         returned will be a dictionary which maps scan number (as a
         string) to fields. In this case, both obsid and arrayid must be
         nonnegative. If asmap=False, a single array of fields is
         returned that matches the query. In this case, if obsid and/or
         arrayid are negative, then it indicates that all fields
         matching any obsid and/or arrayid should be returned. An empty
         array specified for scans means that all scans for the selected
         obsid and arrayid should be included.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scans : undefined

      .. container:: methodparmtable

         Scan numbers for which to return the fields.

.. container:: parameters2

   asnames : undefined = false

.. container:: methodparmtable

   If true, return the field names. If false, return the zero-based
   field IDs.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value means use all observation IDs.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value means use all array IDs.

.. container:: parameters2

   asmap : undefined = false

.. container:: methodparmtable

   Return a dictionary mapping scan numbers to fields?

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field names for scan numbers 5 and 10
   (all obsids, all arrayids) field_names = msmd.fieldsforscan([5, 10],
   True) # get the field IDs for scan numbers 5 and 10 (all obsids, all
   arrayids) field_IDs = msmd.fieldsforscan([5, 10], False) # get
   mapping of scans to fields for arrayid=2 and obsid=4 scans_to_fields
   = msmd.fieldsforscan(obsid=4, arrayid=2, asmap=True) msmd.done()

.. container:: param

   function **fieldsforsource**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique fields for the specified source.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         source : undefined = -1

      .. container:: methodparmtable

         Zero-based source ID for which to return the fields.

.. container:: parameters2

   asnames : undefined = false

.. container:: methodparmtable

   If true, return the field names. If false, return the zero-based
   field IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field names for source ID 1 field_names
   = msmd.fieldsforsource(1, True) # get the field IDs for source ID 1
   field_IDs = msmd.fieldsforsource(1, False) msmd.done()

.. container:: param

   function **fieldsforsources**

   .. container:: collcontent

      .. container:: methoddesc

         Get a map of source IDs to fields. The keys (source IDs) will
         be strings.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         asnames : undefined = false

      .. container:: methodparmtable

         If true, return the field names. If false, return the
         zero-based field IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the source to field name map
   sources_to_fields = msmd.fieldsforsources(True) # access the field
   names for source 1 field = sources_to_fields["1"] msmd.done()

.. container:: param

   function **fieldsforspw**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique fields for the specified spectral
         window.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined = -1

      .. container:: methodparmtable

         Zero-based spectral window ID for which to return the fields.

.. container:: parameters2

   asnames : undefined = false

.. container:: methodparmtable

   If true, return the field names. If false, return the zero-based
   field IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field names for spectral window 1
   field_names = msmd.fieldsforspw(1, True) # get the field IDs for
   spectral window 1 field_IDs = msmd.fieldsforspw(1, False) msmd.done()

.. container:: param

   function **fieldsfortimes**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique, zero-based, fieldIDs for the
         specified time range (time-tol to time+tol).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         time : undefined = -1

      .. container:: methodparmtable

         Time at center of time range.

.. container:: parameters2

   tol : undefined = 0

.. container:: methodparmtable

   Time on either side of center for specifying range.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field IDs associated with the specified
   time range fields = msmd.fieldsfortimes(4.8428293714e+09, 20)
   msmd.done()

.. container:: param

   function **intents**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique intents associated with the MS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the intents associated with the MS
         intents = msmd.intents() msmd.done()

.. container:: param

   function **intentsforfield**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique intents for the specified field.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : any = -1

      .. container:: methodparmtable

         Field ID or name for which to return the intents.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the intents associated with field 4 intents
   = msmd.intentsforfield(4) # get intents for field "MOS" intents2 =
   msmd.intentsforfield("MOS") msmd.done()

.. container:: param

   function **intentsforscan**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique intents for the specified scan,
         observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scan : undefined = -1

      .. container:: methodparmtable

         Scan number for which to return the intents.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value means use all observation IDs.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value means use all array IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the intents associated with scan 4 (all
   obsids, all arrayids) intents = msmd.intentsforscan(4) msmd.done()

.. container:: param

   function **intentsforspw**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique intents for the specified spectral
         window ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined = -1

      .. container:: methodparmtable

         Spectral window ID (\>=0) for which to return the intents.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the intents associated with spectral window
   ID 3 intents = msmd.intentsforspw(3) msmd.done()

.. container:: param

   function **meanfreq**

   .. container:: collcontent

      .. container:: methoddesc

         Get the mean frequency for the specified spectral window.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Spectral window ID.

.. container:: parameters2

   unit : undefined = Hz

.. container:: methodparmtable

   Convert frequencies to this unit.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the mean frequency for spectral window 2.
   mean_freq = msmd.meanfreq(2) msmd.done()

.. container:: param

   function **name**

   .. container:: collcontent

      .. container:: methoddesc

         Get the name of the attached MS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get its name myname = msmd.name()
         msmd.done()

.. container:: param

   function **namesforfields**

   .. container:: collcontent

      .. container:: methoddesc

         Get the name of the specified field.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         fieldids : any

      .. container:: methodparmtable

         Zero-based field IDs for which to get the names (integer or
         interger array). Unspecified will return all field names.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the name for field 8 and 2. field_names =
   msmd.namesforfields([8, 2]) # get all field names all_field_nams =
   namesforfields() msmd.done()

.. container:: param

   function **namesforspws**

   .. container:: collcontent

      .. container:: methoddesc

         Get the name of the specified spw(s).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spwids : any

      .. container:: methodparmtable

         Zero-based spw ID(s) for which to get the names (integer or
         interger array). Unspecified will return all spw names.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the name for spws 8 and 2. spw_names =
   msmd.namesforspws([8, 2]) # get all spw names all_spw_names =
   msmd.namesforspws() msmd.done()

.. container:: param

   function **nantennas**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of antennas associated with the MS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") number_of_antennas = msmd.nantennas()
         msmd.done()

.. container:: param

   function **narrays**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of arrays associated with the MS from the ARRAY
         table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") number_of_array_ids = msmd.narrays()
         msmd.done()

.. container:: param

   function **nbaselines**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of unique baselines (antenna pairs) represented
         in the main MS table. This can, in theory, be less than
         n*(n-1)/2 (n being the number of antennas in the ANTENNA
         table), if data for certain baselines are not included in the
         main MS table. Autocorrelation "baselines" are included in this
         count if ac=True.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         ac : undefined = false

      .. container:: methodparmtable

         Include auto-correlation "baselines"?

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") number_of_baselines = msmd.nbaselines()
   number_of_baselines_including_ac = msmd.nbaselines(True) msmd.done()

.. container:: param

   function **nchan**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of channels associated with the specified
         spectral window.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Zero-based spw ID for which to get the number of channels.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") nchan = msmd.nchan(3) msmd.done()

.. container:: param

   function **ncorrforpol**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of correlations for the specified polarization
         ID. If the specified polarization ID is negative, an array of
         numbers of correlations is returned. The indices of that array
         represent polarization IDs.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         polid : undefined = -1

      .. container:: methodparmtable

         Zero-based polarization ID. A negative number will cause all
         the numbers of correlations to be returned.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the number of correlations associated with
   polarization ID 4 polid = msmd.ncorrforpol(4) # get the array of
   numbers of correlations from the POLARIZATION table polids =
   msmd.ncorrforpol(-1) msmd.done()

.. container:: param

   function **nfields**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of fields associated with the MS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") number_of_fields = msmd.nfields()
         msmd.done()

.. container:: param

   function **nobservations**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of observations associated with the MS from the
         OBSERVATIONS table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") number_of_obs_ids = msmd.nobservations()
         msmd.done()

.. container:: param

   function **nspw**

   .. container:: collcontent

      .. container:: methoddesc

         This method will return the number of spectral windows in the
         associated MS.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         includewvr : undefined = true

      .. container:: methodparmtable

         Include wvr spectral windows? If false, exclude wvr windows
         from count.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") number_of_spectral_windows = msmd.nspw()
   msmd.done()

.. container:: param

   function **nstates**

   .. container:: collcontent

      .. container:: methoddesc

         This method will return the number of states (number of rows in
         the STATES table) in the associated MS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") number_of_states = msmd.nstates()
         msmd.done()

.. container:: param

   function **nscans**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of scans associated with the MS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") number_of_scans = msmd.nscans() msmd.done()

.. container:: param

   function **nsources**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of unique values from the SOURCE_ID column in
         the SOURCE table. The number of rows in the SOURCE table may be
         greater than this value.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") number_of_unique_source_ids =
         msmd.nsources() msmd.done()

.. container:: param

   function **nrows**

   .. container:: collcontent

      .. container:: methoddesc

         Get the number of visibilities (from the main table) associated
         with the MS.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         autoc : undefined = true

      .. container:: methodparmtable

         Include autocorrelation data? If False, only cross correlation
         rows will be summed.

.. container:: parameters2

   flagged : undefined = true

.. container:: methodparmtable

   Include flagged data? If False, only unflagged or patially flagged
   rows will be summed.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the total number of rows nrows =
   msmd.nrows() # got the number of cross correlation rows ncross =
   msmd.nrows(auto=False) # get the number of unflagged rows ngood =
   msmd.nrows(flagged=False) # get the number of unflagged cross
   correlation rows ncrossunflagged = msmd.nrows(auto=False,
   flagged=False) msmd.done()

.. container:: param

   function **observers**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of observers as they are listed in the
         OBSERVATIONS table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the observers observers =
         msmd.observers() msmd.done()

.. container:: param

   function **observatorynames**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of MS telescope (observatory) names as they are
         listed in the OBSERVATIONS table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the telescope names telescope_names =
         msmd.telescopenames() msmd.done()

.. container:: param

   function **observatoryposition**

   .. container:: collcontent

      .. container:: methoddesc

         Get the position of the specified telescope.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         which : undefined = 0

      .. container:: methodparmtable

         Zero-based telescope position in the OBSERVATIONS table (see
         msmd.telescopenames()).

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the position of the 0th telescope
   telescope_position = msmd.telescopeposition(0) msmd.done()

.. container:: param

   function **open**

   .. container:: collcontent

      .. container:: methoddesc

         Attach this tool to the specified MS. This method runs a few
         basic MS validation tests, and if any of these fail (which
         indicates that the MS is invalid), an error occurs and the tool
         is not attached to the MS. Note that it is ultimately the
         user's responsibility to ensure that the MS is valid. Running
         the methods of this tool on an invalid MS may result in
         incorrect results or even a crash of CASA. Such invalidities
         include any MS subtable not having appropriate information (eg,
         an OBSERVATION subtable not having enough rows to account for
         all the OBSERVATION_IDs in the main table).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msfile : undefined

      .. container:: methodparmtable

         Name of the existing measurement set

.. container:: parameters2

   maxcache : undefined = 50

.. container:: methodparmtable

   Maximum cache size, in megabytes, to use.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # do stuff and close it msmd.done()

.. container:: param

   function **phasecenter**

   .. container:: collcontent

      .. container:: methoddesc

         Get a direction measures for the phasecenter of the field id
         and time specified

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         fieldid : undefined = 0

      .. container:: methodparmtable

         Zero-based field ID for which to get the phasecenter; default
         fieldid=0

.. container:: parameters2

   epoch : undefined

.. container:: methodparmtable

   Optional time, expressed as a measures epoch dictionary, if field id
   has a polynomial in time phasecenter or an ephemerides table attached
   to the ID. Default value means evaluate at the origin TIME in the
   FIELD table

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get phasecenter for field ID 1 mydir =
   msmd.phasecenter(1); # if the phasecenter is a polynomial or has an
   ephemerides attached to # it a time is needed to get the phase
   direction ep=me.epoch('utc', '2015/03/15/15:30:55')
   mydir2=msmd.phasecenter(2, ep) msmd.done()

.. container:: param

   function **pointingdirection**

   .. container:: collcontent

      .. container:: methoddesc

         Get the pointing direction for antennas at the specified row
         number in the main MS table. Returns a record containing the
         time, antenna IDs and corresponding pointing directions.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         rownum : undefined = 0

      .. container:: methodparmtable

         Row number in the main MS table.

.. container:: parameters2

   interpolate : undefined = false

.. container:: methodparmtable

   Interpolate pointings in case the interval in the main table is
   shorter than that in the pointing table (often the case in
   fast-scanning in single dish observaitions)

.. container:: parameters2

   initialrow : undefined = 0

.. container:: methodparmtable

   Initial guess of row index in pointing table to start search.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the pointing directions for row ID 500 dirs
   = msmd.pointingdirection(500) msmd.done()

.. container:: param

   function **polidfordatadesc**

   .. container:: collcontent

      .. container:: methoddesc

         Get the polarization ID associated with the specified data
         description ID. If the specified data description ID is
         negative, an array of polarization IDs is returned. The indices
         of that array represent data description IDs.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         ddid : undefined = -1

      .. container:: methodparmtable

         Zero-based data description ID. A negative number will cause
         all the polarization IDs to be returned.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the polarization ID associated with data
   description ID 3 polid = msmd.polidfordatadesc(3) # get the array of
   polarization IDs in the order they appear in the DATA_DESCRIPTION
   table polids = msmd.polidfordatadesc(-1) msmd.done()

.. container:: param

   function **projects**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of projects as they are listed in the OBSERVATIONS
         table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the projects projects =
         msmd.projects() msmd.done()

.. container:: param

   function **propermotions**

   .. container:: collcontent

      .. container:: methoddesc

         Get the values of the DIRECTION column from the SOURCE table.
         Returns a dictionary in which the keys are the associated
         zero-based row numbers, represented as strings, in the SOURCE
         table. The associated values are two element dictionaries, with
         keys "longitude" and "latitude", containing the longitudinal
         and latidinal components of the proper motion, which are valid
         quantity dictionaries.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get PROPER_MOTION column values from the
         SOURCE table mu = msmd.propermotions() msmd.done() # the
         direction associated with zero-based row number 10 mu10 =
         mu["10"]

.. container:: param

   function **refdir**

   .. container:: collcontent

      .. container:: methoddesc

         Get a direction measure for the reference direction of the
         field and time specified

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : any = 0

      .. container:: methodparmtable

         Zero-based field ID or field name for which to get the
         reference direction; default field=0

.. container:: parameters2

   epoch : undefined

.. container:: methodparmtable

   Optional time, expressed as a measures epoch dictionary, if
   associated field has a polynomial in time reference direction or an
   ephemerides table attached it. Default value means evaluate at the
   origin TIME in the FIELD table

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get reference direction for field ID 1 mydir =
   msmd.refdir(1); # if the reference direction is a polynomial or has
   an ephemerides attached to # it a time is needed to get the reference
   direction ep=me.epoch('utc', '2015/03/15/15:30:55')
   mydir2=msmd.phasecenter(2, ep) msmd.done()

.. container:: param

   function **reffreq**

   .. container:: collcontent

      .. container:: methoddesc

         Get the reference frequency of the specified spectral window.
         The returned frequency is in the form of a valid measures
         dictionary.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined = -1

      .. container:: methodparmtable

         Zero-based spectral window ID.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the reference frequency for spw ID 20
   reffreq = msmd.reffreq(20) msmd.done()

.. container:: param

   function **restfreqs**

   .. container:: collcontent

      .. container:: methoddesc

         Get the rest frequencies from the SOURCE table for the
         specified source and spectral window. The return value will be
         a dictionary of frequency measures if the rest frequencies are
         defined for the specified inputs, or False if they do not.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         sourceid : undefined = 0

      .. container:: methodparmtable

         Zero-based source ID (from the SOURCE::SOURCE_ID column).

.. container:: parameters2

   spw : undefined = 0

.. container:: methodparmtable

   Zero-based spectral window ID.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the rest frequencies for source ID 2 and spw
   ID 20 reffreq = msmd.restfreqs(2, 20) msmd.done()

.. container:: param

   function **scannumbers**

   .. container:: collcontent

      .. container:: methoddesc

         This method will return an array of unique scan numbers in the
         associated MS for the specified observation ID and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         obsid : undefined = -1

      .. container:: methodparmtable

         Observation ID. A negative value indicates all observation IDs
         should be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # scan numbers for all obsids and all arrayids
   scan_numbers = msmd.scannumbers() msmd.done()

.. container:: param

   function **scansforfield**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique scan numbers associated with the
         specified field, observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : any

      .. container:: methodparmtable

         Field ID or field name (case sensitive) for which to return the
         scan numbers.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value indicates all observation IDs should
   be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the scan numbers associated with field
   "planet Z" (all obsids, all arrayids) scan_numbers =
   msmd.scansforfield("planet Z") # get the scan numbers associated with
   field ID 5 (all obsids, all arrayids) scan_numbers =
   msmd.scansforfield(5) msmd.done()

.. container:: param

   function **scansforfields**

   .. container:: collcontent

      .. container:: methoddesc

         Get a dictionary of which maps field ID to scan numbers for the
         specified observation ID and array ID. The keys (field IDs)
         will be strings. obsid and arrayid must both be non-negative.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         obsid : undefined = 0

      .. container:: methodparmtable

         Observation ID. Must be non-negative.

.. container:: parameters2

   arrayid : undefined = 0

.. container:: methodparmtable

   Array ID. Must be non-negative.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the field - scan map for arrayID 1 and obsID
   2 field_to_scans = msmd.scansforfields(arrayid=1, obsid=2) # access
   the scans associated with field ID 2 field_to_scans2 =
   field_to_scans["2"] msmd.done()

.. container:: param

   function **scansforintent**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique scan numbers associated with the
         specified intent, observation ID, and arrayID. The "*"
         character matches any number of characters from all character
         classes.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         intent : undefined

      .. container:: methodparmtable

         Intent (case-sensitive) for which to return the scan numbers.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value indicates all observation IDs should
   be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the scan numbers associated with intent
   "detect planet X" (all obsids, all arrayids) scan_numbers =
   msmd.scansforintent("detect planet X", regex=False) # got all the
   scan numbers associated with all intents which contain 'WVR' (all
   obsids, all arrayids) scan_numbers = msmd.scansforintent("*WVR*")
   msmd.done()

.. container:: param

   function **scansforspw**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique scan numbers associated with the
         specified zero-based spectral window ID, observation ID, and
         array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined = -1

      .. container:: methodparmtable

         Zero-based spectral window ID for which to return the scan
         numbers.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value indicates all observation IDs should
   be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the scan numbers associated with spectral
   window ID 14, all obsids, all arrayids scan_numbers =
   msmd.scansforspw(14) msmd.done()

.. container:: param

   function **scansforspws**

   .. container:: collcontent

      .. container:: methoddesc

         Get a dictionary of which maps spw ID to scan numbers for the
         specified observation ID and array ID. The keys (spectral
         window IDs) will be strings. obsid and arrayid must both be
         non-negative.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         obsid : undefined = 0

      .. container:: methodparmtable

         Observation ID. Must be non-negative.

.. container:: parameters2

   arrayid : undefined = 0

.. container:: methodparmtable

   Array ID. Must be non-negative.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the spw - scan map for arrayID 1 and obsID 2
   spw_to_scans = msmd.scansforspws(arrayid=1, obsid=2) # access the
   scans associated with spw ID 2 spw_to_scans2 = spw_to_scans["2"]
   msmd.done()

.. container:: param

   function **scansforstate**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique scan numbers for the specified
         state, observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         state : undefined = -1

      .. container:: methodparmtable

         ID of state for which to return the scan numbers.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value indicates all observation IDs should
   be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the scan numbers associated with state 2,
   all obsids, all arrayids scans = msmd.scansforstate(2) msmd.done()

.. container:: param

   function **scansfortimes**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique scan numbers for the specified time
         range (time-tol to time+tol), observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         time : undefined = -1

      .. container:: methodparmtable

         Time at center of time range.

.. container:: parameters2

   tol : undefined = 0

.. container:: methodparmtable

   Time difference on either side of center for specifying range.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value indicates all observation IDs should
   be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the scan numbers associated with the
   specified time range (all obsids, all array ids) scans =
   msmd.scansfortimes(4.84282937e+09, 20) msmd.done()

.. container:: param

   function **schedule**

   .. container:: collcontent

      .. container:: methoddesc

         Get the schedule information for the specified observation ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         obsid : undefined = -1

      .. container:: methodparmtable

         Observation ID.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the schdule information for observation ID =
   2 schedule = msmd.schedule()[2] msmd.done()

.. container:: param

   function **sideband**

   .. container:: collcontent

      .. container:: methoddesc

         Get the sideband for the specified spectral window.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : undefined

      .. container:: methodparmtable

         Spectral window ID.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get sideband for spectral window 2. sideband =
   msmd.sideband(2) msmd.done()

.. container:: param

   function **sourcedirs**

   .. container:: collcontent

      .. container:: methoddesc

         Get the values of the DIRECTION column from the SOURCE table.
         Returns a dictionary in which the keys are the associated row
         numbers, represented as strings, in the SOURCE table. Each
         value in the returned dictionary is a valid direction measure.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get DIRECTION column values from the
         SOURCE table sourcedirs = msmd.sourcedirs() msmd.done() # the
         direction associated with zero-based row number 10 dir10 =
         sourcedirs["10"] # convert it to B1950, using the measure
         interface dir10_B1950 = me.convert(dir10, "B1950")

.. container:: param

   function **sourcetimes**

   .. container:: collcontent

      .. container:: methoddesc

         Get the values of the TIME column from the SOURCE table.
         Returns a dictionary in which the keys are the associated row
         numbers, represented as strings, in the SOURCE table. Each
         value in the returned dictionary is a valid time quantity.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get TIME column values from the SOURCE
         table sourcetimes = msmd.sourcetimes() msmd.done() # the time
         associated with zero-based row number 10 time10 =
         sourcetimes["10"]

.. container:: param

   function **sourceidforfield**

   .. container:: collcontent

      .. container:: methoddesc

         Get the source ID from the field table for the specified field
         ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : undefined = -1

      .. container:: methodparmtable

         Zero-based field ID for which to return the source ID from the
         field table.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get source ID associated with field ID 2
   sourceid = msmd.sourceidforfield(2) msmd.done()

.. container:: param

   function **sourceidsfromsourcetable**

   .. container:: collcontent

      .. container:: methoddesc

         Get the values of the SOURCE_ID column from the SOURCE table.
         It is unfortunate that the SOURCE table has a column named
         SOURCE_ID, because implicitly the "ID" of a row in an MS
         subtable is generally meant to reflect a row number in that
         table, but that is not the case for the SOURCE table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get SOURCE_ID column values from the
         SOURCE table sourceids = msmd.sourceidsfromsourcetable()
         msmd.done()

.. container:: param

   function **sourcenames**

   .. container:: collcontent

      .. container:: methoddesc

         Get the values of the SOURCE_NAME column from the SOURCE table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get SOURCE_NAME column values from the
         SOURCE table sourcenames = msmd.sourcenames() msmd.done()

.. container:: param

   function **spwsforbaseband**

   .. container:: collcontent

      .. container:: methoddesc

         Get the spectral windows associated with the specified baseband
         or dictionary that maps baseband to spectral windows.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         baseband : undefined = -1

      .. container:: methodparmtable

         Baseband number. If \\<0, return a dictionary mapping basebands
         to spws.

.. container:: parameters2

   sqldmode : undefined = include

.. container:: methodparmtable

   If "include", include SQLD windows, if "exclude", exclude SQLD
   windows, if "only", include only SQLD windows. Case insenstive,
   inimum match honored.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the spectral window IDs associated with all
   the basebands in this dataset basebandtospwdict =
   msmd.spwsforbasebands() # get an array of spws associated with
   baseband 2. spwsforbb2 = msmd.spwsforbasebands(2) msmd.done()

.. container:: param

   function **spwfordatadesc**

   .. container:: collcontent

      .. container:: methoddesc

         Get the spectral window ID associated with the specified data
         description ID. If the specified data description ID is
         negative, an array of spectral window IDs is returned. The
         indices of that array represent data description IDs.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         ddid : undefined = -1

      .. container:: methodparmtable

         Zero-based data description ID. A negative number will cause
         all the spectral window IDs to be returned.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the spectral window ID associated with data
   description ID 3 spw = msmd.spwfordatadesc(3) # get the array of
   spectral window IDs in the order they appear in the DATA_DESCRIPTION
   table spws = msmd.spwfordatadesc(-1) msmd.done()

.. container:: param

   function **spwsforfield**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique spectral window IDs for the
         specified field.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : any

      .. container:: methodparmtable

         Field (case sensitive string or zero-based integer ID) for
         which to return the spectral window IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the spectral window IDs associated with
   field "Fomalhaut" spws = msmd.spwsforfield("Fomalhaut") # get
   spectral window IDs associated with field ID 2 spws =
   msmd.spwsforfield(2) msmd.done()

.. container:: param

   function **spwsforfields**

   .. container:: collcontent

      .. container:: methoddesc

         Get a dictionary which maps field IDs to spectral window IDs.
         The field IDs are keys in the returned dictionary. To access a
         particular element, one must ensure the key is a string.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the map of field IDs to spw IDs
         field_to_spw_map = msmd.spwsforfields() spws_for_field_5 =
         field_to_spw_map[str(5)] msmd.done()

.. container:: param

   function **spwsforintent**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique spectral window IDs for the
         specified intent. The "*" character matches any number of
         characters from all character classes.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         intent : undefined

      .. container:: methodparmtable

         Intent (case sensitive) for which to return the spectral window
         IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the spectral window IDs associated with "MY
   COOL INTENT" spws = msmd.spwsforintent("MY COOL INTENT") # got all
   the spw IDs associated with all intents which contain 'WVR'
   scan_numbers = msmd.spwsforintent("*WVR*") msmd.done() msmd.done()

.. container:: param

   function **spwsfornames**

   .. container:: collcontent

      .. container:: methoddesc

         Get the IDs of the specified spw(s). Returns a dictionary where
         the keys are the requested spectral window names that are
         present in the data set and the values are arrays of the
         spectral window IDs corresponding to the name. If a specified
         name is not present, a warning message is logged and that name
         is not included in the returned dictionary. Specifying no names
         results in a dictionary containing the name to spw ID mapping
         for the entire data set.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spwids : any

      .. container:: methodparmtable

         Names of the spws for which IDs are needed (string or string
         array). Unspecified will return all spw names.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the IDs for spws named "CO" and "HCN"
   spw_ids = msmd.spwsfornames(["CO", "HCN"]) # get the complete spw
   name to ID map spw_names_to_ids = msmd.spwsfornames() msmd.done()

.. container:: param

   function **spwsforscan**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique spectral window IDs for the
         specified scan number, observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scan : undefined = -1

      .. container:: methodparmtable

         Scan number for which to return the spectral window IDs.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value means that all observation IDs
   should be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value means that all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the spectral window IDs associated with scan
   number 20, all obsids, all arrayids. spws = msmd.spwsforscan(20)
   msmd.done()

.. container:: param

   function **spwsforscans**

   .. container:: collcontent

      .. container:: methoddesc

         Get a dictionary of which maps scan number to spectral windows
         for the specified observation ID and array ID. The keys (scan
         numbers) will be strings. obsid and arrayid must both be
         non-negative.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         obsid : undefined = 0

      .. container:: methodparmtable

         Observation ID. Must be non-negative.

.. container:: parameters2

   arrayid : undefined = 0

.. container:: methodparmtable

   Array ID. Must be non-negative.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the scan - spw map for arrayID 1 and obsID 2
   scan_to_spws = msmd.spwsforscans(arrayid=1, obsid=2) # access the
   spws associated with scan 2 spws_for_scan2 = scan_to_spws["2"]
   msmd.done()

.. container:: param

   function **statesforscan**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique state IDs for the specified scan
         number, observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scan : undefined = -1

      .. container:: methodparmtable

         Scan number for which to return the state IDs.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value means that all observation IDs
   should be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value means that all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the state IDs associated with scan number
   251, all obsids, all arrayids states = msmd.statesforscan(251)
   msmd.done()

.. container:: param

   function **statesforscans**

   .. container:: collcontent

      .. container:: methoddesc

         Get a dictionary which maps scan numbers to state IDs for the
         specified array and observation IDs. The returned dictionary
         will have scan numbers, as strings, as keys.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         obsid : undefined = 0

      .. container:: methodparmtable

         Observation ID, must be nonnegative.

.. container:: parameters2

   arrayid : undefined = 0

.. container:: methodparmtable

   Array ID, must be nonnegative.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the map of scan numbers to state IDs for
   arrayID=1, obsID=2 scans_to_states = msmd.statesforscans(obsID=2,
   arrayID=1) states_for_scan_5 = scans_to_states[str(5)] msmd.done()

.. container:: param

   function **summary**

   .. container:: collcontent

      .. container:: methoddesc

         Get dictionary summarizing the MS.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the summary summary = msmd.summary()
         msmd.done()

.. container:: param

   function **tdmspws**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of spectral window IDs used for TDM. These are
         windows that have 64, 128, or 256 channels.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         msmd.open("my.ms") # get the spectral window IDs used for TDM.
         tdm_spws = msmd.tdmspws() msmd.done()

.. container:: param

   function **timerangeforobs**

   .. container:: collcontent

      .. container:: methoddesc

         Get the time range for the specified observation ID. The return
         value is a dictionary containing keys "begin" and "end". Each
         of the associated value are dictionaries representing epochs
         which are valid measure records. The values are taken directly
         from the OBSERVATION subtable; no half-intervals are added or
         subtracted.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         obsid : undefined = -1

      .. container:: methodparmtable

         Zero-based observation ID for which to get the time range.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the time range associated with observation
   ID 3 timerange = msmd.timerangeforobs(3) msmd.done()

.. container:: param

   function **timesforfield**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique times for the specified field.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : undefined = -1

      .. container:: methodparmtable

         Zero-based field ID for which to return the times.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the times associated with field 3 times =
   msmd.timesforfields(3) msmd.done()

.. container:: param

   function **timesforintent**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique times for the specified intent.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         intent : undefined

      .. container:: methodparmtable

         Intent for which to return the times.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the times associated with intent "myintent"
   times = msmd.timesforintent("myintent") msmd.done()

.. container:: param

   function **timesforscan**

   .. container:: collcontent

      .. container:: methoddesc

         Get the unique times for the specified scan number, observation
         ID, and array ID. If perspw=True, the returned data structure
         is a dictionary that has keys representing zero-based spectral
         window IDs and values representing the unique values of the
         TIME column corrsponding to the specified scan and that
         corresponding spectral window ID. If False, an array of unique
         values from the TIME column for the specified scan is returned;
         there is no separation into spectral window IDs.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scan : undefined = -1

      .. container:: methodparmtable

         Scan number for which to return the times.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value indicates all observation IDs should
   be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: parameters2

   perspw : undefined = false

.. container:: methodparmtable

   Return output dictionary with keys representing spectral window IDs
   (True), or an array of all times (False).

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the times associated with scan number 10,
   all obsids, all arrayids. times = msmd.timesforscan(10) msmd.done()

.. container:: param

   function **timesforscans**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of the unique times for the specified scan
         numbers, observation ID, and array ID.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         scans : any = -1

      .. container:: methodparmtable

         Scan number(s) for which to return the times.

.. container:: parameters2

   obsid : undefined = -1

.. container:: methodparmtable

   Observation ID. A negative value indicates all observation IDs should
   be used.

.. container:: parameters2

   arrayid : undefined = -1

.. container:: methodparmtable

   Array ID. A negative value indicates all array IDs should be used.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the times associated with scan numbers 10
   and 20, all obsids, all arrayids times = msmd.timesforscans([10,20])
   msmd.done()

.. container:: param

   undefined **timesforspws**

   .. container:: collcontent

      .. container:: methoddesc

         Get the unique times corresponding to the specified spectral
         window(s). The input indicates the spws for which times are to
         be retrieved, and can be a single integer or an array of
         integers. If a single, non-negative integer, an array of unique
         times associated with that spectral window are returned.
         Otherwise, a dictionary of times associated with the specified
         spectral windows are returned, with the spws (as strings) as
         the keys and the times as the values. A negative integer will
         cause a dictionary of all spws and their associated times to be
         returned.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spw : any = -1

      .. container:: methodparmtable

         Zero-based spectral window ID(s). A negative integer will cause
         the all the times for all spws to be returned.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the times associated with spws 10 and 20
   times = msmd.timesforspws([10,20]) # print the times for spw 10 print
   times["10"] msmd.done()

.. container:: param

   function **transitions**

   .. container:: collcontent

      .. container:: methoddesc

         Get the spectral transitions from the SOURCE table for the
         specified source and spectral window. The return value will be
         an array of transitions if the transitions are defined for the
         specified inputs, or False if they do not.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         sourceid : undefined = 0

      .. container:: methodparmtable

         Zero-based source ID (from the SOURCE::SOURCE_ID column).

.. container:: parameters2

   spw : undefined = 0

.. container:: methodparmtable

   Zero-based spectral window ID.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the transitions for source ID 2 and spw ID
   20 reffreq = msmd.transitions(2, 20) msmd.done()

.. container:: param

   function **wvrspws**

   .. container:: collcontent

      .. container:: methoddesc

         Get an array of spectral window IDs used for WVR. These are
         windows that have 4 channels. If complement is True, return the
         complement set instead (all non-wvr spw IDs). WVR windows are
         identified using the algorithm 1. check for water vapor
         radiometer (WVR) spectral windows using the spectral window
         name "WVR#NOMINAL" and report these. 2. If no SPWs match that
         string, then the names are checked for "WVR" and are reported
         instead.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         complement : undefined = false

      .. container:: methodparmtable

         If True, return all non-wvr spws.

.. container:: methodsection

   Example

.. container:: methodexam

   msmd.open("my.ms") # get the spectral window IDs used for WVR.
   wvr_spws = msmd.wvrspws() msmd.done()

.. container:: section
   :name: viewlet-below-content-body
