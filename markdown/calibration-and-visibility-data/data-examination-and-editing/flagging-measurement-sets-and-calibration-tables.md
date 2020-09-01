

# Flag using flagdata 

Flagging MeasurementSets and calibration tables

**flagdata** is the main flagging task in CASA. **flagdata** can flag MeasurementSets and calibration tables with an elaborate selection syntax. It also contains auto-flagging routines.

 

Other tasks related to flagging are **flagmanager** to save the existing flags before adding more, and  **plotms** and **msview** for interactive flagging. In addition, optionally, data for which calibration solutions have failed will be flagged when these solutions are applied.

 

The inputs to **flagdata** are:

```
#In CASA
CASA<1>: inp flagdata
# flagdata :: All-purpose flagging task based on data-selections and flagging modes/algorithms.
vis              = ''          # Name of MS file or calibration table to flag
mode             = 'manual'    # Flagging mode
     field       = ''          # Field names or field index numbers: '' ==> all, field='0~2,3C286'
     spw         = ''          # Spectral-window/frequency/channel: '' ==> all, spw='0:17~19'
     antenna     = ''          # Antenna/baselines: '' ==> all, antenna ='3,VA04'
     timerange   = ''          # Time range: '' ==> all,timerange='09:14:0~09:54:0'
     correlation = ''          # Correlation: '' ==> all, correlation='XX,YY'
     scan        = ''          # Scan numbers: '' ==> all
     intent      = ''          # Observation intent: '' ==> all, intent='CAL*POINT*'
     array       = ''          # (Sub)array numbers: '' ==> all
     uvrange     = ''          # UV range: '' ==> all; uvrange ='0~100klambda', default units=meters
     observation = ''          # Observation ID: '' ==> all
     feed        = ''          # Multi-feed numbers: Not yet implemented
     autocorr    = False       # Flag auto-correlations

action           = 'apply'     # Action to perform in MS and/or in inpfile (none/apply/calculate)
     display     = ''          # Display data and/or end-of-MS reports at runtime (data/report/both).
     flagbackup  = True        # Back up the state of flags before the run

savepars         = False       # Save the current parameters to the FLAG_CMD table or to a file
```

vis] can take a MeasurementSet or calibration table. Data selection for calibration tables is limited to [field, scan, time, antenna, spw, and observation. See section at end about which parameters are applicable for calibration tables. Since calibration tables do not have a *FLAG_CMD* table, parameter settings, if requested, can only be saved in external files. 

##   {#section .subsection}

## The *mode* parameter {#sec179 .subsection}

The mode parameter selects the flagging algorithm and the following are available:

``` {.verbatim}
list        = list of flagging commands to apply to MS
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
```

these are described in detail lower down.

Flagging will only be applied to the data selection that is performed with the usual selection parameters. The dataset is iterated-through in chunks (small pieces of data) consisting of one field, one spw, and a user-defined timerange (default is one scan). In addition to the typical antenna, spw, timerange, etc. selections, we would like to point out some addition of the correlation] syntax for modes clip, tfcrop, and [ rflag. One can combine correlation products with simple mathematical expressions 

``` {.verbatim}
'ABS', 'ARG', 'RE', 'IM', 'NORM' 
```

where *ABS* is the absolute value, *RE*, the real and *IM* the imaginary part. *NORM* and *ARG* refer to the amplitude and phase. This parameter is followed by the polarization products (using an underscore in between "\_" )

``` {.verbatim}
'ALL', 'I', 'XX', 'YY', 'RR', 'LL', 'WVR' 
```

'WVR'] refers to the water vapour radiometer of ALMA data. Note that the operators [ABS,ARG,RE, etc. are written only once as the first value. if more than one correlation is given, the operator will be applied to all of them. An example would be 

```
correlation = 'RE_XX, XY'
```

which would select all real XX and XY polarization for flagging. 

------------------------------------------------------------------------

## The *action* parameter {#sec179 .subsection}

The parameter action] controls whether the actual flagging commands will be applied or not and the options are the empty string "], ['apply' and ['calculate'.

apply is likely the most popular one as it applies the flags to the MS:

