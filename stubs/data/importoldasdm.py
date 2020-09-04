#
# stub function definition file for docstring parsing
#

def importoldasdm(asdm, corr_mode='all', srt='all', time_sampling='all', ocorr_mode='co', compression=False):
    r"""
Convert an ALMA Science Data Model observation into a CASA visibility file

Parameters
   - **asdm** (string) -  [1]_
   - **corr_mode** (string='all') -  [2]_
   - **srt** (string='all') -  [3]_
   - **time_sampling** (string='all') -  [4]_
   - **ocorr_mode** (string='co') -  [5]_
   - **compression** (bool=False) -  [6]_






Details
   Explanation of each parameter

.. [1] 
   **asdm** (string)
      | Name of input asdm directory (on disk)
.. [2] 
   **corr_mode** (string='all')
      | specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao co ac all separated by whitespaces is expected
.. [3] 
   **srt** (string='all')
      | specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr ca bw all separated by whitespaces is expected
.. [4] 
   **time_sampling** (string='all')
      | specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i si all separated by whitespaces is expected
.. [5] 
   **ocorr_mode** (string='co')
      | output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca)
.. [6] 
   **compression** (bool=False)
      | Flag for turning on data compression

    """
    pass
