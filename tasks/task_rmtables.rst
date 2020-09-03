Description
   This task removes tables (MS, caltables, images) cleanly.

   rmtables is preferred over rm -rf for removing tables because it
   also gets rid of data that may linger in the cache. If you are
   within CASA, the system is keeping a cache of tables that you have
   been using, and using the rm -rf command may confuse things. For
   example, running a script that contains multiplerm commands will
   often not run(and instead crash) the second time as the cache
   gets confused. Also clean sometimes claims that files still exist
   after they have been removed from disk using rm -rf. Use rmtables
   instead. See the Chapter pages on `CASA
   Data <https://casa.nrao.edu/casadocs-devel/stable/casa-fundamentals/casa-data>`__ for
   more details.

   .. note:: NOTE: If you have multiple sessions running, bad thingscould
      happen if you remove a table being accessed by another process.
