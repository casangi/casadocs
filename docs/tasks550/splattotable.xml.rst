splattotable -- Convert a downloaded Splatalogue spectral line list to a casa table. -- analysis task
=======================================

Description
---------------------------------------

This task reads a spectral line list(s) downloaded from Splatalogue
(www.splatalogue.net) and loads it into a CASA table which can be
queried via eg the slsearch task.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - filenames
     - :code:`numpy.array( [  ] )`
     - Files containing Splatalogue lists.
   * - table
     - :code:`''`
     - Output table name. Must be specified.


Parameter Explanations
=======================================



filenames
---------------------------------------

:code:`numpy.array( [  ] )`

Files containing Splatalogue lists.

                     The downloaded files must be in a specific format
		     for this task to succeed. Fro details, see the splattotable
		     task pages on CASA Docs
		     (https://casa.nrao.edu/casadocs/)



table
---------------------------------------

:code:`''`

Output table name. Must be specified.




