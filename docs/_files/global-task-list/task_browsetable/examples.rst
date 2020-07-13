Examples
========

.. container:: documentDescription description

   task browsetable examples

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      **Note:** a detailed description on how to use the table browser
      can be found in the Chapter pages on `"Browsing through
      MeasurementSets and Calibration
      Tables" <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-examination-and-editing/browse-a-table>`__

       

      To open the table browser and display the contents of table
      *measurementset.ms*:

      .. container:: casa-input-box

         browsetable(tablename='measurementset.ms')

       

      The following will open the table browser and displays only those
      data from *measurementset.ms* for which the column ANTENNA2 has a
      value below 6:

      .. container:: casa-input-box

         browsetable(tablename='measurementset.ms',taql='ANTENNA2 < 6')

       

      To get a plot of two table values, click on tools, then click on
      plot 2D.

      Example 1: to get a u-v plot, in the Plotter Option Gui,

      .. container::

                   set Rows:  0   to  <Large Number>
                   X Axis:  UVW      Slice  (set 0)
                   Y Axis:  UVW      Slice  (set 1)
                   click 'Clear and Plot' on right.
            

      Example 2: to get visibility plots (see Figure below)

      |           X Axis:  TIME
      |           Y Axis:  DATA     Slice Amplitude
      |           click 'Clear and Plot' on right.

      | 
      | |image1|

      ======= ============================
      Type    Figure 1
      ID      Create a short, unique name
      Caption 2D plot in the table browser
      ======= ============================

.. |image1| image:: 0ebdba26cba84528a4fa6ab8f42ae176d635c739.png
   :class: image-inline
   :width: 758px
   :height: 308px
