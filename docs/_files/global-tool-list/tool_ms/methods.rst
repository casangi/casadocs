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

            constructor **ms**

            .. container:: collcontent

               .. container:: methoddesc

                  This is the most commonly used constructor. It creates
                  an ms tool which is attached to the specified
                  measurement set table. By default the table is opened
                  read only to prevent you from accidently making
                  changes to the measurement set. Set nomodify to False
                  you you do intend to make changes. Setting the lock
                  argument to True will permanently lock the table
                  preventing other processes from writing to the
                  measurement set. Unless you expect this to happen, and
                  want to prevent it, you should leave the lock argument
                  at the default value which implies auto-locking. The
                  host argument specifies which machine the precompiled
                  ms process should be started on. The default value
                  starts it on the same machine as the one that casapy
                  is running on. In order to run the ms tool on a remote
                  machine you need to satisfy all the following
                  conditions. \\begin{itemize} \\item It must be
                  possible to start casa on the remote machine \\item
                  You must be able to log onto the remote machine
                  without having to type a password \\item The CASAPATH
                  environment variable must be defined on the remote
                  machine. You may want to set this up in the relevant
                  \``dot'' file eg., adding a line like
                  \\texttt{source~/usr/local/aips++/aipsinit.csh} in
                  your .cshrc file (for csh). \\end{itemize} One quick
                  way to check if all three conditions are met is to
                  type, on your local machine (rsh host 'echo
                  \\\$CASAPATH') where host is replaced by the name of
                  the remote machine. If the value of the CASAPATH
                  variable that is printed does not contain something
                  like {aips-root~architecture~site~host} and that all
                  the values are correct for the remote machine you can
                  be certain that starting the ms tool, or any casa
                  server, on the remote host will not work. Each ms tool
                  can only run one function at a time. To solve this you
                  start two servers. The forcenewserver argument allows
                  you to do this by overriding the default behaviour of
                  having each ms tool share the same server. This
                  function returns an ms tool or fail if something went
                  wrong, like an error in the measurement set name.

               .. container:: methodsection

                  Parameters : None

               .. container:: methodsection

                  Example

               .. container:: methodexam

                  See the example for the nrow function.

         .. container:: param

            function **open**

            .. container:: collcontent

               .. container:: methoddesc

                  Use this function when you have detached (using the
                  close function) the ms tool from a measurement set
                  table and wish to reattach to another measurement set
                  table. If check=true, additional referential integrity
                  checks on the MS are run. If any of these fail, an
                  exception is thrown and the MS is not open (since it
                  is not a valid MS).

               .. container:: methodsection

                  Parameters

               .. container:: parameters2

                  thems : undefined

               .. container:: methodparmtable

                  Name of the measurement set table to open.

.. container:: parameters2

   nomodify : undefined = true

.. container:: methodparmtable

   Prevent changes to the measurement set.

.. container:: parameters2

   lock : undefined = false

.. container:: methodparmtable

   Lock the table for exclusive use by this tool.

.. container:: parameters2

   check : undefined = false

.. container:: methodparmtable

   Run additional internal integrity checks on the MS.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') ms.close() ms.open("anotherms",
   nomodify=False, lock=False)

.. container:: param

   function **reset**

   .. container:: collcontent

      .. container:: methoddesc

         This function re-attaches the ms tool to the original MS,
         effectively discarding any prior operations, in particular any
         data selection operations using msselect function.

      .. container:: methodsection

         Parameters : None

.. container:: param

   function **close**

   .. container:: collcontent

      .. container:: methoddesc

         This function detaches the ms tool from the associated
         measurement set table after flushing all the cached changes.
         After calling this function the ms tool is not associated with
         any measurement set and using any function other than open or
         fromfits will result in an error message being sent to the
         logger. This function can be useful to avoid synchronization
         problems which can occur when different processes have the same
         ms open.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         See the example for the open function.

.. container:: param

   function **done**

   .. container:: collcontent

      .. container:: methoddesc

         You should call close() when you are finished using the ms tool
         to close the measurement set table and free any associated file
         locks. The measurement set is not deleted.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open("3C273XC1.MS") ... ms.done()

.. container:: param

   function **name**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns the name of the measurement set table
         that is being manipulated. If the ms tool is not attached to
         any measurement set, this function will return the string
         \``none''.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open('3C273XC1.MS') print "Processing file", ms.name()

.. container:: param

   function **iswritable**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns True if the underlying MeasurementSet was
         opened for writing/update.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open('3C273XC1.MS',nomodify=False) if ms.iswritable(): print
         "MeasurementSet is writable" else: print "MeasurementSet is
         readonly" #MeasurementSet is writable

.. container:: param

   function **nrow**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns the number of rows in the measurement
         set. If the optional argument selected is set to True, it
         returns the number of currently selected rows, otherwise it
         returns the number of rows in the original measurement set.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         selected : undefined = false

      .. container:: methodparmtable

         Return number of selected rows.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') print "Number of rows in ms =", ms.nrow()
   ms.msselect({'field':'3C273'}) print "Number of rows in selected ms
   =", ms.nrow(True)

.. container:: param

   function **getdata**

   .. container:: collcontent

      .. container:: methoddesc

         This function reads the specified items from the currently
         selected measurement set and returns them in fields of a
         record. The main difference between this and direct access of
         the table, using the table tool, is that this function reads
         data from the selected measurement set, provides access to
         derived quantities like amplitude and flag_sum, and can reorder
         the data. As with the ms.range function, the items to read are
         specified using a vector of strings. Allowable items include:
         'amplitude', 'corrected_amplitude', 'model_amplitude',
         'ratio_amplitude', 'residual_amplitude',
         'obs_residual_amplitude', 'antenna1', 'antenna2', 'axis_info',
         'data', 'corrected_data', 'float_data', 'model_data',
         'ratio_data', 'residual_data', 'obs_residual_data', 'feed1',
         'feed2', 'field_id', 'flag', 'flag_row', 'flag_sum', 'ha'
         (added to 'axis_info'), 'ifr_number', 'imaginary',
         'corrected_imaginary', 'model_imaginary', 'ratio_imaginary',
         'residual_imaginary', 'obs_residual_imaginary', 'last' (added
         to 'axis_info'), 'phase', 'corrected_phase', 'model_phase',
         'ratio_phase', 'residual_phase', 'obs_residual_phase', 'real',
         'corrected_real', 'ratio_real', 'residual_real',
         'obs_residual_real', 'scan_number', 'sigma', 'data_desc_id',
         'time', 'ut' (added to 'axis_info'), 'uvw', 'u', 'v', 'w',
         'uvdist', and 'weight'. Unrecognized items will result in a
         warning being sent to the logger. Corrected, model, and float
         visibilities will result in a warning if these columns do not
         exist. Duplicate items are silently ignored. Note that 'ha',
         'last', and 'ut' must be requested along with 'axis_info' and
         ifraxis=True. This data will be found in a subrecord of the
         returned record's 'axis_info' with the key in uppercase. For
         example, for 'ut', the data is found in:
         rec['axis_info']['time_axis']['UT']. See more information about
         'axis_info' below. The record that is returned contains fields
         that correspond to each of the specified items. Most fields
         will contain an array. The array may be one, two or three
         dimensional depending on whether the corresponding row in the
         measurement set is a scalar, one-, or two-dimensional. Unless
         the ifraxis argument is set to True, the length of the last
         axis on these arrays will correspond to the number of rows in
         the selected measurement set. If the ifraxis argument is set to
         True, the row axis is split into an interferometer axis and a
         time axis. For example, a measurement set with 90 rows, in an
         array with 6 telescopes (so that there are 15 interferometers),
         may have a data array of shape [4,32,90] if ifraxis is False,
         or [4,32,15,6] if ifraxis is True (assuming there are 4
         correlations and 32 channels). If there are missing rows, as
         will happen if not all interferometers were used for all
         time-slots, then a default value will be inserted. This
         splitting of the row axis may not happen for items where there
         is only a single value per row. For some items the returned
         vector will contain only as many values as there are
         interferometers and it is implicit that the same value should
         be used for all time slots. The antenna1, antenna2, feed1,
         feed2 and ifr_number items fall in this category. For other
         items, the returned vector will have as many values as there
         are time slots and it is implicit that the same value should be
         used for all interferometers. The field_id, scan_number,
         data_desc_id, and time items fall into this category. The
         'axis_info' item provides data labelling information. It
         returns a record with the following fields: corr_axis,
         freq_axis, ifr_axis, and time_axis. The latter two fields are
         not present if ifraxis is set to False. 1. The corr_axis field
         contains a string vector with elements like 'RR' or 'XY' that
         indicates which polarizations were correlated together to
         produce the data. The length of this vector will always be the
         same as the length of the first axis of the data array. 2. The
         freq_axis field contains a record with two fields, chan_freq
         and resolution. Each of these fields contains vectors which
         indicate the centre frequency and spectral resolution (FWHM) of
         each channel. The length of these vectors will be the same as
         the length of the second axis in the data. 3. The ifr_axis
         field contains fields: ifr_number, ifr_name, ifr_shortname and
         baseline. The ifr_number is the same as returned by the
         'ifr_number' item, 1000*antenna1+antenna2. The ifr_name and
         ifr_shortname are string vectors containing descriptions of the
         interferometer; ifr_name contains the names of the antenna pair
         separated by a hyphen, and ifr_shortname contains the ids of
         the antenna pair separated by a hyphen. The baseline is the
         Euclidian distance in meters between the two antennas. All of
         these vectors have a length equal to the number of
         interferometers in the selected measurement set, i.e., to the
         length of the third axis in the data when ifraxis is True. 4.
         The time_axis field contains the MJD seconds field and
         optionally the HA, UT, and LAST fields. To include the optional
         fields, you need to add 'ha', 'last' or 'ut' strings to the
         list of requested items. All of the fields in the time_axis
         record contain vectors that indicate the time at the midpoint
         of the observation and are in seconds. The MJD seconds field is
         since 0 hours on the day having a modified julian day number of
         zero and the rest are since midnight prior to the start of the
         observation. An optional gap size can be specified to visually
         separate groups of interferometers with the same antenna1 index
         (handy for identifying antennas in an interferometer vs time
         display). The default is no gap. An optional increment can be
         specified to return data from every row matching the increment
         only. When the average flag is set, the data will be averaged
         over the time axis if the ifraxis is True or the row axis i.e.,
         different interferometers and times may be averaged together.
         In the latter case, some of the coordinate information, like
         antenna_id, will no longer make sense. When all data to be
         averaged is unflagged, the result is the averaged value and the
         corresponding flag is False. When all data is flagged, the
         result is set to zero and the corresponding flag is True. When
         data to be averaged is mixed (unflagged and flagged), only the
         unflagged values are averaged and the flag is set to False. You
         need to call selectinit before calling this function. If you
         haven't then selectinit will be called for you with default
         arguments. Items prefixed with corrected, model, residual or
         obs_residual are not available unless your measurement set has
         been processed either with the imager or calibrator tools.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Item names

.. container:: parameters2

   ifraxis : undefined = false

.. container:: methodparmtable

   Create interferometer axis if True.

.. container:: parameters2

   ifraxisgap : undefined = 0

.. container:: methodparmtable

   Gap size on ifr axis when antenna1 changes.

.. container:: parameters2

   increment : undefined = 1

.. container:: methodparmtable

   Row increment for data access.

.. container:: parameters2

   average : undefined = false

.. container:: methodparmtable

   Average the data in time or over rows.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinit(datadescid=0) # Get amplitude
   and MJDseconds d = ms.getdata(["amplitude","axis_info"],
   ifraxis=True) tstart = min(d["axis_info"]["time_axis"]["MJDseconds"])
   tstop = max(d["axis_info"]["time_axis"]["MJDseconds"]) maxamp =
   max(max(d["amplitude"][:,0,0,0]), max(d["amplitude"][0,:,0,0]),
   max(d["amplitude"][0,0,:,0]), max(d["amplitude"][0,0,0,:])) print
   "MJD start time (seconds) =", tstart # MJD start time (seconds) =
   4121629400.0 print "MJD stop time (seconds) =", tstop # MJD stop time
   (seconds) = 4121642670.0 # MJDseconds Correlation amplitude print
   "Maximum correlation amplitude =", maxamp # Maximum correlation
   amplitude = 33.5794372559 chan = 0 corr = 0 freqGHz =
   d["axis_info"]["freq_axis"]["chan_freq"][chan]/1.0E9 baselineStr =
   d["axis_info"]["ifr_axis"]["ifr_name"][corr] corrStr =
   d["axis_info"]["corr_axis"][corr] tcoord =
   d["axis_info"]["time_axis"]["MJDseconds"] acoord =
   d["amplitude"][0,0,0,:] print "Frequency", freqGHz, "GHz",
   "Baseline", baselineStr, "(", corrStr, ")" print "MJDseconds",
   "Correlation amplitude" for i in range(len(tcoord)): print tcoord[i],
   acoord[i] # # Frequency [ 8.085] GHz Baseline 1-2 ( RR ) # MJDseconds
   Correlation amplitude # 4121629400.0 29.2170944214 # 4121629410.0
   29.1688995361 # 4121629420.0 29.2497825623 # 4121629430.0
   29.2029647827 # 4121629440.0 29.166015625 # 4121629450.0
   29.2417526245 # 4121629460.0 29.2867794037 # 4121638270.0 0.0 #
   4121638280.0 29.4539775848 # 4121638290.0 29.472661972 # 4121638300.0
   29.4424362183 # 4121638310.0 29.4234466553 # 4121638320.0
   29.4018745422 # 4121638330.0 29.3326053619 # 4121638340.0
   29.3575496674 # 4121642600.0 31.1411132812 # 4121642610.0
   31.0726108551 # 4121642620.0 31.1242599487 # 4121642630.0
   31.0505466461 # 4121642640.0 31.0448284149 # 4121642650.0
   30.9974422455 # 4121642660.0 31.0648326874 # 4121642670.0
   31.0638961792 This example selects all the data from the measurement
   set where the value in the DATA_DESC_ID column is zero. This
   corresponds to a particular spectral window and polarization setup.
   It then gets the correlated amplitude, and the axis information from
   this selected measurement set. This is returned in the casapy
   variable d. The remainder of the example prints a table of 'hour
   angle' and corresponding 'correlated amplitude' for the first
   channel, correlation and baseline.

.. container:: param

   function **putdata**

   .. container:: collcontent

      .. container:: methoddesc

         This function allows you to write values from casapy variables
         back into the measurement set table. The main difference
         between this and directly accessing the table using the table
         tool is that this function writes data to the selected
         measurement set. Unlike the getdata function, you can only put
         items that correspond to actual table columns. You cannot
         change the data shape either so that the number of
         correlations, channels and rows (or interferometers/time slots)
         must match the values in the selected measurement set. If the
         values were obtained using the getdata function with ifraxis
         argument set to True, then any default values added to fill in
         missing interferometer/timeslots pairs will be ignored when
         writing the modified values back using this function. Allowable
         items include: 'data', 'corrected_data', 'model_data', 'flag',
         'flag_row', 'sigma', and 'weight'. 'float_data' is currently
         not implemented for putdata. The measurement set has to be
         opened for read/write access (nomodify=False) to be able to use
         this function. You need to call selectinit before calling this
         function. If you haven't then selectinit will be called for you
         with default arguments. Items prefixed with corrected, model,
         residual or obs_residual are not available unless your
         measurement set has been processed either with the imager or
         calibrator tools.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Record with items and their new values

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS", nomodify=False) ms.selectinit(datadescid=0)
   rec = ms.getdata(["weight","data"]) rec['weight'][:,:] = 1 import
   numpy as np meanrec = np.mean(rec['data'],axis=None) print "Mean data
   value = ", meanrec rec['data'][:,:,:] -= meanrec ms.putdata(rec) This
   example selects all the data from the measurement set where the value
   in the DATA_DESC_ID column is zero. This corresponds to a particular
   spectral window and polarization setup. Note that the measurement set
   was opened for writing as well as reading. The third line reads all
   the weights and the data into the casapy variable rec. The weights
   are set to one. The more obscure syntax is used as typing
   rec['weight'] = 1 will not preserve the shape of the weight array.
   The data then has its mean subtracted from it. The mean function is
   defined in the numpy module. Finally the data is written back into
   the measurement set table. (NOTE: Normally one should not modify the
   raw data column. Such adjustments are more appropriate for the
   corrected_data column, if it exists.)

.. container:: param

   function **fromfits**

   .. container:: collcontent

      .. container:: methoddesc

         This function will convert a uvfits file to a measurement set
         table and then open the measurement set table. The newly
         created measurement set table will continue to exist after the
         tool has been closed. Setting the lock argument to True will
         permanently lock the table preventing other processes from
         writing to the measurement set. Unless you expect this to
         happen, and want to prevent it, you should leave the lock
         argument at the default value which implies auto-locking. Note
         that the variety of fits files that fromfits is able to
         interpret correctly is limited mostly to files similar to those
         produced by classic AIPS. In particular, it understands only
         binary table extensions for the antenna (AN), frequency (FQ)
         and source (SU) information and ignores other extensions. This
         function returns True if it successfully attaches the ms tool
         to a newly created Measurement Set or False if something went
         wrong, like an error in a file name. NOTE ON WEIGHTS
         ms.fromfits() will generate a WEIGHT_SPECTRUM column in which
         it will fill the absolute value of the weight associated with
         each visibility in the uvfits file. Negative weights will have
         the associated FLAGs set to True. It will compute the
         associated WEIGHT value for that MS row to be the sum of the
         absolute values of the associated WEIGHT_SPECTRUM values.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msfile : undefined

      .. container:: methodparmtable

         Filename for the newly created measurement set

.. container:: parameters2

   fitsfile : undefined

.. container:: methodparmtable

   uvfits file to read

.. container:: parameters2

   nomodify : undefined = true

.. container:: methodparmtable

   Open for read access only.

.. container:: parameters2

   lock : undefined = false

.. container:: methodparmtable

   Lock the table for exclusive use.

.. container:: parameters2

   obstype : undefined = 0

.. container:: methodparmtable

   Specify the observation type: 0=standard, 1=fastmosaic, requiring
   small tiles in the measurement set.

.. container:: parameters2

   host : undefined

.. container:: methodparmtable

   Host to start ms tool on (IGNORED!!!)

.. container:: parameters2

   forcenewserver : undefined = false

.. container:: methodparmtable

   Start a new server tool (IGNORED!!!).

.. container:: parameters2

   antnamescheme : undefined = old

.. container:: methodparmtable

   For VLA only, antenna name scheme, old style is just antenna number,
   new style prepends VA or EV.

Allowed Value(s)

old new

.. container:: methodsection

   Example

