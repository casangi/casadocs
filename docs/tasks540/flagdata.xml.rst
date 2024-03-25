flagdata -- All-purpose flagging task based on data-selections and flagging modes/algorithms. -- editing task
=======================================

Description
---------------------------------------
        
        This task can flag a Measurement Set or a calibration table. It has 
        two main types of operation. One type will read the parameters from 
        the interface and flag using any of the various available modes. The 
        other type will read the commands from a text file, a list of files or 
        a Python list of strings, containing a list of flag commands (each line 
        containing data selection parameters and any parameter specific for the 
        mode being requested). Please see examples at the end of this help.
        
        It is also possible to only save the parameters set in the interface 
        without flagging. The parameters can be saved in the FLAG_CMD sub-table 
        or in a text file. Note that when saving to an external file, the parameters 
        will be appended to the given file.
        
        The available flagging modes are: manual, clip, shadow, quack, elevation, 
        tfcrop, rflag, extend, unflag and summary. For automatic flagging, it is 
        recommended to combine auto-flag modes with extend, via the list mode.

        The current flags can be automatically backed up before applying new 
        flags if the parameter flagbackup is set. Previous flag versions can be 
        recovered using the flagmanager task.
        
        NOTE on flagging calibration tables.
        -----------------------------------
        
        Flagdata can flag many types of calibration tables using mode='manual'. 
        It can only flag using the auto-flagging algorithms (clip, tfcrop or rflag), 
        the cal tables that have the following data columns: CPARAM, FPARAM or SNR. 
        The solution elements of the data columns are given in the correlation parameter using
        the names 'Sol1', 'Sol2', 'Sol3', or 'Sol4'. See examples at the end of
        this help on how to flag different cal tables.            
            
        When the input is a calibration table, the modes 'elevation' and 'shadow'
        will be disabled. Data selection for calibration tables is limited to field,
        scan, time, antenna, spw  and observation. It is only possible to save the 
        parameters to an external file. If the calibration table was created before
        CASA 4.1, this task will create a dummy OBSERVATION column and OBSERVATION
        sub-table in the input calibration table to adapt it to the new cal table
        format.
        
        Selecting antennas in some calibration tables have a different meaning compared
        to selecting the MS. Some calibration tables such as the antenna-based ones,
        created with some modes of gencal or polcal, have the ANTENNA2 column set to -1. 
        This means that when selecting antenna='ANT', will select the whole ANT and not the
        cross-correlations between ANT and the other antennas. Similarly, the baseline
        syntax do not apply to this type of calibration tables. Those values
        with ampersand do not have any meaning when selecting antenna/baselines
        in antenna-based cal tables.
            
    The task will flag a subset of data based on the following modes of operation:

    list        = list of flagging commands to apply to MS/cal table
    manual      = flagging based on specific selection parameters
    clip        = clip data according to values
    quack       = remove/keep specific time range at scan beginning/end
    shadow      = remove antenna-shadowed data
    elevation   = remove data below/above given elevations
    tfcrop      = automatic identification of outliers on the time-freq plane
    rflag       = automatic detection of outliers based on sliding-window RMS filters
    antint      = flag integrations if all baselines to a specified antenna are flagged
    extend      = extend and/or grow flags beyond what the basic algorithms detect
    summary     = report the amount of flagged data
    unflag      = unflag the specified data
                
        


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - 
   * - mode
     - :code:`'manual'`
     - 
   * - autocorr
     - :code:`False`
     - 
   * - inpfile
     - :code:`''`
     - 
   * - reason
     - :code:`'any'`
     - 
   * - tbuff
     - :code:`float(0.0)`
     - 
   * - spw
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - feed
     - :code:`''`
     - 
   * - clipminmax
     - :code:`numpy.array( [  ] )`
     - 
   * - datacolumn
     - :code:`'DATA'`
     - 
   * - clipoutside
     - :code:`True`
     - 
   * - channelavg
     - :code:`False`
     - 
   * - chanbin
     - :code:`int(1)`
     - 
   * - timeavg
     - :code:`False`
     - 
   * - timebin
     - :code:`'0s'`
     - 
   * - clipzeros
     - :code:`False`
     - 
   * - quackinterval
     - :code:`float(1.0)`
     - 
   * - quackmode
     - :code:`'beg'`
     - 
   * - quackincrement
     - :code:`False`
     - 
   * - tolerance
     - :code:`float(0.0)`
     - 
   * - addantenna
     - :code:`''`
     - 
   * - lowerlimit
     - :code:`float(0.0)`
     - 
   * - upperlimit
     - :code:`float(90.0)`
     - 
   * - ntime
     - :code:`'scan'`
     - 
   * - combinescans
     - :code:`False`
     - 
   * - timecutoff
     - :code:`float(4.0)`
     - 
   * - freqcutoff
     - :code:`float(3.0)`
     - 
   * - timefit
     - :code:`'line'`
     - 
   * - freqfit
     - :code:`'poly'`
     - 
   * - maxnpieces
     - :code:`int(7)`
     - 
   * - flagdimension
     - :code:`'freqtime'`
     - 
   * - usewindowstats
     - :code:`'none'`
     - 
   * - halfwin
     - :code:`int(1)`
     - 
   * - extendflags
     - :code:`True`
     - 
   * - winsize
     - :code:`int(3)`
     - 
   * - timedev
     - :code:`''`
     - 
   * - freqdev
     - :code:`''`
     - 
   * - timedevscale
     - :code:`float(5.0)`
     - 
   * - freqdevscale
     - :code:`float(5.0)`
     - 
   * - spectralmax
     - :code:`float(1E6)`
     - 
   * - spectralmin
     - :code:`float(0.0)`
     - 
   * - antint_ref_antenna
     - :code:`''`
     - 
   * - minchanfrac
     - :code:`float(0.6)`
     - 
   * - verbose
     - :code:`False`
     - 
   * - extendpols
     - :code:`True`
     - 
   * - growtime
     - :code:`float(50.0)`
     - 
   * - growfreq
     - :code:`float(50.0)`
     - 
   * - growaround
     - :code:`False`
     - 
   * - flagneartime
     - :code:`False`
     - 
   * - flagnearfreq
     - :code:`False`
     - 
   * - minrel
     - :code:`float(0.0)`
     - 
   * - maxrel
     - :code:`float(1.0)`
     - 
   * - minabs
     - :code:`int(0)`
     - 
   * - maxabs
     - :code:`int(-1)`
     - 
   * - spwchan
     - :code:`False`
     - 
   * - spwcorr
     - :code:`False`
     - 
   * - basecnt
     - :code:`False`
     - 
   * - fieldcnt
     - :code:`False`
     - 
   * - name
     - :code:`'Summary'`
     - 
   * - action
     - :code:`'apply'`
     - 
   * - display
     - :code:`''`
     - 
   * - flagbackup
     - :code:`True`
     - 
   * - savepars
     - :code:`False`
     - 
   * - cmdreason
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`True`
     - 
   * - writeflags
     - :code:`True`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of MS file or calibration table to flag


