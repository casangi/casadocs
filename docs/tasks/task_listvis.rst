

.. _Description:

Description
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
   
   *vis*
   
   Name of input visibility file.
   
   *options*
   
   List options: default = 'ap'. Not yet implemented for suboptions.
   
   *datacolumn*
   
   Visibility file data column. Options are 'data' (default),
   'float_data', 'corrected', 'model', 'residual' (corrected-model).
   
   *field*
   
   Select data based on field id(s) or name(s). Example: field='0~2'
   includes field ids 0 to 2; field='3C*' includes all field names
   starting with 3C. Default is all fields.
   
   *spw*
   
   Select spectral windows and channels to list.
   Example: spw='2:34~46' includes channels 34 to 46 of spectral
   window 2. Default is all spws and channels.
   
   *selectdata*
   
   If selectdata=True, toggle the below 7 selection parameters. If
   selectdata=False, thefollowing parameters are reset to default
   values.
   
   *antenna*
   
   Select data based on antenna. For example: antenna = '5,6'
   includes antenna index 5 and 6 solutions; antenna = '05,06'
   includes antenna names '05' and '06' solutions.
   
   *timerange*

   Select time range to list. For example: timerange='10:37:50.1'
   lists data for this particular sampling interval;
   timerange='<10:37:25' list data before 10:37:25.
   
   *correlation*
   
   Select polarization correlations to list. For example:
   correlation='RR LL' list RR and LL correlations; correlation='XX
   XY' list XX and XY correlations.
   
   *scan*
   
   Select scans to list.For example: scan='2' lists scan 2;
   scan='>2' list scan numbers greater than 2.
   
   *feed (not yet implemented)*
   
   *array (not yet implemented)*
   
   *observation*
   
   Select by observation ID.
   
   *uvrange*
   
   Select baseline lengths to list. For example: uvrange='<5klambda'
   lists all data from baselines less than 5 kilo-wavelengths;
   uvrange='500~1000m' lists all data from baselines between 500m and
   1000m.
   
   .. warning:: CAUTION: Input units default to meters, but listed units are
      always wavelengths!
   
   *average (not yet implemented)*

   *showflags (not yet implemented)*
   
   *pagerows*
   
   Rows per page of listing. Default: 50; pagerows=0 means do not
   paginate.
   
   *listfile*
   
   Write output file to disk (will not overwrite). The default is to
   write to the screen.
   

.. _Examples:

Examples
   To list the visibilities from the DATA column of a MeasurementSet,
   including all data from spectral windows 2 to 4 which have RR
   correlation:
   
   ::
   
      listvis(vis='filename.ms', datacolumn='data', spw='2~4',
              selectdata=True, correlation='RR', pagerows=5,
              listfile='listfile.txt')
   
   The visibilities are listed with 5 rows per page and written out
   in a text file called 'listfile.txt'.
   

.. _Development:

Development
   No additional development details

