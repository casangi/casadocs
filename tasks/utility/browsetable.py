#
# stub function definition file for docstring parsing
#

def browsetable(tablename='', mightedit=False, sortlist='', taql='', skipcols=''):
    """
Browse a table (MS, calibration table, image)

| This task brings up a browser that can open and display any CASA
|table. The tablename can be specified at startup, or any table can be
|loaded after the browser comes up.

Parameters
----------
tablename : string
   Name of input table

Other Parameters
----------
mightedit : bool
   Warning: the GUI seems to ignore whether the table tool is opened read-only. Just be careful, esp. if filtering.
sortlist : string, stringArray
   Columns to sort by (ascending)
taql : string
   TaQL query string for prefiltering the table.
skipcols : string, stringArray
   Columns to omit

Notes
-----





   browse a table (MS, calibration table, image)



      Brings up a browser that can open and display any CASA table (MS,
      calibration table, image). The *tablename* can be specified at
      startup, or any table can be loaded after the browser comes up. It
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

       

      .. rubric:: Parameters
         :name: parameters

      .. rubric:: *tablename*
         :name: tablename

      Name of table file on disk. For example *filename.ms*,
      *caltable.tbl*, *imagefile.image*, etc.

      .. rubric:: *mightedit*
         :name: mightedit

      If the default False is changed to True, this disables the
      filtering options and allows editing the table.

      .. note:: **WARNING**: The GUI appears to ignore whether the table tool
         is opened read-only - just be aware that you should not edit
         filtered tables unless you know what you are doing!

      .. rubric:: *sortlist* 
         :name: sortlist

      List of columns to sort by.

      .. rubric:: *taql*     
         :name: taql

      TaQL query string for prefiltering the table (see "Examples" tab
      at the top-right)

      .. rubric:: *skipcols*
         :name: skipcols

      Columns to NOT display. For example: *skipcols='feed1, feed2' *   

      |             
      |     
      |  |image1|

      ======= =====================================
      Type    Figure 1
      ID      CASA table brower
      Caption CASA table browser with an MS loaded.
      ======= =====================================

.. |image1| image:: ../../_media/e7b82ce6a699178fe6f43360bef6c38bb9c431bb.png
   :class: image-inline

    """
    pass
