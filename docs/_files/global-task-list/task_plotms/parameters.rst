.. container::
   :name: viewlet-above-content-title

Parameters
==========

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   task plotms parameters

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container:: pat-autotoc
      :name: parent-fieldname-text

      .. container:: parsed-parameters

         .. container:: param

            .. container:: parameters2

               vis : string

            Input MS or CalTable (blank for none)

Example

.. container:: param

   .. container:: parameters2

      gridrows : int = 1

   Number of subplot rows

Example

.. container:: param

   .. container:: parameters2

      gridcols : int = 1

   Number of subplot columns

Example

.. container:: param

   .. container:: parameters2

      rowindex : int = 0

   Row location of the plot (0-based)

Example

.. container:: param

   .. container:: parameters2

      colindex : int = 0

   Column location of the plot (0-based)

Example

.. container:: param

   .. container:: parameters2

      plotindex : int = 0

   Index to address a subplot (0-based)

Example

.. container:: param

   .. container:: parameters2

      xaxis : string

   Plot x-axis (blank for default/current)

Allowed Value(s)

scan Scan field Field time Time interval time_interval timeinterval
timeint Interval spw Spw channel chan Channel frequency freq Frequency
correlation corr Corr antenna1 ant1 Antenna1 antenna2 ant2 Antenna2
baseline Baseline row Row observation Observation intent Intent feed1
Feed1 feed2 Feed2 uvdist UVdist uvwave uvdist_l uvdistl UVwave u U v V w
W uwave Uwave vwave Vwave wwave Wwave velocity vel Velocity amp
amplitude Amp phase Phase real Real imag imaginary Imag wt Wt weight
wt*amp Wt*Amp wtsp WtSp weightspectrum WeightSpectrum sigma Sigma
sigmasp SigmaSp sigmaspectrum SigmaSpectrum flag Flag azimuth Azimuth
elevation Elevation hourang hourangle HourAngle parang parangle
parallacticangle ParAngle antenna ant Antenna ant-azimuth Ant-Azimuth
ant-elevation Ant-Elevation ant-ra Ant-RA ant-dec Ant-DEC ant-parang
ant-parangle ant-parallacticangle Ant-Parangle flagrow FlagRow gainamp
gamp GainAmp gainphase gphase GainPhase gainreal greal GainReal gainimag
gimag GainImag delay del Delay swp swpower switchedpower SwPower spgain
tsys Tsys opac opacity Opac snr SNR tec TEC antpos Antenna Positions
antenna positions radialvelocity Radial Velocity rho Distance

Example

.. container:: param

   .. container:: parameters2

      xdatacolumn : string

   Data column to use for x-axis (blank for default/current). Note that
   unspecified residuals are complex (vector) differences or ratios.

Allowed Value(s)

data corrected model float residual corrected-model
corrected-model_vector corrected-model_scalar data-model
data-model_vector data-model_scalar corrected/model
corrected/model_vector corrected/model_scalar data/model
data/model_vector data/model_scalar

Example

.. container:: param

   .. container:: parameters2

      xframe : string

   Coordinate frame to use for x-axis

Allowed Value(s)

icrs j2000 b1950 galactic azelgeo

Example

.. container:: param

   .. container:: parameters2

      xinterp : string

   Interpolation method for x-axis

Allowed Value(s)

nearest cubic spline spline

Example

.. container:: param

   .. container:: parameters2

      yaxis : undefined

   Plot y-axis (blank for default/current)

Allowed Value(s)

scan Scan field Field time Time interval time_interval timeinterval
timeint Interval spw Spw channel chan Channel frequency freq Frequency
correlation corr Corr antenna1 ant1 Antenna1 antenna2 ant2 Antenna2
baseline Baseline row Row observation Observation intent Intent feed1
Feed1 feed2 Feed2 uvdist UVdist uvwave uvdist_l uvdistl UVwave u U v V w
W uwave Uwave vwave Vwave wwave Wwave velocity vel Velocity amp
amplitude Amp phase Phase real Real imag imaginary Imag wt Wt weight
wt*amp Wt*Amp wtsp WtSp weightspectrum WeightSpectrum sigma Sigma
sigmasp SigmaSp sigmaspectrum SigmaSpectrum flag Flag azimuth Azimuth
elevation Elevation hourang hourangle HourAngle parang parangle
parallacticangle ParAngle antenna ant Antenna ant-azimuth Ant-Azimuth
ant-elevation Ant-Elevation ant-ra Ant-RA ant-dec Ant-DEC ant-parang
ant-parangle ant-parallacticangle Ant-Parangle flagrow FlagRow gainamp
gamp GainAmp gainphase gphase GainPhase gainreal greal GainReal gainimag
gimag GainImag delay del Delay swp swpower switchedpower SwPower spgain
tsys Tsys opac opacity Opac snr SNR tec TEC antpos Antenna Positions
antenna positions radialvelocity Radial Velocity rho Distance ra RA
Right Ascension

