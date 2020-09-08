#
# stub function definition file for docstring parsing
#

def listcal(vis, caltable, field='', antenna='', spw='', listfile='', pagerows=50):
    r"""
List antenna gain solutions

Parameters
   - vis_ (string) - Name of input visibility file
   - caltable_ (string) - Input calibration table to list
   - field_ (string='') - Field name or index
   - antenna_ (string='') - Antenna name or index
   - spw_ (string='') - Spectral window and channel
   - listfile_ (string='') - Disk file to write output
   - pagerows_ (int=50) - Rows per page


Description
   This task lists antenna gain solutions in tabular form. The table
   is organized as follows. Solutions are output by

   #. Spectral window
   #. Antenna
   #. Time
   #. Channel
   #. and Polarization

   where the inner-most loop is over polarization.

   | The **listcal** output table contains two table headers. The
     top-level header is printed each time the spectral window
     changes. This header lists
   | the spectral window ID (SpwID), the date of observation (Date),
     the calibration table name (CalTable), and the measurement set
     name (MS name).

   A lower-level header is printed when the top-level header is
   printed, when the antenna names change, and for every *pagerows*
   of output. The lower-level header columns are described here:

   =========== ===================================================
   Column name Description
   Ant         Antenna name (contains sub-columns: Amp, Phs, F)
   Time        Visibility timestamp corresponding to gain solution
   Field       Field name
   Chn         Channel number
   Amp         Complex solution amplitude
   Phs         Complex solution phase
   F           Flag
   =========== ===================================================

   Elements of the "F" column contain an 'F' when the datum is
   flagged, and '' (whitespace) when the datum is not flagged.
   Presently, the polarization mode names (for example: R, L) are not
   given, but the ordering of the polarization modes (left-to-right)
   is equivalent to the order output by task **listobs** (see "Feeds"
   in **listobs** output).

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input visibility file. Default: none. Examples:
   *vis='ngc5921.ms'*

   .. rubric:: *caltable*
      

   Name of input calibration table. Default: none. Examples:
   *caltable='ngc5921.gcal'*

   .. rubric:: *field*
      

   Select data based on field ID(s) or name(s). Default: '' => all.
   Examples: *field='1'*; *field='0~2'* field IDs inclusive from 0 to
   2; *field='3C*'* all field names starting with 3C

   .. rubric:: *antenna*
      

   Select calibration data based on antenna. Default: '' => all.
   Examples: *antenna='5'*; *antenna='5,6'* antenna index 5 and 6
   solutions; *antenna='VA05','VA06'* VLA antenna 5 and 6

   .. rubric:: *spw*
      

   Select spectral window, channel to list. Default: '' => all spws
   and channels. Examples: *spw='2:34'* spectral window 2, channel 34
   (will only list one spw, one channel at a time)

   .. rubric:: *listfile*
      

   Write output to disk (will not overwrite). Default: '' => write to
   screen

   .. rubric:: *pagerows*
      

   Rows per page of listing. Default: 50; *pagerows=0* => do not
   paginate




Details
   Explanation of each parameter

.. _vis:

   .. rubric:: vis

   | Name of input visibility file

.. _caltable:

   .. rubric:: caltable

   | Input calibration table to list

.. _field:

   .. rubric:: field

   | Field name or index

.. _antenna:

   .. rubric:: antenna

   | Antenna name or index

.. _spw:

   .. rubric:: spw

   | Spectral window and channel

.. _listfile:

   .. rubric:: listfile

   | Disk file to write output

.. _pagerows:

   .. rubric:: pagerows

   | Rows per page


    """
    pass
