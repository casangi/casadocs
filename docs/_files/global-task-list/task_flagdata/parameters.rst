Parameters
==========

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Name of input visibility file Default: none Example:
            vis='ngc5921.ms'

Example

.. container:: param

   .. container:: parameters2

      mode : string = manual

   Flagging mode Default: 'manual' Options: 'list', 'manual', 'clip',
   'quack', 'shadow', 'elevation', 'tfcrop', 'rflag', 'antint',
   'extend', 'unflag', 'summary' \* 'list': Flag according to the data
   selection and flag commands specified in the input list. The input
   list may come from a text file, a list of text files or from a Python
   list of strings. Each input line may contain data selection
   parameters and any parameter specific to the mode given in the line.
   Default values will be used for the parameters that are not present
   in the line. Each line will be taken as a command to the task. If
   data is pre-selected using any of the selection parameters, then
   flagging will apply only to that subset of the MS. For optimization
   and whenever possible, the task will create a union of the data
   selection parameters present in the list and select only that portion
   of the MS. NOTE1: the flag commands will be applied only when
   action='apply'. If action='calculate' the flags will be calculated,
   but not applied. This is useful if display is set to something other
   than 'none'. If action='' or 'none', the flag commands will not be
   applied either. An empty action is useful only to save the parameters
   of the list to a file or to the FLAG_CMD sub-table. NOTE2: In list
   mode the parameter quackincrement=True is not supported as part of
   any quack flag command, unless it is the first command of the list.
   See more about this in the quack mode section of this help. \*
   'manual': Flag according to the data selection specified. This is the
   default mode \* 'clip': Clip data according to values of the
   following subparameters. The polarization expression is given by the
   correlation parameter. For calibration tables, the solutions are also
   given by the correlation parameter. \* 'quack': Option to remove
   specified part of scan beginning/end. \* 'shadow': Option to flag
   data of shadowed antennas. This mode is not available for cal tables.
   All antennas in the antenna-subtable of the MS (and the corresponding
   diameters) will be considered for shadow-flag calculations. For a
   given timestep, an antenna is flagged if any of its baselines
   (projected onto the uv-plane) is shorter than radius_1 + radius_2 -
   tolerance. The value of 'w' is used to determine which antenna is
   behind the other. The phase-reference center is used for
   antenna-pointing direction. \* 'elevation': Option to flag based on
   antenna elevation. This mode is not available for cal tables. \*
   'tfcrop': Flag using the TFCrop autoflag algorithm. For each field,
   spw, timerange (specified by ntime), and baseline, (1) Average
   visibility amplitudes along time dimension to form an average
   spectrum (2) Calculate a robust piece-wise polynomial fit for the
   band-shape at the base of RFI spikes. Calculate 'stddev' of (data -
   fit). (3) Flag points deviating from the fit by more than N-stddev
   (4) Repeat (1-3) along the other dimension. This algorithm is
   designed to operate on un-calibrated data (step (2)), as well as
   calibrated data. It is recommended to extend the flags after running
   this algorithm. See the sub-parameter extendflags below. \* 'rflag':
   Detect outliers based on the RFlag algorithm (ref. E.Greisen, AIPS,
   2011). The polarization expression is given by the correlation
   parameter. Iterate through the data in chunks of time. For each
   chunk, calculate local statistics, and apply flags based on user
   supplied (or auto-calculated) thresholds. Step 1 : Time analysis (for
   each channel) -- calculate local rms of real and imag visibilities,
   within a sliding time window -- calculate the median rms across time
   windows, deviations of local rms from this median, and the median
   deviation -- flag if local rms is larger than timedevscale x
   (medianRMS + medianDev) Step 2 : Spectral analysis (for each time) --
   calculate avg of real and imag visibilities and their rms across
   channels -- calculate the deviation of each channel from this avg,
   and the median-deviation -- flag if deviation is larger than
   freqdevscale x medianDev It is recommended to extend the flags after
   running this algorithm. See the sub-parameter extendflags below. Note
   that by default the flag implementation in CASA is able to calculate
   the thresholds and apply them on-the-fly (OTF). There is a
   significant performancegain with this approach, as the visibilities
   don't have to be read twice,and therefore is highly recommended.
   Otherwise it is possible toreproduce the AIPS usage pattern by doing
   a first run with 'calculate' mode and a second run with 'apply' mode.
   The advantage of this approach is that the thresholdsare calculated
   using the data from all scans, instead of calculating them for one
   scan only. For more information and examples of 'rflag', see the task
   pages of rflag in CASA Docs (https://casa.nrao.edu/casadocs/) \*
   'antint': Flag integrations if all baselines to a specified antenna
   are flagged This mode flag all integrations in which a specified
   antenna is flagged. This mode operates for an spectral window. It
   flags any integration in which all baselines to a specified antenna
   are flagged, but only if this condition is satisfied in a fraction of
   channels within the spectral window of interest greater than a
   nominated fraction. For simplicity, it assumes that all polarization
   products must be unflagged for a baseline to be deemed unflagged. The
   antint mode implements the flagging approach introduced in
   'antintflag' (https://doi.org/10.5281/zenodo.163546) The motivating
   application for introducing this mode is removal of data that will
   otherwise lead to changes in reference antenna during gain
   calibration, which will in turn lead to corrupted polarization. \*
   'extend': Extend and/or grow flags beyond what the basic algorithms
   detect. This mode will extend the accumulated flags available in the
   MS, regardless of which algorithm created them. It is recommended
   that any autoflag (tfcrop, rflag) algorithm be followed up by a flag
   extension. Extensions will apply only within the selected data,
   according to the settings of extendpols,growtime,growfreq,growaround,
   flagneartime,flagnearfreq. Note : Runtime summary counts in the
   logger can sometimes report larger flag percentages than what is
   actually flagged. This is because extensions onto already-flagged
   data-points are counted as new flags. An accurate flag count can be
   obtained via the summary mode. \* 'unflag': Unflag according to the
   data selection specified. \* 'summary': List the number of rows and
   flagged data points for the MS's meta-data. The resulting summary
   will be returned as a Python dictionary.

Allowed Value(s)

list manual manualflag clip shadow quack elevation tfcrop rflag antint
extend summary unflag

Example

.. container:: param

   .. container:: parameters2

      autocorr : bool = False

   Flag only the auto-correlations? Subparameter of mode='manual'
   Default: False Options: False|True NOTE: this parameter is only
   active when set to True. If set to False it does NOT mean "do not
   flag auto-correlations". When set to True, it will only flag data
   from a processor of type CORRELATOR.

Example

.. container:: param

   .. container:: parameters2

      inpfile : string stringArray

   Input ASCII file, list of files or Python list of strings with flag
   commands. Subparameter of mode='list' Default: '' Options: [] with
   flag commands or [] with filenames or '' with a filename. The parser
   will be strict and accept only valid flagdata parameters in the list.
   The parser evaluates the commands in the list and considers only
   existing Python types.It will check each parameter name and type and
   exit with an error if any of them is wrong. NOTE: There should be no
   whitespace between KEY=VALUE since the parser first breaks command
   lines on whitespace, then on "=". Use only one whitespace to separate
   the parameters (no commas).

Example

.. container:: param

   .. container:: parameters2

      reason : string stringArray = any

   Select flag commands based on REASON(s) Subparameter of mode='list'
   Default: 'any' (all flags regardless of reason) Can be a string, or
   list of strings Examples: reason='FOCUS_ERROR'
   reason=['FOCUS_ERROR','SUBREFLECTOR_ERROR'] If inpfile is a list of
   files, the reasons given in this parameter will apply to all the
   files. NOTE: what is within the string is literally matched, e.g.
   reason='' matches only blank reasons, and reason =
   'FOCUS_ERROR,SUBREFLECTOR_ERROR' matches this compound reason string
   only.

Example

.. container:: param

   .. container:: parameters2

      tbuff : double doubleArray = 0.0

   A time buffer or list of time buffers to pad the timerange parameters
   in flag commands. Subparameter of mode='list' Default: 0.0 (it will
   not apply any time padding) When a list of 2 time buffers is given,
   it will subtract the first value from the lower time and the second
   value will be added to the upper time in the range. The 2 time buffer
   values can be different, allowing to have an irregular time buffer
   padding to time ranges. If the list contains only one time buffer, it
   will use it to subtract from t0 and add to t1. If more than one list
   of input files is given, tbuff will apply to all of the flag commands
   that have timerange parameters in the files. Each tbuff value should
   be a Float number given in seconds. Examples: tbuff=[0.5, 0.8]
   inpfile=['online.txt','userflags.txt'] The timeranges in the
   online.txt file are first converted to seconds. Then, 0.5 is
   subtracted from t0 and 0.8 is added to t1, where t0 and t1 are the
   two intervals given in timerange. Similarly, tbuff will be applied to
   any timerange in userflags.txt. IMPORTANT: This parameter assumes
   that timerange = t0 ~ t1, therefore it will not work if only t0 or t1
   is given. NOTE: The most common use-case for tbuff is to apply the
   online flags that are created by importasdm when savecmds=True. The
   value of a regular time buffer should be tbuff=0.5*max(integration
   time).

Example

.. container:: param

   .. container:: parameters2

      spw : string stringArray

   Select spectral window/channels Default: '' (all spectral windows and
   channels) Examples: spw='0~2,4'; spectral windows 0,1,2,4 (all
   channels) spw='<2'; spectral windows less than 2 (i.e. 0,1)
   spw='0:5~61'; spw 0, channels 5 to 61 spw='0,10,3:3~45'; spw 0,10 all
   channels, spw 3 - chans 3 to 45. spw='0~2:2~6'; spw 0,1,2 with
   channels 2 through 6 in each. spw = '*:3~64' channels 3 through 64
   for all sp id's spw = ' :3~64' will NOT work. NOTE: For modes clip,
   tfcrop and rflag, channel-ranges can be excluded from flagging by
   leaving them out of the selection range. This is a way to protect
   known spectral-lines from being flagged by the autoflag algorithms.
   For example, if spectral-lines fall in channels 6~9, set the
   selection range to spw='0:0~5;10~63'.

Example

.. container:: param

   .. container:: parameters2

      field : string stringArray

   Select field using field id(s) or field name(s) Default: '' (all
   fields) Use 'go listobs' to obtain the list id's or names. If field
   string is a non-negative integer, it is assumed a field index,
   otherwise, it is assumed a field name. Examples: field='0~2'; field
   ids 0,1,2 field='0,4,5~7'; field ids 0,4,5,6,7 field='3C286,3C295';
   field named 3C286 and 3C295 field = '3,4C*'; field id 3, all names
   starting with 4C

Example

.. container:: param

   .. container:: parameters2

      antenna : string stringArray

   Select data based on antenna/baseline Subparameter of selectdata=True
   Default: '' (all) If antenna string is a non-negative integer, it is
   assumed an antenna index, otherwise, it is assumed as an antenna name
   Examples: antenna='5&6'; baseline between antenna index 5 and index
   6. antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
   antenna='5&6;7&8'; baselines with indices 5-6 and 7-8 antenna='5';
   all baselines with antenna index 5 antenna='05'; all baselines with
   antenna number 05 (VLA old name) antenna='5,6,10'; all baselines with
   antennas 5,6,10 index numbers NOTE: for some antenna-based
   calibration tables, selecting baselines with the & syntax do not
   apply.

Example

.. container:: param

   .. container:: parameters2

      uvrange : string stringArray

   Select data by baseline length. Default = '' (all) Examples:
   uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
   uvrange='>4klambda';uvranges greater than 4 kilo-lambda
   uvrange='0~1000km'; uvrange in kilometers NOTE: uvrange selection is
   not supported for cal tables.

Example

.. container:: param

   .. container:: parameters2

      timerange : string stringArray

   Select data based on time range Subparameter of selectdata=True
   Default = '' (all) Examples: timerange =
   'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss' (Note: if YYYY/MM/DD is
   missing date defaults to first day in data set.)
   timerange='09:14:0~09:54:0' picks 40 min on first day timerange=
   '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
   timerange='09:44:00' pick data within one integration of time
   timerange='>10:24:00' data after this time

Example

.. container:: param

   .. container:: parameters2

      correlation : string stringArray

   Select data based on correlation Default: '' ==> all Options: Any of
   'ABS', 'ARG', 'REAL', 'IMAG', 'NORM' followed by any of 'ALL', 'I',
   'XX', 'YY', 'RR', 'LL', 'WVR' ('WVR' = water vapour radiometer of
   ALMA data). Example: correlation="XX,YY". For modes clip, tfcrop or
   rflag, the default means ABS_ALL. If the input is cal table that does
   not contain a complex data column, the default will fall back to
   REAL_ALL. For calibration tables, the solutions are: 'Sol1', 'Sol2',
   Sol3, Sol4. NOTE: correlation selection is not supported for modes
   other than clip, tfcrop or rflag in cal tables.

Example

.. container:: param

   .. container:: parameters2

      scan : string stringArray

   Scan number range Subparameter of selectdata=True Default: '' = all

Example

.. container:: param

   .. container:: parameters2

      intent : string stringArray

   Select observing intent Default: '' (no selection by intent) Example:
   intent='*BANDPASS*' (selects data labelled with BANDPASS intent)
   NOTE: intent selection is not supported for cal tables.

Example

.. container:: param

   .. container:: parameters2

      array : string stringArray

   Selection based on the antenna array Default: '' (all) NOTE: array
   selection is not supported for cal tables.

Example

.. container:: param

   .. container:: parameters2

      observation : string int

   Select by observation ID(s) Subparameter of selectdata=True Default:
   '' = all Example: observation='0~2,4'

Example

.. container:: param

   .. container:: parameters2

      feed : string stringArray

   Selection based on the feed: Not yet implemented

Example

.. container:: param

   .. container:: parameters2

      clipminmax : doubleArray

   Range to use for clipping Subparameter of mode='clip' Default: [] (it
   will flag only NaN and Infs) It will always flag the NaN/Inf data,
   even when a range is specified. Example: [0.0,1.5]

Example

.. container:: param

   .. container:: parameters2

      datacolumn : string stringArray = DATA

   Data column to image (data or observed, corrected) Subparameter of
   mode='clip|tfcrop|rflag' Default:'corrected' Options: data,
   corrected, model, weight, etc. If 'corrected' does not exist, it will
   use 'data' instead

Example

.. container:: param

   .. container:: parameters2

      clipoutside : bool boolArray = True

   Clip outside the range? Subparameter of mode='clip' Default: True
   Options: True|False

Example

.. container:: param

   .. container:: parameters2

      channelavg : bool boolArray = False

   Pre-average data across channels before analyzing visibilities for
   flagging Subparameter of mode='clip|tfcrop|rflag' Default: False
   Options: False|True Pre-average data across channels before analyzing
   visibilities for flagging. Partially flagged data is not be included
   in the average unless all data contributing to a given output channel
   is flagged. If present, WEIGHT_SPECTRUM / SIGMA_SPECTRUM are used to
   compute a weighted average (WEIGHT_SPECTRUM for CORRECTED_DATA and
   SIGMA_SPECTRUM for DATA). NOTE 1: Pre-average across channels is not
   supported in list mode. NOTE 2: Pre-average across channels is not
   supported for calibration tables

Example

.. container:: param

   .. container:: parameters2

      chanbin : int intArray = 1

   Bin width for channel average in number of input channels
   Subparameter of mode='clip|tfcrop|rflag' Default: 1 Bin width for
   channel average in number of input channels. If a list is given, each
   bin applies to one of the selected SPWs. When chanbin is set to 1 all
   input channels are used considered for the average to produce a
   single output channel, this behaviour aims to be preserve backwards
   compatibility with the previous pre-averaging feature of clip mode.

Example

.. container:: param

   .. container:: parameters2

      timeavg : bool boolArray = False

   Pre-average data across time before analyzing visibilities for
   flagging. Subparameter of mode='clip|tfcrop|rflag' Default: False
   Options: False|True Pre-average data across time before analyzing
   visibilities for flagging. Partially flagged data is not be included
   in the average unless all data contributing to a given output channel
   is flagged. If present, WEIGHT_SPECTRUM / SIGMA_SPECTRUM are used to
   compute a weighted average (WEIGHT_SPECTRUM for CORRECTED_DATA and
   SIGMA_SPECTRUM for DATA). Otherwise WEIGHT/SIGMA are used to average
   together data from different integrations. NOTE 1: Pre-average across
   time is not supported in list mode. NOTE 2: Pre-average across time
   is not supported for calibration tables

Example

.. container:: param

   .. container:: parameters2

      timebin : string = 0s

   Bin width for time average in seconds Subparameter of
   mode='clip|tfcrop|rflag' Default: '0s'

Example

.. container:: param

   .. container:: parameters2

      clipzeros : bool = False

   Clip zero-value data Subparameter of mode='clip' Default: False
   Options: False|True

Example

.. container:: param

   .. container:: parameters2

      quackinterval : double doubleArray int intArray = 1.0

   Time in seconds from scan beginning or end to flag. Subparameter of
   mode='quack' Default: 0.0 Note: Make time slightly smaller than the
   desired time.

Example

.. container:: param

   .. container:: parameters2

      quackmode : string stringArray = beg

   Quack mode flags the region of the scan given by one of the options
   below using the time set at quackinterval. Subparameter of
   mode='quack' Default: 'beg' Options: 'beg' : flag an interval at the
   beginning of scan 'endb': flag an interval at the end of scan 'tail':
   flag all but an interval at the beginning of scan 'end' : flag all
   but an interval at end of scan Visual representation of quack mode
   flagging one scan with 1s duration. The following diagram shows what
   is flagged for each quack mode when quackinterval is set to 0.25s.
   The flagged part is represented by crosses (+++++++++) scan with 1s
   duration -------------------------------------------- beg
   +++++++++++--------------------------------- endb
   ---------------------------------+++++++++++ tail
   -----------+++++++++++++++++++++++++++++++++ end
   +++++++++++++++++++++++++++++++++-----------

Example

.. container:: param

   .. container:: parameters2

      quackincrement : bool boolArray = False

   Increment quack flagging in time taking into account flagged data or
   not. Subparameter of mode='quack' Default: False Options: False|True
   False: the quack interval is counted from the scan boundaries, as
   determined by the quackmode parameter, regardless of if data has been
   flagged or not. True: the quack interval is counted from the first
   unflagged data in the scan. NOTE: on adding quack to a command in
   'list' mode: quackincrement = True works based on the state of prior
   flagging, and unless it is the first item in the list the agent doing
   the quacking in list mode doesn't know about the state of prior
   flags. In this case, the command with quackincrement=True will be
   ignored and the task will issue a WARNING.

Example

.. container:: param

   .. container:: parameters2

      tolerance : double = 0.0

   Amount of shadowing allowed (or tolerated), in meters. Subparameter
   of mode='shadow' Default: 0.0 A positive number allows antennas to
   overlap in projection. A negative number forces antennas apart in
   projection. Zero implies a distance of radius_1+radius_2 between
   antenna centers.

Example

.. container:: param

   .. container:: parameters2

      addantenna : string record

   File name or dictionary with additional antenna names, positions and
   diameters Subparameter of mode='shadow' Default: '' It can be either
   a file name with additional antenna names, positions and diameters,
   or a Python dictionary with the same information. You can use the
   flaghelper functions to create the dictionary from a file. To create
   a dictionary inside casapy. > import flaghelper as fh > antdic =
   fh.readAntennaList(antfile) Where antfile is a text file in disk that
   contains information such as: name=VLA01 diameter=25.0
   position=[-1601144.96146691, -5041998.01971858, 3554864.76811967]
   name=VLA02 diameter=25.0 position=[-1601105.7664601889,
   -5042022.3917835914, 3554847.245159178]

Example

.. container:: param

   .. container:: parameters2

      lowerlimit : double = 0.0

   Lower limiting elevation (in degrees) Subparameter of
   mode='elevation' Default: 0.0 Lower limiting elevation in degrees.
   Data coming from a baseline where one or both antennas were pointing
   at a strictly lower elevation (as function of time), will be flagged.

Example

.. container:: param

   .. container:: parameters2

      upperlimit : double = 90.0

   Upper limiting elevation (in degrees) Subparameter of
   mode='elevation' Default: 90.0 Upper limiting elevation in degrees.
   Data coming from a baseline where one or both antennas were pointing
   at a strictly higher elevation (as function of time), will be
   flagged.

Example

.. container:: param

   .. container:: parameters2

      ntime : double string = scan

   Timerange (in seconds or minutes) over which to buffer data before
   running the algorithm. Subparameter of mode='tfcrop|rflag|extend'
   Default: 'scan' Options: 'scan' or any other float value or string
   containing the units. The dataset will be iterated through in
   time-chunks defined here. Example: ntime='1.5min'; 1.2 (taken in
   seconds) WARNING: if ntime='scan' and combinescans=True, all the
   scans will be loaded at once, thus requesting a lot of memory
   depending on the available spws.

Example

.. container:: param

   .. container:: parameters2

      combinescans : bool = False

   Accumulate data across scans depending on the value of ntime.
   Subparameter of mode='tfcrop|rflag|extend' Default: False Options:
   False|True This parameter should be set to True only when ntime is
   specified as a time-interval (not 'scan'). When set to True, it will
   remove SCAN from the sorting columns, therefore it will only
   accumulate across scans if ntime is not set to 'scan'.

Example

.. container:: param

   .. container:: parameters2

      timecutoff : double = 4.0

   Flagging thresholds in units of deviation from the fit Subparameter
   of mode='tfcrop' Default: 4.0 Flag all data-points further than
   N-stddev from the fit. This threshold catches time-varying RFI spikes
   (narrow and broad-band), but will not catch RFI that is persistent in
   time. Flagging is done in upto 5 iterations. The stddev calculation
   is adaptive and converges to a value that reflects only the data and
   no RFI. At each iteration, the same relative threshold is applied to
   detect flags. (Step (3) of the algorithm).

Example

.. container:: param

   .. container:: parameters2

      freqcutoff : double = 3.0

   Flag threshold in frequency. Subparameter of mode='tfcrop' Default:
   3.0 Flag all data-points further than N-stddev from the fit. Same as
   timecutoff, but along the frequency-dimension. This threshold catches
   narrow-band RFI that may or may not be persistent in time.

Example

.. container:: param

   .. container:: parameters2

      timefit : string = line

   Fitting function for the time direction (poly/line) Subparameter of
   mode='tfcrop' Default: 'line' Options: line|poly 'line': fit is a
   robust straight-line fit across the entire timerange (defined by
   'ntime'). 'poly': fit is a robust piece-wise polynomial fit across
   the timerange. NOTE: A robust fit is computed in upto 5 iterations.
   At each iteration, the stddev between the data and the fit is
   computed, values beyond N-stddev are flagged, and the fit and stddev
   are re-calculated with the remaining points. This stddev calculation
   is adaptive, and converges to a value that reflects only the data and
   no RFI. It also provides a varying set of flagging thresholds, that
   allows deep flagging only when the fit best represents the true data.
   Choose 'poly' only if the visibilities are expected to vary
   significantly over the timerange selected by 'ntime', or if there is
   a lot of strong but intermittent RFI.

Example

.. container:: param

   .. container:: parameters2

      freqfit : string = poly

   Fitting function for the frequency direction (poly/line) Subparameter
   of mode='tfcrop' Default: 'poly' Options: line|poly Same as for the
   'timefit' parameter. Choose 'line' only if you are operating on
   bandpass-corrected data, or residuals,and expect that the bandshape
   is linear. The 'poly' option works better on uncalibrated bandpasses
   with narrow-band RFI spikes.

Example

.. container:: param

   .. container:: parameters2

      maxnpieces : int = 7

   Number of pieces in the polynomial-fits (for "freqfit" or "timefit" =
   "poly") Subparameter of mode='tfcrop' Default: 7 Options: 1-9 This
   parameter is used only if 'timefit' or 'freqfit' are chosen as
   'poly'. If there is significant broad-band RFI, reduce this number.
   Using too many pieces could result in the RFI being fitted in the
   'clean' bandpass. In later stages of the fit, a third-order
   polynomial is fit per piece, so for best results, please ensure that
   nchan/maxnpieces is at-least 10.

Example

.. container:: param

   .. container:: parameters2

      flagdimension : string = freqtime

   Choose the directions along which to perform flagging Subparameter of
   mode='tfcrop' Default: 'freqtime' (first flag along frequency, and
   then along time) Options: 'time', 'freq', 'timefreq', 'freqtime' For
   most cases, 'freqtime' or 'timefreq' are appropriate, and differences
   between these choices are apparant only if RFI in one dimension is
   significantly stronger than the other. The goal is to flag the
   dominant RFI first. If there are very few (less than 5) channels of
   data, then choose 'time'. Similarly for 'freq'.

Example

.. container:: param

   .. container:: parameters2

      usewindowstats : string = none

   Use sliding-window statistics to find additional flags. Subparameter
   of mode='tfcrop' Default: 'none' Options: 'none', 'sum', 'std',
   'both' NOTE: This is experimental! The 'sum' option chooses to flag a
   point, if the mean-value in a window centered on that point deviates
   from the fit by more than N-stddev/2.0. NOTE: stddev is calculated
   between the data and fit as explained in Step (2). This option is an
   attempt to catch broad-band or time-persistent RFI that the above
   polynomial fits will mistakenly fit as the clean band. It is an
   approximation to the sumThreshold method found to be effective by
   Offringa et.al (2010) for LOFAR data. The 'std' option chooses to
   flag a point, if the 'local' stddev calculated in a window centered
   on that point is larger than N-stddev/2.0. This option is an attempt
   to catch noisy RFI that is not excluded in the polynomial fits, and
   which increases the global stddev, and results in fewer flags (based
   on the N-stddev threshold).

Example

.. container:: param

   .. container:: parameters2

      halfwin : int = 1

   Half-width of sliding window to use with "usewindowstats" (1,2,3).
   Subparameter of mode='tfcrop' Default: 1 (a 3-point window size)
   Options: 1, 2, 3 NOTE: This is experimental!

Example

.. container:: param

   .. container:: parameters2

      extendflags : bool = True

   Extend flags along time, frequency and correlation. Subparameter of
   mode='tfcrop|rflag' Default: True Options: True|False NOTE: It is
   usually helpful to extend the flags along time, frequency, and
   correlation using this parameter, which will run the "extend" mode
   after "tfcrop" and extend the flags if more than 50% of the
   timeranges are already flagged, and if more than 80% of the channels
   are already flagged. It will also extend the flags to the other
   polarizations. The user may also set extendflags to False and run the
   "extend" mode in a second step within the same flagging run: Example:
   cmd=["mode='tfcrop' freqcutoff=3.0 usewindowstats='sum'
   extendflags=False", "mode='extend' extendpols=True growtime=50.0
   growaround=True"] flagdata(vis, mode='list', inpfile=cmd)

Example

.. container:: param

   .. container:: parameters2

      winsize : int = 3

   Number of timesteps in the sliding time window ( fparm(1) in AIPS )
   Subparameter of mode='rflag' Default: 3

Example

.. container:: param

   .. container:: parameters2

      timedev : undefined

   Time-series noise estimate ( noise in AIPS ) Subparameter of
   mode='rflag' Default: [] Examples: timedev = 0.5 : Use this
   noise-estimate to calculate flags. Do not recalculate. timedev = [
   [1,9,0.2], [1,10,0.5] ] : Use noise-estimate of 0.2 for field 1, spw
   9, and noise-estimate of 0.5 for field 1, spw 10. timedev = [] :
   Auto-calculate noise estimates. 'tdevfile.txt' : Auto-calculate noise
   estimates and write them into a file with the name given (any string
   will be interpreted as a file name which will be checked for
   existence).

Example

.. container:: param

   .. container:: parameters2

      freqdev : undefined

   Spectral noise estimate ( scutoff in AIPS ) Subparameter of
   mode='rflag' Default: [] This step depends on having a
   relatively-flat bandshape. Same parameter-options as 'timedev'.

Example

.. container:: param

   .. container:: parameters2

      timedevscale : double = 5.0

   Threshold scaling for timedev( fparm(9) in AIPS ). For Step 1 (time
   analysis), flag a point if local rms around it is larger than
   'timedevscale' x 'timedev' (fparm(0) in AIPS) Subparameter of
   mode='rflag' Default: 5.0 This scale parameter is only applied when
   flagging (action='apply') and displaying reports (display option). It
   is not used when the thresholds are simply calculated and saved into
   files (action='calculate', as in the two-passes usage pattern of
   AIPS)

Example

.. container:: param

   .. container:: parameters2

      freqdevscale : double = 5.0

   Threshold scaling for freqdev (fparm(10) in AIPS ). For Step 2
   (spectral analysis), flag a point if local rms around it is larger
   than 'freqdevscale' x 'freqdev' (fparm(10) in AIPS) Subparameter of
   mode='rflag' Default: 5.0 Similarly as with timedevscale,
   freqdevscale is used when applying flags and displaying reports. It
   is not used when the thresholds are simply calculated and saved into
   files (action='calculate', as in the two-passes usage pattern of
   AIPS)

Example

.. container:: param

   .. container:: parameters2

      spectralmax : double = 1E6

   Flag whole spectrum if 'freqdev' is greater than spectralmax (
   fparm(6) in AIPS ) Subparameter of mode='rflag' Default: 1E6

Example

.. container:: param

   .. container:: parameters2

      spectralmin : double = 0.0

   Flag whole spectrum if 'freqdev' is less than spectralmin ( fparm(5)
   in AIPS ) Subparameter of mode='rflag' Default: 0.0

Example

.. container:: param

   .. container:: parameters2

      antint_ref_antenna : string

   Antenna of interest. Baselines with this antenna will be checked for
   flagged channels. Subparameter of mode='antint' Note that this is not
   the same as the general 'antenna' parameter of flagdata. The
   parameter antint_ref_antenna is mandatory with the 'antint' mode and
   chooses the antenna for which the fraction of channels flagged will
   be checked.

Example

.. container:: param

   .. container:: parameters2

      minchanfrac : double = 0.6

   Minimum fraction of flagged channels required for a baseline to be
   deemed as flagged Subparameter of mode='antint' Takes values between
   0-1 (float). In this mode flagdata does the following for every point
   in time. It checks the fraction of channels flagged for any of the
   polarization products and for every baseline to the antenna of
   interest. If the fraction is higher than this 'minchanfrac' threshold
   then the data are flagged for this pont in time (this includes all
   the rows selected with the flagdata command that have that
   timestamp). This parameter will be ignored if spw specifies a
   channel.

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = False

   Print timestamps of flagged integrations to the log Subparameter of
   mode='antint' Examples: flagdata(vis, ..., spw='9',
   antint_ref_antenna='ea01') flagdata(vis, ..., spw='9',
   antint_ref_antenna='ea01', minchanfrac=0.3, verbose=True) ==> reduce
   the fraction of channels that are required to be flagged, and print
   information for every integration that is flagged.

Example

.. container:: param

   .. container:: parameters2

      extendpols : undefined = True

   Extend flags to all selected correlations Subparameter of
   mode='extend' Default: True Options: True|False For example, to
   extend flags from RR to only RL and LR, a data-selection of
   correlation='RR,LR,RL' is required along with extendpols=True.

Example

.. container:: param

   .. container:: parameters2

      growtime : double = 50.0

   For any channel, flag the entire timerange in the current 2D chunk
   (set by 'ntime') if more than X% of the timerange is already flagged.
   Subparameter of mode='extend' Default: 50.0 Options: 0.0 - 100.0 This
   option catches the low-intensity parts of time-persistent RFI.

Example

.. container:: param

   .. container:: parameters2

      growfreq : double = 50.0

   For any timestep, flag all channels in the current 2D chunk (set by
   data-selection) if more than X% of the channels are already flagged.
   Subparameter of mode='extend' Default: 50.0 Options: 0.0 - 100.0 This
   option catches broad-band RFI that is partially identified by earlier
   steps.

Example

.. container:: param

   .. container:: parameters2

      growaround : bool = False

   Flag a point based on the number of flagged points around it.
   Subparameter of mode='extend' Default: False Options: False|True For
   every un-flagged point on the 2D time/freq plane, if more than four
   surrounding points are already flagged, flag that point. This option
   catches some wings of strong RFI spikes.

Example

.. container:: param

   .. container:: parameters2

      flagneartime : bool = False

   Flag points before and after every flagged one, in the
   time-direction. Subparameter of mode='extend' Default: False Options:
   False|True NOTE: This can result in excessive flagging.

Example

.. container:: param

   .. container:: parameters2

      flagnearfreq : bool = False

   Flag points before and after every flagged one, in the
   frequency-direction Subparameter of mode='extend' Default: False
   Options: False|True NOTE: This can result in excessive flagging

Example

.. container:: param

   .. container:: parameters2

      minrel : double = 0.0

   Minimum number of flags (relative) to include in histogram
   Subparameter of mode='summary' Default: 0.0

Example

.. container:: param

   .. container:: parameters2

      maxrel : double = 1.0

   Maximum number of flags (relative) to include in histogram
   Subparameter of mode='summary' Default: 1.0

Example

.. container:: param

   .. container:: parameters2

      minabs : int = 0

   Minimum number of flags (absolute, inclusive) to include in histogram
   Subparameter of mode='summary' Default: 0

Example

.. container:: param

   .. container:: parameters2

      maxabs : int = -1

   Maximum number of flags (absolute, inclusive) to include in histogram
   Subparameter of mode='summary' Default: -1 To indicate infinity, use
   any negative number.

Example

.. container:: param

   .. container:: parameters2

      spwchan : bool = False

   List the number of flags per spw and per channel. Subparameter of
   mode='summary' Default: False Options: False|True

Example

.. container:: param

   .. container:: parameters2

      spwcorr : bool = False

   List the number of flags per spw and per correlation. Subparameter of
   mode='summary' Default: False Options: False|True

Example

.. container:: param

   .. container:: parameters2

      basecnt : bool = False

   List the number of flags per baseline Subparameter of mode='summary'
   Default: False Options: False|True

Example

.. container:: param

   .. container:: parameters2

      fieldcnt : bool = False

   Produce a separated breakdown per field Subparameter of
   mode='summary' Default: False Options: False|True

Example

.. container:: param

   .. container:: parameters2

      name : string = Summary

   Name for this summary, to be used as a key in the returned Python
   dictionary Subparameter of mode='summary' Default: 'Summary' It is
   possible to call the summary mode multiple times in list mode. When
   calling the summary mode as a command in a list, one can give
   different names to each one of them so that they can be easily pulled
   out of the summary's dictionary. In summary mode, the task returns a
   dictionary of flagging statistics. Example 1: s = flagdata(...,
   mode='summary') Then s will be a dictionary which contains s['total']
   : total number of data s['flagged'] : amount of flagged data Example
   2: Two summary commands in list mode, intercalating a manual flagging
   command. s = flagdata(..., mode='list', inpfile=["mode='summary'
   name='InitFlags'", "mode='manual' autocorr=True", "mode='summary'
   name='Autocorr'"]) The dictionary returned in 's' will contain two
   dictionaries, one for each of the two summary modes.
   s['report0']['name'] : 'InitFlags' s['report1']['name'] : 'Autocorr'

Example

.. container:: param

   .. container:: parameters2

      action : string = apply

   Action to perform in MS/cal table or in the input list of parameters.
   Default: 'apply' Options: 'none', 'apply','calculate' \* 'apply':
   Apply the flags to the MS. \* 'calculate': Only calculate the flags
   but do not write them to the MS. This is useful if used together with
   the display to analyse the results before writing to the MS. \* '':
   When set to empty, the underlying tool will not be executed and no
   flags will be produced. No data selection will be done either. This
   is useful when used together with the parameter savepars to only save
   the current parameters (or list of parameters) to the FLAG_CMD
   sub-table or to an external file.

Allowed Value(s)

apply calculate none

Example

.. container:: param

   .. container:: parameters2

      display : string

   Display data and/or end-of-MS reports at runtime. Subparameter of
   action='apply|calculate' Default: 'none' Options: 'none', 'data',
   'report', 'both' \* 'none': will not display anything. \* 'data':
   display data and flags per-chunk at run-time, within an interactive
   GUI. This option opens a GUI to show the 2D time-freq planes of the
   data with old and new flags, for all correlations per baseline. --
   The GUI allows stepping through all baselines (prev/next) in the
   current chunk (set by 'ntime'), and stepping to the next-chunk. --
   The 'flagdata' task can be quit from the GUI, in case it becomes
   obvious that the current set of parameters is just wrong. -- There is
   an option to stop the display but continue flagging. \* 'report':
   displays end-of-MS reports on the screen. \* 'both': displays data
   per chunk and end-of-MS reports on the screen

Example

.. container:: param

   .. container:: parameters2

      flagbackup : bool = True

   Automatically backup flags before the run? Default: True Options:
   True|False Flagversion names are chosen automatically, and are based
   on the mode being used.

Example

.. container:: param

   .. container:: parameters2

      savepars : bool = False

   Save the current parameters to the FLAG_CMD table of the MS or to an
   output text file? Default: False Options: False|True Note that when
   display is set to anything other than 'none', savepars will be
   disabled. This is done because in an interactive mode, the user may
   skip data which may invalidate the initial input parameters and there
   is no way to save the interactive commands. When the input is a
   calibration table it is only possible to save the parameters to a
   file.

Example

.. container:: param

   .. container:: parameters2

      cmdreason : string

   A string containing a reason to save to the FLAG_CMD table or to an
   output text file given by the outfile sub-parameter. Subparameter of
   savepars=True Default: '' (no reason will be added to output) If the
   input contains any reason, they will be replaced with this one. At
   the moment it is not possible to add more than one reason. Example:
   cmdreason='CLIP_ZEROS'

Example

.. container:: param

   .. container:: parameters2

      outfile : string

   Name of output file to save current parameters. If empty, save to
   FLAG_CMD Subparameter of savepars=True Default: '' (save the
   parameters to the FLAG_CMD table of the MS) Example:
   outfile='flags.txt' will save the parameters in a text file.

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = True

   Overwrite the existing file given in 'outfile' Default: True Options:
   True|False The default True will remove the existing file given in
   'outfile' and save the current flag commands to a new file with the
   same name. When set to False, the task will exit with an error
   message if the file exist.

Example

.. container:: section
   :name: viewlet-below-content-body
