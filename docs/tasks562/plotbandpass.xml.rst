plotbandpass -- Makes detailed plots of Tsys and bandpass solutions. -- visualization, calibration task
=======================================

Description
---------------------------------------
Developed at the NAASC, this is a generic task to display CASA 
  Tsys and bandpass solution tables with options to overlay them in various
  combinations, and/or with an atmospheric transmission or sky temperature
  model.  It works with both the 'new' (casa 3.4) and 'old' calibration
  table formats, and allows for mixed mode spws (e.g. TDM and FDM for ALMA).
  It uses the new msmd tool to access the information about an ms.  This
  task is still being developed as new ALMA observing modes are commissioned.
  So if you encounter problems, please report them.
  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - caltable
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - yaxis
     - :code:`'amp'`
     - 
   * - xaxis
     - :code:`'chan'`
     - 
   * - figfile
     - :code:`''`
     - 
   * - plotrange
     - :code:`numpy.array( [  ] )`
     - 
   * - caltable2
     - :code:`''`
     - 
   * - overlay
     - :code:`''`
     - 
   * - showflagged
     - :code:`False`
     - 
   * - timeranges
     - :code:`''`
     - 
   * - buildpdf
     - :code:`False`
     - 
   * - caltable3
     - :code:`''`
     - 
   * - markersize
     - :code:`int(3)`
     - 
   * - density
     - :code:`int(108)`
     - 
   * - interactive
     - :code:`True`
     - 
   * - showpoints
     - :code:`'auto'`
     - 
   * - showlines
     - :code:`'auto'`
     - 
   * - subplot
     - :code:`'22'`
     - 
   * - zoom
     - :code:`''`
     - 
   * - poln
     - :code:`''`
     - 
   * - showatm
     - :code:`False`
     - 
   * - pwv
     - :code:`'auto'`
     - 
   * - gs
     - :code:`'gs'`
     - 
   * - convert
     - :code:`'convert'`
     - 
   * - chanrange
     - :code:`''`
     - 
   * - solutionTimeThresholdSeconds
     - :code:`float(30.0)`
     - 
   * - debug
     - :code:`False`
     - 
   * - phase
     - :code:`''`
     - 
   * - vis
     - :code:`''`
     - 
   * - showtsky
     - :code:`False`
     - 
   * - showfdm
     - :code:`False`
     - 
   * - showatmfield
     - :code:`''`
     - 
   * - lo1
     - :code:`''`
     - 
   * - showimage
     - :code:`False`
     - 
   * - showatmpoints
     - :code:`False`
     - 
   * - parentms
     - :code:`''`
     - 
   * - pdftk
     - :code:`'pdftk'`
     - 
   * - channeldiff
     - :code:`False`
     - 
   * - edge
     - :code:`int(8)`
     - 
   * - resample
     - :code:`int(1)`
     - 
   * - platformingThreshold
     - :code:`float(10.0)`
     - 
   * - platformingSigma
     - :code:`float(10.0)`
     - 
   * - basebands
     - :code:`''`
     - 
   * - showBasebandNumber
     - :code:`False`
     - 
   * - scans
     - :code:`''`
     - 
   * - figfileSequential
     - :code:`False`
     - 
   * - chanrangeSetXrange
     - :code:`False`
     - 


Parameter Explanations
=======================================



caltable
---------------------------------------

:code:`''`

Input table name, either a bandpass solution or a Tsys solution


antenna
---------------------------------------

:code:`''`

A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.


field
---------------------------------------

:code:`''`

A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.


spw
---------------------------------------

:code:`''`

A comma-delimited string list of spws for which to display solutions.  Default = all spws.


yaxis
---------------------------------------

:code:`'amp'`

The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).


xaxis
---------------------------------------

:code:`'chan'`

The quantity to plot on the x-axis ("chan" or "freq").


figfile
---------------------------------------

:code:`''`

The name of the plot file to produce.


plotrange
---------------------------------------

:code:`numpy.array( [  ] )`

The axes limits to use [x0,x1,y0,y1].


caltable2
---------------------------------------

:code:`''`

A second cal table, of type BPOLY or B, to overlay on a B table


overlay
---------------------------------------

