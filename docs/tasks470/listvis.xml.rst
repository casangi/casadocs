listvis -- List measurement set visibilities. -- information, analysis task
=======================================

Description
---------------------------------------


This task lists measurement set visibility data under a number of
input selection conditions.  The measurement set data columns that 
can be listed are: the raw data, float_data, corrected data, model data, 
and residual (corrected - model) data.

The output table format is dynamic.  Field, Spectral Window, and
Channel columns are not displayed if the column contents are uniform.
For example, if "spw = '1'" is specified, the spw column will not be
displayed.  When a column is not displayed, a message is sent to the
logger and terminal indicating that the column values are uniform and 
listing the uniform value.

Table column descriptions:

COLUMN NAME       DESCRIPTION
-----------       -----------
Date/Time         Time stamp of data sample (YYMMDD/HH:MM:SS UT)
Intrf             Interferometer baseline (antenna names)
UVDist            uv-distance (units of wavelength)
Fld               Field ID (if more than 1)
SpW               Spectral Window ID (if more than 1)
Chn               Channel number (if more than 1)
(Correlated       Correlated polarizations (eg: RR, LL, XY)
  polarization)     Sub-columns are: Amp, Phs, Wt, F
Amp               Visibility amplitude
Phs               Visibility phase (deg)
Wt                Weight of visibility measurement
F                 Flag: 'F' = flagged datum; ' ' = unflagged
UVW               UVW coordinates (meters)


Input Parameters:
vis         Name of input visibility file
            default: none; example: vis='ngc5921.ms'

options     List options: default = 'ap'
            Not yet implemented for suboptions

datacolumn  Visibility file data column:
            default = 'data':  options are
            data, float_data, corrected, model, residual (corrected-model)

field       Select data based on field id(s) or name(s)
            default: ''==>all; example: field='1'
            field='0~2' field ids inclusive from 0 to 2
            field='3C*' all field names starting with 3C

spw         Select spectral window, channel to list
            default: '0:0' --> spw=0, chan=0
            spw='2:34' spectral window 2, channel 34

selectdata  Toggle the following 7 selection parameters.
            default: False; example: selectdata=True
            If false, the following parameters are reset
            to default values.

      antenna     Select calibration data based on antenna
                  default: ''-->all; examples: 
                  antenna = '5,6'; antenna index 5 and 6 solutions
                  antenna = '05,06'; antenna names '05' and '06 solutions
                 
      timerange   Select time range to list
                  default: ''-->all; examples:
                  timerange='10:37:50.1'; list data for this sampling interval
                  timerange='<10:37:25'; list data before 10:37:25
      
      correlation Select polarization correlations to list
                  default: ''-->all; examples: 
                  correlation='RR LL'; list RR and LL correlations
                  correlation='XX XY'; list XX and XY correlations
      
      scan        Select scans to list
                  default: ''-->all; examples:
                  scan='2'; list scan 2
                  scan='>2'; list scan numbers greater than 2
      
      feed        (not yet implemented)
      
      array       (not yet implemented)

      observation Select by observation ID.
      
      uvrange     Select baseline lengths to list.
                  default: ''--> all; examples:
                  uvrange='<5klambda'; less than 5 kilo-wavelengths
                  Caution: Input units default to meters.
                  Listed units are always wavelengths.

average     (not yet implemented)

showflags   (not yet implemented)

pagerows    rows per page of listing
            default: 50; 0 --> do not paginate

listfile    write output to disk; will not overwrite
            default: '' --> write to screen
            listfile = 'solutions.txt'

async       Run asynchronously
            default = False; do not run asychronously

  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - 
   * - options
     - :code:`'ap'`
     - 
   * - datacolumn
     - :code:`'data'`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`'*'`
     - 
   * - selectdata
     - :code:`False`
     - 
   * - antenna
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - correlation
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - feed
     - :code:`''`
     - 
   * - array
     - :code:`''`
     - 
   * - observation
     - :code:`''`
     - 
   * - uvrange
     - :code:`''`
     - 
   * - average
     - :code:`''`
     - 
   * - showflags
     - :code:`False`
     - 
   * - pagerows
     - :code:`int(50)`
     - 
   * - listfile
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


options
---------------------------------------

:code:`'ap'`

List options: ap only 


datacolumn
---------------------------------------

:code:`'data'`

Column to list: data, float_data, corrected, model, residual


field
---------------------------------------

:code:`''`

Field names or index to be listed: \'\'==>all


spw
---------------------------------------

:code:`'*'`

Spectral window:channels: \'\*\'==>all, spw=\'1:5~57\'


selectdata
---------------------------------------

:code:`False`

Other data selection parameters


antenna
---------------------------------------

:code:`''`

Antenna/baselines: \'\'==>all, antenna = \'3\'


timerange
---------------------------------------

:code:`''`

Time range: \'\'==>all


correlation
---------------------------------------

:code:`''`

Correlations: \'\'==>all, correlation = \'RR RL\'


scan
---------------------------------------

:code:`''`

Scan numbers


feed
---------------------------------------

:code:`''`

Multi-feed numbers (Not yet implemented)


array
---------------------------------------

:code:`''`

Array numbers (Not yet implemented)


observation
---------------------------------------

:code:`''`

Select by observation ID(s)


uvrange
---------------------------------------

:code:`''`

uv range: \'\'==>all; not yet implemented 


average
---------------------------------------

:code:`''`

Averaging mode: ''==>none (Not yet implemented)


showflags
---------------------------------------

:code:`False`

Show flagged data (Not yet implemented)


pagerows
---------------------------------------

:code:`int(50)`

Rows per page


listfile
---------------------------------------

:code:`''`

Output file




