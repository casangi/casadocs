

.. _Description:

Description
   This generic task was developed at the North American ALMA Science
   Center (NAASC). It displays T sys and bandpass solution tables
   with options to overlay them in various combinations, and/or with
   an atmospheric transmission or sky temperature model. It allows
   for mixed-mode spws (e.g., TDM and FDM for ALMA) and uses the msmd
   tool to access the information about an MS.
   
   Note that the ability to compute and overlay an atmospheric
   transmission curve or a sky temperature curve is now also
   available in **plotms**.

   
   .. rubric:: Parameter descriptions
   
   *antenna*
   
   Must be either an ID (int or string or list), or a single antenna
   name or list.
   
   *basebands*
   
   Show only spws from the specified baseband or list of basebands
   (default: ''=[]=all)
   
   *buildpdf*
   
   True/False; if True and figfile is set, assemble pngs into a pdf
   
   *caltable*
   
   A bandpass table, of type B or BPOLY
   
   *caltable2*
   
   A second cal table, of type BPOLY or B, to overlay on a B table
   
   *caltable3*
   
   A third cal table, of type BPOLY, to overlay on the first two
   
   *channeldiff*
   
   Set to value > 0 to plot derivatives of amplitude. The value is
   also used as sigma, and any outliers beyond this sigma will be
   printed to the logger
   
   *chanrange*
   
   set xrange over which to autoscale y-axis for xaxis='freq' (e.g.,
   "5~100")
   
   *chanrangeSetXrange*
   
   If True, then chanrange also sets the xrange to display
   
   *convert*
   
   Full path for convert command (in case it's not found)
   
   *density*
   
   Dpi to use in creating PNGs and PDFs (default=108)
   
   *edge*
   
   The number of edge channels to ignore in finding outliers (for
   channeldiff>0)
   
   *field*
   
   must be an ID, source name, or list thereof; can use trailing \*:
   'J*'
   
   *figfile*
   
   The base_name of the png files to save: base_name.antX.spwY.png
   
   *figfileSequential*
   
   Naming scheme. False: name by spw/antenna (default).True:
   figfile.1.png, figfile.2.png, etc.
   
   *gs*
   
   Full path for ghostscript command (in case it's not found)
   
   *interactive*
   
   If False, then figfile will run to completion automatically
   
   *lo1*
   
   Specify the LO1 setting (in GHz) for the observation
   
   *overlay*
   
   Overlay 'antenna','time','spw', or 'baseband'; make 1 plot with
   different items in colors
   
   *markersize*
   
   Size of points (default=3)
   
   *ms*
   
   Name of the ms for this table, in case it does not match the
   string in the caltable
   
   *parentms*
   
   Name of the parent ms, in case the ms has been previously split
   
   *pdftk*
   
   Full path for pdftk command (in case it's not found)
   
   *phase*
   
   The y-axis limits to use for phase plots when yaxis='both'
   
   *platformingSigma*
   
   Declare platforming if the amplitude derivative exceeds this many
   times the MAD
   
   *platformingThreshold*
   
   If *platformingSigma=0*, then declare platforming if the amplitude
   derivative exceeds this percentage of the median
   
   *plotrange*
   
   Define axis limits: [x0,x1,y0,y1] where 0,0 means auto
   
   *poln*
   
   Polarizations to plot (e.g., 'XX','YY','RR','LL' or '' for both)
   
   *pwv*
   
   Define the precipitable water vapour(pwv) to use for the showatm
   option: 'auto' or value in mm
   
   *resample*
   
   Channel expansion factor to use when computing MAD of derivative
   (for channeldiff>0)
   
   *scans*
   
   Show only solutions for the specified scans (int, list, or string)
   
   *showatm*
   
   Compute and overlay the atmospheric transmission curve (on B or
   T sys solutions)
   
   *showatmfield*
   
   Use first observation of this fieldID or name
   
   *showatmPoints*
   
   Draw atmospheric curve with points instead of a line
   
   *showBasebandNumber*
   
   Put the BBC_NO in the title of each plot
   
   *showfdm*
   
   When showing TDM spws with xaxis='freq', draw locations of FDM
   spws
   
   *showflagged*
   
   Show the values of data, even if flagged
   
   *showimage*
   
   Also show the atmospheric curve for the image sideband (in black)
   
   *showtsky*
   
   Compute and overlay the sky temperature curve instead of
   transmission
   
   *showlines*
   
   Draw lines connecting the data (default=True for amp, False for
   phase)
   
   *showpoints*
   
   Draw points for the data (default=False for amp, True for phase)
   
   *solutionTimeThresholdSeconds*
   
   Consider 2 solutions simultaneously if within this interval
   (default=60)
   
   *spw*
   
   Must be single ID or list or range (e.g., "0~4", not the original
   ID)
   
   *subplot*
   
   11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is
   ignored
   
   *timeranges*
   
   Show only these timeranges, the first timerange being 0
   
   *xaxis*
   
   'chan' or 'freq'
   
   *yaxis*
   
   'amp', 'tsys', 'phase', or 'both' amp+phase == 'ap'. Append 'db'
   for dB
   
   *zoom*
   
   'intersect' will zoom to overlap region of caltable with caltable2
   

.. _Examples:

Examples
   To plot the system temperature (channel vs. amplitude) of fields
   0, 1 and 4, overlaying all antennas, and printing a png plot:
   
   ::
   
      plotbandpass(caltable='X3c1.tsys', overlay='antenna',
                   yaxis='amp', field='0~1,4', xaxis='chan',
                   figfile='tsys.png').
   
   To overplot two bandpass tables, with x-axis frequency:
   
   ::
   
      plotbandpass(caltable='bandpass.bcal', caltable2='bandpass.bcal_smooth',
                   xaxis='freq')
   
   To overplot the XX-polarisation two bandpass tables, with x-axis
   frequency; the atmospheric transmission curve is also computed and
   overlaid:
   
   ::
   
      plotbandpass(caltable='bandpass.bcal', caltable2='bandpass.bcal_smooth',
                   xaxis='freq', poln='X', showatm=True)
   
   The following returns void unless the *channeldiff* option is
   selected, in which case it returns a dictionary containing the
   statistics of the solutions, keyed by the antenna name,
   followed by the spw, timerange, polarization, and finally 'amp'
   and/or 'phase' depending on the yaxis selection.
   
   ::
   
      plotbandpass(caltable='bandpass.bcal',channeldiff='5')
   

.. _Development:

Development
   No additional development details

