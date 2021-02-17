

.. _Description:

Description
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
   Tables" <../../notebooks/data_examination.ipynb#Browse-MS/Calibration-Tables>`__.
   
   .. warning:: **Warning:** the inp/go functionality does not work for browsetable in CASA 6.
      Use the argument browstable(tablename='filename.ms') to invoke browsetable.

   .. rubric:: Parameters

   *tablename*

   Name of table file on disk. For example *filename.ms*,
   *caltable.tbl*, *imagefile.image*, etc.
   
   *mightedit*
   
   If the default False is changed to True, this disables the
   filtering options and allows editing the table.
   
   .. warning:: **WARNING**: The GUI appears to ignore whether the table tool
      is opened read-only - just be aware that you should not edit
      filtered tables unless you know what you are doing!
   
   *sortlist*

   List of columns to sort by.
   
   *taql*

   TaQL query string for prefiltering the table (see "Examples" tab
   at the top-right)
   
   For more information about the Table Query Language (TaQL) string, see [this note](https://casa.nrao.edu/aips2_docs/notes/199/199.html).
   
   *skipcols*

   Columns to NOT display. For example: *skipcols='feed1, feed2'

   .. figure:: _apimedia/e7b82ce6a699178fe6f43360bef6c38bb9c431bb.png

      CASA table browser with an MS loaded.


.. _Examples:

Examples
   **Note:** a detailed description on how to use the table browser
   can be found in the Chapter pages on `"Browsing through
   MeasurementSets and Calibration
   Tables" <../../notebooks/data_examination.ipynb#Browse-MS/Calibration-Tables>`__

   To open the table browser and display the contents of table
   *measurementset.ms*:
   
   ::
   
      browsetable(tablename='measurementset.ms')


   The following will open the table browser and displays only those
   data from *measurementset.ms* for which the column ANTENNA2 has a
   value below 6:
   
   ::
   
      browsetable(tablename='measurementset.ms',taql='ANTENNA2 < 6')
   

   To get a plot of two table values, click on tools, then click on
   plot 2D.
   
   Example 1: to get a u-v plot, in the Plotter Option Gui,
   
   |          set Rows:  0   to  <Large Number>
   |          X Axis:  UVW      Slice  (set 0)
   |          Y Axis:  UVW      Slice  (set 1)
   |          click 'Clear and Plot' on right.
      
   
   Example 2: to get visibility plots (see Figure below)
   
   |           X Axis:  TIME
   |           Y Axis:  DATA     Slice Amplitude
   |           click 'Clear and Plot' on right.
   

   .. figure:: _apimedia/0ebdba26cba84528a4fa6ab8f42ae176d635c739.png

      2D plot in the table browser


.. _Development:

Development
   No additional development details

