importuvfits -- Convert a UVFITS file to a CASA visibility data set -- import/export task
=======================================

Description
---------------------------------------
Convert a UVITS file to a CASA visiblity data set.
                Don\'t forget to flag autocorrelations using taskname flagdata, autocorr = true
    


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - fitsfile
     - :code:`''`
     - Name of input UV FITS file
   * - vis
     - :code:`''`
     - Name of output visibility file (MS)
   * - antnamescheme
     - :code:`'old'`
     - VLA/EVLA/CARMA only; \'new\' or \'old\'; \'VA04\' or \'04\' for VLA ant 4


Parameter Explanations
=======================================



fitsfile
---------------------------------------

:code:`''`

Name of input UV FITS file


vis
---------------------------------------

:code:`''`

Name of output visibility file (MS)


antnamescheme
---------------------------------------

:code:`'old'`

VLA/EVLA/CARMA only; \'new\' or \'old\'; \'VA04\' or \'04\' for VLA ant 4




