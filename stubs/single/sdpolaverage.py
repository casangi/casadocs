#
# stub function definition file for docstring parsing
#

def sdpolaverage(infile, datacolumn='data', antenna='', field='', spw='', timerange='', scan='', intent='', polaverage='', outfile=''):
    r"""
Average SD spectra over polarisation

Parameters
   - **infile** (string) - name of input SD dataset [1]_
   - **datacolumn** (string='data') - name of data column to be used ["data", "float_data", or "corrected_data"] [2]_
   - **antenna** (string='') - select data by antenna name or ID, e.g. "PM03" [3]_
   - **field** (string='') - select data by field IDs and names, e.g. "3C2*" (""=all) [4]_
   - **spw** (string='') - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all) [5]_
   - **timerange** (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help) [6]_
   - **scan** (string='') - select data by scan numbers, e.g. "21~23" (""=all) [7]_
   - **intent** (string='') - select data by observational intent, e.g. "*ON_SOURCE*" (""=all) [8]_
   - **polaverage** (string='') - polarization averaging mode ("", "stokes" or "geometric"). [9]_
   - **outfile** (string='') - name of output file [10]_


Description
   Task **sdpolaverage** is used to export Single Dish MS data
   averaged over different polarizations, to obtain Stokes I from
   orthogonal autocorrelation pairs (XXYY/LLRR).

   .. rubric:: Polarization Average
      

   Two modes of polarizaton averaging are available. One is 'stokes'
   which is an average based on a formulation of Stokes parameter. In
   this mode, averaged data is calculated by (XX + YY) / 2 or (RR +
   LL) / 2. The other option is 'geometric', which is a conventional
   way of averaging in the field of single-dish data reduction; the
   output data is given by weighted average of XX and YY, or RR and
   LL.




Details
   Explanation of each parameter

.. [1] 
   **infile** (string)
      | name of input SD dataset
.. [2] 
   **datacolumn** (string='data')
      | name of data column to be used ["data", "float_data", or "corrected_data"]
.. [3] 
   **antenna** (string='')
      | select data by antenna name or ID, e.g. "PM03"
.. [4] 
   **field** (string='')
      | select data by field IDs and names, e.g. "3C2*" (""=all)
.. [5] 
   **spw** (string='')
      | select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
.. [6] 
   **timerange** (string='')
      | select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
.. [7] 
   **scan** (string='')
      | select data by scan numbers, e.g. "21~23" (""=all)
.. [8] 
   **intent** (string='')
      | select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
.. [9] 
   **polaverage** (string='')
      | polarization averaging mode ("", "stokes" or "geometric").
.. [10] 
   **outfile** (string='')
      | name of output file

    """
    pass
