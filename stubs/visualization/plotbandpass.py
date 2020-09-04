#
# stub function definition file for docstring parsing
#

def plotbandpass(caltable, antenna='', field='', spw='', yaxis='amp', xaxis='chan', figfile='', plotrange=[0,0,0,0], caltable2='', overlay='', showflagged=False, timeranges='', buildpdf=False, caltable3='', markersize=3, density=108, interactive=True, showpoints='auto', showlines='auto', subplot='22', zoom='', poln='['']', showatm=False, pwv='auto', gs='gs', convert='convert', chanrange='', solutionTimeThresholdSeconds=30.0, debug=False, phase='['']', vis='', showtsky=False, showfdm=False, showatmfield='', lo1='', showimage=False, showatmpoints=False, parentms='', pdftk='pdftk', channeldiff=False, edge=8, resample=1, platformingThreshold=10.0, platformingSigma=10.0, basebands='', showBasebandNumber=False, scans='', figfileSequential=False, chanrangeSetXrange=False):
    r"""
Makes detailed plots of Tsys and bandpass solutions.

Parameters
   - **caltable** (string) - Input table name, either a bandpass solution or a Tsys solution [1]_
   - **antenna** ({string, int, stringArray, intArray}='') - A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas. [2]_
   - **field** ({string, int, stringArray, intArray}='') - A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields. [3]_
   - **spw** ({string, int, stringArray, intArray}='') - A comma-delimited string list of spws for which to display solutions.  Default = all spws. [4]_
   - **yaxis** (string='amp') - The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB). [5]_

      .. raw:: html

         <details><summary><i> yaxis = both </i></summary>

      - **phase** ({intArray, string}='['']') - The y-axis limits to use for phase plots when yaxis="both" [30]_

      .. raw:: html

         </details>
   - **xaxis** (string='chan') - The quantity to plot on the x-axis ("chan" or "freq"). [6]_

      .. raw:: html

         <details><summary><i> xaxis = freq </i></summary>

      - **chanrange** ({string, intArray}='') - Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq" [27]_
      - **showfdm** (bool=False) - when showing TDM spws, draw the locations of the corresponding FDM spws [33]_
      - **chanrangeSetXrange** (bool=False) - If True, then chanrange also sets the xrange to display [49]_

      .. raw:: html

         </details>
   - **figfile** (string='') - The name of the plot file to produce. [7]_
   - **plotrange** (doubleArray=[0,0,0,0]) - The axes limits to use [x0,x1,y0,y1]. [8]_
   - **caltable2** (string='') - A second cal table, of type BPOLY or B, to overlay on a B table [9]_
   - **overlay** (string='') - Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna) [10]_

      .. raw:: html

         <details><summary><i> overlay = time </i></summary>

      - **showatmfield** ({int, string}='') - for overlay="time", use first observation of this fieldID or name [34]_

      .. raw:: html

         </details>
   - **showflagged** (bool=False) - Show the values of the solution, even if flagged [11]_
   - **timeranges** (string='') - Show only these timeranges, the first timerange being 0 [12]_
   - **markersize** (int=3) - Size of points [15]_
   - **interactive** (bool=True) - if False, then run to completion automatically without pause [17]_
   - **showpoints** ({string, bool}='auto') - Draw points for the data (default=F for amp, T for phase) [18]_
   - **showlines** ({string, bool}='auto') - Draw lines connecting the data (default=T for amp, F for phase) [19]_
   - **subplot** ({string, int}='22') - 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored [20]_
   - **poln** ({stringArray, string}='['']') - Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY" [22]_
   - **showatm** (bool=False) - Compute and overlay the atmospheric transmission curve [23]_
   - **solutionTimeThresholdSeconds** (double=30.0) - Consider 2 solutions simultaneous if within this interval in seconds [28]_
   - **debug** (bool=False) - Print verbose messages for debugging purposes [29]_
   - **vis** (string='') - name of the ms for this table, in case it does not match the string in the caltable [31]_
   - **showtsky** (bool=False) - Compute and overlay the sky temperature curve instead of transmission [32]_
   - **channeldiff** ({bool, double}=False) - Set to a value > 0 (sigma) to plot derivatives of the solutions [40]_
   - **basebands** ({int, string, intArray}='') - A baseband number or list of baseband numbers for which to display solutions.  Default = all. [45]_
   - **showBasebandNumber** (bool=False) - Put the baseband converter number (BBC_NO) in the title of each plot [46]_
   - **scans** ({int, string, intArray}='') - A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time". [47]_
   - **figfileSequential** (bool=False) - naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc. [48]_


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




Details
   Explanation of each parameter

.. [1] 
   **caltable** (string)
      | Input table name, either a bandpass solution or a Tsys solution
.. [2] 
   **antenna** ({string, int, stringArray, intArray}='')
      | A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.
.. [3] 
   **field** ({string, int, stringArray, intArray}='')
      | A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.
.. [4] 
   **spw** ({string, int, stringArray, intArray}='')
      | A comma-delimited string list of spws for which to display solutions.  Default = all spws.
.. [5] 
   **yaxis** (string='amp')
      | The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).
.. [6] 
   **xaxis** (string='chan')
      | The quantity to plot on the x-axis ("chan" or "freq").
.. [7] 
   **figfile** (string='')
      | The name of the plot file to produce.
.. [8] 
   **plotrange** (doubleArray=[0,0,0,0])
      | The axes limits to use [x0,x1,y0,y1].
.. [9] 
   **caltable2** (string='')
      | A second cal table, of type BPOLY or B, to overlay on a B table
.. [10] 
   **overlay** (string='')
      | Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)
.. [11] 
   **showflagged** (bool=False)
      | Show the values of the solution, even if flagged
.. [12] 
   **timeranges** (string='')
      | Show only these timeranges, the first timerange being 0
.. [13] 
   **buildpdf** (bool=False)
      | If True, assemble all the pngs into a pdf
.. [14] 
   **caltable3** (string='')
      | A third cal table, of type BPOLY, to overlay on the first two tables
.. [15] 
   **markersize** (int=3)
      | Size of points
.. [16] 
   **density** (int=108)
      | dpi to use in creating PNGs and PDFs (default=108)
.. [17] 
   **interactive** (bool=True)
      | if False, then run to completion automatically without pause
.. [18] 
   **showpoints** ({string, bool}='auto')
      | Draw points for the data (default=F for amp, T for phase)
.. [19] 
   **showlines** ({string, bool}='auto')
      | Draw lines connecting the data (default=T for amp, F for phase)
.. [20] 
   **subplot** ({string, int}='22')
      | 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored
.. [21] 
   **zoom** (string='')
      | "intersect" will zoom to overlap region of caltable with caltable2
.. [22] 
   **poln** ({stringArray, string}='['']')
      | Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"
.. [23] 
   **showatm** (bool=False)
      | Compute and overlay the atmospheric transmission curve
.. [24] 
   **pwv** ({double, string}='auto')
      | Define the pwv to use for the showatm option: "auto" or value in mm
.. [25] 
   **gs** (string='gs')
      | For buildpdf=T, full path for ghostscript command (in case it is not found)
.. [26] 
   **convert** (string='convert')
      | For buildpdf=T, full path for the ImageMagick convert command (in case it is not found)
.. [27] 
   **chanrange** ({string, intArray}='')
      | Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"
.. [28] 
   **solutionTimeThresholdSeconds** (double=30.0)
      | Consider 2 solutions simultaneous if within this interval in seconds
.. [29] 
   **debug** (bool=False)
      | Print verbose messages for debugging purposes
.. [30] 
   **phase** ({intArray, string}='['']')
      | The y-axis limits to use for phase plots when yaxis="both"
.. [31] 
   **vis** (string='')
      | name of the ms for this table, in case it does not match the string in the caltable
.. [32] 
   **showtsky** (bool=False)
      | Compute and overlay the sky temperature curve instead of transmission
.. [33] 
   **showfdm** (bool=False)
      | when showing TDM spws, draw the locations of the corresponding FDM spws
.. [34] 
   **showatmfield** ({int, string}='')
      | for overlay="time", use first observation of this fieldID or name
.. [35] 
   **lo1** ({string, double}='')
      | specify the LO1 setting (in GHz) for the observation ('' = automatic)
.. [36] 
   **showimage** (bool=False)
      | also show the atmospheric curve for the image sideband (in black)
.. [37] 
   **showatmpoints** (bool=False)
      | Draw atmospheric curve with points instead of a line
.. [38] 
   **parentms** (string='')
      | if showimage=T, name of the parent ms (only needed if the ms has been previously split)
.. [39] 
   **pdftk** (string='pdftk')
      | For buildpdf=T, full path for pdftk command (in case it is not found)
.. [40] 
   **channeldiff** ({bool, double}=False)
      | Set to a value > 0 (sigma) to plot derivatives of the solutions
.. [41] 
   **edge** (int=8)
      | The number of edge channels to ignore in finding outliers (for channeldiff>0)
.. [42] 
   **resample** (int=1)
      | The channel expansion factor to use when computing MAD of derivative (for channeldiff>0)
.. [43] 
   **platformingThreshold** (double=10.0)
      | if platformingSigma=0, then declare platforming if the amplitude derivative exceeds this percentage of the median
.. [44] 
   **platformingSigma** (double=10.0)
      | declare platforming if the amplitude derivative exceeds this many times the MAD
.. [45] 
   **basebands** ({int, string, intArray}='')
      | A baseband number or list of baseband numbers for which to display solutions.  Default = all.
.. [46] 
   **showBasebandNumber** (bool=False)
      | Put the baseband converter number (BBC_NO) in the title of each plot
.. [47] 
   **scans** ({int, string, intArray}='')
      | A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".
.. [48] 
   **figfileSequential** (bool=False)
      | naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.
.. [49] 
   **chanrangeSetXrange** (bool=False)
      | If True, then chanrange also sets the xrange to display

    """
    pass
