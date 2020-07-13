splattotable
============

.. container:: documentDescription description

   task description

.. container:: section
   :name: content-core

   .. container::
      :name: parent-fieldname-text

      .. rubric:: Summary
         :name: summary
         :class: p1

      This task reads one or more spectral line lists downloaded from
      the `Splatalogue spectral line
      database <http://www.cv.nrao.edu/php/splat/>`__ and loads them
      into a CASA table. This tablecan then be queried via the slsearch
      task within CASA.

      The downloaded files must be in a specific format for this task to
      succeed. The columns are the important things; one can filter the
      results as one desires using Splatalogue, but the particular
      columns must be present as described below. The columns which must
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

      In order to get these columns in this order, one should select
      exactly the following items on the `Splatalogue "Advanced" search
      interface <https://www.cv.nrao.edu/php/splat/advanced.php>`__ .

      -  Under "Specify Ranges" one should select "GHz" for the
         frequency unit. 
      -  Under "Line Strength Display" select exactly "CDMS/JPL
         Intensity", "Sij mu2", and "Aij".
      -  Under "Energy Levels", one should select exactly "Elower (K)"
         and "Eupper (K)".
      -  Under "Miscellaneous", one should select exactly "Display
         Ordered Frequency ONLY" and "Display NRAO Recommended
         Frequencies".

      One should then initiate the search and on the resulting page, one
      should select the Tab Field Separator and then export the list.
      The resulting list should be in the proper format for importing
      into CASA.

      In order to assist the user in selecting the correct fields from
      the Splatalogue database in the proper format, the Splatalogue
      webpage has an option to "Export CASA Fields" after a search is
      conducted.  By selecting this option, regardless of how the search
      was conducted on the webpage, the correct fields in the proper
      format will be exported for use by splattotable.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions
         :class: p1

      .. rubric:: filenames 
         :name: filenames
         :class: p1

      Files containing Splatalogue spectral line lists.

      .. rubric:: table 
         :name: table
         :class: p1

      Output table name. Must be specfied.

.. container:: section
   :name: viewlet-below-content-body

.. toctree::
   :hidden:
   :maxdepth: 3

   task_splattotable/parameters
   task_splattotable/changelog
   task_splattotable/examples
