plotms -- A plotter/interactive flagger for visibility data. -- visualization, information,editing, manipulation, utility task
=======================================

Description
---------------------------------------


        Task for plotting and interacting with visibility
        data.  Limited support for caltable plotting is also
        included as of CASA v4.1.

        A variety of axes choices (including data column) along 
        with MS selection and averaging options are provided for data 
        selection.  Flag extension parameters are also available for
        flagging operations in the plotter.
        
        All of the provided parameters can also be set using the GUI once
        the application has been launched.  Additional and more specific
        operations are available through the GUI and/or through the plotms
        tool (pm).

        Most basic functions (plotting, iteration, locate, flagging)
        will work for most CalTables. Parameterized CalTables
        (delays, antpos, gaincurve, opacity), will, at best, currently 
        just plot the simple parameters contained in the
        table, not the effective amplitudes or phases sampled at
        observing times, frequencies etc.  BPOLY and GSPLINE tables
        are not yet supported.   Features currently unsupported for
        CalTables include Averaging, Transformations (velocity 
        conversions, etc.), and some details of selection (channel and 
        polarization selection are not yet enabled) and axes choices 
        (geometry options are not yet enabled).  In the plotms gui,
        many options irrelevant for CalTables are not yet hidden when
        interacting with a CalTable, and such settings will be ignored
        (when benign) or cause an error message.
        



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
   * - yaxis
     - :code:`''`
     - 
   * - ydatacolumn
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


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

input MS (or CalTable) (blank for none)


gridrows
---------------------------------------

:code:`int(1)`

Number of subplot rows (default 1).


gridcols
---------------------------------------

:code:`int(1)`

Number of subplot columns (default 1).


rowindex
---------------------------------------

:code:`int(0)`

Row location of the plot (0-based, default 0)


colindex
---------------------------------------

:code:`int(0)`

Column location of the plot (0-based, default 0)


plotindex
---------------------------------------

:code:`int(0)`

Index to address a subplot (0-based, default 0)


xaxis
---------------------------------------

:code:`''`

plot x-axis (blank for default/current)


xdatacolumn
---------------------------------------

:code:`''`

data column to use for x-axis (blank for default/current)


yaxis
---------------------------------------

:code:`''`

plot y-axis (blank for default/current)


ydatacolumn
---------------------------------------

:code:`''`

data column to use for y-axis (blank for default/current)


yaxislocation
---------------------------------------

:code:`''`

whether to use a left or right y-axis for the data (blank for default)


selectdata
---------------------------------------

:code:`True`

data selection parameters


field
---------------------------------------

:code:`''`

field names or field index numbers (blank for all)


spw
---------------------------------------

:code:`''`

spectral windows:channels (blank for all)


timerange
---------------------------------------

:code:`''`

time range (blank for all)


uvrange
---------------------------------------

:code:`''`

uv range (blank for all)


antenna
---------------------------------------

:code:`''`

antenna/baselines (blank for all)


scan
---------------------------------------

:code:`''`

scan numbers (blank for all)


correlation
---------------------------------------

:code:`''`

correlations (blank for all)


array
---------------------------------------

:code:`''`

(sub)array numbers (blank for all)


observation
---------------------------------------

:code:`''`

observation ID(s) (blank for all)


intent
---------------------------------------

:code:`''`

observing intent (blank for all)


feed
---------------------------------------

:code:`''`

Select feed (blank for all)


msselect
---------------------------------------

:code:`''`

MS selection (blank for all)


averagedata
---------------------------------------

:code:`True`

data averaging parameters


avgchannel
---------------------------------------

:code:`''`

average over channel?  (blank = False, otherwise value in channels)


avgtime
---------------------------------------

:code:`''`

average over time? (blank = False, other value in seconds)


avgscan
---------------------------------------

:code:`False`

only valid if time averaging is turned on.  average over scans?


avgfield
---------------------------------------

:code:`False`

only valid if time averaging is turned on.  average over fields?


avgbaseline
---------------------------------------

:code:`False`

average over all baselines?  (mutually exclusive with avgantenna)


avgantenna
---------------------------------------

:code:`False`

average by per-antenna?  (mutually exclusive with avgbaseline)


avgspw
---------------------------------------

:code:`False`

average over all spectral windows?


scalar
---------------------------------------

:code:`False`

Do scalar averaging?


transform
---------------------------------------

:code:`True`

transform data in various ways?


freqframe
---------------------------------------

:code:`''`

the frame in which to render frequency and velocity axes 