mode
---------------------------------------

:code:`'manual'`

Flagging mode


autocorr
---------------------------------------

:code:`False`

Flag only the auto-correlations


inpfile
---------------------------------------

:code:`''`

Input ASCII file, list of files or Python list of strings with flag commands.


reason
---------------------------------------

:code:`'any'`

Select by REASON types


tbuff
---------------------------------------

:code:`float(0.0)`

List of time buffers (sec) to pad timerange in flag commands


spw
---------------------------------------

:code:`''`

Spectral-window/frequency/channel: '' ==> all, spw="0:17~19"


field
---------------------------------------

:code:`''`

Field names or field index numbers: '' ==> all, field="0~2,3C286"


antenna
---------------------------------------

:code:`''`

Antenna/baselines: '' ==> all, antenna ="3,VA04"


uvrange
---------------------------------------

:code:`''`

UV range: '' ==> all; uvrange ="0~100klambda", default units=meters


timerange
---------------------------------------

:code:`''`

Time range: '' ==> all,timerange="09:14:0~09:54:0"


correlation
---------------------------------------

:code:`''`

Correlation: '' ==> all, correlation="XX,YY"


scan
---------------------------------------

:code:`''`

Scan numbers: '' ==> all


intent
---------------------------------------

:code:`''`

Scan intent: '' ==> all, intent="CAL*POINT*"


array
---------------------------------------

:code:`''`

(Sub)array numbers: '' ==> all


observation
---------------------------------------

:code:`''`

Observation ID: '' ==> all


feed
---------------------------------------

:code:`''`

Multi-feed numbers: Not yet implemented


clipminmax
---------------------------------------

:code:`numpy.array( [  ] )`

Range to use for clipping


datacolumn
---------------------------------------

:code:`'DATA'`

Data column on which to operate (data,corrected,model,weight,etc.)


clipoutside
---------------------------------------

:code:`True`

Clip outside the range, or within it


channelavg
---------------------------------------

:code:`False`

Pre-average data across channels before analyzing visibilities for flagging


chanbin
---------------------------------------

:code:`int(1)`

Bin width for channel average in number of input channels


timeavg
---------------------------------------

:code:`False`

Pre-average data across time before analyzing visibilities for flagging.


timebin
---------------------------------------

:code:`'0s'`

Bin width for time average in seconds


clipzeros
---------------------------------------

:code:`False`

Clip zero-value data


quackinterval
---------------------------------------

:code:`float(1.0)`

Quack n seconds from scan beginning or end


quackmode
---------------------------------------

:code:`'beg'`

Quack mode. beg: first n seconds of scan; endb: last n seconds of scan; end: all but first n seconds of scan; tail: all but last n seconds of scan.


quackincrement
---------------------------------------

:code:`False`

Increment quack flagging in time taking into account flagged data or not.


tolerance
---------------------------------------

:code:`float(0.0)`

Amount of shadow allowed (in meters)


addantenna
---------------------------------------

:code:`''`

File name or dictionary with additional antenna names, positions and diameters


lowerlimit
---------------------------------------

:code:`float(0.0)`

Lower limiting elevation (in degrees)


upperlimit
---------------------------------------