.. container:: methodexam

   ms.fromfits("3C273XC1.MS", "3C273XC1.fits")

.. container:: param

   function **fromfitsidi**

   .. container:: collcontent

      .. container:: methoddesc

         This function will convert a uvfits file to a measurement set
         table and then open the measurement set table. The newly
         created measurement set table will continue to exist after the
         tool has been closed. Setting the lock argument to True will
         permanently lock the table preventing other processes from
         writing to the measurement set. Unless you expect this to
         happen, and want to prevent it, you should leave the lock
         argument at the default value which implies auto-locking. Note
         that the variety of fits files that fromfits is able to
         interpret correctly is limited mostly to files similar to those
         produced by classic AIPS. In particular, it understands only
         binary table extensions for the antenna (AN), frequency (FQ)
         and source (SU) information and ignores other extensions. This
         function returns True if it successfully attachs the ms tool to
         a newly created Measurement Set or False if something went
         wrong, like an error in a file name.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msfile : undefined

      .. container:: methodparmtable

         Filename for the newly created measurement set

.. container:: parameters2

   fitsfile : undefined

.. container:: methodparmtable

   fits-idi file to read

.. container:: parameters2

   nomodify : undefined = true

.. container:: methodparmtable

   Open for read access only.

.. container:: parameters2

   lock : undefined = false

.. container:: methodparmtable

   Lock the table for exclusive use.

.. container:: parameters2

   obstype : undefined = 0

.. container:: methodparmtable

   Specify the observation type: 0=standard, 1=fastmosaic, requiring
   small tiles in the measurement set.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.fromfits("3C273XC1.MS", "3C273XC1.fits")

.. container:: param

   function **tofits**

   .. container:: collcontent

      .. container:: methoddesc

         This function writes a uvfits file that contains the data in
         the measurement set associated with this tool. The fits file is
         always written in floating point format and the data are always
         stored in the primary array of the fits file. IMPORTANT NOTE:
         In general, some of the data averaging features of this method
         have never worked properly. In general, users should run
         mstransform to select and average data prior to running
         tofits(). The associated input parameters are slowly being
         deprecated and removed. If the measurement set has been imaged
         or calibrated in CASA, it may contain additional data columns.
         You need to select ONE of these columns to be written to the
         fits file. The possible options are: 1. observed This is the
         raw data as collected by the telescope. All interferometric
         measurement sets must contain this column. A synonym for
         'observed' is 'data'. 2. corrected This is the calibrated data.
         A synonym for 'corrected' is 'corrected_data'. 3. model This is
         the visibilites that would be measured using the current model
         of the sky. A synonym for 'model' is 'model_data'. The parsing
         of these strings is case insensitive. If any other option is
         specified then the observed data will be written. By default a
         single-source uvfits file is written, but if the measurement
         set contains more than one field or if you set the multisource
         argument to True a multi-source uvfits file will be written.
         Because of limitations in the uvfits format you have to ensure
         that the data shape is fixed for all the data you intend to
         write to one fits file. See the general description of this
         tool for how you can select data to meet this condition. The
         combinespw argument is used to control whether data from
         different spectral windows will be written as different entries
         in the fits FQ (frequency) table or combined as different IF's
         within one entry in the FQ table. You should normally only set
         this to True if you know that the data from different spectral
         windows were observed simultaneously, and the data in the
         measurement set can be equally divided between all the spectral
         windows (i.e. each window should have the same width). Use of
         this switch is recommended for data to be processed in classic
         AIPS and difmap (if possible, e.g., standard dual IF
         observations). The padwithflags argument is only relevant if
         combinespw is True. If true, it will fill in data that is
         'missing' with flags to fit the IF structure. This is
         appropriate if the MS had a few frequency-dependent flags
         applied, and was then time-averaged by split. If the spectral
         windows were observed at different times, padwithflags=True
         will add a large number of flags, making the output file
         significantly longer. It does not yet support spectral windows
         with different widths. The fits GC (gain curve) and TY (system
         temperature) tables can be optionally written by setting the
         writesyscal argument to True. This is a rather WSRT-specific
         operation at the moment and may not work correctly for
         measurement sets from other telescopes. One may overwrite the
         specified output file if it exists by specifying
         overwrite=True. NOTE ON WEIGHTS If the MS has no
         WEIGHT_SPECTRUM column, or if it does, but that column does not
         contain any data, ms.tofits() will compute the associated
         weight it writes to the uvfits file by taking the associated
         WEIGHT column value in the MS and dividing it by the number of
         channels associated with the spectral window of that
         visibility.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         fitsfile : undefined

      .. container:: methodparmtable

         Name of the new uvfits file.

.. container:: parameters2

   column : undefined = corrected

.. container:: methodparmtable

   Data column to write, see above for options.

.. container:: parameters2

   field : any

.. container:: methodparmtable

   Field ids (0-based) or fieldnames to split out.

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral windows to split.

.. container:: parameters2

   baseline : any

.. container:: methodparmtable

   Antenna names or Antenna indices to select.

.. container:: parameters2

   time : undefined

.. container:: methodparmtable

   Limit data selected to be within a given time range. Syntax is the
   defined in the msselection link.

.. container:: parameters2

   scan : any

.. container:: methodparmtable

   Limit data selected on scan numbers. Syntax is the defined in the
   msselection link.

.. container:: parameters2

   uvrange : any

.. container:: methodparmtable

   Limit data selected on uv distance. Syntax is the defined in the
   msselection link.

.. container:: parameters2

   taql : undefined

.. container:: methodparmtable

   For the TAQL experts, flexible data selection using the TAQL syntax.

.. container:: parameters2

   writesyscal : undefined = false

.. container:: methodparmtable

   Write GC and TY tables.

.. container:: parameters2

   multisource : undefined = false

.. container:: methodparmtable

   Write in multisource format.

.. container:: parameters2

   combinespw : undefined = false

.. container:: methodparmtable

   Export spectral windows as IFs.

.. container:: parameters2

   writestation : undefined = false

.. container:: methodparmtable

   Write station name instead of antenna name.

.. container:: parameters2

   padwithflags : undefined = false

.. container:: methodparmtable

   If combinespw==True, pad data with flags to fit IFs.

.. container:: parameters2

   overwrite : undefined = false

.. container:: methodparmtable

   Overwrite output file if it exists?

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') ms.tofits('3C273XC1.fits', column='DATA');
   ms.done() This example writes the observed data of a measurement set
   to a uvfits file. ms.open('big.ms') ms.tofits('part.fits',
   column='CORRECTED', field=[0,1], spw=[2]) ms.done() This example
   writes part (the first two fields and the third spectral window) of
   the corrected data to the fits file.

.. container:: param

   function **listfits**

   .. container:: collcontent

      .. container:: methoddesc

         List HDU and typical data rows in a uvfits file

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         fitsfile : undefined

      .. container:: methodparmtable

         uvfits file to list.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.listfits('ngc5921.fits')

.. container:: param

   function **asdmref**

   .. container:: collcontent

      .. container:: methoddesc

         If the MS is imported from an ASDM with option lazy=True, the
         DATA or FLOAT_DATA column of the MS is virtual and directly
         reads the visibilities from the ASDM. A reference to the
         original ASDM is stored with the MS. If the ASDM needs to be
         moved to a different path, the reference to it in the MS needs
         to be updated. This can be achieved with ms.asdmref(). When
         called with an empty string (default), the method just reports
         the currently set ASDM path. Return value is a string
         containing the new path if the path was successfully set or (in
         the case abspath was empty) the MS indeed contains a ASDM
         reference, i.e. was lazily imported. If the ASDM does not
         contain an ASDM reference, the method returns an empty string.
         If abspath is not empty and there was an error setting the new
         reference, the method throws an exception.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         abspath : undefined

      .. container:: methodparmtable

         New absolute path of the ASDM to be referenced (empty string =
         report current setting).

.. container:: methodsection

   Example

.. container:: methodexam

   Set the path to the referenced ASDM to
   "/home/alma/myanalysis/uid___A12345_X678_X910":
   ms.open("uid___A12345_X678_X910.ms",False)
   ms.asdmref("/home/alma/myanalysis/uid___A12345_X678_X910") ms.close()
   Test if the MS was imported with lazy=True and therefore references
   an ASDM: ms.open("uid___A12345_X678_X910.ms") myref = ms.asdmref()
   ms.close() if myref=="": print "This MS does not reference an ASDM."
   else: print "This MS references the ASDM ", myref

.. container:: param

   function **concatenate**

   .. container:: collcontent

      .. container:: methoddesc

         This function concatenates two measurement sets together. The
         data is copied from the measurement set specified in the msfile
         arguement to the end of the measurement set attached to the ms
         tool. If a lot of data needs to be copied this function may
         take some time. You need to open the measurement set for
         writing in order to use this function.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msfile : undefined

      .. container:: methodparmtable

         The name of the measurement set to append.

.. container:: parameters2

   freqtol : any = 1Hz

.. container:: methodparmtable

   Frequency difference within which 2 spectral windows are considered
   similar; e.g '10Hz'.

.. container:: parameters2

   dirtol : any = 1mas

.. container:: methodparmtable

   Direction difference within which 2 fields are considered the same;
   e.g '1mas'.

.. container:: parameters2

   weightscale : undefined = 1.

.. container:: methodparmtable

   Scale the weights of the MS to be appended by this factor.

.. container:: parameters2

   handling : undefined = 0

.. container:: methodparmtable

   Switch for the handling of the Main and Pointing tables: 0=standard,
   1=no Main, 2=no Pointing, 3=no Main and Pointing, 4=virtual.

Allowed Value(s)

0 1 2 3

.. container:: parameters2

   destmsfile : undefined

.. container:: methodparmtable

   Optional support for virtual concat: empty table (no subtables) where
   to store the appended MS copy.

.. container:: parameters2

   respectname : undefined = false

.. container:: methodparmtable

   If true, fields with a different name are not merged even if their
   direction agrees.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS", nomodify=False) ms.concatenate("BLLAC.ms",
   '1GHz', '1arcsec') ms.done() This example appends the data from the
   BLLAC measurement set to the end of the 3C273 measurement set. Its
   going to assume a frequency tolerance of 1GHz and position tolerance
   of 1 arcsec in deciding if the spw and field in the measurementsets
   are similar or not.

.. container:: param

   function **testconcatenate**

   .. container:: collcontent

      .. container:: methoddesc

         This function acts like ms.concatenate() with handling==3 (do
         not concatenate the MAIN and POINTING tables). This is useful
         for generating, e.g., SPECTRAL_WINDOW and FIELD tables which
         contain all used SPW and FIELD ids for a set of MSs without
         having to actually carry out a time-consuming concatenation on
         disk. The MAIN table in the resulting output MS is that of the
         original MS, i.e. it is not touched.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msfile : undefined

      .. container:: methodparmtable

         The name of the measurement set from which the subtables should
         be appended.

.. container:: parameters2

   freqtol : any = 1Hz

.. container:: methodparmtable

   Frequency difference within which 2 spectral windows are considered
   similar; e.g '10Hz'.

.. container:: parameters2

   dirtol : any = 1mas

.. container:: methodparmtable

   Direction difference within which 2 fields are considered the same;
   e.g '1mas'.

.. container:: parameters2

   respectname : undefined = false

.. container:: methodparmtable

   If true, fields with a different name are not merged even if their
   direction agrees.

.. container:: methodsection

   Example

.. container:: methodexam

   tb.open("3C273XC1.MS") tb.copy("TEMP.MS", norows=True) tb.close()
   ms.open("TEMP.MS", nomodify=False) ms.testconcatenate("3C273XC1.ms",
   '1GHz', '1arcsec') ms.testconcatenate("BLLAC.ms", '1GHz', '1arcsec')
   ms.done() This example makes a copy of the structure of an MS and
   then appends the subtables data from two measurement sets to the
   empty structure. It will assume a frequency tolerance of 1GHz and
   position tolerance of 1 arcsec in deciding if the spw and field in
   the measurementsets are similar or not.

.. container:: param

   function **virtconcatenate**

   .. container:: collcontent

      .. container:: methoddesc

         This function virtually concatenates two measurement sets
         together such that they can later be turned into a multi-MS
         with createmultims(). You need to open the measurement set for
         writing in order to use this function.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msfile : undefined

      .. container:: methodparmtable

         The name of the measurement set to append

.. container:: parameters2

   auxfilename : undefined

.. container:: methodparmtable

   The name of a auxiliary file which is needed when more than two MSs
   are to be concatenated.

.. container:: parameters2

   freqtol : any = 1Hz

.. container:: methodparmtable

   Frequency difference within which 2 spectral windows are considered
   similar; e.g '10Hz'.

.. container:: parameters2

   dirtol : any = 1mas

.. container:: methodparmtable

   Direction difference within which 2 fields are considered the same;
   e.g '1mas'.

.. container:: parameters2

   weightscale : undefined = 1.

.. container:: methodparmtable

   Scale the weights of the MS to be appended by this factor.

.. container:: parameters2

   respectname : undefined = true

