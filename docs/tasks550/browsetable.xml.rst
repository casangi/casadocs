browsetable -- Browse a table (MS, calibration table, image) -- utility task
=======================================

Description
---------------------------------------

This task brings up a browser that can open and display any CASA
table. The tablename can be specified at startup, or any table can be
loaded after the browser comes up.
  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - tablename
     - :code:`''`
     - Name of input table
   * - mightedit
     - :code:`False`
     - Warning: the GUI seems to ignore whether the table tool is opened read-only. Just be careful, esp. if filtering.
   * - sortlist
     - :code:`''`
     - Columns to sort by (ascending)
   * - taql
     - :code:`''`
     - TaQL query string for prefiltering the table.
   * - skipcols
     - :code:`''`
     - Columns to omit


Parameter Explanations
=======================================



tablename
---------------------------------------

:code:`''`

Name of table file (vis, calibration table, image)
                     Default: none
                     
                        Example: tablename='ngc5921.ms'



mightedit
---------------------------------------

:code:`False`

Disable the filtering options (below) and allow editing
the table.
                     Default: False
                     Options: False|True

                     Warning: the GUI seems to ignore whether the
		     table tool is opened read-only - just be careful,
		     esp. if filtering.



sortlist
---------------------------------------

:code:`''`

List of columns to sort by
                     Default: none



taql
---------------------------------------

:code:`''`

TaQL query string for prefiltering the table.
                     Default: none

                        Example: taql="ANTENNA2 < 6



skipcols
---------------------------------------

:code:`''`

Columns to NOT display.
                     Default: none

                        Example: skipcols='feed1, feed2'





