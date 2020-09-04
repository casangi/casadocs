#
# stub function definition file for docstring parsing
#

def slsearch(outfile='', freqrange=[84, 90], species=[''], reconly=False, chemnames=[''], qns=[''], intensity=[-1], smu2=[-1], loga=[-1], el=[-1], eu=[-1], rrlinclude=True, rrlonly=False, verbose=False, logfile='""', append=False):
    r"""
Search a spectral line table.

Parameters
   - **tablename** (string='') - Input spectral line table name to search. If not specified, use the default table in the system. [1]_
   - **outfile** (string='') - Results table name. Blank means do not write the table to disk. [2]_
   - **freqrange** (doubleArray=[84, 90]) - Frequency range in GHz. [3]_
   - **species** (stringArray=['']) - Species to search for. [4]_
   - **reconly** (bool=False) - List only NRAO recommended frequencies. [5]_
   - **chemnames** (stringArray=['']) - Chemical names to search for. [6]_
   - **qns** (stringArray=['']) - Resolved quantum numbers to search for. [7]_
   - **rrlinclude** (bool=True) - Include RRLs in the result set? [13]_
   - **rrlonly** (bool=False) - Include only RRLs in the result set? [14]_

      .. raw:: html

         <details><summary><i> rrlonly = False </i></summary>

      - **intensity** (doubleArray=[-1]) - CDMS/JPL intensity range. -1 -> do not use an intensity range. [8]_
      - **smu2** (doubleArray=[-1]) - Quantum mechanical line strength. -1 -> do not use a smu2 range. [9]_
      - **loga** (doubleArray=[-1]) - log(A) (Einstein coefficient) range. -1 -> do not use a loga range. [10]_
      - **eu** (doubleArray=[-1]) - Upper energy state range in Kelvin. -1 -> do not use an eu range. [12]_
      - **el** (doubleArray=[-1]) - Lower energy state range in Kelvin. -1 -> do not use an el range. [11]_

      .. raw:: html

         </details>
   - **verbose** (bool=False) - List result set to logger (and optionally logfile)? [15]_

      .. raw:: html

         <details><summary><i> verbose = True </i></summary>

      - **logfile** (string='""') - List result set to this logfile (only used if verbose=True). [16]_
      - **append** (bool=False) - If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank. [17]_

      .. raw:: html

         </details>


Description
   .. rubric:: Summary
      

   This task allows the user to search a specified spectral line
   table. If no spectral line table is specified, the default is to
   use a subset of the `Splatalogue spectral line
   catalog <http://www.cv.nrao.edu/php/splat/>`__ , which is
   distributed with CASA. One can also export custom catalogs from
   the Splatalogue website and import them to CASA using the task
   splattotable ,or tool method sl.splattotable. The results table
   can be written to disk by specifying its name in the outfile
   parameter.If outfile is not specified (i.e. outfile=''), no table
   is created.

   Because  `Splatalogue <http://www.cv.nrao.edu/php/splat/>`__  does
   not have values forthe CDMS/JPL intensity (intensity), quantum
   mechanical line strength (smu2), Einstein A coefficient (loga),
   the upper state energy level (eu), or the lower state energy level
   (el) measured in K for radio recombination lines (RRLs), one must
   specify to include RRLs in the specified frequency range in the
   output. In this case, RRLs will be included ignoring any filters
   on intensity, smu2, loga, eu, and el. One can also specify tolist
   only RRLs.

   One can specify to list the search results to the logger via the
   verbose parameter. If verbose=False, nologger output is listed.
   If verbose=True, one can also specify that the results be listed
   to a logfile. If this file alreadyexists, one can specify that
   the results be appended to it, or to overwrite it with the
   results.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: tablename
      

   Input spectral line table name to search. If not specified, use
   the default table in the system.

   .. rubric:: *outfile
      *
      

   Results table name. Blank means do not write the table to disk.

   .. rubric:: *freqrange*
      

   Frequency range in GHz.

   .. rubric:: *species
      *
      

   Species to search for.

   .. rubric:: *reconly
      *
      

   List only NRAO recommended frequencies.

   .. rubric:: *chemnames
      *
      

   Chemical names to search for.

   .. rubric:: *qns
      *
      

   Resolved quantum numbers to search for.

   .. rubric:: *intensity
      *
      

   CDMS/JPL intensity range. -1 -> do not use an intensity range.

   .. rubric:: smu2 
      

   Sμ 2 range in Debye 2. -1 -> do not use an Sμ 2 range.

   .. rubric:: loga 
      

   log(A) (Einstein A coefficient) range. -1 -> do not use a loga
   range.

   .. rubric:: el 
      

   Lower energy state range in Kelvin. -1 -> do not use an el range.

   .. rubric:: eu 
      

   Upper energy state range in Kelvin. -1 -> do not use an eu range.

   .. rubric:: rrlinclude 
      

   Include Radio Recombination Lines (RRLs) in the result set?

   .. rubric:: *rrlonly
      *
      

   Include only RRLs in the result set?

   .. rubric:: *verbose
      *
      

   List result set to logger (and optionally logfile)

   .. rubric:: *logfile
      *
      

   List result set to this logfile (only used if verbose=True).

   .. rubric:: append 
      

   If True, append to logfile if it already exists, if False
   overwrite logfile it it exists. Only used if verbose=True and
   logfile not blank.




Details
   Explanation of each parameter

.. [1] 
   **tablename** (string='')
      | Input spectral line table name to search. If not specified, use the default table in the system.
.. [2] 
   **outfile** (string='')
      | Results table name. Blank means do not write the table to disk.
.. [3] 
   **freqrange** (doubleArray=[84, 90])
      | Frequency range in GHz.
.. [4] 
   **species** (stringArray=[''])
      | Species to search for.
.. [5] 
   **reconly** (bool=False)
      | List only NRAO recommended frequencies.
.. [6] 
   **chemnames** (stringArray=[''])
      | Chemical names to search for.
.. [7] 
   **qns** (stringArray=[''])
      | Resolved quantum numbers to search for.
.. [8] 
   **intensity** (doubleArray=[-1])
      | CDMS/JPL intensity range. -1 -> do not use an intensity range.
.. [9] 
   **smu2** (doubleArray=[-1])
      | Quantum mechanical line strength. -1 -> do not use a smu2 range.
.. [10] 
   **loga** (doubleArray=[-1])
      | log(A) (Einstein coefficient) range. -1 -> do not use a loga range.
.. [11] 
   **el** (doubleArray=[-1])
      | Lower energy state range in Kelvin. -1 -> do not use an el range.
.. [12] 
   **eu** (doubleArray=[-1])
      | Upper energy state range in Kelvin. -1 -> do not use an eu range.
.. [13] 
   **rrlinclude** (bool=True)
      | Include RRLs in the result set?
.. [14] 
   **rrlonly** (bool=False)
      | Include only RRLs in the result set?
.. [15] 
   **verbose** (bool=False)
      | List result set to logger (and optionally logfile)?
.. [16] 
   **logfile** (string='""')
      | List result set to this logfile (only used if verbose=True).
.. [17] 
   **append** (bool=False)
      | If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.

    """
    pass