.. container:: methodparmtable

   If true, fields with a different name are not merged even if their
   direction agrees.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.ms", nomodify=False)
   ms.virtconcatenate("3C273XC1-2.ms", '3Caux.dat', '1GHz', '1arcsec')
   ms.virtconcatenate("3C273XC1-3.ms", '3Caux.dat', '1GHz', '1arcsec')
   ms.close() os.remove('3Caux.dat') ms.createmultims(concatvis,
   ["3C273XC1.ms","3C273XC1-2.ms","3C273XC1-3.ms"], [], True, # nomodify
   False,# lock True) # copysubtables from first to all other members
   ms.close() This example virtually appends the data from the
   3C273XC1-2 and 3C273XC1-3 to the end of the 3C273XC1 measurement set.
   Its going to assume a frequency tolerance of 1GHz and position
   tolerance of 1 arcsec in deciding if the spw and field in the
   measurementsets are similar or not. The file 3Caux.dat which is
   created in the process is no longer needed after the last call to
   virtconcatenate() and can be deleted.

.. container:: param

   function **createmultims**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         outputTableName : undefined

      .. container:: methodparmtable

.. container:: parameters2

   tables : undefined

.. container:: methodparmtable

.. container:: parameters2

   subtables : undefined

.. container:: methodparmtable

.. container:: parameters2

   nomodify : undefined = true

.. container:: methodparmtable

   Prevent changes to the measurement set.

.. container:: parameters2

   lock : undefined = false

.. container:: methodparmtable

   Lock the table for exclusive use by this tool.

.. container:: parameters2

   copysubtables : undefined = false

.. container:: methodparmtable

   Copy the subtables from the first to all other member MSs.

.. container:: parameters2

   omitsubtables : undefined

.. container:: methodparmtable

   Omit the subtables from this list when copying subtables.

.. container:: param

   function **ismultims**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

.. container:: param

   function **split**

   .. container:: collcontent

      .. container:: methoddesc

         This function splits out part of the MS into a new MS. Time and
         channel averaging can be performed in the process (but not in
         the same call). When splitting multiple spectral windows, the
         parameters nchan, start, and step can be vectors, so that each
         spectral window has its own selection on averaging and number
         of output channels. But the option of using only one value for
         each of these parameters means that it will be replicated for
         all the spectral windows selected.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         outputms : undefined

      .. container:: methodparmtable

         The name of the resulting measurement set

.. container:: parameters2

   field : undefined

.. container:: methodparmtable

   Fields to include, by names or 0-based ids. ('' => all).

.. container:: parameters2

   spw : undefined = \*

.. container:: methodparmtable

   Spectral windows (and :channels) to select.

.. container:: parameters2

   step : undefined = 1

.. container:: methodparmtable

   Number of input per output channels - Int vector of length 1 or same
   as spw.

.. container:: parameters2

   baseline : undefined

.. container:: methodparmtable

   Antenna names or indices to select ('' => all).

.. container:: parameters2

   timebin : undefined = -1s

.. container:: methodparmtable

   Duration for averaging. Defaults to no averaging.

.. container:: parameters2

   time : undefined

.. container:: methodparmtable

   Only use data in the given time range, using the msselection syntax.

.. container:: parameters2

   scan : undefined

.. container:: methodparmtable

   Only use the scan numbers requested using the msselection syntax.

.. container:: parameters2

   uvrange : undefined

.. container:: methodparmtable

   Limit data by uv distance using the msselection syntax.

.. container:: parameters2

   taql : undefined

.. container:: methodparmtable

   For the TAQL experts, flexible data selection using the TAQL syntax

.. container:: parameters2

   whichcol : undefined = DATA

.. container:: methodparmtable

   'DATA', 'MODEL_DATA', 'CORRECTED_DATA', 'FLOAT_DATA', 'LAG_DATA',
   and/or 'all'.

.. container:: parameters2

   tileshape : undefined

.. container:: methodparmtable

   Tile shape of the disk data columns, most users should not need to
   touch this parameter. [0] => normal tiling, [1] => fast mosaic style
   tile, [4,15,351] => a tile shape of 4 pol 15 chan and 351 rows

.. container:: parameters2

   subarray : undefined

.. container:: methodparmtable

   Limit data to specific (sub)array numbers.

.. container:: parameters2

   combine : undefined

.. container:: methodparmtable

   Ignore changes in these columns (scan, and/or state) when time
   averaging.

.. container:: parameters2

   correlation : undefined

.. container:: methodparmtable

   Limit data to specific correlations (LL, XX, LR, XY, etc.).

.. container:: parameters2

   intent : undefined

.. container:: methodparmtable

   Only use the requested scan intents.

.. container:: parameters2

   obs : undefined

.. container:: methodparmtable

   Only use the requested observation IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("multiwin.ms") ms.split('subms.ms', field=[0], spw=[0],
   nchan=[10], start=[0], step=[5], whichcol='CORRECTED_DATA') In this
   example we split out data from the first field and first spectral
   window. The output data will have 10 channels which is taken from 50
   channels from the input data starting at channel 0 and averaging
   every 5. ms.open("multiwin.ms") ms.split('subms.ms', field=[0],
   spw=[0,1,2,3], nchan=[10], start=[0], step=[5],
   whichcol='CORRECTED_DATA') In this example we split out data from the
   1st field and four spectral windows. The output data will have 4
   spectral windows each of 10 channels which is taken from 50 channels
   from the input data starting at channel 0 and averaging every 5.
   ms.open("multiwin.ms") ms.split('subms.ms', field=[0], spw=[0,1,2,3],
   nchan=[10,10,30,40], start=[0,4,9,9], step=[1,10,5,2],
   whichcol='CORRECTED_DATA') In this example we split out data from the
   1st field and four spectral windows. There will be four spectral
   windows in the output data, with 10, 10, 30 and 40 channels
   respectively. These are averages of the input spectral windows. The
   first output spectral window will be formed by picking 10 channels,
   starting at 0 with no averaging, of the input spwid 0. The second
   output spectral window will consists of 10 channels and is formed by
   picking 100 channels from spwid 1 of the input data, starting at
   channel 4, and every 10 channels to make one output channel.
   ms.open("WSRT.ms") ms.split('subms.ms', timebin='20s',
   whichcol='all', combine='scan') ms.close() This example averages a
   WSRT MS into 20s bins, selecting whichever of DATA, MODEL_DATA,
   CORRECTED_DATA, or FLOAT_DATA, or LAG_DATA is present. Normally the
   bins would not cross scans, but in this MS the scan number goes up
   with each integration, making it redundant enough with time that it
   would defeat any time averaging. Therefore the combine parameter
   forces the SCAN column to be ignored for setting the bins.

.. container:: param

   function **partition**

   .. container:: collcontent

      .. container:: methoddesc

         This function splits out part of the MS into a new MS. Time
         averaging can be performed in the process. Unlike split, the
         subtables and IDs (ANTENNA1, DATA_DESCRIPTION_ID, etc.) are
         never changed to account for the selection. As a side effect of
         that property, partition cannot select by channel or
         correlation, or average channels. It CAN select by spectral
         window(s).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         outputms : undefined

      .. container:: methodparmtable

         The name of the resulting measurement set.

.. container:: parameters2

   field : undefined

.. container:: methodparmtable

   Fields to include, by names or 0-based ids. ('' => all).

.. container:: parameters2

   spw : undefined = \*

.. container:: methodparmtable

   Spectral windows (and :channels) to select.

.. container:: parameters2

   baseline : undefined

.. container:: methodparmtable

   Antenna names or indices to select ('' => all).

.. container:: parameters2

   timebin : undefined = -1s

.. container:: methodparmtable

   Duration for averaging. Defaults to no averaging.

.. container:: parameters2

   time : undefined

.. container:: methodparmtable

   Only use data in the given time range, using the msselection syntax.

.. container:: parameters2

   scan : undefined

.. container:: methodparmtable

   Only use the scan numbers requested using the msselection syntax.

.. container:: parameters2

   uvrange : undefined

.. container:: methodparmtable

   Limit data by uv distance using the msselection syntax.

.. container:: parameters2

   taql : undefined

.. container:: methodparmtable

   For the TAQL experts, flexible data selection using the TAQL syntax.

.. container:: parameters2

   whichcol : undefined = DATA

.. container:: methodparmtable

   'DATA', 'MODEL_DATA', 'CORRECTED_DATA', 'FLOAT_DATA', 'LAG_DATA',
   and/or 'all'.

.. container:: parameters2

   tileshape : undefined

.. container:: methodparmtable

   Tile shape of the disk data columns, most users should not need to
   touch this parameter [0] => normal tiling, [1] => fast mosaic style
   tile, [4,15,351] => a tile shape of 4 pol 15 chan and 351 rows.

.. container:: parameters2

   subarray : undefined

.. container:: methodparmtable

   Limit data to specific (sub)array numbers.

.. container:: parameters2

   combine : undefined

.. container:: methodparmtable

   Ignore changes in these columns (scan, and/or state) when time
   averaging.

.. container:: parameters2

   intent : undefined

.. container:: methodparmtable

   Only use the requested scan intents.

.. container:: parameters2

   obs : undefined

.. container:: methodparmtable

   Only use the requested observation IDs.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("multiwin.ms") ms.partition('partition.ms', field=[0],
   spw=[1], whichcol='CORRECTED_DATA') In this example we partition out
   data from the first field and second spectral window. Only the
   CORRECTED_DATA data column will be copied, and it will be written to
   the DATA column of partition.ms. ms.open("multiwin.ms")
   ms.partition('partition.ms', field=[0], spw=[0,1,2,3],
   whichcol='CORRECTED_DATA') In this example we partition out
   calibrated data from the first field and four spectral windows.
   ms.open("WSRT.ms") ms.partition('partition.ms', timebin='20s',
   whichcol='all', combine='scan') ms.close() This example averages a
   WSRT MS into 20s bins, selecting whichever of DATA, MODEL_DATA,
   CORRECTED_DATA, or FLOAT_DATA, or LAG_DATA is present. Normally the
   bins would not cross scans, but in this MS the scan number goes up
   with each integration, making it redundant enough with time that it
   would defeat any time averaging. Therefore combine parameter forces
   the SCAN column to be ignored for setting the bins.

.. container:: param

   function **summary**

   .. container:: collcontent

      .. container:: methoddesc

         This method will print a summary of the measurement set to the
         system logger. The verbose argument provides some control on
         how much information is displayed. For especially large
         datasets, the cachesize parameter can be increased for possibly
         better performance. This method can also return, in the header
         argument, a record containing the following fields: 1. nrow
         Number of rows in the measurement set 2. name Name of the
         measurement set DESCRIPTION OF ALGORITHM TO CALCULATE THE
         NUMBER OF UNFLAGGED ROWS The number of unflagged rows will only
         be computed if listunflis True. The number of unflagged rows
         (the nUnflRows columns in the scans and fields portions of the
         listing) is calculated by summing the fractional unflagged
         bandwidth for each row (and hence why the number of unflagged
         rows, in general, is not an integer). Thus a row which has half
         of its total bandwidth flagged contributes 0.5 rows to the
         unflagged row count. A row with 20 of 32 channels of
         homogeneous width contributes 20/32 = 0.625 rows to the
         unflagged row count. A row with a value of False in the
         FLAG_ROW column is not counted in the number of unflagged rows.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         verbose : undefined = false

      .. container:: methodparmtable

         Produce verbose logging output.

.. container:: parameters2

   listfile : undefined

.. container:: methodparmtable

   Output file.

.. container:: parameters2

   listunfl : undefined = false

.. container:: methodparmtable

   List unflagged row counts? If true, it can have significant negative
   performance impact.

.. container:: parameters2

   cachesize : undefined = 50

.. container:: methodparmtable

   EXPERIMENTAL. Maximum size in megabytes of cache in which data
   structures can be held.

.. container:: parameters2

   overwrite : undefined = false

.. container:: methodparmtable

   If True, tacitly overwrite listfile if it exists.

.. container:: parameters2

   wantreturn : undefined = true

.. container:: methodparmtable

   If true, construct a record containing summary info and return it,
   else return nothing. If you don't need the record and just want the
   log output, setting this to False will provide a small performance
   increase.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') outr=ms.summary(verbose=True) ###print the
   begining of observation in this ms print
   qa.time(qa.quantity(outr['header']['BeginTime'],'d'), form='ymd')
   ###print a dictionary of the info of scan 1 outr['header']['scan_1']
   This example will send a verbose summary of the measurement set to
   the logger.

.. container:: param

   function **getscansummary**

   .. container:: collcontent

      .. container:: methoddesc

         This function will return a summary of the main table as a
         structure

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open('3C273XC1.MS') scanInfo = ms.getscansummary()

.. container:: param

   function **getspectralwindowinfo**

   .. container:: collcontent

      .. container:: methoddesc

         This method will get a summary of the spectral window actually
         used in this ms. To be precise those reference by the data
         description table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open('3C273XC1.MS') spwInfo = ms.getspectralwindowinfo()

.. container:: param

   function **getreferencedtables**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

.. container:: param

   function **getfielddirmeas**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns the direction measures from the given
         direction column of the MS FIELD table as a either a measure
         dictionary or sexigesimal string representation. If there is an
         ephemeris attached, this will give you the time dependent
         direction for the given direction column including the offset
         which each field may have to the ephemeris it is referencing.
         You can use the value "EPHEMERIS_DIR" for parameter
         "dircolname" to access the unaltered ephemeris direction
         without any potential mosaic offsets.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         dircolname : undefined = PHASE_DIR

      .. container:: methodparmtable

         Name of the direction column in the FIELD table or
         'EPHEMERIS_DIR'.

Allowed Value(s)

PHASE_DIR DELAY_DIR REFERENCE_DIR EPHEMERIS_DIR

.. container:: parameters2

   fieldid : undefined = 0

.. container:: methodparmtable

   Field ID, starting at 0.

.. container:: parameters2

   time : undefined = 0

.. container:: methodparmtable

   (optional) Time for ephemeris access (in seconds, as in Main table
   TIME column).

.. container:: parameters2

   format : undefined = measure

.. container:: methodparmtable

   Output format. Either "measure" (measure dictionary) or "string"
   (sexigesimal representation). Minimum match supported.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') print "Delay direction from FIELD table row 3
   =", ms.getfielddirmeas("DELAY_DIR", 3) print "Phase direction from
   ephemeris FIELD table row 4 for time = 5019988459.968 s",
   ms.getfielddirmeas("PHASE_DIR", 4, 5019988459.968)

.. container:: param

   function **listhistory**

   .. container:: collcontent

      .. container:: methoddesc

         This function lists the contents of the measurement set history
         table.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open('3C273XC1.MS') ms.listhistory() The history table
         contents are listed in the logger.

.. container:: param

   function **writehistory**

   .. container:: collcontent

      .. container:: methoddesc

         This function adds a row to the history table of the specified
         measurement set containing any message that the user wishes to
         record. By default the history entry is written to the history
         table of the measurement set that is currently open, the
         message origin is recorded as 'MSHistoryHandler::addMessage()',
         the originating application is 'ms' and the input parameters
         field is empty.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         message : undefined

      .. container:: methodparmtable

         Message to be recorded in message field.

.. container:: parameters2

   parms : undefined

.. container:: methodparmtable

   String to be written to input parameter field.

.. container:: parameters2

   origin : undefined = MSHistoryHandler::addMessage()

.. container:: methodparmtable

   String to be written to origin field.

.. container:: parameters2

   msname : undefined

.. container:: methodparmtable

   Name of selected measurement set.

.. container:: parameters2

   app : undefined = ms

.. container:: methodparmtable

   String to be written to application field.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') ms.writehistory('an arbitrary history
   message') ms.listhistory() A row is appended to the measurement set
   history table.

.. container:: param

   function **writehistory_batch**

   .. container:: collcontent

      .. container:: methoddesc

         This function works as writehistory but adds a list of messages
         to the history table, instead of a single message. Each message
         is written into in a new row. It is recommended for efficiency,
         as adding rows one at a time can be rather slow, causing for
         example a delay of the order of 10-30 seconds when writing the
         history at the end of a normal flagdata command (with 70+
         parameter rows).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         messages : undefined

      .. container:: methodparmtable

         Message to be recorded in message field.

.. container:: parameters2

   parms : undefined

.. container:: methodparmtable

   String to be written to input parameter field.

.. container:: parameters2

   origin : undefined = MSHistoryHandler::addMessage()

.. container:: methodparmtable

   String to be written to origin field.

.. container:: parameters2

   msname : undefined

.. container:: methodparmtable

   Name of selected measurement set.

.. container:: parameters2

   app : undefined = ms

.. container:: methodparmtable

   String to be written to application field.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') ms.writehistory_batch(['message 1', 'message
   2', 'message 3']) ms.listhistory() One or more rows are appended to
   the measurement set history table.

.. container:: param

   function **statistics**

   .. container:: collcontent

      .. container:: methoddesc

         This function computes descriptive statistics on the
         measurement set. It returns the statistical values as a python
         dictionary. The given column name must be a numerical column.
         If it is a complex valued column, the parameter complex_value
         defines which derived real value is used for the statistics
         computation.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         column : undefined

      .. container:: methodparmtable

         Column name

.. container:: parameters2

   complex_value : undefined

.. container:: methodparmtable

   Which derived value to use for complex columns (amp, amplitude,
   phase, imag, real, imaginary)

.. container:: parameters2

   useflags : undefined = true

.. container:: methodparmtable

   Use the data flags.

.. container:: parameters2

   useweights : undefined = false

.. container:: methodparmtable

   Use the data weights.

.. container:: parameters2

   spw : undefined

.. container:: methodparmtable

   Spectral Window Indices or names. Example : '1,2'

.. container:: parameters2

   field : undefined

.. container:: methodparmtable

   Field indices or source names. Example : '2,3C48'

.. container:: parameters2

   baseline : undefined

.. container:: methodparmtable

   Baseline number(s). Example: "2&3;4&5"

.. container:: parameters2

   uvrange : undefined

.. container:: methodparmtable

   UV-distance range, with a unit. Example : '2.0-3000.0 m'

.. container:: parameters2

   time : undefined

.. container:: methodparmtable

   Time range, as MJDs or date strings. Example :
   'xx.x.x.x.x~yy.y.y.y.y'

.. container:: parameters2

   correlation : undefined

.. container:: methodparmtable

   Correlations/polarizations. Example : 'RR,LL,RL,LR,XX,YY,XY,YX'

.. container:: parameters2

   scan : undefined

.. container:: methodparmtable

   Scan number. Example : '1,2,3'

.. container:: parameters2

   intent : undefined

.. container:: methodparmtable

   Scan intents. Example : '*AMPL*,*PHASE*'

.. container:: parameters2

   array : undefined

.. container:: methodparmtable

   Array Indices or names. Example : 'VLAA'

.. container:: parameters2

   obs : undefined

.. container:: methodparmtable

   Observation ID(s). Examples : '' or '1~3'

.. container:: parameters2

   reportingaxes : undefined

.. container:: methodparmtable

   Statistics reporting axes. Example: 'ddid,field'

.. container:: parameters2

   timeaverage : undefined = false

.. container:: methodparmtable

   Average data in time.

.. container:: parameters2

   timebin : undefined = 0s

.. container:: methodparmtable

   Time averaging interval.

.. container:: parameters2

   timespan : undefined

.. container:: methodparmtable

   Boundaries to ignore in time averaging. Example: 'scan,state'

.. container:: parameters2

   maxuvwdistance : undefined = 0.0

.. container:: methodparmtable

   Maximum separation of start-to-end baselines that can be included in
   an average. (meters)

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.statistics(column="DATA",
   complex_value='amp', field="2")

.. container:: param

   function **statisticsold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::statistics() function in place
         of ms::statisticsold(). This function computes descriptive
         statistics on the measurement set. It returns the statistical
         values as a python dictionary. The given column name must be a
         numerical column. If it is a complex valued column, the
         parameter complex_value defines which derived real value is
         used for the statistics computation.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         column : undefined

      .. container:: methodparmtable

         Column name.

.. container:: parameters2

   complex_value : undefined

.. container:: methodparmtable

   Which derived value to use for complex columns (amp, amplitude,
   phase, imag, real, imaginary).

.. container:: parameters2

   useflags : undefined = true

.. container:: methodparmtable

   Use the data flags.

.. container:: parameters2

   spw : undefined

.. container:: methodparmtable

   Spectral Window Indices or names. Example : '1,2'

.. container:: parameters2

   field : undefined

.. container:: methodparmtable

   Field indices or source names. Example : '2,3C48'

.. container:: parameters2

   baseline : undefined

.. container:: methodparmtable

   Baseline number(s). Example: "2&3;4&5"

.. container:: parameters2

   uvrange : undefined

.. container:: methodparmtable

   UV-distance range, with a unit. Example : '2.0-3000.0 m'

.. container:: parameters2

   time : undefined

.. container:: methodparmtable

   Time range, as MJDs or date strings. Example :
   'xx.x.x.x.x~yy.y.y.y.y'

.. container:: parameters2

   correlation : undefined

.. container:: methodparmtable

   Correlations/polarizations. Example : 'RR,LL,RL,LR,XX,YY,XY,YX'

.. container:: parameters2

   scan : undefined

.. container:: methodparmtable

   Scan number. Example : '1,2,3'

.. container:: parameters2

   array : undefined

.. container:: methodparmtable

   Array Indices or names. Example : 'VLAA'

.. container:: parameters2

   obs : undefined

.. container:: methodparmtable

   Observation ID(s). Examples : '' or '1~3'

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.statisticsold(column="DATA",
   complex_value='amp', field="2")

.. container:: param

   function **range**

   .. container:: collcontent

      .. container:: methoddesc

         This function returns the range of values in the currently
         selected measurement set for the items specified. Possible
         items include 'amplitude', 'corrected_amplitude',
         'model_amplitude', 'antenna1', 'antenna2', 'antennas',
         'array_id', 'chan_freq', 'corr_names', 'corr_types', 'feed1',
         'feed2', 'field_id', 'fields', 'float_data', 'ifr_number'
         (1000*antenna1 + antenna2), 'imaginary', 'corrected_imaginary',
         'model_imaginary', 'num_corr', 'num_chan', 'phase',
         'corrected_phase', 'model_phase', 'phase_dir', 'real',
         'corrected_real', 'model_real', 'ref_frequency', 'rows',
         'scan_number', 'sigma', 'data_desc_id', 'time', 'times', 'u',
         'v', 'w', 'uvdist', and 'weight'. Note that corrected, model,
         and float versions are available only if these columns are
         present in the data. You specify items in which you are
         interested using a string vector where each element is a case
         insensitive item name. This function will then return a record
         that has fields corresponding to each of the specified items.
         Each field will contain the range of the specified item. For
         many items the range will be the minimum and maximum values but
         for some it will be a list of unique values. Unrecognized items
         are ignored. By default the FLAG column is used to exclude
         flagged data before any ranges are determined, but you can set
         useflags=False to include flagged data in the range. However,
         if you average in frequency, flagging will still be applied.
         You can influence the memory use and the reading speed using
         the blocksize argument - it specifies how big a block of data
         to read at once (in MB). For large datasets on machines with
         lots of memory you may speed things up by setting this higher
         than the default (10 MB). For some items, you need to call
         selectinit to select a portion of the data with a unique shape
         prior to calling this function. Items prefixed with corrected,
         model, residual or obs_residual are not available unless your
         measurement set has been processed either with the imager or
         calibrator tools.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Item names.

.. container:: parameters2

   useflags : undefined = true

.. container:: methodparmtable

   Use the data flags.

.. container:: parameters2

   blocksize : undefined = 10

.. container:: methodparmtable

   Set the blocksize in MB.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinit(datadescid=0)
   ms.range(["time","uvdist","amplitude","antenna1"]) #{'amplitude':
   array([ 2.60339398e-02, 3.38518333e+01]), # 'antenna1': array([ 0, 1,
   2, 3, 4, 5, 6, 7, 8, 9, # 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
   22, 23, 24, 25, # 26]), # 'time': array([ 4.12162940e+09,
   4.12164267e+09]), # 'uvdist': array([ 46.26912101, 3727.97385983])}
   In this example the minimum and maximum observation times,
   uvdistances, data amplitudes are returned as well as a list of all
   the antennas in the antenna1 column. For this dataset the selectinit
   function did not need to be called as all the data is of one shape.

