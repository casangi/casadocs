

.. _Description:

Description
   **plotms** is a task for plotting and interacting with visibility
   data. A variety of axes choices (including data column) along with
   MS selection and averaging options are provided.  All of the
   provided parameters can also be set using the GUI once the
   application has been launched.  Additional operations are
   available through the GUI such as marking a region then using the
   *Locate tool* to list information about the points in the plot, or
   using the *Flag* and *Unflag* tools to change the flags in the
   marked region. Flag extension parameters are also available for
   flagging operations in the plotter.
   
   Support for calibration table plotting is included in plotms. 
   Most basic plotms functions (plotting, selection, averaging,
   iteration, locate, summary, flagging) will work for most CalTables.
   Parameterized CalTables (delay, antpos, gaincurve, opacity, fringefit)
   will currently just plot the simple parameters contained in the table.
   Baseline-based A and M tables are supported; X tables are not yet
   supported. Transformations (velocity conversions, etc.) are
   currently unsupported for CalTables.  In the **plotms** GUI, many 
   options irrelevant for CalTables (some selection and axis choices)
   are not hidden when interacting with a calibration table, and such
   settings will be ignored (when benign) or cause an error message.
   
   In CASA5, the return value of **plotms** is a Boolean *True* or *False*,
   where *True* indicates that the supplied parameters were processed
   successfully with no errors; however, a plot may or may not have
   been produced.  For example, a null selection returns *True* with
   no plot, but an invalid argument or combination of arguments
   returns *False*.  In CASA6, **plotms** has no return value but
   may throw an exception.
   
   For a detailed explanation of the **plotms** GUI and its
   corresponding task parameters, see the `documentation on using
   plotms <../../notebooks/data_examination.ipynb#Plot/Edit-using-plotms>`__
   under Data Examination and Editing.
   
   .. rubric:: Parameter Descriptions
   
   The options for each parameter are explained in detail below. The
   parameter’s default value, if any, will be described.
   
   .. rubric:: Plotter settings
   
   -  *showgui*
   
      -  Whether to show or hide the GUI window
      -  True (default): show the GUI window (False=hide).
      -  The casaplotms process runs in the background whether the
         GUI is shown or not.
   
   .. rubric:: Input Dataset
   
   -  *vis*
   
      -  The directory name of the input MeasurementSet or CalTable.
         The path is needed if this directory is not in the current
         working directory.
      -  “” (default) : launch casaplotms without plotting.
      -  If input file not found: plotms issues a warning and does
         not launch or, if already launched, does not update.
   
   .. rubric:: Page and Subplot Settings
   
   -  *gridrows*
   
      -  Number of subplot rows in each page of plots. There is no
         maximum, but consider legibility for larger grids.
      -  1 (default): one plot per row
   
   -  *gridcols*
   
      -  Number of subplot columns in each page of plots There is no
         maximum, but consider legibility for larger grids.
      -  1 (default): one plot per column
   
   -  *rowindex*
   
      -  Row location of this subplot (0-based), used to indicate
         location of plot in grid.  If *iteraxis* is enabled for the
         subplot, this indicates where to put the first plot.
      -  0 (default): locate the plot in the first row.
   
   -  *colindex*
   
      -  Column location of this subplot (0-based), used to indicate
         location of plot in grid.  If *iteraxis* is enabled for the
         subplot, this indicates where to put the first plot.
      -  0 (default): locate the plot in the first column.
   
   -  *plotindex*
   
      -  Index of subplot (0-based). When there is more than one plot
         on a page (overplot or on a grid without iteration), each
         plot should increment the plotindex by 1 and set
         *clearplots=False*.  If a plotindex is skipped, plotms will
         adjust the plotindex with a message to the user.
      -  0 (default): first (and possibly only) plot
   
   -  *clearplots*
   
      -  Make a new plot (remove existing plots) or overplot/add plot
         to grid.
      -  True (default): make a new plot.
   
   .. rubric:: Iteration
   
   *iteraxis*
   
   -  axis over which to iterate plots, one per page or per grid
      location.
   -  “” (default) : no iteration.
   -  Options: *'scan', 'field', 'spw', 'baseline', 'antenna',
      'time', 'corr'*.
   -  Each plot shows all of the points in the cache associated with
      the current iteration value.  This means that when iterating
      over '*antenna'* for a CalTable, the plot for the reference
      antenna shows all of the other antennas, since their baselines
      include the reference antenna.
   -  Iteration changes the plot title, appending the iteraxis and
      the iteration value, e.g. “Amp vs. Time Spw: 9”.
   -  Subparameters are enabled when iteraxis is set:
   
   -  *xselfscale, yselfscale*
   
      -  all axes in iterated plots will have the same scale (axis
         range and tick marks).
      -  False (default) : scale the each plot individually.
   
   -  *xsharedaxis, ysharedaxis*
   
      -  iterated plots on a grid share a single x-axis (top or
         bottom of the grid) in each column, or a single y-axis (left
         or right of the grid) in each row. Must also set
         *xselfscale=True, yselfscale=True*.
      -  False (default) : each plot has its own x-axis and y-axis.
      -  *xsharedaxis=True* ignored with warning when *gridrows=1.*
      -  *ysharedaxis=True* ignored with warning when *gridcols=1*.


   .. rubric:: Axes and Calibration
   
   -  *xaxis, yaxis*
   
      -  What to plot on the xaxis and yaxis
      -  “” (default) : use the default axis for the dataset
      -  Default xaxis
   
         -  For MeasurementSets, the default xaxis is *‘time’*.
         -  For CalTables, the default xaxis depends on the cal table type.  For most types, this is *‘time’*, i.e. for G Jones and GSPLINE; *‘chan’* for B Jones and B TSYS; *‘freq’* for BPOLY; *‘ant1’* for D Jones, K Jones, and KAntPos.
   
      -  Default yaxis
   
         -  For MeasurementSets, the default yaxis is *‘amp’*.
         -  For CalTables, the default yaxis depends on the cal table type. For most types, this is *‘gainamp’*. For K Jones (delay) and Fringe Jones (fringefit) tables the default is *‘delay’*. For KAntPos Jones tables, the default is *‘antpos’*. For GSPLINE tables, the default yaxis depends on the POLY_MODE column: if “AMP”or “A&P” the default is *‘gainamp’*, if “PHAS” the default is *‘gainphase’*.
   
      -  yaxis can be a list, e.g. *yaxis=[‘amp’,’phase’]* to plot
         more than one yaxis for a dataset on the same plot. You may
         choose to set different axis locations for multiple yaxes
         (see *yaxislocation*).
      -  Subparameters *xdatacolumn* and *ydatacolumn* are enabled
         when *xaxis* and *yaxis* are visibility axes, respectively.
   
   -  Axis options, with synonyms in parentheses and ordered by type,
      are in the following subsections.
   
   .. rubric:: Metadata Axes
   
   -  *‘scan’*
   
      -  scan number from the *SCAN_NUMBER* column, as shown in
         `listobs <../../api/casatasks.rst>`__.
      -  When averaging over scans is enabled, the scan value for
         each bin is the first scan number in the averaged data,
         independent of unflagged/flagged data.

   -  *‘field’*
   
      -  index from the *FIELD_ID* column which references a row in
         the *FIELD* subtable, as shown in
         `listobs <../../api/casatasks.rst>`__.
      -  When averaging over fields is enabled, the field value for
         each bin is the first field id in the averaged data,
         independent of unflagged/flagged data.

   -  *‘time’*
   
      -  timestamps from the *TIME* column, converted for display to
         time format HH:MM:SS.S (precision depends on the interval
         between tick marks).
      -  When time averaging is enabled, the average of the timestamps
         in each bin is used for the time values.

   -  *‘interval’* (*‘timeint’, ‘timeinterval’, ‘time_interval’*)
   
      -  integration time values from the *INTERVAL* column, in
         seconds.
      -  Not supported for CalTables.
   
   -  *‘spw’*
   
      -  spectral window IDs, as shown in
         `listobs <../../api/casatasks.rst>`__.
      -  For MeasurementSets, the data description ID is used to
         reference a row in the *DATA_DESCRIPTION* subtable, then the
         spw index value is retrieved from the row’s
         *SPECTRAL_WINDOW* column. This index references a row in the
         *SPECTRAL_WINDOW* subtable.
      -  For CalTables, the index from the main table
         *SPECTRAL_WINDOW* column which references a row in the
         *SPECTRAL_WINDOW* subtable.
   
   -  *‘chan’* (*‘channel’*)
   
      -  index into the number of channels in the selected spws,
         ranging 0~nChan.
      -  When channel averaging is enabled, the channel numbers
         are re-indexed starting at 0 to reflect the bin
         number, not the averaged channel number.
   
   -  ‘ *freq’* (*‘frequency’*)
   
      -  the *CHAN_FREQ* column in the *SPECTRAL_WINDOW* subtable, in
         GHz.  This is an array of frequencies, one per channel.
      -  The frame can be set with the *freqframe* parameter.
      -  When channel averaging is enabled, the average of the
         frequencies in each bin is used.

   -  *‘vel’* (*‘velocity’*)
   
      -  velocity in km/s, as defined by the *freqframe*, *veldef*,
         and *restfreq* parameters. Converted from frequencies
         ('*freq*') using the
         `measures <../../api/casatools.rst>`__
         (me) tool.
      -  Not supported for CalTables.
      -  When channel averaging is enabled, the average of the
         velocities in each bin is used.
   
   -  *‘corr’* (*‘correlation’*)
   
      -  correlation IDs (for MeasurementSets) or polarization IDs
         (for CalTables).
      -  For MeasurementSets, the data description ID is used to
         reference a row in the *DATA_DESCRIPTION* subtable, then the
         polarization index value is retrieved from the row’s
         *POLARIZATION_ID* column. This index references a row in the
         *POLARIZATION* subtable and the values are obtained from the
         *CORR_TYPE* column. These IDs correspond to values RR (5),
         RL (6), LR (7), LL (8), XX (9), XY (10), YX (11), and
         YY (12).
      -  For CalTables, this is the index into the number of
         polarizations in the first axis of the array in the
         *CPARAM/FPARAM* column. The CalTable’s PolBasis keyword may
         indicate whether the polarizations are linear (0=X, 1=Y) or
         circular (0=R, 1=L).  If not, the index 0 or 1 is used.
         For antenna position (KAntPos Jones) tables, *'corr'* refers
         to the x, y, and z position offsets in the first axis of the
         *FPARAM* column.
   
   -  *‘ant1’* (*‘antenna1’*)
   
      -  the ID of the first antenna in a baseline pair, as shown in
         `listobs <../../api/casatasks.rst>`__.
      -  index from the *ANTENNA1* column which references a row in
         the *ANTENNA* subtable.
   
   -  *‘ant2’* (*‘antenna2’*)
   
      -  the ID of the second antenna in a baseline pair, as shown in
         `listobs <../../api/casatasks.rst>`__.
      -  index from the *ANTENNA2* column which references a row in
         the *ANTENNA* subtable.
      -  Some CalTables have antenna2 IDs of -1, indicating this
         column is irrelevant to the table.
   
   -  *‘baseline’*
   
      -  unique number for all antenna baselines, computed as follows
         for a particular row (where ant1 is the antenna1 ID and ant2
         is the antenna2 ID for that row):
         (nAnts+1)*ant1-(ant1*(ant1+1))/2+ant2
   
   -  *‘row’*
   
      -  index into the number of rows, ranging 0~nRow.
      -  For a selected table (see *selectdata*), these are not the
         same as the row numbers in the original MeasurementSet.
      -  Not supported for CalTables.
   
   -  *‘observation’*
   
      -  index from the *OBSERVATION_ID* column which references a
         row in the *OBSERVATION* subtable, which contains
         information about the observer, project, and telescope as
         shown in
         `listobs <../../api/casatasks.rst>`__.
      -  Some CalTables have observation IDs of -1, indicating this
         column is irrelevant to the table. Often there is no
         *OBSERVATION* subtable.
   
   -  *‘intent’*
   
      -  index from the *STATE_ID* column which references a row in
         the *STATE* subtable.  This includes OBS_MODE information
         about the Scan Intent as shown in
         `listobs <../../api/casatasks.rst>`__.
      -  Some MeasurementSets and CalTables have state IDs of -1,
         indicating this column is irrelevant to the table. Often
         there is no *STATE* subtable or it has zero rows.
   
   -  *‘feed1’*
   
      -  the first feed number, most useful for single-dish data with
         multi-feed receivers.
      -  index from the *FEED1* column which references a row in the
         *FEED* subtable.
      -  Not supported for CalTables.
   
   -  *‘feed2’*
   
      -  the second feed number, most useful for single-dish data
         with multi-feed receivers.
      -  index from the *FEED2* column which references a row in the
         *FEED* subtable.
      -  Not supported for CalTables.
   
   .. rubric:: Visibility and Flag Axes
   
   -  *‘amp’* (*‘amplitude’*)
   
      -  amplitude of the complex visibility cube from the
         MeasurementSet data column specified in the *datacolumn*
         parameter.
      -  If only the *FLOAT_DATA* column exists, the float values are
         plotted and the axis is labeled “Amp:float”.
      -  For residual data columns, vector (complex) subtraction or
         division occurs before the amplitude is computed.  When
         averaging is enabled, the averaged data for each column is
         used for the subtraction or division, then the amplitude is
         taken.
      -  For CalTables with complex parameters (*CPARAM* column),
         this axis is relabeled “Gain Amp”. For CalTables with float
         parameters (*FPARAM* column), the float values are plotted
         and the axis is relabeled appropriately, e.g. "Delay",
         "SwPower", "Tsys", "Opac", etc.
   
   -  *‘phase’*
   
      -  phase of the complex visibility cube from the MeasurementSet
         data column specified in the *datacolumn* parameter, in
         degrees.
      -  Not valid if only non-complex *FLOAT_DATA* column exists.
      -  For residual data columns, vector (complex) subtraction or
         division occurs before the phase is computed.  When
         averaging is enabled, the averaged data for each column is
         used for the subtraction or division, then the phase is
         taken.
      -  For CalTables with complex parameters (*CPARAM* column),
         this axis is relabeled “Gain Phase”. Not valid for CalTables
         with non-complex float parameters (*FPARAM* column).
   
   -  *‘real’*
   
      -  the real part of the complex visibility cube from the
         MeasurementSet data column specified in the *datacolumn*
         parameter.
      -  If only the *FLOAT_DATA* column exists, the float values are
         plotted and the axis is labeled “Amp:float”.
      -  For residual data columns, vector (complex) subtraction or
         division occurs before the real part is computed.  When
         averaging is enabled, the averaged data for each column is
         used for the subtraction or division, then the real part is
         taken.
      -  For CalTables with complex parameters (*CPARAM* column),
         this axis is relabeled ‘Gain Real’. Not valid for CalTables
         with non-complex float parameters (*FPARAM* column).
   
   -  *‘imag’* (*‘imaginary’*)
   
      -  the imaginary part of the complex visibility cube from the
         MeasurementSet data column specified in the *datacolumn*
         parameter.
      -  Not valid if only non-complex *FLOAT_DATA* column exists.
      -  For residual data columns, vector (complex) subtraction or
         division occurs before the imaginary part is computed.  When
         averaging is enabled, the averaged data for each column is
         used for the subtraction or division, then the imaginary
         part is taken.
      -  For CalTables with complex parameters (*CPARAM* column),
         this axis is re-labeled ‘Gain Imag’. Not valid for CalTables
         with non-complex float parameters (*FPARAM* column).
   
   -  *‘wt’* (*‘weight’*)
   
      -  values from the *WEIGHT* column, which reflects how much
         weight each corrected data sample (*CORRECTED_DATA* column)
         should receive when combined, e.g. in averaging. See also
         chapter on `Data
         Weights <../../notebooks/data_weights.ipynb>`__.
      -  Not supported for CalTables.
   
   -  *‘wtamp’* (*‘wt*amp’*)
   
      -  product of the weight from the *WEIGHT* column and the
         amplitude of the visibility cube from the requested data
         column.
         Not supported for CalTables.
   
   -  *‘wtsp’* (*‘weightspectrum’*)
   
      -  values from the *WEIGHT_SPECTRUM* column, which reflects
         per-channel frequency variations of the *WEIGHT* column. If
         this column does not exist, a warning is issued and *WEIGHT*
         is plotted instead. See also chapter on `Data
         Weights <../../notebooks/data_weights.ipynb>`__.
      -  Not supported for CalTables.
   
   -  *‘sigma’*
   
      -  values from the *SIGMA* column, which reflects the rms noise
         of the *DATA* column.  See also chapter on `Data
         Weights <../../notebooks/data_weights.ipynb>`__.
      -  Not supported for CalTables.
   
   -  *‘sigmasp’* (*‘sigmaspectrum’*)
   
      -  values from the *SIGMA_SPECTRUM* column, which reflects
         per-channel frequency variations of the *SIGMA* column. If
         this column does not exist, the values are derived.  See
         also chapter on `Data
         Weights <../../notebooks/data_weights.ipynb>`__.
      -  Not supported for CalTables.
   
   -  *‘flag’*
   
      -  boolean values from the *FLAG* column (0=unflagged,
         1=flagged).
   
   -  *‘flagrow’*
   
      -  boolean values from the *FLAG_ROW* column (0=no flags in
         row, 1=flags in row).
      -  This can be inconsistent with *FLAG*, as it is not always
         updated as flags are changed.
   
   .. rubric:: Observational Geometry Axes
      
   
   -  *‘uvdist’*
   
      -  uv distance (baseline separations), in meters. Calculated as
         sqrt(u*u+v*v), where u and v are values from the *UVW*
         column
         Not supported for CalTables.
   
   -  *‘uvwave’* (*’uvdistl’, ’uvdist_l’*)
   
      -  uv distance (baseline separations) as a function of
         frequency, in units of the observing wavelength λ (lambda).
      -  Not supported for CalTables.
   
   -  *‘u’*
   
      -  u in meters, from the *UVW* column.
      -  Not supported for CalTables.
   
   -  *‘v’*
   
      -  v in meters, from the *UVW* column.
      -  Not supported for CalTables.
   
   -  *‘w’*
   
      -  w in meters, from the *UVW* column.
      -  Not supported for CalTables.
   
   -  *‘uwave’*
   
      -  u in units of wavelength λ (lambda).
      -  Not supported for CalTables.
   
   -  *‘vwave’*
   
      -  v in units of wavelength λ (lambda).
      -  Not supported for CalTables.
   
   -  *‘wwave’*
   
      -  w in units of wavelength λ (lambda).
      -  Not supported for CalTables.
   
   -  *‘azimuth’*
   
      -  azimuth for the entire array, in degrees. Calculated from
         the *FIELD* table’s *PHASE_DIR* column and the observatory
         position, using the
         `measures <../../api/casatools.rst>`__
         (me) tool.
      -  Not supported for CalTables.
   
   -  *‘elevation* ’
   
      -  elevation for the entire array, in degrees. Calculated from
         the *FIELD* table’s *PHASE_DIR* column and the observatory
         position, using the
         `measures <../../api/casatools.rst>`__
         (me) tool.
      -  Not supported for CalTables.
   
   -  *‘hourang’* (*‘hourangle’*)
   
      -  hour angle for the entire array, in units of hours.
         Calculated from the FIELD table’s *PHASE_DIR* column and the
         observatory position, using
         the `measures <../../api/casatools.rst>`__
         (me) tool.
      -  Not supported for CalTables.
   
   -  *‘parang’* (*‘parangle’, ‘parallacticangle’*)
   
      -  parallactic angle for the entire array, in degrees.
         Calculated from the FIELD table’s *PHASE_DIR* column and the
         observatory position, using
         the `measures <../../api/casatools.rst>`__
         (me) tool .
      -  Not supported for CalTables.
   
   -  *‘antenna’* (*‘ant’*)
   
      -  antenna IDs in range 0~nAnt, for plotting antenna-based
         quantities.
      -  For CalTables with no antenna2 IDs, ‘antenna’ is the same as
         ‘antenna1’.
   
   -  *‘ant-azimuth’*
   
      -  azimuth for each antenna, in degrees. Calculated from the
         *FIELD* table’s *PHASE_DIR* column and the positions in the
         *ANTENNA* table, using
         the `measures <../../api/casatools.rst>`__
         (me) tool.
      -  Not supported for CalTables.
   
   -  *‘ant-elevation’*
   
      -  elevation for each antenna, in degrees. Calculated from the
         *FIELD* table’s *PHASE_DIR* column and the positions in the
         *ANTENNA* table, using
         the `measures <../../api/casatools.rst>`__
         (me) tool.
      -  Not supported for CalTables.
   
   -  *'ant-ra'*
   
      -  Only implemented for ALMA, ASTE, and NRO data.
      -  longitude of the direction to which the first antenna of a
         baseline points at data-taking timestamps. Calculated by
         interpolating at data-taking timestamps POINTING table's
         DIRECTION column, and converting the result to a
         user-specified reference frame. See xinterp, yinterp and
         xframe, yframe parameters below for supported interpolation
         methods and reference frames.
      -  Not supported for CalTables.
      -  Averaging not supported.
   
   -  *'ant-dec'*
   
      -  Only implemented for ALMA, ASTE, and NRO data.
      -  latitude of the direction to which the first antenna of a
         baseline points at data-taking timestamps. Calculated by
         interpolating at data-taking timestamps POINTING table's
         DIRECTION column, and converting the result to a
         user-specified reference frame. See xinterp, yinterp and
         xframe, yframe parameters below for supported interpolation
         methods and reference frames.
      -  Not supported for CalTables.
      -  Averaging not supported.
   
   -  *‘ant-parang’* (*‘ant-parangle’, ‘ant-parallacticangle’*)
   
      -  parallactic angle for each antenna, in degrees. Calculated
         from the *FIELD* table’s *PHASE_DIR* column and the
         positions in the *ANTENNA* table, using
         the `measures <../../api/casatools.rst>`__
         (me) tool.
      -  Not supported for CalTables.
   
   .. rubric:: Calibration Axes
   
   -  *‘gainamp’* (*‘gamp’*)
   
      -  Invalid for MeasurementSets.
      -  amplitude of complex gain parameters (*CPARAM* column). For
         CalTables with float parameters (*FPARAM* column), the float
         values are plotted.  For polynomial CalTables, including
         BPOLY and GSPLINE, the viscube values are calculated
         according to the *POLY_MODE* and their amplitudes are
         plotted.
      -  When the default *xaxis* or *yaxis* parameter (“”) is used,
         the *gainamp* axis is relabeled with the axis appropriate
         for the table type.  However, when the xaxis or yaxis is
         explicitly set to *‘gainamp’*, the axis is labeled ”Gain
         Amplitude” although the float parameter values may actually
         be Tsys, opacity, etc.
   
   -  *‘gainphase’* (‘ *gphase’*)
   
      -  Invalid for MeasurementSets.
      -  phase of complex gain parameters (*CPARAM* column). Invalid
         for CalTables with float parameters (*FPARAM* column).  For
         polynomial CalTables, including BPOLY and GSPLINE, the
         viscube values are calculated according to the *POLY_MODE*
         and their phases are plotted.
   
   -  *‘gainreal’* (*‘greal’*)
   
      -  Invalid for MeasurementSets.
      -  real part of complex gain parameters (*CPARAM* column).
         Invalid for CalTables with float parameters (*FPARAM*
         column).  For polynomial CalTables, including BPOLY and
         GSPLINE, the viscube values are calculated according to the
         *POLY_MODE* and the real part is plotted.
   
   -  *‘gainimag’* (*‘gimag’*)
   
      -  Invalid for MeasurementSets.
      -  imaginary part of complex gain parameters (*CPARAM* column).
         Invalid for CalTables with float parameters (*FPARAM*
         column).  For polynomial CalTables, including BPOLY and
         GSPLINE, the viscube values are calculated according to the
         *POLY_MODE* and their phases are plotted.
   
   -  *‘delay* ’ (*‘del’*)
   
      -  Invalid for MeasurementSets.
      -  delay values of a delay or fringefit CalTable, from the *FPARAM* column.
         Invalid for other CalTable types.
   
   -  *‘delayrate* ’ (*‘rate’*)
   
      -  Invalid for MeasurementSets.
      -  delay rates of a fringefit CalTable, from the *FPARAM* column.
         Invalid for other CalTable types.
   
   -  *‘dispdelay* ’ (*‘disp’*)
   
      -  Invalid for MeasurementSets.
      -  dispersive delay values of a fringefit CalTable, from the *FPARAM* column.
         Invalid for other CalTable types.
   
   -  *‘swpower’* (*‘swp’, ‘switchedpower’, ‘spgain’*)
   
      -  Invalid for MeasurementSets.
      -  switched power values for a VLA switched power CalTable,
         from the *FPARAM* column. Invalid for other CalTable types.
   
   -  *‘tsys’*
   
      -  Invalid for MeasurementSets.
      -  tsys of a Tsys CalTable, from the *FPARAM* column. Invalid
         for otherCalTable types.
   
   -  *‘opacity’* (*‘opac’*)
   
      -  Invalid for MeasurementSets.
      -  opacity of an opacity CalTable, from the *FPARAM* column.
         Invalid for other CalTable types.
   
   -  *‘snr’*
   
      -  Invalid for MeasurementSets.
      -  signal-to-noise ratio of a CalTable, from the *SNR* column.
   
   -  *‘tec’*
   
      -  Invalid for MeasurementSets.
      -  total electron content of an ionosphere correction CalTable,
         from the *FPARAM* column. Invalid for other CalTable types.
   
   .. rubric:: Ephemeris Axes
   
   -  *‘radialvelocity’*
   
      -  radial velocity of an ephemeris field, in km/s. Valid only
         for MeasurementSets whose *FIELD* subtable has an ephemeris
         table.
      -  Invalid for CalTables.
   
   -  *‘distance’* (*‘rho’*)
   
      -  distance (rho) of an ephemeris field, in km. Valid only for
         MeasurementSets whose *FIELD* subtable has an ephemeris
         table.
      -  Invalid for CalTables.
   
   .. rubric:: Other Axis Settings
   
   -  *xdatacolumn, ydatacolumn*
   
      -  data column in the MeasurementSet from which to retrieve
         visibilities
      -  “” (default) : ‘ *data* ’ (*DATA* column).
      -  Subparameters of visibility axes only.
      -  If a data column other than ‘ *data’* is selected, the
         visibility axis in the plot title is appended with the data
         column name, e.g. “Amp:corrected vs. Time”.
      -  For residual data columns:
   
         -  Vector (complex) subtraction or division occurs before
            the axis operation (amplitude, phase, real, imaginary) is
            computed.
         -  When the '*corrected/model*' or '*data/model*' data
            column is selected, some of the resulting values may be
            infinite or "not a number" due to division by zero. 
            These values are ignored when plotting.
         -  When averaging is enabled, each column's data is
            averaged, then it is subtracted or divided, then the axis
            operation is computed.
         -  Data residual columns *‘data-model’* and *‘data/model’*
            are invalid for singledish datasets.  There are no float
            residual columns.
   
      -  Options:
   
         -  *‘data’*
   
            -  raw data. Use the *DATA* column in the MeasurementSet.
            -  For singledish datasets, a warning is issued and
               *FLOAT_DATA* is plotted with ":float" appended to the
               visibility axis label.
   
         -  *‘corrected’*
   
            -  calibrated data. Use the *CORRECTED_DATA* column in
               the MeasurementSet, or use on-the-fly calibration if
               *callib* parameter is set. Plotms will prefer OTF
               calibration over an existing *CORRECTED_DATA* column.
            -  If no calibrated data can be used, a warning is issued
               and the raw data (*DATA* or *FLOAT_DATA*) is plotted
               instead.
   
         -  *‘model’*
   
            -  model data. Use the *MODEL_DATA* column in the
               MeasurementSet.
            -  For interferometry datasets, model data is created
               dynamically if it does not exist.
            -  For singledish datasets with no model data, an error
               is issued and no plot is made.
   
         -  *‘float’*
   
            -  non-complex data.  Use the *FLOAT_DATA* column in the
               MeasurementSet. Primarily for single-dish data.
            -  Fails if *FLOAT_DATA* does not exist.
   
         -  *’corrected-model’* ('*corrected-model_vector'*, *’residual’)*
   
            -  subtract the model data from the corrected data before
               the amplitude, phase, etc. is calculated.
            -  For interferometry datasets with no corrected data and
               cannot be generated with the *callib* parameter, a
               warning is issued and '*data-model_vector*' is
               plotted.
            -  For singledish datasets with no corrected data and/or
               no model data, an error is issued and no plot is made.
   
         -  *’corrected-model_scalar’*
   
            -  subtract the model data from the corrected data after
               the amplitude, phase, etc. is calculated.
            -  For interferometry datasets with no corrected data and
               cannot be generated with the *callib* parameter, a
               warning is issued and '*data-model_scalar*' is
               plotted.
            -  For singledish datasets with no corrected data and/or
               no model data, an error is issued and no plot is made.
   
         -  *‘data-model’* ('*data-model_vector'*)

            -  subtract the model data from the raw data before the
               amplitude, phase, etc. is calculated.
            -  For interferometry datasets, model data is created
               dynamically if it does not exist.
            -  Invalid for singledish datasets: no data or model
               columns. An error is issued and no plot is made.
   
         -  *‘data-model'* ('*data-model_scalar'*)
   
            -  subtract the model data from the raw data after the
               amplitude, phase, etc. is calculated.
            -  For interferometry datasets, model data is created
               dynamically if it does not exist.
            -  Invalid for singledish datasets: no data or model
               columns. An error is issued and no plot is made.
   
         -  *‘corrected/model’ ('corrected/model_vector')*
   
            -  divide the corrected data by the model data before the
               amplitude, phase, etc. is calculated.
            -  For interferometry datasets with corrected data, model
               data is created dynamically if it does not exist.
            -  For interferometry datasets with no corrected data and
               cannot be generated with the *callib* parameter, a
               warning is issued and '*data/model_vector*' is
               plotted.
            -  For singledish datasets with no corrected data and/or
               no model data, an error is issued and no plot is made.
   
         -  *'corrected/model_scalar'*
   
            -  divide the corrected data by the model data after the
               amplitude, phase, etc. is calculated.
            -  For interferometry datasets with corrected data, model
               data is created dynamically if it does not exist.
            -  For interferometry datasets with no corrected data and
               cannot be generated with the *callib* parameter, a
               warning is issued and '*data/model_scalar*' is
               plotted.
            -  For singledish datasets with no corrected data and/or
               no model data, an error is issued and no plot is made.
   
         -  *‘data/model’* ('*data/model_vector'*)
   
            -  divide the raw data by the model data before the
               amplitude, phase, etc. is calculated..
            -  For interferometry datasets, model data is created
               dynamically if it does not exist.
            -  Invalid for singledish datasets: no data or  model
               columns.  An error is issued and no plot is made.
   
         -  '*data/model_scalar*'
   
            -  divide the raw data by the model data after the
               amplitude, phase, etc. is calculated..
            -  For interferometry datasets, model data is created
               dynamically if it does not exist.
            -  Invalid for singledish datasets: no data or  model
               columns.  An error is issued and no plot is made.
   
   -  *xinterp, yinterp*
   
      -  *Sub-parameter of xaxis (resp. yaxis) when xaxis='ant-ra' or
         xaxis='ant-dec' (resp. yaxis='ant-ra' or yaxis='ant-dec')*
      -  *Interpolation method to use for interpolating antennas'
         pointing directions recorded in MeasurementSet's POINTING
         table (DIRECTION and TIME columns) at data-taking timestamps
         (MAIN table, TIME column)*
      -  *(default) : ‘ cubic spline ’*
      -  *Options: 'cubic spline', 'spline', 'nearest'*
   
         -  *'spline' is a synonym for 'cubic spline'*
   
   -  *xframe, yframe*
   
      -  *Sub-parameter of xaxis (resp. yaxis) when xaxis='ant-ra' or xaxis='ant-dec' (resp. yaxis='ant-ra' or yaxis='ant-dec')*
      -  *Convert antennas' interpolated pointing directions to the supplied reference frame*
      -  *“” (default) : ‘icrs’*
      -  *Options: 'icrs', 'j2000','b1950','galactic','azelgeo'*
   
   -  *yaxislocation*
   
      -  whether to put the yaxis on the left or right.
      -  “” (default) : left.
      -  Options: *‘left’*, *‘right’*
      -  Can be a string or list when yaxis is a list, e.g.
         (yaxis=[‘amp’, ‘phase’], yaxislocation=[‘left’, ‘right’])
         will plot amp on the left yaxis and phase on the right
         yaxis.
      -  xaxis location can be set in the GUI but there is no
         corresponding parameter.
   
   -  *plotrange*

      -  format is [xmin, xmax, ymin, ymax]; when min=max=0,
         autoscaling is used.
      -  [] (default) : [0,0,0,0] to autoscale the x and y ranges.
      -  You may autoscale one axis and not the other.  For example,
         [0,0,0,10] will autoscale the xaxis but set the yaxis range
         to [0,10].
   
   -  *callib*

      -  calibration library string or filename to use for on-the-fly
         (OTF) calibration to produce calibrated data (the
         ‘ *corrected* ’ datacolumn).
      -  "" (default): no calibration library
      -  See `Cal Library Syntax
         documentation <../../notebooks/cal_library_syntax.ipynb>`__.
         When this parameter is set, OTF calibration is enabled. 
         Plotms will prefer OTF calibration over an existing
         *CORRECTED_DATA* column.
   
   -  .. rubric:: *showatm, showtsky, showimage*

      -  overplot the atmospheric transmission curve or the sky
         temperature curve, with the yaxis on the right. The *xaxis*
         must be *‘chan’* or ‘ *freq’*, else the plot is made
         without the overlay.
      -  False (default): no overlay.
      -  Only one overlay may be chosen. If both are True, only the
         atmospheric curve is computed and plotted.
      -  Overlays are computed with the
         `atmosphere <../../api/casatools.rst>`__
         (atm) tool using pressure, humidity, temperature, and
         precipitable water vapor (pwv) computed from the
         MeasurementSet subtables:
   
         -  The *WEATHER* subtable is used to compute mean weather
            values, else defaults are used. humidity: 20.0,
            temperature: 273.15, pressure: 563.0 (ALMA) or 786.0
            (other).
         -  The ALMA *ASDM_CALWVR* or *ASDM_CALATMOSPHERE* subtable
            is used to compute pwv, else defaults are used. 1.0
            (ALMA), 5.0 (other).
   
      -  When *showimage=True*, the image sideband curve is also
         plotted.  This feature can only be used when *showatm* or
         *showtsky* is True.  In addition, the MS (associated MS for
         a calibration table) cannot be split and must have an
         ASDM_RECEIVER table, or a warning is issued and the atm/tsky
         curve is plotted without the sideband curve.
   
   .. rubric:: Data Selection
   
   .. *selectdata*
   
   -  parameter to enable data selection.
   -  True (default) : data selection always enabled.
   -  See
      `MSSelection <../../notebooks/visibility_data_selection.ipynb>`__
      for syntax of subparameters below.  All arguments are strings.
   -  For all subparameters, “” (default) selects all (no selection).
   -  Selection is done before averaging, calibration, plotting, etc.
   -  Selection by uvrange, array, intent, and feed is invalid for
      CalTables, which do not have these columns.
   
   -  *field*
   
      -  select fields by name or ID.
   
   -  *spw*
   
      -  select spectral windows/channels.
   
   -  *timerange*
   
      -  select data based on time range.
   
   -  *uvrange*
   
      -  select data within uvrange (default meters), or include
         units: ‘0~1000klamba’.
      -  Not supported for CalTables.
   
   -  *antenna*
   
      -  select baselines and auto/cross-correlations for
         MeasurementSet and baseline-based CalTable.
      -  select antenna1 for antenna-based CalTable, including single-dish
         sky calibration table. Antenna-based CalTable with a reference
         antenna may use the ANT1&ANT2 syntax to select a reference antenna.
   
   -  *scan*

      -  select scan numbers.
   
   -  *correlation*

      -  select correlations for MeasurementSet.
      -  select polarizations for CalTable, including ratio plots. 
         Options include "RL", "R", "L", "XY", "X", "Y", and "/".
   
   -  *array*

      -  select array ID.
      -  Not supported for CalTables.
   
   -  *observation*

      -  select observation ID.
   
   -  *intent*

      -  select state ID or intent by name.
      -  Not supported for CalTables.
   
   -  *feed*

      -  select feed IDs by number.
      -  Note: as with antenna IDs, a single feed ID selection (e.g.
         *feed="1"*) will only select where feed1 or feed2 is the
         selected ID but not both, unless "auto-correlation"-like
         syntax is used .
      -  Not supported for CalTables.
   
   -  *msselect*

      -  select using TaQL expression.
   
   .. rubric:: Data Averaging

   *averagedata*

   -  parameter to enable data averaging.  
   -  True (default) : averaging always enabled.
   -  For all subparameters, “” or False (default) does no averaging.
   -  When averaging, plotms will prefer unflagged data. If an
      averaging bin contains any unflagged data at all, only the
      average of the unflagged will be shown. When flagging on a plot
      of averaged data, the flags will be applied to the unaveraged
      data in the MS.
   -  When plotting weight axes with averaging enabled, the values
      are the weights applied to the averaged data, i.e. it is the
      sum not the average of the weight values.
   -  Some axes are invalid or not implemented for some averaging
      modes.  For example, you cannot plot weight axes when baseline,
      averaging, spw, or scalar averaging is enabled.
   -  The result is a weighted average. When averaging corrected
      data, weight spectrum is used. When averaging raw data, sigma
      spectrum is used.
   -  Normally, the data averaged together has the same scan number,
      field, baseline, and spw.  Subparameters allow data to be
      averaged across these boundaries.
   -  By default, data uses vector averaging, where the complex
      average is formed by averaging the complex values of the
      visibilities, then the amplitude or phase of the result is
      plotted.  To compute the average of the amplitude or phase
      values instead, set *scalar=True*.
   -  Averaging is supported for calibration tables except BPOLY and
      GSPLINE, which have an older table format.
   
   -  *avgchannel*

      -  Average data across the channel axis; value is number of
         channels to average together to form one output channel.
      -  When plotting the *‘channel’* axis, output channel numbers
         are reindexed 0~nAvgChan, rather than using the average of
         the channel numbers in each bin, and the axis label is
         changed to “Average Channel”. When plotting the *‘frequency‘*
         or *‘velocity‘* axis, the average of the frequency or
         velocity values in each bin is used.
      -  The plotms Locate tool indicates which channels were
         averaged together for a point in the plot, e.g.
         “Chan=<7~13>” which may be shown as channel 1 on the plot.
         The frequency of the point is labelled "Avg Freq" in the
         Locate output.
      -  see
         `mstransform <../../api/casatasks.rst>`__
         description for channel averaging.
      -  Combining channel averaging with channel selection is handled
         differently for MeasurementSets and calibration tables.

         -  *‘MeasurementSet’*
   
            -  Each selected channel range is averaged separately.
            -  When the avgchannel value is less than the number of
               channels selected in a range, the channels in each
               range are binned together and extra channels are 
               dropped. For example, (spw='0:10~20; 30~40',
               avgchannel='8') will average channel bins [10~17] and
               [30~37] but drop channels [18~20] and [38~40]. Since
               each range is treated separately, the order of the
               channel ranges does not matter; (spw='0:30~40; 10~20',
               avgchannel='8') will have the same result.
            -  When the avgchannel value is greater than the
               number of channels selected in a range, if a single
               range is selected, all selected channels are binned;
               if multiple ranges are selected and the binning fails
               for both ranges, an error is issued: "Channel selection
               does not allow to produce any output channel with the
               requested width."  For example, (spw='0:10~20',
               avgchannel='15') will average channels [10~20].
               (spw='0:10~20; 30~40', avgchannel='15') will produce
               the error. (spw='0:10~20; 30~50', avgchannel='15') will
               average [30~44] only.

         -  *‘Calibration Table’*
   
            -  Selected channel ranges are treated as contiguous to
               increase SNR.
            -  When the avgchannel value is less than the number of
               channels selected, the channels are binned as if there
               were no gaps and extra channels are dropped. For
               example, (spw='0:10~20; 30~40', avgchannel='8') will
               average channel bins [10~17], [18~20, 30~34] to
               complete the bin, and drop [35~40]. The Locate tool
               will show the output channels as <10~17> and <18~34>.
               The order of the channel ranges does matter:
               (spw='0:30~40; 10~20', avgchannel='8') will bin
               [30~37], [38~40, 10~14] and drop [15~20].  The Locate
               tool will show the output channels as <30~37> and
               <38~14>.
            -  When the avgchannel value is greater than the
               number of channels selected in a range, if a single
               range is selected, all selected channels are binned;
               if multiple ranges are selected, the channels are
               binned as if there were no gaps.  For example,
               (spw='0:10~20', avgchannel='15') will average channels
               [10~20].  (spw='0:10~20; 30~40', avgchannel='15') will
               bin [10~20, 30~33] and drop [34~40].  The Locate tool
               will show the output channel as <10~33>.
               (spw='0:10~20; 30~50', avgchannel='15') will bin
               [10~20, 30~33], [34~48] and drop [49~50].  The Locate
               tool will show the output channels as <10~33> and
               <34~48>.  Changing the selection order changes the
               averaging: (spw='0:30~40; 10~20', avgchannel='15') will
               bin [30~40, 10~13] and drop [14~20].  The Locate tool
               will show the output channel as <30~13>.
    
   -  *avgtime*

      -  Average data across the time axis; value string is number of
         seconds to average together.
      -  "" (default): do not time-average data.
      -  The “bins” of averaged data have the same scan number and
         field ID unless avgscan or avgfield are True.
      -  The time value of each bin is the average of the timestamps
         in that bin.

   -  *avgscan*

      -  Ignore scan boundaries when time-averaging data; parameter
         ignored when *avgtime* is not set.
      -  False (default): time-average data within individual scans.
      -  The scan value of each bin is the first scan number in the
         bin, independent of unflagged/flagged data.

   -  *avgfield*

      -  Ignore field boundaries when time-averaging data; parameter
         ignored when *avgtime* is not set.
      -  False (default): time-average data within individual fields.
      -  The field value of each bin is the first field id in the
         bin, independent of unflagged/flagged data.

   -  *avgbaseline*

      -  Average data for all baselines together in each "chunk"
         (rows having the same scan number, field ID, spw, and
         correlation).
      -  False (default): do not average data over baseline.
      -  Exclusive with avgantenna.
   
   -  *avgantenna*

      -  Average data for each antenna separately in each "chunk"
         (rows having the same scan number, field ID, spw, and
         correlation).
      -  False (default): do not average data per antenna.
      -  Exclusive with avgbaseline.
   
   -  *avgspw*
   
      -  Average data over spectral window. For a given channel
         number, the channels in the spectral windows with that
         number are averaged together.
      -  False (default): do not average data over spectral window.
   
   -  *scalar*

      -  Values like amplitude or phase of the individual complex
         values are calculated before averaging.
      -  False (default) results in vector averaging: complex values
         are averaged, then the values for amp, phase, etc. are
         calculated.
      -  Ignored when other averaging is not enabled.
   
   .. rubric:: Data Transformations

   *transform*

   -  parameter to enable transformations.  Not implemented for
      CalTables.
   -  False (default) disables subparameters below.
   
   -  *freqframe*

      -  the coordinate frame in which to render frequency and
         velocity axes.
      -  “” (default) : use frame in which data were taken.
      -  Options: *"LSRK", "LSRD", "BARY", "GEO", "TOPO", "GALACTO", "LGROUP", "CMB"*
   
   -  *restfreq*

      -  the rest frequency to use in velocity conversions (MHz).
      -  “” (default) : use spw central frequency and show relative
         velocity.
   
   -  *veldef*

      -  the velocity definition (Doppler ratio) to use in velocity
         conversions.
      -  "*RADIO*" (default)
      -  Options: *“RADIO”, “OPTICAL”, “TRUE”* (Relativistic)
   
   -  *phasecenter*

      -  Direction coordinates of the desired phase center.
      -  "" (default) : use phase center in MeasurementSet.
   
   .. rubric:: Interactive Flagging Extensions
   
   *extendflag*

   -  parameter to enable flag extensions according to subparameters.
   -  False (default): do not extend flags.
   
   -  *extcorr*

      -  Extend flagging to unplotted correlations when
         *extendflag=True*, else ignored.
      -  False (default) : do not extend flagging by correlation.
      -  True : for example, if correlation RR is selected, plotted,
         and interactively flagged, correlations RL, LR, and LL will
         be flagged for the points in the marked region.
   
   -  *extchannel*

      -  Extend flagging to unplotted channels in the same spw when
         *extendflag=True*, else ignored.
      -  False (default) : do not extend flagging by channel.
      -  True : for example, if spw 0:0 (spw 0, channel 0) is
         selected, plotted, and interactively flagged, all channels
         in spw 0 will be flagged for the points in the marked
         region.
   
   .. rubric:: Display: Symbols

   *coloraxis*

   -  colorize the symbols based on the given axis. Points with the
      same value for that axis will be the same color.
   -  “” (default) : do not colorize.
   -  Options: *“scan”, “field”, “spw”, “antenna1”* (*“ant1”*),
      *“antenna2”* (*“ant2”*), *“baseline”, “channel”* (*“chan”*),
      *“corr”, “time”, “observation”, “intent”*
   -  Overrides custom symbol settings below and xconnector
      colorization.  Flagged points will be colorized according to
      the *coloraxis*.
   -  For CalTables, colorization by *"corr"* usually refers to 
      polarization.  For an antenna position (KAntPos Jones) table,
      the first axis contains the x, y, and z offsets so
      *coloraxis="corr"* may be used to distinguish these values.
   
   *customsymbol*

   -  parameter to enable custom symbol for unflagged data.
   
   -  False (default) : disables subparameters below, symbols use
      default values (“blue” autoscaling).
   
   -  *symbolshape*

      -  set the shape of the symbol for points plotted.
      -  *“autoscaling”* (default) changes the size according to the
         number of points; the shape is *“pixel”* for the highest
         range of points, *“circle”* otherwise.
      -  Options: *“autoscaling”, “circle”, “square”, “diamond”,
         “pixel”, “nosymbol”* (do not show points)
   
   -  *symbolsize*

      -  set size in number of pixels.
   
   -  *symbolcolor*

      -  set color by RGB hex code or string color name e.g. ‘red’.
      -  *"0000ff"* (default) is blue.
   
   -  *symbolfill*

      -  set fill pattern for symbol.
      -  *"fill"* (default).
      -  Options: *“fill”, “mesh1”, “mesh2”, “mesh3”, “nofill”*
   
   -  *symboloutline*

      -  outline the symbol.
      -  False (default).
   
   *customflaggedsymbol*

   -  parameter to enable custom symbol for flagged data.
   -  False (default) : disables subparameters below, shape is
      “nosymbol”.
   -  True: show flagged points as red circles of size 2 (default),
      unless subparameters are set otherwise.
   
   -  *flaggedsymbolshape="circle", flaggedsymbolsize=2, flaggedsymbolcolor="ff0000" (‘red’), flaggedsymbolfill="fill", flaggedsymboloutline=False*

      -  Subparameter defaults are shown.  Their options are the same
         as for unflagged symbols, when *customflaggedsymbol=True*.
   
   *xconnector*

   -  parameter to enable connecting the data points by line or step
      along the xaxis; connected points will have the same metadata
      (including flag) with only the x-axis value changing.  Points
      will be colorized based on their connection metadata. 
      Unflagged points are not connected to flagged points, even when
      not displayed.
   
   -  Supported for calibration tables *only* at present.  When enabled
      for a MeasurementSet, a warning will be issued and the plot
      will complete without connection.
   
   -  "none" (default), "line", or "step".
   
   -  *timeconnector*

      -  subparameter when xconnector is not "none".
      -  False (default).  When True, connect the points which change
         by time only, irrespective of the x-axis value.
   
   .. rubric:: Display: Title, Axis Labels
   
   -  *title*
   
      -  Set title text.
      -  “” (default) : yaxis vs. xaxis
      -  Will append data column to visibility axis if not *‘data’*.
      -  Will prepend “Average” to axis, if axis is averaged.
      -  Will append iteration axis and value to title, if *iteraxis*
         set.
   
   -  *titlefont*
   
      -  set the size of the title text.
      -  0 (default) : autosize the title according to the plot size,
         especially important when making a grid of plots.
   
   -  *xlabel, ylabel*
   
      -  set the xaxis or yaxis label.
      -  “” (default) : label string for the axis plotted, e.g. use
         the label “Amp” for the axis ‘amp’.
   
   -  *xaxisfont, yaxisfont*
   
      -  set the axis label font size.
      -  0 (default) : autosize depending on the plot size.
   
   .. rubric:: Display: Plot Gridlines, Legend, Header
   
   *showmajorgrid*
   
   -  parameter to enable major gridlines (at labeled tick marks) and
      subparameters.
   -  False (default): do not show major gridlines.
   -  True: show solid black gridlines of width 1 unless
      subparameters are set otherwise.
   -  Not to be confused with *gridrows* and *gridcols*, for making
      plots in a grid.
   
   -  *majorwidth*
   
      -  width of major gridlines, when major grid is enabled.
      -  0 (default) : automatically sets width to 1.
   
   -  *majorstyle*
   
      -  style of major gridlines, when major grid is enabled.
      -  *“solid”* (default) when *showmajorgrid=True*.
      -  Options: *“solid”, “dash”, “dot”, “none”*.
   
   -  *majorcolor*

      -  set color by RGB hex code or string color name, e.g.
         *‘blue’*, when major grid is enabled.
      -  *"B0B0B0"* (default): dark gray.
   
   *showminorgrid*

   -  parameter to enable minor gridlines (between labeled tick
      marks) and subparameters.
   -  False (default): do not show show minor gridlines.
   -  True: show solid light gray gridlines of width 1 unless
      subparameters are set otherwise.
   
   -  *minorwidth=1, minorstyle="" (“solid”), minorcolor="D0D0D0"* (light gray)

      -  Subparameter defaults are shown.  Options are the same as
         for major gridlines, when *showminorgrid=True*.
   
   *showlegend*

   -  Show legend; useful when setting two y-axes or overplotting two
      plots on one canvas, with different colors for each yaxis/plot.
   -  False (default) : do not show legend.
   -  Legend is shown at upper right unless subparameter
      *legendposition* is set.
   
   *legendposition*

   -  position of the legend, either inside the plot canvas (may
      cover part of the plot) or exterior to it.
   -  None (default) when *showlegend=False*; set to
      *‘upperRight’* when *showlegend=True*.
   -  Options: *“upperRight”, “upperLeft”, “lowerRight”,
      “lowerLeft”, “exteriorRight”, “exteriorLeft”, “exteriorTop”,
      “exteriorBottom”*
   
   *headeritems*

   -  Add plot header: comma-separated list of options in a string,
      e.g. headeritems=“filename, telescope”.
   -  “” (default) : Do not show plot header.
   -  Options: *“filename”, “projid”, “telescope”, “observer”,
      “obsdate”, “obstime”, “targname”, “targdir”, “ycolumn”.*
   -  Items are always loaded into cache along with plotted axes,
      even if not requested, so that all of the disk I/O of the
      dataset is done at once.
   -  Requested items will appear in the header even if no value is
      found for it in dataset.
   -  The page header is only applicable to MeasurementSets. A header
      will be added to CalTable plots but with no values for
      requested items.

   .. rubric:: Plot Export

   *plotfile*

   -  filename for plot export. Enables subparameters to be set.
   -  “” (default) : do not export the plot.
   -  If no path is included in the filename, the plot will be
      exported to the current directory.
   -  If the filename exists and *overwrite=False* (default), the
      plot and the export will fail with an error.
   -  If the filename has no extension and *expformat* is set, the
      given filename will be used and the extension will not be
      added.
   
   -  *expformat*
   
      -  export format type.
      -  “” (default) : use *plotfile* extension to determine type.
         If the *plotfile* has no extension, the export will fail.
      -  Options: *“jpg”, “png”, “pdf”, “ps”, “txt”*
      -  For *‘txt’* format, Locate information (x and y values plus
         metadata) for each point is exported to an ASCII text file.
         This can take some time and produce a large file when many
         points are plotted. Use averaging and selection to keep the
         file size manageable.
      -  If the *expformat* does not match the *plotfile* extension
         (e.g. plotfile=’test.pdf’, expformat=’jpg’), both will take
         effect; a jpg file will be created with the name “test.pdf”.
         Not recommended!
   
   -  *verbose*
   
      -  include metadata in text export
      -  True (default): When False, export only x and y values.
   
   -  *exprange*
   
      -  range of iteration plots to export, one plotfile per page.
         Multipage pdf exports are not supported. Ignored if iteraxis
         is not set.
      -  “” (default) : current page only.
      -  Options: *“current”, “all”*
   
   -  *highres*
   
      -  Export .jpg or .png plot in high resolution.
      -  False (default) : screen resolution export not implemented. 
         Plotms always exports a high resolution plot (high quality,
         no compression) for .png and .jpg formats.
   
   -  *dpi*
   
      -  set DPI (dots per inch) of exported plot.
      -  -1 (default) : use Qt default settings.
   
   -  *width, height*
   
      -  set size of exported plot, in pixels (does not affect GUI
         plot).
      -  -1 (default) : use default settings.
   
   -  *overwrite*
   
      -  overwrite existing *plotfile*.
      -  False (default) : do not overwrite existing *plotfile*.
      -  If False and *plotfile* exists, plotms will issue an error
         and fail to make the plot.
   

