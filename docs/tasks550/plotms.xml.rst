plotms -- A plotter/interactive flagger for visibility data. -- visualization, information,editing, manipulation, utility task
=======================================

Description
---------------------------------------


		Task for plotting and interacting with visibility data and
		calibration tables.

		Plotms provides a variety of axis choices (including data column)
		along with selection, averaging, and transformation options for
		MeasurementSets.  Flag extension parameters are also available for
		interactive flagging operations in the plotter.
        
		All of the provided parameters can also be set using the GUI once
		the application has been launched or through the plotms tool (pm).

		Most of the basic plotms functions will work for calibration tables.
		The correlation selection string may be used to select polarization
		in a cal table, including ratio plots ("/").  The antenna selection
		string is used to select antenna1 only, rather than baselines as in
		an MS. When plotting parameterized CalTables, such as delays, antpos,
		gaincurve, or opacity, plotms will currently just plot the simple
		parameters contained in the table, not the effective amplitudes or
		phases sampled at observing times, frequencies etc.  BPOLY and
		GSPLINE tables are supported but interactive flagging is not allowed.
		Features currently unsupported for CalTables include averaging,
		transformations (velocity conversions, etc.), and some axis and
		selection options which do not exist in these tables. In the plotms
		GUI, many options irrelevant for CalTables are not hidden when
		interacting with a CalTable, and such settings will be ignored (when
		benign) or cause an error message.
        



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
   * - gridrows
     - :code:`int(1)`
     - 
   * - gridcols
     - :code:`int(1)`
     - 
   * - rowindex
     - :code:`int(0)`
     - 
   * - colindex
     - :code:`int(0)`
     - 
   * - plotindex
     - :code:`int(0)`
     - 
   * - xaxis
     - :code:`''`
     - 
   * - xdatacolumn
     - :code:`''`
     - 
   * - xframe
     - :code:`''`
     - 
   * - xinterp
     - :code:`''`
     - 
   * - yaxis
     - :code:`''`
     - 
   * - ydatacolumn
     - :code:`''`
     - 
   * - yframe
     - :code:`''`
     - 
   * - yinterp
     - :code:`''`
     - 
   * - yaxislocation
     - :code:`''`
     - 
   * - selectdata
     - :code:`True`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - intent
     - :code:`''`
     - 
   * - feed
     - :code:`''`
     - 
   * - msselect
     - :code:`''`
     - 
   * - averagedata
     - :code:`True`
     - 
   * - avgchannel
     - :code:`''`
     - 
   * - avgtime
     - :code:`''`
     - 
   * - avgscan
     - :code:`False`
     - 
   * - avgfield
     - :code:`False`
     - 
   * - avgbaseline
     - :code:`False`
     - 
   * - avgantenna
     - :code:`False`
     - 
   * - avgspw
     - :code:`False`
     - 
   * - scalar
     - :code:`False`
     - 
   * - transform
     - :code:`True`
     - 
   * - freqframe
     - :code:`''`
     - 
   * - restfreq
     - :code:`''`
     - 
   * - veldef
     - :code:`'RADIO'`
     - 
   * - shift
     - :code:`numpy.array( [ float(0.0),float(0.0) ] )`
     - 
   * - extendflag
     - :code:`False`
     - 
   * - extcorr
     - :code:`False`
     - 
   * - extchannel
     - :code:`False`
     - 
   * - iteraxis
     - :code:`''`
     - 
   * - xselfscale
     - :code:`False`
     - 
   * - yselfscale
     - :code:`False`
     - 
   * - xsharedaxis
     - :code:`False`
     - 
   * - ysharedaxis
     - :code:`False`
     - 
   * - customsymbol
     - :code:`[ ]`
     - 
   * - symbolshape
     - :code:`'autoscaling'`
     - 
   * - symbolsize
     - :code:`int(2)`
     - 
   * - symbolcolor
     - :code:`'0000ff'`
     - 
   * - symbolfill
     - :code:`'fill'`
     - 
   * - symboloutline
     - :code:`False`
     - 
   * - coloraxis
     - :code:`''`
     - 
   * - customflaggedsymbol
     - :code:`False`
     - 
   * - flaggedsymbolshape
     - :code:`'circle'`
     - 
   * - flaggedsymbolsize
     - :code:`int(2)`
     - 
   * - flaggedsymbolcolor
     - :code:`'ff0000'`
     - 
   * - flaggedsymbolfill
     - :code:`'fill'`
     - 
   * - flaggedsymboloutline
     - :code:`False`
     - 
   * - xconnector
     - :code:`''`
     - 
   * - timeconnector
     - :code:`False`
     - 
   * - plotrange
     - :code:`numpy.array( [  ] )`
     - 
   * - title
     - :code:`''`
     - 
   * - titlefont
     - :code:`int(0)`
     - 
   * - xlabel
     - :code:`''`
     - 
   * - xaxisfont
     - :code:`int(0)`
     - 
   * - ylabel
     - :code:`''`
     - 
   * - yaxisfont
     - :code:`int(0)`
     - 
   * - showmajorgrid
     - :code:`False`
     - 
   * - majorwidth
     - :code:`int(1)`
     - 
   * - majorstyle
     - :code:`''`
     - 
   * - majorcolor
     - :code:`'B0B0B0'`
     - 
   * - showminorgrid
     - :code:`False`
     - 
   * - minorwidth
     - :code:`int(1)`
     - 
   * - minorstyle
     - :code:`''`
     - 
   * - minorcolor
     - :code:`'D0D0D0'`
     - 
   * - showlegend
     - :code:`False`
     - 
   * - legendposition
     - :code:`''`
     - 
   * - plotfile
     - :code:`''`
     - 
   * - expformat
     - :code:`''`
     - 
   * - verbose
     - :code:`True`
     - 
   * - exprange
     - :code:`''`
     - 
   * - highres
     - :code:`False`
     - 
   * - dpi
     - :code:`int(-1)`
     - 
   * - width
     - :code:`int(-1)`
     - 
   * - height
     - :code:`int(-1)`
     - 
   * - overwrite
     - :code:`False`
     - 
   * - showgui
     - :code:`True`
     - 
   * - clearplots
     - :code:`True`
     - 
   * - callib
     - :code:`numpy.array( [  ] )`
     - 
   * - headeritems
     - :code:`''`
     - 
   * - showatm
     - :code:`False`
     - 
   * - showtsky
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Input MS or CalTable (blank for none)


