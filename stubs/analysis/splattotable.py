#
# stub function definition file for docstring parsing
#

def splattotable(filenames, table=''):
    r"""
Convert a downloaded Splatalogue spectral line list to a casa table.

Parameters
   - filenames_ (stringArray) - Files containing Splatalogue lists.
   - table_ (string='') - Output table name. Must be specified.


Description
   .. rubric:: Summary
      

   This task reads one or more spectral line lists downloaded from
   the `Splatalogue spectral line
   database <http://www.cv.nrao.edu/php/splat/>`__ and loads them
   into a CASA table. This tablecan then be queried via the slsearch
   task within CASA.

   The downloaded files must be in a specific format for this task to
   succeed. The columns are theimportant things; one can filter the
   results as one desires using Splatalogue, but the particular
   columns must be present as describedbelow. The columns which must
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

   In order to get these columns in this order, one shouldselect
   exactly the following items on the `Splatalogue "Advanced" search
   interface <https://www.cv.nrao.edu/php/splat/advanced.php>`__ .

   -  Under "Specify Ranges" one should select "GHz" for the
      frequency unit.
   -  Under "Line Strength Display" select exactly "CDMS/JPL
      Intensity","Sij mu2", and "Aij".
   -  Under "Energy Levels", one should select exactly "Elower (K)"
      and "Eupper (K)".
   -  Under "Miscellaneous", one shouldselect exactly "Display
      Ordered Frequency ONLY" and "Display NRAO Recommended
      Frequencies".

   One should then initiate the search and onthe resulting page, one
   should select the Tab Field Separator and then export the list.
   The resulting list should be in the properformat for importing
   into CASA.

   In order to assist the user in selecting the correct fields from
   the Splatalogue database in the proper format, the Splatalogue
   webpage has an option to "Export CASA Fields" after a search is
   conducted. By selecting this option, regardless of how the search
   was conducted on the webpage, the correct fields in the proper
   format will be exported for use by splattotable.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: filenames 
      

   Files containing Splatalogue spectral line lists.

   .. rubric:: table 
      

   Output table name. Must be specfied.


.. _filenames:

filenames (stringArray)
   | Files containing Splatalogue lists.
   | 
   |                      The downloaded files must be in a specific format
   |                      for this task to succeed. Fro details, see the splattotable
   |                      task pages on CASA Docs
   |                      (https://casa.nrao.edu/casadocs/)

.. _table:

table (string='')
   | Output table name. Must be specified.


    """
    pass