Example

.. container:: param

   .. container:: parameters2

      ydatacolumn : undefined

   Data column to use for y-axis (blank for default/current). Note that
   unspecified residuals are complex (vector) differences or ratios.

Allowed Value(s)

data corrected model float residual corrected-model
corrected-model_vector corrected-model_scalar data-model
data-model_vector data-model_scalar corrected/model
corrected/model_vector corrected/model_scalar data/model
data/model_vector data/model_scalar

Example

.. container:: param

   .. container:: parameters2

      yframe : undefined

   Coordinate frame to use for y-axis

Allowed Value(s)

icrs j2000 b1950 galactic azelgeo

Example

.. container:: param

   .. container:: parameters2

      yinterp : undefined

   Interpolation method for y-axis

Allowed Value(s)

nearest cubic spline spline

Example

.. container:: param

   .. container:: parameters2

      yaxislocation : undefined

   Location of the y-axis (blank for default: left)

Allowed Value(s)

left right

Example

.. container:: param

   .. container:: parameters2

      selectdata : bool = True

   Enable data selection parameters

Example

.. container:: param

   .. container:: parameters2

      field : string

   Field names or ids (blank for all)

Example

.. container:: param

   .. container:: parameters2

      spw : string

   Spectral windows:channels (blank for all)

Example

.. container:: param

   .. container:: parameters2

      timerange : string

   Time range (blank for all)

Example

.. container:: param

   .. container:: parameters2

      uvrange : string

   UV range (blank for all)

Example

.. container:: param

   .. container:: parameters2

      antenna : string

   Baseline/antenna names or ids (blank for all)

Example

.. container:: param

   .. container:: parameters2

      scan : string

   Scan numbers (blank for all)

Example

.. container:: param

   .. container:: parameters2

      correlation : string

   Correlations/polarizations (blank for all)

Example

.. container:: param

   .. container:: parameters2

      array : string

   (Sub)array numbers (blank for all)

Example

.. container:: param

   .. container:: parameters2

      observation : string

   Observation IDs (blank for all)

Example

.. container:: param

   .. container:: parameters2

      intent : string

   Observing intent (blank for all)

Example

.. container:: param

   .. container:: parameters2

      feed : string

   Feed numbers (blank for all)

Example

.. container:: param

   .. container:: parameters2

      msselect : string

   MSSelection TaQL string (blank for none)

Example

.. container:: param

   .. container:: parameters2

      averagedata : bool = True

   Enable data averaging parameters

Example

.. container:: param

   .. container:: parameters2

      avgchannel : string

   Average over channel (blank = False, otherwise value in channels)

Example

.. container:: param

   .. container:: parameters2

      avgtime : string

   Average over time (blank = False, otherwise value in seconds)

Example

.. container:: param

   .. container:: parameters2

      avgscan : bool = False

   Average over scans. Only valid with time averaging

Example

.. container:: param

   .. container:: parameters2

      avgfield : bool = False

   Average over fields. Only valid with time averaging

Example

.. container:: param

   .. container:: parameters2

      avgbaseline : bool = False

   Average over all baselines (mutually exclusive with avgantenna)

Example

.. container:: param

   .. container:: parameters2

      avgantenna : bool = False

   Average per antenna (mutually exclusive with avgbaseline)

Example

.. container:: param

   .. container:: parameters2

      avgspw : bool = False

   Average over all spectral windows

Example

.. container:: param

   .. container:: parameters2

      scalar : bool = False

   Scalar averaging (False=vector averaging)

Example

.. container:: param

   .. container:: parameters2

      transform : bool = True

   Enable data transformations

Example

.. container:: param

   .. container:: parameters2

      freqframe : string

   The frame in which to render frequency and velocity axes

