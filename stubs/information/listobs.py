#
# stub function definition file for docstring parsing
#

def listobs(vis, selectdata=True, spw='', field='', antenna='', uvrange='', timerange='', correlation='', scan='', intent='', feed='', array='', observation='', verbose=True, listfile='', listunfl=False, cachesize=50, overwrite=False):
    r"""
List the summary of a data set in the logger or in a file

Parameters
   - vis_ (string) - Name of input visibility file (MS)
   - selectdata_ (bool=True) - Data selection parameters

      .. raw:: html

         <details><summary><i> selectdata = True </i></summary>

      - field_ ({string, stringArray}='') - Selection based on field names or field index numbers. Default is all.
      - spw_ ({string, stringArray}='') - Selection based on spectral-window/frequency/channel.
      - antenna_ ({string, stringArray}='') - Selection based on antenna/baselines. Default is all.
      - timerange_ ({string, stringArray}='') - Selection based on time range. Default is entire range.
      - correlation_ ({string, stringArray}='') - Selection based on correlation. Default is all.
      - scan_ ({string, stringArray}='') - Selection based on scan numbers. Default is all.
      - intent_ ({string, stringArray}='') - Selection based on observation intent. Default is all.
      - feed_ ({string, stringArray}='') - Selection based on multi-feed numbers: Not yet implemented
      - array_ ({string, stringArray}='') - Selection based on (sub)array numbers. Default is all.
      - uvrange_ ({string, stringArray}='') - Selection based on uv range. Default: entire range. Default units: meters.
      - observation_ ({string, int}='') - Selection based on observation ID. Default is all.

      .. raw:: html

         </details>
   - verbose_ (bool=True) - Controls level of information detail reported. True reports more than False.
   - listfile_ (string='') - Name of disk file to write output. Default is none (output is written to logger only).

      .. raw:: html

         <details><summary><i> listfile != '' </i></summary>

      - overwrite_ (bool=False) - If True, tacitly overwrite listfile if it exists.

      .. raw:: html

         </details>
   - listunfl_ (bool=False) - List unflagged row counts? If true, it can have significant negative performance impact.
   - cachesize_ (double=50) - EXPERIMENTAL. Maximum size in megabytes of cache in which data structures can be held.


Description
   This application reports various metadata related to an MS. The
   listing is sent to the logger or can be saved to a file. Standard
   MS selection parameters can be used to limit the listing (see
   `Visibility Data
   Selections <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-selection-in-a-measurementset>`__
   for details).

   The report begins with information such as the observer, the
   project ID, the number of records, the length of the observation,
   and minimum and maxiumum timestamp of the records included.
   Following this are several tables summarizing metadata. There is a
   table which summarizes scan data (only if verbose = True), a table
   that summarizes field data, a table that summarizes spectral
   window data, a table that summarizes source data (only if verbose
   = True), and a table that summarizes antenna data. If verbose =
   False, the antenna summary will only list antenna and station
   names. If verbose = True, additional information such as the
   diameter, latitude and longitude, position relative to the array
   center, and the ITRF geocentric coordinates for each antenna will
   be listed.

   Should the MS have multiple array IDs and/or multiple observation
   IDs, the report will list all of these tables for each array
   ID/observation ID pair.

   Note: The 'Average Interval (s)' column in the scan table is the
   average of the MS's *INTERVAL* column for each scan.

   

   .. rubric:: Description of algorithm to calculate the number of
      unflagged rows
      

   The number of unflagged rows is only computed and reported in the
   scan and field table if *listunfl=True*. Computing these
   quantities can have a negative performance impact, especially for
   large datasets. The number of unflagged rows (the *nUnflRows*
   columns in the scans and fields portions of the listing) is
   calculated by summing the fractional unflagged bandwidth for each
   row (and hence why the number of unflagged rows, in general, is
   not an integer). Thus a row which has half of its total bandwidth
   flagged contributes 0.5 rows to the unflagged row count. A row
   with 20 of 32 channels of homogeneous width contributes 20/32 =
   0.625 rows to the unflagged row count. A row with a value of False
   in the *FLAG_ROW* column is not counted in the number of unflagged
   rows.


.. _vis:

vis (string)
   | Name of input visibility file (MS)

.. _selectdata:

selectdata (bool=True)
   | Data selection parameters

.. _spw:

spw ({string, stringArray}='')
   | Selection based on spectral-window/frequency/channel.

.. _field:

field ({string, stringArray}='')
   | Selection based on field names or field index numbers. Default is all.

.. _antenna:

antenna ({string, stringArray}='')
   | Selection based on antenna/baselines. Default is all.

.. _uvrange:

uvrange ({string, stringArray}='')
   | Selection based on uv range. Default: entire range. Default units: meters.

.. _timerange:

timerange ({string, stringArray}='')
   | Selection based on time range. Default is entire range.

.. _correlation:

correlation ({string, stringArray}='')
   | Selection based on correlation. Default is all.

.. _scan:

scan ({string, stringArray}='')
   | Selection based on scan numbers. Default is all.

.. _intent:

intent ({string, stringArray}='')
   | Selection based on observation intent. Default is all.

.. _feed:

feed ({string, stringArray}='')
   | Selection based on multi-feed numbers: Not yet implemented

.. _array:

array ({string, stringArray}='')
   | Selection based on (sub)array numbers. Default is all.

.. _observation:

observation ({string, int}='')
   | Selection based on observation ID. Default is all.

.. _verbose:

verbose (bool=True)
   | Controls level of information detail reported. True reports more than False.

.. _listfile:

listfile (string='')
   | Name of disk file to write output. Default is none (output is written to logger only).

.. _listunfl:

listunfl (bool=False)
   | List unflagged row counts? If true, it can have significant negative performance impact.

.. _cachesize:

cachesize (double=50)
   | EXPERIMENTAL. Maximum size in megabytes of cache in which data structures can be held.

.. _overwrite:

overwrite (bool=False)
   | If True, tacitly overwrite listfile if it exists.


    """
    pass
