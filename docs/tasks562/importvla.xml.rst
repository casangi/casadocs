importvla -- Import VLA archive file(s) to a measurement set -- import/export task
=======================================

Description
---------------------------------------

Imports an arbitrary number of VLA archive-format data sets into a
casa measurement set.  If more than one band is present, they will be
put in the same measurement set but in a separate spectral window.
The task will handle old style and new style VLA (after July 2007)
archive data and apply the tsys to the data and to the weights.



Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - archivefiles
     - :code:`numpy.array( [  ] )`
     - Name of input VLA archive file(s)
   * - vis
     - :code:`''`
     - Name of output visibility file
   * - bandname
     - :code:`''`
     - VLA frequency band name:\'\'=>obtain all bands in the archive file
   * - frequencytol
     - :code:`'150000.0Hz'`
     - Frequency shift to define a unique spectra window (Hz)
   * - project
     - :code:`''`
     - Project name: \'\' => all projects in files
   * - starttime
     - :code:`''`
     - Start time to search for data
   * - stoptime
     - :code:`''`
     - End time to search for data
   * - applytsys
     - :code:`True`
     - Apply nominal sensitivity scaling to data and weights
   * - autocorr
     - :code:`False`
     - Import autocorrelations to MS, if set to True
   * - antnamescheme
     - :code:`'new'`
     - \'old\' or \'new\'; \'VA04\' or \'04\' for VLA ant 4
   * - keepblanks
     - :code:`False`
     - Fill scans with blank (empty) source names (e.g. tipping scans)
   * - evlabands
     - :code:`False`
     - Use updated eVLA frequencies and bandwidths for bands and wavelengths


Parameter Explanations
=======================================



archivefiles
---------------------------------------

:code:`numpy.array( [  ] )`

Name of input VLA archive file(s)
                     Default: none.  Must be supplied

                        Examples: 
                        archivefiles = 'AP314_A959519.xp1'
                        archivefiles=['AP314_A950519.xp1',
                        'AP314_A950519.xp2']



vis
---------------------------------------

:code:`''`

Name of output visibility file
                     Default: none.  Must be supplied

                        Example: vis='NGC7538.ms'

                     NOTE: Will not over-write existing ms of same
                     name. A backup flag-file version 'Original' will
                     be made in vis.flagversions.  See help
                     flagmanager.
 


bandname
---------------------------------------

:code:`''`

VLA frequency band name:
                     Default: '' (obtain all bands in the archive
                     file)
                     Options: '4'=48-96 MHz,'P'=298-345
                     MHz,'L'=1.15-1.75 GHz, 'C'=4.2-5.1
                     GHz,'X'=6.8-9.6 GHz,'U'=13.5-16.3 GHz,
                     'K'=20.8-25.8 GHz,'Q'=38-51 GHz

                        Example: bandname='K'



frequencytol
---------------------------------------

:code:`'150000.0Hz'`

Tolerance in frequency shift in making spectral windows
                     Default: = 150000.0Hz'

                        Example: frequencytol = 1500000.0 (units = Hz)

                     For Doppler shifted data, less than 10000 Hz may
                     may produce too many unnecessary spectral
                     windows.



project
---------------------------------------

:code:`''`

Project name to import from archive files
                     Default: '' (all projects in file)

                        Example: project='AL519'             
                        Project = 'al519' or AL519 will work. 

                     WARNING: Do not include leading zeros; project =
                     'AL0519' will not work.



starttime
---------------------------------------

:code:`''`

Time after which data will be considered for importing
                     Default: '' (all)

                     syntax: starttime = '2003/1/31/05:05:23'. Date
                     must be included!



stoptime
---------------------------------------

:code:`''`

Time before which data will be considered for
importing
                     Default: '' (all)

                     syntax: starttime = '2003/1/31/08:05:23'. Date
                     must be included!



applytsys
---------------------------------------

:code:`True`

Apply data scaling and weight scaling by nominal
sensitivity (~Tsys)
                     Default: True (strongly recommended)
                     Options: True|False



autocorr
---------------------------------------

:code:`False`

Import autocorrelations to MS
                     Default: False (no autocorrelations)
                     Options: False|True



antnamescheme
---------------------------------------

:code:`'new'`

'old' or 'new' antenna names.
                     Default: 'new'
                     Options: new|old

                     * 'new' gives antnenna names 'VA04' or 'EA13 for
                       VLA telescopse 04 and 13 (EVLA)
                     * 'old' gives names '04' or '13'



keepblanks
---------------------------------------

:code:`False`

Should sources with blank names be filled into the data
base?
                     Default: False (do not fill)
                     Options: False|True

                     These scans are tipping scans (as of June 1,
                     2009) and should not be filled in the visibility
                     data set.



evlabands
---------------------------------------

:code:`False`

Use the EVLA's center frequency and bandwidths for
frequencies specified via wavelength or band.
                     Default: False
                     Options: False|True