restfreq
---------------------------------------

:code:`''`

Rest frequency to use for velocity conversions 


veldef
---------------------------------------

:code:`'RADIO'`

the definition in which to render velocity 


shift
---------------------------------------

:code:`numpy.array( [ float(0.0),float(0.0) ] )`

Adjust phases by this approximate phase center shift [dx,dy] (arcsec)


extendflag
---------------------------------------

:code:`False`

have flagging extend to other data points?


extcorr
---------------------------------------

:code:`False`

extend flags based on correlation? 


extchannel
---------------------------------------

:code:`False`

extend flags based on channel?


iteraxis
---------------------------------------

:code:`''`

the axis over which to iterate


xselfscale
---------------------------------------

:code:`False`

If true, iterated plots should share a common x-axis label per column.


yselfscale
---------------------------------------

:code:`False`

If true, iterated plots should share a common y-axis label per row.


xsharedaxis
---------------------------------------

:code:`False`

Plots should share a common x-axis. Must also set xselfscale=True.


ysharedaxis
---------------------------------------

:code:`False`

Plots should share a common y-axis. Must also set yselfscale=True.


customsymbol
---------------------------------------

:code:`[ ]`

set a custom symbol(s) for unflagged points


symbolshape
---------------------------------------

:code:`'autoscaling'`

shape of plotted unflagged symbols


symbolsize
---------------------------------------

:code:`int(2)`

size of plotted unflagged symbols


symbolcolor
---------------------------------------

:code:`'0000ff'`

color of plotted unflagged symbols


symbolfill
---------------------------------------

:code:`'fill'`

fill type of plotted unflagged symbols


symboloutline
---------------------------------------

:code:`False`

selects outlining plotted unflagged points


coloraxis
---------------------------------------

:code:`''`

selects which data to use for colorizing


customflaggedsymbol
---------------------------------------

:code:`False`

set a custom plot symbol for flagged points


flaggedsymbolshape
---------------------------------------

:code:`'circle'`

shape of plotted flagged symbols


flaggedsymbolsize
---------------------------------------

:code:`int(2)`

size of plotted flagged symbols


flaggedsymbolcolor
---------------------------------------

:code:`'ff0000'`

color of plotted flagged symbols


flaggedsymbolfill
---------------------------------------

:code:`'fill'`

fill type of plotted flagged symbols


flaggedsymboloutline
---------------------------------------

:code:`False`

selects outlining plotted flagged points


plotrange
---------------------------------------

:code:`numpy.array( [  ] )`

plot axes ranges: [xmin,xmax,ymin,ymax]


title
---------------------------------------

:code:`''`

Title written along top of plot


titlefont
---------------------------------------

:code:`int(0)`

Font for plot title


xlabel
---------------------------------------

:code:`''`

Text for horizontal axis. Blank for default.


xaxisfont
---------------------------------------

:code:`int(0)`

Font for plot x-axis


ylabel
---------------------------------------

:code:`''`

Text for vertical axis. Blank for default.


yaxisfont
---------------------------------------

:code:`int(0)`

Font for plot y-axis.


showmajorgrid
---------------------------------------

:code:`False`

Show major grid lines (horiz and vert.)


majorwidth
---------------------------------------

:code:`int(1)`

Line width in pixels of major grid lines


majorstyle
---------------------------------------

:code:`''`

Major grid line style: solid dash dot none


majorcolor
---------------------------------------

:code:`'B0B0B0'`

Color as name or hex code of major grid lines


showminorgrid
---------------------------------------

:code:`False`

Show minor grid lines (horiz and vert.)


minorwidth
---------------------------------------

:code:`int(1)`

Line width in pixels of minor grid lines


minorstyle
---------------------------------------

:code:`''`

Minor grid line style: solid dash dot none


minorcolor
---------------------------------------

:code:`'D0D0D0'`

Color as name or hex code of minor grid lines


showlegend
---------------------------------------

:code:`False`

Show a legend on the plot.


legendposition
---------------------------------------

:code:`''`

Legend position.


plotfile
---------------------------------------

:code:`''`

Name of plot file to save automatically.


expformat
---------------------------------------

:code:`''`

Export format type (jpg, png, ps, pdf, txt), if not provided, plotfile extension will be used.


exprange
---------------------------------------

:code:`''`

Export all iteration plots or only the current one.


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

Width of exported plot


height
---------------------------------------

:code:`int(-1)`

Height of exported plot


overwrite
---------------------------------------

:code:`False`

Overwrite plot file if it already exists?


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