.. _Examples:

Examples
   NOTE: These examples are not comprehensive, as **plotms** has a
   substantial list of parameters and allowed values!  See the
   `documentation on using
   plotms <../../notebooks/data_examination.ipynb#Plot/Edit-using-plotms>`__
   under Data Examination and Editing for details of the task
   parameters and how they correspond to settings in the GUI.
   
   .. rubric:: Default Plots (unflagged data only)
   
   All that is really required is a dataset or cal table to plot. 
   The first example will plot Amp vs. Time, the default axes for a
   MeasurementSet.  The second plot will be Tsys vs. Channel, the
   default axes for the cal table type being plotted.  By default,
   *customflaggedsymbol=False* and no flagged data is plotted.  Since
   no averaging or selection is done, **plotms** will plot the entire
   dataset, which could take some time and substantial memory.
   
   ::
   
      plotms(vis='test.ms')
      plotms(vis='uid___A002_X99c183_X25b6.ms.tsys')
   
   .. rubric:: Change Default Axis and Datacolumn
   
   Here we change the default datacolumn and axes. In the first
   example, *yaxis='amp'* is implied since it is the default.
   
   ::
   
      plotms(vis='test.ms', ydatacolumn='corrected', xaxis='channel')
      plotms(vis='test.ms', xaxis='elevation', yaxis='azimuth')
   
   .. rubric:: Plot Flagged Data
   
   By setting *customflaggedsymbol=True*, **plotms** uses the default
   red circles for the flagged data. In the second example, a custom
   symbol is specified.
   
   ::
   
      plotms(vis='test.ms', customflaggedsymbol=True)
      plotms(vis='test.ms', customflaggedsymbol=True, flaggedsymbolshape='diamond', flaggedsymbolsize=5,
             flaggedsymbolcolor='00ff00', flaggedsymbolfill='mesh3')
   
   .. rubric:: Plot with Colorized Data
   
   Note that the colorization overrides the default or custom color
   for all data, unflagged or flagged.  In the following example, all
   data in the MS will be colorized according to its spectral window.
   
   ::
   
      plotms(vis='test.ms', customflaggedsymbol=True, coloraxis='spw')
   
   .. rubric:: Plot with Data Selection
   
   Note that all selections are strings, including numerical values. 
   Refer to the documentation on `Data
   Selection <../../notebooks/visibility_data_selection.ipynb>`__
   for an explanation of MeasurementSet selection.  In the second
   example, the *correlation* parameter is used for polarization
   selection on a calibration table, and the result is plotted with
   the default axes Gain Amplitude vs. Time for this cal table type.
   
   ::
   
      plotms(vis='test.ms', field='1', spw='0:3~10', antenna='1&2', scan='2~4', corr='XX,YY')
      plotms(vis='bpphase.gcal', correlation='R')
   
   .. rubric:: Plot with Iteration
   
   The first example plots one plot per page.  The second example
   demonstrates iteration plots on a 2x2 grid.  In the third example,
   all iteration plots are exported with the plotfile name appended
   with the iteration label and index, i.e. test_Scan2.jpg,
   test_Scan3_2.jpg, test_Scan4_3.jpg.
   
   ::
   
      plotms(vis='test.ms', xaxis='freq', iteraxis='baseline')
      plotms(vis='test.ms', xaxis='freq', iteraxis='baseline', gridrows=2, gridcols=2)
      plotms(vis='test.ms', scan='2~4', iteraxis='scan', plotfile='test.jpg', exprange='all')
   
   .. rubric:: Plot with Averaging
   
   In the first example, the *avgtime* value is in seconds.  In the
   second example, the channel numbers plotted on the x-axis
   (*'chan'*) will refer to the binned channels (0-based), not the
   averaged channel number for the bin.  Use the Locate feature to
   find the channel range for each bin.
   
   ::
   
      plotms(vis='test.ms', avgtime='1e8', avgscan=True)
      plotms(vis='test.ms', xaxis='chan', avgchannel='128')
   
   .. rubric:: Using On-the-Fly Calibration
   
   The calibration library to apply is contained in the file
   *calibration.txt*.  By default, this sets Calibration to "On" in
   the GUI and applies the cal library; you can select "OFF" but keep
   the callib setting.
   
   ::
   
      plotms(vis='ngc5921.ms', xaxis='frequency', yaxis='amp', ydatacolumn='corrected',
             field='N5921_2', antenna='*&*', callib='calibration.txt')
   
   .. rubric:: Overplot Two Datasets on One Plot
   
   This is **one example** with two **plotms** calls.  Be sure to
   increment *plotindex* and set *clearplots* to False on the second
   call.  Here the second plot is set to a different color.  A legend
   is included to indicate which points represent the Scan axis and
   which are Field points.
   
   ::
   
      plotms(vis='test1.ms', yaxis='scan', showlegend=True, legendposition='lowerRight')
      plotms(vis='test2.ms', yaxis='field', plotindex=1, clearplots=False, showlegend=True,
             legendposition='lowerRight', customsymbol=True, symbolcolor='00FF00')
   
   .. rubric:: Plot Two Datasets on One Page
   
   Here we use a grid with 2 rows, 1 column, and specify the plot for
   each row.  The first **plotms** call uses the defaults
   *rowindex=0, colindex=0, plotindex=0, clearplots=True*.  In the
   second call we must increment the *plotindex* and *rowindex* (so
   it does not overplot the first plot), and set *clearplots=False*
   so that it keeps the first plot.  We can also export this page
   with two plots.
   
   ::
   
      plotms(vis='test1.ms', yaxis='field', gridrows=2, gridcols=1)
      plotms(vis='test2.ms', yaxis='field', gridrows=2, gridcols=1, rowindex=1,
             plotindex=1, clearplots=False, plotfile='fields.jpg')
   
   .. rubric:: Saving your plot
   
   The export format can be indicated in the plotfile name or by
   using the *expformat* parameter.  Allowed extensions include jpg,
   png, pdf, ps, and txt.  Exporting the plot as text produces
   Locate-style output.
   
   Here the plot will be exported in PNG format, as indicated by the
   plotfile extension:
   
   ::
   
      plotms(vis='test.ms', plotfile='test.png')
   
   Example with *expformat* parameter.  Note that the plotfile name
   is used as given and no extension is added:
   
   ::
   
      plotms(vis='ngc5921.ms', plotfile='ngc5921', expformat='jpg')
   
   When scripting the **plotms** calls, one may want to produce
   plotfiles without a GUI:
   
   ::
   
      plotms(vis='test.ms', plotfile='test.jpg', showgui=False)
   
   With iteration, one may wish to export only the first plot
   (default) or all plots using the *exprange* parameter.  The
   iteration string will be appended to the filename before the
   extension.
   
   ::
   
      plotms(vis='ngc5921.ms', iteraxis='baseline', plotfile='ngc5921.jpg', exprange='all')
   

