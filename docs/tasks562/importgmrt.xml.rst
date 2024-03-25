importgmrt -- Convert a UVFITS file to a CASA visibility data set -- import/export task
=======================================

Description
---------------------------------------

Convert a GRMT FITS file to a CASA visiblity data set.
Also read GMRT flag file(s) and flag data based on the contents of the
files.
    


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
   * - flagfile
     - :code:`''`
     - List of files containing flagging information.
   * - vis
     - :code:`''`
     - Name of input visibility file


Parameter Explanations
=======================================



fitsfile
---------------------------------------

:code:`''`

Name of input UV FITS file
                     Default: none

                        Example: fitsimage='3C273XC1.fits'



flagfile
---------------------------------------

:code:`''`

List of files containing flagging information.
                     Default: none

                        Examples:
                        flagfile='3c273XC1.flag'
                        flagfile=['3c273Cc1_1.flag','3c273Cc2_1.flag',']



vis
---------------------------------------

:code:`''`

Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'





