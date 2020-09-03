#
# stub function definition file for docstring parsing
#

def importvla(archivefiles, vis='', bandname='', frequencytol='150000.0Hz', project='', starttime='', stoptime='', applytsys=True, autocorr=False, antnamescheme='new', keepblanks=False, evlabands=False):
    r"""
Import VLA archive file(s) to a measurement set

Parameters
   - **archivefiles** (stringArray) - Name of input VLA archive file(s)
   - **vis** (string='') - Name of output visibility file
   - **bandname** (string='') - VLA frequency band name:\'\'=>obtain all bands in the archive file
   - **frequencytol** (string='150000.0Hz') - Frequency shift to define a unique spectra window (Hz)
   - **project** (string='') - Project name: \'\' => all projects in files
   - **starttime** (string='') - Start time to search for data
   - **stoptime** (string='') - End time to search for data
   - **applytsys** (bool=True) - Apply nominal sensitivity scaling to data and weights
   - **autocorr** (bool=False) - Import autocorrelations to MS, if set to True
   - **antnamescheme** (string='new') - \'old\' or \'new\'; \'VA04\' or \'04\' for VLA ant 4
   - **keepblanks** (bool=False) - Fill scans with blank (empty) source names (e.g. tipping scans)
   - **evlabands** (bool=False) - Use updated eVLA frequencies and bandwidths for bands and wavelengths




    """
    pass
