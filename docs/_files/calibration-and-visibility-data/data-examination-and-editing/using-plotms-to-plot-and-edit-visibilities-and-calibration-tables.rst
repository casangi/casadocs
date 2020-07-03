.. container::
   :name: viewlet-above-content-title

Plot/Edit using plotms
======================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Using plotms to plot and edit visibilities and calibration tables

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      plotms is a GUI-style plotter, based on Qt, for creating X-Y plots
      of visibility data and calibration tables. It can either be
      started as a task within CASA or from outside CASA (type
      casaplotms on the command line).  This task also provides editing
      capability.

      plotms was originally intended to plot MeasurementSets (the "ms"
      in "plotms"), but has been extended to include calibration
      tables.  Supported cal table types include B Jones, B TSYS,
      EGainCurve, F Jones, G Jones, K Jones, Kcross Jones, KAntPos, T
      Jones, TOpac, Xf Jones, A Mueller, BPOLY, and GSPLINE.  Some
      options (axis choice, averaging, channel selection) do not apply
      to calibration tables or have not been implemented yet.  Other
      options, such as calibration axes, do not apply to
      MeasurementSets. For simplicity, this document primarily addresses
      plotting MeasurementSets.

      The current inputs and default values for plotms include:

      .. container:: casa-input-box

         plotms :: A plotter/interactive flagger for visibility data.
         vis                 =         ''        #  input MS (or
         CalTable) (blank for none)
         gridrows            =          1        #  Number of subplot
         rows (default 1).    
         gridcols            =          1        #  Number of subplot
         columns (default 1).
         rowindex            =          0        #  Row location of the
         plot (0-based, default 0)
         colindex            =          0        #  Column location of
         the plot (0-based, default 0)
         plotindex           =          0        #  Index to address a
         subplot (0-based, default 0)
         xaxis               =         ''        #  plot x-axis (blank
         for default/current)         
         yaxis               =         ''        #  plot y-axis (blank
         for default/current)         
         selectdata          =       True        #  data selection
         parameters                       
              field          =         ''        #  field names or field
         index numbers (blank for all)
              spw            =         ''        #  spectral
         windows:channels (blank for all)
              timerange      =         ''        #  time range (blank
         for all)
              uvrange        =         ''        #  uv range (blank for
         all)
              antenna        =         ''        #  antenna/baselines
         (blank for all)
              scan           =         ''        #  scan numbers (blank
         for all)
              correlation    =         ''        #  correlations (blank
         for all)
              array          =         ''        #  (sub)array numbers
         (blank for all)
              observation    =         ''        #  observation ID(s)
         (blank for all)
              intent         =         ''        #  observing intent
         (blank for all)
              feed           =         ''        #  Select feed (blank
         for all)
              msselect       =         ''        #  MS selection (blank
         for all)
         averagedata         =       True        #  data averaging
         parameters
              avgchannel     =         ''        #  average over
         channel?  (blank = False, otherwise
                                                 #   value in channels)
              avgtime        =         ''        #  average over time?
         (blank = False, other value in
                                                 #   seconds)
              avgscan        =      False        #  only valid if time
         averaging is turned on.  average
                                                 #   over scans?
              avgfield       =      False        #  only valid if time
         averaging is turned on.  average
                                                 #   over fields?
              avgbaseline    =      False        #  average over all
         baselines?  (mutually exclusive
                                                 #   with avgantenna)
              avgantenna     =      False        #  average by
         per-antenna?  (mutually exclusive with
                                                 #   avgbaseline)
              avgspw         =      False        #  average over all
         spectral windows?
              scalar         =      False        #  Do scalar averaging?
         transform           =      False        #  transform data in
         various ways?
         extendflag          =      False        #  have flagging extend
         to other data points?
         iteraxis            =         ''        #  the axis over which
         to iterate
         customsymbol        =      False        #  set a custom
         symbol(s) for unflagged points
         coloraxis           =         ''        #  selects which data
         to use for colorizing
         customflaggedsymbol =      False        #  set a custom plot
         symbol for flagged points
         xconnector          =          ''       #  Set connector for
         data points
                                                 #   (blank="none";
         "line","step")
         plotrange           =         []        #  plot axes ranges:
         [xmin,xmax,ymin,ymax]
         title               =         ''        #  Title written along
         top of plot
         titlefont           =          0        #  Font for plot title
         xlabel              =         ''        #  Text for horizontal
         axis. Blank for default.
         xaxisfont           =          0        #  Font for plot x-axis
         ylabel              =         ''        #  Text for vertical
         axis. Blank for default.
         yaxisfont           =          0        #  Font for plot
         y-axis.
         showmajorgrid       =      False        #  Show major grid
         lines (horiz and vert.)
         showminorgrid       =      False        #  Show minor grid
         lines (horiz and vert.)
         showlegend          =      False        #  Show a legend on the
         plot.
         plotfile            =         ''        #  Name of plot file to
         save automatically.
         showgui             =       True        #  Show GUI
              clearplots     =       True        #  Remove any existing
         plots so new ones can replace
                                                 #   them.
         callib              =       ['']        #  Calibration library
         string or filename for on-the-
                                                 #   fly calibration.
         headeritems         =         ''        # Comma-separated list
         of pre-defined
                                                 #   page header items.
         showatm             =     False         # Compute and overlay
         the atmospheric
                                                 #   transmission curve.
         showtsky            =     False         # Compute and overlay
         the sky
                                                 #   temperature curve.
         showimage           =     False         # Compute and overlay
         the image
                                                 #   sideband curve.

      Note that when some parameters are set or are True, their
      subparameters are displayed by inp( ).  By default, selectdata,
      averagedata, and showgui are True and their subparameters are
      shown above.  Other parameters with subparameters include:

      .. container:: casa-input-box

         xaxis               =     'real'        #  plot x-axis (blank
         for default/current)         
              xdatacolumn    =         ''        #  data column to use
         for x-axis (blank for        
                                                 #  
         default/current)                               
         yaxis               =     'imag'        #  plot y-axis (blank
         for default/current)
              ydatacolumn    =         ''        #  data column to use
         for y-axis (blank for
                                                 #  default/current)
              yaxislocation  =      'left'       #  yaxis is to the left
         of the plot
         transform           =       True        #  transform data in
         various ways?
              freqframe      =         ''        #  the frame in which
         to render frequency and velocity
                                                 #   axes
              restfreq       =         ''        #  Rest frequency to
         use for velocity conversions
              veldef         =    'RADIO'        #  the definition in
         which to render velocity
              shift          = [0.0, 0.0]        #  Adjust phases by
         this approximate phase center
                                                 #   shift [dx,dy]
         (arcsec)
         extendflag          =       True        #  have flagging extend
         to other data points?
              extcorr        =      False        #  extend flags based
         on correlation?
              extchannel     =      False        #  extend flags based
         on channel?
         iteraxis            = 'baseline'        #  the axis over which
         to iterate
              xselfscale     =      False        #  When true, iterated
         plots have a common
                                                 #   x-axis range
         (scale).
              yselfscale     =      False        #  When true, iterated
         plots have a common
                                                 #   y-axis range
         (scale).
              xsharedaxis    =      False        #  Enables iterated
         plots on a grid to share a
                                                 #  common external
         x-axis per column. Must also set 
                                                 #  xselfscale=True and
         gridrows>1.
              ysharedaxis    =      False        #  Enables iterated
         plots on a grid to share a 
                                                 #  common external
         y-axis per row. Must also set 
                                                 #  yselfscale=True and
         gridcols>1.
         customsymbol        =       True        #  set a custom
         symbol(s) for unflagged points
              symbolshape    = 'autoscaling'     #  shape of plotted
         unflagged symbols
              symbolsize     =          2        #  size of plotted
         unflagged symbols
              symbolcolor    =   '0000ff'        #  color of plotted
         unflagged symbols
              symbolfill     =     'fill'        #  fill type of plotted
         unflagged symbols
              symboloutline  =      False        #  selects outlining
         plotted unflagged points
         customflaggedsymbol =       True        #  set a custom plot
         symbol for flagged points
              flaggedsymbolshape = 'nosymbol'    #  shape of plotted
         flagged symbols
              flaggedsymbolsize =          2     #  size of plotted
         flagged symbols
              flaggedsymbolcolor =   'ff0000'    #  color of plotted
         flagged symbols
              flaggedsymbolfill =     'fill'     #  fill type of plotted
         flagged symbols
              flaggedsymboloutline =      False  #  selects outlining
         plotted flagged points
         showmajorgrid       =       True        #  Show major grid
         lines (horiz and vert.)
              majorwidth     =          0        #  Line width in pixels
         of major grid lines
              majorstyle     =         ''        #  Major grid line
         style: solid dash dot none
              majorcolor     =         ''        #  Color as name or hex
         code of major grid lines
         showminorgrid       =       True        #  Show minor grid
         lines (horiz and vert.)
              minorwidth     =          0        #  Line width in pixels
         of minor grid lines
              minorstyle     =         ''        #  Minor grid line
         style: solid dash dot none
              minorcolor     =         ''        #  Color as name or hex
         code of minor grid lines
         plotfile            = 'plot.jpg'        #  Name of plot file to
         save automatically.
              expformat      =         ''        #  Export format type
         (jpg, png, ps, pdf, txt), if not
                                                 #   provided, plotfile
         extension will be used.
              verbose        =      True         #  Include metadata in
         text export.
              exprange       =         ''        #  Export all iteration
         plots or only the current one.
              highres        =      False        #  Use high resolution
              dpi            =         -1        #  DPI of exported plot
              width          =         -1        #  Width of exported
         plot
              height         =         -1        #  Height of exported
         plot
              overwrite      =      False        #  Overwrite plot file
         if it already exists?

      Note that if the vis parameter is set to the name of a
      MeasurementSet here, when you start plotms the entire
      MeasurementSet will be plotted, which can be time consuming.  You
      may want to set selection or averaging parameters first.

      To start a "blank" plotms window then enter your selections
      interactively in the GUI, use these commands:

      .. container:: casa-input-box

         default plotms
         plotms

      Alternatively, they can be specified as task parameters in a
      plotms call, for scripting:

      .. container:: casa-input-box

         plotms(vis1, yaxis='phase', ydatacolumn='corrected',
         xaxis='frequency', coloraxis='spw', antenna='1', spw='0:3~10',
         corr='RR', avgtime='1e8', plotfile='vis1.jpg')

      Note that subsequent plotms calls will return any unspecified
      parameters in that call to their default values.  See also
      the\ `Examples <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_plotms/examples>`__\ tab
      in the plotms task for plotms calls using many of the parameters.

      The plotms GUI will be described in the following sections, along
      with the corresponding parameters for the task interface or
      scripting.  For non-interactive scripting, set showgui=False and
      export the plot into an image specified by plotfile.

      --------------

      .. rubric:: 1. The Plot Tab
         :name: the-plot-tab

      .. rubric:: 1.1 Loading, Selecting, and Averaging Data: the Plot
         Data Tab
         :name: loading-selecting-and-averaging-data-the-plot-data-tab

      |image1|

      +---------+-----------------------------------------------------------+
      | Type    | Figure 1                                                  |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | The plotms window starts on the *Plot > Data* tab.  No    |
      |         | parameters have been set.                                 |
      +---------+-----------------------------------------------------------+

      .. rubric:: 1.1.1 File Selection
         :name: file-selection

      When plotms is first started, by default it will display the Plot
      tab (as chosen from the tabs at the top of the plotms window) and
      its Data subtab (as chosen from the tabs on the left side) as
      shown in Figure 1. First, a MeasurementSet or calibration table
      should be loaded by clicking on Browse in the File section and
      selecting a MeasurementSet directory (just select the directory
      itself; do not descend into it).

      A plot can now be made of the MeasurementSet by clicking on the
      Plot button, but you may want to set selection or averaging
      parameters first rather than plot the entire dataset.  By default,
      plotms will plot Amplitude versus Time for a MeasurementSet; see
      this section on\ \ `selecting
      axes <#1-3-1-selecting-axes>`__\ \ for axis options.  The default
      axes change for calibration tables depending on the table type. 
      plotms self-scales axes and the symbol size. For a very large
      range, this can hide points close to zero; see the sections below
      for information on setting\ `axes
      ranges <#1-3-4-axes-ranges>`__\ and\ `symbol
      sizes <#1-6-2-customizing-your-symbols>`__\ .

      The plotms task parameter for file selection is vis.

      .. rubric::  1.1.2 Data Selection
         :name: data-selection

      The options for data selection are:

      -  field
      -  spw
      -  timerange
      -  uvrange
      -  antenna
      -  scan
      -  corr (correlated polarizations)
      -  array
      -  observation
      -  intent
      -  feed
      -  msselect

      Note that, unlike when setting data selection parameters from the
      CASA command line, no quotation marks are needed around strings in
      the GUI.  For more information on data selection strings, see the
      documentation\ `here <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__\ . 
      To view information about your data in order to make your
      selection, see
      the\ `Summary <#5-3-summary-menu--information-about-your-dataset>`__\ section
      below or use the listobs task.

      Calibration table selection differs from MeasurementSet
      selection.  The antenna selection selects baselines which contain
      the selected antennas in MeasurementSets, but selects antenna1
      only for calibration tables.  Spectral window selection (spw) is
      used to select spw only (channel selection is ignored) in
      calibration tables.  corr may be used to select cal table
      polarizations, including "/" for a ratio plot.

      The plotms parameter for data selection is selectdata (default is
      True, but no selection occurs unless one or more subparameters is
      set).  Its subparameters include field, spw, timerange. uvrange,
      antenna, scan, correlation, array, observation, intent, feed, and
      msselect.  These should be set to string values.

      .. rubric:: 1.1.3 Averaging Data
         :name: averaging-data

      plotms enables averaging of the data in order to increase
      signal-to-noise of the plotted points or to increase plotting
      speed.  Averaging is currently not supported for

      -  calibration tables
      -  Ant-Ra, Ant\ -Dec axes

      and will result in a warning in the log, then the unaveraged data
      will be plotted.

      The options for averaging in the Plot > Data tab include:

      -  channel
      -  time (optionally over scans or fields)
      -  all baselines or per antenna
      -  all spectral windows
      -  vector (default) or scalar

      The box next to a given averaging mode needs to be checked for
      that averaging to take effect.  The Weight and Sigma axes are not
      supported in some averaging modes.  Note that the "average weight"
      is actually the weight sum accumulated when performing the
      average; i.e., the net weight of a weighted-averaged datum is the
      sum of the weights going into the average.

      When averaging, plotms will prefer unflagged data.  If an
      averaging bin contains any unflagged data at all, only the average
      of the unflagged will be shown. For averaging bins that contain
      only unflagged data, the average of that unflagged data will be
      shown. When flagging on a plot of averaged data, the flags will be
      applied to the unaveraged data in the MS.

      The plotms task parameter for averaging is averagedata (default is
      True, but no averaging occurs unless one or more subparameters are
      set).  It subparameters include avgchannel and avgtime (set to a
      string value in channels or seconds, default ""), and boolean
      parameters avgscan, avgfield, avgbaseline, avgantenna, avgspw, and
      scalar (True/False, default False).  Invalid combinations of
      averaging will result in an error message (e.g. avgbaseline=True,
      avgantenna=True) or will be ignored (e.g. avgscan=True but avgtime
      has not been set).

      .. rubric:: Channel Averaging:
         :name: channel-averaging

      For example, to average n channels together, the user would click
      on the box next to Channel so that an “X” appears in it, and then
      type the number n in the empty box. When the user next clicks on
      Plot, every n channels will then be averaged together and plotted
      against the average channel numbers. The total number of channels
      plotted will be decreased by a factor of n.

      Warning: If a complex channel selection is made e.g. of continuum
      in the presense of multiple lines, channel averaging is unlikely
      to produce a meaningful plot.

      .. rubric:: Time Averaging:
         :name: time-averaging

      Time averaging is a little trickier, as it is controlled by three
      fields. If the checkbox next to Time is checked, a blank box with
      units of seconds will become active, along with two additional
      checkboxes: Scan and Field. If averaging is desired over a
      relatively short interval (say, 30 seconds, shorter than the scan
      length), a number can simply be entered into the blank box and,
      when the data are replotted, the data will be time averaged.
      Clicking on the Scan or Field checkbox in this case will have no
      impact on the time averaging.  These checkboxes become relevant if
      averaging over a relatively long time—say the entire observation,
      which consists of multiple scans—is desired. Regardless of how
      large a number is set in the Time averaging box, only data within
      individual scans will be averaged together. In order to average
      data across scan boundaries, the Scan checkbox must be checked and
      the data replotted. Finally, clicking on the Field checkbox
      enables the averaging of multiple fields together in time.

      .. rubric:: Averaging All Baselines/Per Antenna:
         :name: averaging-all-baselinesper-antenna

      Clicking on the All Baselines checkbox will average all baselines
      in the array together. Alternatively, the Per Antenna box may be
      checked, which will average all baselines for a given antenna
      together. In this case, all baselines are represented twice;
      baseline 3-24 will contribute to the averages for both antenna 3
      and antenna 24. This can produce some rather strange-looking plots
      if the user also selects on antenna—say, if the user requests to
      plot only antenna 0 and then averages Per Antenna, In this case,
      an average of all baselines including antenna 0 will be plotted,
      but each individual baseline including antenna 0 will also be
      plotted (because the presence of baselines 0-1, 0-2, 0-3,
      etc. trigger Per Antenna averaging to compute averages for
      antennae 1, 2, 3, etc. Therefore, baseline 0-1 will contribute to
      the average for antenna 0, but it will also singlehandedly be the
      average for antenna 1.)  These averaging modes currently do not
      support the Weight and Sigma axes.

      .. rubric:: Averaging All Spectral Windows:
         :name: averaging-all-spectral-windows

      Spectral windows can be averaged together by checking the box next
      to All Spectral Windows. This will result in, for a given channel
      n, all channels n from the individual spectral windows being
      averaged together.  This averaging mode currently does not support
      the Weight and Sigma axes.

      .. rubric:: Vector/Scalar Averaging:
         :name: vectorscalar-averaging

      Finally, the default mode is vector averaging, where the complex
      average is formed by averaging the real and imaginary parts of the
      relevant visibilities. If Scalar is chosen, then the amplitude of
      the average is formed by a scalar average of the individual
      visibility amplitudes.

      .. rubric:: 1.1.4 A Brief Note Regarding plotms Memory Usage
         :name: a-brief-note-regarding-plotms-memory-usage

      In order to provide a wide range of flexible interactive plotting
      options while minimizing the I/O burden and speeding up the
      plotting, plotms caches the data values for the plot (along with a
      subset of relevant meta-info) in as efficient a manner as
      possible.  Sometimes, however, the data changes on disk, for
      example when other data processing tasks are applied. To force
      plotms to reload the data, check the Reload box next to the Plot
      button or press the SHIFT key while clicking the Plot button.

      For plots of large numbers of points, the total memory requirement
      can be quite large. plotms attempts to predict the memory it will
      require (typically 5 or 6 bytes per plotted point when only one
      axis is a data axis, depending upon the data shapes involved), and
      will complain if it believes there is insufficient memory to
      support the requested plot. For most practical interactive
      purposes (plots that load and draw in less than a few or a few 10s
      of minutes), there is usually not a problem on typical modern
      workstations.  Attempts to plot large datasets on small laptops
      might be more likely to encounter problems here.

      | The absolute upper limit on the number of simultaneously plotted
        points is currently set by the ability to index the points in
        the cache. For modern 64 bit machines, this is about 4.29
        billion points (requiring around 25GB of memory). Such plots are
        not especially useful interactively, since the I/O and draw
        become prohibitive.
      | In general, it is usually most efficient to plot data in modest
        chunks of no more than a few hundred million points or less,
        either using selection or averaging. Note that all iterations
        are (currently) cached simultaneously for iterated plots, so
        iteration is not a way to manage memory use. A few hundred
        million points tends to be the practical limit of interactive
        plotms use with respect to information content and utility in
        the resulting plots, especially when you consider the number of
        available pixels on your screen.

      --------------

      .. rubric:: 1.2 On-The-Fly Calibration: the Plot Calibration Tab
         :name: on-the-fly-calibration-the-plot-calibration-tab

      +---------+-----------------------------------------------------------+
      | Type    | Figure 2                                                  |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | The plotms Calibration tab.  This MeasurementSet has no   |
      |         | *CORRECTED_DATA* column. A calibration library file was   |
      |         | selected with the file browser and applied on the fly.    |
      +---------+-----------------------------------------------------------+

      One can apply calibration tables to the uncalibrated data on the
      fly, i.e. without a run of applycal beforehand, by specifying a
      calibration library and selecting the corrected Data Column for
      the plotted axes.  See the\ `Cal Library
      Syntax <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/cal-library-syntax>`__\ documentation
      for more information on specifying calibration in a string or
      file.

      The Calibration tab on the left hand side contains a field to
      specify a calibration library file, or use Browse to open a file
      selection dialog.  You can also specify the calibration library
      commands directly in a string.  There is a switch to apply the
      calibration library to produce the corrected data (Calibration On)
      or to show an existing CORRECTED_DATA column (Calibration Off). 
      If the corrected Data Column is requested but the column is not
      present in the MS and the calibration library is not set or
      enabled, plotms issues a warning and plots the DATA column
      instead.

      The plotms task parameter ’callib’ can be used to provide a
      calibration library file or a string containing the cal library
      commands.  It is enabled by default when the parameter is set.

      --------------

      .. rubric:: 1.3 Selecting Plot Axes: The Plot Axes Tab
         :name: selecting-plot-axes-the-plot-axes-tab

      |image2|

       

      +---------+-----------------------------------------------------------+
      | Type    | Figure 3                                                  |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | The plotms Plot > Axes tab, used here to make a plot of   |
      |         | Amp vs. Channel.                                          |
      +---------+-----------------------------------------------------------+

      .. container:: center

         --------------

      .. rubric:: 1.3.1 Selecting Axes
         :name: selecting-axes

      The X and Y axes of a plot are selected by clicking on the Plot >
      Axes tab and choosing an entry from the drop-down menus below X
      Axis and Y Axis. The axes are grouped by type and listed in this
      order:

      -  MeasurementSet metadata:

         -  Scan — The scan number, as listed by listobs or the plotms
            summary
         -  Field — The field number, as listed by listobs or the plotms
            summary
         -  Time —\ The time at which the visibility was observed, given
            in terms of calendar year (yyyy/mm/dd/hh:mm:ss.s).
         -  Interval — The integration time in seconds.
         -  Spw — The spectral window number. The characteristics of
            each spectral window are listed in listobs or the plotms
            summary.
         -  Channel — The spectral channel number.
         -  Frequency — Frequency in units of GHz. The frame for the
            frequency (e.g., topocentric, barycentric, LSRK) can be set
            in the Plots > Transform tab.
         -  Velocity — Velocity in units of km s−1, as defined by the
            Frame, Velocity Defn, and Rest Freq parameters in the Plots
            > Transform tab.
         -  Corr — Correlations which have been assigned integer IDs,
            including RR (5), RL (6), LR (7), LL (8), XX (9), XY (10),
            YX (11), and YY (12).  The axis values are these IDs, as
            listed by listobs or the plotms summary.
         -  Antenna1 — The first antenna in a baseline pair; for
            example, for baseline 2-4, Antenna1= 2. Antennae are
            numbered according to the antenna IDs listed in listobs or
            the plotms summary.
         -  Antenna2 — The second antenna in a baseline pair; for
            baseline 2-4, Antenna2 = 4. Antennae are numbered according
            to the antenna IDs listed in listobs or the plotms summary.
         -  Antenna — Antenna ID for plotting antenna-based quantities.
            Antennae are numbered according to the antenna IDs listed in
            listobs or the plotms summary.
         -  Baseline — The baseline number.
         -  Row — The MS data row number. A row number corresponds to a
            unique timestamp, baseline, and spectral window in the
            MeasurementSet.
         -  Observation — The observation ID (index)
         -  Intent — The intent ID (index)
         -  Feed1 — The first feed number, most useful for single-dish
            data.
         -  Feed2 — The second feed number, most useful for single-dish
            data.

      -  Visibility values and flags:

         -  Amp — Data amplitudes in units which are proportional to
            Jansky (for data which are fully calibrated, the units
            should be in Jy).
         -  Phase — Data phases in units of degrees.
         -  Real and Imag — The real and imaginary parts of the
            visibility in units which are proportional to Jansky (for
            data which are fully calibrated, the units should be Jy).
         -  Wt and Wt*Amp — the weight of the visibility and the product
            of the weight and the amplitude.
         -  WtSp — WEIGHT_SPECTRUM column, i.e. a weight per channel.
         -  Sigma — the SIGMA column of the visibilities
         -  SigmaSp — SIGMA_SPECTRUM column, i.e. a sigma per channel
         -  Flag — Data which are flagged have Flag = 1, whereas
            unflagged data are set to Flag = 0.  Note that, to display
            flagged data, you will have to click on the Plots > Display
            tab and choose a Flagged Points Symbol.
         -  FlagRow — In some tasks, if a whole data row is flagged,
            then FlagRow will be set to 1 for that row. Unflagged rows
            have FlagRow = 0. However, note that some tasks (like
            plotms) may flag a row, but not set FlagRow = 1. It is
            probably better to plot Flag than FlagRow for most
            applications.

      -  Observational geometry:

         -  UVdist — Projected baseline separations in units of meters.
            Note that UVDist is not a function of frequency.

         -  UVwave — Projected baseline separations in units of the
            observing wavelength (lambda, not kilolambda). UVwave is a
            function of frequency, and therefore, there will be a
            different data point for each frequency channel.

         -  U, V, and W — u, v, and w in units of meters.

         -  Uwave, Vwave, and Wwave — u, v, and w in units of
            wavelengths lambda.

         -  Azimuth and Ant-Azimuth — Azimuth in units of degrees.
            Azimuth plots a fiducial value for the entire array, while
            Ant-Azimuth plots the azimuth for each individual antenna
            (their azimuths will differ depending on each antenna's
            longitude, latitude, and elevation).

         -  

            .. container::

               Elevation and Ant-Elevation — Elevation in units of
               degrees. Elevation is a representative value for the
               entire array, while Ant-Elevation is the elevation for
               each individual antenna (their elevations will differ
               depending on each antenna's longitude, latitude, and
               elevation).

         -  Ant-Ra and Ant-Dec — Longitude and latitude of the direction
            to which the first antenna of a baseline points at
            data-taking timestamps.

         -  

            .. container::

               HourAngle — Hour angle in units of hours. This is a
               fiducial value for the entire array.

         -  ParAngle and Ant-ParAng — Parallactic angle in units of
            degrees. ParAngle is the fiducial parallactic angle for all
            antennae in the array, while Ant-ParAng plots the
            parallactic angle for each individual antenna (their
            parallactic angles will differ depending on each antenna's
            longitude, latitude, and elevation).

      -  Calibration:

         -  GainAmp, GainPhase, GainReal, GainImag — the amplitude,
            phase, real and imaginary part of the calibration tables for
            regular complex gain tables.
         -  Delay — The delay of a delay calibration table.
         -  SwPower — Switched Power values for VLA switched power
            calibration tables.
         -  Tsys — Tsys for Tsys calibration tables.
         -  Opac — Opacity values of a Opacity calibration table.
         -  SNR — Signal-to-Noise Ratio of a calibration table.
         -  TEC — Total Electron Content of an ionosphere correction
            calibration table.

      -  **Ephemeris:**

         -  **Radial Velocity**\  —for an ephemeris source, in km/s.
         -  **Distance (rho)**\  —for an ephemeris source, in km.

      -  

      If the data axis selected from the drop-down menu is already
      stored in the cache (therefore implying that plotting will proceed
      relatively quickly), an “X” will appear in the checkbox next to
      Cached.   To reload the data from disk, the Reload checkmark
      should be set at the bottom of this display.

      The plotms task parameters used to select the axes are xaxis and
      yaxis.  Valid options include 'scan', 'field', 'time', 'interval',
      'spw', 'chan' (or 'channel'), 'freq' (or 'frequency'), 'vel' (or
      'velocity'), 'corr' (or 'correlation), 'ant1' (or 'antenna1'),
      'ant2' (or 'antenna2'), 'baseline', 'row', 'observation',
      'intent', 'feed1', 'feed2', 'amp' (or 'amplitude'), 'phase',
      'real', 'imag', 'wt' (or 'weight'), 'wtsp' (or 'weightspectrum'),
      'flag', 'flagrow', 'uvdist', 'uvwave' (or 'uvdistl'), 'u', 'v',
      'w', 'uwave', 'vwave', 'wwave', 'azimuth', 'elevation', 'hourang'
      (or 'hourangle'), 'parang' (or 'parangle'), 'ant' (or 'antenna'),
      'ant-azimuth', 'ant-elevation', 'ant-ra', 'ant-dec', 'ant-parang'
      (or 'ant-parangle'), 'gainamp' (or 'gamp'), 'gainphase' (or
      'gphase'), 'gainreal' (or 'greal'), 'gainimag' (or 'gimag'),
      'delay' (or 'del'), 'swpower' (or 'swp' or 'spgain'), 'tsys',
      'opacity' (or 'opac'), 'snr', 'tec', 'radialvelocity', 'distance'
      (or 'rho').

      When left as the default empty strings (""), the axes for a
      MeasurementSet will be Amp vs. Time.  The default axes for a
      calibration table depend on the type.

      .. rubric:: 1.3.2 Setting Axes Parameters
         :name: setting-axes-parameters

      .. rubric:: 1.3.2.1 Data Columns
         :name: data-columns

      For relevant data axes like Amp and Phase, the user will be
      presented with the option to plot raw data or calibrated data.
      This can be selected via a Data Column drop-down menu, located
      directly under the drop-down menu for X Axis or Y Axis selection.
      To plot raw data, select “data”; to plot calibrated data, select
      “corrected”. Note that this choice will only have an impact on a
      plot if a calibration table has been applied to the MeasurementSet
      or a calibration library is set and enabled.

      If a data model is present in the MeasurementSet (e.g., created by
      setjy, clean, or ft), it can be plotted by selecting “model” from
      the Data Column menu. For MeasurementSets with float data instead
      of complex data, common in singledish datasets, select the "float"
      datacolumn.

      Residuals can be plotted via "corrected-model_vector",
      "corrected-model_scalar", "data-model_vector", data-model_scalar",
      "corrected/model_vector", "corrected/model_scalar",
      "data/model_vector", and "data/model_scalar".  The vector and
      scalar options distinguish between versions where values like amp,
      phase, etc. are calculated before (scalar) or after (vector) the
      subtraction or division.

      The plotms task parameters used to select the data columns are
      xdatacolumn and ydatacolumn.  Valid options include 'data',
      corrected', 'model', 'float', 'corrected-model' (vector implied),
      'corrected-model_vector', 'corrected-model_scalar', 'data-model'
      (vector implied), 'data-model_vector', 'data-model_scalar',
      'corrected/model' (vector implied), 'corrected/model_vector',
      'corrected/model_scalar', 'data/model' (vector implied),
      'data/model_vector', and 'data/model_scalar'.  The implied vector
      residual datacolumns were kept for backwards compatibility. 
      Default data columns for x and y are both 'data'.

      .. rubric:: 1.3.2.2 Antenna Pointing Direction Parameters
         :name: antenna-pointing-direction-parameters

      Ant-Ra, Ant-Dec axes are the longitude and the latitude of the
      direction to which the first antenna of a baseline points at
      data-taking timestamps. Their value is computed by

      -  interpolating with a user-supplied method the direction of that
         antenna at that data-taking timestamp, from the known
         directions pointed by that antenna at
         pointing-direction-recording timestamps, recorded in
         MeasurementSet's POINTING table
      -  converting the result to a user-specified output reference
         frame

      The plotms task parameters to set ant-ra and ant-dec axes
      parameters are:

      -  xinterp: interpolation method to use when xaxis='ant-ra' or
         xaxis='ant-dec'
      -  xframe: output reference frame to use when xaxis='ant-ra' or
         xaxis='ant-dec'
      -  yinterp: interpolation method to use when yaxis='ant-ra' or
         yaxis='ant-dec'
      -  yframe: output reference frame to use when yaxis='ant-ra' or
         yaxis='ant-dec'

      Valid values for xframe and yframe are: 'icrs', 'j2000', 'b1950',
      'galactic', 'azelgeo' (default "" == 'icrs')

      Valid values for xinterp and yinterp are: 'nearest', 'cubic
      spline', 'spline' (default "" == 'cubic spline')

      Note:

      -  'spline' is a synonym for 'cubic spline'
      -  when the interpolation method is set to 'nearest', reference
         frame conversion is performed at the nearest pointing-recording
         timestamp, not at the data-taking timestamp

      .. container:: alert-box

         WARNING: plotting antennas pointing directions with the Ant-Ra
         / Ant-Dec axes has only been implemented for ALMA, ASTE, and
         NRO data.

       

      .. rubric:: 1.3.3 Axis Locations
         :name: axis-locations

      The location of the x-axis and y-axis can be set using the radio
      buttons in the GUI, where the x-axis can be located at the Bottom
      (default) or Top, and the y-axis can be located at the Left
      (default) or Right.

      The plotms task parameter to set the y-axis location is
      yaxislocation.  There is no parameter to set the x-axis location. 
      Valid values for this parameter include 'left' and 'right'
      (default "" == 'left').

      .. rubric:: 1.3.4 Axes Ranges
         :name: axes-ranges

      The X and Y ranges of the plot can be set manually or
      automatically. By default, the circle next to Automatic will be
      checked, and the ranges will be auto-scaled. To define the range,
      click on the circle below Automatic and enter a minimum and
      maximum value in the blank boxes. Note that if identical values
      are placed in the blank boxes (xmin=xmax and/or ymin=ymax), then
      the values will be ignored and a best guess will be made to
      auto-range that axis.

      The plotms task parameter used to set the axes ranges
      is plotrange, and its value is a list of numbers in the format
      [xmin, xmax, ymin, ymax] (default [ ], automatic range).

      .. rubric:: 1.3.5 Plotting Multiple Y-Axes
         :name: plotting-multiple-y-axes

      Different values of the same dataset can be shown at the same
      time. To add a second y-axis, press the Add Y Axis Data button at
      the bottom of the Axes tab. Then select the parameters for the
      newly created axis by selecting from the new “Y Axis Data”
      drop-down menu. If the two y-axes have the same units, they can be
      displayed both on the same axis. If they are different (or their
      ranges are dissimilar), e.g. Amplitude and Elevation (both versus
      Time; see Figure 4 below), one axis should be attached to the left
      and the other to the right hand side of the plot. Using more than
      a single y-axis data is also reflected in the Display tab where a
      drop-down menu appears in order to select multiple y-axis options;
      here you may colorize each axis differently.  See the section
      belowto learn more about\ \ \ \ \ `symbol
      properties <#1-6-2-customizing-your-symbols>`__\ \ \ \ \ . To
      remove the additional y-axis, click Delete Y Axis Data at the
      bottom of the Axes tab.

      +---------+-----------------------------------------------------------+
      | Type    | Figure 4                                                  |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | Overplotting in plotms: Two different y-axes for the same |
      |         | dataset have been chosen for this plot, amplitude and     |
      |         | elevation.                                                |
      +---------+-----------------------------------------------------------+

      The plotms task parameters used to plot multiple y-axes are the
      same as for a single y-axis: yaxis and yaxislocation; multiple
      y-axes can be specified as a list of strings if you are specifying
      the plotms command in the terminal. The values for yaxis and
      yaxislocation should be set to lists of the same length:

      .. container:: casa-input-box

         plotms(vis='ngc5921.ms', yaxis=['amp','elevation'],
         yaxislocation=['left','right'])

      .. rubric:: 1.3.6 Atmospheric Curve Overlays
         :name: atmospheric-curve-overlays

      The ability to compute and overlay an atmospheric transmission
      curve or a sky temperature curve, available in plotbandpass, has
      been added to plotms.  For this feature, the x-axis must be
      Channel or Frequency; if another axis is chosen, a warning is
      issued and the plot continues without the overlay.

      plotms uses the dataset's subtables to compute the mean weather
      values: pressure, humidity, temperature, and precipitable water
      vapor (pwv).  If these subtables are not found, reasonable
      defaults are used instead and reported in a log message. 
      The\ `atmosphere
      tool <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_atmosphere>`__\ is
      then used by plotms to calculate dry and wet opacities to produce
      the requested overlay curve, corrected by the airmass based on
      elevation.

      +---------+-----------------------------------------------------------+
      | Type    | Figure 5                                                  |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | Amp vs. Frequency plot with a Tsky overlay.  The Tsky     |
      |         | y-axis is automatically added on the right, and the curve |
      |         | is plotted in magenta.  The Plot > Axes tab shows the     |
      |         | radio buttons to select the Overlay: None, Atm, or Tsky.  |
      +---------+-----------------------------------------------------------+

      The plotms task parameters used to plot the overlays are showatm
      and showtsky.  These take boolean values and their defaults are
      False.  Only one overlay can be selected; if both are set to True,
      only the atmospheric curve (showatm) will be displayed.

      .. container:: casa-input-box

         plotms(vis=myvis, yaxis='amp', xaxis='freq', showatm=True)

      The image sideband curve may also be shown in plotms when the
      atmospheric transmission or sky temperature curves are plotted. 
      In order to do this, the MS (or associated MS for a calibration
      table) cannot have reindexed spectral window IDs as a result of a
      split, and must have an ASDM_RECEIVER table in order to read the
      LO frequencies.  If these conditions are not met, a warning is
      issued and only the atm/tsky curves are calculated and plotted.

      +---------+-----------------------------------------------------------+
      | Type    | Figure 5b                                                 |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | Gain Amp vs. Frequency plot for a bandpass calibration    |
      |         | table with the Atm Transmission (magenta) and Image       |
      |         | Sideband (black) overlays, colorized by spw and one       |
      |         | antenna selected.  The Plot > Axes tab shows the checkbox |
      |         | to select the image sideband curve, enabled only when the |
      |         | Overlay is Atm or Tsky.                                   |
      +---------+-----------------------------------------------------------+

      The plotms task parameter used to plot the image sideband curve
      overlay is showimage.  This takes a boolean value and its default
      is False.  If showatm=False and showtsky=False, a warning is
      issued and the curve will not be calculated and plotted.

      .. container:: casa-input-box

         plotms(vis=mycaltable, yaxis='amp', xaxis='freq', antenna='0',
         coloraxis='spw', showatm=True, showimage=True)

      --------------

      .. rubric:: 1.4 Iteration and Page Header : The Plot Page Tab
         :name: iteration-and-page-header-the-plot-page-tab

      .. rubric::  |Plotms Plot Page Tab|
         :name: plotms-plot-page-tab

      ======= ================
      Type    Figure 6
      ID      plotms.plot.page
      Caption Plot Page Tab
      ======= ================

      .. rubric:: 1.4.1 Iteration
         :name: iteration

      In many cases, it is desirable to iterate through the data that
      were selected in the Data tab. A typical example is to display a
      single baseline in an amplitude vs. time plot and then proceed to
      the next baselines step by step. This can be done via the Plot >
      Page tab.  A drop-down menu allows you to select the axis to be
      iterated on, with options None, Scan, Field, Spw, Baseline,
      Antenna, Time, and Corr.  Press the Plot button after changing
      your selection.  Each plot will be autoscaled according to its
      iteration value range unless a Range is specified in the Axis tab.

      The current iteration is indicated in the plot title of the
      displayed plot. To proceed to the next plot use the green arrow
      buttons below the main panel. The different button symbols let you
      to proceed panel by panel (single arrow symbols) or to jump to the
      first or last panel directly (double arrow symbols).

      The number of plots per page can be selected under Options > Grid,
      the last of the top row of tabs, as described in the section
      on\ `plotting on a grid <#4-1-plotting-on-a-grid>`__\ .  There are
      two scaling options for the iterated axes in a grid, set in this
      tab: Global and Shared. Global will use a common axis range based
      on data loaded with the selection criteria specified in the Data
      tab. Shared displays one set of x-axes and y-axes for the page
      rather than per-plot.  When left
      unchecked, Global \ and Shared \ results in plots with axes
      scaling to the data for each individual panel of the iteration. 
      See Figure 9 in\ `section
      4.1.1 <#4-1-1-plotting-iterations-on-a-grid>`__\ for an example of
      global shared x-axes and y-axes.

      The plotms task parameter used to select an iteration axis is
      iteraxis.  The options include 'scan', 'field', 'spw', 'baseline',
      'antenna', 'time', and 'corr'.

      To use a global axis range for iterated plots, set parameters
      xselfscale=True and/or yselfscale=True.  To use a shared external
      x-axis per column on a grid, set xsharedaxis=True (must also set
      xselfscale=True and gridrows greater than 1).  To use a shared
      external y-axis per row on a grid, set ysharedaxis=True (must also
      set yselfscale=True and gridcols greater than 1).

      .. rubric:: 1.4.2 Page Header
         :name: page-header

      It is sometimes useful to display above the plots a page header
      showing some metadata information. To do so, select in the lower
      list the header items you want to display, and press the
      antenna-shaped "arrow" pointing up. This will move the items you
      selected to the upper list showing the header contents, without
      updating the page header. Press the Plot button to update the page
      header.

      Multiple items can be selected at once by pressing the Shift or
      the Control key, Control+A selects all items.

      Items displayed in the Contents list are laid out on 2 columns in
      the page header, in "Z" order.

      To remove items from the Contents list, select in that list the
      items to remove and press  the antenna-shaped "arrow" pointing
      down.

      Antennas blink red when clicked while their corresponding
      selection is empty, green otherwise.

      Header items from multiple plots can be displayed in the page
      header. In that case items from the first plot are laid out first,
      items from the second plot are then laid out starting from the
      first empty row, and so on.

      The contents of the header is common to all pages.

      The plotms task parameter used to specify header items is
      headeritems. Legal value is a string whose value can be any
      comma-separated combination of the following pre-defined
      keywords: 

      -  'filename',
         'projid','telescope','observer','obsdate','obstime','targname','targdir','ycolumn'

      When selected data leaves room for multiple candidates (e.g when
      selected data spans multiple observations or include multiple
      fields or sources), the first selected row in MeasurementSet's
      Main table is used as a starting point for looking up a single
      "first" candidate in  MeasurementSet's auxiliary tables.

      Observation Start Date and Observation Start Time are looked up in
      MeasurementSet's Observation table, and therefore differ from the
      output of listobs task.

      --------------

      .. rubric:: 1.5 Transforming the Velocity Frame or Phase Center:
         The Plot Transform Tab
         :name: transforming-the-velocity-frame-or-phase-center-the-plot-transform-tab

      .. rubric:: 1.5.1 Frequency Frame
         :name: frequency-frame

      If the user plans to plot frequency, the reference frame must be
      defined. By default, plotms selects the frame keyword (if any)
      present in the data, usually the frame observed at the telescope
      unless modified during previous processing. However,
      transformations can be made by choosing a\ *Frame*\ from the
      drop-down menu in the\ *Plot>Transform*\ tab. Frequency reference
      frames can be chosen to be:

      -  LSRK— local standard of rest (kinematic)
      -  LSRD— local standard of rest (dynamic)
      -  BARY— barycentric
      -  GEO— geocentric
      -  TOPO— topocentric
      -  GALACTO— galactocentric
      -  LGROUP— local group
      -  CMB— cosmic microwave background dipole

      The plotms task parameter used to select frequency frame is
      freqframe.  Valid options include those listed above (strings with
      all caps).  The default empty string "" results in no frame
      transformation.

      .. rubric:: 1.5.2 Velocity
         :name: velocity

      If Velocity is selected as an axis, by default the transformation
      from frequency uses the parameters in the MS metadata, or, if
      absent, using the central frequency and TOPO frame. The user can
      change this by using the Frame, Velocity Defn, and Rest Freq
      options in the Transform tab\ . The velocity definition is chosen
      from the\ *Velocity Defn*\ drop-down menu, offering selections
      of\ *Radio,True*\ (Relativistic), or\ *Optical.*

      For more information on frequency frames and spectral coordinate
      systems, see the paper by Greisen et al. (A&A, 446, 747, 2006)
      (Also
      at\ \ \ `http://www.aoc.nrao.edu/~egreisen/scs.ps <http://www.aoc.nrao.edu/%7Eegreisen/scs.ps>`__\ \ )\ :sup:`
      `

      Finally, the spectral line’s rest frequency in units of MHz should
      be typed into the Rest Freq input box next. You can use
      the\ `slsearch <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_slsearch>`__\ task
      to search a spectral line table, or theme.spectrallinetool method
      to turn transition names into frequencies:

      .. container:: casa-input-box

         | CASA <16>: me.spectralline('HI')
         | Out[17]:
         | {'m0': {'unit': 'Hz', 'value': 1420405751.786},
         | 'refer': 'REST',
         | 'type': 'frequency'}

      For a list of known lines in the CASAmeasuressystem, use the
      toolkit commandme.linelist(). For example:

      .. container:: casa-input-box

         | CASA <21>: me.linelist()
         | Out[21]: 'HI H186A H185A H184A H183A H182A H181A H180A H179A
           H178A H177A H176A H175A
         | H174A H173A H172A H171A H170A H169A H168A H167A H166A H165A
           H164A H163A H162A H161A H160A...
         | He182A He181A He180A He179A He178A He177A He176A He175A
           He174A He173A He172A He171A He170A
         | He169A He168A He167A He166A He165A He164A He163A He162A
           He161A He160A He159A He158A He157A...
         | C186A C185A C184A C183A C182A C181A C180A C179A C178A C177A
           C176A C175A C174A C173A C172A
         | C171A C170A C169A C168A C167A C166A C165A C164A C163A C162A
           C161A C160A C159A C158A C157A...
         | NH3_11 NH3_22 NH3_33 NH3_44 NH3_55 NH3_66 NH3_77 NH3_88
           NH3_99 NH3_1010 NH3_1111 NH3_1212
         | OH1612 OH1665 OH1667 OH1720 OH4660 OH4750 OH4765 OH5523
           OH6016 OH6030 OH6035 OH6049 OH13433
         | OH13434 OH13441 OH13442 OH23817 OH23826 CH3OH6.7 CH3OH44
           H2O22 H2CO4.8 CO_1_0 CO_2_1 CO_3_2
         | CO_4_3 CO_5_4 CO_6_5 CO_7_6 CO_8_7 13CO_1_0 13CO_2_1 13CO_3_2
           13CO_4_3 13CO_5_4 13CO_6_5
         | 13CO_7_6 13CO_8_7 13CO_9_8 C18O_1_0 C18O_2_1 C18O_3_2
           C18O_4_3 C18O_5_4 C18O_6_5 C18O_7_6
         | C18O_8_7 C18O_9_8 CS_1_0 CS_2_1 CS_3_2 CS_4_3 CS_5_4 CS_6_5
           CS_7_6 CS_8_7 CS_9_8 CS_10_9
         | CS_11_10 CS_12_11 CS_13_12 CS_14_13 CS_15_14 CS_16_15
           CS_17_16 CS_18_17 CS_19_18 CS_12_19
         | SiO_1_0 SiO_2_1 SiO_3_2 SiO_4_3 SiO_5_4 SiO_6_5 SiO_7_6
           SiO_8_7 SiO_9_8 SiO_10_9 SiO_11_10
         | SiO_12_11 SiO_13_12 SiO_14_13 SiO_15_14 SiO_16_15 SiO_17_16
           SiO_18_17 SiO_19_18 SiO_20_19
         | SiO_21_20 SiO_22_21 SiO_23_22'

      The plotms task parameters used to set velocity definition and
      rest frequency are veldef and restfreq.  Valid options for veldef
      are 'RADIO', 'TRUE', or 'OPTICAL' (default is 'RADIO').  restfreq
      should be in a string in MHz, for example '22235.08MHz'.

      .. rubric:: 1.5.3 Shifting the Phase Center
         :name: shifting-the-phase-center

      The plot’s phase center can be shifted in
      the\ *Plot>Transform*\ tab. This will allow coherent vector
      averaging of visibility amplitudes far from the phase tracking
      center.  Enter the X and Y shifts in units of arcseconds in the dX
      and dY boxes under\ *Phase center shift*\ .

      The plotms task parameter used to shift the phase center is
      shift.  Its value should be a list in the format [dx,dy] in arcsec
      (default [0.0, 0.0]).

      --------------

      .. rubric:: 1.6 Display Options for Plots: The Plot Display Tab
         :name: display-options-for-plots-the-plot-display-tab

      .. rubric:: 1.6.1 Colorizing Your Data
         :name: colorizing-your-data

      Data points can be given informative symbol colors using
      the\ *Colorize*\ option in the Plot > Display tab. By checking the
      box next to\ *Colorize*\ and selecting a data axis from the
      drop-down menu, the data will be plotted with colors that vary
      along that axis. For example, if “corr” is chosen from
      the\ *Colorize*\ menu, “RR”, “LL”, “RL”, and “LR” data will each
      be plotted with a different color. Note that\ *Colorize*\ while
      plotting flagged data will override the default flagged red symbol
      color.

      The plotms task parameter used to colorize data is coloraxis. 
      Options include 'scan', 'field', 'spw', 'antenna1', 'antenna2',
      'baseline', 'channel', 'corr', 'time', 'observation', and
      'intent'.

      .. rubric:: 1.6.2 Customizing Your Symbols
         :name: customizing-your-symbols

      Unflagged and flagged plot symbols can be customized in
      the\ *Plot>Display*\ tab. Most fundamentally, the user can choose
      to plot unflagged data and/or flagged data. By default, unflagged
      data is plotted (the circle next to\ *Default*\ is checked
      under\ *Unflagged Points Symbol*\ ), and flagged data is not
      plotted (the circle next to\ *None*\ is checked under\ *Flagged
      Points Symbol*\ ). We note here that plotting flagged data on an
      averaged plot is undertaken at the user’s own risk, as the
      distinction between flagged points and unflagged points becomes
      blurred if data are averaged over a dimension that is partially
      flagged. Take, for example, a plot of Amplitude vs. Time where all
      channels are averaged together, but some channels have been
      flagged due to RFI spikes. In creating the average,plotms will
      skip over the flagged channels and only use the unflagged ones.
      The averaged points will be considered unflagged, and the flagged
      data will not appear on the plot at all.

      Symbol options include:

      -  None— no data points
      -  Default— data points which are small circles (blue for
         unflagged data and red for flagged data)
      -  Custom— allows the user to define a plot symbol

      If\ *Custom*\ plot symbols are chosen, the user can determine:

      #. Size, by typing a number in the blank box next to\ *px*\ or by
         clicking on the adjacent up or down arrows.
      #. Shape, chosen from the drop-down menu; options include circle,
         square, diamond, pixel, or autoscaling.  Note that pixel only
         has one possible size.  autoscaling attempts to adjust the size
         of the points from dots to circles of different sizes,
         depending on how many points are plotted.\ 
      #. **Color**\ , chosen by typing a hex color code in the Fill
         input boxor by clicking on the...button and selecting a color
         from the pop-up GUI.
      #. Fill, using the adjacent drop-down menu for how heavily the
         plot symbol is shaded with this color, from heaviest to
         lightest; options include fill, mesh1, mesh2, mesh3, and no
         fill.
      #. Outline, by selecting None (no outline) or Default \ (outlined
         in black)

      Note that if “no fill” and Outline: None\ are selected, the plot
      symbols will be invisible.

      The plotms task parameter and subparameters used to customize
      unflagged symbols include:

      -  customsymbol (True/False, default False) - must be True for
         subparameters to take effect
      -  symbolshape ('autoscaling', 'circle', 'square', 'diamond',
         'pixel', 'nosymbol', default 'autoscaling')
      -  symbolsize (in number of pixels, default 2)
      -  symbolcolor (RGB hex code e.g. 'aa55ff' or string color name
         e.g. 'purple', default '0000ff' blue)
      -  symbolfill ('fill', 'mesh1', 'mesh2', 'mesh3', 'no fill',
         default 'fill')
      -  symboloutline (True/False, default False)

      The plotms task parameters used to customize flagged symbols
      include customflaggedsymbol (default False) with subparameters
      flaggedsymbolshape (default 'nosymbol'), flaggedsymbolsize
      (default 2), flaggedsymbolcolor (default 'ff0000' red),
      flaggedsymbolfill (default 'fill'), and flaggedsymboloutline
      (default False).  Supported values are the same as for unflagged
      symbols.

      .. rubric:: 1.6.3 Symbols for Multiple Y-Axes
         :name: symbols-for-multiple-y-axes

      If you have added an additional y-axis in the Plot > Axes tab, you
      may customize each y-axis individually by selecting the axis in
      the Y Axis Data pull-down menu at the top of the Plot > Display
      tab and then customizing the symbols for that axis.

      To set multiple symbols in the plotms task, set the symbol
      parameters as a list:

      .. container:: casa-input-box

         plotms(vis='ngc5921.ms', yaxis=['amp','elevation'],
         yaxislocation=['left','right'], customsymbol=[True,True],
         symbolcolor=['purple','green'])

      In this plot, the 'amp' axis will be purple, and the 'elevation'
      axis will be green.

      .. rubric:: 1.6.4 Connecting the Points
         :name: connecting-the-points

      Plotms has the capability to connect points for calibration
      tables; support for MeasurementSets will be added later.  The
      points are colorized and connected along the x-axis or time axis
      by line or step.  Points with the same metadata but varying values
      of the x-axis or time are connected.  Unflagged points are not
      connected to flagged points, even when they are not displayed. 
      The "Colorize" axis will override the connection colorization.

      +---------+-----------------------------------------------------------+
      | Type    | Figure 7                                                  |
      +---------+-----------------------------------------------------------+
      | ID      | plotms.plot.display                                       |
      +---------+-----------------------------------------------------------+
      | Caption | Plot Display tab showing the Connect Points options for a |
      |         | gain table.  Here, points with the same spw, channel,     |
      |         | polarization, and antenna1 are connected along the time   |
      |         | axis.                                                     |
      +---------+-----------------------------------------------------------+

      The plotms task parameters used to connect points in a calibration
      table plot are xconnector (default "none", options "line" or
      "step") and timeconnector (default False, or True to connect along
      time axis instead of x-axis).

      --------------

      .. rubric:: 1.7 Plot Labels: The Plot Canvas Tab
         :name: plot-labels-the-plot-canvas-tab

      .. rubric:: 1.7.1 Plot Title
         :name: plot-title

      Options to change the plot title include None (no title), Default,
      and a user-input string.  To set the plot title, under\ *Title*\ ,
      click on the circle next to the input box and enter the desired
      text. This text box shows the grayed-out default string,
      "%%yaxis%% vs. %%xaxis%%" (to substitute the axis names for
      "yaxis" and "xaxis").  The user can also choose the size of the
      title font by checking the Title Font checkbox and entering the
      font size or using the arrows to increase or decrease the value. 
      The default is to scale the title font depending on the plot size.

      The plotms task parameters used to set the title and its font are
      title (default "" for yaxis vs. xaxis string) and titlefont
      (default is 0 to autoscale).  Set title='"" for the default title
      (Y vs. X) or " " (space) for no title.

      .. rubric:: 1.7.2 Legend
         :name: legend

      A plot symbol legend can be added to the plot by clicking on the
      checkbox next to\ Legend\ . For a simple plot,a symbol legend
      simply echoes the plot axes (e.g. "Amp vs Time") but is useful
      when\ \ `overplotting
      data <#7-1-overplotting-multiple-data-sets-on-the-same-plot>`__\ \ with
      custom colors so that you can identify the data (e.g. "Amp vs
      Time" in blue and "Phase vs Time" in green on the same plot).

      When enabled, a drop-down menu next to Legend allows the user to
      select the legend location either within the plot (Upper Right,
      Lower Right, Upper Left, Lower Left) or outside the plot (Out
      Right, Out Left, Out Top, Out Bottom).

      The plotms task parameter used to enable the legend is showlegend
      (default is False).  To select the legend location subparameter,
      set legendposition to 'upperRight', 'upperLeft', 'lowerRight',
      'lowerLeft', 'exteriorRight', 'exteriorLeft', 'exteriorTop', or
      'exteriorBottom' (default is "" == upperRight).

      .. rubric:: 1.7.3 Axis Labels
         :name: axis-labels

      To enable the X- and Y-axis labels, check the Show Label
      checkboxes under\ *X Axis*\ and\ *Y Axis *\ (default is checked). 
      As with the plot title, the user may set the label to None (no
      label), Default (axis name with units),\   ortype the desired text
      in the blank box.  The font size of labels can also be customized
      by enabling then setting the font size for each axis.  The
      location of axis labels is determined by the axis location as set
      in the\ *Plot>Axes*\ tab, as shown in\ `the section
      above <#1-3-3-axis-locations>`__\ .

      The plotms task parameters used to set the label text and font
      are xlabel and ylabel (default "" is axis name with units, set to
      ' ' space to disable label) and xaxisfont and yaxisfont (default 0
      == autoscale).

      .. rubric:: 1.7.4 Grid Lines
         :name: grid-lines

      A grid of lines can be superimposed on the plot using\ *Grid
      Lines*\ in the\ *Plot>Canvas*\ tab. “Major” grid lines are drawn
      at the locations of major tick marks, while “minor” grid lines are
      drawn at minor tick marks.

      Grid line colors, thicknesses, and styles are selected
      independently for the “major” and “minor” grid lines. Desired line
      thickness should be typed into the blank boxes just to the right
      of the\ *Major*\ and\ *Minor*\ labels. Colors are set by clicking
      on the...buttons. The blank boxes to the left of the...buttons
      will then contain the hex codes for the selected colors (e.g.,
      “808080”). Line styles can also be selected from the drop-down
      menus to the right of...buttons; style options include solid,
      dash, dot, and none.

      The plotms task parameter used to add and customize major grid
      lines include showmajorgrid (default is False) with subparameters
      majorwidth (default is 1), majorstyle ('solid', 'dash', 'dot',
      'none'; default is 'solid'), and majorcolor (RGB hex code or color
      name; default is 'b0b0b0' dark gray).

      Parameters for minor grid lines include showminorgrid (default is
      False) with subparameters minorwidth (default is 0), minorstyle
      (default is 'solid'), and minorcolor (default is 'd0d0d0' light
      gray).

      --------------

      .. rubric:: 2. Flag Extensions: The Flag Tab
         :name: flag-extensions-the-flag-tab

      |image3|

      +---------+-----------------------------------------------------------+
      | Type    | Figure 8                                                  |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | The plotms *Flag* tab.  Here the *Extend flags* box has   |
      |         | been checked, enabling the *Correlation* and *Channel*    |
      |         | options.  The plot shows unflagged data in blue and       |
      |         | flagged data in red.                                      |
      +---------+-----------------------------------------------------------+

      See the section below on\ `interactive flagging in
      plotms. <#8--interactive-flagging>`__\   The options in this tab
      allows the user to have flagging extend to other data points
      besides what is marked on the plot.

      When enabled with the Extend flags checkbox, the user may choose
      to extend flags based on correlation or channel by checking the
      corresponding checkboxes.  Future options for flag extensions are
      planned.

      By checking the boxes next to Extend Flags\ and\ Correlation\ ,
      flags will be extended beyond the correlations displayed.
      Currently the only option is to extend to Allcorrelations as noted
      by the radio button, implying that all correlations will be
      flagged.  For example, with RR displayed, the correlations RR, RL,
      LR, and LL will all be flagged when this option is enabled.

      By checking the boxes next to\ *Extend Flags*\ and\ *Channel*\ ,
      flagging will be extended to other channels in the samespwas the
      displayed point. For example, ifspw=’0:0’and channel 0 is
      displayed, then flagging will extend to all channels in spw 0.

      The plotms task parameter used to extend flags is extendflag
      (True/False, default is False) with subparameters extcorr
      (True/False), and extchannel (True/False).  These parameters will
      enable flag extensions when interactively flagging the plot.

      --------------

      .. rubric:: 3. Interactive Tools: The Tools Tab, Annotate Tab, and
         Tool Icons
         :name: interactive-tools-the-tools-tab-annotate-tab-and-tool-icons

      +---------+-----------------------------------------------------------+
      | Type    | Figure 9                                                  |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | The plotms Tools tab.  Here the Tracker Display tool is   |
      |         | showing the (X,Y) coordinates of the cursor position.  A  |
      |         | previous position was saved to the text box by pressing   |
      |         | the SPACE bar.                                            |
      +---------+-----------------------------------------------------------+

      Various interactive GUI tools are selectable with the radio
      buttons in the Hand Tools section of the Tools \ tab at the top of
      the plotms window.  They are also available as icon buttons at the
      bottom of the plotms window.  These tools can be used to zoom,
      pan, annotate, flag/unflag, and locate data.  Described below are
      the bottom icon buttons in order.

      -  

         .. container::

            Zoom — The “magnifying glass” button (1st on left) lets you
            draw a box around a region of the plot (left-click on one
            corner of the box, and drag the mouse to the opposite corner
            of the desired box), and then zooms in on this box.

      -  

         .. container::

            Pan — The “four-arrow” button (2nd from left) lets you pan
            around a zoomed plot.

      -  

         .. container::

            Annotate — The 3rd button from the left is chosen from a
            drop-down menu to either Annotate Text (“T with a green
            diamond” button) or Annotate Rectangle (“pencil” button).
            With Annotate Text activated, click on a location in the
            plot where text is desired; a window will pop up, allowing
            you to type text in it. When you click the OK button, this
            text will appear on the plot. Annotate Rectangle simply lets
            you draw a box on the plot by left-clicking and dragging the
            mouse. By clicking on the Annotate tab near the top of the
            plotms window, different fonts, colors, line styles, etc.
            can be selected for annotations.

      -  

         .. container::

            Stack Base — The “house” button (5th from left) returns to
            the original zoom level.

      -  

         .. container::

            Stack Back and Stack Forward — The left and right arrow
            buttons (4th and 6th from left) step through the zoom
            settings you’ve visited.

      -  

         .. container::

            Mark Regions — The “box with a green diamond” button (7th
            from left) lets you mark a region for flagging, unflagging,
            or locating. Left-click on one corner of the desired region,
            and then drag the mouse to set the opposite corner of the
            region. You can mark multiple boxes before performing an
            operation on them.  The selected regions will appear on the
            plot as shaded rectangles.

      -  Subtract Regions — The “box with a minus sign” button (8th from
         left) lets you de-select marked regions (draw around a marked
         region and the shaded area will disappear).  To de-select all
         marked regions, use the next button.

      -  

         .. container::

            Clear Regions — Clicking on the “box with a red circle”
            button (9th from left) will clear all regions which have
            been marked using Mark Regions.

      -  Locate — The “magnifying glass on a sheet of paper” button
         (10th from left) will print out information about points in the
         marked regions.  This information is printed to the shell
         terminal when plotms was started with casaplotms, or to the
         casa logger/logfile when plotms was started in a casa python
         session.  The header of the output indicates the plotted X and
         Y axes and the range of values in the selected region.  The
         output for each point includes scan, field, time, baseline,
         spw, channel, frequency, correlation, X, Y, and observation
         ID.  By copying this list to a text file, or setting a new
         logfile with casalog.setlogfile as described in the\ `CASA
         logger
         documentation <https://casa.nrao.edu/casadocs-devel/stable/usingcasa/casa-logger>`__\ ,
         the Locate information can be edited to provide input for
         flagdata.  To list an entire column, e.g. all visibilities for
         a source, use the listvis task or the\ `table
         tools <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list/tool_table>`__\ .

      -  

         .. container::

            Flag — Click on the “flag” button (11th from left) to flag
            all points in the marked regions.  See the section below
            on\ `Interactive Flagging <#8--interactive-flagging>`__\ .

      -  

         .. container::

            Unflag — Click on the “crossed-out flag” button (12th from
            left) to unflag any flagged points in the marked regions
            (even if not displayed).

      -  Flag All — Click on the "per-grid flag/unflag" button (13th
         from left) to enter/leave the "Flag All" mode. See the section
         below on\ `Interactive
         Flagging <#8--interactive-flagging>`__\ .

      -  **Iteration**\ — The next four green arrow buttons (14th
         through 17th from left) control iteration, with the first and
         last "double arrow" buttons used to display the first and last
         iteration, and the center two "single arrow" button to display
         the previous or next iteration.  If the plots are on a grid,
         these arrows navigate through the pages of plots which contain
         multiple iterations.

      -  

         .. container::

            Hold Drawing — If the Hold Drawing button (rightmost, or
            18th from left) is clicked to activate it, when new plot
            axes are selected from the Plot > Axes tab, the new data
            will be cached but not plotted. When the button is clicked
            again (de-activated), it will automatically plot the data
            that was last requested. This can be particularly useful
            when changing the size of the plotms window.

      The Tools tab also contains Tracker tools including Hover and
      Display.  When Hover is selected and the mouse is moved over the
      plot, the pointer's position is displayed on the plot in (X, Y)
      format.  When Display is selected, the (X, Y) position is
      displayed in the text box under the Display checkbox.

      To record various tracked positions, enable Display then click on
      the plot to activate it.  As usual, moving the pointer displays
      the position in the small display text box.  Pressing the SPACE
      bar will copy the displayed line into the larger white box below
      it. This can be repeated many times and a log of positions and
      values will be created. The content in the box can then be easily
      copied and pasted into any other application that is used for data
      analysis. The Clear button wipes out the content of the box for a
      fresh start into new scientific adventures.

      --------------

      .. rubric:: 4. Miscellaneous Options: The Options Tab
         :name: miscellaneous-options-the-options-tab

      A few miscellaneous per-page plot options and GUI options are
      available in the\ *Options*\ tab, the last tab at the top of the
      plotmswindow.

      .. rubric:: 4.1 Plotting on a Grid
         :name: plotting-on-a-grid

      The layout of the page is set on the plotms Options tab. For
      multiple plots per page, set the grid layout, the number of rows
      and columns that determine the number of sub-plots.  When set,
      click "Update" to activate the grid changes.

      .. rubric:: 4.1.1 Plotting Iterations on a Grid
         :name: plotting-iterations-on-a-grid

       

      |image4| 

      +---------+-----------------------------------------------------------+
      | Type    | Figure 10                                                 |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | The plotms Options tab.  Here a 2x2 grid has been created |
      |         | with iteration on the 'antenna' axis.                     |
      +---------+-----------------------------------------------------------+

      If\ `iteration <#1-4-iteration--the-plot-page-tab>`__\ is enabled
      in the Plot > Page tab, the grid will be filled automatically with
      each iterated plot.  The Plot > Page tab is also where common axis
      scales and shared axes will be set; they are enabled for the plot
      in Figure 9.  These axis options are only available for iterated
      plots in a grid.

      The plotms task parameters used to create a grid with iteration
      include gridrows and gridcols (default is 1)\ . To create the plot
      shown in Figure 9, the plotms command would be:

      .. container:: casa-input-box

         plotms('ngc5921_ut.ms', xaxis='freq', iteraxis='antenna',
         gridrows=2, gridcols=2, xsharedaxis=True, xselfscale=True,
         ysharedaxis=True, yselfscale=True)

      .. rubric:: 4.1.2 Plotting Multiple Data on a Grid
         :name: plotting-multiple-data-on-a-grid

      We note here that plotting multiple datasets or axes on a grid is
      possible in plotms but covered separately in the\ `section
      below <#6-2-plotting-multiple-datasets-or-axes-on-a-grid>`__\ \ \ ,
      as this involves many settings in the GUI or multiple plotms task
      commands.  Since the grid affects all of the plots, its settings
      are in the Options tab rather than the Plot tab.

      .. rubric:: 4.2 Tool Button Style
         :name: tool-button-style

      The Tool Button Style drop-down menu determines the format of the
      tool buttons at the bottom of the plotms window. The options
      include Icon Only, Text Only, Text Beside Icon, and Text Under
      Icon.  In Icon Only mode (default), hovering the cursor over each
      icon will give a text description of the icon.

      To hide the bottom icons, see the description of the\ \ `View
      menu <#5-2-view-menu>`__\ \ . The tools can also be accessed in
      the Tools tab.

      .. rubric:: 4.3 Log Events
         :name: log-events

      This drop-down menu shows a checklist of events and plotms
      functions so that you can customize how verbose plotmsis in
      documenting its actions.

      .. rubric:: 4.4 Clear Regions and Annotations
         :name: clear-regions-and-annotations

      The When changing plot axes, clear any existing regions or
      annotations checkbox determines when regions and annotation are
      deleted from the plot. By default, this is enabled.

      .. rubric:: 4.5 Cached Images
         :name: cached-images

      A useful option is the Use\ *fixed size for cached
      image*\ checkbox. It determines how large the dots in the panel
      are with respect to the screen resolution. The values influence
      how the data is redrawn on the panel. When\ *Screen
      resolution*\ is selected, the plotmswindow can be resized without
      redrawing on the canvas – a considerable speedup for large data
      sets. The penalty is that the dots of the data points are the size
      of a pixel on the screen, which may be very small for high
      resolution monitors.  By default, this feature is not enabled.

      .. rubric:: 4.6 File Chooser History Limit
         :name: file-chooser-history-limit

      This setting allows the user to limit how many remembered
      filepaths are displayed in file chooser dialogs produced by
      clicking Browse in the Plot > Data tab to select a MeasurementSet
      or calibration table and in the Plot > Calibration tab to select a
      calibration library.

      --------------

      .. rubric:: 5. The plotms Menus
         :name: the-plotms-menus

      .. rubric:: 5.1 File Menu: Quit
         :name: file-menu-quit

      The File menu in the top menu bar allows you to Quit plotms, or
      you can click the X in the upper right corner of the window.

      .. rubric:: 5.2 Export Menu: Saving Your Plot
         :name: export-menu-saving-your-plot

      You can save a copy of a plot to file with theExport menu, which
      produces an Export Plots dialog box with many settings.

      -  Filename: Click the\ *Browse*\ button for a GUI-based selection
         of the directory and filename to which the plot will be saved,
         or click the Insert MS Name button to minimize typing. You may
         also just type in a file name.The file format can be determined
         in this GUI by the suffix given to the
         filename:.png,.jpg,.ps,.pdf, andtxt. 

         .. container:: alert-box

            If a file already exists with the given filename, it will be
            overwritten without warning!

      -  Format: Alternatively, the file format can be selected from
         the\ *Format*\ drop-down menu, with these options: [by file
         extension], PNG, JPG, PS, PDF, and TEXT. For the first option,
         if your filename is "test.jpg" the plot will be exported in JPG
         format.  For the other formats, plotms will use the filename as
         given and notadd a suffix to indicate its format. See below for
         an example of TEXT format; the header will include the name of
         the visibility and other specified parameters including
         selection, averaging, transformations, etc.
      -  Verbose: When a text export is selected, the output can be
         verbose (include metadata).  When this checkbox is unchecked,
         the text export will include x and y values only.  This
         parameter is ignored for other formats.
      -  Range: When iteration is chosen, producing multiple plots, you
         may select to export only the Current Page or A\ ll Pages\ . 
         Each saved plot will have the name of the iteration appended to
         the given filename before the extension.  For example, with
         filename "ngc5921_ut.jpg" and iteration on antenna, the first
         plot will be named "ngc5921_ut_Antenna1@VLA:N7.jpg".  This is
         so the exported plots can be identified without viewing them. 
         Be warned that if you are plotting iterations on a grid, the
         filenames will have all of the iterations on the page appended,
         which can lead to a very long filename. Filenames exceeding 255
         characters in length will be automatically shortened upon
         export. One plotfile per page is produced; multipage pdf
         exports are not currently supported.
      -  **HighResolution:**\ Exporting to images in screen resolution
         is currently not working, so plot exports are always high
         resolution.  A notice is issued in the console/log.
      -  **DPI, Size**\ : Use the text boxes or up/down arrows to set
         the output DPI or size (in pixels) of the exported plot.
      -  Export: When settings are complete, click Export to create your
         plotfile.

      Note:The plot files produced by the PS and PDF options can be
      large and time-consuming to export. The JPG is the smallest.

      The TEXTformat will not save an image but all of the data points
      themselves. This allows one to dump the current plot into a file
      that is used in other programs for further processing.

      .. container:: alert-box

         ALERT: The exported TEXT file can be quite large and take some
         time to create.  Using averaging, selection, etc. is
         recommended to keep the file size manageable.  If a region is
         marked as described in section 3, only those points are
         exported to the text file.

      The reported data is the same as when using the L\ *ocate*\ button
      in plotms, with the following format (when verbose=True):

      .. container:: casa-output-box

         | # vis: ngc5921_ut.ms
         | # scan: 4
         | # channel average: 63
         | # time average: None
         | # From plot 0
         | # x y chan scan field ant1 ant2 ant1name ant2name time freq
           spw corr obs
         | # Time Amp None None None None None None None MJD(seconds)
           GHz None None None
         | 4304483429.999 62.7219 0 4 1 1 1 2@VLA:W1 2@VLA:W1
           4304483429.999 1.413332233 0 RR 0
         | 4304483429.999 59.0717 0 4 1 1 1 2@VLA:W1 2@VLA:W1
           4304483429.999 1.413332233 0 LL 0
         | 4304483429.999 59.0252 0 4 1 27 27 28@VLA:W7 28@VLA:W7
           4304483429.999 1.413332233 0 RR 0
         | 4304483429.999 60.8603 0 4 1 27 27 28@VLA:W7 28@VLA:W7
           4304483429.999 1.413332233 0 LL 0
         | 4304483429.999 57.4048 0 4 1 7 7 8@VLA:W8 8@VLA:W8
           4304483429.999 1.413332233 0 RR 0
         | etc.

      where x and y are the two plotted axes and the other columns
      contain additional information such as the baselines and
      frequencies, with an additional line for units.  The header for
      the file includes the name of the visibility and other parameters
      such as selection, averaging, etc.

      The plotms task parameter used to export plots is plotfile. 
      Unlike the Export Plots dialog box in the GUI, plotms will issue
      an error if this file exists unless overwrite=True.  Its
      subparameters include:

      -  expformat ('jpg', 'png', 'pdf', 'ps', 'txt') - select the
         format if no extension is included in the plotfile. If there is
         no plotfile extension and no expformat set, the plot will be
         exported as a PNG.
      -  verbose (True/False, default is True) - include metadata in
         text export; ignored for other formats.
      -  *exprange*\ ('current', 'all'; defaults to current)
      -  highres (True/False, default is False)
      -  *dpi*
      -  width (in pixels)
      -  height (in pixels)
      -  *overwrite*\ (True/False, default is False)

      .. rubric:: 5.3 Summary Menu: Information About Your Dataset
         :name: summary-menu-information-about-your-dataset

      Information about the MeasurementSet can be obtained from within
      plotmsby clicking on the\ *Summary*\ menu in the top menu bar. If
      All is chosen from the pull-down menu next
      to\ *Type*\ ,listobs-style output about scans, correlator
      configurations, and antennae will be written to the console or
      log.  Other options for a subset of the data include Where, What,
      How, Main, Tables, Antenna, Feed, Field, Observation, History,
      Polarization, Source, Spectral Window, Spectral Window and
      Polarization, SysCal, and Weather.

      For calibration tables, options in the Summary menu include All,
      Where, What, How, Main, Tables, Antenna, Field, Observation,
      History, and Spectral Window.

      For more detail, click on the\ *Verbose*\ checkbox.

      .. rubric:: 5.4 View Menu: Hide or Display Tool Icons
         :name: view-menu-hide-or-display-tool-icons

      This menu controls the display of tool icons.  Use the View >
      Toolbars menu to de-select and hide the Tools, Iteration (green
      arrows), or Display (Hold Drawing) icons.  By default these icons
      are all selected and displayed at the bottom of the plotms window.

      .. rubric:: 5.4 Help Menu: About plotms
         :name: help-menu-about-plotms

      This menu's About option describes plotms and the versions of
      CASA, Qt, and Qwt it uses, along with links.  Qt is the software
      framework that plotms uses for its GUI, and Qwt is a library that
      provides plotting functionality on top of the Qt framework.

      Click About Qt  for more detail about this software package and
      its licensing.

      --------------

      .. rubric:: 6. Plotting Multiple Data
         :name: plotting-multiple-data

      .. rubric:: 6.1 Overplotting Multiple Datasets or Axes on the Same
         Plot
         :name: overplotting-multiple-datasets-or-axes-on-the-same-plot

      It is possible to overplot two datasets on the same plot, or the
      same dataset with different y-axes in each plot.  To do this, set
      up the first plot as usual.  Then press the Add Plot button at the
      bottom left of the plotms window. This will bring up an additional
      data input panel in the Plot > Data tab where you can specify the
      plot parameters as you did for the first one, which is
      automatically minimized.  Use the slider to scroll vertically
      through the panels.  Use right-click options or the Minimize,
      Maximize, or Close buttons to keep a better overview on the
      individual datasets.

      When overplotting, you may want to set different custom colors for
      each dataset in its Display tab.  If you are plotting different
      axes or the axes ranges are a significantly different range of
      values, you may want to set different axes locations for each plot
      in the Axes tab.  When you are done, click the Plot button to see
      the overplot.

      Use the Close button in each data panel to close the panel and
      remove that plot.

      In the plotmstask interface, you can overplot by invoking
      plotmsmore than once withclearplots=False. Each plotms
      commandcorresponds to a plot to go on top of previous ones, and
      each must have its own plotindex (0-based, default is 0). 
      Otherwise, with the same plotindex, the second plot will overwrite
      the first.  In the following example, we are plotting Scan vs.
      Time for MeasurementSet test1.ms with plotindex 0, and Field vs.
      Time for MeasurementSet test2.ms on the same  plot with plotindex
      1.  The test2 data is a different color and its yaxis is on the
      right.

      Note that since the plotindex is an index into subplots, this
      parameter must be assigned in consecutive order.  If a plotindex
      is skipped, plotms will adjust the index number and inform the
      user of the corrected plotindex value.

      .. container:: casa-input-box

         plotms(vis='test1.ms', yaxis='scan')
         plotms(vis='test2.ms', yaxis='field', plotindex=1,
         clearplots=False, customsymbol=True, symbolcolor='00FF00',
         yaxislocation='right')

      .. rubric:: 6.2 Plotting Multiple Datasets or Axes on a Grid
         :name: plotting-multiple-datasets-or-axes-on-a-grid

      plotms allows you to plot more than one dataset or axes on the
      same page by\ `specifying a grid
      size <#4-1-plotting-on-a-grid>`__\ then a grid location for each
      plot as described below. Here is an example of two plots with
      different datasets:

      +---------+-----------------------------------------------------------+
      | Type    | Figure 11                                                 |
      +---------+-----------------------------------------------------------+
      | ID      |                                                           |
      +---------+-----------------------------------------------------------+
      | Caption | Plotting multiple data sets on a 2x1 grid.  Here, the MS  |
      |         | is plotted in grid location (1,1).  Then the *Add Plot*   |
      |         | button was used to select its bandpass calibration table  |
      |         | and plot it in grid location (2,1).                       |
      +---------+-----------------------------------------------------------+

      The process is similar to the one above, except that you specify
      the grid  and each plot's location:

      #. Set up your first plot as described above.
      #. Use the Options tab to set up a grid by incrementing the number
         of rows and/or columns.  By default the plot you set up in step
         1 will be in row 0, column 0.
      #. Use the Add Plot button to set up the second plot's parameters.
         Pay particular attention to the new dataset's Page tab, where
         you can set the Grid Location (row and column number) of the
         new plot.  This section appears only when a grid is set up.
      #. Unlike iteration, you cannot share axes among the plots.
      #. Add as many plots as you desire to fill your grid, then click
         Plot.

      Several plotms task parameters are used to create a grid and
      specify a plot location.

      -  gridcolsandgridrowsdefine the number of plots on the screen.
      -  colindexandrowindex(0-based) set the location of an individual
         plot
      -  plotindex(0-based) must be incremented by 1 for each plotms
         call
      -  clearplots is set to False to keep previous plots

      Here is an example of multiple plotmscalls to set up two plots on
      a grid and export the plot page; note the defaults on the first
      call are rowindex=0, colindex=0, plotindex=0 so just set up the
      grid.  On each subsequent plotms call set clearplots=False and
      increment the plotindex by 1\ .  To save the gridded plot, set a
      plotfile on the final plot.

      .. container:: casa-input-box

         plotms(vis='test1.ms', yaxis='field', gridrows=2, gridcols=1)
         plotms(vis='test2.ms', yaxis='field', gridrows=2, gridcols=1,
         rowindex=1, colindex=0, plotindex=1, clearplots=False,
         plotfile='fields.jpg')

      --------------

      .. rubric:: 7. Interactive Flagging
         :name: interactive-flagging

      Interactive flagging, on the principle of “see it — flag it”, is
      possible on the X-Y display of the data plotted by plotms. Use the
      cursor to mark one or more regions, and then flag, unflag, or list
      (\ `Locate <#3--interactive-tools--the-tools-tab--annotate-tab--and-tool-icons>`__\ )
      the data that falls in these regions of the display.

      .. container:: alert-box

         Do not attempt to flag data while another task is accessing the
         same data set.

      For plotting, plotms opens the MeasurementSet read-only, so there
      should be no problem if another task accesses the same dataset,
      unless the other task locks the file.  When this happens, you can
      wait for the lock to be released, cancel cache-loading in the
      plotms dialog box, type go clearstat at the prompt, or exit
      plotms. Do not attempt to flag data in plotms while another task
      is accessing the same data set, as in this case plotms must open
      the MeasurementSet with a file lock for writing.

      Using the row of icons at the bottom of the plotmswindow, click on
      the\ *Mark Regions*\ button, then mark a region by left-clicking
      and dragging the mouse.  Each click and drag will mark an
      additional region. You can remove all of your marked regions by
      clicking on the\ *Clear Regions*\ button. Once regions are marked,
      you can then click on one of the other buttons to take action:

      1. Flag— flag all of the points in the region(s),
      2. Unflag— unflag flagged points in the region(s),
      3. Locate— list information (X and Y value, scan, field, baseline,
         frequency, etc.) about the points in the region(s) to the
         command line or log (Warning: this could be a long list!).

      Note that if you mark a region with flagged and unflagged values
      and Flag it, using Unflag will not return the data to its previous
      state but will unflag all of the data in the marked region.

      The following figureshows an example of marking regions and then
      clicking the\ *Flag*\ button. Whenever you click on a button, that
      action occurs without requiring an explicit disk-write. If you
      quit plotmsand re-enter, you will see your previous edits because
      your flag changes were written to the MeasurementSet on disk.

      .. container:: center

         --------------

      .. container:: center

         \ 

      .. container:: center

         +---------+-----------------------------------------------------------+
         | Type    | Figure 12                                                 |
         +---------+-----------------------------------------------------------+
         | ID      |                                                           |
         +---------+-----------------------------------------------------------+
         | Caption | Plot of amplitude versus time, before (top) and after     |
         |         | (bottom) flagging two marked regions. Note that flagged   |
         |         | data is not displayed so these regions are hidden after   |
         |         | flagging.  To unflag these regions, mark the two same     |
         |         | regions and click the Unflag button.                      |
         +---------+-----------------------------------------------------------+

      .. container:: center

          

      .. container:: center

         --------------

      New interactive flagging is available in CASA 5.5 and later. You
      have a new button **Flag All**, which is located next to
      the **Unflag **\ button, and can turn on and off "Flag all/Unflag
      all" mode by clicking it. Instead of flag/unflag operation on
      selected region, the "Flag all/Unflag all" mode allows you to
      flag/unflag whole data associated with the grid. The usage of this
      mode is as follows:

      #. Press the **Flag All** button -- You now enter the "Flag
         all/Unflag all" mode. Background color of completely flagged
         grids will become yellow.
         |image5|
      #. Select grids to flag/unflag -- You can click each grid to
         select for flag/unflag when the mode is active. Unflag is
         selected for the grids where all data are already flagged,
         otherwise flag is selected. The background color of the grids
         selected for flag will change to yellow while the grids
         selected for unflag will change to the default color.
         |image6|
      #. Press the **Flag All** button again -- You now leave the "Flag
         all/Unflag all" mode. At this moment, flag/unflag operations
         are applied to the data of the currently displayed grids
         selected in the previous step, and each grid is updated
         accordingly. 
         |image7|

      .. container:: alert-box

         WARNING:  On macOS, the "Flag all/Unflag all" mode doesn't work
         as expected!

      On macOS, background color of grids doesn't yet change properly
      although flag/unflag operations work fine. It is not recommended
      to use this mode on macOS.

      .. container:: alert-box

         WARNING:  You cannot "undo" flagging to a previous state!

      plotms does not automatically create flag backups in
      the<msname>.flagversionsfile. It is thus recommended to save the
      initial flags with the flagmanagertaskbefore starting
      plotmsinteractive flagging. Important intermediate flagging stages
      may also be saved during plotmsflagging in the same fashion. 
      Flagging can also be performed using the interactive msview task
      or scripted with the flagdata or flagcmd tasks.

      Flags can also be extended with options in
      the\ `Flag\ tab; <#2--flag-extensions--the-flag-tab>`__\ see this
      section for a more detailed description of these options. Flag
      extension enables the user to plot a subset of the data and extend
      the flagging to a wider set. In this release, the only functional
      extensions are over correlation and channel.

      .. container:: alert-box

         WARNING:  Use of flag extensions may lead to deletion of much
         more data than desired. Be careful!

      .. container:: alert-box

         WARNING:  Interactive flagging doesn't support a collaboration
         with Iteration buttons! 

      The flag/unflag operations are applied to currently displayed
      grids only, although you can move to other iterations in the "Flag
      all/Unflag all" mode.

      --------------

      .. rubric:: 8. Scripting With No GUI
         :name: scripting-with-no-gui

      When scripting to produce exported plotfiles, you may want to set
      the plotms parameter showgui=False to suppress the GUI and pop-up
      dialog boxes.  The default is True.

      --------------

      .. rubric:: 9. Exiting plotms
         :name: exiting-plotms

      To exit the plotmsGUI, select\ *Quit*\ from the\ *File*\ menu at
      the top of the plotmswindow. You can also dismiss the window by
      killing it with the “X” on the frame.

      Alternatively, you can just leave it alone, and plotmswill keep
      running in the background and update with each subsequent plotms
      call. If the data file changes in the background while you are
      using other tasks, you can force reloading the data via the Reload
      checkbox next to the Plot button, or press SHIFT while clicking on
      Plot for the same purpose.

      If started in a casa session, plotms will automatically quit when
      the session is ended.

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/plotms1-1.png/@@images/5344d21a-413d-4869-8a37-65755bb81513.png
   :class: image-inline
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/axestab.png/@@images/319549be-314e-4b16-ae69-babf3975e859.png
   :class: image-inline
.. |Plotms Plot Page Tab| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/plotms-plot-page-tab-4.png/@@images/ebbc7bf8-8540-4763-a96f-ba461d181e3b.png
   :class: image-inline
   :width: 591px
   :height: 384px
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/flagtab-4.png/@@images/a098d399-95d7-4fbe-92f1-f964723e0cee.png
   :class: image-inline
.. |image4| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/2x2grid_figure.png/@@images/8d0ce94a-d26d-4242-abe0-58250c9e5cf4.png
   :class: image-inline
.. |image5| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/plotms-flagall-enter.png/@@images/95094082-86cb-4553-87cf-653655cbd904.png
   :class: image-inline
.. |image6| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/plotms-flagall-select.png/@@images/3378e978-b944-405f-9148-91cb8830b550.png
   :class: image-inline
.. |image7| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/plotms-flagall-leave.png/@@images/1d41b321-6636-4293-b579-e0ec84454bd8.png
   :class: image-inline
   :name: __mcenew
