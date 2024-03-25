exportuvfits -- Convert a CASA visibility data set to a UVFITS file: -- import/export task
=======================================

Description
---------------------------------------




Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - vis
     - :code:`''`
     - 
   * - fitsfile
     - :code:`''`
     - 
   * - datacolumn
     - :code:`'corrected'`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - antenna
     - :code:`''`
     - 
   * - timerange
     - :code:`''`
     - 
   * - avgchan
     - :code:`int(1)`
     - 
   * - writesyscal
     - :code:`False`
     - 
   * - multisource
     - :code:`True`
     - 
   * - combinespw
     - :code:`True`
     - 
   * - writestation
     - :code:`True`
     - 
   * - padwithflags
     - :code:`False`
     - 
   * - overwrite
     - :code:`False`
     - 


Parameter Explanations
=======================================



vis
---------------------------------------

:code:`''`

Name of input visibility file


fitsfile
---------------------------------------

:code:`''`

Name of output UV FITS file


datacolumn
---------------------------------------

:code:`'corrected'`

Visibility file data column


field
---------------------------------------

:code:`''`

Select field using field id(s) or field name(s)


spw
---------------------------------------

:code:`''`

Select spectral window/channels


antenna
---------------------------------------

:code:`''`

Select data based on antenna/baseline


timerange
---------------------------------------

:code:`''`

Select data based on time range


avgchan
---------------------------------------

:code:`int(1)`

Channel averaging width (value > 1 indicates averaging)


writesyscal
---------------------------------------

:code:`False`

Write GC and TY tables, (Not yet available)


multisource
---------------------------------------

:code:`True`

Write in multi-source format? Set to False if only one source is selected. Note that diffmap does not work on multisource uvfits files.


combinespw
---------------------------------------

:code:`True`

Export the spectral windows as IFs


writestation
---------------------------------------

:code:`True`

Write station name instead of antenna name


padwithflags
---------------------------------------

:code:`False`

Fill in missing data with flags to fit IFs


overwrite
---------------------------------------

:code:`False`

Overwrite output file if it exists?




