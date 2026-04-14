.. _Description:

Description
   Task for ALMA Total Power (Single Dish). It generates Jy/K calibration table.
   The task without 'infile' sub-parameter queries Jy/K DB from the environmental variable JYPERKDB_URL (https://asa.alma.cl/science/jy-kelvins), if available, via the internet to obtain factors and generate a caltable. 
   Factors can also be taken from the backup hosts or from a file in the local storage specified by the 'infile' sub-parameter to generate a caltable.
   Task queries the information with the following priorities (if available):
   - JYPERKDB_URL
   - Backup host 1
   - Backup host 2
   .
   .
   .
   - Infile

.. _Examples:

Examples
   getjyperkalma usage for an infile.
   
   ::
   
      getjyperkalma(vis='test.ms', caltable='test.G', infile='jyperk_factor_csv')
   Retrieve the factors with backup URLs if JYPERKDB_URL is unavailable, and fall back on one from backup_hosts.
   If JYPERKDB_URL is accessible, the fallback does not occur.
   
   ::
   
      getjyperkalma(vis='test.ms', caltable='test.G',backup_hosts=[https://backup1.url/jy-kelvins',"https://backup2.url/jy-kelvins"])


.. _Development:

Development
   No additional development details
