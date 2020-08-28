#
# stub function definition file for docstring parsing
#

def slsearch(tablename='', outfile='', freqrange=[84, 90], species=[''], reconly=False, chemnames=[''], qns=[''], intensity=[-1], smu2=[-1], loga=[-1], el=[-1], eu=[-1], rrlinclude=True, rrlonly=False, verbose=False, logfile='""', append=False):
    r"""
Search a spectral line table.

Parameters
   - **tablename** (string) - Input spectral line table name to search. If not specified, use the default table in the system.
   - **outfile** (string) - Results table name. Blank means do not write the table to disk.
   - **freqrange** (doubleArray) - Frequency range in GHz.
   - **species** (stringArray) - Species to search for.
   - **reconly** (bool) - List only NRAO recommended frequencies.
   - **chemnames** (stringArray) - Chemical names to search for.
   - **qns** (stringArray) - Resolved quantum numbers to search for.
   - **rrlinclude** (bool) - Include RRLs in the result set?
   - **rrlonly** (bool) - Include only RRLs in the result set?
   - **verbose** (bool) - List result set to logger (and optionally logfile)?

Subparameters
   *verbose = True*

   - **logfile** (string="") - List result set to this logfile (only used if verbose=True).
   - **append** (bool=True) - If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.

   *rrlonly = False*

   - **intensity** (doubleArray=-1) - CDMS/JPL intensity range. -1 -> do not use an intensity range.
   - **smu2** (doubleArray=-1) - Quantum mechanical line strength. -1 -> do not use a smu2 range.
   - **loga** (doubleArray=-1) - log(A) (Einstein coefficient) range. -1 -> do not use a loga range.
   - **eu** (doubleArray=-1) - Upper energy state range in Kelvin. -1 -> do not use an eu range.
   - **el** (doubleArray=-1) - Lower energy state range in Kelvin. -1 -> do not use an el range.


Description
      .. rubric:: Summary
         :name: summary

      This task allows the user to search a specified spectral line
      table. If no spectral line table is specified, the default is to
      use a subset of the `Splatalogue spectral line
      catalog <http://www.cv.nrao.edu/php/splat/>`__ , which is
      distributed with CASA. One can also export custom catalogs from
      the Splatalogue website and import them to CASA using the task
      splattotable ,or tool method sl.splattotable. The results table
      can be written to disk by specifying its name in the outfile
      parameter. If outfile is not specified (i.e. outfile=''), no table
      is created.

      Because  `Splatalogue <http://www.cv.nrao.edu/php/splat/>`__  does
      not have values forthe CDMS/JPL intensity (intensity), quantum
      mechanical line strength (smu2), Einstein A coefficient (loga),
      the upper state energy level (eu), or the lower state energy level
      (el) measured in K for radio recombination lines (RRLs), one must
      specify to include RRLs in the specified frequency range in the
      output. In this case, RRLs will be included ignoring any filters
      on intensity, smu2, loga, eu, and el. One can also specify to list
      only RRLs.

      One can specify to list the search results to the logger via the
      verbose parameter. If verbose=False, no logger output is listed.
      If verbose=True, one can also specify that the results be listed
      to a logfile. If this file already exists, one can specify that
      the results be appended to it, or to overwrite it with the
      results.

       

      .. rubric:: Parameter descriptions
         :name: parameter-descriptions

      .. rubric:: tablename
         :name: tablename
         :class: p1

      Input spectral line table name to search. If not specified, use
      the default table in the system.

      .. rubric:: *outfile
         *
         :name: outfile
         :class: p1

      Results table name. Blank means do not write the table to disk.

      .. rubric:: *freqrange*
         :name: freqrange
         :class: p1

      Frequency range in GHz.

      .. rubric:: *species
         *
         :name: species
         :class: p1

      Species to search for.

      .. rubric:: *reconly
         *
         :name: reconly
         :class: p1

      List only NRAO recommended frequencies.

      .. rubric:: *chemnames
         *
         :name: chemnames
         :class: p1

      Chemical names to search for.

      .. rubric:: *qns
         *
         :name: qns
         :class: p1

      Resolved quantum numbers to search for.

      .. rubric:: *intensity
         *
         :name: intensity
         :class: p1

      CDMS/JPL intensity range. -1 -> do not use an intensity range.

      .. rubric:: smu2 
         :name: smu2
         :class: p1

      Sμ 2 range in Debye 2. -1 -> do not use an Sμ 2 range.

      .. rubric:: loga 
         :name: loga
         :class: p1

      log(A) (Einstein A coefficient) range. -1 -> do not use a loga
      range.

      .. rubric:: el 
         :name: el
         :class: p1

      Lower energy state range in Kelvin. -1 -> do not use an el range.

      .. rubric:: eu 
         :name: eu
         :class: p1

      Upper energy state range in Kelvin. -1 -> do not use an eu range.

      .. rubric:: rrlinclude 
         :name: rrlinclude
         :class: p1

      Include Radio Recombination Lines (RRLs) in the result set?

      .. rubric:: *rrlonly
         *
         :name: rrlonly
         :class: p1

      Include only RRLs in the result set?

      .. rubric:: *verbose
         *
         :name: verbose
         :class: p1

      List result set to logger (and optionally logfile)

      .. rubric:: *logfile
         *
         :name: logfile
         :class: p1

      List result set to this logfile (only used if verbose=True).

      .. rubric:: append 
         :name: append
         :class: p1

      If True, append to logfile if it already exists, if False
      overwrite logfile it it exists. Only used if verbose=True and
      logfile not blank.

    """
    pass
