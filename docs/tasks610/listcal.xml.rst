listcal -- List antenna gain solutions -- information, calibration task
=======================================

Description
---------------------------------------


This task lists antenna gain solutions in tabular form.  The table
is organized as follows.  Solutions are output by
    1) Spectral window,
    2) Antenna,
    3) Time,
    4) Channel,
    5) and Polarization;
where the inner-most loop is over polarization.

The listcal output table contains two table headers.  The top-level header
is printed each time the spectral window changes.  This header lists
the spectral window ID (SpwID), the date of observation (Date),
the calibration table name (CalTable), and the measurement set name (MS name).

A lower-level header is printed when the the top-level header is printed,
when the antenna names change, and every `pagerows' of output.
The lower-level header columns are described here:

Column Name    Description
-----------    -----------
Ant            Antenna name (contains sub-columns: Amp, Phs, F)
Time           Visibility timestamp corresponding to gain solution
Field          Field name
Chn            Channel number
Amp            Complex solution amplitude
Phs            Complex solution  phase
F              Flag

Elements of the ``F'' column contain an `F' when the datum is flagged,
and ` ' (whitespace) when the datum is not flagged.

Presently, the polarization mode names (for example: R, L)
are not given, but the ordering of the polrization modes (left-to-right) is
equivalent to the order output by task listobs (see ``Feeds'' in listobs
output).

Input Parameters:

vis         Name of input visibility file
            default: none; example: vis='ngc5921.ms'

caltable    Name of input calibration table
            default: none; example: caltable='ngc5921.gcal'

field       Select data based on field ID(s) or name(s)
            default: ''==>all; example: field='1'
            field='0~2' field ids inclusive from 0 to 2
            field='3C*' all field names starting with 3C

antenna     Select calibration data based on antenna
            default: ''-->all; example: antenna='5'
            antenna='5,6' antenna index 5 and 6 solutions
            antenna='VA05','VA06'  VLA antenna 5 and 6

spw         Select spectral window, channel to list
            default: '' --> All spws and channels;
            spw='2:34' spectral window 2, channel 34
            will only list one spw, one channel at a time

listfile    write output to disk; will not overwrite
            default: '' --> write to screen

pagerows    rows per page of listing
            default: 50; 0 --> do not paginate

  


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
     - Name of input visibility file
   * - caltable
     - :code:`''`
     - Input calibration table to list
   * - field
     - :code:`''`
     - Field name or index
   * - antenna
     - :code:`''`
     - Antenna name or index
   * - spw
     - :code:`''`
     - Spectral window and channel
   * - listfile
     - :code:`''`
     - Disk file to write output
   * - pagerows
     - :code:`int(50)`
     - Rows per page


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


caltable
---------------------------------------

:code:`''`

Input calibration table to list


field
---------------------------------------

:code:`''`

Field name or index


antenna
---------------------------------------

:code:`''`

Antenna name or index


spw
---------------------------------------

:code:`''`

Spectral window and channel


listfile
---------------------------------------

:code:`''`

Disk file to write output


pagerows
---------------------------------------

:code:`int(50)`

Rows per page




