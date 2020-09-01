#
# stub function definition file for docstring parsing
#

def oldsplit(vis, outputvis='', datacolumn='corrected', field='', spw='', width='1', antenna='', timebin='0s', timerange='', array='', uvrange='', scan='', intent='', correlation='', observation='', combine='', keepflags=True, keepmms=False):
    r"""
Create a visibility subset from an existing visibility set

Parameters
   - **vis** (string) - Name of input measurement set
   - **outputvis** (string='') - Name of output measurement set
   - **datacolumn** (string='corrected') - Data column(s) to Oldsplit out
   - **field** ({string, stringArray, int, intArray}='') - Select field using ID(s) or name(s)
   - **spw** ({string, stringArray, int, intArray}='') - Select spectral window/channels
   - **width** ({string, stringArray, int, intArray}='1') - Number of channels to average to form one output channel
   - **antenna** ({string, stringArray, int, intArray}='') - Select data based on antenna/baseline
   - **timebin** (string='0s') - Interval for time averaging
   - **timerange** (string='') - Select data by time range
   - **array** (string='') - Select (sub)array(s) by array ID number
   - **uvrange** (string='') - Select data by baseline length (default units meters)
   - **scan** (string='') - Select data by scan numbers
   - **intent** (string='') - Select data by scan intents
   - **correlation** ({string, stringArray}='') - Select correlations
   - **observation** ({string, int}='') - Select by observation ID(s)
   - **keepflags** (bool=True) - If practical, keep *completely flagged rows* instead of dropping them.
   - **keepmms** (bool=False) - If the input is a multi-MS, make the output one,too.



    """
    pass
