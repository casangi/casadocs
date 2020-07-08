.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               caltable : string

            Input table name, either a bandpass solution or a Tsys
            solution

Example

.. container:: param

   .. container:: parameters2

      antenna : string int stringArray intArray

   A comma-delimited string list of antennas (either names or integer
   indices) for which to display solutions. Default = all antennas.

Example

.. container:: param

   .. container:: parameters2

      field : string int stringArray intArray

   A comma-delimited string list of fields (either names or integer
   indices) for which to display solutions. Default = all fields.

Example

.. container:: param

   .. container:: parameters2

      spw : string int stringArray intArray

   A comma-delimited string list of spws for which to display solutions.
   Default = all spws.

Example

.. container:: param

   .. container:: parameters2

      yaxis : string = amp

   The quantity to plot on the y-axis ("amp", "phase", "both", "tsys",
   append "db" for dB).

Allowed Value(s)

amp ampdb phase tsys both bothdb ap apdb

Example

.. container:: param

   .. container:: parameters2

      xaxis : string = chan

   The quantity to plot on the x-axis ("chan" or "freq").

Allowed Value(s)

chan freq

Example

.. container:: param

   .. container:: parameters2

      figfile : string

   The name of the plot file to produce.

Example

.. container:: param

   .. container:: parameters2

      plotrange : doubleArray = 0,0,0,0

   The axes limits to use [x0,x1,y0,y1].

Example

.. container:: param

   .. container:: parameters2

      caltable2 : string

   A second cal table, of type BPOLY or B, to overlay on a B table

Example

.. container:: param

   .. container:: parameters2

      overlay : string

   Show multiple solutions in same frame in different colors (time,
   antenna, spw, baseband, or time,antenna)

Allowed Value(s)

antenna baseband spw time antenna,time time,antenna

Example

.. container:: param

   .. container:: parameters2

      showflagged : bool = False

   Show the values of the solution, even if flagged

Example

.. container:: param

   .. container:: parameters2

      timeranges : string

   Show only these timeranges, the first timerange being 0

Example

.. container:: param

   .. container:: parameters2

      buildpdf : bool = False

   If True, assemble all the pngs into a pdf

Example

.. container:: param

   .. container:: parameters2

      caltable3 : string

   A third cal table, of type BPOLY, to overlay on the first two tables

Example

.. container:: param

   .. container:: parameters2

      markersize : int = 3

   Size of points

Example

.. container:: param

   .. container:: parameters2

      density : int = 108

   dpi to use in creating PNGs and PDFs (default=108)

Example

.. container:: param

   .. container:: parameters2

      interactive : bool = True

   if False, then run to completion automatically without pause

Example

.. container:: param

   .. container:: parameters2

      showpoints : string bool = auto

   Draw points for the data (default=F for amp, T for phase)

Example

.. container:: param

   .. container:: parameters2

      showlines : string bool = auto

   Draw lines connecting the data (default=T for amp, F for phase)

Example

.. container:: param

   .. container:: parameters2

      subplot : string int = 22

   11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is
   ignored

Allowed Value(s)

11 21 31 41 51 61 71 81 22 32 42

Example

.. container:: param

   .. container:: parameters2

      zoom : string

   "intersect" will zoom to overlap region of caltable with caltable2

Allowed Value(s)

intersect

Example

.. container:: param

   .. container:: parameters2

      poln : stringArray string

   Polarizations to plot: "" = all, or
   "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"

Example

.. container:: param

   .. container:: parameters2

      showatm : bool = False

   Compute and overlay the atmospheric transmission curve

Example

.. container:: param

   .. container:: parameters2

      pwv : double string = auto

   Define the pwv to use for the showatm option: "auto" or value in mm

Example

.. container:: param

   .. container:: parameters2

      gs : string = gs

   For buildpdf=T, full path for ghostscript command (in case it is not
   found)

Example

.. container:: param

   .. container:: parameters2

      convert : string = convert

   For buildpdf=T, full path for the ImageMagick convert command (in
   case it is not found)

Example

.. container:: param

   .. container:: parameters2

      chanrange : string intArray

   Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"

Example

.. container:: param

   .. container:: parameters2

      solutionTimeThresholdSeconds : double = 30.0

   Consider 2 solutions simultaneous if within this interval in seconds

Example

.. container:: param

   .. container:: parameters2

      debug : bool = False

   Print verbose messages for debugging purposes

Example

.. container:: param

   .. container:: parameters2

      phase : intArray string

   The y-axis limits to use for phase plots when yaxis="both"

Example

.. container:: param

   .. container:: parameters2

      vis : string

   name of the ms for this table, in case it does not match the string
   in the caltable

Example

.. container:: param

   .. container:: parameters2

      showtsky : bool = False

   Compute and overlay the sky temperature curve instead of transmission

Example

.. container:: param

   .. container:: parameters2

      showfdm : bool = False

   when showing TDM spws, draw the locations of the corresponding FDM
   spws

Example

.. container:: param

   .. container:: parameters2

      showatmfield : int string

   for overlay="time", use first observation of this fieldID or name

Example

.. container:: param

   .. container:: parameters2

      lo1 : string double

   specify the LO1 setting (in GHz) for the observation ('' = automatic)

Example

.. container:: param

   .. container:: parameters2

      showimage : bool = False

   also show the atmospheric curve for the image sideband (in black)

Example

.. container:: param

   .. container:: parameters2

      showatmpoints : bool = False

   Draw atmospheric curve with points instead of a line

Example

.. container:: param

   .. container:: parameters2

      parentms : string

   if showimage=T, name of the parent ms (only needed if the ms has been
   previously split)

Example

.. container:: param

   .. container:: parameters2

      pdftk : string = pdftk

   For buildpdf=T, full path for pdftk command (in case it is not found)

Example

.. container:: param

   .. container:: parameters2

      channeldiff : bool double = False

   Set to a value > 0 (sigma) to plot derivatives of the solutions

Example

.. container:: param

   .. container:: parameters2

      edge : int = 8

   The number of edge channels to ignore in finding outliers (for
   channeldiff>0)

Example

.. container:: param

   .. container:: parameters2

      resample : int = 1

   The channel expansion factor to use when computing MAD of derivative
   (for channeldiff>0)

Example

.. container:: param

   .. container:: parameters2

      platformingThreshold : double = 10.0

   if platformingSigma=0, then declare platforming if the amplitude
   derivative exceeds this percentage of the median

Example

.. container:: param

   .. container:: parameters2

      platformingSigma : double = 10.0

   declare platforming if the amplitude derivative exceeds this many
   times the MAD

Example

.. container:: param

   .. container:: parameters2

      basebands : int string intArray

   A baseband number or list of baseband numbers for which to display
   solutions. Default = all.

Example

.. container:: param

   .. container:: parameters2

      showBasebandNumber : bool = False

   Put the baseband converter number (BBC_NO) in the title of each plot

Example

.. container:: param

   .. container:: parameters2

      scans : int string intArray

   A scan or list of scans for which to display solutions. Default =
   all. Does not work with overlay="time".

Example

.. container:: param

   .. container:: parameters2

      figfileSequential : bool = False

   naming scheme for pngs: False: name by spw/antenna (default), True:
   figfile.000.png, figfile.001.png, etc.

Example

.. container:: param

   .. container:: parameters2

      chanrangeSetXrange : bool = False

   If True, then chanrange also sets the xrange to display

Example

.. container:: section
   :name: viewlet-below-content-body
