

.. _Description:

Description
   Task **nrobeamaverage** is dedicated to the data obtained with the multi-beam receivers in the NRO45m telescope,
   and is used to export Single Dish MS data averaged over different beams.

   This task is in particular useful for the data observed in the On-On mode, in which two beams are used to observe
   same source position on the sky. When one beam (beam-1) points to the source position, the other beam (beam-3)
   points the reference position, and when beam-3 observes the source position, beam-1 points to its reference position.
   Compared to the observations with a single beam, this mode can reduce the dead-time due to observations of the reference
   position, and observers can obtain betterr sensitivities by averaging the spectra obtained with the two beams. This task
   can be used in this averaging process.

   Details of the On-On mode can be seen in the NRO official web page
   (https://www.nro.nao.ac.jp/~nro45mrt/html/obs/nobs/scan.html#on-on).


.. _Examples:

Examples
   Average the spectra over all the beams:

   ::

      nrobeamaverage(infile='sd_data.ms', outfile='sd_data_bave.ms')

   Average the spectra over the selected beam IDs:

   ::

      nrobeamaverage(infile='sd_data.ms', outfile='sd_data_bave.ms', beam='1,3')

   You can apply time-averaging at the same time:

   ::

      nrobeamaverage(infile='sd_data.ms', outfile='sd_data_bave.ms', timebin='3600s')



.. _Development:

Development
   No additional development details