gridrows
---------------------------------------

:code:`int(1)`

Number of subplot rows


gridcols
---------------------------------------

:code:`int(1)`

Number of subplot columns


rowindex
---------------------------------------

:code:`int(0)`

Row location of the plot (0-based)


colindex
---------------------------------------

:code:`int(0)`

Column location of the plot (0-based)


plotindex
---------------------------------------

:code:`int(0)`

Index to address a subplot (0-based)


xaxis
---------------------------------------

:code:`''`

Plot x-axis (blank for default/current)


xdatacolumn
---------------------------------------

:code:`''`

Data column to use for x-axis (blank for default/current).  Note that unspecified residuals are complex (vector) differences or ratios.


xframe
---------------------------------------

:code:`''`

Coordinate frame to use for x-axis


xinterp
---------------------------------------

:code:`''`

Interpolation method for x-axis


yaxis
---------------------------------------

:code:`''`

Plot y-axis (blank for default/current)


ydatacolumn
---------------------------------------

:code:`''`

Data column to use for y-axis (blank for default/current). Note that unspecified residuals are complex (vector) differences or ratios.


yframe
---------------------------------------

:code:`''`

Coordinate frame to use for y-axis


yinterp
---------------------------------------

:code:`''`

Interpolation method for y-axis


yaxislocation
---------------------------------------

