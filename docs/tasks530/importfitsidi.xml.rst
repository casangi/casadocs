importfitsidi -- Convert a FITS-IDI file to a CASA visibility data set -- import/export task
=======================================

Description
---------------------------------------
Convert a FITS-IDI file to a CASA visiblity data set.
	


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
     - 
   * - vis
     - :code:`''`
     - 
   * - constobsid
     - :code:`False`
     - 
   * - scanreindexgap_s
     - :code:`float(0.)`
     - 
   * - specframe
     - :code:`'GEO'`
     - 


Parameter Explanations
=======================================



fitsidifile
---------------------------------------

:code:`numpy.array( [  ] )`

Name(s) of input FITS-IDI file(s)


vis
---------------------------------------

:code:`''`

Name of output visibility file (MS)


constobsid
---------------------------------------

:code:`False`

If True, give constant obs ID==0 to the data from all input fitsidi files (False = separate obs id for each file)


scanreindexgap_s
---------------------------------------

:code:`float(0.)`

min time gap (seconds) between integrations to start a new scan


specframe
---------------------------------------

:code:`'GEO'`

spectral reference frame for all spectral windows in the output MS




