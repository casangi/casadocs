#
# stub function definition file for docstring parsing
#

def nrobeamaverage(infile, datacolumn='float_data', field='', spw='', timerange='', scan='', beam='', timebin='0s', outfile=''):
    r"""
Average SD data over beams and do time averaging

Parameters
   - **infile** (string) - name of input SD dataset
   - **datacolumn** (string='float_data') - name of data column to be used ["data", "float_data", or "corrected_data"]
   - **field** (string='') - select data by field IDs and names, e.g. "3C2*" (""=all)
   - **spw** (string='') - select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
   - **timerange** (string='') - select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
   - **scan** (string='') - select data by scan numbers, e.g. "21~23" (""=all)
   - **beam** (string='') - beam IDs to be averaged over, e.g. "1,3" (""=all)
   - **timebin** (string='0s') - bin width for time averaging.
   - **outfile** (string='') - name of output file



    """
    pass