:code:`''`

Location of the y-axis (blank for default: left)


selectdata
---------------------------------------

:code:`True`

Enable data selection parameters


field
---------------------------------------

:code:`''`

Field names or ids (blank for all)


spw
---------------------------------------

:code:`''`

Spectral windows:channels (blank for all)


timerange
---------------------------------------

:code:`''`

Time range (blank for all)


uvrange
---------------------------------------

:code:`''`

UV range (blank for all)


antenna
---------------------------------------

:code:`''`

Baseline/antenna names or ids (blank for all)


scan
---------------------------------------

:code:`''`

Scan numbers (blank for all)


correlation
---------------------------------------

:code:`''`

Correlations/polarizations (blank for all)


array
---------------------------------------

:code:`''`

(Sub)array numbers (blank for all)


observation
---------------------------------------

:code:`''`

Observation IDs (blank for all)


intent
---------------------------------------

:code:`''`

Observing intent (blank for all)


feed
---------------------------------------

:code:`''`

Feed numbers (blank for all)


msselect
---------------------------------------

:code:`''`

MSSelection TaQL string (blank for none)


averagedata
---------------------------------------

:code:`True`

Enable data averaging parameters


avgchannel
---------------------------------------

:code:`''`

Average over channel (blank = False, otherwise value in channels)


avgtime
---------------------------------------

:code:`''`

Average over time (blank = False, otherwise value in seconds)


avgscan
---------------------------------------

:code:`False`

Average over scans. Only valid with time averaging


avgfield
---------------------------------------

:code:`False`

Average over fields. Only valid with time averaging


avgbaseline
---------------------------------------

:code:`False`

Average over all baselines (mutually exclusive with avgantenna)


avgantenna
---------------------------------------

:code:`False`

Average per antenna (mutually exclusive with avgbaseline)


avgspw
---------------------------------------

:code:`False`

Average over all spectral windows


scalar
---------------------------------------

:code:`False`

Scalar averaging (False=vector averaging)


transform
---------------------------------------

:code:`True`

Enable data transformations


freqframe
---------------------------------------

:code:`''`

The frame in which to render frequency and velocity axes


restfreq
---------------------------------------

:code:`''`

Rest frequency to use for velocity conversions 


veldef
---------------------------------------

:code:`'RADIO'`

The definition in which to render velocity 


shift
---------------------------------------

:code:`numpy.array( [ float(0.0),float(0.0) ] )`

Adjust phases by this approximate phase center shift [dx,dy] (arcsec)


extendflag
---------------------------------------

:code:`False`

Extend flagging to other data points not plotted


extcorr
---------------------------------------

:code:`False`

Extend flags based on correlation 


extchannel
---------------------------------------

:code:`False`

Extend flags based on channel


iteraxis
---------------------------------------

:code:`''`

The axis over which to iterate


xselfscale
---------------------------------------

:code:`False`

When True, iterated plots have a common x-axis range (scale).


yselfscale
---------------------------------------

:code:`False`

When True, iterated plots have a common y-axis range (scale).


xsharedaxis
---------------------------------------

:code:`False`

Iterated plots on a grid share a common external x-axis per column. Must also set xselfscale=True and gridrows>1.


ysharedaxis
---------------------------------------

:code:`False`

Iterated plots on a grid share a common external y-axis per row. Must also set yselfscale=True and gridcols>1.


customsymbol
---------------------------------------

:code:`[ ]`

Enable custom symbol(s) for unflagged points


symbolshape
---------------------------------------

:code:`'autoscaling'`

Shape of plotted unflagged symbols


symbolsize
---------------------------------------

:code:`int(2)`

Size of plotted unflagged symbols


symbolcolor
---------------------------------------

:code:`'0000ff'`

Color (name or hex code) of plotted unflagged symbols


symbolfill
---------------------------------------

:code:`'fill'`

Fill type of plotted unflagged symbols


