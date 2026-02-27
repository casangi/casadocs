:orphan:

:py:mod:`casatablebrowser.browsetable`
=============================================

.. currentmodule:: casalith

.. autoapisummary::

   casatablebrowser.browsetable


.. py:function:: browsetable(tablename=None, cleanup=True)

   Brings up a browser that can open and display any CASA table (MS, calibration table, image)

   The ``tablename`` can be specified at
   startup, or any table can be loaded after the browser GUI comes up.
   It is possible to edit any table and its contents using the "Edit"
   tab on the top bar, but be careful with this, and make a backup
   copy of the table before editing!

   The tab "table keywords" on the left side of the table browser
   will allow you to look at sub-tables by left-clicking and then
   view the desired sub-table. Another useful feature is to make a 2D
   plot of the values in two table columns.

   Use the "Close Tables and Exit" option from the Files menu to quit
   the ``casabrowser``.

   A detailed description on how to use the table browser can be
   found in the Chapter pages on `"Browsing through MeasurementSets
   and Calibration
   Tables" <https://casadocs.readthedocs.io/en/stable/notebooks/data_examination.html#Browse-MS/Calibration-Tables>`__.

   :param tablename: Path to the table directory on disk (MS, cal. table, image)
                     default: none; example: tablename='ngc5921.ms'
   :type tablename: str

   .. rubric:: Examples

   To open the table browser and display the contents of table
   ``measurementset.ms``::

     browsetable(tablename='measurementset.ms')

   To get a plot of two table values, click on tools, then click on
   plot 2D.

   Example 1: to get a u-v plot, in the Plotter Option Gui::

     set Rows:  0   to  <Large Number>
     X Axis:  UVW      Slice  (set 0)
     Y Axis:  UVW      Slice  (set 1)
     click 'Clear and Plot' on right.

   Example 2: to get visibility plots::

     X Axis:  TIME
     Y Axis:  DATA     Slice Amplitude
     click 'Clear and Plot' on right.
