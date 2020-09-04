#
# stub function definition file for docstring parsing
#

def nrobeamaverage(infile, datacolumn='float_data', field='', spw='', timerange='', scan='', beam='', timebin='0s', outfile=''):
    r"""
Average SD data over beams and do time averaging

Parameters
   - **infile** (string) - name of input SD dataset [1]_
   - **datacolumn** (string='float_data') - name of data column to be used ["data", "float_data", or "corrected_data"] [2]_
   - **field** (string='') - select data by field IDs and names, e.g. "3C2*" (""=all) [3]_
   - **spw** (string='') - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all) [4]_
   - **timerange** (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help) [5]_
   - **scan** (string='') - select data by scan numbers, e.g. "21~23" (""=all) [6]_
   - **beam** (string='') - beam IDs to be averaged over, e.g. "1,3" (""=all) [7]_
   - **timebin** (string='0s') - bin width for time averaging. [8]_
   - **outfile** (string='') - name of output file [9]_






Details
   Explanation of each parameter

.. [1] 
   **infile** (string)
      | name of input SD dataset
.. [2] 
   **datacolumn** (string='float_data')
      | name of data column to be used ["data", "float_data", or "corrected_data"]
.. [3] 
   **field** (string='')
      | select data by field IDs and names, e.g. "3C2*" (""=all)
.. [4] 
   **spw** (string='')
      | select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
.. [5] 
   **timerange** (string='')
      | select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
.. [6] 
   **scan** (string='')
      | select data by scan numbers, e.g. "21~23" (""=all)
.. [7] 
   **beam** (string='')
      | beam IDs to be averaged over, e.g. "1,3" (""=all)
.. [8] 
   **timebin** (string='0s')
      | bin width for time averaging.
.. [9] 
   **outfile** (string='')
      | name of output file

    """
    pass