symboloutline
---------------------------------------

:code:`False`

Outline plotted unflagged symbols


coloraxis
---------------------------------------

:code:`''`

Selects data axis for colorizing


customflaggedsymbol
---------------------------------------

:code:`False`

Enable custom symbol(s) for flagged points


flaggedsymbolshape
---------------------------------------

:code:`'circle'`

Shape of plotted flagged symbols


flaggedsymbolsize
---------------------------------------

:code:`int(2)`

Size of plotted flagged symbols


flaggedsymbolcolor
---------------------------------------

:code:`'ff0000'`

Color (name or hex code) of plotted flagged symbols


flaggedsymbolfill
---------------------------------------

:code:`'fill'`

Fill type of plotted flagged symbols


flaggedsymboloutline
---------------------------------------

:code:`False`

Outline plotted flagged symbols


xconnector
---------------------------------------

:code:`''`

Set connector for data points (blank="none"; "line","step")


timeconnector
---------------------------------------

:code:`False`

Connect points by time rather than x-axis


plotrange
---------------------------------------

:code:`numpy.array( [  ] )`

Plot axes ranges: [xmin,xmax,ymin,ymax]


title
---------------------------------------

:code:`''`

Title at top of plot


titlefont
---------------------------------------

:code:`int(0)`

Font size for plot title


xlabel
---------------------------------------

:code:`''`

Text for horizontal x-axis. Blank for default.


xaxisfont
---------------------------------------

:code:`int(0)`

Font size for x-axis label


ylabel
---------------------------------------

:code:`''`

Text for vertical y-axis. Blank for default.


yaxisfont
---------------------------------------

:code:`int(0)`

Font size for y-axis label


showmajorgrid
---------------------------------------

:code:`False`

Show major grid lines


majorwidth
---------------------------------------

:code:`int(1)`

Line width in pixels of major grid lines


majorstyle
---------------------------------------

:code:`''`

Major grid line style


majorcolor
---------------------------------------

:code:`'B0B0B0'`

Color (name or hex code) of major grid lines


showminorgrid
---------------------------------------

:code:`False`

Show minor grid lines


minorwidth
---------------------------------------

:code:`int(1)`

Line width in pixels of minor grid lines


minorstyle
---------------------------------------

:code:`''`

Minor grid line style


minorcolor
---------------------------------------

:code:`'D0D0D0'`

Color (name or hex code) of minor grid lines


showlegend
---------------------------------------

:code:`False`

Show a legend on the plot.


legendposition
---------------------------------------

:code:`''`

Legend position, default upperRight.


plotfile
---------------------------------------

:code:`''`

Name of plot file to save automatically


expformat
---------------------------------------

:code:`''`

Export format type. If not provided, plotfile extension will be used to determine type.


verbose
---------------------------------------

:code:`True`

Include metadata in text export


exprange
---------------------------------------

:code:`''`

Range of iteration plots to export, one plotfile per page.  Multipage pdf exports are not supported.


highres
---------------------------------------

:code:`False`

Use high resolution


dpi
---------------------------------------

:code:`int(-1)`

DPI of exported plot


width
---------------------------------------

:code:`int(-1)`

Width in pixels of exported plot


height
---------------------------------------

:code:`int(-1)`

Height in pixels of exported plot


overwrite
---------------------------------------

:code:`False`

Overwrite plot file if it already exists


showgui
---------------------------------------

:code:`True`

Show GUI


clearplots
---------------------------------------

:code:`True`

Remove any existing plots so new ones can replace them.


callib
---------------------------------------

:code:`numpy.array( [  ] )`

Calibration library string or filename for on-the-fly calibration.


headeritems
---------------------------------------

:code:`''`

Comma-separated list of pre-defined page header items.


showatm
---------------------------------------

:code:`False`

Compute and overlay the atmospheric transmission curve


showtsky
---------------------------------------

:code:`False`

Compute and overlay the sky temperature curve




