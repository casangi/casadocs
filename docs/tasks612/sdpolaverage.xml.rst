sdpolaverage -- Average SD spectra over polarisation -- single dish task
=======================================

Description
---------------------------------------

    
    The task sdpolaverage exports data averaged over different polarisations.
    Scope of this task is to obtain Stokes I from orthogonal autocorrelation 
    pairs (XXYY/LLRR). Available options include:

    * '' (blank string as the default: polarisation averaging turned off)
    * stokes
    * geometric




Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infile
     - :code:`''`
     - name of input SD dataset
   * - datacolumn
     - :code:`'data'`
     - name of data column to be used ["data", "float_data", or "corrected_data"]
   * - antenna
     - :code:`''`
     - select data by antenna name or ID, e.g. "PM03"
   * - field
     - :code:`''`
     - select data by field IDs and names, e.g. "3C2*" (""=all)
   * - spw
     - :code:`''`
     - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
   * - timerange
     - :code:`''`
     - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   * - scan
     - :code:`''`
     - select data by scan numbers, e.g. "21~23" (""=all)
   * - intent
     - :code:`''`
     - select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
   * - polaverage
     - :code:`''`
     - polarization averaging mode ("", "stokes" or "geometric").
   * - outfile
     - :code:`''`
     - name of output file


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset


datacolumn
---------------------------------------

:code:`'data'`

name of data column to be used ["data", "float_data", or "corrected_data"]


antenna
---------------------------------------

:code:`''`

select data by antenna name or ID, e.g. "PM03"


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. "3C2*" (""=all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)


timerange
---------------------------------------

:code:`''`

select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. "21~23" (""=all)


intent
---------------------------------------

:code:`''`

select data by observational intent, e.g. "*ON_SOURCE*" (""=all)


polaverage
---------------------------------------

:code:`''`

polarization averaging mode ("", "stokes" or "geometric").


outfile
---------------------------------------

:code:`''`

name of output file




