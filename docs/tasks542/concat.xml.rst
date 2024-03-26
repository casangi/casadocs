concat -- Concatenate several visibility data sets. -- utility, manipulation task
=======================================

Description
---------------------------------------

The list of data sets given in the vis argument are chronologically concatenated 
into an output data set in concatvis, i.e. the data sets in vis are first ordered
by the time of their earliest integration and then concatenated.  

If there are fields whose direction agrees within the direction tolerance
(parameter dirtol), the actual direction in the resulting, merged output field
will be the one from the chronologically first input MS.

If concatvis already exists (e.g., it is the same as the first input data set), 
then the other input data sets will be appended to the concatvis data set.  
There is no limit to the number of input data sets.

If none of the input data sets have any scratch columns (model and corrected
columns), none are created in the concatvis.  Otherwise these columns are
created on output and initialized to their default value (1 in model column,
data in corrected column) for those data with no input columns.

Spectral windows for each data set with the same chanelization, and within a
specified frequency tolerance of another data set will be combined into one
spectral window.

A field position in one data set that is within a specified direction tolerance
of another field position in any other data set will be combined into one
field.  The field names need not be the same---only their position is used.

Each appended dataset is assigned a new observation id (provided the entries
in the observation table are indeed different).

Keyword arguments:
vis -- Name of input visibility files to be combined
	default: none; example: vis = ['src2.ms','ngc5921.ms','ngc315.ms']
concatvis -- Name of visibility file that will contain the concatenated data
	note: if this file exits on disk then the input files are 
              added to this file.  Otherwise the new file contains  
	      the concatenated data.  Be careful here when concatenating to
              an existing file.
	default: none; example: concatvis='src2.ms'
	         example: concatvis='outvis.ms'

freqtol -- Frequency shift tolerance for considering data to be in the same
           spwid.  The number of channels must also be the same.
	default: '' == 1 Hz
	example: freqtol='10MHz' will not combine spwid unless they are
	   within 10 MHz.
        Note: This option is useful to combine spectral windows with very slight
           frequency differences caused by Doppler tracking, for example.

dirtol -- Direction shift tolerance for considering data as the same field
	default: '' == 1 mas (milliarcsec)
	example: dirtol='1arcsec' will not combine data for a field unless
	   their phase center differ by less than 1 arcsec.  If the field names
           are different in the input data sets, the name in the output data
           set will be the first relevant data set in the list.

respectname -- If true, fields with a different name are not merged even if their 
        direction agrees (within dirtol)
        default: False

timesort -- If true, the output visibility table will be sorted in time.
        default: false.  Data in order as read in.
	example: timesort=true
     Note: There is no constraint on data that is simultaneously observed for
        more than one field; for example multi-source correlation of VLBA data.

copypointing -- Make a proper copy of the POINTING subtable (can be time consuming).
        If False, the result is an empty POINTING table.
        default: True

visweightscale -- The weights of the individual MSs will be scaled in the concatenated
        output MS by the factors in this list. SIGMA will be scaled by 1/sqrt(factor).
        Useful for handling heterogeneous arrays.
	Use plotms to inspect the "Wt" column as a reference for determining the scaling 
	factors. See the cookbook for more details.
	example: [1.,3.,3.] - scale the weights of the second and third MS by a factor 3
                 and the SIGMA column of these MS by a factor 1/sqrt(3).
	default: [] (empty list) - no scaling

forcesingleephemfield -- By default, concat will only merge two ephemeris fields if
        the first ephemeris covers the time range of the second. Otherwise, two separate
        fields with separate ephemerides are placed in the output MS.
        In order to override this behaviour and make concat merge the non-overlapping 
        or only partially overlapping input ephemerides, the name or id of the field
        in question needs to be placed into the list in parameter 'forcesingleephemfield'.
        example: ['Neptune'] - will make sure that there is only one joint ephemeris for
                                       field Neptune in the output MS
        default: '' - standard treatment of all ephemeris fields




Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`numpy.array( [  ] )`
     - 
   * - concatvis
     - :code:`''`
     - 
   * - freqtol
     - :code:`''`
     - 
   * - dirtol
     - :code:`''`
     - 
   * - respectname
     - :code:`False`
     - 
   * - timesort
     - :code:`False`
     - 
   * - copypointing
     - :code:`True`
     - 
   * - visweightscale
     - :code:`numpy.array( [  ] )`
     - 
   * - forcesingleephemfield
     - :code:`''`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`numpy.array( [  ] )`

Name of input visibility files to be concatenated


concatvis
---------------------------------------

:code:`''`

Name of output visibility file


freqtol
---------------------------------------

:code:`''`

Frequency shift tolerance for considering data as the same spwid


dirtol
---------------------------------------

:code:`''`

Direction shift tolerance for considering data as the same field


respectname
---------------------------------------

:code:`False`

If true, fields with a different name are not merged even if their direction agrees


timesort
---------------------------------------

:code:`False`

If true, sort by TIME in ascending order


copypointing
---------------------------------------

:code:`True`

Copy all rows of the POINTING table.


visweightscale
---------------------------------------

:code:`numpy.array( [  ] )`

List of the weight scaling factors to be applied to the individual MSs


forcesingleephemfield
---------------------------------------

:code:`''`

make sure that there is only one joint ephemeris for every field in this list