Allowed Value(s)

LSRK LSRD BARY GEO TOPO GALACTO LGROUP CMB

Example

.. container:: param

   .. container:: parameters2

      restfreq : string

   Rest frequency to use for velocity conversions

Example

.. container:: param

   .. container:: parameters2

      veldef : string = RADIO

   The definition in which to render velocity

Allowed Value(s)

RADIO OPTICAL TRUE

Example

.. container:: param

   .. container:: parameters2

      shift : doubleArray = 0.0 0.0

   Adjust phases by this approximate phase center shift [dx,dy] (arcsec)

Example

.. container:: param

   .. container:: parameters2

      extendflag : bool = False

   Extend flagging to other data points not plotted

Example

.. container:: param

   .. container:: parameters2

      extcorr : bool = False

   Extend flags based on correlation

Example

.. container:: param

   .. container:: parameters2

      extchannel : bool = False

   Extend flags based on channel

Example

.. container:: param

   .. container:: parameters2

      iteraxis : string

   The axis over which to iterate

Allowed Value(s)

scan Scan field Field spw Spw baseline Baseline antenna Antenna time
Time corr Corr

Example

.. container:: param

   .. container:: parameters2

      xselfscale : bool = False

   When True, iterated plots have a common x-axis range (scale).

Example

.. container:: param

   .. container:: parameters2

      yselfscale : bool = False

   When True, iterated plots have a common y-axis range (scale).

Example

.. container:: param

   .. container:: parameters2

      xsharedaxis : bool = False

   Iterated plots on a grid share a common external x-axis per column.
   Must also set xselfscale=True and gridrows>1.

Example

.. container:: param

   .. container:: parameters2

      ysharedaxis : bool = False

   Iterated plots on a grid share a common external y-axis per row. Must
   also set yselfscale=True and gridcols>1.

Example

.. container:: param

   .. container:: parameters2

      customsymbol : undefined = False

   Enable custom symbol(s) for unflagged points

Example

.. container:: param

   .. container:: parameters2

      symbolshape : undefined = autoscaling

   Shape of plotted unflagged symbols

Allowed Value(s)

nosymbol autoscaling circle square diamond pixel

Example

.. container:: param

   .. container:: parameters2

      symbolsize : undefined = 2

   Size of plotted unflagged symbols

Example

.. container:: param

   .. container:: parameters2

      symbolcolor : undefined = 0000ff

   Color (name or hex code) of plotted unflagged symbols

Example

.. container:: param

   .. container:: parameters2

      symbolfill : undefined = fill

   Fill type of plotted unflagged symbols

Allowed Value(s)

fill mesh1 mesh2 mesh3 nofill

Example

.. container:: param

   .. container:: parameters2

      symboloutline : undefined = False

   Outline plotted unflagged symbols

Example

.. container:: param

   .. container:: parameters2

      coloraxis : string

   Selects data axis for colorizing

Allowed Value(s)

scan Scan field Field spw Spw antenna1 ant1 Antenna1 antenna2 ant2
Antenna2 baseline Baseline channel chan Channel corr Corr time Time
observation Observation intent Intent

Example

.. container:: param

   .. container:: parameters2

      customflaggedsymbol : undefined = False

   Enable custom symbol(s) for flagged points

Example

.. container:: param

   .. container:: parameters2

      flaggedsymbolshape : undefined = circle

   Shape of plotted flagged symbols

Allowed Value(s)

nosymbol autoscaling circle square diamond pixel

Example

.. container:: param

   .. container:: parameters2

      flaggedsymbolsize : undefined = 2

   Size of plotted flagged symbols

Example

.. container:: param

   .. container:: parameters2

      flaggedsymbolcolor : undefined = ff0000

   Color (name or hex code) of plotted flagged symbols

Example

.. container:: param

   .. container:: parameters2

      flaggedsymbolfill : undefined = fill

   Fill type of plotted flagged symbols

Allowed Value(s)

fill mesh1 mesh2 mesh3 nofill

Example

.. container:: param

   .. container:: parameters2

      flaggedsymboloutline : undefined = False

   Outline plotted flagged symbols

Example

.. container:: param

   .. container:: parameters2

      xconnector : string

   Set connector for data points (blank="none"; "line","step")

Allowed Value(s)

none line step

Example