.. _Development:

Development
   Plotms is a GUI plotter based on Qt and Qwt for making X-Y plots
   of measurement sets and calibration tables.  It can be started as
   a task (**plotms**) or tool (**pm**) within CASA, or as a
   standalone app (**casaplotms**) from the shell prompt.  All
   available options should be accessible from both the task/tool
   arguments and GUI text boxes, check boxes, etc.
   
   .. rubric:: C++ layers
   
   The main C++ code body for plotms is in **code/plotms**.  This
   directory contains several subdirectories:
   
   -  **app** - standalone casaplotms executable, which launches the
      PlotMSApp controller.
   -  **PlotMS** - highest level code for the main controller, DBus
      interface, constants and enums.  Classes are also defined to
      save plotms parameters for averaging, calibration, export,
      flagging, iteration, plotting, selection, and transformations.
   -  **Client** - factory and classes for GUI and scripted clients
   -  **Threads** - includes BackgroundThreads and ThreadControllers
      for caching the data, drawing the plots, and exporting the plot
      files. Plotms uses threads for speed and as a means to return
      control to the user.  
   -  **Data** - classes to load the cache for measurement sets
      (using VIVB2) and calibration tables (using CTIter), as well as
      utility classes to estimate the required memory, average the
      data (soon to be moved to the VIVB2 layered architecture), and
      index the cached data for flagging and locating data.
   -  **Plots** - classes to organize one or more plots and pages, as
      well as the display parameters for plotting.
   -  **Gui, GuiTabs, Actions** - handles the GUI layout (tabs,
      buttons, etc.) and interactions with the user (signals and
      slots).
   
   The plotms GUI is built on base classes specifically for using Qt
   in CASA (**code/casaqt**) and for a generic plotter
   (**code/graphics/GenericPlotter**) in case a different package is
   chosen to be used instead of Qt.  **Gotcha:** some Qt
   functionality is unaccessible since the types are abstracted to
   the base classes in GenericPlotter.  For basic non-comprehensive
   UML diagrams, see
   `PlotmsDocs. <https://safe.nrao.edu/wiki/bin/view/Main/PlotMSDocs>`_
   
   .. rubric:: Python layer
   
   Within CASA, **plotms** is set up like other tasks.  Briefly, the
   parameters and allowed values are defined in
   **gcwrap/tasks/plotms.xml**, and the starting point to process the
   parameters and launch the casaplotms process (with or without the
   GUI) is **gcwrap/python/scripts/task_plotms.py. ** It is important
   to keep the GUI and the task arguments in sync, so that all
   functionality is available in either case.  Unfortunately, the
   result is a very long list of plotms parameters.
   
   The python code has a SWIG interface to the C++ **pm** tool
   methods defined in **gcwrap/tools/plotms/plotms_cmpt.cc**.  This
   component handles setting the arguments in the plotms code
   described above via DBus XML calls (see
   **code/plotms/PlotMS/PlotMSDBusApp.cc**), then starts the plotting
   with a call to update().
   
   Once update() is called, control returns to the casa session and
   the log contains the message "End Task: plotms".  However, the
   cache thread and then the draw thread continue to make the plot,
   so additional plotms output appears in the log even after the task
   supposedly ended.
   
   .. rubric:: Plotms tests
   
   Python regression tests for all of the plotms parameters and some
   bug fixes are in **gcwrap/python/scripts/tests/test_plotms.py**. 
   There are test classes within this suite for:  basic plots,
   averaging, axes options, calibration, calibration tables, display
   options, grid options, iteration, selection, transformations, and
   combinations of these ("multi").  The entire suite takes over 10
   minutes to run, so it is useful to run a single test or subset of
   tests (for example, "runUnitTest.py
   test_plotms['test_averaging']").
   
   Google tests, with suffix **\_GT**, have been added in
   **code/plotms/test/**.  These tests generally load the cache and
   check the values.  Some legacy C++ tests are also in this
   directory, with prefix **d**.  They can be compiled and run
   manually as "demo" tests and can be useful for creating the google
   tests.
   
   .. rubric:: Debugging
   
   Whether you run a plotms command in a casa session or run
   *casaplotms * from the command line, a casaplotms process is
   started and continues to run until you exit the casa session (for
   plotms) or the plotms GUI (for casaplotms).  This makes debugging
   with gdb/ddd very easy, as you can run plotms (with arguments
   which work or even no arguments, in order to start the process),
   attach the PID in the debugger, then set breakpoints and run
   plotms with the failing arguments.
   
   In the unlikely event of a segmentation fault producing a core
   file, use *gdb casaplotms core.XXXX* and look at the backtrace. 
   When debugging a tarball, the executable is (for example)
   *casa-prerelease-5.0.0-112.el6/lib/casa/bin/casaplotms,* not the
   path returned by 'which casaplotms', *bin/casaplotms,* which is a
   perl script.
   
   **Gotcha:** When new third-party libraries are used in a CASA
   release (e.g. devtoolset-4 in release 5.0), including the
   compiler, the system gdb may be incompatible with your build.  The
   result is a gdb seg fault when running gdb on a core file or
   setting a breakpoint in gdb with an attached casaplotms process. 
   In this case, use the gdb executable in the third-party libraries
   (e.g. devtoolset-4/root/usr/bin/gdb), which was compiled with the
   same compiler.
   
