

.. _Description:

Description
   This task reads one or more spectral line lists downloaded from
   the `Splatalogue spectral line
   database <http://www.cv.nrao.edu/php/splat/>`__ and loads them
   into a CASA table. This tablecan then be queried via the slsearch
   task within CASA.
   
   The downloaded files must be in a specific format for this task to
   succeed. The columns are the important things; one can filter the
   results as one desires using Splatalogue, but the particular
   columns must be present as described below. The columns which must
   be present in the downloaded file in exactly the following order
   are:
   
   -  "Species"
   -  "NRAO Recommended"
   -  "Chemical Name"
   -  "Freq in GHz"
   -  "Resolved QNs"
   -  "CDMS/JPL Intensity"
   -  "Sijmu2 (D2)"
   -  "Log10 (Aij)"
   -  "EL (K)
   -  "EU (K)"
   -  "Linelist"
   
   In order to get these columns in this order, one should select
   exactly the following items on the `Splatalogue "Advanced" search
   interface <https://www.cv.nrao.edu/php/splat/advanced.php>`__ .
   
   -  Under "Specify Ranges" one should select "GHz" for the
      frequency unit. 
   -  Under "Line Strength Display" select exactly "CDMS/JPL
      Intensity", "Sij mu2", and "Aij".
   -  Under "Energy Levels", one should select exactly "Elower (K)"
      and "Eupper (K)".
   -  Under "Miscellaneous", one should select exactly "Display
      Ordered Frequency ONLY" and "Display NRAO Recommended
      Frequencies".
   
   One should then initiate the search and on the resulting page, one
   should select the Tab Field Separator and then export the list.
   The resulting list should be in the proper format for importing
   into CASA.
   
   In order to assist the user in selecting the correct fields from
   the Splatalogue database in the proper format, the Splatalogue
   webpage has an option to "Export CASA Fields" after a search is
   conducted.  By selecting this option, regardless of how the search
   was conducted on the webpage, the correct fields in the proper
   format will be exported for use by splattotable.

   
   .. rubric:: Parameter descriptions
   
   *filenames*
   
   Files containing Splatalogue spectral line lists.
   
   *table*
   
   Output table name. Must be specfied.
   

.. _Examples:

Examples
   To write two spectral line lists, 'mysplatlist1.txt' and
   'mysplatlist2.txt', into a single spectral line table
   'mynewsl.tbl':
   
   ::
   
      splattotable(filenames=['mysplatlist1.txt',mysplatlist2.txt'],
                   table='mynewsl.tbl')
   

.. _Development:

Development
   No additional development details

