importfitsidi -- Convert a FITS-IDI file to a CASA visibility data set -- import/export task
=======================================

Description
---------------------------------------

Convert a FITS-IDI file to a CASA visiblity data set.
If several files are given, they will be concatenated into one MS.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - fitsidifile
     - :code:`numpy.array( [  ] )`
     - Name(s) of input FITS-IDI file(s)
   * - vis
     - :code:`''`
     - Name of output visibility file
   * - constobsid
     - :code:`False`
     - If True, give constant obs ID==0 to the data from all input fitsidi files (False = separate obs id for each file)
   * - scanreindexgap_s
     - :code:`float(0.)`
     - Min time gap (seconds) between integrations to start a new scan
   * - specframe
     - :code:`'GEO'`
     - Spectral reference frame for all spectral windows in the output MS


Parameter Explanations
=======================================



fitsidifile
---------------------------------------

:code:`numpy.array( [  ] )`

Name(s) of input FITS-IDI file(s)
                     Default: none (must be supplied)

                        Examples: 
                        fitsidifile='3C273XC1.IDI'
                        fitsidifile=['3C273XC1.IDI1','3C273XC1.IDI2']



vis
---------------------------------------

:code:`''`

Name of output visibility file
                     Default: none

                        Example: outputvis='3C273XC1.ms'



constobsid
---------------------------------------

:code:`False`

If True, give constant obs ID==0 to the data from all
input fitsidi files (False = separate obs id for each file)
                     Default: False (new obs id for each input file)
                     Options: False|True





scanreindexgap_s
---------------------------------------

:code:`float(0.)`

Min time gap (seconds) between integrations to start a
new scan
                     Default: 0. (no reindexing)

                     If > 0., a new scan is started whenever the gap
                     between two integrations is > the given value
                     (seconds) or when a new field starts or when the
                     ARRAY_ID changes.



specframe
---------------------------------------

:code:`'GEO'`

This frame will be used to set the spectral reference
frame for all spectral windows in the output MS
                     Default: GEO (geocentric)
                     Options: GEO|TOPO|LSRK|BARY

                     NOTE: if specframe is set to TOPO, the reference
                     location will be taken from the Observatories
                     table in the CASA data repository for the given
                     name of the observatory. You can edit that table
                     and add new rows.