:code:`''`

Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)


showflagged
---------------------------------------

:code:`False`

Show the values of the solution, even if flagged


timeranges
---------------------------------------

:code:`''`

Show only these timeranges, the first timerange being 0


buildpdf
---------------------------------------

:code:`False`

If True, assemble all the pngs into a pdf


caltable3
---------------------------------------

:code:`''`

A third cal table, of type BPOLY, to overlay on the first two tables


markersize
---------------------------------------

:code:`int(3)`

Size of points


density
---------------------------------------

:code:`int(108)`

dpi to use in creating PNGs and PDFs (default=108)


interactive
---------------------------------------

:code:`True`

if False, then run to completion automatically without pause


showpoints
---------------------------------------

:code:`'auto'`

Draw points for the data (default=F for amp, T for phase)


showlines
---------------------------------------

:code:`'auto'`

Draw lines connecting the data (default=T for amp, F for phase)


subplot
---------------------------------------

:code:`'22'`

11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored


zoom
---------------------------------------

:code:`''`

"intersect" will zoom to overlap region of caltable with caltable2


poln
---------------------------------------

:code:`''`

Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"


showatm
---------------------------------------

:code:`False`

Compute and overlay the atmospheric transmission curve


pwv
---------------------------------------

:code:`'auto'`

Define the pwv to use for the showatm option: "auto" or value in mm


gs
---------------------------------------

:code:`'gs'`

For buildpdf=T, full path for ghostscript command (in case it is not found)


convert
---------------------------------------

:code:`'convert'`

For buildpdf=T, full path for the ImageMagick convert command (in case it is not found)


chanrange
---------------------------------------

:code:`''`

Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"


solutionTimeThresholdSeconds
---------------------------------------

:code:`float(30.0)`

Consider 2 solutions simultaneous if within this interval in seconds


debug
---------------------------------------

:code:`False`

Print verbose messages for debugging purposes


phase
---------------------------------------

:code:`''`

The y-axis limits to use for phase plots when yaxis="both"


vis
---------------------------------------

:code:`''`

name of the ms for this table, in case it does not match the string in the caltable


showtsky
---------------------------------------

:code:`False`

Compute and overlay the sky temperature curve instead of transmission


showfdm
---------------------------------------

:code:`False`

when showing TDM spws, draw the locations of the corresponding FDM spws


showatmfield
---------------------------------------

:code:`''`

for overlay="time", use first observation of this fieldID or name


lo1
---------------------------------------

:code:`''`

specify the LO1 setting (in GHz) for the observation ('' = automatic)


showimage
---------------------------------------

:code:`False`

also show the atmospheric curve for the image sideband (in black)


showatmpoints
---------------------------------------

:code:`False`

Draw atmospheric curve with points instead of a line


parentms
---------------------------------------

:code:`''`

if showimage=T, name of the parent ms (only needed if the ms has been previously split)


pdftk
---------------------------------------

:code:`'pdftk'`

For buildpdf=T, full path for pdftk command (in case it is not found)


channeldiff
---------------------------------------

:code:`False`

Set to a value > 0 (sigma) to plot derivatives of the solutions


edge
---------------------------------------

:code:`int(8)`

The number of edge channels to ignore in finding outliers (for channeldiff>0)


resample
---------------------------------------

:code:`int(1)`

The channel expansion factor to use when computing MAD of derivative (for channeldiff>0)


platformingThreshold
---------------------------------------

:code:`float(10.0)`

if platformingSigma=0, then declare platforming if the amplitude derivative exceeds this percentage of the median


platformingSigma
---------------------------------------

:code:`float(10.0)`

declare platforming if the amplitude derivative exceeds this many times the MAD


basebands
---------------------------------------

:code:`''`

A baseband number or list of baseband numbers for which to display solutions.  Default = all.


showBasebandNumber
---------------------------------------

:code:`False`

Put the baseband converter number (BBC_NO) in the title of each plot


scans
---------------------------------------

:code:`''`

A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".


figfileSequential
---------------------------------------

:code:`False`

naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.


chanrangeSetXrange
---------------------------------------

:code:`False`

If True, then chanrange also sets the xrange to display




