#
# stub function definition file for docstring parsing
#

def flagdata(vis, mode='manual', autocorr=False, inpfile='', reason='any', tbuff=0.0, spw='', field='', antenna='', uvrange='', timerange='', correlation='', scan='', intent='', array='', observation='', feed='', clipminmax=[''], datacolumn='DATA', clipoutside=True, channelavg=False, chanbin=1, timeavg=False, timebin='0s', clipzeros=False, quackinterval=1.0, quackmode='beg', quackincrement=False, tolerance=0.0, addantenna='', lowerlimit=0.0, upperlimit=90.0, ntime='scan', combinescans=False, timecutoff=4.0, freqcutoff=3.0, timefit='line', freqfit='poly', maxnpieces=7, flagdimension='freqtime', usewindowstats='none', halfwin=1, extendflags=True, winsize=3, timedev='', freqdev='', timedevscale=5.0, freqdevscale=5.0, spectralmax=1E6, spectralmin=0.0, antint_ref_antenna='', minchanfrac=0.6, verbose=False, extendpols=True, growtime=50.0, growfreq=50.0, growaround=False, flagneartime=False, flagnearfreq=False, minrel=0.0, maxrel=1.0, minabs=0, maxabs=-1, spwchan=False, spwcorr=False, basecnt=False, fieldcnt=False, name='Summary', action='apply', display='', flagbackup=True, savepars=False, cmdreason='', outfile='', overwrite=True, writeflags=True):
    r"""
All-purpose flagging task based on data-selections and flagging modes/algorithms.

Parameters
   - **vis** (string) - Name of input visibility file
   - **mode** (string='manual') - Flagging mode (list/manual/clip/quack/shadow/elevation/tfcrop/rflag/antint/extent/unflag/summary)

      .. raw:: html

         <details><summary><i> mode = manual </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **autocorr** (bool=False) - Flag only the auto-correlations?

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = manualflag </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **autocorr** (bool=False) - Flag only the auto-correlations?

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = list </i></summary>

      - **inpfile** ({string, stringArray}='') - Input ASCII file, list of files or Python list of strings with flag commands.
      - **reason** ({string, stringArray}='any') - Select by REASON types
      - **tbuff** ({double, doubleArray}=0.0) - List of time buffers (sec) to pad timerange in flag commands

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = clip </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **datacolumn** ({string, stringArray}='DATA') - Data column on which to operate
      - **clipminmax** (doubleArray=['']) - Range to use for clipping
      - **clipoutside** ({bool, boolArray}=True) - Clip outside the range, or within it
      - **channelavg** ({bool, boolArray}=False) - Pre-average data across channels before analyzing visibilities for flagging
      - **chanbin** ({int, intArray}=1) - Bin width for channel average in number of input channels
      - **timeavg** ({bool, boolArray}=False) - Pre-average data across time before analyzing visibilities for flagging.
      - **timebin** (string='0s') - Bin width for time average in seconds
      - **clipzeros** (bool=False) - Clip zero-value data

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = quack </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **quackinterval** ({double, doubleArray, int, intArray}=1.0) - Quack n seconds from scan beginning or end
      - **quackmode** ({string, stringArray}='beg') - Quack mode. Flag intervals of the scan according to given mode.
      - **quackincrement** ({bool, boolArray}=False) - Increment quack flagging in time taking into account flagged data or not.

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = shadow </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **tolerance** (double=0.0) - Amount of shadow allowed (in meters)
      - **addantenna** ({string, record}='') - File name or dictionary with additional antenna names, positions and diameters

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = elevation </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **lowerlimit** (double=0.0) - Lower limiting elevation (in degrees)
      - **upperlimit** (double=90.0) - Upper limiting elevation (in degrees)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = tfcrop </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **ntime** ({double, string}='scan') - Time-range to use for each chunk (in seconds or minutes)
      - **combinescans** (bool=False) - Accumulate data across scans depending on the value of ntime.
      - **datacolumn** ({string, stringArray}='DATA') - Data column on which to operate
      - **timecutoff** (double=4.0) - Flagging thresholds in units of deviation from the fit
      - **freqcutoff** (double=3.0) -  Flagging thresholds in units of deviation from the fit
      - **timefit** (string='line') - Fitting function for the time direction (poly/line)
      - **freqfit** (string='poly') - Fitting function for the frequency direction (poly/line)
      - **maxnpieces** (int=7) - Number of pieces in the polynomial-fits (for freqfit or timefit poly)
      - **flagdimension** (string='freqtime') - Dimensions along which to calculate fits (freq, time, freqtime, timefreq)
      - **usewindowstats** (string='none') - Calculate additional flags using sliding window statistics (none, sum, std, both)
      - **halfwin** (int=1) - Half-width of sliding window to use with usewindowstats (1,2,3).
      - **extendflags** (bool=True) - Extend flags along time, frequency and correlation.
      - **channelavg** ({bool, boolArray}=False) - Pre-average data across channels before analyzing visibilities for flagging
      - **chanbin** ({int, intArray}=1) - Bin width for channel average in number of input channels
      - **timeavg** ({bool, boolArray}=False) - Pre-average data across time before analyzing visibilities for flagging.
      - **timebin** (string='0s') - Bin width for time average in seconds

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = rflag </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **ntime** ({double, string}='scan') - Time-range to use for each chunk (in seconds or minutes)
      - **combinescans** (bool=False) - Accumulate data across scans depending on the value of ntime.
      - **datacolumn** ({string, stringArray}='DATA') - Data column on which to operate
      - **winsize** (int=3) - Number of timesteps in the sliding time window
      - **timedev** (variant='') - Time-series noise estimate
      - **freqdev** (variant='') - Spectral noise estimate
      - **timedevscale** (double=5.0) - Threshold scaling for timedev
      - **freqdevscale** (double=5.0) - Threshold scaling for freqdev.
      - **spectralmax** (double=1E6) - Flag whole spectrum if freqdev is greater than spectralmax
      - **spectralmin** (double=0.0) - Flag whole spectrum if freqdev is less than spectralmin
      - **extendflags** (bool=True) - Extend flags along time, frequency and correlation.
      - **channelavg** ({bool, boolArray}=False) - Pre-average data across channels before analyzing visibilities for flagging
      - **chanbin** ({int, intArray}=1) - Bin width for channel average in number of input channels
      - **timeavg** ({bool, boolArray}=False) - Pre-average data across time before analyzing visibilities for flagging.
      - **timebin** (string='0s') - Bin width for time average in seconds

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = antint </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **datacolumn** ({string, stringArray}='DATA') - Data column on which to operate
      - **antint_ref_antenna** (string='') - Antenna of interest. Baselines with this antenna will be checked for flagged channels.
      - **minchanfrac** (double=0.6) - Minimum fraction of flagged channels required for a baseline to be deemed as flagged
      - **verbose** (bool=False) - Print timestamps of flagged integrations to the log

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = extend </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **ntime** ({double, string}='scan') - Time-range to use for each chunk (in seconds or minutes)
      - **combinescans** (bool=False) - Accumulate data across scans depending on the value of ntime.
      - **extendpols** (bool=True) - If any correlation is flagged, flag all correlations
      - **growtime** (double=50.0) - Flag all ntime integrations if more than X percent of the timerange is flagged (0-100)
      - **growfreq** (double=50.0) - Flag all selected channels if more than X percent of the frequency range is flagged (0-100)
      - **growaround** (bool=False) - Flag data based on surrounding flags
      - **flagneartime** (bool=False) - Flag one timestep before and after a flagged one (True/False)
      - **flagnearfreq** (bool=False) - Flag one channel before and after a flagged one (True/False)

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = unflag </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> mode = summary </i></summary>

      - **field** ({string, stringArray}='') - Select field using field id(s) or field name(s)
      - **spw** ({string, stringArray}='') - Select spectral window/channels
      - **antenna** ({string, stringArray}='') - Select data based on antenna/baseline
      - **timerange** ({string, stringArray}='') - Select data based on time range
      - **correlation** ({string, stringArray}='') - Select data based on correlation
      - **scan** ({string, stringArray}='') - Scan number range
      - **intent** ({string, stringArray}='') - Select observing intent
      - **array** ({string, stringArray}='') - (Sub)array numbers
      - **uvrange** ({string, stringArray}='') - Select data by baseline length.
      - **observation** ({string, int}='') - Select by observation ID(s)
      - **feed** ({string, stringArray}='') - Multi-feed numbers: Not yet implemented
      - **minrel** (double=0.0) - Minimum number of flags (relative)
      - **maxrel** (double=1.0) - Maximum number of flags (relative)
      - **minabs** (int=0) - Minimum number of flags (absolute)
      - **maxabs** (int=-1) - Maximum number of flags (absolute). Use a negative value to indicate infinity.
      - **spwchan** (bool=False) - Print summary of channels per spw
      - **spwcorr** (bool=False) - Print summary of correlation per spw
      - **basecnt** (bool=False) - Print summary counts per baseline
      - **fieldcnt** (bool=False) - Produce a separated breakdown for each field
      - **name** (string='Summary') - Name of this summary report (key in summary dictionary)

      .. raw:: html

         </details>
   - **action** (string='apply') - Action to perform in MS and/or in inpfile (none/apply/calculate)

      .. raw:: html

         <details><summary><i> action = apply </i></summary>

      - **display** (string='') - Display data and/or end-of-MS reports at runtime (data/report/both).
      - **flagbackup** (bool=True) - Back up the state of flags before the run

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> action = calculate </i></summary>

      - **display** (string='') - Display data and/or end-of-MS reports at runtime (data/report/both).

      .. raw:: html

         </details>
   - **savepars** (bool=False) - Save the current parameters to the FLAG_CMD table or to a file

      .. raw:: html

         <details><summary><i> savepars = True </i></summary>

      - **cmdreason** (string='') - Reason to save to output file or to FLAG_CMD table.
      - **outfile** (string='') - Name of output file to save current parameters. If empty, save to FLAG_CMD
      - **overwrite** (bool=True) - Overwrite an existing file to save the flag commands

      .. raw:: html

         </details>


Description
      This task can flag a MeasurementSet or a calibration table. It has
      two main types of operation. One type will read the parameters
      from the interface and flag using any of the various available
      modes. The other type will read the commands from a text file, a
      list of files or a Python list of strings, containing a list of
      flag commands (each line containing data selection parameters and
      any parameter specific for the mode being requested). Please see
      examples at the end of this help.

      It is also possible to only save the parameters set in the
      interface without flagging. The parameters can be saved in the
      FLAG_CMD sub-table or in a text file. Note that when saving to an
      external file, the parameters will be appended to the given file.

      The available flagging modes are: 'manual', 'clip', 'shadow',
      'quack', 'elevation', 'tfcrop', 'rflag', 'extend', 'unflag' and
      'summary'. For automatic flagging, it is recommended to combine
      auto-flag modes with 'extend', via the *list* mode.

      The current flags can be automatically backed up before applying
      new flags if the parameter *flagbackup* is set. Previous flag
      versions can be recovered using the **flagmanager** task.

      .. note:: | **NOTE** on flagging calibration tables:
         |         
         | **flagdata** can flag many types of calibration tables using
           *mode='manual'*. It can only flag using the auto-flagging
           algorithms ('clip', 'tfcrop', or 'rflag'), the cal tables
           that have the following data columns: CPARAM, FPARAM or SNR.
           The solution elements of the data columns are given in the
           *correlation* parameter using the names 'Sol1', 'Sol2',
           'Sol3', or 'Sol4'. See examples at the end of this help on
           how to flag different cal tables.

         When the input is a calibration table, the modes 'elevation'
         and 'shadow' will be disabled. Data selection for calibration
         tables is limited to *field*, *scan*, *timerange*, *antenna*,
         *spw*  and *observation*. It is only possible to save the
         parameters to an external file. If the calibration table was
         created before CASA 4.1, this task will create a dummy
         OBSERVATION column and OBSERVATION sub-table in the input
         calibration table to adapt it to the new cal table format.

         Selecting antennas in some calibration tables have a different
         meaning compared to selecting the MS. Some calibration tables
         such as the antenna-based ones, created with some modes of
         **gencal** or **polcal**, have the ANTENNA2 column set to -1.
         This means that when selecting *antenna='ANT'*, will select the
         whole ANT and not the cross-correlations between ANT and the
         other antennas. Similarly, the baseline syntax do not apply to
         this type of calibration tables. Those values with ampersand do
         not have any meaning when selecting antenna/baselines in
         antenna-based cal tables.

      The task will flag a subset of data based on the following modes
      of operation:

      -  'list' = list of flagging commands to apply to MS/cal table
      -  'manual' = flagging based on specific selection parameters
      -  'clip' = clip data according to values
      -  'quack' = remove/keep specific time range at scan beginning/end
      -  'shadow' = remove antenna-shadowed data
      -  'elevation' = remove data below/above given elevations
      -  'tfcrop' = automatic identification of outliers on the
         time-freq plane
      -  'rflag' = automatic detection of outliers based on
         sliding-window RMS filters
      -  'antint' = flag integrations if all baselines to a specified
         antenna are flagged
      -  'extend' = extend and/or grow flags beyond what the basic
         algorithms detect
      -  'summary' = report the amount of flagged data
      -  'unflag' = unflag the specified data 

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *vis*
         :name: vis

      Name of input visibility file or calibration table. Default: ''
      (none). Examples: *vis='uid___A002_X2a5c2f_X54.ms'*,
      *vis='cal-X54.B1'*

      .. rubric:: *mode*
         :name: mode

      Mode of operation. Options: 'list', 'manual', 'clip', 'quack',
      'shadow', 'elevation', 'tfcrop', 'extend', 'unflag', 'summary'.
      Default: 'manual'

      .. rubric:: *mode* expandable parameters (except *mode='list'*)
         :name: mode-expandable-parameters-except-modelist

      .. rubric:: *field*
         :name: field

      Select fields in mosaic. Use field id(s) or field name(s). [go
      listobs to obtain the list id's or names] Default: '' = all
      fields. If field string is a non-negative integer, it is assumed
      to be a field index otherwise, it is assumed to be a field name.
      Examples: *field='0~2'*, field ids 0,1,2; *field='0,4,5~7'*, field
      ids 0,4,5,6,7; *field='3C286,3C295'*, field named 3C286 and 3C295;
      *field = '3,4C*'*, field id 3 and all names starting with 4C.

      .. rubric:: *spw*
         :name: spw

      Select data based on spectral window and channels. Default: '' =>
      all spectral windows and channels. Examples: *spw='0~2,4'*,
      spectral windows 0,1,2,4 (all channels); *spw='0:5~61'*, spw 0,
      channels 5 to 61; *spw='<2'*, spectral windows less than 2 (i.e.
      0,1); *spw='0,10,3:3~45'*, spw 0,10 all channels, spw 3, channels
      3 to 45; *spw='0~2:2~6'*; spw 0,1,2 with channels 2 through 6 in
      each; *spw='0:0~10;15~60'*; spectral window 0 with channels
      0-10,15-60; *spw='0:0~10,1:20~30,2:1;2;3'*; spw 0, channels 0-10,
      spw 1, channels 20-30, and spw 2, channels, 1,2 and 3.

      .. note:: **NOTE** : For modes 'clip', 'tfcrop', and 'rflag',
         channel-ranges can be excluded from flagging by leaving them
         out of the selection range. This is a way to protect known
         spectral-lines from being flagged by the autoflag algorithms.

      .. rubric:: *antenna*
         :name: antenna

      Select data based on baseline. Default: '' (all). Examples:
      *antenna='DV04&DV06'* baseline DV04-DV06;
      *antenna='DV04&DV06;DV07&DV10'* baselines DV04-DV06 and DV07-DV10;
      *antenna='DV06'* all cross-correlation baselines between antenna
      DV06 and all other available antennas; *antenna='DV04,DV06'* all
      baselines with antennas DV04 and DV06; *antenna='DV06&&DV06'* only
      the auto-correlation baselines for antenna DV06;
      *antenna='DV04&&*'* cross and auto-correlation baselines between
      antenna DV04 and all other available antennas; *antenna='0~2&&&'*
      only the auto-correlation baselines for antennas in range 0~2   

      .. note:: **NOTE**: For some antenna-based calibration tables, selecting
         baselines with the & syntax do not apply.

      .. rubric:: *timerange*
         :name: timerange

      Select data based on time range. Default: '' (all). Examples:
      *timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'*;

      .. note:: **NOTE**: if YYYY/MM/DD is missing date defaults to first day
         in data set.

      *timerange='09:14:0~09:54:0'* picks 40 min on first day;
      *timerange='25:00:00~27:30:00'* picks 1 hr to 3 hr 30min on NEXT
      day; *timerange='09:44:00'* pick data within one integration of
      time; *timerange='>10:24:00'* data after this time.

      .. rubric:: *correlation*
         :name: correlation

      Correlation types or expression. Default: '' (all correlations).
      For modes clip, tfcrop or rflag, the default means ABS_ALL. If the
      input is cal table that does not contain a complex data column,
      the default will fall back to REAL_ALL. Examples:
      *correlation='XX,YY'* or options: Any of 'ABS', 'ARG', 'REAL',
      'IMAG', 'NORM' followed by any of 'ALL', 'I', 'XX', 'YY', 'RR',
      'LL', 'WVR'. 'WVR' refers to the water vapour radiometer of ALMA
      data. For calibration tables, the solutions are: 'Sol1', 'Sol2',
      Sol3, Sol4. Correlation selection is not supported for modes other
      than 'clip', 'tfcrop', or 'rflag' in cal tables.

      .. note:: **NOTE**: The operators ABS, ARG, REAL, etc. are written only
         once as the first value. If more than one correlation is given,
         the operator will be applied to all of them. The expression is
         used only in modes 'clip', 'tfcrop', and 'rflag'.

      .. rubric:: *scan*
         :name: scan

      Scan number range. Default: '' (all). Examples: *scan='1~5'*.
      Check 'go listobs' to insure the scan numbers are in order.

      .. rubric:: *intent*
         :name: intent

      Select data based on scan intent. Intent selection is not
      supported for cal tables. Default: '' (all). Examples:
      *intent='*CAL*,*BAND*'*

      .. rubric:: *array*
         :name: array

      Selection based on the antenna array. Array selection is not
      supported for cal tables. Default: '' (all).

      .. rubric:: *uvrange*
         :name: uvrange

      Select data within uvrange (default units meters). Default: ''
      (all). Examples: *uvrange='0~1000klambda'*, uvrange from 0-1000
      kilo-lambda; *uvrange='>4klambda'*, uvranges greater than 4 kilo
      lambda. *uvrange* selection is not supported for cal tables.

      .. rubric:: *observation*
         :name: observation

      Selection based on the observation ID. Default: '' (all).
      Examples: *observation='1'* or *observation=1*

      .. rubric:: *feed*
         :name: feed

      Selection based on the feed - NOT IMPLEMENTED YET

       

      .. rubric:: *mode='manual'* expandable parameters
         :name: modemanual-expandable-parameters

      Flag according to the data selection specified. This is the
      default mode (used when the mode is not specified).

      .. rubric:: *autocorr*
         :name: autocorr

      Flag only the auto-correlations. Note that this parameter is only
      active when set to True. If set to False it does NOT mean "do not
      flag auto-correlations". When set to True, it will only flag data
      from a processor of type CORRELATOR. Default: False. Otions: True,
      False

       

      .. rubric:: *mode='list'* expandable parameters
         :name: modelist-expandable-parameters

      Flag according to the data selection and flag commands specified
      in the input list. The input list may come from a text file, a
      list of text files or from a Python list of strings. Each input
      line may contain data selection parameters and any parameter
      specific to the mode given in the line. Default values will be
      used for the parameters that are not present in the line. Each
      line will be taken as a command to the task. If data is
      pre-selected using any of the selection parameters, then flagging
      will apply only to that subset of the MS.

      For optimization and whenever possible, the task will create a
      union of the data selection parameters present in the list and
      select only that portion of the MS.

      .. note:: **NOTE1**: The flag commands will be applied only when
         *action='apply'*. If *action='calculate'* the flags will be
         calculated, but not applied. This is useful if *display* is set
         to something other than 'none'. If *action=''* or *'none'*, the
         flag commands will not be applied either. An empty *action* is
         useful only to save the parameters of the list to a file or to
         the FLAG_CMD sub-table.

         **NOTE2**: quackincrement = True works based on the state of
         prior flagging, and unless it is the first item in the list the
         agent doing the quacking in list mode doesn't know about the
         state of prior flags. In this case, the command with
         quackincrement=True  will be ignored and the task will issue a
         WARNING.

      .. rubric:: *inpfile*
         :name: inpfile

      Input ASCII file, list of files or a Python list of command
      strings. Default: ''. Options: [ ] with flag commands or [ ] with
      filenames or ' ' with a filename.

      .. note:: **IMPORTANT**: From CASA 4.3 onwards, the parser will be strict
         and accept only valid **flagdata** parameters in the list. It
         will check each parameter name and type and exit with an error
         if any of them is wrong. String values must contain quotes
         around them or the parser will not work. The parser evaluates
         the commands in the list and considers only existing Python
         types.

      .. note:: **NOTE**: There should be no whitespace between KEY=VALUE since
         the parser first breaks command lines on whitespace, then on
         "=". Use only one whitespace to separate the parameters (no
         commas). Scroll down to the bottom to see a detailed
         description of the input list syntax..

      Example1: The following commands can be saved to a file or group
      of files and given to the task (e.g., save it to 'flags.txt'): 

      ::

         scan='1~3' mode='manual'
         mode='clip' clipminmax=[0,2] correlation='ABS_XX' clipoutside=False
         spw='9' mode='tfcrop' correlation='ABS_YY' ntime=51.0
         mode='extend' extendpols=True

      .. note:: flagdata(vis, mode='list', inpfile='flags.txt')

      or

      .. note:: flagdata(vis, mode='list', inpfile=['onlineflags.txt'
         ,'otherflags.txt'])

      Example2: The same commands can be given in a Python list on the
      command line to the task.

      .. note:: | cmd=["scan='1~3' mode='manual'",
         |      "mode='clip' clipminmax=[0,2] correlation='ABS_XX'
           clipoutside=False",
         |      "spw='9' mode='tfcrop' correlation='ABS_YY' ntime=51.0",
         |      "mode='extend' extendpols=True"]
         | flagdata(vis,mode='list',inpfile=cmd)

      .. rubric:: *reason*
         :name: reason

      Select flag commands based on REASON(s). Can be a string, or list
      of strings. If *inpfile* is a list of files, the reasons given in
      this parameter will apply to all the files. Default: 'any' (all
      flags regardless of reason). Examples: *reason='FOCUS_ERROR'*;
      *reason=['FOCUS_ERROR', 'SUBREFLECTOR_ERROR']*   

      .. note:: **NOTE**: what is within the string is literally matched, e.g.
         reason='' matches only blank reasons, and r *eason =
         'FOCUS_ERROR, SUBREFLECTOR_ERROR'* matches this compound reason
         string only. See the syntax for writing flag commands at the
         end of this help. 

      .. rubric:: *tbuff*
         :name: tbuff

      A time buffer or list of time buffers to pad the *timerange*
      parameters in flag commands. When a list of 2 time buffers is
      given, it will subtract the first value from the lower time and
      the second value will be added to the upper time in the range. The
      2 time buffer values can be different, allowing to have an
      irregular time buffer padding to time ranges. If the list contains
      only one time buffer, it will use it to subtract from t0 and add
      to t1. If more than one list of input files is given, *tbuff* will
      apply to all of the flag commands that have *timerange* parameters
      in the files.

      Each *tbuff* value should be a float number given in seconds.
      Default: 0.0 (it will not apply any time padding). Example:
      *tbuff=[0.5, 0.8] inpfile=['online.txt','userflags.txt'].* The
      *timerange* parameters in the 'online.txt' file are first
      converted to seconds. Then, 0.5 is subtracted from t0 and 0.8 is
      added to t1, where t0 and t1 are the two intervals given in
      timerange. Similarly, *tbuff* will be applied to any timerange in
      'userflags.txt'.   

      .. note:: **IMPORTANT**: This parameter assumes that timerange = t0 ~ t1,
         therefore it will not work if only t0 or t1 is given.

      .. note:: **NOTE**: The most common use-case for tbuff is to apply the
         online flags that are created by importasdm when savecmds=True.
         The value of a regular time buffer should be
         *tbuff=0.5*max* (integration time).

       

      .. rubric:: *mode='clip'* expandable parameters
         :name: modeclip-expandable-parameters

      Clip data according to values of the following subparameters. The
      polarization expression is given by the *correlation* parameter.
      For calibration tables, the solutions are also given by the
      *correlation* parameter.

      .. rubric:: *clipminmax*
         :name: clipminmax

      Range of data (Jy) that will NOT be flagged. It will always flag
      the NaN/Inf data, even when a range is specified. Default: [ ].
      Example: *clipminmax=[0.0,1.5]*

      .. rubric:: *clipoutside*
         :name: clipoutside

      Clip OUTSIDE the range. Default: True. Example:
      *clipoutside=False*, flag data WITHIN the *clipminmax* range.

      .. rubric:: *clipzeros*
         :name: clipzeros

      Clip zero-value data. Default: False.

       

      .. rubric:: *mode='clip', 'tfcrop', or 'rflag'* expandable
         parameters
         :name: modeclip-tfcrop-or-rflag-expandable-parameters

      .. rubric:: *datacolumn*
         :name: datacolumn

      Column to use for clipping. Default: 'DATA'. Options: MS columns:
      'DATA', 'CORRECTED', 'MODEL', 'RESIDUAL', 'RESIDUAL_DATA',
      'WEIGHT_SPECTRUM', 'WEIGHT', 'FLOAT_DATA'. Cal table columns:
      'FPARAM', 'CPARAM', 'SNR', 'WEIGHT'.                            

      .. note:: | **NOTE1**: RESIDUAL = CORRECTED - MODEL
         |              RESIDUAL_DATA = DATA - MODEL
         | **NOTE2**: When *datacolumn* is WEIGHT, the task will
           internally use WEIGHT_SPECTRUM. If WEIGHT_SPECTRUM does not
           exist, it will create one on-the-fly based on the values of
           WEIGHT.

      .. rubric:: *channelavg*
         :name: channelavg

      Pre-average data across channels before analyzing visibilities for
      flagging. Partially flagged data is not be included in the average
      unless all data contributing to a given output channel is flagged.
      If present, WEIGHT_SPECTRUM/ SIGMA_SPECTRUM are used to compute a
      weighted average (WEIGHT_SPECTRUM for CORRECTED_DATA and
      SIGMA_SPECTRUM for DATA). Default: False. Options:
      True/False                   

      .. note:: | NOTE1: Pre-average across channels is meant to be used with
           the auto-flagging methods (clip, tfcrop, rflag) only. In list
           mode, if channelavg is enabled and any other method than
           clip, tfcrop, rflag is used, that is forbidden and flagdata
           will produce an error message and stop. The same applies to
           timeavg.
         | **NOTE2**: Pre-average across channels is not supported for
           calibration tables.

      .. rubric:: *chanbin*
         :name: chanbin

      Bin width for channel average in number of input channels. If a
      list is given, each bin applies to one of the selected SPWs. When
      chanbin is set to 1 all input channels are used considered for the
      average to produce a single output channel, this behaviour aims to
      be preserve backwards compatibility with the previous
      pre-averaging feature of clip mode. Default: 1    

      .. rubric:: *timeavg*
         :name: timeavg

      Pre-average data across time before analyzing visibilities for
      flagging. Partially flagged data is not be included in the average
      unless all data contributing to a given output channel is flagged.
      If present, WEIGHT_SPECTRUM/ SIGMA_SPECTRUM are used to compute a
      weighted average (WEIGHT_SPECTRUM for CORRECTED_DATA and
      SIGMA_SPECTRUM for DATA). Otherwise WEIGHT/ SIGMA are used to
      average together data from different integrations. Default: False.
      Options: True/False 

      .. note:: | NOTE1: Pre-average across time is meant to be used with the
           auto-flagging methods (clip, tfcrop, rflag) only. In list
           mode, if timeavg is enabled and any other method than clip,
           tfcrop, rflag is used, that is forbidden and flagdata will
           produce an error message and stop. The same applies to
           channelavg.
         | **NOTE2**: Pre-average across time is not supported for
           calibration tables 

      .. rubric:: *timebin*
         :name: timebin

      Bin width for time average in seconds. Default: '0s'

      [NOTE ADDED FROM CAS-12294] The auto-flagging methods (clip,
      tfcrop, rflag) can be used together with timeavg and channelavg,
      and other modes or agents. But when timeavg, channelavg (or both)
      are enabled the set of other modes or agents that can be used
      simultaneously is limited to the following ones: extendflags,
      antint, and the display='data' GUI. display='data' and extendflags
      can be added either in the flagdata command line or in list mode.
      antint can only be added in list mode, as there is no subparameter
      of clip, rflag, or tfcrop for this.

      .. rubric:: *mode='quack'* expandable parameters
         :name: modequack-expandable-parameters

      Option to remove specified part of scan beginning/end.

      .. rubric:: *quackinterval*
         :name: quackinterval

      Time in seconds from scan beginning or end to flag. Make time
      slightly smaller than the desired time. Default: 0.0. Type: int or
      float.

      .. rubric:: *quackmode*
         :name: quackmode

      Quack mode. Default: 'beg'. Options:

      -  'beg'  ==> flag an interval at the beginning of scan
      -  'endb' ==> flag an interval at the end of scan
      -  'tail' ==> flag all but an interval at the beginning of scan
      -  'end'  ==> flag all but an interval at end of scan

      Visual representation of quack mode flagging one scan with 1s
      duration. The following diagram shows what is flagged for each
      quack mode when *quackinterval* is set to 0.25s. The flagged part
      is represented by crosses (+++++++++):

      ::

                    scan with 1s duration
         --------------------------------------------
         beg
         +++++++++++---------------------------------
                                          endb
         ---------------------------------+++++++++++
                    tail
         -----------+++++++++++++++++++++++++++++++++
         end
         +++++++++++++++++++++++++++++++++-----------

      .. rubric:: q *uackincrement*
         :name: quackincrement

      Increment quack flagging in time taking into account flagged data
      or not. Default: False. Type: bool

      -  False  ==> the quack interval is counted from the scan
         boundaries, as determined by the quackmode parameter,
         regardless if data has been flagged or not.
      -  True   ==> the quack interval is counted from the first
         unflagged data in the scan.

      .. note:: quackincrement = True works based on the state of prior
         flagging, and unless it is the first item in the list the agent
         doing the quacking in list mode doesn't know about the state of
         prior flags. In this case, the command with quackincrement=True
          will be ignored and the task will issue a WARNING.

       

      .. rubric:: *mode='shadow'* expandable parameters
         :name: modeshadow-expandable-parameters

      Option to flag data of shadowed antennas. This mode is not
      available for cal tables.

      All antennas in the ANTENNA subtable of the MS (and the
      corresponding diameters) will be considered for shadow-flag
      calculations. For a given timestep, an antenna is flagged if any
      of its baselines (projected onto the uv-plane) is shorter than 
      radius :math:`_{1}` :math:`+` radius :math:`_{2}` :math:`-`
      tolerance. The value of 'w' is used to determine which antenna is
      behind the other. The phase-reference center is used for
      antenna-pointing direction.

      .. rubric:: *tolerance*
         :name: tolerance

      Amount of shadowing allowed (or tolerated), in meters. A positive
      number allows antennas to overlap in projection. A negative number
      forces antennas apart in projection. Zero implies a distance of
      radius :math:`_{1}` :math:`+` radius :math:`_{2}` between
      antenna centers. Default: 0.0

      .. rubric:: *addantenna*
         :name: addantenna

      It can be either a file name with additional antenna names,
      positions and diameters, or a Python dictionary with the same
      information. You can use the **flaghelper** functions to create
      the dictionary from a file. Default: ''. Type: string or {}
      (dictionary). To create a dictionary inside CASA:

      .. note:: | import flaghelper as fh
         | antdic = fh.readAntennaList(antfile)

      Where antfile is a text file in disk that contains information
      such as:

      ::

         name=VLA01
         diameter=25.0
         position=[-1601144.96146691, -5041998.01971858, 3554864.76811967]
         name=VLA02
         diameter=25.0
         position=[-1601105.7664601889, -5042022.3917835914, 3554847.245159178]

       

      .. rubric:: *mode='elevation'* expandable parameters
         :name: modeelevation-expandable-parameters

      Option to flag based on antenna elevation. This mode is not
      available for cal tables.

      .. rubric:: *lowerlimit*
         :name: lowerlimit

      Lower limiting elevation in degrees. Data coming from a baseline
      where one or both antennas were pointing at a strictly lower
      elevation (as function of time), will be flagged. Default: 0.0

      .. rubric:: *upperlimit*
         :name: upperlimit

      Upper limiting elevation in degrees. Data coming from a baseline
      where one or both antennas were pointing at a strictly higher
      elevation (as function of time), will be flagged. Default: 90.0

       

      .. rubric:: *mode='tfcrop', 'rflag',* or *'extend'* expandable
         parameters
         :name: modetfcrop-rflag-or-extend-expandable-parameters

      .. rubric:: *ntime*
         :name: ntime

      Time range (in seconds or minutes) over which to buffer data
      before running the algorithm. Options: 'scan' or any other float
      value or string containing the units. Default: 'scan'. Examples:
      *ntime='1.5min'*; *ntime=1.2* (taken in seconds). The dataset will
      be iterated through in time-chunks defined here.

      .. note:: **WARNING**: If *ntime='scan'* and *combinescans=True*, all the
         scans will be loaded at once, thus requesting a lot of memory
         depending on the available spws.

      .. rubric:: *combinescans*
         :name: combinescans

      Accumulate data across scans depending on the value of *ntime*.
      Default: False. This parameter should be set to True only when
      *ntime* is specified as a time-interval (not 'scan'). When set to
      True, it will remove SCAN from the sorting columns, therefore it
      will only accumulate across scans if *ntime* is not set to 'scan'.

       

      .. rubric:: *mode='tfcrop'* expandable parameters
         :name: modetfcrop-expandable-parameters

      Flag using the TFCrop autoflag algorithm. For each field, spw,
      timerange (specified by ntime), and baseline:

      #.  Average visibility amplitudes along time dimension to form an
         average spectrum
      #. Calculate a robust piece-wise polynomial fit for the band-shape
         at the base of RFI spikes. Calculate 'stddev' of (data - fit).
      #. Flag points deviating from the fit by more than N-stddev
      #. Repeat (1-3) along the other dimension.

      This algorithm is designed to operate on un-calibrated data (step
      (2)), as well as calibrated data. It is recommended to extend the
      flags after running this algorithm. See the sub-parameter
      *extendflags* below.

      .. rubric:: *timecutoff*
         :name: timecutoff

      Flag threshold in time. Flag all data-points further than N-stddev
      from the fit. This threshold catches time-varying RFI spikes
      (narrow and broad-band), but will not catch RFI that is persistent
      in time. Default: 4.0.

      Flagging is done in up to 5 iterations. The stddev calculation is
      adaptive and converges to a value that reflects only the data and
      no RFI. At each iteration, the same relative threshold is applied
      to detect flags. (Step (3) of the algorithm).

      .. rubric:: *freqcutoff*
         :name: freqcutoff

      Flag threshold in frequency. Flag all data-points further than
      N-stddev from the fit. Same as *timecutoff*, but along the
      frequency-dimension. This threshold catches narrow-band RFI that
      may or may not be persistent in time. Default: 3.0

      .. rubric:: *timefit*
         :name: timefit

      Fitting function for the time direction. Default: 'line'. Options:
      'line', 'poly'

      A 'line' fit is a robust straight-line fit across the entire
      *timerange* (defined by *ntime*). A 'poly' fit is a robust
      piece-wise polynomial fit across the *timerange*. 

      .. note:: **NOTE**: A robust fit is computed in upto 5 iterations. At
         each iteration, the stddev between the data and the fit is
         computed, values beyond N-stddev are flagged, and the fit and
         stddev are re-calculated with the remaining points. This stddev
         calculation is adaptive, and converges to a value that reflects
         only the data and no RFI. It also provides a varying set of
         flagging thresholds, that allows deep flagging only when the
         fit best represents the true data. Choose 'poly' only if the
         visibilities are expected to vary significantly over the
         timerange selected by *ntime*, or if there is a lot of strong
         but intermittent RFI.

       

      .. rubric:: *freqfit*
         :name: freqfit

      Fitting function for the frequency direction. Same as for the
      *timefit* parameter. Default: 'poly'. Options: 'line', 'poly'.
      Choose 'line' only if you are operating on bandpass-corrected
      data, or residuals, and expect that the bandshape is linear. The
      'poly' option works better on uncalibrated bandpasses with
      narrow-band RFI spikes.

      .. rubric:: *maxnpieces*
         :name: maxnpieces

      Maxinum number of pieces to allow in the piecewise-polynomial
      fits. Default: 7. Options: 1 - 9. This parameter is used only if
      *timefit* or *freqfit* are chosen as 'poly'. If there is
      significant broad-band RFI, reduce this number. Using too many
      pieces could result in the RFI being fitted in the clean bandpass.
      In later stages of the fit, a third-order polynomial is fit per
      piece, so for best results, please ensure that
      *nchan*/*maxnpieces* is at-least 10.

      .. rubric:: *flagdimension*
         :name: flagdimension

      Choose the directions along which to perform flagging. Default:
      'freqtime'; first flag along frequency, and then along time.
      Options: 'time', 'freq', 'timefreq', 'freqtime'. For most cases,
      'freqtime' or 'timefreq' are appropriate, and differences between
      these choices are apparant only if RFI in one dimension is
      significantly stronger than the other. The goal is to flag the
      dominant RFI first. If there are very few (less than 5) channels
      of data, then choose 'time'. Similarly for 'freq'.

      .. rubric:: *usewindowstats*
         :name: usewindowstats

      Use sliding-window statistics to find additional flags. Default:
      'none'. Options: 'none', 'sum', 'std', 'both'

      .. note:: **WARNING**: This parameter is experimental!

      The 'sum' option chooses to flag a point, if the mean-value in a
      window centered on that point deviates from the fit by more than
      N-stddev :math:`/ 2.0`.

      .. note:: **NOTE**: stddev is calculated between the data and fit as
         explained in Step (2). This option is an attempt to catch
         broad-band or time-persistent RFI  that the above polynomial
         fits will mistakenly fit as the clean band. It is an
         approximation to the sumThreshold method found to be effective
         by Offringa et.al (2010) for LOFAR data.

      The 'std' option chooses to flag a point, if the 'local' stddev
      calculated in a window centered on that point is larger than
      N-stddev :math:`/2.0`. This option is an attempt to catch noisy
      RFI that is not excluded in the polynomial fits, and which
      increases the global stddev, and results in fewer flags (based on
      the N-stddev threshold).

      .. rubric:: *halfwin*
         :name: halfwin

      Half width of sliding window to use with *usewindowstats*.
      Default: 1 (a 3-point window size). Options: 1,2,3

      .. note:: **WARNING**: This is experimental!

       

      .. rubric:: *mode='tfcrop'* or *'rflag'* expandable parameters
         :name: modetfcrop-or-rflag-expandable-parameters

      .. rubric:: *extendflags*
         :name: extendflags

      Extend flags along time, frequency and correlation. Default: True

      .. note:: **NOTE**: It is usually helpful to extend the flags along time,
         frequency, and correlation using this parameter, which will run
         the 'extend' mode after 'tfcrop' and extend the flags if more
         than 50% of the timeranges are already flagged, and if more
         than 80% of the channels are already flagged. It will also
         extend the flags to the other polarizations. The user may also
         set extendflags to False and run the 'extend' mode in a second
         step within the same flagging run. See the example below.

       

      .. rubric:: *mode='rflag'* expandable parameters
         :name: moderflag-expandable-parameters

      Detect outliers based on the RFlag algorithm `[1] <#cit1>`__. The
      polarization expression is given by the *correlation* parameter.
      Iterate through the data in chunks of time. For each chunk,
      calculate local statistics, and apply flags based on user supplied
      (or auto-calculated) thresholds.

      -  Time analysis (for each channel):

         -  calculate local RMS of real and imaginary visibilities
            within a sliding time window
         -  calculate the median RMS across time windows, deviations of
            local RMS from this median, and the median deviation
         -  flag if local RMS is larger than *timedevscale* :math:`x`
            (medianRMS :math:`+` medianDev)

      -  Spectral analysis (for each time):

         -  calculate avg of real and imaginary visibilities and their
            RMS across channels
         -  calculate the deviation of each channel from this avg, and
            the median-deviation
         -  flag if deviation is larger than *freqdevscale* :math:`x`
            medianDev

      It is recommended to extend the flags after running this
      algorithm. See the sub-parameter *extendflags* below.

      Notice that by default the flag implementation in CASA is able to
      calculate the thresholds and apply them on-the-fly (OTF). There is
      a significant performance gain with this approach, as the
      visibilities don't have to be read twice, and therefore is highly
      recommended (see example 1). Otherwise it is possible to reproduce
      the AIPS usage pattern by doing a first run with
      *action='calculate'* and a second run with *action='apply'*. The
      advantage of this approach is that the thresholds are calculated
      using the data from all scans, instead of calculating them for one
      scan only (see example 3).

      Example usage :

      #. Calculate thresholds automatically per scan, and use them to
         find flags. Specify scale-factor for time-analysis thresholds,
         use default for frequency.

         .. note:: flagdata('my.ms', mode='rflag', spw='9', timedevscale=4.0)

      #. Supply noise-estimates to be used with default scale-factors.

         .. note:: flagdata(vis='my.ms', mode='rflag', spw='9', timedev=0.1,
            freqdev=0.5, action='calculate')

      #. Two-passes. This replicates the usage pattern in AIPS.

         -  The first pass saves commands in output text files, with
            auto-calculated thresholds. Thresholds are returned from
            'rflag' only when *action='calculate'*. The user can edit
            this file before doing the second pass, but the
            python-dictionary structure must be preserved. The
            parameters timedevscale and freqdevscale are not used in
            this first pass.
         -  The second pass applies these commands (*action='apply'*).

            .. note:: flagdata(vis='my.ms', mode='rflag', spw='9,10',
               timedev='tdevfile.txt', freqdev='fdevfile.txt',
               action='calculate')

            .. note:: flagdata(vis='my.ms', mode='rflag', spw='9,10',
               timedev='tdevfile.txt', freqdev='fdevfile.txt',
               action='apply')

      With *action='calculate'*, *display='report'* will produce
      diagnostic plots showing data-statistics and thresholds (the same
      thresholds as those written out to 'tdevfile.txt' and
      'fdevfile.txt'). In this second pass, with *action='apply'*, the
      parameters freqdevscale and timedevscale can be used to re-scale
      the thresholds calculated in the first pass.

      .. note:: | **NOTE1**: The RFlag algorithm was originally developed by
           Eric Greisen in AIPS `[1] <#cit1>`__ .
         | **NOTE2**: Since this algorithm operates with two passes
           through each chunk of data (time and freq axes), some data
           points get flagged twice. This can affect the flag-percentage
           estimate printed in the logger at runtime. An accurate
           estimate can be obtained via the 'summary' mode.
         | **NOTE3**: RFlag calculates statistics across all selected
           correlations. Therefore, if there is a significant amplitude
           difference between parallel-hand and cross-hand correlations,
           or between different solutions in a gain table, it is
           advisable to pre-select subsets of correlations (or sols) on
           which to run one instance of RFlag. For example,
           *correlation='RR,LL'* or *correlation='ABS sol1,sol2'.*

      .. note:: | **NOTE: dictionaries returned by action='calculate'.**
         | Rflag with action='calculate' (the first pass of the
           two-passes usage) can return a dictionary. The dictionary
           holds the freqdev and timedev thresholds calculated in that
           first pass. For example:

         thresholds = flagdata(vis='my.ms', mode='rflag',
         action='calculate')

         print(thresholds)

            {'type': 'list', 'report0': {'type': 'rflag', 'freqdev':
         array([[  1.0e+00,   0.0e+00,   3.13e-02], ... , 'name':
         'Rflag', 'timedev': array([[  1.0e+00,   0.0e+00,   6.8e-03],
         ... ])}, 'nreport': 1}

         The timedev and freqdev items from this dictionary can be used
         in the second pass call to flagdata, but their respective
         values need to be passed as separate parameters. For example:

         flagdata(vis=ms, mode='rflag', action='apply',
         timedev=thresholds['report0']['timedev'],
         freqdev=thresholds['report0']['freqdev'])

         This is an alternative approach (and fully equivalent) to using
         two files to save and reuse the timedev and freqdev values.

      .. rubric:: *winsize*
         :name: winsize

      Number of timesteps in the sliding time window (fparm(1) in AIPS).
      Default: 3

      .. rubric:: *timedev*
         :name: timedev

      Time-series noise estimate (noise in AIPS). Default: [ ].
      Examples: *timedev = 0.5*: Use this noise-estimate to calculate
      flags. Do not recalculate; *timedev = [[1,9,0.2], [1,10,0.5]]*:
      Use noise-estimate of 0.2 for field 1, spw 9, and noise-estimate
      of 0.5 for field 1, spw 10; *timedev = [ ]*: Auto-calculate noise
      estimates; *timedev='timedevfile'*: Auto-calculate noise estimates
      and write them into a file with the name given (any string will be
      interpreted as a file name which will be checked for existence).

      .. rubric:: *freqdev*
         :name: freqdev

      Spectral noise estimate (scutoff in AIPS). This step depends on
      having a relatively-flat bandshape. Same parameter-options as
      *timedev*. Default: [ ]

      .. rubric:: *timedevscale*
         :name: timedevscale

      For Step 1 (time analysis), flag a point if local RMS around it is
      larger than *timedevscale* :math:`x` *timedev* (fparm(0) in AIPS).
      This scale parameter is only applied when flagging
      (*action='apply'*) and displaying reports (display option). It is
      not used when the thresholds are simply calculated and saved into
      files (*action='calculate'*, as in the two-passes usage pattern of
      AIPS). Default: 5.0

      .. rubric:: *freqdevscale*
         :name: freqdevscale

      For Step 2 (spectral analysis), flag a point if local rms around
      it is larger than *freqdevscale* :math:`x` *freqdev* (fparm(10) in
      AIPS). Similarly as with timedevscale, freqdevscale is not used
      when the thresholds are simply calculated and saved into files
      (*action='calculate',* as in the two-passes usage pattern of
      AIPS). Default: 5.0

      .. rubric:: *spectralmax*
         :name: spectralmax

      Flag whole spectrum if *freqdev* is greater than *spectralmax*
      (fparm(6) in AIPS). Default: 1E6

      .. rubric:: *spectralmin*
         :name: spectralmin

      Flag whole spectrum if *freqdev* is less than *spectralmin*
      (fparm(5) in AIPS). Default: 0.0

       

      .. rubric:: *mode='extend'* expandable parameters
         :name: modeextend-expandable-parameters

      Extend and/or grow flags beyond what the basic algorithms detect.
      This mode will extend the accumulated flags available in the MS,
      regardless of which algorithm created them. It is recommended that
      any autoflag (tfcrop, rflag) algorithm be followed up by a flag
      extension. Extensions will apply only within the selected data,
      according to the settings of *extendpols*, *growtime*, *growfreq*,
      *growaround*, *flagneartime*, and *flagnearfreq*.

      .. note:: **NOTE** : Runtime summary counts in the logger can sometimes
         report larger flag percentages than what is actually flagged.
         This is because extensions onto already-flagged data-points are
         counted as new flags. An accurate flag count can be obtained
         via the 'summary' mode.

      .. rubric:: *extendpols*
         :name: extendpols

      Extend flags to all selected correlations. Default: True. Options:
      True/False. For example, to extend flags from RR to only RL and
      LR, a data-selection of *correlation='RR,LR,RL'* is required along
      with *extendpols=True*.

      .. rubric:: *growtime*
         :name: growtime

      For any channel, flag the entire timerange in the current 2D chunk
      (set by *ntime*) if more than X% of the *timerange* is already
      flagged. Default: 50.0. Options: 0.0 - 100.0. This option catches
      the low-intensity parts of time-persistent RFI.

      .. rubric:: g *rowfreq*
         :name: growfreq

      For any timestep, flag all channels in the current 2D chunk (set
      by data-selection) if more than X% of the channels are already
      flagged. Default: 50.0. Options: 0.0 - 100.0. This option catches
      broad-band RFI that is partially identified by earlier steps.

      .. rubric:: *growaround*
         :name: growaround

      Flag a point based on the number of flagged points around it.
      Default: False. Options: True/False. For every un-flagged point on
      the 2D time/freq plane, if more than four surrounding points are
      already flagged, flag that point. This option catches some wings
      of strong RFI spikes.

      .. rubric:: *flagneartime*
         :name: flagneartime

      Flag points before and after every flagged one, in the
      time-direction. Default: False. Options: True/False. Note that
      this can result in excessive flagging.

      .. rubric:: *flagnearfreq*
         :name: flagnearfreq

      Flag points before and after every flagged one, in the
      frequency-direction. Default: False. Options: True/False. This
      option allows flagging of wings in the spectral response of strong
      RFI. Note that this can result in excessive flagging.

       

      .. rubric:: mode='antint' expandable parameters
         :name: modeantint-expandable-parameters

      | This mode flag all integrations in which a specified antenna is
        flagged. This mode operates for an spectral window. It flags any
        integration in which all baselines to a specified antenna are
        flagged, but only if this condition is satisfied in a fraction
        of channels within the spectral window of interest greater than
        a nominated fraction. For simplicity, it assumes that all
        polarization products must be unflagged for a baseline to be
        deemed unflagged. The antint mode implements the flagging
        approach introduced in 'antintflag'
        (https://doi.org/10.5281/zenodo.163546)                                                                              
         
      |                                                                                                                                        
      | The motivating application for introducing this mode is removal
        of data that will otherwise lead to changes in reference antenna
        during gain calibration, which will in turn lead to corrupted
        polarization calibration.

      .. rubric:: antint_ref_antenna
         :name: antint_ref_antenna

      Check the baselines to this antenna. Note that this is not the
      same as the general 'antenna' parameter of flagdata. The parameter
      antint_ref_antenna is mandatory with the   'antint' mode and
      chooses the antenna for which the fraction of channels flagged
      will be checked.

      .. rubric:: minchanfrac
         :name: minchanfrac

      Minimum fraction of flagged channels required for a baseline  to
      be deemed as flagged. Takes values between 0-1 (float). In this
      mode flagdata does the following for every point in time. It
      checks the fraction of channels flagged for any of the
      polarization products and for every baseline to the antenna of
      interest. If the fraction is higher than this 'minchanfrac'
      threshold then the data are flagged for this pont in time (this
      includes all the rows selected with the flagdata command that have
      that timestamp). This parameter will be ignored if spw specifies a
      channel.

      .. rubric:: verbose
         :name: verbose

      Print timestamps of flagged integrations to the log.

       

      .. rubric:: mode='unflag' expandable parameters
         :name: modeunflag-expandable-parameters

      | Unflag according to the data selection specified.

      .. rubric:: mode='summary' expandable parameters
         :name: modesummary-expandable-parameters

      List the number of rows and flagged data points for the MS's
      meta-data. The resulting summary will be returned as a Python
      dictionary.

      In 'summary' mode, the task returns a dictionary of flagging
      statistics.

      Example1:

      .. note:: s = flagdata(..., mode='summary')

      s will be a dictionary which contains:

      -  s['total']: total number of data
      -  s['flagged']: amount of flagged data

      Example2: two summary commands in 'list' mode, intercalating a
      manual flagging command.

      .. note:: s = flagdata(..., mode='list', inpfile=["mode='summary'
         name='InitFlags'", "mode='manual' autocorr=True",
         "mode='summary' name='Autocorr'"])

      The dictionary returned in s will contain two dictionaries, one
      for each of the two summary modes.

      -  s['report0']['name']: 'InitFlags'
      -  s['report1']['name']: 'Autocorr'

      .. rubric:: *minrel*
         :name: minrel

      Minimum number of flags (relative) to include in histogram.
      Default: 0.0

      .. rubric:: *maxrel*
         :name: maxrel

      Maximum number of flags (relative) to include in histogram.
      Default: 1.0

      .. rubric:: *minabs*
         :name: minabs

      Minimum number of flags (absolute, inclusive) to include in
      histogram. Default: 0

      .. rubric:: *maxabs*
         :name: maxabs

      Maximum number of flags (absolute, inclusive) to include in
      histogram. To indicate infinity, use any negative number. Default:
      -1

      .. rubric:: *spwchan*
         :name: spwchan

      List the number of flags per spw and per channel. Default: False

      .. rubric:: *spwcorr*
         :name: spwcorr

      Llist the number of flags per spw and per correlation. Default:
      False

      .. rubric:: *basecnt*
         :name: basecnt

      List the number of flags per baseline. Default: False

      .. rubric:: *fieldcnt*
         :name: fieldcnt

      Produce a separated breakdown per field. Default: False

      .. rubric:: *name*
         :name: name

      Name for this summary, to be used as a key in the returned Python
      dictionary. It is possible to call the 'summary' *mode* multiple
      times in 'list' *mode*. When calling the 'summary' *mode* as a
      command in a list, one can give different names to each one of
      them so that they can be easily pulled out of the summary's
      dictionary. Default: 'Summary'

       

      .. rubric:: *action*
         :name: action

      Action to perform in MS/cal table or in the input list of
      parameters. Options: 'none', 'apply', 'calculate'. Default:
      'apply'

      .. rubric:: *action='apply'* or *'calculate'* expandable
         parameters
         :name: actionapply-or-calculate-expandable-parameters

      action='apply' applies the flags to the MS. action='calculate'
      only calculates the flags but does not write them to the MS. This
      is useful if used together with the display to analyze the results
      before writing to the MS.

      .. rubric:: *display*
         :name: display

      | Display data and/or end-of-MS reports at run-time. It needs to
        read a *datacolumn* for the plotting. The default for an MS is
        DATA, but the task will use FLOAT_DATA for a Single-dish MS.
        Default: 'none'. Options: 'none', 'data', 'report', 'both'

      'none' --> It will not display anything.
      'data' --> display data and flags per-chunk at run-time, within an
      interactive GUI.

      -  This option opens a GUI to show the 2D time-freq planes of the
         data with old and new flags, for all correlations per baseline.
      -  The GUI allows stepping through all baselines (prev/next) in
         the current chunk (set by *ntime*), and stepping to the
         next-chunk.
      -  The **flagdata** task can be quit from the GUI, in case it
         becomes obvious that the current set of parameters is just
         wrong.
      -  There is an option to stop the display but continue flagging.

      'report' --> displays end-of-MS reports on the screen.
      'both' --> displays data per chunk and end-of-MS reports on the
      screen
       

      .. rubric:: *action='apply'* expandable parameters
         :name: actionapply-expandable-parameters

      .. rubric:: *flagbackup*
         :name: flagbackup

      Automatically backup flags before running the tool. Flagversion
      names are chosen automatically, and are based on the *mode* being
      used. Default: True. Options: True/False

       

      .. rubric:: action='' or 'none' description
         :name: action-or-none-description

      When set to empty or 'none', the underlying tool will not be
      executed and no flags will be produced. No data selection will be
      done either. This is useful when used together with the parameter
      *savepars* to only save the current parameters (or list of
      parameters) to the FLAG_CMD sub-table or to an external file.  

       

      .. rubric:: *savepars*
         :name: savepars

      Save the current parameters to the FLAG_CMD table of the MS or to
      an output text file.

      Note that when *display* is set to anything other than 'none',
      *savepars* will be disabled. This is done because in an
      interactive mode, the user may skip data which may invalidate the
      initial input parameters and there is no way to save the
      interactive commands. When the input is a calibration table it is
      only possible to save the parameters to a file.

      Default: False. Options: True/False

      .. rubric:: savepars=True expandable parameters
         :name: saveparstrue-expandable-parameters

      .. rubric:: *cmdreason*
         :name: cmdreason

      A string containing a reason to save to the FLAG_CMD table or to
      an output text file given by the *outfile* sub-parameter. If the
      input contains any *reason*, they will be replaced with this one.
      At the moment it is not possible to add more than one *reason*.
      Default: ' ', no *reason* will be added to output. Examples:
      *cmdreason='CLIP_ZEROS'*

      .. rubric:: *outfile*
         :name: outfile

      Name of output file to save the current parameters. Default: ' ',
      will save the parameters to the FLAG_CMD table of the MS.
      Examples: *outfile='flags.txt'* will save the parameters in a text
      file.

      .. rubric:: *overwrite*
         :name: overwrite

      Overwrite the existing file given in *outfile*. Options:
      True/False. Default: True, it will remove the existing file given
      in *outfile* and save the current flag commands to a new file with
      the same name. When set to False, the task will exit with an error
      message if the file exist.

       

      .. rubric:: SYNTAX FOR COMMANDS GIVEN IN A FILE or LIST OF STRINGS
         :name: syntax-for-commands-given-in-a-file-or-list-of-strings

      .. rubric:: Basic Syntax Rules
         :name: basic-syntax-rules

      #. Commands are strings (which may contain internal "strings")
         consisting of KEY=VALUE pairs separated by one whitespace only.

      .. note:: **NOTE**: There should be no whitespace between KEY=VALUE.The
         parser first breaks command lines on whitespace, then on "=".

      #. Use only ONE white space to separate the parameters (no
         commas). Each key should only appear once on a given command
         line/string.
      #. There is an implicit *mode* for each command, with the default
         being 'manual' if not given.
      #. Comment lines can start with '#' and will be ignored. The
         parser used in **flagdata** will check each parameter name and
         type and exit with an error if the parameter is not a valid
         **flagdata** parameter or of a wrong type.

      Example:

      ::

         scan='1~3' mode='manual'
         # this line will be ignored
         spw='9' mode='tfcrop' correlation='ABS_XX,YY' ntime=51.0
         mode='extend' extendpols=True
         scan='1~3,10~12' mode='quack' quackinterval=1.0


   Bibliography
         :sup:`1. Greisen, Eric, Dec 31, 2011. AIPS documentation:
         Section E.5 of the AIPS cookbook (Appendix E: Special
         Considerations for EVLA data calibration and imaging in
         AIPS,` http://www.aips.nrao.edu/cook.html#CEE :sup:`)` `<#ref-cit1>`__

    """
    pass
