#
# stub function definition file for docstring parsing
#

def importgmrt(fitsfile, flagfile='', vis=''):
    r"""
Convert a UVFITS file to a CASA visibility data set

Parameters
   - **fitsfile** (string) - Name of input UV FITS file [1]_
   - **flagfile** ({string, stringArray}='') - List of files containing flagging information. [2]_
   - **vis** (string='') - Name of input visibility file [3]_


Description
   Converts a FITS file with visibility data from the Giant Metrewave
   Radio Telescope (GMRT) into a CASA MeasurementSet (MS).

   GMRT flag files can also be read and applied using the *flagfile*
   parameter.




Details
   Explanation of each parameter

.. [1] 
   **fitsfile** (string)
      | Name of input UV FITS file
      |                      Default: none
      | 
      |                         Example: fitsimage='3C273XC1.fits'
.. [2] 
   **flagfile** ({string, stringArray}='')
      | List of files containing flagging information.
      |                      Default: none
      | 
      |                         Examples:
      |                         flagfile='3c273XC1.flag'
      |                         flagfile=['3c273Cc1_1.flag','3c273Cc2_1.flag',']
.. [3] 
   **vis** (string='')
      | Name of input visibility file
      |                      Default: none
      | 
      |                         Example: vis='ngc5921.ms'

    """
    pass
