

.. _Description:

Description
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
   
   *tablename*
   
   Input spectral line table name to search. If not specified, use
   the default table in the system.
   
   *outfile*
   
   Results table name. Blank means do not write the table to disk.
   
   *freqrange*
   
   Frequency range in GHz.
   
   *species*
   
   Species to search for.
   
   *reconly*
   
   List only NRAO recommended frequencies.
   
   *chemnames*
   
   Chemical names to search for.
   
   *qns*
   
   Resolved quantum numbers to search for.
   
   *intensity*
   
   CDMS/JPL intensity range. -1 -> do not use an intensity range.
   
   *smu2*
   
   Sμ 2 range in Debye 2. -1 -> do not use an Sμ 2 range.
   
   *loga*
   
   log(A) (Einstein A coefficient) range. -1 -> do not use a loga
   range.
   
   *el*
   
   Lower energy state range in Kelvin. -1 -> do not use an el range.
   
   *eu*
   
   Upper energy state range in Kelvin. -1 -> do not use an eu range.
   
   *rrlinclude*
   
   Include Radio Recombination Lines (RRLs) in the result set?
   
   *rrlonly*
   
   Include only RRLs in the result set?
   
   *verbose*
   
   List result set to logger (and optionally logfile)
   
   *logfile*
   
   List result set to this logfile (only used if verbose=True).
   
   *append*
   
   If True, append to logfile if it already exists, if False
   overwrite logfile it it exists. Only used if verbose=True and
   logfile not blank.
   

.. _Examples:

Examples
   To search the `Splatalogue
   database <http://www.cv.nrao.edu/php/splat/>`__ for spectral
   lines in the frequency range 90 - 92 GHz, and write the result to
   a table named "myspectrallines.tbl" as well as to the logger:
   
   ::
   
      slsearch(outfile="myspectrallines.tbl", freqrange=[90,92], verbose=True)
   

.. _Development:

Development
   No additional development details

