.. contents::
   :depth: 3
..

.. container::
   :name: viewlet-above-content-title

Browse MS/Calibration Tables
============================

.. container::
   :name: viewlet-below-content-title

.. container:: documentDescription description

   Browse a table (MeasurementSet, calibration table, image)

.. container:: section
   :name: viewlet-above-content-body

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      The browsetable task is available for viewing data directly.  It
      handles all CASA tables, including MeasurementSets, calibration
      tables, and images. This task brings up a CASA Qt table browser,
      which can be launched from outside CASA using **casabrowser**.

      browsetable is not required for normal data reduction but is
      useful for troubleshooting or for identifying table column names
      and formats. If you want to edit a long column or extract data for
      manipulation outside CASA (e.g. the uv data), see flagdata and the
      table tools in the `Global Tool
      List <https://casa.nrao.edu/casadocs-devel/stable/global-tool-list>`__. 
      The MeasurementSet columns and subtables are described
      `here <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/measurement-set>`__.

      The default inputs for the CASA browsetable task are:

      .. container:: casa-input-box

         #In CASA
         #   browsetable :: Browse a table (MS, calibration table,
         image)
         tablename = ''             # Name of input table

      Once the tablename is specified, available parameters include:

      .. container:: casa-input-box

         #   browsetable :: Browse a table (MS, calibration table,
         image)
         tablename      =   'ngc5921_ut.ms' #  Name of input table
         mightedit      =      False        #  Warning: the GUI seems to
         ignore whether the table
                                            #   tool is opened read-only
         - just be careful, esp.
                                            #   if filtering.
         sortlist       =         ''        #  Columns to sort by
         (ascending)
         taql           =         ''        #  TaQL query string for
         prefiltering the table.
         skipcols       =         ''        #  Columns to omit

      For more information about the Table Query Language (TaQL) string,
      see `this
      note <https://casa.nrao.edu/aips2_docs/notes/199/199.html>`__.

      Example with *tablename* argument:

      .. container:: casa-input-box

         browsetable('ngc5921_ut.ms')

      For an MS, as in this example, the table browser will display the
      MAIN table (Figure 1). To look at subtables, use the *table
      keywords* tab along the left side to bring up a panel with the
      subtables listed (Figure 2), then choose (double-click) a table
      name (Keyword) to display the subtable in a new tab (Figures 3 and
      4). You can double-click on a cell in a table to view the contents
      (fourth figure below) then use the "Close" or "Close All" buttons
      at the bottom of the contents display to close one or all
      displayed values.

         .. container:: center

            --------------

         .. container:: center

         .. container:: center

            +---------+-----------------------------------------------------------+
            | Type    | Figure 1                                                  |
            +---------+-----------------------------------------------------------+
            | ID      | examination-fig-browser1                                  |
            +---------+-----------------------------------------------------------+
            | Caption | The browser displays the MAIN table within a frame. You   |
            |         | can scroll through the data with the sliders at right and |
            |         | bottom, and step through the pages with the "<<" and ">>" |
            |         | buttons or using "First" and "Last" to quickly advance to |
            |         | the beginning or end.  To go to a specific page, input    |
            |         | the page number in the text box then click "Go".  By      |
            |         | default, 1000 rows of the table are loaded at a time, but |
            |         | you can specify this setting in the "Loading ... rows"    |
            |         | text box.                                                 |
            +---------+-----------------------------------------------------------+

         .. container:: center

             

         .. container:: center

            .. container:: caption

                

      ..

         +---------+-----------------------------------------------------------+
         | Type    | Figure 2                                                  |
         +---------+-----------------------------------------------------------+
         | ID      | examination-fig-browser-subtables                         |
         +---------+-----------------------------------------------------------+
         | Caption | Use the "table keywords" tab to look at other tables      |
         |         | within an MS. Double-click on a table name to view its    |
         |         | contents in a new tab, as shown in the following figures. |
         +---------+-----------------------------------------------------------+

         .. container:: caption

            |image1| 

      ..

         ======= ======================================
         Type    Figure 3
         ID      examination-fig-browser-antenna
         Caption Viewing the *ANTENNA* table of the MS.
         ======= ======================================

         .. container::

             |image2|

            +---------+-----------------------------------------------------------+
            | Type    | Figure 4                                                  |
            +---------+-----------------------------------------------------------+
            | ID      | examination-fig-browser-polarization                      |
            +---------+-----------------------------------------------------------+
            | Caption | The *POLARIZATION* table shows the number and types of    |
            |         | correlations.  The *CORR_TYPE* integer array indicates    |
            |         | the Stokes type as defined in the Stokes class            |
            |         | enumeration.  Common types include RR (5), RL (6), LR     |
            |         | (7), and LL (8) for circular polarization, and XX (9), XY |
            |         | (10), YX (11), and YY (12) for linear polarization.       |
            +---------+-----------------------------------------------------------+

            |image3|

            +---------+-----------------------------------------------------------+
            | Type    | Figure 5                                                  |
            +---------+-----------------------------------------------------------+
            | ID      | examination-fig-browser-contents                          |
            +---------+-----------------------------------------------------------+
            | Caption | Double-click a cell in the table or sub-table to see its  |
            |         | value displayed to the right.  Here, the *DATA* column    |
            |         | cell (top right) contains a [2,63] array of complex       |
            |         | numbers.  The *WEIGHT_SPECTRUM* for this data is shown    |
            |         | below it as a [2,63] array of float values.  Use the      |
            |         | sliders to see other values in the arrays, and click      |
            |         | "Close" to close the cell contents display or "Close All" |
            |         | to close all contents displays.                           |
            +---------+-----------------------------------------------------------+

      Many options are available on the browsetable toolbar and menus:

      -  To open a table, click the "Open Table" button or use the
         **File > Open Table** menu to open a file browser dialog box.
      -  To close a table, click the "Close Table" button to close the
         table in the active tab, or use the options on the "File" menu
         to close the table in the active tab ("Close Table"), to select
         an open table to close ("Close..."), or to close all tables
         ("Close All").  You can also "Close All and Exit" the table
         browser.
      -  To edit the table and its contents, click the "Edit Table"
         button or use the **Edit > Edit Table** menu.  You can also use
         the "Edit\ **"** menu to add a row to the table.  Be careful
         with this, and make a backup copy of the table before editing!
      -  To view table information, click the "Table Information" (blue
         **"i"** button) or use the **View** **> Table Information**
         menu.  You can also hover the mouse pointer over the table name
         tab to get a popup with information.
      -  To set a TaQL filter, click the "Filter on Fields" button or
         use the **View > Filter on Fields** menu.  This will open a
         "Filter Rules" dialog box within the table browser in which to
         set the filter.  Another option is to use the *taql* parameter
         in the browsetable() call.
      -  To choose which columns to display, use **View > Columns** to
         select the columns from a list, which you can select
         individually or toggle with "Show All Columns" or "Hide All
         Columns".  Another option is to use the *skipcols* parameter in
         the browsetable() call.
      -  To format the contents of the column cells, use **View > Format
         Display** to select a column then choose its formatting
         (depending on its type).  For example, for numerical values you
         can set the precision and choose to use scientific format, or
         set the font and color for negative and nonnegative values.
      -  To find data using filter rules, click the "Find" button or use
         **Tools > Find** to open a Search Rules dialog box.
      -  To sort the table, click the "Sort" button, use the **Tools >
         Sort** menu to open a Table Sorter dialog box in which you can
         select the sort columns,or just click on the column name. 
         Another option is to use the *sortlist* parameter in the
         browsetable() call.
      -  To plot table data, click the "Plot 2D" button or use the
         **Tools > Plot 2D** menu to open a Plot Options dialog box
         where you can select the rows and axes to plot, along with plot
         display options.  Click  "Overplot" or "Clear and Plot" to make
         the plot in the Table Browser Plotter window.  There is also an
         option to export the plot; select PNG or JPG format and click
         Go.
      -  Currently, **Export > VOTable** results in a Fatal IO Error and
         kills the table browser.
      -  The default display is 1000 rows, but this can be set in the
         input box at the lower right.  To page through the table, use
         the PAGE NAVIGATION buttons to advance forward or backward one
         page, or go directly to the First or Last page.  You can also
         enter a page number and click Go.
      -  To exit the table browser, use **File > Exit** or click the
         Close "X" button at the upper right of the window.

      .. container:: alert-box

         **Alert:** You are likely to find that browsetable needs to get
         a table lock before proceeding. Use the **clearstat** command
         to clear the lock status in this case.  You may also be unable
         to use other tasks on the table while it is open in the table
         browser.

       

.. container:: section
   :name: viewlet-below-content-body

.. |image1| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/antenna.jpeg/@@images/f142682c-8820-42ea-8954-574d3e65344b.jpeg
   :class: image-inline
.. |image2| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/poln.jpeg/@@images/ea9af86f-b863-429f-b705-e98c517e17d9.jpeg
   :class: image-inline
.. |image3| image:: https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/data-1.jpeg/@@images/a1ab0a4a-4387-49c4-864d-939ad38ca1ac.jpeg
   :class: image-inline
