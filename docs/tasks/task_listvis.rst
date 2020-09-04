Description
   List the visibility data in a MeasurementSet.

   This task lists MeasurementSet visibility data under a number
   ofinput selection conditions. The MeasurementSet data columns
   thatcan be listed are: raw data, float_data, corrected data,
   model data,and residual (corrected - model) data.

   The output table format is dynamic.The columns for field, spectral
   window, and channel are not displayed if the column contents are
   uniform.For example, if "spw = '1'" is specified, the spw column
   will not bedisplayed. When a column is not displayed, a message
   is sent to thelogger and terminal indicating that the column
   values are uniform andlisting the uniform value.

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
      

   .. rubric:: *vis*
      

   Name of input visibility file.

   .. rubric:: *options*
      

   List options: default = 'ap'. Not yet implemented for suboptions.

   .. rubric:: *datacolumn*
      

   Visibility file data column. Options are 'data' (default),
   'float_data', 'corrected', 'model', 'residual' (corrected-model).

   .. rubric:: *field*
      

   Select data based on field id(s) or name(s). Example: field='0~2'
   includes field ids 0 to 2; field='3C*' includes all field names
   starting with 3C. Default is all fields.

   .. rubric:: *spw*
      

   Select spectral windows and channels to list.
   Example: spw='2:34~46' includes channels 34 to 46 of spectral
   window 2. Default is all spws and channels.

   .. rubric:: *selectdata*
      

   If selectdata=True, toggle the below 7 selection parameters. If
   selectdata=False, thefollowing parameters are reset to default
   values.

   .. rubric:: *antenna*
      

   Select data based on antenna. For example: antenna = '5,6'
   includes antenna index 5 and 6 solutions;antenna = '05,06'
   includes antenna names '05' and '06' solutions.

   .. rubric:: *timerange*
      

   Select time range to list. For example: timerange='10:37:50.1'
   lists data for this particular sampling interval;
   timerange='<10:37:25' list data before 10:37:25.

   .. rubric:: *correlation*
      

   Select polarization correlations to list. For example:
   correlation='RR LL' list RR and LL correlations;correlation='XX
   XY' list XX and XY correlations.

   .. rubric:: *scan*
      

   Select scans to list.For example: scan='2' lists scan 2;
   scan='>2' list scan numbers greater than 2.

   .. rubric:: feed (not yet implemented)
      

   .. rubric:: array (not yet implemented)
      

   .. rubric:: *observation*
      

   Select by observation ID.

   .. rubric:: *uvrange*
      

   Select baseline lengths to list. For example: uvrange='<5klambda'
   lists all data from baselines less than 5 kilo-wavelengths;
   uvrange='500~1000m' lists all data from baselines between 500m and
   1000m.

   .. warning:: CAUTION: Input units default to meters, but listed units are
      always wavelengths!

   .. rubric:: average (not yet implemented)
      

   .. rubric:: showflags (not yet implemented)
      

   .. rubric:: *pagerows*
      

   Rows per page of listing. Default: 50; pagerows=0 means do not
   paginate.

   .. rubric:: listfile
      

   Write output file to disk (will not overwrite). The default is to
   write to the screen.
