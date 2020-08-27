#
# stub function definition file for docstring parsing
#

def listvis(vis, options='ap', datacolumn='data', field='', spw='*', selectdata=False, antenna='', timerange='', correlation='', scan='', feed='', array='', observation='', uvrange='', average='', showflags=False, pagerows=50, listfile=''):
    """
List measurement set visibilities.

| This task lists measurement set visibility data under a number of
|input selection conditions.  The measurement set data columns that
|can be listed are: the raw data, float_data, corrected data, model data,
|and residual (corrected - model) data.
|
|The output table format is dynamic.  Field, Spectral Window, and
|Channel columns are not displayed if the column contents are uniform.
|For example, if "spw = '1'" is specified, the spw column will not be
|displayed.  When a column is not displayed, a message is sent to the
|logger and terminal indicating that the column values are uniform and
|listing the uniform value.
|
|Table column descriptions:
|
|COLUMN NAME       DESCRIPTION
|-----------       -----------
|Date/Time         Time stamp of data sample (YYMMDD/HH:MM:SS UT)
|Intrf             Interferometer baseline (antenna names)
|UVDist            uv-distance (units of wavelength)
|Fld               Field ID (if more than 1)
|SpW               Spectral Window ID (if more than 1)
|Chn               Channel number (if more than 1)
|(Correlated       Correlated polarizations (eg: RR, LL, XY)
|  polarization)     Sub-columns are: Amp, Phs, Wt, F
|Amp               Visibility amplitude
|Phs               Visibility phase (deg)
|Wt                Weight of visibility measurement
|F                 Flag: 'F' = flagged datum; ' ' = unflagged
|UVW               UVW coordinates (meters)
|
|
|Input Parameters:
|vis         Name of input visibility file
|            default: none; example: vis='ngc5921.ms'
|
|options     List options: default = 'ap'
|            Not yet implemented for suboptions
|
|datacolumn  Visibility file data column:
|            default = 'data':  options are
|            data, float_data, corrected, model, residual (corrected-model)
|
|field       Select data based on field id(s) or name(s)
|            default: ''==>all; example: field='1'
|            field='0~2' field ids inclusive from 0 to 2
|            field='3C*' all field names starting with 3C
|
|spw         Select spectral window, channel to list
|            default: '0:0' --> spw=0, chan=0
|            spw='2:34' spectral window 2, channel 34
|
|selectdata  Toggle the following 7 selection parameters.
|            default: False; example: selectdata=True
|            If false, the following parameters are reset
|            to default values.
|
|      antenna     Select calibration data based on antenna
|                  default: ''-->all; examples:
|                  antenna = '5,6'; antenna index 5 and 6 solutions
|                  antenna = '05,06'; antenna names '05' and '06 solutions
|
|      timerange   Select time range to list
|                  default: ''-->all; examples:
|                  timerange='10:37:50.1'; list data for this sampling interval
|                  timerange='<10:37:25'; list data before 10:37:25
|
|      correlation Select polarization correlations to list
|                  default: ''-->all; examples:
|                  correlation='RR LL'; list RR and LL correlations
|                  correlation='XX XY'; list XX and XY correlations
|
|      scan        Select scans to list
|                  default: ''-->all; examples:
|                  scan='2'; list scan 2
|                  scan='>2'; list scan numbers greater than 2
|
|      feed        (not yet implemented)
|
|      array       (not yet implemented)
|
|      observation Select by observation ID.
|
|      uvrange     Select baseline lengths to list.
|                  default: ''--> all; examples:
|                  uvrange='<5klambda'; less than 5 kilo-wavelengths
|                  Caution: Input units default to meters.
|                  Listed units are always wavelengths.
|
|average     (not yet implemented)
|
|showflags   (not yet implemented)
|
|pagerows    rows per page of listing
|            default: 50; 0 --> do not paginate
|
|listfile    write output to disk; will not overwrite
|            default: '' --> write to screen
|            listfile = 'solutions.txt'

Parameters
----------
vis : string
   Name of input visibility file
options : string
   List options: ap only 
datacolumn : string
   Column to list: data, float_data, corrected, model, residual
field : string
   Field names or index to be listed
spw : string
   Spectral window channels 
selectdata : bool
   Other data selection parameters
observation : string, int
   Select by observation ID(s)
average : string
   Averaging mode 
showflags : bool
   Show flagged data (Not yet implemented)
pagerows : int
   Rows per page
listfile : string
   Output file

Other Parameters
----------
antenna : string
   Antenna/baselines
timerange : string
   Time range
correlation : string
   Correlations
scan : string
   Scan numbers
feed : string
   Multi-feed numbers (Not yet implemented)
array : string
   Array numbers (Not yet implemented)
uvrange : string
   uv range

Notes
-----





   task description



      List the visibility data in a MeasurementSet.

      This task lists MeasurementSet visibility data under a number
      of input selection conditions. The MeasurementSet data columns
      that can be listed are: raw data, float_data, corrected data,
      model data,and residual (corrected - model) data.

      The output table format is dynamic.The columns for field, spectral
      window, and channel are not displayed if the column contents are
      uniform. For example, if "spw = '1' " is specified, the spw column
      will not be displayed. When a column is not displayed, a message
      is sent to the logger and terminal indicating that the column
      values are uniform and listing the uniform value.

      Table column descriptions:

      +---------------------------+-----------------------------------------+
      | **Column Name**           | **Description**                         |
      +---------------------------+-----------------------------------------+
      | Date/Time                 | Time stamp of data sample               |
      |                           | (YYMMDD/HH:MM:SS UT)                    |
      +---------------------------+-----------------------------------------+
      | Intrf                     | Interferometer baseline (antenna names) |
      +---------------------------+-----------------------------------------+
      | UVDist                    | uv-distance (units of wavelength)       |
      +---------------------------+-----------------------------------------+
      | Fld                       | Field ID (if more than 1 field)         |
      +---------------------------+-----------------------------------------+
      | SpW                       | Spectral Window ID (if more than 1      |
      |                           | spectral window)                        |
      +---------------------------+-----------------------------------------+
      | Chn                       | Channel number (if more than 1 channel) |
      +---------------------------+-----------------------------------------+
      | (Correlated polarization) | Correlated polarizations (eg: RR, LL,   |
      |                           | XY). Sub-columns are: Amp, Phs, Wt, F   |
      +---------------------------+-----------------------------------------+
      | Amp                       | Visibility amplitude                    |
      +---------------------------+-----------------------------------------+
      | Phs                       | Visibility phase (deg)                  |
      +---------------------------+-----------------------------------------+
      | Wt                        | Weight of visibility measurement        |
      +---------------------------+-----------------------------------------+
      | F                         | Flag: 'F' = flagged datum; ' ' =        |
      |                           | unflagged                               |
      +---------------------------+-----------------------------------------+
      | UVW                       | UVW coordinates (meters)                |
      +---------------------------+-----------------------------------------+

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions
         :class: p1

      .. rubric:: *vis*
         :name: vis
         :class: p1

      Name of input visibility file.

      .. rubric:: *options*
         :name: options
         :class: p1

      List options: default = 'ap'. Not yet implemented for suboptions.

      .. rubric:: *datacolumn*
         :name: datacolumn

      Visibility file data column. Options are 'data' (default),
      'float_data', 'corrected', 'model', 'residual' (corrected-model).

      .. rubric:: *field*
         :name: field

      Select data based on field id(s) or name(s). Example: field='0~2'
      includes field ids 0 to 2; field='3C*' includes all field names
      starting with 3C. Default is all fields.

      .. rubric:: *spw*
         :name: spw

      Select spectral windows and channels to list.
      Example: spw='2:34~46' includes channels 34 to 46 of spectral
      window 2. Default is all spws and channels.

      .. rubric:: *selectdata*
         :name: selectdata
         :class: p1

      If selectdata=True, toggle the below 7 selection parameters. If
      selectdata=False, thefollowing parameters are reset to default
      values.

      .. rubric:: *antenna*
         :name: antenna

      Select data based on antenna. For example: antenna = '5,6'
      includes antenna index 5 and 6 solutions; antenna = '05,06'
      includes antenna names '05' and '06' solutions.

      .. rubric:: *timerange*
         :name: timerange
         :class: p1

      Select time range to list. For example: timerange='10:37:50.1'
      lists data for this particular sampling interval;
      timerange='<10:37:25' list data before 10:37:25.

      .. rubric:: *correlation*
         :name: correlation
         :class: p1

      Select polarization correlations to list. For example:
      correlation='RR LL' list RR and LL correlations; correlation='XX
      XY' list XX and XY correlations.

      .. rubric:: *scan*
         :name: scan
         :class: p1

      Select scans to list.For example: scan='2' lists scan 2;
      scan='>2' list scan numbers greater than 2.

      .. rubric:: feed (not yet implemented)
         :name: feed-not-yet-implemented
         :class: p1

      .. rubric:: array (not yet implemented)
         :name: array-not-yet-implemented
         :class: p1

      .. rubric:: *observation*
         :name: observation
         :class: p1

      Select by observation ID.

      .. rubric:: *uvrange*
         :name: uvrange
         :class: p1

      Select baseline lengths to list. For example: uvrange='<5klambda'
      lists all data from baselines less than 5 kilo-wavelengths;
      uvrange='500~1000m' lists all data from baselines between 500m and
      1000m.

      .. note:: CAUTION: Input units default to meters, but listed units are
         always wavelengths!

      .. rubric:: average (not yet implemented)
         :name: average-not-yet-implemented

      .. rubric:: showflags (not yet implemented)
         :name: showflags-not-yet-implemented

      .. rubric:: *pagerows*
         :name: pagerows
         :class: p1

      Rows per page of listing. Default: 50; pagerows=0 means do not
      paginate.

      .. rubric:: listfile
         :name: listfile

      Write output file to disk (will not overwrite). The default is to
      write to the screen.

    """
    pass
