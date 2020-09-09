#
# stub function definition file for docstring parsing
#

def plotbandpass(caltable, antenna='', field='', spw='', yaxis='amp', xaxis='chan', figfile='', plotrange=[0,0,0,0], caltable2='', overlay='', showflagged=False, timeranges='', buildpdf=False, caltable3='', markersize=3, density=108, interactive=True, showpoints='auto', showlines='auto', subplot='22', zoom='', poln='['']', showatm=False, pwv='auto', gs='gs', convert='convert', chanrange='', solutionTimeThresholdSeconds=30.0, debug=False, phase='['']', vis='', showtsky=False, showfdm=False, showatmfield='', lo1='', showimage=False, showatmpoints=False, parentms='', pdftk='pdftk', channeldiff=False, edge=8, resample=1, platformingThreshold=10.0, platformingSigma=10.0, basebands='', showBasebandNumber=False, scans='', figfileSequential=False, chanrangeSetXrange=False):
    r"""
Makes detailed plots of Tsys and bandpass solutions.

Parameters
   - caltable_ (string) - Input table name, either a bandpass solution or a Tsys solution
   - antenna_ ({string, int, stringArray, intArray}='') - A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.
   - field_ ({string, int, stringArray, intArray}='') - A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.
   - spw_ ({string, int, stringArray, intArray}='') - A comma-delimited string list of spws for which to display solutions.  Default = all spws.
   - yaxis_ (string='amp') - The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).

      .. raw:: html

         <details><summary><i> yaxis = both </i></summary>

      - phase_ ({intArray, string}='['']') - The y-axis limits to use for phase plots when yaxis="both"

      .. raw:: html

         </details>
   - xaxis_ (string='chan') - The quantity to plot on the x-axis ("chan" or "freq").

      .. raw:: html

         <details><summary><i> xaxis = freq </i></summary>

      - chanrange_ ({string, intArray}='') - Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"
      - showfdm_ (bool=False) - when showing TDM spws, draw the locations of the corresponding FDM spws
      - chanrangeSetXrange_ (bool=False) - If True, then chanrange also sets the xrange to display

      .. raw:: html

         </details>
   - figfile_ (string='') - The name of the plot file to produce.

      .. raw:: html

         <details><summary><i> figfile != '' </i></summary>

      - density_ (int=108) - dpi to use in creating PNGs and PDFs (default=108)
      - buildpdf_ (bool=False) - If True, assemble all the pngs into a pdf
      - convert_ (string='convert') - For buildpdf=T, full path for the ImageMagick convert command (in case it is not found)
      - gs_ (string='gs') - For buildpdf=T, full path for ghostscript command (in case it is not found)
      - pdftk_ (string='pdftk') - For buildpdf=T, full path for pdftk command (in case it is not found)

      .. raw:: html

         </details>
   - plotrange_ (doubleArray=[0,0,0,0]) - The axes limits to use [x0,x1,y0,y1].
   - caltable2_ (string='') - A second cal table, of type BPOLY or B, to overlay on a B table

      .. raw:: html

         <details><summary><i> caltable2 != '' </i></summary>

      - zoom_ (string='') - "intersect" will zoom to overlap region of caltable with caltable2
      - caltable3_ (string='') - A third cal table, of type BPOLY, to overlay on the first two tables

      .. raw:: html

         </details>
   - overlay_ (string='') - Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)

      .. raw:: html

         <details><summary><i> overlay = time </i></summary>

      - showatmfield_ ({int, string}='') - for overlay="time", use first observation of this fieldID or name

      .. raw:: html

         </details>
   - showflagged_ (bool=False) - Show the values of the solution, even if flagged
   - timeranges_ (string='') - Show only these timeranges, the first timerange being 0
   - markersize_ (int=3) - Size of points
   - interactive_ (bool=True) - if False, then run to completion automatically without pause
   - showpoints_ ({string, bool}='auto') - Draw points for the data (default=F for amp, T for phase)
   - showlines_ ({string, bool}='auto') - Draw lines connecting the data (default=T for amp, F for phase)
   - subplot_ ({string, int}='22') - 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored
   - poln_ ({stringArray, string}='['']') - Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"
   - showatm_ (bool=False) - Compute and overlay the atmospheric transmission curve

      .. raw:: html

         <details><summary><i> showatm != False </i></summary>

      - pwv_ ({double, string}='auto') - Define the pwv to use for the showatm option: "auto" or value in mm
      - showimage_ (bool=False) - also show the atmospheric curve for the image sideband (in black)
      - parentms_ (string='') - if showimage=T, name of the parent ms (only needed if the ms has been previously split)
      - lo1_ ({string, double}='') - specify the LO1 setting (in GHz) for the observation ('' = automatic)
      - showatmpoints_ (bool=False) - Draw atmospheric curve with points instead of a line

      .. raw:: html

         </details>
   - solutionTimeThresholdSeconds_ (double=30.0) - Consider 2 solutions simultaneous if within this interval in seconds
   - debug_ (bool=False) - Print verbose messages for debugging purposes
   - vis_ (string='') - name of the ms for this table, in case it does not match the string in the caltable
   - showtsky_ (bool=False) - Compute and overlay the sky temperature curve instead of transmission

      .. raw:: html

         <details><summary><i> showtsky != False </i></summary>

      - pwv_ ({double, string}='auto') - Define the pwv to use for the showatm option: "auto" or value in mm
      - showimage_ (bool=False) - also show the atmospheric curve for the image sideband (in black)
      - parentms_ (string='') - if showimage=T, name of the parent ms (only needed if the ms has been previously split)
      - lo1_ ({string, double}='') - specify the LO1 setting (in GHz) for the observation ('' = automatic)
      - showatmpoints_ (bool=False) - Draw atmospheric curve with points instead of a line

      .. raw:: html

         </details>
   - channeldiff_ ({bool, double}=False) - Set to a value > 0 (sigma) to plot derivatives of the solutions

      .. raw:: html

         <details><summary><i> channeldiff != False </i></summary>

      - edge_ (int=8) - The number of edge channels to ignore in finding outliers (for channeldiff>0)
      - resample_ (int=1) - The channel expansion factor to use when computing MAD of derivative (for channeldiff>0)
      - platformingSigma_ (double=10.0) - declare platforming if the amplitude derivative exceeds this many times the MAD
      - platformingThreshold_ (double=10.0) - if platformingSigma=0, then declare platforming if the amplitude derivative exceeds this percentage of the median

      .. raw:: html

         </details>
   - basebands_ ({int, string, intArray}='') - A baseband number or list of baseband numbers for which to display solutions.  Default = all.
   - showBasebandNumber_ (bool=False) - Put the baseband converter number (BBC_NO) in the title of each plot
   - scans_ ({int, string, intArray}='') - A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".
   - figfileSequential_ (bool=False) - naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.


Description
   .. rubric:: Summary
      

   Plots the bandpass and system temperature (T sys) solutions.

   This generic task was developed at the North American ALMA Science
   Center (NAASC). It displays T sys and bandpass solution tables
   with options to overlay them in variouscombinations, and/or with
   an atmospheric transmission or sky temperaturemodel. It allows
   for mixed-mode spws (e.g., TDM and FDM for ALMA) and uses the msmd
   tool to access the information about an MS.

   Note thatthe ability to compute and overlay an atmospheric
   transmission curve or a sky temperature curve is now also
   available in **plotms**.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *antenna*
      

   Must be either an ID (int or string or list), or a single antenna
   name or list.

   .. rubric:: *basebands*
      

   Show only spws from the specified baseband or list of basebands
   (default: ''=[]=all)

   .. rubric:: buildpdf
      

   True/False; if True and figfile is set, assemble pngs into a pdf

   .. rubric:: caltable
      

   A bandpass table, of type B or BPOLY

   .. rubric:: *caltable2*
      

   A second cal table, of type BPOLY or B, to overlay on a B table

   .. rubric:: *caltable3*
      

   A third cal table, of type BPOLY, to overlay on the first two

   .. rubric:: channeldiff
      

   Set to value > 0 to plot derivatives of amplitude. The value is
   also used as sigma, and any outliers beyond this sigma will be
   printed to the logger

   .. rubric:: *chanrange*
      

   set xrange over which to autoscale y-axis for xaxis='freq' (e.g.,
   "5~100")

   .. rubric:: *chanrangeSetXrange*
      

   If True, then chanrange also sets the xrange to display

   .. rubric:: *convert*
      

   Full path for convert command (in case it's not found)

   .. rubric:: *density*
      

   Dpi to use in creating PNGs and PDFs (default=108)

   .. rubric:: *edge*
      

   The number of edge channels to ignore in finding outliers (for
   channeldiff>0)

   .. rubric:: *field*
      

   must be an ID, source name, or list thereof; can use trailing \*:
   'J*'

   .. rubric:: *figfile*
      

   The base_name of the png files to save: base_name.antX.spwY.png

   .. rubric:: figfileSequential
      

   Naming scheme. False: name by spw/antenna (default).True:
   figfile.1.png, figfile.2.png, etc.

   .. rubric:: *gs*
      

   Full path for ghostscript command (in case it's not found)

   .. rubric:: *interactive*
      

   If False, then figfile will run to completion automatically

   .. rubric:: *lo1*
      

   Specify the LO1 setting (in GHz) for the observation

   .. rubric:: overlay
      

   Overlay 'antenna','time','spw', or 'baseband'; make 1 plot with
   different items in colors

   .. rubric:: *markersize*
      

   Size of points (default=3)

   .. rubric:: ms
      

   Name of the ms for this table, in case it does not match the
   string in the caltable

   .. rubric:: *parentms*
      

   Name of the parent ms, in case the ms has been previously split

   .. rubric:: *pdftk*
      

   Full path for pdftk command (in case it's not found)

   .. rubric:: *phase*
      

   The y-axis limits to use for phase plots when yaxis='both'

   .. rubric:: *platformingSigma*
      

   Declare platforming if the amplitude derivative exceeds this many
   times the MAD

   .. rubric:: *platformingThreshold*
      

   If *platformingSigma=0*, then declare platforming if the amplitude
   derivative exceeds this percentage of the median

   .. rubric:: *plotrange*
      

   Define axis limits: [x0,x1,y0,y1] where 0,0 means auto

   .. rubric:: *poln*
      

   Polarizations to plot (e.g., 'XX','YY','RR','LL' or '' for both)

   .. rubric:: *pwv*
      

   Define the precipitable water vapour(pwv) to use for the showatm
   option: 'auto' or value in mm

   .. rubric:: *resample*
      

   Channel expansion factor to use when computing MAD of derivative
   (for channeldiff>0)

   .. rubric:: *scans*
      

   Show only solutions for the specified scans (int, list, or string)

   .. rubric:: *showatm*
      

   Compute and overlay the atmospheric transmission curve (on B or
   T sys solutions)

   .. rubric:: *showatmfield*
      

   Use first observation of this fieldID or name

   .. rubric:: *showatmPoints*
      

   Draw atmospheric curve with points instead of a line

   .. rubric:: *showBasebandNumber*
      

   Put the BBC_NO in the title of each plot

   .. rubric:: *showfdm*
      

   When showing TDM spws with xaxis='freq', draw locations of FDM
   spws

   .. rubric:: *showflagged*
      

   Show the values of data, even if flagged

   .. rubric:: *showimage*
      

   Also show the atmospheric curve for the image sideband (in black)

   .. rubric:: *showtsky*
      

   Compute and overlay the sky temperature curve instead of
   transmission

   .. rubric:: *showlines*
      

   Draw lines connecting the data (default=True for amp, False for
   phase)

   .. rubric:: *showpoints*
      

   Draw points for the data (default=False for amp, True for phase)

   .. rubric:: *solutionTimeThresholdSeconds*
      

   Consider 2 solutions simultaneously if within this interval
   (default=60)

   .. rubric:: *spw*
      

   Must be single ID or list or range (e.g., "0~4", not the original
   ID)

   .. rubric:: *subplot*
      

   11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is
   ignored

   .. rubric:: *timeranges*
      

   Show only these timeranges, the first timerange being 0

   .. rubric:: *xaxis*
      

   'chan' or 'freq'

   .. rubric:: *yaxis*
      

   'amp', 'tsys', 'phase', or 'both' amp+phase == 'ap'. Append 'db'
   for dB

   .. rubric:: *zoom*
      

   'intersect' will zoom to overlap region of caltable with caltable2


.. _caltable:

caltable (string)
   | Input table name, either a bandpass solution or a Tsys solution

.. _antenna:

antenna ({string, int, stringArray, intArray}='')
   | A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.

.. _field:

field ({string, int, stringArray, intArray}='')
   | A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.

.. _spw:

spw ({string, int, stringArray, intArray}='')
   | A comma-delimited string list of spws for which to display solutions.  Default = all spws.

.. _yaxis:

yaxis (string='amp')
   | The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).

.. _xaxis:

xaxis (string='chan')
   | The quantity to plot on the x-axis ("chan" or "freq").

.. _figfile:

figfile (string='')
   | The name of the plot file to produce.

.. _plotrange:

plotrange (doubleArray=[0,0,0,0])
   | The axes limits to use [x0,x1,y0,y1].

.. _caltable2:

caltable2 (string='')
   | A second cal table, of type BPOLY or B, to overlay on a B table

.. _overlay:

overlay (string='')
   | Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)

.. _showflagged:

showflagged (bool=False)
   | Show the values of the solution, even if flagged

.. _timeranges:

timeranges (string='')
   | Show only these timeranges, the first timerange being 0

.. _buildpdf:

buildpdf (bool=False)
   | If True, assemble all the pngs into a pdf

.. _caltable3:

caltable3 (string='')
   | A third cal table, of type BPOLY, to overlay on the first two tables

.. _markersize:

markersize (int=3)
   | Size of points

.. _density:

density (int=108)
   | dpi to use in creating PNGs and PDFs (default=108)

.. _interactive:

interactive (bool=True)
   | if False, then run to completion automatically without pause

.. _showpoints:

showpoints ({string, bool}='auto')
   | Draw points for the data (default=F for amp, T for phase)

.. _showlines:

showlines ({string, bool}='auto')
   | Draw lines connecting the data (default=T for amp, F for phase)

.. _subplot:

subplot ({string, int}='22')
   | 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored

.. _zoom:

zoom (string='')
   | "intersect" will zoom to overlap region of caltable with caltable2

.. _poln:

poln ({stringArray, string}='['']')
   | Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"

.. _showatm:

showatm (bool=False)
   | Compute and overlay the atmospheric transmission curve

.. _pwv:

pwv ({double, string}='auto')
   | Define the pwv to use for the showatm option: "auto" or value in mm

.. _gs:

gs (string='gs')
   | For buildpdf=T, full path for ghostscript command (in case it is not found)

.. _convert:

convert (string='convert')
   | For buildpdf=T, full path for the ImageMagick convert command (in case it is not found)

.. _chanrange:

chanrange ({string, intArray}='')
   | Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"

.. _solutionTimeThresholdSeconds:

solutionTimeThresholdSeconds (double=30.0)
   | Consider 2 solutions simultaneous if within this interval in seconds

.. _debug:

debug (bool=False)
   | Print verbose messages for debugging purposes

.. _phase:

phase ({intArray, string}='['']')
   | The y-axis limits to use for phase plots when yaxis="both"

.. _vis:

vis (string='')
   | name of the ms for this table, in case it does not match the string in the caltable

.. _showtsky:

showtsky (bool=False)
   | Compute and overlay the sky temperature curve instead of transmission

.. _showfdm:

showfdm (bool=False)
   | when showing TDM spws, draw the locations of the corresponding FDM spws

.. _showatmfield:

showatmfield ({int, string}='')
   | for overlay="time", use first observation of this fieldID or name

.. _lo1:

lo1 ({string, double}='')
   | specify the LO1 setting (in GHz) for the observation ('' = automatic)

.. _showimage:

showimage (bool=False)
   | also show the atmospheric curve for the image sideband (in black)

.. _showatmpoints:

showatmpoints (bool=False)
   | Draw atmospheric curve with points instead of a line

.. _parentms:

parentms (string='')
   | if showimage=T, name of the parent ms (only needed if the ms has been previously split)

.. _pdftk:

pdftk (string='pdftk')
   | For buildpdf=T, full path for pdftk command (in case it is not found)

.. _channeldiff:

channeldiff ({bool, double}=False)
   | Set to a value > 0 (sigma) to plot derivatives of the solutions

.. _edge:

edge (int=8)
   | The number of edge channels to ignore in finding outliers (for channeldiff>0)

.. _resample:

resample (int=1)
   | The channel expansion factor to use when computing MAD of derivative (for channeldiff>0)

.. _platformingThreshold:

platformingThreshold (double=10.0)
   | if platformingSigma=0, then declare platforming if the amplitude derivative exceeds this percentage of the median

.. _platformingSigma:

platformingSigma (double=10.0)
   | declare platforming if the amplitude derivative exceeds this many times the MAD

.. _basebands:

basebands ({int, string, intArray}='')
   | A baseband number or list of baseband numbers for which to display solutions.  Default = all.

.. _showBasebandNumber:

showBasebandNumber (bool=False)
   | Put the baseband converter number (BBC_NO) in the title of each plot

.. _scans:

scans ({int, string, intArray}='')
   | A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".

.. _figfileSequential:

figfileSequential (bool=False)
   | naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.

.. _chanrangeSetXrange:

chanrangeSetXrange (bool=False)
   | If True, then chanrange also sets the xrange to display


    """
    pass