.. container:: param

   .. container:: parameters2

      timeconnector : bool = False

   Connect points by time rather than x-axis

Example

.. container:: param

   .. container:: parameters2

      plotrange : doubleArray

   Plot axes ranges: [xmin,xmax,ymin,ymax]

Example

.. container:: param

   .. container:: parameters2

      title : string

   Title at top of plot

Example

.. container:: param

   .. container:: parameters2

      titlefont : int = 0

   Font size for plot title

Example

.. container:: param

   .. container:: parameters2

      xlabel : string

   Text for horizontal x-axis. Blank for default.

Example

.. container:: param

   .. container:: parameters2

      xaxisfont : int = 0

   Font size for x-axis label

Example

.. container:: param

   .. container:: parameters2

      ylabel : string

   Text for vertical y-axis. Blank for default.

Example

.. container:: param

   .. container:: parameters2

      yaxisfont : int = 0

   Font size for y-axis label

Example

.. container:: param

   .. container:: parameters2

      showmajorgrid : bool = False

   Show major grid lines

Example

.. container:: param

   .. container:: parameters2

      majorwidth : int = 1

   Line width in pixels of major grid lines

Example

.. container:: param

   .. container:: parameters2

      majorstyle : string

   Major grid line style

Allowed Value(s)

solid dash dot none

Example

.. container:: param

   .. container:: parameters2

      majorcolor : string = B0B0B0

   Color (name or hex code) of major grid lines

Example

.. container:: param

   .. container:: parameters2

      showminorgrid : bool = False

   Show minor grid lines

Example

.. container:: param

   .. container:: parameters2

      minorwidth : int = 1

   Line width in pixels of minor grid lines

Example

.. container:: param

   .. container:: parameters2

      minorstyle : string

   Minor grid line style

Allowed Value(s)

solid dash dot none

Example

.. container:: param

   .. container:: parameters2

      minorcolor : string = D0D0D0

   Color (name or hex code) of minor grid lines

Example

.. container:: param

   .. container:: parameters2

      showlegend : bool = False

   Show a legend on the plot.

Example

.. container:: param

   .. container:: parameters2

      legendposition : string

   Legend position, default upperRight.

Allowed Value(s)

upperRight upperLeft lowerRight lowerLeft exteriorRight exteriorLeft
exteriorTop exteriorBottom

Example

.. container:: param

   .. container:: parameters2

      plotfile : string

   Name of plot file to save automatically

Example

.. container:: param

   .. container:: parameters2

      expformat : string

   Export format type. If not provided, plotfile extension will be used
   to determine type.

Allowed Value(s)

jpg png pdf ps txt

Example

.. container:: param

   .. container:: parameters2

      verbose : bool = True

   Include metadata in text export

Example

.. container:: param

   .. container:: parameters2

      exprange : string

   Range of iteration plots to export, one plotfile per page. Multipage
   pdf exports are not supported.

Allowed Value(s)

current all

Example

.. container:: param

   .. container:: parameters2

      highres : bool = False

   Use high resolution

Example

.. container:: param

   .. container:: parameters2

      dpi : int = -1

   DPI of exported plot

Example

.. container:: param

   .. container:: parameters2

      width : int = -1

   Width in pixels of exported plot

Example

.. container:: param

   .. container:: parameters2

      height : int = -1

   Height in pixels of exported plot

Example

.. container:: param

   .. container:: parameters2

      overwrite : bool = False

   Overwrite plot file if it already exists

Example

.. container:: param

   .. container:: parameters2

      showgui : bool = True

   Show GUI

Example

.. container:: param

   .. container:: parameters2

      clearplots : bool = True

   Remove any existing plots so new ones can replace them.

Example

.. container:: param

   .. container:: parameters2

      callib : stringArray

   Calibration library string or filename for on-the-fly calibration.

Example

.. container:: param

   .. container:: parameters2

      headeritems : string

   Comma-separated list of pre-defined page header items.

Example

.. container:: param

   .. container:: parameters2

      showatm : bool = False

   Compute and overlay the atmospheric transmission curve

Example

.. container:: param

   .. container:: parameters2

      showtsky : bool = False

   Compute and overlay the sky temperature curve

Example

.. container:: param

   .. container:: parameters2

      showimage : bool = False

   Compute and overlay the image sideband curve

Example

.. container:: section
   :name: viewlet-below-content-body