```
#In CASA:
action = 'apply' # Action to perform in MS and/or in inpfile
# (none/apply/calculate)
display = '' # Display data and/or end-of-MS reports at runtime
# (data/report/both).
flagbackup = True # Back up the state of flags before the run
```

flagbackup] specifies if a backup of the current flags should be saved in the "\*.flagversions"] file. [display] can be [ ", 'data', 'report', 'both'] where the empty string ["] will report no individual flagging statistics, whereas ['data'] launches an interactive GUI to display data and flags for each chunk to browse through. The plots are time-frequency planes and both old and new flags are being overlaid for all correlations per baseline. In the GUI, one can step though all chunks for inspection and if the flagging is unsatisfactory, one can exit without applying the flags. If the flagging is acceptable, it is also possible to continue flagging without viewing all chunks (the number of chunks can be very large for typical JVLA and ALMA data sets. [display='report' lists the flagging statistics at the end of the procedure on the screen and [ both starts the GUI and reports all statistics at the end.

action='calculate' calculates the flags but does not write them to the MS or calibration table. This is useful if one would like to inspect the computed flags in the GUI without a straight application:

```
action  = 'calculate' # Action to perform in MS and/or in inpfile (none/apply/calculate)
display = ''          # Display data and/or end-of-MS reports at runtime (data/report/both).
```

The empty string action="] will do nothing and is useful when the commands themselves shall only be written to the FLAG_CMD sub-table or to an external file using the [savepars parameter to specify the filename.

savepars] will save the flagging commands to a file that can be later used for input in flagdata] via [mode='list']. It also shares the [flagcmd] syntax and can be used there. The file name is specified by [outfile] and, if empty, the [FLAG_CMD] table in the MS will be populated. A [REASON] can be given by the [ reason] parameter which may be useful for bookkeeping as well as for unflagging data that are marked by specific [REASON parameters. The [overwrite parameter will control overwriting an existing file when saving the flag commands.

##   {#section-1 .subsection}

## Flagging Modes {#sec180 .subsection}

### Manual Flag/Unflag {#sec181 .subsubsection}

```
mode = 'manual' # Flagging mode (list/manual/clip/shadow/quack/el
# evation/tfcrop/rflag/extend/unflag/summary)
field = '' # Field names or field index numbers: '' ==> all,
# field='0~2,3C286'
spw = '' # Spectral-window/frequency/channel: '' ==> all,
# spw='0:17~19'
antenna = '' # Antenna/baselines: '' ==> all, antenna
# ='3,VA04'
timerange = '' # Time range: '' ==>
# all,timerange='09:14:0~09:54:0'
correlation = '' # Correlation: '' ==> all, correlation='XX,YY'
scan = '' # Scan numbers: '' ==> all
intent = '' # Observation intent: '' ==> all,
# intent='CAL*POINT*'
array = '' # (Sub)array numbers: '' ==> all
uvrange = '' # UV range: '' ==> all; uvrange ='0~100klambda',
# default units=meters
observation = '' # Observation ID: '' ==> all
feed = '' # Multi-feed numbers: Not yet implemented
autocorr = False # Flag auto-correlations
```

The 'manual'] mode is the most straight-forward of all modes. All visibilities that are selected by the various data selection parameters will be flagged or unflagged, depending on the  action] parameter. [autocorr is a shorthand for [ antenna='\*&&&' to flag all auto correlations in the data.

 

### List {#sec182 .subsubsection}

```
mode = 'list' # Flagging mode (list/manual/clip/shadow/quack/el
# evation/tfcrop/rflag/extend/unflag/summary)
inpfile = '' # Input ASCII file, list of
# files or Python list of strings with

# flag commands.
reason = 'any' # Select by REASON types
```

A list of flag commands can be provided through a file or a list of files, specified by the inpfile] parameter. Each input line may contain a flagging mode] with data selection parameters as well as parameters that are specific to that [mode]. All parameters that are not set will be reset to their default values (default [ mode] is ['manual']). Each line of this file or list of strings will be taken as a command to the [flagdata] task. This [ mode='list' is similar to the task flagcmd with the [ inpmode='list' option.

An example for such a file would be: 

``` {.verbatim}
mode='shadow'
mode='clip' clipminmax=[0,5] correlation='ABS_ALL'
mode='quack' quackmode='end' quackinterval=1.0
antenna='ea01' timerange='00:00:00~01:00:00'
antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'
```

Alternatively, this can be issued in the task directly like:

```
#In CASA:
CASA<1>: flagdata(vis='vis',mode='list',
inpfile=["mode='shadow'",
"mode='clip' clipminmax=[0,5] correlation='ABS_ALL'",
"mode='quack' quackmode='end' quackinterval=1.0"'
"antenna='ea01' timerange='00:00:00~01:00:00'",
"antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'"])
```

  or via a variable 

```
#In CASA:
CASA<1>:cmds=["mode='shadow',
"mode='clip' clipminmax=[0,5] correlation='ABS_ALL'",
"mode='quack' quackmode='end' quackinterval=1.0",
"antenna='ea01' timerange='00:00:00~01:00:00'",
"antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'"]

CASA<2>: flagdata(vis='vis',mode='list', inpfile=cmds)
```

The syntax needs to be written with quotes e.g. mode='manual' antenna='ea10']. There should be no space between [key=value. Spaces are used to separate pairs of parameters, not commas.

 

### Clip {#sec183 .subsubsection}

```
mode = 'clip' # Flagging mode (list/manual/clip/shadow/quack/
# elevation/tfcrop/rflag/extend/unflag/summary)
...
datacolumn = 'DATA' # Data column on which to operate
# (data,corrected,model,residual)
clipminmax = [] # Range to use for clipping
clipoutside = True # Clip outside the range, or within it
channelavg = False # Average over channels (scalar average)
timeavg = False # Average over time ranges
timebin = '' # Bin width for time averaging.
clipzeros = False # Clip zero-value data
```

in addition to the regular selection parameters, mode='clip'] also has an option to select between a number of scratch columns in datacolumn]. This includes the usual [DATA], [CORRECTED], etc., and also clipping based on data weights [WEIGHT], [ WEIGHT_SPECTRUM] as well as other MS columns. [clipminmax] selects the range of values to be clipped -- usually this is combined with [ clipoutside=True] to clip everything [but] the values covered in [clipminmax]. The data can also be averaged over the selected [ spw] channel ranges by setting [channelavg=True], or time averages via [timeavg=True] and setting of [timebin]. [clip will also flag 'NaN', 'inf', and '-inf' values by default and can flag exact zero values (these are sometimes produced by the JVLA correlator) using the [clipzeros parameter.

Note : For modes clip, tfcrop] and rflag, channel-ranges can be excluded from flagging by selecting ranges such as [ spw='0:05;1063'. This is a way to protect known spectral-lines from being flagged by the autoflag algorithms.

 

### Shadow {#sec184 .subsubsection}

```
mode = 'shadow' # Flagging mode (list/manual/clip/shadow/quack/
# elevation/tfcrop/rflag/extend/unflag/summary)
...
tolerance = 0.0 # Amount of shadow allowed (in meters)
addantenna = '' # File name or dictionary with additional antenna names,
# positions and diameters
```

This option flags shadowed antennas, i.e. when one antenna blocks part of the aperture of a second antenna that is behind the first one. Shadowing can be gradual and the criterion for a shadow flag is when a baseline is shorter than radius]~1~ + radius]~2~ − [tolerance] (where the radii of the antennae are taken from the MS antenna subtable); see the figure below. [addantenna may be used to account for shadowing when antennas are not listed in the MS but are physically present. Please read the [flagdata inline help for the syntax of this option.

------------------------------------------------------------------------

 ![1549b953275f8856b049cd09f60d19c320b125b8](media/1549b953275f8856b049cd09f60d19c320b125b8.png), [[http://www.aips.nrao.edu/cook.html\#CEE](http://www.aips.nrao.edu/cook.html#CEE))

In RFlag, the data is iterated-through in chunks of time, statistics are accumulated across time-chunks, thresholds are calculated at the end, and applied during a second pass through the dataset.

The CASA implementation also optionally allows a single-pass operation where statistics and thresholds are computed and also used for flagging, within each time-chunk (defined by 'ntime' and 'combinescans').

For each chunk, calculate local statistics, and apply flags based on user supplied (or auto-calculated) thresholds.

As of CASA 4.6 the data can also be pre-averaged over the selected spw] channel ranges by setting channelavg=True] and [chanbin] to the desired bin (in number of channels), or time averaged over the selected time ranges by setting [timeavg=True and [timebin to the desired time range (in seconds). This averaging is independent from the rflag time/channel sliding window, as it performs not only an average but also a binning operation (so there is no data overlap between adjacent bins), and allows to specify independent time/channel bins.

1.  Time analysis (for each channel) 
    a.  Calculate local rms of real and imag visibilities, within a sliding time window 
    b.  Calculate the median rms across time windows, deviations of local rms from this median, and the median deviation 
    c.  Flag if local rms is larger than timedevscale x (medianRMS + medianDev) 
2.  Spectral analysis (for each time) 
    a.  Calculate avg of real and imag visibilities and their rms across channels 
    b.  Calculate the deviation of each channel from this avg, and the median-deviation 
    c.  Flag if deviation is larger than freqdevscale x medianDev 

The extendflags] parameter will clean up small portions of data between flagged data points along time and/or frequency when more than 50% of all timeranges or 80% of all channels are already flagged. It will also extend the flags to the other polarizations. Alternatively, [mode='extend' can be used.

Some examples (see figure below):

1.  Calculate thresholds automatically per scan, and use them to find flags. Specify scale-factor for time-analysis thresholds, use default for frequency.
    ```
    #In CASA:
    CASA<1>: flagdata('my.ms', mode='rflag',spw='9',timedevscale=4.0)
    ```

2.  Supply noise-estimates to be used with default scale-factors.

    ```
    #In CASA:
    CASA<1>: flagdata(vis='my.ms', mode='rflag', spw='9', timedev=0.1, freqdev=0.5);
    ```

    Two-passes. This replicates the usage pattern in AIPS. 

    -   The first pass saves commands in an output text files, with auto-calculated thresholds. Thresholds are returned from rflag only when action=\'calculate\' (calc-only mode). The user can edit this file before doing the second pass, but the python-dictionary structure must be preserved.
    -   The second pass applies these commands (action=\'apply\').
        ```
        #In CASA:
        CASA<1>: flagdata(vis='my.ms', mode='rflag', spw='9,10', timedev='tdevfile.txt', freqdev='fdevfile.txt', action='calculate');
        CASA<2>: flagdata(vis='my.ms', mode='rflag', spw='9,10', timedev='tdevfile.txt', freqdev='fdevfile.txt', action='apply');
        ```

        

        ------------------------------------------------------------------------
        

        
         ![](markdown/_media/0897c13b6603be6efd68d97c7fc69171bef47cf6.png)
        
          --------------------------------------------------------------------------------------------------------------------------------------------------------------
          Example of rflag on narrow-band RFI
          --------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        

> 
>
> ------------------------------------------------------------------------
> 
>
> 
> 
>  
> 
>
> 
>  
> 
> 

### Extend {#sec188 .subsubsection}

```
mode = 'extend' # Flagging mode (list/manual/clip/shadow/quack/el
# evation/tfcrop/rflag/extend/unflag/summary)
field = '' # Field names or field index numbers: '' ==> all,
# field='0~2,3C286'
spw = '' # Spectral-window/frequency/channel: '' ==> all,
# spw='0:17~19'
antenna = '' # Antenna/baselines: '' ==> all, antenna
# ='3,VA04'
timerange = '' # Time range: '' ==>
# all,timerange='09:14:0~09:54:0'
correlation = '' # Correlation: '' ==> all, correlation='XX,YY'
scan = '' # Scan numbers: '' ==> all
intent = '' # Observation intent: '' ==> all,
# intent='CAL*POINT*'
array = '' # (Sub)array numbers: '' ==> all
uvrange = '' # UV range: '' ==> all; uvrange ='0~100klambda',
# default units=meters
observation = '' # Observation ID: '' ==> all
feed = '' # Multi-feed numbers: Not yet implemented
ntime = 'scan' # Time-range to use for each chunk (in seconds or
# minutes)
combinescans = False # Accumulate data across scans.
extendpols = True # If any correlation is flagged, flag all
# correlations
growtime = 50.0 # Flag all 'ntime' integrations if more than X%
# of the timerange is flagged (0-100)
growfreq = 50.0 # Flag all selected channels if more than X% of
# the frequency range is flagged(0-100)
growaround = False # Flag data based on surrounding flags
flagneartime = False # Flag one timestep before and after a flagged
# one (True/False)
flagnearfreq = False # Flag one channel before and after a flagged one
# (True/False)
```

Although the modes tfcrop] and rflag already have [ extendflags parameters, some autoflagging algorithms may still leave small islands of unflagged data behind, data that are surrounded by flagged visibilities in the time-frequency space. Although the algorithm may deem these visibilities as good ones, they are frequently affected by low-level RFI that spills from the adjacent, flagged points and one may wish to clean those up.

ntime] specifies the time ranges over which to clean up, e.g. '1.5min'] or ['scan'] which checks on all data within a scan. To span time ranges larger than scans, one can set [ combinescans to [True.

extendpols=True would extend all flags to all polarization products when at least one of them is flagged.

growtime flags the entire time range for a flagged channel, when a certain fraction of flagged time intervals is exceeded. 

growfreq is similar but extends the flags in frequency when a given fraction of channels is already flagged.

growaround checks for flagged data points in the time-frequency domain that neighbor a datum. The threshold is four data points. If more surrounding points are flagged, the central datum will be flagged, too.

flagneartime flags adjacent data points along the time axis, around a flagged datum

flagnearfreq flags neighboring channels. 

------------------------------------------------------------------------

 ![](markdown/_media/ff49a17852eab157b2326e6879023523c60dba54.png)

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  This screenshot represents a run where 'tfcrop' was run only on 'ABS_RR' (top row) and followed by an extension along time and correlations (bottom row). 
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

####   {#section-5 .subsubsection}

### Unflag {#sec190 .subsubsection}

```
mode = 'unflag' # Flagging mode (list/manual/clip/shadow/quack/
# elevation/tfcrop/rflag/extend/unflag/summary
# )
field = '' # Field names or field index numbers: ''==>all,
# field='0~2,3C286'
spw = '' # spectral-window/frequency/channel
antenna = 'ea01' # antenna/baselines: ''==>all, antenna
# ='3,VA04'
timerange = '' # time range:
# ''==>all,timerange='09:14:0~09:54:0'
correlation = '' # Select data based on correlation
scan = '' # scan numbers: ''==>all
intent = '' # Select data based on observation intent:
# ''==>all
feed = '' # multi-feed numbers: Not yet implemented
array = '' # (sub)array numbers: ''==>all
uvrange = '' # uv range: ''==>all; uvrange ='0~100klambda',
# default units=meters
observation = '' # Select data based on observation ID: ''==>all
```

The selection data will be unflagged. 

####   {#section-6 .subsubsection}

### Summary {#sec191 .subsubsection}

```
mode = 'summary' # Flagging mode (list/manual/clip/shadow/quack/
# elevation/tfcrop/rflag/extend/unflag/summary
# )
...
minrel = 0.0 # minimum number of flags (relative)
maxrel = 1.0 # maximum number of flags (relative)
minabs = 0 # minimum number of flags (absolute)
maxabs = -1 # maximum number of flags (absolute). Use a
# negative value to indicate infinity.
spwchan = False # Print summary of channels per spw
spwcorr = False # Print summary of correlation per spw
basecnt = False # Print summary counts per baseline
```

This mode reports the number of rows and data points that are flagged. The selection of reported points can be restricted (see inline help for details).

mode='summary' can also report back a dictionary if the task is run as 

```
#In CASA:
CASA<1>: s = flagdata(..., mode='summary')
```

with a variable assigned, here 's'.

