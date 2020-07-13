.. container::
   :name: viewlet-above-content-title

plotbandpass
============

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task description

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary
         :name: summary
         :class: p1

      Plots the bandpass and system temperature (T\ sys) solutions.

      This generic task was developed at the North American ALMA Science
      Center (NAASC). It displays T\ sys and bandpass solution tables
      with options to overlay them in various combinations, and/or with
      an atmospheric transmission or sky temperature model. It allows
      for mixed-mode spws (e.g., TDM and FDM for ALMA) and uses the msmd
      tool to access the information about an MS.

      Note that the ability to compute and overlay an atmospheric
      transmission curve or a sky temperature curve is now also
      available in **plotms**.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: *antenna*
         :name: antenna
         :class: p1

      Must be either an ID (int or string or list), or a single antenna
      name or list.

      .. rubric:: *basebands*
         :name: basebands
         :class: p1

      Show only spws from the specified baseband or list of basebands
      (default: ''=[]=all)

      .. rubric:: buildpdf
         :name: buildpdf
         :class: p1

      True/False; if True and figfile is set, assemble pngs into a pdf

      .. rubric:: caltable
         :name: caltable
         :class: p1

      A bandpass table, of type B or BPOLY

      .. rubric:: *caltable2*
         :name: caltable2
         :class: p1

      A second cal table, of type BPOLY or B, to overlay on a B table

      .. rubric:: *caltable3*
         :name: caltable3
         :class: p1

      A third cal table, of type BPOLY, to overlay on the first two

      .. rubric:: channeldiff
         :name: channeldiff

      Set to value > 0 to plot derivatives of amplitude. The value is
      also used as sigma, and any outliers beyond this sigma will be
      printed to the logger

      .. rubric:: *chanrange*
         :name: chanrange
         :class: p1

      set xrange over which to autoscale y-axis for xaxis='freq' (e.g.,
      "5~100")

      .. rubric:: *chanrangeSetXrange*
         :name: chanrangesetxrange
         :class: p1

      If True, then chanrange also sets the xrange to display

      .. rubric:: *convert*
         :name: convert

      Full path for convert command (in case it's not found)

      .. rubric:: *density*
         :name: density
         :class: p1

      Dpi to use in creating PNGs and PDFs (default=108)

      .. rubric:: *edge*
         :name: edge
         :class: p1

      The number of edge channels to ignore in finding outliers (for
      channeldiff>0)

      .. rubric:: *field*
         :name: field
         :class: p1

      must be an ID, source name, or list thereof; can use trailing \*:
      'J*'

      .. rubric:: *figfile*
         :name: figfile
         :class: p1

      The base_name of the png files to save: base_name.antX.spwY.png

      .. rubric:: figfileSequential
         :name: figfilesequential
         :class: p1

      Naming scheme. False: name by spw/antenna (default).True:
      figfile.1.png, figfile.2.png, etc.

      .. rubric:: *gs*
         :name: gs
         :class: p1

      Full path for ghostscript command (in case it's not found)

      .. rubric:: *interactive*
         :name: interactive
         :class: p1

      If False, then figfile will run to completion automatically

      .. rubric:: *lo1*
         :name: lo1
         :class: p1

      Specify the LO1 setting (in GHz) for the observation

      .. rubric:: overlay
         :name: overlay
         :class: p1

      Overlay 'antenna','time','spw', or 'baseband'; make 1 plot with
      different items in colors

      .. rubric:: *markersize*
         :name: markersize
         :class: p1

      Size of points (default=3)

      .. rubric:: ms
         :name: ms
         :class: p1

      Name of the ms for this table, in case it does not match the
      string in the caltable

      .. rubric:: *parentms*
         :name: parentms
         :class: p1

      Name of the parent ms, in case the ms has been previously split

      .. rubric:: *pdftk*
         :name: pdftk

      Full path for pdftk command (in case it's not found)

      .. rubric:: *phase*
         :name: phase
         :class: p1

      The y-axis limits to use for phase plots when yaxis='both'

      .. rubric:: *platformingSigma*
         :name: platformingsigma

      Declare platforming if the amplitude derivative exceeds this many
      times the MAD

      .. rubric:: *platformingThreshold*
         :name: platformingthreshold

      If *platformingSigma=0*, then declare platforming if the amplitude
      derivative exceeds this percentage of the median

      .. rubric:: *plotrange*
         :name: plotrange
         :class: p1

      Define axis limits: [x0,x1,y0,y1] where 0,0 means auto

      .. rubric:: *poln*
         :name: poln
         :class: p1

      Polarizations to plot (e.g., 'XX','YY','RR','LL' or '' for both)

      .. rubric:: *pwv*
         :name: pwv
         :class: p1

      Define the precipitable water vapour(pwv) to use for the showatm
      option: 'auto' or value in mm

      .. rubric:: *resample*
         :name: resample

      Channel expansion factor to use when computing MAD of derivative
      (for channeldiff>0)

      .. rubric:: *scans*
         :name: scans
         :class: p1

      Show only solutions for the specified scans (int, list, or string)

      .. rubric:: *showatm*
         :name: showatm
         :class: p1

      Compute and overlay the atmospheric transmission curve (on B or
      T\ sys solutions)

      .. rubric:: *showatmfield*
         :name: showatmfield
         :class: p1

      Use first observation of this fieldID or name

      .. rubric:: *showatmPoints*
         :name: showatmpoints
         :class: p1

      Draw atmospheric curve with points instead of a line

      .. rubric:: *showBasebandNumber*
         :name: showbasebandnumber
         :class: p1

      Put the BBC_NO in the title of each plot

      .. rubric:: *showfdm*
         :name: showfdm
         :class: p1

      When showing TDM spws with xaxis='freq', draw locations of FDM
      spws

      .. rubric:: *showflagged*
         :name: showflagged
         :class: p1

      Show the values of data, even if flagged

      .. rubric:: *showimage*
         :name: showimage
         :class: p1

      Also show the atmospheric curve for the image sideband (in black)

      .. rubric:: *showtsky*
         :name: showtsky
         :class: p1

      Compute and overlay the sky temperature curve instead of
      transmission

      .. rubric:: *showlines*
         :name: showlines
         :class: p1

      Draw lines connecting the data (default=True for amp, False for
      phase)

      .. rubric:: *showpoints*
         :name: showpoints
         :class: p1

      Draw points for the data (default=False for amp, True for phase)

      .. rubric:: *solutionTimeThresholdSeconds*
         :name: solutiontimethresholdseconds
         :class: p1

      Consider 2 solutions simultaneously if within this interval
      (default=60)

      .. rubric:: *spw*
         :name: spw
         :class: p1

      Must be single ID or list or range (e.g., "0~4", not the original
      ID)

      .. rubric:: *subplot*
         :name: subplot

      11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is
      ignored

      .. rubric:: *timeranges*
         :name: timeranges
         :class: p1

      Show only these timeranges, the first timerange being 0

      .. rubric:: *xaxis*
         :name: xaxis
         :class: p1

      'chan' or 'freq'

      .. rubric:: *yaxis*
         :name: yaxis
         :class: p1

      'amp', 'tsys', 'phase', or 'both' amp+phase == 'ap'. Append 'db'
      for dB

      .. rubric:: *zoom*
         :name: zoom
         :class: p1

      'intersect' will zoom to overlap region of caltable with caltable2

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_plotbandpass/about
   task_plotbandpass/examples