.. container:: param

   function **lister**

   .. container:: collcontent

      .. container:: methoddesc

         This tool lists measurement set visibility data under a number
         of input selection conditions. The measurement set data columns
         that can be listed are: the raw data, corrected data, model
         data, and residual (corrected - model) data. The output table
         format is dynamic. Field, Spectral Window, and Channel columns
         are not displayed if the column contents are uniform. For
         example, if \``spw = \`1' '' is specified, the spw column will
         not be displayed. When a column is not displayed, a message is
         sent to the logger and terminal indicating that the column
         values are uniform and listing the uniform value. Table column
         descriptions: Date/Time Average date and time of data sample
         interval Intrf Interferometer baseline (antenna names) UVDist
         uv-distance (units of wavelength) Fld Field ID SpW Spectral
         Window ID Chn Channel number Correlated polarization Correlated
         polarizations (eg: RR, LL, XY) Sub-columns: Amp Visibility
         amplitude Phs Visibility phase Wt Weight of visibility
         measurement F Flag: \`F' = flagged datum; \` ' = unflagged

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         options : undefined

      .. container:: methodparmtable

         Output options (not yet implemented)

.. container:: parameters2

   datacolumn : undefined = data

.. container:: methodparmtable

   Column to list: data, model, corrected, residual

.. container:: parameters2

   field : undefined

.. container:: methodparmtable

   Fields

.. container:: parameters2

   spw : undefined

.. container:: methodparmtable

   Spectral Windows

.. container:: parameters2

   antenna : undefined

.. container:: methodparmtable

   Antenna/Baselines

.. container:: parameters2

   timerange : undefined

.. container:: methodparmtable

   Time range

.. container:: parameters2

   correlation : undefined

.. container:: methodparmtable

   Polarization correlations

.. container:: parameters2

   scan : undefined

.. container:: methodparmtable

   Scan

.. container:: parameters2

   feed : undefined

.. container:: methodparmtable

   Feed (not yet implemented)

.. container:: parameters2

   array : undefined

.. container:: methodparmtable

   Array

.. container:: parameters2

   observation : undefined

.. container:: methodparmtable

   Select by observation ID(s)

.. container:: parameters2

   uvrange : undefined

.. container:: methodparmtable

   uv-distance (output units: wavelength)

.. container:: parameters2

   average : undefined

.. container:: methodparmtable

   Average mode (not yet implemented)

.. container:: parameters2

   showflags : undefined = false

.. container:: methodparmtable

   Showflags (not yet implemented)

.. container:: parameters2

   msselect : undefined

.. container:: methodparmtable

   TaQL expression

.. container:: parameters2

   pagerows : undefined = 50

.. container:: methodparmtable

   Rows per page

.. container:: parameters2

   listfile : undefined

.. container:: methodparmtable

   Output file

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('AZ136.ms') ms.lister() These commands yield the following
   listing: Date/Time: RR: RL: LR: LL: 2001/12/01/ Intrf UVDist Fld SpW
   Amp Phs Wt F Amp Phs Wt F Amp Phs Wt F Amp Phs Wt F
   ------------|-----|------|---|---|-------------------------|------------------------|------------------------|------------------------
   19:30:05.0 0- 1 1400 0 0: 0.002-102.7 229035 F 0.003-178.3 239694 F
   0.001 136.0 208264 F 0.001 -79.7 263599 F 19:30:05.0 0- 2 7203 0 0:
   0.002 127.3 267464 F 0.001 165.0 305192 F 0.003-118.2 265174 F 0.002
   16.3 307829 F 19:30:05.0 0- 3 9621 0 0: 0.002 -55.9 179652 F 0.002
   -27.1 230130 F 0.001 -94.9 199954 F 0.003 -89.3 206764 F 19:30:05.0
   0- 4 1656 0 0: 0.001 133.3 199677 F 0.002 80.6 258140 F 0.001 -35.1
   224291 F 0.003 23.9 229812 F 19:30:05.0 0- 5 3084 0 0: 0.002 -18.4
   197565 F 0.001 -83.1 228541 F 0.002 -85.1 198574 F 0.002 -28.5 227381
   F 19:30:05.0 0- 6 5020 0 0: 0.001-173.2 236475 F 0.002-104.0 257575 F
   0.000 0.0 223800 F 0.000-142.5 272162 F 19:30:05.0 0- 7 12266 0 0:
   0.003 -34.6 264977 F 0.002 5.3 280113 F 0.001-152.7 243383 F 0.002
   -78.8 304966 F . . . Notice that the channel column is not displayed.
   This measurement set contains only one channel; since the channel
   column values are uniform, the channel column is not displayed.
   Instead, message "All selected data has CHANNEL = 0" is sent to the
   console.

.. container:: param

   function **metadata**

   .. container:: collcontent

      .. container:: methoddesc

         Get the MS metadata associated with this MS.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         cachesize : undefined = 50

      .. container:: methodparmtable

         Maximum cache size, in megabytes, to use.

.. container:: methodsection

   Example

.. container:: methodexam

   # get the number of spectral windows in the specified MS
   ms.open"my.ms") metadata = ms.metadata() ms.done() nspw =
   metadata.nspw() metadata.done()

.. container:: param

   function **msselect**

   .. container:: collcontent

      .. container:: methoddesc

         A return value of True implies that the combination of all
         selection expressions resulted in a non-Null combined TaQL
         expression. False implies that the combined TaQL could not be
         formed (i.e. it is Null, and the "selected MS" will be the same
         as the input MS). The details of selection expressions are
         desribed in the MSSelection Memo. Note that this function can
         be called multiple times but the result is cumulative. Each
         selection will work on the data already selected from all
         previous calls of this function. Use the function reset() to
         reset all selections to NULL (original dataset).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Record with fields contain the selection expressions. Keys
         recognized in the record are: "spw", "time", "field",
         "baseline", "scan", "scanintent", "polarization",
         "observation", "array", "uvdist" and "taql".

.. container:: parameters2

   onlyparse : undefined = false

.. container:: methodparmtable

   If set to True, expressions will only be parsed but not applied to
   the MS for selection. When set to False, a selected MS will also be
   generated internally. Default is False. When only parsing is
   requested, the selected-MS is the same as the original MS.

.. container:: methodsection

   Example

.. container:: methodexam

   staql={'field':'3C286', 'spw':'0~7:10~55'}; ms.open(MSNAME); # For
   only getting the list of indices # corresponding to the selection,
   onlyparse=True ms.msselect(staql, onlyparse=True);
   ndx=ms.msselectedindices(); ndx['field'] Out[5]: array([1],
   dtype=int32) : : ms.msselect(staql); # To do the actual selection. #
   From this point on, the ms-tool is attached to the selected MS.

.. container:: param

   function **msselectedindices**

   .. container:: collcontent

      .. container:: methoddesc

         The return indices are the result of parsing the MSSelection
         expressions provided in the msselect function.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

.. container:: param

   function **msseltoindex**

   .. container:: collcontent

      .. container:: methoddesc

         Utility function that will return the ids of the selection
         used.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         vis : undefined

      .. container:: methodparmtable

         Measurementset for which this selection applies.

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Spectral Window Ids (0 relative) to select; -1 interpreted as all.

.. container:: parameters2

   field : any

.. container:: methodparmtable

   Field Ids (0 relative) or Field names (msselection syntax and
   wilcards are used) to select.

.. container:: parameters2

   baseline : any

.. container:: methodparmtable

   Antenna Ids (0 relative) or Antenna names (msselection syntax and
   wilcards are used) to select.

.. container:: parameters2

   time : any

.. container:: methodparmtable

   Limit data selected to be within a given time range. Syntax is the
   defined in the msselection link.

.. container:: parameters2

   scan : any

.. container:: methodparmtable

   Limit data selected on scan numbers. Syntax is the defined in the
   msselection link.

.. container:: parameters2

   uvrange : any

.. container:: methodparmtable

   Limit data selected on uv distance. Syntax is the defined in the
   msselection link.

.. container:: parameters2

   observation : any

.. container:: methodparmtable

   Select data by observation ID(s). The syntax is the same as for scan
   numbers.

.. container:: parameters2

   polarization : any

.. container:: methodparmtable

   Select data by polarization(s).

.. container:: parameters2

   taql : undefined

.. container:: methodparmtable

   For the TAQL experts, flexible data selection using the TAQL syntax.

.. container:: methodsection

   Example

.. container:: methodexam

   a= ms.msseltoindex(vis='3C273XC1.MS', field='3C*') print a['field'] #
   [0] print a #{'antenna1': array([], dtype=int32), # 'antenna2':
   array([], dtype=int32), # 'channel': array([], shape=(0, 0),
   dtype=int32), # 'field': array([0]), # 'scan': array([],
   dtype=int32), # 'spw': array([], dtype=int32), # 'obsids': array([],
   dtype=int32)} Field name '3C*', in this case 3C273, corresponds to
   field id 0. N.B.: The return values of unspecified fields (like
   antenna\* and spw in the above example) will be left empty - this
   does not mean that selection excludes all antennas! Some fields (like
   'field') are checked against the subtables of vis, but others are
   not. For example, field='123~132' will produce an error if vis does
   not have fields 123 to 132, but for scan and obsids '123~132' would
   just return an array of integers from 123 to 132 regardless of
   whether vis has those scan or observation IDs. (The difference comes
   from it being quicker to check a subtable than the main table.)

.. container:: param

   function **selectinit**

   .. container:: collcontent

      .. container:: methoddesc

         A measurement set can contain data with a variety of different
         shapes (as described in the overall description to this tool).
         To allow functions to return data in fixed shape arrays you
         need to select, using this function, rows that contain the same
         data shape. You do not need to use this function if all the
         data in your measurement set has only one shape. The
         DATA_DESC_ID column in the measurement set contains a value
         that maps to a particular row in the POLARIZATION and
         SPECTRAL_WINDOW subtables. Hence all rows with the same value
         in the DATA_DESC_ID column must have the same data shape. To
         select all the data where the DATA_DESC_ID value is N you call
         this function with the datadescid argument set to N. It is
         possible to have a measurement set with differing values in the
         DATA_DESC_ID column but where all the data is a fixed shape.
         For example this will occur if the reference frequency changes
         but the number of spectral channels is fixed. In cases like
         this all the data can be selected and this function does not
         need to be used. To return to the completely unselected
         measurement set, set the reset argument to True. This will
         allow you to access the full range of rows in the measurement
         set, rather than just the selected measurement set. The
         datadescid must always be a non-negative integer.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datadescid : undefined = 0

      .. container:: methodparmtable

         Data description id.

.. container:: parameters2

   reset : undefined = false

.. container:: methodparmtable

   Reset to unselected state.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinit(datadescid=0) print
   ms.range(["uvdist"]) ms.selectinit(reset=True) print
   ms.range("uvdist") In this example we display the range of uv
   distances for the data in the specified measurement set (the range
   'items' argument is a list of strings, even if only one item is
   requested). The first print statement will only use data where the
   DATA_DESC_ID column is 0. This will correspond to a specific spectral
   window and polarization setup. The second print statement will print
   the range of uv distances for all the data in the measurement set
   (which is the same in this case).

.. container:: param

   function **select**

   .. container:: collcontent

      .. container:: methoddesc

         This function will select a subset of the current measurement
         set based on the range of values for each field in the input
         record. The range function will return a record that can be
         altered and used as the argument for this function. A
         successful selection returns True. Unrecognized fields are
         ignored. Allowable items for select include: 'antenna1',
         'antenna2', 'array_id', 'feed1', 'feed2', 'field_id',
         'ifr_number', 'rows', 'scan_number', 'data_desc_id', 'time',
         'times', 'u', 'v', 'w', and 'uvdist'. You need to call
         selectinit before calling this function. If you haven't then
         selectinit will be called for you with default arguments.
         Repeated use of this function, with different arguments, will
         further refine the selection, resulting in a successively
         smaller selected measurement set. If the selected measurement
         set does not contain any rows then this function will return
         False and send a warning message in the logger. Otherwise this
         function will return True. To undo all the selections you need
         to use the selectinit function (with reset=True).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Record with fields of ranges or enumerations

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinit(datadescid=0)
   ms.select({'antenna1':[1,3,5],'uvdist':[1200.,1900.]})
   ms.select({'time':[4121629420.,4121638290.]}) # Or, convert time
   strings to seconds: start =
   qa.getvalue(qa.convert(qa.quantity('1989/06/27/01:03:40'), 's'))[0]
   stop = qa.getvalue(qa.convert(qa.quantity('1989/06/27/03:31:30'),
   's'))[0] rec = {} rec['time'] = [start, stop] ms.select(items=rec)
   This example selects all the data from the measurement set where the
   value in the DATA_DESC_ID column is zero. This corresponds to a
   particular spectral window and polarization setup. It then selects
   all the data where the first antenna in the interferometer is number
   one, three or five and where the uv distance is between 1200 and 1900
   meters. Finally it selects all the data which was observed between
   4121629420 seconds and 4121638290 seconds (since zero hours on the
   day where the modified Julian day is zero). Since this time in
   seconds is quite obscure, use the quanta tool to convert a date/time
   string into seconds which can then be used to perform the same time
   selection. The selections are cumulative so that at the end of this
   example only data in the specified time range, with the specified,
   interferometers, uv distances, spectral window and polarization setup
   are selected.

.. container:: param

   function **selecttaql**

   .. container:: collcontent

      .. container:: methoddesc

         This function will select a subset of the current measurement
         set based on the standard TaQL selection string given. Repeated
         use of this function, with different arguments, will further
         refine the selection, resulting in a successively smaller
         selected measurement set. If the selected measurement set does
         not contain any rows then this function will return False and
         send a warning message in the logger. Otherwise this function
         will return True. To undo all the selections you need to use
         the selectinit function (with reset=True). Note that index
         values used in the TaQL string are zero-based as are all tool
         indices.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msselect : undefined

      .. container:: methodparmtable

         TaQL selection string

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinit(datadescid=0)
   ms.select({'antenna1':[0,2,4],'uvdist':[1200.,1900.]})
   ms.selecttaql('ANTENNA1==2') ms.range(["ANTENNA1","ANTENNA2"]) #
   {'antenna1': array([2]), # 'antenna2': array([ 6, 9, 11, 18, 20, 21,
   24])} This example selects all the data from the measurement set
   where the value in the DATA_DESC_ID column is zero. This corresponds
   to a particular spectral window and polarization setup. It then
   selects all the data where the first antenna in the interferometer is
   number zero, two or four and where the uv distance is between 1200
   and 1900 meters. Finally it uses a query to select all the data for
   which the ANTENNA1 column is 2 (this selects the middle antenna of
   the previous, zero-based, selection). The selections are cumulative
   so that at the end of this example only data in the specified time
   range, with the specified, interferometers, uv distances, spectral
   window and polarization setup are selected.

.. container:: param

   function **selectchannel**

   .. container:: collcontent

      .. container:: methoddesc

         This function allows you to select a subset of the frequency
         channels in the current measurement set. This function can also
         average, over frequency channels, prior to providing the values
         to the user. Selection on channels is not allowed using either
         the select or command functions, as they can only select entire
         rows in a measurement set. Channel selection involves accessing
         only some of the values in a row. Like all the selection
         functions, this function does not change the current
         measurement but updates the measurement set selection
         parameters so that functions like getdata will return the
         desired subset of the data. Repeated use of this function will
         overwrite any previous channel selection. There are four
         parameters, the number of output channels, the first input
         channel to use, the number of input channels to average into
         one output channel, and the increment in the input spectrum for
         the next output channel. All four parameters need to be
         specified. When all data to be averaged is unflagged, the
         result is the averaged value and the corresponding flag is
         False. When all data is flagged, the result is set to zero and
         the corresponding flag is True. When data to be averaged is
         mixed (unflagged and flagged), only the unflagged values are
         averaged and the flag is set to False. This function return
         True if the selection was successful, and False if not. In the
         latter case an error message will also be sent to the logger.
         You need to call selectinit before calling this function. If
         you haven't then selectinit will be called for you with default
         arguments.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         nchan : undefined = 1

      .. container:: methodparmtable

         Number of output channels, positive integer.

.. container:: parameters2

   start : undefined = 0

.. container:: methodparmtable

   First input channel to use, positive integer.

.. container:: parameters2

   width : undefined = 1

.. container:: methodparmtable

   Number of input channels to average together, positive integer.

.. container:: parameters2

   inc : undefined = 1

.. container:: methodparmtable

   Increment to next (group of) input channel(s), positive integer.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.fromfits("NGC5921.MS", "/usr/lib/casapy/data/demo/NGC5921.fits")
   ms.selectinit(datadescid=0) ms.selectchannel(3,2,5,3) rec =
   ms.getdata(["data"]) This example selects all the data from the
   measurement set where the value in the DATA_DESC_ID column is zero.
   This corresponds to a particular spectral window and polarization
   setup. It then selects on frequency channels to produce 3 output
   channels, the first output channel is the average of channels
   2,3,4,5,6 in the input, the second output channel is the average of
   channel 5,6,7,8,9 and the third is the average of channels
   8,9,10,11,12.

.. container:: param

   function **selectpolarization**

   .. container:: collcontent

      .. container:: methoddesc

         This function allows you to select a subset of the
         polarizations in the current measurement set. This function can
         also setup conversion to different polarization
         representations. You specify the polarizations using a string
         vector. Allowable strings are include I, Q, U, V, RR, RL, LR,
         LL, XX, YY, XY, YX. These string must be specified in upper
         case. If the polarizations match those present in the
         measurement set they will be selected directly, otherwise all
         polarizations are read and then a conversion step is done. If
         the conversion cannot be done then an error will be produced
         when you try to access the data. This function return True if
         the selection was successful, and False if not. You need to
         call selectinit before calling this function. If you haven't
         then selectinit will be called for you with default arguments.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         wantedpol : undefined

      .. container:: methodparmtable

         The polarizations wanted.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinit(datadescid=0)
   ms.selectpolarization(["I","V"]) rec = ms.getdata(["data"]) This
   example selects all the data from the measurement set where the value
   in the DATA_DESC_ID column is zero. This corresponds to a particular
   spectral window and polarization setup. It then selects the I and V
   polarizations and when the getdata function is called the conversion
   from RR, LL, LR, RL polarizations to I and V occurs.

.. container:: param

   function **statwt**

   .. container:: collcontent

      .. container:: methoddesc

         IF NOT RUN IN PREVIEW MODE, THIS APPLICATION WILL MODIFY THE
         WEIGHT, WEIGHT SPECTRUM, FLAG, AND FLAG_ROW COLUMNS OF THE
         INPUT MS. IF YOU WANT A PRISTINE COPY OF THE INPUT MS TO BE
         PRESERVED, YOU SHOULD MAKE A COPY OF IT BEFORE RUNNING THIS
         APPLICATION. This application computes weights for the WEIGHT
         and WEIGHT_SPECTRUM (if present) columns based on the variance
         of values in the CORRECTED_DATA or DATA column. If the MS does
         not have the specified data column, the application will fail.
         The following algorithm is used: 1. For unflagged data in each
         sample, create two sets of values, one set is composed solely
         of the real part of the data values, the other set is composed
         solely of the imaginary part of the data values. 2. Compute the
         weighted (by exposure time) variance of each of these sets, v_r
         and v_i. The weighted variance per unit inverse eposure time,
         v, is computed using v = sum(e_i \* (V_i - )^2)/N, where e_i is
         the exposure time for real/imaginary part of visibility V_i and
         = sum(e_i \* V_i)/sum(e_i) is the weighted mean of all the
         visibilities in the set, and N is the number of (unflagged)
         visibilities. 3. Compute v_eq = (v_r + v_i)/2. 4. Compute the
         normalized variance, v_norm = v_eq \* , where = sum(e_i)/N is
         the mean of the exposure times. The associated weight of
         visibility V_i is e_i/v_eq. The weight will have unit of (data
         unit)^(-2), e.g., Jy^(-2). The visibility weights are what this
         application computes and writes. Data are aggregated on a
         per-baseline, per-data description ID basis. Data are
         aggregated in bins determined by the specified values of the
         timebin and chanbin parameters. By default, data for separate
         correlations are aggregated separately. This behavior can be
         overridden by specifying combine="corr" (see below). RULES
         REGARDING CREATING/INITIALIZING WEIGHT_SPECTRUM COLUMN 1. If
         run in preview mode (preview=True), no data are modified and no
         columns are added. 2. Else if datacolumn equals 'residual' or
         'residual_data' and a CORRECTED_DATA column exists, the WEIGHT
         and WEIGHT_SPECTRUM columns are not modified. 3. Else if the MS
         already has a WEIGHT_SPECTRUM and this column has been
         initialized (has values), it will be populated with the new
         weights. The WEIGHT column will be populated with the
         corresponding median values of the associated WEIGHT_SPECTRUM
         array. 4. Else if the frequency range specified for the sample
         is not the default ("spw"), the WEIGHT_SPECTRUM column will be
         created (if it doesn't already exist) and the new weights will
         be written to it. The WEIGHT column should be populated with
         the corresponding median values of the WEIGHT_SPECTRUM array.
         5. Otherwise the single value for each spectral window will be
         written to the WEIGHT column; the WEIGHT_SPECTRUM column will
         not be added if it doesn't already exist, and if it does, it
         will remain uninitialized (no values will be written to it). In
         cases where columns are added and initialized, the
         WEIGHT_SPECTRUM values will be set equal to the corresponding
         WEIGHT values, and the SIGMA_SPECTRUM values will be set to the
         corresponding SIGMA values. CAUTION: For some cases when only a
         subset of data is selected and the WEIGHT_SPECTRUM and/or
         SIGMA_SPECTRUM columns are created, there is a known code issue
         in which these columns are not properly created and initialized
         for the specified subset of data, although they are properly
         initialized for the entire dataset. In such cases, an exception
         will be thrown. Because the columns are created for the entire
         dataset, the user simply needs to rerun the statwt task using
         the same parameters and the task should complete as expected.
         Should this condition occur when the user is using the
         ms.statwt() tool method, the user should close the ms tool, and
         then reopen it using the same data set and configure the same
         selection, and rerun ms.statwt(). The tool method should then
         complete as expected. RULES FOR MODIFYING WEIGHT,
         WEIGHT_SPECTRUM, SIGMA, and SIGMA_SPECTRUM 1. If
         datacolum='corrected' or 'residual' then values are written to
         the WEIGHT and WEIGHT_SPECTRUM (if applicable) columns only. 2.
         If datacolumn='data' or 'residual_data' and the
         'CORRECTED_DATA' column does not exist, then values are written
         to the WEIGHT and WEIGHT_SPECTRUM (if applicable) columns and
         values in the SIGMA and SIGMA_SPECTRUM are set to 1/sqrt(newly
         computed weight). If a weight value is 0, the corresponding
         sigma value is -1. 3. If datacolumn='data' or 'residual_data'
         and the 'CORRECTED_DATA' column does exist, then the WEIGHT and
         WEIGHT_SPECTRUM columns are not updated and values in the SIGMA
         and SIGMA_SPECTRUM are set to 1/sqrt(of the newly computed
         weight). If a weight value is 0, the corresponding sigma value
         is -1. In this case, you should either split out the DATA
         column and run statwt, or run with datacolumn='corrected' or
         'residual' to update WEIGHT/WEIGHT_SPECTRUM. Otherwise the data
         are internally not consistent. TIME BINNING One of two
         algorithms can be used for time binning. If slidetimebin=True,
         then a sliding time bin of the specified width is used. If
         slidetimebin=False, then block time processing is used. The
         sliding time bin algorithm will generally be both more memory
         intensive and take longer than the block processing algorithm.
         Each algorithm is discussed in detail below. If the value of
         timebin is an integer, this value represents the number of
         contiguous, unique time stamps (from the MS TIME column) that
         should be used for averaging. Block Time Processing The data
         are processed in contiguous time blocks in this case. This
         means that all WEIGHT_SPECTRUM values will be set to the same
         value for all data within the same time bin/channel
         bin/correlation bin (see the section on channel binning and
         description of combine="corr" for more details on channel
         binning and correlation binning). If timebin is specified as a
         time quantity (eg, '110s'), then the time bins are not
         necessarily contiguous and are not necessarily the same width.
         The start of a bin is always coincident with a value from the
         TIME column, So for example, if values from the TIME column are
         [20s, 60s, 100s, 140s, 180s, 230s], and timebin = 110s, the
         first bin would start at 20s and run to 130s, so that data from
         timestamps 20s, 60s, and 100s will be included in the first
         bin. The second bin would start at 140s, so that data for
         timestamps 140s, 180s, and 230s would be included in the second
         bin. In the case where timebin is an integer, this denotes the
         number of contigous timestamps that should be binned together.
         Note that, in this case, for rows "left over" in the upper edge
         of the bin, their values are computed using timebin that would
         include rows with times earlier than them. For example, in an
         MS with 8 rows in one block to be processed and timebin=3,
         timestamps 1, 2, and 3 would be used to compute the weights of
         the first three three rows, and rows 4, 5, and 6 would be used
         to compute weights for the next three rows as expected. Rows 7
         and 8 are "left over" rows, but three rows (as per the integer
         timebin specification) are still used to compute them. Row 7
         and 8 weights are computed by combining data in rows 6, 7, and
         8. Sliding Time Window Processing In the sliding time window
         case, in the case where timebin is a time quantity, the time
         window is always centered on the timestamp of the row in
         question and extends +/-timebin/2 around that timestamp,
         subject the the time block boundaries. In the case where
         timebin is an integer, there are two cases to consider: timebin
         is odd: In this case the target row's data and the data from
         the +/-(n-1)/2 rows around the target row are also used.
         timebin is even: In this case, the target row's data and the
         data from the n/2 rows after the target row and the n/2 - 1
         rows before the target row are used. When timebin is an int,
         for "edge" rows, the timebin extends from the edge of the block
         to the corresponding timebin value of rows away from the edge,
         so that the timebin is not symmetrical around the target rows,
         but includes the number of rows specified by the timebin value.
         OVERRIDING DEFAULT BLOCK BOUNDARIES Rows with the same
         baselines and data description IDs which are included in that
         window are used for determining the weight of that row. The
         boundaries of the time block to which the window is restricted
         are determined by changes in FIELD_ID, ARRAY_ID, and
         SCAN_NUMBER. One can override this behavior for FIELD_ID and/or
         SCAN_NUMBER by specifying the combine parameter (see below).
         Unlike the time block processing algorithm, this sliding time
         window algorithm requires that details of all rows for the time
         window in question are kept in memory, and thus the sliding
         window algorithm in general and the block processing row when
         timebin is an int, requires more memory than the block
         processing method when timebin is a quantity. Also, unlike the
         block processing method which computes a single value for all
         weights within a single bin, the sliding window method requires
         that each row (along with each channel and correlation bin) be
         processed individually, so in general the sliding window method
         will take longer than the block processing method. CHANNEL
         BINNING The width of channel bins is specified via the chanbin
         parameter. Channel binning occurs within individual spectral
         windows; bins never span multiple spectral windows. Each
         channel will be included in exactly one bin. The default value
         "spw" indicates that all channels in each spectral window are
         to be included in a single bin. Any other string value is
         interpreted as a quantity, and so should have frequency units,
         eg "1MHz". In this case, the channel frequencies from the
         CHAN_FREQ column of the SPECTRAL_WINDOW subtable of the MS are
         used to determine the bins. The first bin starts at the channel
         frequency of the 0th channel in the spectral window. Channels
         with frequencies that differ by less than the value specified
         by the chanbin parameter are included in this bin. The next bin
         starts at the frequency of the first channel outside the first
         bin, and the process is repeated until all channels have been
         binned. If specified as an integer, the value is interpreted as
         the number of channels to include in each bin. The final bin in
         the spectral window may not necessarily contain this number of
         channels. For example, if a spectral window has 15 channels,
         and chanbin is specified to be 6, then channels 0-5 will
         comprise the first bin, channels 6-11 the second, and channels
         12-14 the third, so that only three channels will comprise the
         final bin. MINIMUM REQUIRED NUMBER OF VISIBILITIES The minsamp
         parameter allows the user to specify the minimum number of
         unflagged visibilities that must be present in a sample for
         that sample's weight to be computed. If a sample has less than
         this number of unflagged points, the associated weights of all
         the points in the sample are set to zero, and all the points in
         the sample are flagged. AGGREGATING DATA ACROSS BOUNDARIES By
         default, data are not aggregated across changes in values in
         the columns ARRAY_ID, SCAN_NUMBER, STATE_ID, FIELD_ID, and
         DATA_DESC_ID. One can override this behavior for SCAN_NUMBER,
         STATE_ID, and FIELD_ID by specifying the combine parameter. For
         example, specifying combine="scan" will ignore scan boundaries
         when aggregating data. Specifying combine="field, scan" will
         ignore both scan and field boundaries when aggregating data.
         Also by default, data for separate correlations are aggregated
         separately. Data for all correlations within each spectral
         window can be aggregated together by specifying "corr" in the
         combine parameter. Any combination and permutation of "scan",
         "field", "state", and "corr" are supported by the combine
         parameter. Other values will be silently ignored. STATISTICS
         ALGORITHMS The supported statistics algorithms are described in
         detail in the imstat and ia.statistics() help. For the current
         application, these algorithms are used to compute vr and vi
         (see above), such that the set of the real parts of the
         visibilities and the set of the imaginary parts of the
         visibilities are treated as independent data sets. RANGE OF
         ACCEPTABLE WEIGHTS The wtrange parameter allows one to specify
         the acceptable range (inclusive, except for zero) for weights.
         Data with weights computed to be outside this range will be
         flagged. If not specified (empty array), all weights are
         considered to be acceptable. If specified, the array must
         contain exactly two nonnegative numeric values. Note that data
         with weights of zero are always flagged. INCLUDING CHANNELS
         Channels can be included in the computation of the weights by
         specifying the fitspw parameter. This parameter accepts a valid
         MS channel selection string. Data associated with the selected
         channels will be used in computing the weights; all other
         channels will be excluded from the computation of weights. By
         default (empty string), all channels are included. PREVIEW MODE
         By setting preview=True, the application is run in "preview"
         mode. In this mode, no data in the input MS are changed,
         although the amount of data that the application would have
         flagged is reported. DATA COLUMN The datacolumn parameter can
         be specified to indicate which data column should be used for
         computing the weights. The values "corrected" for the
         CORRECTED_DATA column and "data" for the DATA column are
         supported (minimum match, case insensitive). One may specify
         'residual' in which case the values used are the result of the
         CORRECTED_DATA column - model, or 'residual_data' in which case
         the values used are the DATA column - model, where model is the
         CORRECTED_DATA column if it exists, or if it doesn't, the
         virtual source model if one exists, or if that doesn't, then no
         model is used and the 'residual' and 'residual_data' cases are
         equivalent to the 'corrected' and 'data' cases, respectively.
         The last two options are to allow for operation on timescales
         or frequency ranges which are larger than that over which the
         sky signal is expected to be constant. This situation arises in
         eg, OTF mapping, and also perhaps with sources with significant
         spectral structure. In cases where a necessary column doesn't
         exist, an exception will be thrown and no data will be changed.
         NOTE: It is the user's responsibility to ensure that a model
         has been set for all selected fields before using
         datacolumn='residual' or 'residual_data'. RETURN VALUE In all
         cases, the mean and variance of the set of all weights computed
         by the application is reported and returned in a dictionary
         with keys 'mean' and 'variance'. Weights for which there are
         corresponding flags (=True) prior to running the application
         are excluded from the computation of these statistics. If the
         WEIGHT_SPECTRUM values are available, they are used to compute
         the statistics, otherwise, the WEIGHT values are used. The
         returned statistics are always computed using the classic
         algorithm; the value of statalg has no impact on how they are
         computed. OTHER CONSIDERATIONS Flagged values are not used in
         computing the weights, although the associated weights of these
         values are updated. If the variance for a set of data is 0, all
         associated flags for that data are set to True, and the
         corresponding weights are set to 0. Because data are modified
         in the input MS, the nomodify parameter must be set to False
         when opening the associated MS tool.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         combine : undefined

      .. container:: methodparmtable

         Ignore changes in these columns (scan, field, and/or state)
         when aggregating samples to compute weights. The value "corr"
         is also supported to aggregate samples across correlations.

.. container:: parameters2

   timebin : any = 1

.. container:: methodparmtable

   Size of the time window that is used to determine the statistics of a
   weight. Can be an integer number of timestamps or a time interval in
   time units.

Example

4"300s"

.. container:: parameters2

   slidetimebin : undefined = false

.. container:: methodparmtable

   Use a sliding window for time binning, as opposed to time block
   processing?

Example

True

.. container:: parameters2

   chanbin : any = spw

.. container:: methodparmtable

   Channel bin width for computing weights. Can either be integer, in
   which case it is interpreted as number of channels to include in each
   bin, or a string "spw" or quantity with frequency units.

Example

51.5MHz

.. container:: parameters2

   minsamp : undefined = 2

.. container:: methodparmtable

   Minimum number of visibilities required for computing weights in a
   sample. Must be >= 2.

Example

10

.. container:: parameters2

   statalg : undefined = classic

.. container:: methodparmtable

   Statistics algorithm to use for computing variances. Supported values
   are "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum
   match is supported.

Example

"cl", "ch", "f", or "h"

.. container:: parameters2

   fence : undefined = -1

.. container:: methodparmtable

   Fence value for statalg="hinges-fences". A negative value means use
   the entire data set (ie default to the "classic" algorithm). Ignored
   if statalg is not "hinges-fences".

Example

0.2

.. container:: parameters2

   center : undefined = mean

.. container:: methodparmtable

   Center to use for statalg="fit-half". Valid choices are "mean",
   "median", and "zero". Ignored if statalg is not "fit-half".

Example

"mean", "median", or "zero"

.. container:: parameters2

   lside : undefined = true

.. container:: methodparmtable

   For statalg="fit-half", real data are <=; center? If false, real data
   are >= center. Ignored if statalg is not "fit-half".

Example

True

.. container:: parameters2

   zscore : undefined = -1

.. container:: methodparmtable

   For statalg="chauvenet", this is the target maximum number of
   standard deviations data may have to be included. If negative, use
   Chauvenet's criterion. Ignored if statalg is not "chauvenet".

Example

3.5

.. container:: parameters2

   maxiter : undefined = -1

.. container:: methodparmtable

   For statalg="chauvenet", this is the maximum number of iterations to
   attempt. Iterating will stop when either this limit is reached, or
   the zscore criterion is met. If negative, iterate until the zscore
   criterion is met. Ignored if statalg is not "chauvenet".

Example

10

.. container:: parameters2

   fitspw : undefined

.. container:: methodparmtable

   Channels to include in the computation of weights. Specified as an MS
   select channel selection string.

Example

"0:5~30"

.. container:: parameters2

   excludechans : undefined = false

.. container:: methodparmtable

   If True: invert the channel selection in fitspw and exclude the
   fitspw selection from the computation of the weights.

Example

True

.. container:: parameters2

   wtrange : undefined

.. container:: methodparmtable

   Range of acceptable weights. Data with weights outside this range
   will be flagged. Empty array (default) means all weights are good.

Example

[0.1, 10]

.. container:: parameters2

   preview : undefined = false

.. container:: methodparmtable

   Preview mode. If True, no data is changed, although the amount of
   data that would have been flagged is reported.

Example

True or False

.. container:: parameters2

   datacolumn : undefined = corrected

.. container:: methodparmtable

   Data column to use to compute weights. Supported values are "data",
   "corrected", "residual, and "residual_data" (case insensitive,
   minimum match supported).

Example

"data" or "corrected"

.. container:: methodsection

   Example

.. container:: methodexam

   # update the weights of an MS ms.open("my.ms", nomodify=False) #
   compute weights, using time bins of 300s if
   ms.statwt(timebin=("300s")): print "Successfully updated weights"
   else: print "Updating weights failed" ms.done()

.. container:: param

   function **oldstatwt**

   .. container:: collcontent

      .. container:: methoddesc

         NOT IMPLEMENTED YET. This function estimates the noise from the
         scatter of the visibilities, sets SIGMA to it, and WEIGHT to
         SIGMA**-2. Ideally the visibilities used to estimate the
         scatter, as selected by fitspw and fitcorr, should be pure
         noise. If you know for certain that they are, then setting
         dorms to True will give the best result. Otherwise, use False
         (standard sample standard deviation). More robust scatter
         estimates like the interquartile range or median absolute
         deviation from the median are not offered because they require
         sorting by value, which is not possible for complex numbers. To
         beat down the noise of the noise estimate, the sample size per
         estimate can be made larger than a single spw and baseline.
         (Using combine='spw' is to interpolate between spws with
         line-free channels is recommended when an spw has no line-free
         channels.) timebin smooths the noise estimate over time.
         windowtype sets the type of time smoothing. WEIGHT and SIGMA
         will not be changed for samples that have fewer than minsamp
         visibilities. Selected visibilities for which no noise estimate
         is made will be flagged. Note that minsamp is effectively at
         least 2 if dorms is False, and 1 if it is True.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         dorms : undefined = false

      .. container:: methodparmtable

         How the scatter should be estimated (True -> rms, False ->
         stddev).

.. container:: parameters2

   byantenna : undefined = true

.. container:: methodparmtable

   How the scatters are solved for (by antenna or by baseline).

.. container:: parameters2

   sepacs : undefined = true

.. container:: methodparmtable

   If solving by antenna, treat autocorrs separately.

.. container:: parameters2

   fitspw : undefined = \*

.. container:: methodparmtable

   Line-free spectral windows (and :channels) to get the scatter from.
   ('' => all)

.. container:: parameters2

   fitcorr : undefined

.. container:: methodparmtable

   Correlations (V, LL, XX, LR, XY, etc.) to get the scatter from. (''
   => all)

.. container:: parameters2

   combine : undefined

.. container:: methodparmtable

   Ignore changes in these columns (spw, scan, and/or state) when
   getting the scatter.

.. container:: parameters2

   timebin : undefined = 0s

.. container:: methodparmtable

   Duration of the moving window over which to estimate the scatter.
   Defaults to 0s, with an effective minimum of 1 integration.

.. container:: parameters2

   minsamp : undefined = 3

.. container:: methodparmtable

   The minimum number of visibilities for a scatter estimate.

.. container:: parameters2

   field : undefined

.. container:: methodparmtable

   Fields to reweight, by names or 0-based ids. ('' => all)

.. container:: parameters2

   spw : undefined = \*

.. container:: methodparmtable

   Spectral windows to reweight. ('' => all)

.. container:: parameters2

   antenna : any

.. container:: methodparmtable

   Select data based on antenna/baseline.

.. container:: parameters2

   timerange : undefined

.. container:: methodparmtable

   Select data by time range.

.. container:: parameters2

   scan : undefined

.. container:: methodparmtable

   Scan numbers to reweight. ('' => all)

.. container:: parameters2

   intent : undefined

.. container:: methodparmtable

   Scan intents to reweight. ('' => all)

.. container:: parameters2

   array : undefined

.. container:: methodparmtable

   Select (sub)array(s) by array ID number.

.. container:: parameters2

   correlation : undefined

.. container:: methodparmtable

   Correlations (LL, XX, LR, XY, etc.) to reweight. ('' => all)

.. container:: parameters2

   obs : undefined

.. container:: methodparmtable

   Observation IDs to reweight. ('' => all)

.. container:: parameters2

   datacolumn : undefined = corrected_data

.. container:: methodparmtable

   Which data column to calculate the scatter from.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("multiwin.ms", nomodify=False)
   ms.oldstatwt(fitspw='0:0~123;145~211,2:124~255', field=[0],
   spw='0,2') In this example the noise estimates are separately made
   from and applied to spws 0 and 2.
   ms.oldstatwt(fitspw='0:0~123;145~211,2:124~255', fitorder=0,
   field=[0], combine='spw') ms.close() This time the estimate for each
   baseline is made from the line-free channels of spws 0 and 2, and
   applied to all the spws, including 1 (which could be a completely
   line-filled spw).

.. container:: param

   function **regridspw**

   .. container:: collcontent

      .. container:: methoddesc

         This function permits you to transform the spectral data of
         your measurement set to a given reference frame. The present
         reference frame information in the MS is examined and the
         transformation performed accordingly. Since all such
         transformations are linear in frequency, a pure change of
         reference frame only affects the channel boundary definitions.
         In addition, the function permits you to permanently regrid the
         data, i.e. reduce the channel number and/or move the boundaries
         using several interpolation methods (selected using parameter
         "interpolation"). The new channels are equidistant in frequency
         (if parameter "mode" is chosen to be vrad or freq, or
         equidistant in wavelength if parameter "mode" is chosen to be
         vopt or wave). If "mode" is chosen to be "chan", the regridding
         is performed by combining the existing channels, i.e. not
         moving but just eliminating channel boundaries where necessary.
         The regridding is applied to the channel definition and all
         data of the MS, i.e. all columns which contain arrays whose
         dimensions depend on the number of channels. The input
         parameters are verified before any modification is made to the
         MS. The target reference frame can be set by providing the name
         of a standard reference frame (LSRK, LSRD, BARY, GALACTO,
         LGROUP, CMB, TOPO, GEO, or SOURCE, default = no change of
         frame) in parameter "outframe". For each field in the MS, the
         channel frequencies are transformed from their present
         reference frame to the one given by parameter "outframe". If
         the regridding parameters are set, they are interpreted in the
         "outframe" reference frame. The regridding is applied to the
         data after the reference frame transformation.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         outframe : undefined = LSRK

      .. container:: methodparmtable

         Name of the reference frame to transform to (LSRK, LSRD, BARY,
         GALACTO, LGROUP, CMB, GEO, TOPO, or SOURCE). SOURCE is meant
         for solar system work and corresponds to GEO + a radial
         velocity correction (only available for ephemeris objects). If
         no reference frame is given, the present reference frame given
         by the data is used, i.e. the reference frame is not changed.
         The observatory position is taken as the average of all antenna
         positions.

.. container:: parameters2

   mode : undefined = chan

.. container:: methodparmtable

   The quantity (radio velocity (m/s), optical velocity (m/s), frequency
   (Hz), wavelength (m), or original channels) in which the user would
   like to give the regridding parameters below ("center", "chanwidth",
   "bandwidth"): vrad, vopt, freq, wave, or chan.

.. container:: parameters2

   restfreq : undefined = -3E30

.. container:: methodparmtable

   Required in case the value of mode is "vrad" or "vopt": Rest
   frequency (Hz) for the conversion of the regrid parameters "center",
   "chanwidth", and "bandwidth" to frequencies.

.. container:: parameters2

   interpolation : undefined = LINEAR

.. container:: methodparmtable

   Name of the interpolation method (NEAREST, LINEAR, SPLINE, CUBIC,
   FFTSHIFT) used in the regridding. Flagging information is combined
   using "inclusive or".

.. container:: parameters2

   start : undefined = -3E30

.. container:: methodparmtable

   Desired lower edge of the spectral window after regridding in the
   units given by "mode" and in the reference frame given by "outframe".
   If no value is given, it is determined from "center" and "bandwidth".

.. container:: parameters2

   center : undefined = -3E30

.. container:: methodparmtable

   (Alternative to setting the parameter "start".) Desired center of the
   spectral window after regridding in the units given by "mode" and in
   the reference frame given by "outframe". If no value is given, the
   center is determined from "start" and "bandwidth" or, if "start" is
   not given either, it is kept as it is.

.. container:: parameters2

   bandwidth : undefined = -1.

.. container:: methodparmtable

   Desired width of the entire spectral window after regridding in the
   units given by "mode" and in the reference frame given by "outframe".
   If no value is given or the given width is larger than the bandwidth
   of the data, the width will be truncated to the maximum width
   possible symmetrically around the value given by "center".

.. container:: parameters2

   chanwidth : undefined = -1.

.. container:: methodparmtable

   Desired width of the channels in the units given by "mode" and in the
   reference frame given by "outframe". This implies that channels will
   be equidistant in the unit given by "mode". If no value is given and
   "mode" is vrad or freq, the function will keep the resolution as it
   is. If "mode" is vopt or wave, the total number of channels will be
   kept as is.

.. container:: parameters2

   hanning : undefined = true

.. container:: methodparmtable

   If true, perform hanning smoothing before regridding.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.fromfits("NGC5921.MS","/usr/lib/casapy/data/demo/NGC5921.fits")
   ms.regridspw(outframe="LSRK") This example reads a measurement set
   and transforms its spectral axis to the LSRK reference frame.
   ms.regridspw(outframe="BARY", mode="vrad", center=73961800.,
   chanwidth=50., bandwidth=1000., restfreq=1420405750e6) In this
   example, all spectral windows in the MS will be transformed to the
   BARY reference frame and then be regridded such that the center of
   the new spectral window is at radio velocity = 73961800. m/s (BARY).
   If the bandwidth of the observation is large enough the total width
   of the spectral window will be 1000 m/s, i.e. 20 channels of width 50
   m/s, 10 on each side of the given center. ms.regridspw(mode="vopt",
   restfreq=1420405750e6) In this example the channels are regridded
   such that they are equidistant in optical velocity. The reference
   frame and number of channels is kept as is. ms.regridspw(mode="chan",
   center=64, chanwidth=2, bandwidth=102) In this example, the channels
   are regridded such that the new bandwidth is 102 of the original
   channels centered on the original channel 64, and the new channels
   are twice as wide as the original channels.

.. container:: param

   function **cvel**

   .. container:: collcontent

      .. container:: methoddesc

         This function permits you to transform the spectral data of
         your measurement set to a given reference frame and/or regrid
         it. It will combine all spectral windows of the MS into one.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         mode : undefined = channel

      .. container:: methodparmtable

         "channel", "velocity", "frequency", or "channel_b", default =
         "channel".

.. container:: parameters2

   nchan : undefined = -1

.. container:: methodparmtable

   number of channels, default = -1 = all.

.. container:: parameters2

   start : any = 0

.. container:: methodparmtable

   start channel, default =

.. container:: parameters2

   width : any = 1

.. container:: methodparmtable

   new channel width, default =

.. container:: parameters2

   interp : undefined = linear

.. container:: methodparmtable

   interpolation method "nearest", "linear", "spline", "cubic",
   "fftshift", default =

.. container:: parameters2

   phasec : any

.. container:: methodparmtable

   phase center, default = first field

.. container:: parameters2

   restfreq : any = 1.4GHz

.. container:: methodparmtable

   rest frequency, default =

.. container:: parameters2

   outframe : undefined

.. container:: methodparmtable

   LSRK, LSRD, BARY, GALACTO, LGROUP, CMB, GEO, TOPO, or SOURCE default
   = "" = keep reference frame.

.. container:: parameters2

   veltype : undefined = radio

.. container:: methodparmtable

   radio or optical, default =

.. container:: parameters2

   hanning : undefined = true

.. container:: methodparmtable

   If true, perform hanning smoothing before regridding.

.. container:: methodsection

   Example

.. container:: methodexam

.. container:: param

   function **hanningsmooth**

   .. container:: collcontent

      .. container:: methoddesc

         This function Hanning smooths the frequency channels with a
         weighted running average of: smoothedData[i] =
         0.25*correctedData[i-1] + 0.50*correctedData[i] +
         0.25*correctedData[i-1] The first and last channels are
         flagged. Inclusion of a flagged value in an average causes that
         averaged data value to be flagged.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datacolumn : undefined = corrected

      .. container:: methodparmtable

         the name of the MS column into which to write the smoothed data

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('ngc5921.ms',nomodify=False) ms.hanningsmooth('data')
   ms.close()

.. container:: param

   function **cvelfreqs**

   .. container:: collcontent

      .. container:: methoddesc

         Take the spectral grid of a given spectral window, tranform and
         regrid it as prescribed by the given grid parameters (same as
         in cvel and clean) and return the transformed values as a list.
         The MS is not modified. Useful for tests of gridding parameters
         before using them in cvel or clean.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         spwids : undefined = 0

      .. container:: methodparmtable

         The list of ids of the spectral windows from which the input
         grid is to be taken.

.. container:: parameters2

   fieldids : undefined = 0

.. container:: methodparmtable

   The list of ids of the fields which are selected (for observation
   time determination), default: all

.. container:: parameters2

   obstime : undefined

.. container:: methodparmtable

   The observation time to assume, default: time of the first row of the
   MS

.. container:: parameters2

   mode : undefined = channel

.. container:: methodparmtable

   "channel", "velocity", "frequency", or "channel_b"

.. container:: parameters2

   nchan : undefined = -1

.. container:: methodparmtable

   Number of channels, default = all

.. container:: parameters2

   start : any = 0

.. container:: methodparmtable

   Start channel.

.. container:: parameters2

   width : any = 1

.. container:: methodparmtable

   New channel width.

.. container:: parameters2

   phasec : any

.. container:: methodparmtable

   Phase center, default=first field in selection.

.. container:: parameters2

   restfreq : any = 1.4GHz

.. container:: methodparmtable

   Rest frequency.

.. container:: parameters2

   outframe : undefined

.. container:: methodparmtable

   LSRK, LSRD, BARY, GALACTO, LGROUP, CMB, GEO, TOPO, or SOURCE default
   = keep reference frame.

.. container:: parameters2

   veltype : undefined = radio

.. container:: methodparmtable

   Radio or optical.

.. container:: parameters2

   verbose : undefined = true

.. container:: methodparmtable

   If true, create log output.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('my.ms') ms.cvelfreqs(spwids=[1], mode='channel', nchan=20,
   start=2, width=3, outframe='LSRK') This will take the grid of SPW 1
   (i.e. the second in the SPW table), regrid it as in cvel with the
   given grid parameters and return the resulting channel centers as an
   array. The MS is not modified. See help cvel for more details on the
   grid parameters.

.. container:: param

   function **contsub**

   .. container:: collcontent

      .. container:: methoddesc

         NOT FULLY IMPLEMENTED YET. uvcontsub uses the cb tool for now.
         (The only reason to implement it in ms is to save time and disk
         space.) This function estimates the continuum emission of the
         MS and writes a MS with that estimate subtracted, using the ms
         tool. The estimate is made, separately for the real and
         imaginary parts of each baseline, by fitting a low order
         polynomial to the unflagged visibilities selected by fitspw
         (depending on combine).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         outputms : undefined

      .. container:: methodparmtable

         The name of the resulting measurement set.

.. container:: parameters2

   fitspw : undefined = \*

.. container:: methodparmtable

   Line-free spectral windows (and :channels) to fit to.

.. container:: parameters2

   fitorder : undefined = 1

.. container:: methodparmtable

   The order of the polynomial to use when fitting.

.. container:: parameters2

   combine : undefined

.. container:: methodparmtable

   Ignore changes in these columns (spw, scan, and/or state) when
   fitting.

.. container:: parameters2

   spw : undefined = \*

.. container:: methodparmtable

   Spectral windows (and :channels) to select.

.. container:: parameters2

   unionspw : undefined = \*

.. container:: methodparmtable

   The union of fitspw and spw, i.e. how much needs to be read. '*'
   always works, but may be more than you need.

.. container:: parameters2

   field : undefined

.. container:: methodparmtable

   Fields to include, by names or 0-based ids. ('' => all)

.. container:: parameters2

   scan : undefined

.. container:: methodparmtable

   Only use the scan numbers requested using the msselection syntax.

.. container:: parameters2

   intent : undefined

.. container:: methodparmtable

   Only use the requested scan intents.

.. container:: parameters2

   correlation : undefined

.. container:: methodparmtable

   Limit data to specific correlations (LL, XX, LR, XY, etc.).

.. container:: parameters2

   obs : undefined

.. container:: methodparmtable

   Only use the requested observation IDs.

.. container:: parameters2

   whichcol : undefined = CORRECTED_DATA

.. container:: methodparmtable

   'DATA', 'MODEL_DATA', 'CORRECTED_DATA', and/or 'FLOAT_DATA'

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("multiwin.ms") ms.contsub('contsub.ms',
   fitspw='0:0~123;145~211,2:124~255', fitorder=0, field=[0], spw='0,2')
   In this example the continuum estimates are made by seperately
   averaging channels 0:0~123;145~211 and 2:124~255, and the separate
   estimates are subtracted from spws 0 and 2. The output only includes
   field 0 and spws 0 and 2 (now called 1). ms.contsub('contsub.ms',
   fitspw='0:0~123;145~211,2:124~255', fitorder=0, field=[0],
   combine='spw') ms.close() This time the estimate was made by
   simultaneously averaging channels 0:0~123;145~211 and 2:124~255, and
   the continuum is subtracted from all the spws, including 1 (treated
   as a completely line-filled spw). The output only includes field 0.

.. container:: param

   function **continuumsub**

   .. container:: collcontent

      .. container:: methoddesc

         This function provides a means of continuum determination and
         subtraction by fitting a polynomial of desired order to a
         subset of channels in each time-averaged uv spectrum. The fit
         is used to model the continuum in all channels (not just those
         used in the fit), for subtraction, if desired. Use the fitspw
         parameter to limit the spectral windows processed and the range
         of channels used to estimate the continuum in each (avoid
         channels containing spectral lines). The default solution
         interval 'int' will result in per-integration continuum fits
         for each baseline. The mode parameter indicates how the
         continuum model (the result of the fit) should be used: -
         'subtract' will store the continuum model in the MODEL_DATA
         column and subtract it from the CORRECTED_DATA column -
         'replace' will replace the CORRECTED_DATA column with the
         continuum model (useful if you want to image the continuum
         model result) - 'model' will only store the continuum model in
         the MODEL_DATA column (the CORRECTED_DATA is unaffected). It is
         important to start the ms tool with nomodify=False so that
         changes to the dataset will be allowed (see example below). For
         now, the only way to recover the un-subtracted CORRECTED_DATA
         column is to use calibrater.correct() again. Note that the
         MODEL_DATA and CORRECTED_DATA columns must be present for
         continuumsub to work correctly. The function will warn the user
         if they are not present, and abort. To add these scratch
         columns, close the ms tool, then start a calibrater or an
         imager tool, which will add the scratch columns. Then restart
         the ms tool, and try continuumsub again.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : any

      .. container:: methodparmtable

         Select fields to fit.

.. container:: parameters2

   fitspw : any

.. container:: methodparmtable

   Spectral windows/channels to use for fitting the continuum; default
   all spectral windows in all channels.

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Select spectral windows and channels from which to subtract a
   continuum estimate; default: all channels in all spectral windows for
   which the continuum was estimated

.. container:: parameters2

   solint : any = int

.. container:: methodparmtable

   Continuum fit timescale (units optional).

.. container:: parameters2

   fitorder : undefined = 0

.. container:: methodparmtable

   Polynomial order for fit.

.. container:: parameters2

   mode : undefined = subtract

.. container:: methodparmtable

   Desired use of fit model (see above).

.. container:: methodsection

   Example

.. container:: methodexam

   ms.fromfits('ngc5921.ms','/aips++/data/demo/NGC5921.fits') ms.close()
   cb.open('ngc5921.ms') # add MODEL_DATA, CORRECTED_DATA columns
   cb.close() ms.open('ngc5921.ms', nomodify=False); # writable!
   ms.continuumsub(field=2, fitspw='0:5~9;50~59', solint=0.0,
   fitorder=1, mode='subtract') ms.done() This example will fit a linear
   continuum to channels 5-9 and 50-59 in spectral window 0 in each
   scan-averaged spectrum for field 2, store the result in the
   MODEL_DATA column, and subtract it from the CORRECTED_DATA column.

.. container:: param

   function **uvsub**

   .. container:: collcontent

      .. container:: methoddesc

         This function subtracts model visibility data from corrected
         visibility data leaving the residuals in the corrected data
         column. If the parameter reverse is set True, this process is
         reversed.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         reverse : undefined = false

      .. container:: methodparmtable

         When False, subtracts model from visibility data; when True,
         adds model to visibility data.

.. container:: methodsection

   Example

.. container:: methodexam

   The following example subtracts a model from the visibility data
   leaving the residuals in the corrected data column.
   ms.open('ngc5921.ms',nomodify=False) ms.uvsub() ms.close() The
   following example adds the model back into the residuals.
   ms.open('ngc5921.ms',nomodify=False) ms.uvsub(reverse=True)
   ms.close()

.. container:: param

   function **addephemeris**

   .. container:: collcontent

      .. container:: methoddesc

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         id : undefined = -1

      .. container:: methodparmtable

         The unique id number to give to this ephemeris (will overwrite
         pre-existing ephemeris of same id, -1 will use next unused id).

.. container:: parameters2

   ephemerisname : undefined

.. container:: methodparmtable

   The name of the ephemeris table which is to be copied into the MS.

.. container:: parameters2

   comment : undefined

.. container:: methodparmtable

   Comment string (no spaces, will be part of a file name).

.. container:: parameters2

   field : any

.. container:: methodparmtable

   Field id(s) (0-based) or fieldname(s) to connect this ephemeris to.

.. container:: methodsection

   Example

.. container:: methodexam

   ms.addephemeris(id=0, ephemerisname="Titan_55002-55003dUTC.tab",
   comment="JPLTitan", field="Titan")

.. container:: param

   function **timesort**

   .. container:: collcontent

      .. container:: methoddesc

         This function sorts the main table of the measurement set by
         the contents of the column TIME in ascending order and writes a
         copy of the MS with the sorted main table into newmsfile. If no
         newmsname is given, a sorted copy of the MS is written into a
         new MS under the name x.sorted (where x is the name of the
         original MS). The original MS is then closed and deleted. The
         new MS is renamed to the name of the original MS and then
         reopened.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         newmsname : undefined

      .. container:: methodparmtable

         Name of the output measurement set (default: overwrite
         original)

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS", nomodify=False) ms.timesort() ms.done() This
   example sorts the main table of 3C273XC1.MS by time. The original MS
   is overwritten by the sorted one.

.. container:: param

   function **sort**

   .. container:: collcontent

      .. container:: methoddesc

         This function sorts the main table of the measurement set by
         the contents of the input set of columns in ascending order and
         writes a copy of the MS with the sorted main table into
         newmsfile. If no newmsname is given, a sorted copy of the MS is
         written into a new MS under the name x.sorted (where x is the
         name of the original MS). The original MS is then closed and
         deleted. The new MS is renamed to the name of the original MS
         and then reopened.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         newmsname : undefined

      .. container:: methodparmtable

         Name of the output measurement set (default: overwrite
         original).

.. container:: parameters2

   columns : undefined

.. container:: methodparmtable

   Vector of column names (case sensitive).

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS", nomodify=False)
   ms.sort(['ANTENNA1','ANTENNA2']) ms.done() This example sorts the
   main table of 3C273XC1.MS by ANTENNA1 and then ANTENNA2. The original
   MS is overwritten by the sorted one.

.. container:: param

   function **iterinit**

   .. container:: collcontent

      .. container:: methoddesc

         Specify the columns to iterate over and the time interval to
         use for the TIME column iteration. The columns are specified by
         their MS column name and must contain scalar values. Note that
         the following default sort columns are always added to the
         specified columns: array_id, field_id, data_desc_id and time.
         This is so that the iterator can keep track of the coordinates
         associated with the data (field direction, frequency, etc.). If
         you want to sort on these columns last instead of first, you
         need to include them in the columns specified. If you don't
         want to sort on these columns at all, you can set
         adddefaultsortcolumns to False. You may want to use iteration
         for a large dataset. After calling iterinit, you must call
         iterorigin before attempting to retrieve data with getdata. You
         need to call selectinit before calling this.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columns : undefined

      .. container:: methodparmtable

         Vector of column names (case sensitive).

.. container:: parameters2

   interval : undefined = 0.0

.. container:: methodparmtable

   Time interval in seconds (greater than 0), to group together in
   iteration.

.. container:: parameters2

   maxrows : undefined = 0

.. container:: methodparmtable

   Max number of rows (greater than 0) to return in iteration.

.. container:: parameters2

   adddefaultsortcolumns : undefined = true

.. container:: methodparmtable

   Add the default sort columns.

.. container:: methodsection

   Example

.. container:: methodexam

   See the example for the iterend function.

.. container:: param

   function **iterorigin**

   .. container:: collcontent

      .. container:: methoddesc

         Set or reset the iterator to the start of the currently
         specified iteration. You need to call this after iterinit,
         before attempting to retrieve data with getdata. You may also
         use iterorigin to set the iterator back to the start before you
         reach the end of the data.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         See the example for the iterend function.

.. container:: param

   function **iternext**

   .. container:: collcontent

      .. container:: methoddesc

         This sets the currently selected table (as accessed with
         getdata) to the next iteration. If there is no more data, the
         function returns False and the selection is reset to that
         before the iteration started. You need to call iterinit and
         iterorigin before calling this.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         See the example for the iterend function.

.. container:: param

   function **iterend**

   .. container:: collcontent

      .. container:: methoddesc

         This sets the currently selected table (as accessed with
         getdata) to the table that was selected before iteration
         started. Use this to end the iteration prematurely. There is no
         need to call this if you continue iterating until iternext
         returns False. See the example below.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open("3C273XC1.MS") ms.selectinit(datadescid=0)
         ms.iterinit(["ANTENNA1","ANTENNA2","TIME"],60.0)
         ms.iterorigin() rec=ms.getdata(["u","v","data"]) ms.iternext()
         rec=ms.getdata(["u","v","data"]) ms.iterend() We open the MS,
         select an array and spectral window and then specify an
         iteration over interferometer and time, with a 60s time
         interval. We then set the iterator to the start of the data and
         get out some data. Then we advance the iterator to the next lot
         of data, and finally end the iteration.

.. container:: param

   function **ngetdata**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::getdata() function in place of
         ms::ngetdata(). This method extracts the data as specified in
         the items parameter. The data is returned as a record with each
         item as a separate key in the record (all in lower case).
         Unless the iterator was initialized with a niterinit(), this
         method initializes the iterator as
         niterinit([".."],0.0,0,False).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Item names (NOT USED)

.. container:: parameters2

   ifraxis : undefined = false

.. container:: methodparmtable

   Create interferometer axis if True (NOT USED)

.. container:: parameters2

   ifraxisgap : undefined = 0

.. container:: methodparmtable

   Gap size on ifr axis when antenna1 changes (NOT USED)

.. container:: parameters2

   increment : undefined = 1

.. container:: methodparmtable

   Row increment for data access (NOT USED)

.. container:: parameters2

   average : undefined = false

.. container:: methodparmtable

   Average the data in time or over rows (NOT USED)

.. container:: param

   function **niterinit**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iterinit() function in place of
         ms::niterinit().

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columns : undefined

      .. container:: methodparmtable

         Vector of column names (case sensitive). This parameter is not
         used and is here only for backwards compatibility with the
         iterinit() method.

.. container:: parameters2

   interval : undefined = 0.0

.. container:: methodparmtable

   Time interval in seconds (greater than 0), to group together in
   iteration

.. container:: parameters2

   maxrows : undefined = 0

.. container:: methodparmtable

   Max number of rows (greater than 0) to return in iteration.

.. container:: parameters2

   adddefaultsortcolumns : undefined = true

.. container:: methodparmtable

   Add the default sort columns

.. container:: param

   function **niterorigin**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iterorigin() function in place
         of ms::niterorigin(). Set or reset the iterator to the start of
         the currently specified iteration. You need to call this before
         attempting to iteratively retrieve data with ngetdata. You can
         set the iteration back to the start before you reach the end of
         the data. You need to call iterinit before calling this. See
         the example below.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         See the example for the niterend function.

.. container:: param

   function **niternext**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iternext() function in place of
         ms::niternext(). This sets the currently selected table (as
         accessed with ngetdata) to the next iteration. If there is no
         more data, the function returns False. You need to call
         iterinit and iterorigin before calling this. See the example
         below.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         See the example for the niterend function.

.. container:: param

   function **niterend**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iterend() function in place of
         ms::niterend(). The serves redundant purpose and is here only
         for backward compatibility. This method returns True if there
         are no more iterations left. I.e., the iterations have ended.
         This same information is also returned by niternext(). With the
         use of the VisibilityIterator in the niterinit(),
         niterorigin(), niternext() methods, the iterator is set to the
         original state by calling niterinit() at any time. See the
         example below.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open("3C273XC1.MS") staql={'baseline':'1 & 2'};
         ms.msselect(staql); ms.niterinit([" "],60.0) ms.niterorigin()
         while (!ms.niterend()): rec=ms.ngetdata(["u","v","data"])
         ms.niternext() ms.close() We open the MS, select a baseline and
         then specify an iteration over time, with a 60s time interval.
         We then set the iterator to the start of the data and get out
         some data. We advance the iterator to the next lot of data and
         continue till the end of iterations is indicated. Finally, we
         close the ms tool which restores the tool to its original
         state.

.. container:: param

   function **nrowold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::nrow() function in place of
         ms::nrowold(). This function returns the number of rows in the
         measurement set. If the optional argument selected is set to
         True, it returns the number of currently selected rows,
         otherwise it returns the the number of rows in the original
         measurement.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         selected : undefined = false

      .. container:: methodparmtable

         return number of selected rows

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open('3C273XC1.MS') print "Number of rows in ms =", ms.nrowold()
   #Number of rows in ms = 7669

.. container:: param

   function **rangeold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::range() function in place of
         ms::rangeold(). This function will return the range of values
         in the currently selected measurement set for the items
         specified. Possible items include most scalar columns,
         interferometer number (1000*antenna1+antenna2), uvdist(ance),
         u, v, w, amplitude, phase, real and imaginary components of the
         data (and corrected and model versions of these - if these
         columns are present). See the table at the top of the document
         to find the exact list. You specify items in which you are
         interested using a string vector where each element is a case
         insensitive item name. This function will then return a record
         that has fields corresponding to each of the specified items.
         Each field will contain the range of the specified item. For
         many items the range will be the minimum and maximum values but
         for some it will be a list of unique values. Unrecognized items
         are ignored. By default the FLAG column is used to exclude
         flagged data before any ranges are determined, but you can set
         useflags=False to include flagged data in the range. However,
         if you average in frequency, flagging will still be applied.
         You can influence the memory use and the reading speed using
         the blocksize argument - it specifies how big a block of data
         to read at once (in MB). For large datasets on machines with
         lots of memory you may speed things up by setting this higher
         than the default (10 MB). For some items, you need to call
         selectinitold to select a portion of the data with a unique
         shape prior to calling this function. Items prefixed with
         corrected, model, residual or obs_residual are not available
         unless your measurement set has been processed either with the
         imager or calibrator tools.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Item names

.. container:: parameters2

   useflags : undefined = true

.. container:: methodparmtable

   Use the data flags

.. container:: parameters2

   blocksize : undefined = 10

.. container:: methodparmtable

   Set the blocksize in MB

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinitold(datadescid=0)
   ms.rangeold(["time","uvdist","amplitude","antenna1"]) #{'amplitude':
   array([ 2.60339398e-02, 3.38518333e+01]), # 'antenna1': array([ 0, 1,
   2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, # 14, 15, 16, 17, 18, 19, 20, 21,
   22, 23, 24, 25, 26]), # 'time': array([ 4.12162940e+09,
   4.12164267e+09]), # 'uvdist': array([ 46.26912101, 3727.97385983])}
   In this example the minimum and maximum observation times,
   uvdistances, data amplitudes are returned as well as a list of all
   the antennas in the antenna1 column. For this dataset the
   selectinitold function did not need to be called as all the data is
   of one shape.

.. container:: param

   function **selectinitold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::selectinit() function in place
         of ms::selectinitold(). A measurement set can contain data with
         a variety of different shapes (as described in the overall
         description to this tool). To allow functions to return data in
         fixed shape arrays you need to select, using this function,
         rows that contain the same data shape. You do not need to use
         this function if all the data in your measurement set has only
         one shape. The DATA_DESC_ID column in the measurement set
         contains a value that maps to a particular row in the
         POLARIZATION and SPECTRAL_WINDOW subtables. Hence all rows with
         the same value in the DATA_DESC_ID column must have the same
         data shape. To select all the data where the DATA_DESC_ID value
         is $N$ you call this function with the datadescid argument set
         to $N$. It is possible to have a measurement set with differing
         values in the DATA_DESC_ID column but where all the data is a
         fixed shape. For example this will occur if the reference
         frequency changes but the number of spectral channels is fixed.
         In cases like this all the data can be selected, using this
         function with an argument of zero. If the data shape does
         change and you call this function with an datadescid set to
         zero the return value will be False. In all other cases it will
         be True. To return to the completely unselected measurement
         set, set the reset argument to True. This will allow you to
         access the full range of rows in the measurement set, rather
         than just the selected measurement set. The datadescid must
         always be a non-negative integer.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         datadescid : undefined = 0

      .. container:: methodparmtable

         Data description id

.. container:: parameters2

   reset : undefined = false

.. container:: methodparmtable

   Reset to unselected state

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinitold(datadescid=0) print
   ms.rangeold(["uvdist"]) ms.selectinitold(reset=True) print
   ms.rangeold("uvdist") In this example we display the range of uv
   distances for the data in the specified measurement set (the range
   'items' argument is a list of strings, even if only one item is
   requested). The first print statement will only use data where the
   DATA_DESC_ID column is 0. This will correspond to a specific spectral
   window and polarization setup. The second print statement will print
   the range of uv distances for all the data in the measurement set
   (which is the same in this case).

.. container:: param

   function **selectold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::select() function in place of
         ms::selectold(). This function will select a subset of the
         current measurement set based on the range of values for each
         field in the input record. The rangeold function will return a
         record that can be altered and used as the argument for this
         function. A successful selection returns True. Unrecognized
         fields are ignored. Allowable items for selectold include:
         antenna1, antenna2, array_id, feed1, feed2, field_id,
         ifr_number, rows, scan_number, data_desc_id, time, times, u, v,
         w, and uvdist. You need to call selectinitold before calling
         this function. If you haven't then selectinitold will be called
         for you with default arguments. Repeated use of this function,
         with different arguments, will further refine the selection,
         resulting in a successively smaller selected measurement set.
         If the selected measurement set does not contain any rows then
         this function will return False and send a warning message in
         the logger. Otherwise this function will return True. To undo
         all the selections you need to use the selectinitold function
         (with reset=True).

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         record with fields contain ranges and enumerations

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinitold(datadescid=0)
   ms.selectold({'antenna1':[1,3,5],'uvdist':[1200.,1900.]})
   ms.selectold({'time':[4121629420.,4121638290.]}) # Or, convert time
   strings to seconds: start = qa.getvalue(qa.convert(
   qa.quantity('1989/06/27/01:03:40'),'s'))[0] stop =
   qa.getvalue(qa.convert( qa.quantity('1989/06/27/03:31:30'),'s'))[0]
   rec = {} rec['time'] = [start, stop] ms.selectold(items=rec) This
   example selects all the data from the measurement set where the value
   in the DATA_DESC_ID column is zero. This corresponds to a particular
   spectral window and polarization setup. It then selects all the data
   where the first antenna in the interferometer is number one, three or
   five and where the uv distance is between 1200 and 1900 meters.
   Finally it selects all the data which was observed between 4121629420
   seconds and 4121638290 seconds (since zero hours on the day where the
   modified Julian day is zero). Since this time in seconds is quite
   obscure I have also illustrated how to use the quanta tool to convert
   a date/time string into seconds which can then be used to perform the
   same time selection. The selections are cumulative so that at the end
   of this example only data in the specified time range, with the
   specified, interferometers, uv distances, spectral window and
   polarization setup are selected.

.. container:: param

   function **selecttaqlold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::selecttaql() function in place
         of ms::selecttaqlold(). This function will select a subset of
         the current measurement set based on the standard TaQL
         selection string given. Repeated use of this function, with
         different arguments, will further refine the selection,
         resulting in a successively smaller selected measurement set.
         If the selected measurement set does not contain any rows then
         this function will return False and send a warning message in
         the logger. Otherwise this function will return True. To undo
         all the selections you need to use the selectinitold function
         (with reset=True). Note that index values used in the TaQL
         string are zero-based as are all tool indices.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         msselect : undefined

      .. container:: methodparmtable

         TaQL selection string

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinitold(datadescid=0)
   ms.selectold({'antenna1':[0,2,4],'uvdist':[1200.,1900.]})
   ms.selecttaqlold('ANTENNA1==2') ms.rangeold(["ANTENNA1","ANTENNA2"])
   # {'antenna1': array([2]), # 'antenna2': array([ 6, 9, 11, 18, 20,
   21, 24])} This example selects all the data from the measurement set
   where the value in the DATA_DESC_ID column is zero. This corresponds
   to a particular spectral window and polarization setup. It then
   selects all the data where the first antenna in the interferometer is
   number zero, two or four and where the uv distance is between 1200
   and 1900 meters. Finally it uses a query to select all the data for
   which the ANTENNA1 column is 2 (this selects the middle antenna of
   the previous, zero-based, selection). The selections are cumulative
   so that at the end of this example only data in the specified time
   range, with the specified interferometers, uv distances, spectral
   window and polarization setup are selected.

.. container:: param

   function **selectchannelold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::selectchannel() function in
         place of ms::selectchannelold(). This function allows you to
         select a subset of the frequency channels in the current
         measurement set. This function can also average, over frequency
         channels, prior to providing the values to the user. Selection
         on channels is not allowed using either the select or command
         functions as they can only select entire rows in a measurement
         set. Channel selection involves accessing only some of the
         values in a row. Like all the selection functions this function
         does not change the current measurement but updates the
         measurement set selection parameters so that functions like
         getdataold will return the desired subset of the data. Repeated
         use of this function will overwrite any previous channel
         selection. There are four parameters, the number of output
         channels, the first input channel to use, the number of input
         channels to average into one output channel, and the increment
         in the input spectrum for the next output channel. All four
         parameters need to be specified. When all data to be averaged
         is unflagged, the result is the averaged value and the
         corresponding flag is False. When all data is flagged, the
         result is set to zero and the corresponding flag is True. When
         data to be averaged is mixed (unflagged and flagged), only the
         unflagged values are averaged and the flag is set to False.
         This function return True if the selection was successful, and
         False if not. In the latter case an error message will also be
         sent to the logger. You need to call selectinitold before
         calling this function. If you haven't then selectinitold will
         be called for you with default arguments.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         nchan : undefined = 1

      .. container:: methodparmtable

         Number of output channels, positive integer

.. container:: parameters2

   start : undefined = 0

.. container:: methodparmtable

   First input channel to use, positive integer

.. container:: parameters2

   width : undefined = 1

.. container:: methodparmtable

   Number of input channels to average together, positive integer

.. container:: parameters2

   inc : undefined = 1

.. container:: methodparmtable

   Increment to next (group of) input channel(s), positive integer

.. container:: methodsection

   Example

.. container:: methodexam

   ms.fromfits("NGC5921.MS", "/usr/lib/casapy/data/demo/NGC5921.fits")
   ms.selectinitold(datadescid=0) ms.selectchannelold(3,2,5,3) This
   example selects all the data from the measurement set where the value
   in the DATA_DESC_ID column is zero. This corresponds to a particular
   spectral window and polarization setup. It then selects on frequency
   channels to produce 3 output channels, the first output channel is
   the average of channels 2,3,4,5,6 in the input, the second output
   channel is the average of channel 5,6,7,8,9 and the third is the
   average of channels 8,9,10,11,12.

.. container:: param

   function **selectpolarizationold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::selectpolarization() function in
         place of ms::selectpolarizationold(). This function allows you
         to select a subset of the polarizations in the current
         measurement set. This function can also setup conversion to
         different polarization representations. You specify the
         polarizations using a string vector. Allowable strings are
         include I, Q, U, V, RR, RL, LR, LL, XX, YY, XY, YX. These
         string must be specified in upper case. If the polarizations
         match those present in the measurement set they will be
         selected directly, otherwise all polarizations are read and
         then a conversion step is done. If the conversion cannot be
         done then an error will be produced when you try to access the
         data. This function return True if the selection was
         successful, and False if not. You need to call selectinitold
         before calling this function. If you haven't then selectinitold
         will be called for you with default arguments.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         wantedpol : undefined

      .. container:: methodparmtable

         The polarizations wanted

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinitold(datadescid=0)
   ms.selectpolarizationold(["I","V"]) rec = ms.getdataold("data") This
   example selects all the data from the measurement set where the value
   in the DATA_DESC_ID column is zero. This corresponds to a particular
   spectral window and polarization setup. It then selects the I and V
   polarizations and when the getdataold function is called the
   conversion from RR, LL, LR, RL polarizations to I and V occurs.

.. container:: param

   function **getdataold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::getdata() function in place of
         ms::getdataold(). This function will read the specified items
         from the currently selected measurement set and returns them in
         fields of a record. The main difference between this and direct
         access of the table, using the table tool, is that this
         function reads data from the selected measurement set, it
         provides access to derived quantities like amplitude and
         flag_sum and it can reorder the data. The items to read are
         specified, as with the rangeold function, using a vector of
         strings. Allowable items include: amplitude,
         corrected_amplitude, model_amplitude, ratio_amplitude,
         residual_amplitude, obs_residual_amplitude, antenna1, antenna2,
         axis_info, data, corrected_data, model_data, ratio_data,
         residual_data, obs_residual_data, feed1, feed2, field_id, flag,
         flag_row, flag_sum, ha (added to axis_info), ifr_number,
         imaginary, corrected_imaginary, model_imaginary,
         ratio_imaginary, residual_imaginary, obs_residual_imaginary,
         last (added to axis_info), phase, corrected_phase, model_phase,
         ratio_phase, residual_phase, obs_residual_phase, real,
         corrected_real, ratio_real, residual_real, obs_residual_real,
         scan_number, sigma, data_desc_id, time, ut (added to
         axis_info), uvw, u, v, w, uvdist, and weight. Unrecognized
         items will result in a warning being sent to the logger.
         Duplicate items are silently ignored. The record that is
         returned contains fields that correspond to each of the
         specified items. Most fields will contain an array. The array
         may be one, two or three dimensional depending on whether the
         corresponding row in the measurement set is a scalar, one or
         two dimensional. Unless the ifraxis argument is set to True the
         length of the last axis on these arrays will correspond to the
         number of rows in the selected measurement set. If the ifraxis
         argument is set to True, the row axis is split into an
         interferometer axis and a time axis. For example a measurement
         set with 90 rows, in an array with 6 telescopes (so that there
         are 15 interferometers), may have a data array of shape
         [4,32,90] if ifraxis is False or [4,32,15,6], if ifraxis is
         True (assuming there are 4 correlations and 32 channels). If
         there are missing rows as will happen if not all
         interferometers where used for all time-slots then a default
         value will be inserted. This splitting of the row axis may not
         happen for items where there is only a single value per row.
         For some items the returned vector will contain only as many
         values as there are interferometers and it is implicit that the
         same value should be used for all time slots. The antenna1,
         antenna2, feed1, feed2, and ifr_number items fall in this
         category. For other items the returned vector will have as many
         values as there are time slots and it is implicit that the same
         value should be used for all interefometers. The field_id,
         scan_number, data_desc_id, and time items fall into this
         category. The axis_info item provides data labelling
         information. It returns a record with the following fields:
         corr_axis, freq_axis, ifr_axis and time_axis. The latter two
         fields are not present if ifr_axis is set to False. The
         corr_axis field contains a string vector with elements like
         'RR' or 'XY' that indicates which polarizations where
         correlated together to produce the data. The length of this
         vector will always be the same as the length of the first axis
         of the data array. The freq_axis field contains a record with
         two fields, chan_freq and resolution. Each of these fields
         contains vectors which indicate the centre frequency and
         spectral resolution (FWHM) of each channel. The length of these
         vectors will be the same as the length of the second axis in
         the data. The ifr_axis field contains fields: ifr_number,
         ifr_name, ifr_shortname, and baseline. The ifr_number is the
         same as returned by the ifr_item, the ifr_name and
         ifr_shortname are string vecors containing descriptions of the
         interferometer and the baseline is the Euclidian distance, in
         meters between the two antennas. All of these vectors have a
         length equal to the number of interferometers in the selected
         measurement set ie., to the length of the third axis in the
         data when ifraxis is True. The time_axis field contains the MJD
         seconds field and optionally the HA, UT, and LAST fields. To
         include the optional fields you need to add the ha, last or ut
         strings to the list of requested items. All the fields in the
         time_axis record contain vectors that indicate the time at the
         midpoint of the observation and are in seconds. The MJD seconds
         field is since 0 hours on the day having a modified julian day
         number of zero and the rest are since midnight prior to the
         start of the observation. An optional gap size can be specified
         to visually separate groups of interferometers with the same
         antenna1 index (handy for identifying antennas in an
         interferometer vs time display). The default is no gap. An
         optional increment can be specified to return data from every
         row matching the increment only. When the average flag is set,
         the data will be averaged over the time axis if the ifraxis is
         True or the row axis i.e., different interferometers and times
         may be averaged together. In the latter case, some of the
         coordinate information, like antenna_id, will no longer make
         sense. When all data to be averaged is unflagged, the result is
         the averaged value and the corresponding flag is False. When
         all data is flagged, the result is set to zero and the
         corresponding flag is True. When data to be averaged is mixed
         (unflagged and flagged), only the unflagged values are averaged
         and the flag is set to False. You need to call selectinitold
         before calling this function. If you haven't then selectinitold
         will be called for you with default arguments. Items prefixed
         with corrected, model, residual or obs_residual are not
         available unless your measurement set has been processed either
         with the imager or calibrator tools.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Item names

.. container:: parameters2

   ifraxis : undefined = false

.. container:: methodparmtable

   Create interferometer axis if True

.. container:: parameters2

   ifraxisgap : undefined = 0

.. container:: methodparmtable

   Gap size on ifr axis when antenna1 changes

.. container:: parameters2

   increment : undefined = 1

.. container:: methodparmtable

   Row increment for data access

.. container:: parameters2

   average : undefined = false

.. container:: methodparmtable

   Average the data in time or over rows

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS") ms.selectinitold(datadescid=0) # Get amplitude
   and MJDseconds d =
   ms.getdataold(["amplitude","axis_info"],ifraxis=True) tstart =
   min(d["axis_info"]["time_axis"]["MJDseconds"]) tstop =
   max(d["axis_info"]["time_axis"]["MJDseconds"]) maxamp =
   max(max(d["amplitude"][:,0,0,0]),max(d["amplitude"][0,:,0,0]),
   max(d["amplitude"][0,0,:,0]),max(d["amplitude"][0,0,0,:])) print "MJD
   start time (seconds) =", tstart # MJD start time (seconds) =
   4121629400.0 print "MJD stop time (seconds) =", tstop # MJD stop time
   (seconds) = 4121642670.0 # MJDseconds Correlation amplitude print
   "Maximum correlation amplitude =", maxamp # Maximum correlation
   amplitude = 33.5794372559 chan = 0 corr = 0 freqGHz =
   d["axis_info"]["freq_axis"]["chan_freq"][chan]/1.0E9 baselineStr =
   d["axis_info"]["ifr_axis"]["ifr_name"][corr] corrStr =
   d["axis_info"]["corr_axis"][corr] tcoord =
   d["axis_info"]["time_axis"]["MJDseconds"] acoord =
   d["amplitude"][0,0,0,:] print "Frequency", freqGHz, "GHz",
   "Baseline", baselineStr, "(", corrStr, ")" print "MJDseconds",
   "Correlation amplitude" for i in range(len(tcoord)): print tcoord[i],
   acoord[i] # # Frequency [ 8.085] GHz Baseline 1-2 ( RR ) # MJDseconds
   Correlation amplitude # 4121629400.0 29.2170944214 # 4121629410.0
   29.1688995361 # 4121629420.0 29.2497825623 # 4121629430.0
   29.2029647827 # 4121629440.0 29.166015625 # 4121629450.0
   29.2417526245 # 4121629460.0 29.2867794037 # 4121638270.0 0.0 #
   4121638280.0 29.4539775848 # 4121638290.0 29.472661972 # 4121638300.0
   29.4424362183 # 4121638310.0 29.4234466553 # 4121638320.0
   29.4018745422 # 4121638330.0 29.3326053619 # 4121638340.0
   29.3575496674 # 4121642600.0 31.1411132812 # 4121642610.0
   31.0726108551 # 4121642620.0 31.1242599487 # 4121642630.0
   31.0505466461 # 4121642640.0 31.0448284149 # 4121642650.0
   30.9974422455 # 4121642660.0 31.0648326874 # 4121642670.0
   31.0638961792 This example selects all the data from the measurement
   set where the value in the DATA_DESC_ID column is zero. This
   corresponds to a particular spectral window and polarization setup.
   It then gets the correlated amplitude, and the axis information from
   this selected measurement set. This is returned in the casapy
   variable d. The remainder of the example prints a table of 'hour
   angle' and corresponding 'correlated amplitude' for the first
   channel, correlation and baseline.

.. container:: param

   function **putdataold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::putdata() function in place of
         ms::putdataold(). This function allows you to write values from
         casapy variables back into the measurement set table. The main
         difference between this and directly accessing the table using
         the table tool is that this function writes data to the
         selected measurement set. Unlike the getdataold function you
         can only put items that correspond to actual table columns. You
         cannot change the data shape either so that the number of
         correlations, channels and rows (or intereferometers/time
         slots) must match the values in the selected measurement set.
         If the values were obtained using the getdataold function with
         ifraxis argument set to True, then any default values added to
         fill in missing intereferometer/timeslots pairs will be ignored
         when writing the modified values back using this function.
         Allowable items include: data, corrected_data, model_data,
         flag, flag_row, sigma, and weight. The measurement set has to
         be opened for read/write access to be able to use this
         function. You need to call selectinitold before calling this
         function. If you haven't then selectinitold will be called for
         you with default arguments. Items prefixed with corrected,
         model, residual or obs_residual are not available unless your
         measurement set has been processed either with the imager or
         calibrator tools.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         items : undefined

      .. container:: methodparmtable

         Record with items and their new values

.. container:: methodsection

   Example

.. container:: methodexam

   ms.open("3C273XC1.MS", nomodify=False) ms.selectinitold(datadescid=0)
   rec = ms.getdataold(["weight","data"]) rec['weight'][:,:] = 1 import
   Numeric meanrec = Numeric.average(rec['data'],axis=None) print "Mean
   data value = ", meanrec rec['data'][:,:,:] -= meanrec
   ms.putdataold(rec) This example selects all the data from the
   measurement set where the value in the DATA_DESC_ID column is zero.
   This corresponds to a particular spectral window and polarization
   setup. Note that the measurement set was opened for writing as well
   as reading. The third line reads all the weights and the data into
   the variable rec. The weights are set to one. The more obscure syntax
   is used as typing rec['weight'] = 1 will not preserve the shape of
   the weight array. The data then has its mean subtracted from it. The
   average function is defined in Numeric module. Finally the data is
   written back into the measurement set table. (NOTE: normally one
   should not modify the raw data column. Such adjustments are more
   appropriate for the corrected_data column, if it exists.)

.. container:: param

   function **iterinitold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iterinit() function in place of
         ms::iterinitold(). Specify the columns to iterate over and the
         time interval to use for the TIME column iteration. The columns
         are specified by their MS column name and must contain scalar
         values. Note that the following columns are always added to the
         specified columns: array_id, field_id, data_desc_id and time.
         This is so that the iterator can keep track of the coordinates
         associated with the data (field direction, frequency, etc.). If
         you want to sort on these columns last instead of first, you
         need to include them in the columns specified. If you don't
         want to sort on these columns at all, you can set
         adddefaultsortcolumns to False. You may want to use iteration
         for a large dataset. After calling iterinitold, you must call
         iteroriginold before attempting to retrieve data with
         getdataold. You need to call selectinitold before calling this.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         columns : undefined

      .. container:: methodparmtable

         Vector of column names (case sensitive).

.. container:: parameters2

   interval : undefined = 0.0

.. container:: methodparmtable

   Time interval in seconds (greater than 0), to group together in
   iteration

.. container:: parameters2

   maxrows : undefined = 0

.. container:: methodparmtable

   Max number of rows (greater than 0) to return in iteration

.. container:: parameters2

   adddefaultsortcolumns : undefined = true

.. container:: methodparmtable

   Add the default sort columns

.. container:: methodsection

   Example

.. container:: methodexam

   See the example for the iterendold function.

.. container:: param

   function **iteroriginold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iterorigin() function in place
         of ms::iteroriginold(). Set or reset the iterator to the start
         of the currently specified iteration. You need to call this
         after iterinitold, before attempting to retrieve data with
         getdataold. You may also use iteroriginold to set the iteration
         back to the start before you reach the end of the data.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         See the example for the iterendold function.

.. container:: param

   function **iternextold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iternext() function in place of
         ms::iternextold(). This sets the currently selected table (as
         accessed with getdataold) to the next iteration. If there is no
         more data, the function returns False and the selection is
         reset to that before the iteration started. You need to call
         iterinitold and iteroriginold before calling this.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         See the example for the iterendold function.

.. container:: param

   function **iterendold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::iterend() function in place of
         ms::iterendold(). This sets the currently selected table (as
         accessed with getdataold) to the table that was selected before
         iteration started. Use this to end the iteration prematurely.
         There is no need to call this if you continue iterating until
         iternextold returns False. See the example below.

      .. container:: methodsection

         Parameters : None

      .. container:: methodsection

         Example

      .. container:: methodexam

         ms.open("3C273XC1.MS") ms.selectinitold(datadescid=0)
         ms.iterinitold(["ANTENNA1","ANTENNA2","TIME"],60.0)
         ms.iteroriginold() rec=ms.getdataold(["u","v","data"])
         ms.iternextold() ms.iterendold() We open the MS, select an
         array and spectral window and then specify an iteration over
         interferometer and time, with a 60s time interval. We then set
         the iterator to the start of the data and get out some data.
         Finally we advance the iterator to the next lot of data and
         then end the iteration.

.. container:: param

   function **continuumsubold**

   .. container:: collcontent

      .. container:: methoddesc

         DEPRECATED: Please use the ms::continuumsub() function in place
         of ms::continuumsubold(). This function provides a means of
         continuum determination and subtraction by fitting a polynomial
         of desired order to a subset of channels in each time-averaged
         uv spectrum. The fit is used to model the continuum in all
         channels (not just those used in the fit), for subtraction, if
         desired. Use the fitspw parameter to limit the spectral windows
         processed and the range of channels used to estimate the
         continuum in each (avoid channels containing spectral lines).
         The default solution interval 'int' will result in
         per-integration continuum fits for each baseline. The mode
         parameter indicates how the continuum model (the result of the
         fit) should be used: 'subtract' will store the continuum model
         in the MODEL_DATA column and subtract it from the
         CORRECTED_DATA column; 'replace' will replace the
         CORRECTED_DATA column with the continuum model (useful if you
         want to image the continuum model result); and 'model' will
         only store the continuum model in the MODEL_DATA column (the
         CORRECTED_DATA is unaffected). It is important to open the
         dataset with nomodify=False so that changes will be allowed
         (see example below). For now, the only way to recover the
         un-subtracted CORRECTED_DATA column is to use
         calibrater.correct() again. Note that the MODEL_DATA and
         CORRECTED_DATA columns must be present for continuumsubold to
         work correctly. The function will warn the user if they are not
         present, and abort. To add these scratch columns, close the ms
         tool, then start a calibrater or an imager tool, which will add
         the scratch columns. Then restart the ms tool, and try
         continuumsubold again.

      .. container:: methodsection

         Parameters

      .. container:: parameters2

         field : any

      .. container:: methodparmtable

         Select fields to fit

.. container:: parameters2

   fitspw : any

.. container:: methodparmtable

   Spectral windows/channels to use for fitting the continuum; default
   all spectral windows in all channels

.. container:: parameters2

   spw : any

.. container:: methodparmtable

   Select spectral windows and channels from which to subtract a
   continuum estimate; default: all channels in all spectral windows for
   which the continuum was estimated

.. container:: parameters2

   solint : any = int

.. container:: methodparmtable

   Continuum fit timescale (units optional)

.. container:: parameters2

   fitorder : undefined = 0

.. container:: methodparmtable

   Polynomial order for fit

.. container:: parameters2

   mode : undefined = subtract

.. container:: methodparmtable

   Desired use of fit model (see below)

.. container:: methodsection

   Example

.. container:: methodexam

   ms.fromfits('ngc5921.ms','/aips++/data/demo/NGC5921.fits') ms.close()
   cb.open('ngc5921.ms') # add MODEL_DATA, CORRECTED_DATA columns
   cb.close() ms.open('ngc5921.ms',nomodify=False); # writable!
   ms.continuumsubold(field=2,fitspw='0:5~9;50~59',solint=0.0,
   fitorder=1,mode='subtract') ms.done() This example will fit a linear
   continuum to channels 5-9 and 50-59 in spectral window 0 in each
   scan-averaged spectrum for field 2, and store the result in the
   MODEL_DATA column and subtract it from the CORRECTED_DATA column.

.. container:: section
   :name: viewlet-below-content-body
