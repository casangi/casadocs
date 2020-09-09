#
# stub function definition file for docstring parsing
#

def browsetable(tablename='', mightedit=False, sortlist='', taql='', skipcols=''):
    r"""
Browse a table (MS, calibration table, image)

Parameters
   - tablename_ (string='') - Name of input table

      .. raw:: html

         <details><summary><i> tablename != '' </i></summary>

      - mightedit_ (bool=False) - Warning: the GUI seems to ignore whether the table tool is opened read-only. Just be careful, esp. if filtering.
      - sortlist_ ({string, stringArray}='') - Columns to sort by (ascending)
      - taql_ (string='') - TaQL query string for prefiltering the table.
      - skipcols_ ({string, stringArray}='') - Columns to omit

      .. raw:: html

         </details>


Description
   Brings up a browser that can open and display any CASA table (MS,
   calibration table, image). The *tablename* can be specified at
   startup, or any table can be loaded after the browser comes up.It
   is possible to edit any table and its contents using the "Edit"
   tab on the top bar, but be careful with this, and make a backup
   copy of the table before editing!

   The tab "table keywords" on the left side of the table browser
   will allow you to look at sub-tables by left-clicking and then
   view the desired sub-table. Another useful feature is to make a 2D
   plot of the values in two table columns.

   Use the "Close Tables and Exit" option from the Files menu to quit
   the **casabrowser**.

   A detailed description on how to use the table browser can be
   found in the Chapter pages on `"Browsing through MeasurementSets
   and Calibration
   Tables" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/browse-a-table>`__.
  
   |image1|

   ======= =====================================
   Type    Figure 1
   ID      CASA table brower
   Caption CASA table browser with an MS loaded.
   ======= =====================================

.. |image1| image:: ../media/e7b82ce6a699178fe6f43360bef6c38bb9c431bb.png


.. _tablename:

tablename (string='')
   | Name of table file (vis, calibration table, image)
   |                      Default: none
   |                      
   |                         Example: tablename='ngc5921.ms'

.. _mightedit:

mightedit (bool=False)
   | Disable the filtering options (below) and allow editing
   | the table.
   |                      Default: False
   |                      Options: False|True
   | 
   |                      Warning: the GUI seems to ignore whether the
   |                      table tool is opened read-only - just be careful,
   |                      esp. if filtering.

.. _sortlist:

sortlist ({string, stringArray}='')
   | List of columns to sort by
   |                      Default: none

.. _taql:

taql (string='')
   | TaQL query string for prefiltering the table.
   |                      Default: none
   | 
   |                         Example: taql="ANTENNA2 < 6

.. _skipcols:

skipcols ({string, stringArray}='')
   | Columns to NOT display.
   |                      Default: none
   | 
   |                         Example: skipcols='feed1, feed2'


    """
    pass
