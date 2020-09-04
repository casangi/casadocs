#
# stub function definition file for docstring parsing
#

def importvla(archivefiles, vis='', bandname='', frequencytol='150000.0Hz', project='', starttime='', stoptime='', applytsys=True, autocorr=False, antnamescheme='new', keepblanks=False, evlabands=False):
    r"""
Import VLA archive file(s) to a measurement set

Parameters
   - **archivefiles** (stringArray) - Name of input VLA archive file(s) [1]_
   - **vis** (string='') - Name of output visibility file [2]_
   - **bandname** (string='') - VLA frequency band name:\'\'=>obtain all bands in the archive file [3]_
   - **frequencytol** (string='150000.0Hz') - Frequency shift to define a unique spectra window (Hz) [4]_
   - **project** (string='') - Project name: \'\' => all projects in files [5]_
   - **starttime** (string='') - Start time to search for data [6]_
   - **stoptime** (string='') - End time to search for data [7]_
   - **applytsys** (bool=True) - Apply nominal sensitivity scaling to data and weights [8]_
   - **autocorr** (bool=False) - Import autocorrelations to MS, if set to True [9]_
   - **antnamescheme** (string='new') - \'old\' or \'new\'; \'VA04\' or \'04\' for VLA ant 4 [10]_
   - **keepblanks** (bool=False) - Fill scans with blank (empty) source names (e.g. tipping scans) [11]_
   - **evlabands** (bool=False) - Use updated eVLA frequencies and bandwidths for bands and wavelengths [12]_







Details
   Explanation of each parameter

.. [1] 
   **archivefiles** (stringArray)
      | Name of input VLA archive file(s)
      |                      Default: none.  Must be supplied
      | 
      |                         Examples: 
      |                         archivefiles = 'AP314_A959519.xp1'
      |                         archivefiles=['AP314_A950519.xp1',
      |                         'AP314_A950519.xp2']
.. [2] 
   **vis** (string='')
      | Name of output visibility file
      |                      Default: none.  Must be supplied
      | 
      |                         Example: vis='NGC7538.ms'
      | 
      |                      NOTE: Will not over-write existing ms of same
      |                      name. A backup flag-file version 'Original' will
      |                      be made in vis.flagversions.  See help
      |                      flagmanager.
.. [3] 
   **bandname** (string='')
      | VLA frequency band name:
      |                      Default: '' (obtain all bands in the archive
      |                      file)
      |                      Options: '4'=48-96 MHz,'P'=298-345
      |                      MHz,'L'=1.15-1.75 GHz, 'C'=4.2-5.1
      |                      GHz,'X'=6.8-9.6 GHz,'U'=13.5-16.3 GHz,
      |                      'K'=20.8-25.8 GHz,'Q'=38-51 GHz
      | 
      |                         Example: bandname='K'
.. [4] 
   **frequencytol** (string='150000.0Hz')
      | Tolerance in frequency shift in making spectral windows
      |                      Default: = 150000.0Hz'
      | 
      |                         Example: frequencytol = 1500000.0 (units = Hz)
      | 
      |                      For Doppler shifted data, less than 10000 Hz may
      |                      may produce too many unnecessary spectral
      |                      windows.
.. [5] 
   **project** (string='')
      | Project name to import from archive files
      |                      Default: '' (all projects in file)
      | 
      |                         Example: project='AL519'             
      |                         Project = 'al519' or AL519 will work. 
      | 
      |                      WARNING: Do not include leading zeros; project =
      |                      'AL0519' will not work.
.. [6] 
   **starttime** (string='')
      | Time after which data will be considered for importing
      |                      Default: '' (all)
      | 
      |                      syntax: starttime = '2003/1/31/05:05:23'. Date
      |                      must be included!
.. [7] 
   **stoptime** (string='')
      | Time before which data will be considered for
      | importing
      |                      Default: '' (all)
      | 
      |                      syntax: starttime = '2003/1/31/08:05:23'. Date
      |                      must be included!
.. [8] 
   **applytsys** (bool=True)
      | Apply data scaling and weight scaling by nominal
      | sensitivity (~Tsys)
      |                      Default: True (strongly recommended)
      |                      Options: True|False
.. [9] 
   **autocorr** (bool=False)
      | Import autocorrelations to MS
      |                      Default: False (no autocorrelations)
      |                      Options: False|True
.. [10] 
   **antnamescheme** (string='new')
      | 'old' or 'new' antenna names.
      |                      Default: 'new'
      |                      Options: new|old
      | 
      |                      * 'new' gives antnenna names 'VA04' or 'EA13 for
      |                        VLA telescopse 04 and 13 (EVLA)
      |                      * 'old' gives names '04' or '13'
.. [11] 
   **keepblanks** (bool=False)
      | Should sources with blank names be filled into the data
      | base?
      |                      Default: False (do not fill)
      |                      Options: False|True
      | 
      |                      These scans are tipping scans (as of June 1,
      |                      2009) and should not be filled in the visibility
      |                      data set.
.. [12] 
   **evlabands** (bool=False)
      | Use the EVLA's center frequency and bandwidths for
      | frequencies specified via wavelength or band.
      |                      Default: False
      |                      Options: False|True

    """
    pass
