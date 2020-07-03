.. container::
   :name: viewlet-above-content-title

Flag using flagdata
===================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Flagging MeasurementSets and calibration tables

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      flagdata is the main flagging task in CASA. flagdata can flag
      MeasurementSets and calibration tables with an elaborate selection
      syntax. It also contains auto-flagging routines.

       

      Other tasks related to flagging are flagmanager to save the
      existing flags before adding more, and  plotms and msview for
      interactive flagging. In addition, optionally, data for which
      calibration solutions have failed will be flagged when these
      solutions are applied.

       

      The inputs toflagdataare:

      .. container:: casa-input-box

         | #In CASA
         | CASA<1>: inp flagdata
         | # flagdata :: All-purpose flagging task based on
           data-selections and flagging modes/algorithms.
         | vis              = ''          # Name of MS file or
           calibration table to flag
         | mode             = 'manual'    # Flagging mode
         |      field       = ''          # Field names or field index
           numbers: '' ==> all, field='0~2,3C286'
         |      spw         = ''          #
           Spectral-window/frequency/channel: '' ==> all, spw='0:17~19'
         |      antenna     = ''          # Antenna/baselines: '' ==>
           all, antenna ='3,VA04'
         |      timerange   = ''          # Time range: '' ==>
           all,timerange='09:14:0~09:54:0'
         |      correlation = ''          # Correlation: '' ==> all,
           correlation='XX,YY'
         |      scan        = ''          # Scan numbers: '' ==> all
         |      intent      = ''          # Observation intent: '' ==>
           all, intent='CAL*POINT*'
         |      array       = ''          # (Sub)array numbers: '' ==>
           all
         |      uvrange     = ''          # UV range: '' ==> all;
           uvrange ='0~100klambda', default units=meters
         |      observation = ''          # Observation ID: '' ==> all
         |      feed        = ''          # Multi-feed numbers: Not yet
           implemented
         |      autocorr    = False       # Flag auto-correlations

         | action           = 'apply'     # Action to perform in MS
           and/or in inpfile (none/apply/calculate)
         |      display     = ''          # Display data and/or
           end-of-MS reports at runtime (data/report/both).
         |      flagbackup  = True        # Back up the state of flags
           before the run

         savepars         = False       # Save the current parameters to
         the FLAG_CMD table or to a file

      viscan take a MeasurementSet or calibration table. Data selection
      for calibration tables is limited tofield, scan, time, antenna,
      spw, and observation. See section at end about which parameters
      are applicable for calibration tables. Since calibration tables do
      not have a FLAG_CMD table, parameter settings, if requested, can
      only be saved in external files.

      .. rubric::  
         :name: section
         :class: subsection

      .. rubric:: Themodeparameter
         :name: sec179
         :class: subsection

      Themodeparameterselects the flagging algorithm and the following
      are available:

      .. code:: verbatim

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

      these are described in detail lower down.

      Flagging will only be applied to the data selection that is
      performed with the usual selection parameters. The dataset is
      iterated-through in chunks (small pieces of data) consisting of
      one field, one spw, and a user-defined timerange (default is one
      scan). In addition to the typical antenna, spw, timerange, etc.
      selections, we would like to point out some addition of
      thecorrelationsyntax for modesclip, tfcrop, andrflag. One can
      combine correlation products with simple mathematical expressions

      .. code:: verbatim

         'ABS', 'ARG', 'RE', 'IM', 'NORM' 

      where ABS is the absolute value, RE, the real and IM the imaginary
      part. NORM and ARG refer to the amplitude and phase. This
      parameter is followed by the polarization products (using an
      underscore in between “_” )

      .. code:: verbatim

         'ALL', 'I', 'XX', 'YY', 'RR', 'LL', 'WVR' 

      ’WVR’refers to the water vapour radiometer of ALMA data. Note that
      the operatorsABS,ARG,RE, etc. are written only once as the first
      value. if more than one correlation is given, the operator will be
      applied to all of them. An example would be

      .. container:: casa-input-box

         correlation = 'RE_XX, XY'

      which would select all real XX and XY polarization for flagging.

      --------------

      .. rubric:: Theactionparameter
         :name: sec179
         :class: subsection

      The parameteractioncontrols whether the actual flagging commands
      will be applied or not and the options are the empty
      string”,’apply’and’calculate’.

      applyis likely the most popular one as it applies the flags to the
      MS:

      .. container:: casa-input-box

         | #In CASA:
         | action = 'apply' # Action to perform in MS and/or in inpfile
         | # (none/apply/calculate)
         | display = '' # Display data and/or end-of-MS reports at
           runtime
         | # (data/report/both).
         | flagbackup = True # Back up the state of flags before the run

      flagbackupspecifies if a backup of the current flags should be
      saved in the“*.flagversions”file.displaycan be”, ’data’, ’report’,
      ’both’where the empty string”will report no individual flagging
      statistics, whereas’data’launches an interactive GUI to display
      data and flags for each chunk to browse through. The plots are
      time-frequency planes and both old and new flags are being
      overlaid for all correlations per baseline. In the GUI, one can
      step though all chunks for inspection and if the flagging is
      unsatisfactory, one can exit without applying the flags. If the
      flagging is acceptable, it is also possible to continue flagging
      without viewing all chunks (the number of chunks can be very large
      for typical JVLA and ALMA data sets.display=’report’lists the
      flagging statistics at the end of the procedure on the screen
      andbothstarts the GUI and reports all statistics at the end.

      action=’calculate’calculates the flags but does not write them to
      the MS or calibration table. This is useful if one would like to
      inspect the computed flags in the GUI without a straight
      application:

      .. container:: casa-input-box

         | action  = 'calculate' # Action to perform in MS and/or in
           inpfile (none/apply/calculate)
         | display = ''          # Display data and/or end-of-MS reports
           at runtime (data/report/both).

      The empty stringaction=”will do nothing and is useful when the
      commands themselves shall only be written to theFLAG_CMDsub-table
      or to an external file using thesaveparsparameter to specify the
      filename.

      saveparswill save the flagging commands to a file that can be
      later used for input inflagdataviamode=’list’. It also shares
      theflagcmdsyntax and can be used there. The file name is specified
      byoutfileand, if empty, theFLAG_CMDtable in the MS will be
      populated. AREASONcan be given by thereasonparameter which may be
      useful for bookkeeping as well as for unflagging data that are
      marked by specificREASONparameters. Theoverwriteparameter will
      control overwriting an existing file when saving the flag
      commands.

      .. rubric::  
         :name: section-1
         :class: subsection

      .. rubric:: Flagging Modes
         :name: sec180
         :class: subsection

      .. rubric:: Manual Flag/Unflag
         :name: sec181
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'manual' # Flagging mode
           (list/manual/clip/shadow/quack/el
         | # evation/tfcrop/rflag/extend/unflag/summary)
         | field = '' # Field names or field index numbers: '' ==> all,
         | # field='0~2,3C286'
         | spw = '' # Spectral-window/frequency/channel: '' ==> all,
         | # spw='0:17~19'
         | antenna = '' # Antenna/baselines: '' ==> all, antenna
         | # ='3,VA04'
         | timerange = '' # Time range: '' ==>
         | # all,timerange='09:14:0~09:54:0'
         | correlation = '' # Correlation: '' ==> all,
           correlation='XX,YY'
         | scan = '' # Scan numbers: '' ==> all
         | intent = '' # Observation intent: '' ==> all,
         | # intent='CAL*POINT*'
         | array = '' # (Sub)array numbers: '' ==> all
         | uvrange = '' # UV range: '' ==> all; uvrange ='0~100klambda',
         | # default units=meters
         | observation = '' # Observation ID: '' ==> all
         | feed = '' # Multi-feed numbers: Not yet implemented
         | autocorr = False # Flag auto-correlations

      The’manual’mode is the most straight-forward of all modes. All
      visibilities that are selected by the various data selection
      parameters will be flagged or unflagged, depending on
      theactionparameter.autocorris a shorthand forantenna=’*&&&’to flag
      all auto correlations in the data.

       

      .. rubric:: List
         :name: sec182
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'list' # Flagging mode
           (list/manual/clip/shadow/quack/el
         | # evation/tfcrop/rflag/extend/unflag/summary)
         | inpfile = '' # Input ASCII file, list of
         | # files or Python list of strings with

         | # flag commands.
         | reason = 'any' # Select by REASON types

      A list of flag commands can be provided through a file or a list
      of files, specified by theinpfileparameter. Each input line may
      contain a flaggingmodewith data selection parameters as well as
      parameters that are specific to thatmode. All parameters that are
      not set will be reset to their default values
      (defaultmodeis’manual’). Each line of this file or list of strings
      will be taken as a command to theflagdatatask. Thismode=’list’is
      similar to the task flagcmd with theinpmode=’list’option.

      An example for such a file would be:

      .. code:: verbatim

         mode='shadow'
         mode='clip' clipminmax=[0,5] correlation='ABS_ALL'
         mode='quack' quackmode='end' quackinterval=1.0
         antenna='ea01' timerange='00:00:00~01:00:00'
         antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'

      Alternatively, this can be issued in the task directly like:

      .. container:: casa-input-box

         | #In CASA:
         | CASA<1>: flagdata(vis='vis',mode='list',
         | inpfile=["mode='shadow'",
         | "mode='clip' clipminmax=[0,5] correlation='ABS_ALL'",
         | "mode='quack' quackmode='end' quackinterval=1.0"'
         | "antenna='ea01' timerange='00:00:00~01:00:00'",
         | "antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'"])

      or via a variable

      .. container:: casa-input-box

         | #In CASA:
         | CASA<1>:cmds=["mode='shadow',
         | "mode='clip' clipminmax=[0,5] correlation='ABS_ALL'",
         | "mode='quack' quackmode='end' quackinterval=1.0",
         | "antenna='ea01' timerange='00:00:00~01:00:00'",
         | "antenna='ea11' timerange='00:00:00~03:00:00' spw='0~4'"]

         | 
         | CASA<2>: flagdata(vis='vis',mode='list', inpfile=cmds)

      The syntax needs to be written with quotes e.g.mode=’manual’
      antenna=’ea10’. There should be no space betweenkey=value. Spaces
      are used to separate pairs of parameters, not commas.

       

      .. rubric:: Clip
         :name: sec183
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'clip' # Flagging mode (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary)
         | ...
         | datacolumn = 'DATA' # Data column on which to operate
         | # (data,corrected,model,residual)
         | clipminmax = [] # Range to use for clipping
         | clipoutside = True # Clip outside the range, or within it
         | channelavg = False # Average over channels (scalar average)
         | timeavg = False # Average over time ranges
         | timebin = '' # Bin width for time averaging.
         | clipzeros = False # Clip zero-value data

      in addition to the regular selection parameters,mode=’clip’also
      has an option to select between a number of scratch columns
      indatacolumn. This includes the usualDATA,CORRECTED, etc., and
      also clipping based on data weightsWEIGHT,WEIGHT_SPECTRUMas well
      as other MS columns.clipminmaxselects the range of values to be
      clipped – usually this is combined withclipoutside=Trueto clip
      everythingbutthe values covered inclipminmax. The data can also be
      averaged over the selectedspwchannel ranges by
      settingchannelavg=True, or time averages viatimeavg=Trueand
      setting oftimebin.clipwill also flag ’NaN’, ’inf’, and ’-inf’
      values by default and can flag exact zero values (these are
      sometimes produced by the JVLA correlator) using
      theclipzerosparameter.

      Note : For modesclip, tfcropandrflag, channel-ranges can be
      excluded from flagging by selecting ranges such asspw=’0:05;1063’.
      This is a way to protect known spectral-lines from being flagged
      by the autoflag algorithms.

       

      .. rubric:: Shadow
         :name: sec184
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'shadow' # Flagging mode
           (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary)
         | ...
         | tolerance = 0.0 # Amount of shadow allowed (in meters)
         | addantenna = '' # File name or dictionary with additional
           antenna names,
         | # positions and diameters

      This option flags shadowed antennas, i.e. when one antenna blocks
      part of the aperture of a second antenna that is behind the first
      one. Shadowing can be gradual and the criterion for a shadow flag
      is when a baseline is shorter
      thanradius\ :sub:`1`\ +radius\ :sub:`2`\ −tolerance(where the
      radii of the antennae are taken from the MS antenna subtable); see
      the figure below.addantennamay be used to account for shadowing
      when antennas are not listed in the MS but are physically present.
      Please read theflagdatainline help for the syntax of this option.

      .. container:: center

         --------------

      .. container:: center

         .. container:: caption

            +-------------------------------------------------------------------+
            | This figure shows the geometry used to compute shadowed antennas. |
            +-------------------------------------------------------------------+

       

       

      .. rubric:: Quack
         :name: quack

      .. container:: casa-input-box

         | mode = 'quack' # Flagging mode
           (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary)
         | ...
         | quackinterval = 0.0 # Quack n seconds from scan beginning or
           end
         | quackmode = 'beg' # flag an interval at the beginning of scan
         | 'endb' # flag an interval at the end of scan
         | 'tail' # flag all but an interval at the beginning of
         | scan
         | 'end' # flag all but an interval at end of scan

         quackincrement = False # Flag incrementally in time?

      quackis used to remove data at scan
      boundaries.quackintervalspecifies the time in seconds to be
      flagged, andquackmodecan be’beg’to flag thequackintervalat the
      beginning of each selected scan,’endb’at the end of
      scan.’tail’flags all but the beginning of scan and’end’all but the
      end of scan. Thequackincrementis eitherTrueorFalse, depending if
      one wishes to flag thequackintervalfrom the first unflagged data
      in the scan, or from the scan boundaries independent of data being
      already flagged or not.

       

      Because quackincrement=True needs to know the state of the
      previous flags in order to know which is the first unflagged data,
      it cannot be used in 'list' mode, unless it is the first command
      of the list.

      .. container:: casa-output-box

         | Visual representation of quack mode when flagging a scan
         | with 1s duration. The following diagram shows what is flagged
         | for each quack mode when quackinterval is set to 0.25s.
         | The flagged part is represented by crosses (+++++++++)

         | scan with 1s duration
         | --------------------------------------------
         | beg
         | +++++++++++---------------------------------
         | endb
         | ---------------------------------+++++++++++
         | tail
         | -----------+++++++++++++++++++++++++++++++++
         | end
         | +++++++++++++++++++++++++++++++++-----------

      .. rubric::  
         :name: section-2
         :class: subsubsection

      .. rubric:: Elevation
         :name: sec186
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'elevation' # Flagging mode
           (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary)
         | ...
         | lowerlimit = 0.0 # Lower limiting elevation (in degrees)
         | upperlimit = 90.0 # Upper limiting elevation (in degrees)

      Flagging based on the elevation of the antennae. This may be
      useful to avoid data taken at very low elevations or close to
      transit and thelowerlimitandupperlimitparameters specify the range
      of good elevations.

      .. rubric::  
         :name: section-3
         :class: subsubsection

      .. rubric:: Tfcrop
         :name: sec187
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'tfcrop' # Flagging mode
           (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary
         | # )
         | ...
         | ntime = 'scan' # Time-range to use for each chunk (in seconds
         | # or minutes)
         | combinescans = False # Accumulate data across scans.
         | datacolumn = 'DATA' # Data column on which to operate
         | # (data,corrected,model,residual)
         | timecutoff = 4.0 # Flagging thresholds in units of deviation
         | # from the fit
         | freqcutoff = 3.0 # Flagging thresholds in units of deviation
         | # from the fit
         | timefit = 'line' # Fitting function for the time direction
         | # (poly/line)
         | freqfit = 'poly' # Fitting function for the frequency
           direction
         | # (poly/line)
         | maxnpieces = 7 # Number of pieces in the polynomial-fits (for
         | # 'freqfit' or 'timefit' = 'poly')
         | flagdimension = 'freqtime' # Dimensions along which to
           calculate fits
         | # (freq/time/freqtime/timefreq)
         | usewindowstats = 'none' # Calculate additional flags using
           sliding
         | # window statistics (none,sum,std,both)
         | halfwin = 1 # Half-width of sliding window to use with
         | # 'usewindowstats' (1,2,3).
         | extendflags = True # Extend flags along time,
         | # frequency and correlation.
         | channelavg = False # Pre-average data across channels before
         | # analyzing visibilities for flagging.
         | chanbin = False # Bin width for channel average in
         | # number of input channels.
         | timeavg = False # Pre-average data across time before
         | # analyzing visibilities for flagging
         | timebin = False # Bin width for time average in seconds

      TFCrop is an autoflag algorithm that detects outliers on the 2D
      time-frequency plane, and can operate on un-calibrated data (non
      bandpass-corrected). The original implementation of this algorithm
      is described in NCRA Technical Report 202 (Oct 2003).

      The algorithm iterates through the data in chunks of time. For
      each chunk, the result of user-specified visibility-expressions
      are organized as 2D time-frequency planes, one for each baseline
      and correlation-expression result, and the following steps are
      performed.

      As of CASA 4.6 the data can also be pre-averaged over the
      selectedspwchannel ranges by settingchannelavg=Trueandchanbinto
      the desired bin (in number of channels), or time averaged over the
      selected time ranges by settingtimeavg=Trueandtimebinto the
      desired time range (in seconds). This averaging is independent
      from the tfcrop time/channel average, and allows to specify custom
      time/channel average bins, instead of averaging all data across
      time and/or channel direction.

      1. Calculate a bandshape template : Average the data across time,
         to construct an average bandpass. Construct an estimate of a
         clean bandpass (without RFI) via a robust piece-wise polynomial
         fit to the average bandpass shape.

         Note : A robust fit is computed in up to 5 iterations. It
         begins with a straight line fit across the full range, and
         gradually increases to ’maxnpieces’ number of pieces with
         third-order polynomials in each piece. At each iteration, the
         stddev between the data and the fit is computed, values beyond
         N-stddev are flagged, and the fit and stddev are re-calculated
         with the remaining points. This stddev calculation is adaptive,
         and converges to a value that reflects only the data and no
         RFI. At each iteration, the same relative threshold is applied
         to detect flags, and this results in a varying set of flagging
         thresholds, that allows deep flagging only when the fit
         represents the true data best. Iterations stop when the stddev
         changes by less than 10%, or when 5 iterations are completed.

         The resulting clean bandpass is a fit across the base of RFI
         spikes.

      2. Divide out this clean bandpass function from all timesteps in
         the current chunk. Now, any data points that deviate from a
         mean of 1 can be considered RFI. This step helps to separate
         narrow-band RFI spikes from a smooth but varying bandpass, in
         situations where a simple range-based clipping will flag good
         sections of the bandpass.

      3. Perform iterative flagging (robust flagging) of points
         deviating from a value of 1.

         Flagging is done in up to 5 iterations. In each iteration, for
         every timestep, calculate the stddev of the bandpass-flattened
         data, flag all points further than N times stddev from the fit,
         and recalculate the stddev. At each iteration, the same
         relative threshold is applied to detect flags. Optionally, use
         sliding-window based statistics to calculate additional flags.

      4. Repeat steps 1 and 3, but in the other direction (i.e. average
         the data across frequency, calculate a piece-wise polynomial
         fit to the average time-series, and find flags based on
         deviations w.r.to this fit.)

      The default parameters of the tfcrop implementation are optimized
      for strong narrow-band RFI (see the example figure below). With
      broad-band RFI, the piece-wise polynomial can sometimes model it
      as part of the band-shape, and therefore not detect it as RFI. In
      this case, reducing the maximum number of pieces in the polynomial
      can help. This algorithm usually has trouble with noisy RFI that
      is also extended in time of frequency, and additional
      statistics-based flagging is recommended (via the ’usewindowstats’
      parameter). It is often required to set up parameters separately
      for each spectral-window.

      If frequency ranges of known astronomical spectral lines are
      knowna-priori, they can be protected from automatic flagging by
      de-selecting those frequency-ranges via the ’spw’ data-selection
      parameter.

      Theextendflagparameter will clean up small portions of data
      between flagged data points along time and/or frequency when more
      than 50% of all timeranges or 80% of all channels are already
      flagged. It will also extend the flags to the other polarizations.
      Alternatively,mode=’extend’can be used (see section below).

       

      .. container:: center

         .. container:: caption

            +----------------------------------------------------------------------+
            | This screenshot represents a run where ’tfcrop’ was run on a spw=’9’ |
            | with mainly narrow-band RFI. RIGHT : An example of protecting a      |
            | spectral line (in this case, demonstrated on an RFI spike) by        |
            | setting the spw-selection to spw=’0:0 45;53 63’. In both figures,    |
            | the top row indicates the data before flagging, and the bottom row   |
            | after flagging.                                                      |
            +----------------------------------------------------------------------+

      ..

         .. container:: center

            --------------

      .. rubric::  
         :name: section-4
         :class: subsubsection

      .. rubric:: Rflag
         :name: sec188
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'rflag' # Flagging mode
           (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary
         | # )
         | ...
         | ntime = 'scan' # Time-range to use for each chunk (in seconds
         | # or minutes)
         | combinescans = False # Accumulate data across scans.
         | datacolumn = 'DATA' # Data column on which to operate
         | # (data,corrected,model,residual)
         | winsize = 3 # Number of timesteps in the sliding time
         | # window [aips:fparm(1)]
         | timedev = '' # Time-series noise estimate [aips:noise]
         | freqdev = '' # Spectral noise estimate [aips:scutoff]
         | timedevscale = 5.0 # Threshold scaling for timedev
           [aips:fparm(9)]
         | freqdevscale = 5.0 # Threshold scaling for freqdev
         | # [aips:fparm(10)]
         | spectralmax = 1000000.0 # Flag whole spectrum if freqdev is
           greater
         | # than spectralmax [aips:fparm(6)]
         | spectralmin = 0.0 # Flag whole spectrum if freqdev is less
           than
         | # spectralmin [aips:fparm(5)]
         | extendflags = True # Extend flags along time, frequency and
           correlation.
         | channelavg = False # Pre-average data across channels before
         | # analyzing visibilities for flagging.
         | chanbin = False # Bin width for channel average in
         | # number of input channels.
         | timeavg = False # Pre-average data across time before
         | # analyzing visibilities for flagging
         | timebin = False # Bin width for time average in seconds

      RFlag is an autoflag algorithm based on a sliding window
      statistical filter. The RFlag algorithm was originally developed
      by Eric Greisen in AIPS (31DEC11). AIPS documentation : Subsection
      E.5 of the AIPS cookbook (Appendix E : Special Considerations for
      JVLA data calibration and imaging in
      AIPS\ ` <https://casa.nrao.edu/casadocs-devel/docs/cookbook/casa_cookbook004.html#note3>`__\ ,\ http://www.aips.nrao.edu/cook.html#CEE\ )

      In RFlag, the data is iterated-through in chunks of time,
      statistics are accumulated across time-chunks, thresholds are
      calculated at the end, and applied during a second pass through
      the dataset.

      The CASA implementation also optionally allows a single-pass
      operation where statistics and thresholds are computed and also
      used for flagging, within each time-chunk (defined by ’ntime’ and
      ’combinescans’).

      For each chunk, calculate local statistics, and apply flags based
      on user supplied (or auto-calculated) thresholds.

      As of CASA 4.6 the data can also be pre-averaged over the
      selectedspwchannel ranges by settingchannelavg=Trueandchanbinto
      the desired bin (in number of channels), or time averaged over the
      selected time ranges by settingtimeavg=Trueandtimebinto the
      desired time range (in seconds). This averaging is independent
      from the rflag time/channel sliding window, as it performs not
      only an average but also a binning operation (so there is no data
      overlap between adjacent bins), and allows to specify independent
      time/channel bins.

      1. Time analysis (for each channel)

         a. Calculate local rms of real and imag visibilities, within a
            sliding time window
         b. Calculate the median rms across time windows, deviations of
            local rms from this median, and the median deviation
         c. Flag if local rms is larger than timedevscale x (medianRMS +
            medianDev)

      2. Spectral analysis (for each time)

         a. Calculate avg of real and imag visibilities and their rms
            across channels
         b. Calculate the deviation of each channel from this avg, and
            the median-deviation
         c. Flag if deviation is larger than freqdevscale x medianDev

      Theextendflagsparameter will clean up small portions of data
      between flagged data points along time and/or frequency when more
      than 50% of all timeranges or 80% of all channels are already
      flagged. It will also extend the flags to the other polarizations.
      Alternatively,mode=’extend’can be used.

      Some examples (see figure below):

      1. Calculate thresholds automatically per scan, and use them to
         find flags. Specify scale-factor for time-analysis thresholds,
         use default for frequency.

         .. container:: casa-input-box

            | #In CASA:
            | CASA<1>: flagdata('my.ms',
              mode='rflag',spw='9',timedevscale=4.0)

      2. Supply noise-estimates to be used with default scale-factors.

         .. container:: casa-input-box

            | #In CASA:
            | CASA<1>: flagdata(vis='my.ms', mode='rflag', spw='9',
              timedev=0.1, freqdev=0.5);

         Two-passes. This replicates the usage pattern in AIPS.

         -  The first pass saves commands in an output text files, with
            auto-calculated thresholds. Thresholds are returned from
            rflag only when action='calculate' (calc-only mode). The
            user can edit this file before doing the second pass, but
            the python-dictionary structure must be preserved.
         -  The second pass applies these commands (action='apply').

            .. container:: casa-input-box

               | #In CASA:
               | CASA<1>: flagdata(vis='my.ms', mode='rflag',
                 spw='9,10', timedev='tdevfile.txt',
                 freqdev='fdevfile.txt', action='calculate');
               | CASA<2>: flagdata(vis='my.ms', mode='rflag',
                 spw='9,10', timedev='tdevfile.txt',
                 freqdev='fdevfile.txt', action='apply');

            .. container:: center

               --------------

            .. container:: center

               .. container:: caption

                  +-----------------------------------+
                  | Example ofrflagon narrow-band RFI |
                  +-----------------------------------+

      ..

         .. container:: center

            --------------

         .. container:: center

            .. container:: center

                

            .. container:: center

                

      .. rubric:: Extend
         :name: sec188
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'extend' # Flagging mode
           (list/manual/clip/shadow/quack/el
         | # evation/tfcrop/rflag/extend/unflag/summary)
         | field = '' # Field names or field index numbers: '' ==> all,
         | # field='0~2,3C286'
         | spw = '' # Spectral-window/frequency/channel: '' ==> all,
         | # spw='0:17~19'
         | antenna = '' # Antenna/baselines: '' ==> all, antenna
         | # ='3,VA04'
         | timerange = '' # Time range: '' ==>
         | # all,timerange='09:14:0~09:54:0'
         | correlation = '' # Correlation: '' ==> all,
           correlation='XX,YY'
         | scan = '' # Scan numbers: '' ==> all
         | intent = '' # Observation intent: '' ==> all,
         | # intent='CAL*POINT*'
         | array = '' # (Sub)array numbers: '' ==> all
         | uvrange = '' # UV range: '' ==> all; uvrange ='0~100klambda',
         | # default units=meters
         | observation = '' # Observation ID: '' ==> all
         | feed = '' # Multi-feed numbers: Not yet implemented
         | ntime = 'scan' # Time-range to use for each chunk (in seconds
           or
         | # minutes)
         | combinescans = False # Accumulate data across scans.
         | extendpols = True # If any correlation is flagged, flag all
         | # correlations
         | growtime = 50.0 # Flag all 'ntime' integrations if more than
           X%
         | # of the timerange is flagged (0-100)
         | growfreq = 50.0 # Flag all selected channels if more than X%
           of
         | # the frequency range is flagged(0-100)
         | growaround = False # Flag data based on surrounding flags
         | flagneartime = False # Flag one timestep before and after a
           flagged
         | # one (True/False)
         | flagnearfreq = False # Flag one channel before and after a
           flagged one
         | # (True/False)

      Although the modestfcropandrflagalready haveextendflagsparameters,
      some autoflagging algorithms may still leave small islands of
      unflagged data behind, data that are surrounded by flagged
      visibilities in the time-frequency space. Although the algorithm
      may deem these visibilities as good ones, they are frequently
      affected by low-level RFI that spills from the adjacent, flagged
      points and one may wish to clean those up.

      ntimespecifies the time ranges over which to clean up,
      e.g.’1.5min’or’scan’which checks on all data within a scan. To
      span time ranges larger than scans, one can setcombinescanstoTrue.

      extendpols=Truewould extend all flags to all polarization products
      when at least one of them is flagged.

      growtimeflags the entire time range for a flagged channel, when a
      certain fraction of flagged time intervals is exceeded.

      growfreqis similar but extends the flags in frequency when a given
      fraction of channels is already flagged.

      growaroundchecks for flagged data points in the time-frequency
      domain that neighbor a datum. The threshold is four data points.
      If more surrounding points are flagged, the central datum will be
      flagged, too.

      flagneartimeflags adjacent data points along the time axis, around
      a flagged datum

      flagnearfreqflags neighboring channels.

      .. container:: center

         --------------

      .. container:: center

         .. container:: caption

            +----------------------------------------------------------------------+
            | This screenshot represents a run where ’tfcrop’ was run only on      |
            | ’ABS_RR’ (top row) and followed by an extension along time and       |
            | correlations (bottom row).                                           |
            +----------------------------------------------------------------------+

      .. rubric::  
         :name: section-5
         :class: subsubsection

      .. rubric:: Unflag
         :name: sec190
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'unflag' # Flagging mode
           (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary
         | # )
         | field = '' # Field names or field index numbers: ''==>all,
         | # field='0~2,3C286'
         | spw = '' # spectral-window/frequency/channel
         | antenna = 'ea01' # antenna/baselines: ''==>all, antenna
         | # ='3,VA04'
         | timerange = '' # time range:
         | # ''==>all,timerange='09:14:0~09:54:0'
         | correlation = '' # Select data based on correlation
         | scan = '' # scan numbers: ''==>all
         | intent = '' # Select data based on observation intent:
         | # ''==>all
         | feed = '' # multi-feed numbers: Not yet implemented
         | array = '' # (sub)array numbers: ''==>all
         | uvrange = '' # uv range: ''==>all; uvrange ='0~100klambda',
         | # default units=meters
         | observation = '' # Select data based on observation ID:
           ''==>all

      The selection data will be unflagged.

      .. rubric::  
         :name: section-6
         :class: subsubsection

      .. rubric:: Summary
         :name: sec191
         :class: subsubsection

      .. container:: casa-input-box

         | mode = 'summary' # Flagging mode
           (list/manual/clip/shadow/quack/
         | # elevation/tfcrop/rflag/extend/unflag/summary
         | # )
         | ...
         | minrel = 0.0 # minimum number of flags (relative)
         | maxrel = 1.0 # maximum number of flags (relative)
         | minabs = 0 # minimum number of flags (absolute)
         | maxabs = -1 # maximum number of flags (absolute). Use a
         | # negative value to indicate infinity.
         | spwchan = False # Print summary of channels per spw
         | spwcorr = False # Print summary of correlation per spw
         | basecnt = False # Print summary counts per baseline

      This mode reports the number of rows and data points that are
      flagged. The selection of reported points can be restricted (see
      inline help for details).

      mode=’summary’can also report back a dictionary if the task is run
      as

      .. container:: casa-input-box

         | #In CASA:
         | CASA<1>: s = flagdata(..., mode='summary')

      with a variable assigned, here ’s’.

.. container:: section
   :name: viewlet-below-content-body