:code:`float(90.0)`

Upper limiting elevation (in degrees)


ntime
---------------------------------------

:code:`'scan'`

Time-range to use for each chunk (in seconds or minutes)


combinescans
---------------------------------------

:code:`False`

Accumulate data across scans depending on the value of ntime.


timecutoff
---------------------------------------

:code:`float(4.0)`

Flagging thresholds in units of deviation from the fit


freqcutoff
---------------------------------------

:code:`float(3.0)`

Flagging thresholds in units of deviation from the fit


timefit
---------------------------------------

:code:`'line'`

Fitting function for the time direction (poly/line)


freqfit
---------------------------------------

:code:`'poly'`

Fitting function for the frequency direction (poly/line)


maxnpieces
---------------------------------------

:code:`int(7)`

Number of pieces in the polynomial-fits (for "freqfit" or "timefit" = "poly")


flagdimension
---------------------------------------

:code:`'freqtime'`

Dimensions along which to calculate fits (freq/time/freqtime/timefreq)


usewindowstats
---------------------------------------

:code:`'none'`

Calculate additional flags using sliding window statistics (none,sum,std,both)


halfwin
---------------------------------------

:code:`int(1)`

Half-width of sliding window to use with "usewindowstats" (1,2,3).


extendflags
---------------------------------------

:code:`True`

Extend flags along time, frequency and correlation.


winsize
---------------------------------------

:code:`int(3)`

Number of timesteps in the sliding time window [aips:fparm(1)]


timedev
---------------------------------------

:code:`''`

Time-series noise estimate [aips:noise]


freqdev
---------------------------------------

:code:`''`

Spectral noise estimate [aips:scutoff]


timedevscale
---------------------------------------

:code:`float(5.0)`

Threshold scaling for timedev [aips:fparm(9)]. Ignored for the purpose of calculating thresholds (when action is "calculate") It is used when applying flags (i.e. action="apply") and displaying reports when action="calculate".


freqdevscale
---------------------------------------

:code:`float(5.0)`

Threshold scaling for freqdev [aips:fparm(10)]. Similarly as timedevscale, it is used when applying flags and displaying reports.


spectralmax
---------------------------------------

:code:`float(1E6)`

Flag whole spectrum if freqdev is greater than spectralmax [aips:fparm(6)]


spectralmin
---------------------------------------

:code:`float(0.0)`

Flag whole spectrum if freqdev is less than spectralmin [aips:fparm(5)] 


antint_ref_antenna
---------------------------------------

:code:`''`

Antenna of interest. Baselines with this antenna will be checked for flagged channels.


minchanfrac
---------------------------------------

:code:`float(0.6)`

Minimum fraction of flagged channels required for a baseline to be deemed as flagged


verbose
---------------------------------------

:code:`False`

Print timestamps of flagged integrations to the log


extendpols
---------------------------------------

:code:`True`

If any correlation is flagged, flag all correlations


growtime
---------------------------------------

:code:`float(50.0)`

Flag all "ntime" integrations if more than X% of the timerange is flagged (0-100)


growfreq
---------------------------------------

:code:`float(50.0)`

Flag all selected channels if more than X% of the frequency range is flagged(0-100)


growaround
---------------------------------------

:code:`False`

Flag data based on surrounding flags


flagneartime
---------------------------------------

:code:`False`

Flag one timestep before and after a flagged one (True/False)


flagnearfreq
---------------------------------------

:code:`False`

Flag one channel before and after a flagged one (True/False)


minrel
---------------------------------------

:code:`float(0.0)`

minimum number of flags (relative)


maxrel
---------------------------------------

:code:`float(1.0)`

maximum number of flags (relative)


minabs
---------------------------------------

:code:`int(0)`

minimum number of flags (absolute)


maxabs
---------------------------------------

:code:`int(-1)`

maximum number of flags (absolute). Use a negative value to indicate infinity.


spwchan
---------------------------------------

:code:`False`

Print summary of channels per spw


spwcorr
---------------------------------------

:code:`False`

Print summary of correlation per spw


basecnt
---------------------------------------

:code:`False`

Print summary counts per baseline


fieldcnt
---------------------------------------

:code:`False`

Produce a separated breakdown for each field


name
---------------------------------------

:code:`'Summary'`

Name of this summary report (key in summary dictionary)


action
---------------------------------------

:code:`'apply'`

Action to perform in MS and/or in inpfile (none/apply/calculate)


display
---------------------------------------

:code:`''`

Display data and/or end-of-MS reports at runtime (data/report/both).


flagbackup
---------------------------------------

:code:`True`

Back up the state of flags before the run


savepars
---------------------------------------

:code:`False`

Save the current parameters to the FLAG_CMD table or to a file


cmdreason
---------------------------------------

:code:`''`

Reason to save to output file or to FLAG_CMD table.


outfile
---------------------------------------

:code:`''`

Name of output file to save current parameters. If empty, save to FLAG_CMD


overwrite
---------------------------------------

:code:`True`

Overwrite an existing file to save the flag commands


writeflags
---------------------------------------

:code:`True`

Internal hidden parameter. Do not modify.




