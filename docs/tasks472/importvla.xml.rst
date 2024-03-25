importvla -- Import VLA archive file(s) to a measurement set -- import/export task
=======================================

Description
---------------------------------------

      Imports an arbitrary number of VLA archive-format data sets into
      a casa measurement set.  If more than one band is present, they
      will be put in the same measurement set but in a separate spectral
      window.  The task will handle old style and new style VLA (after
      July 2007) archive data and apply the tsys to the data and to
      the weights.
   


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
     - 
   * - vis
     - :code:`''`
     - 
   * - bandname
     - :code:`''`
     - 
   * - frequencytol
     - :code:`{'value': float(150000.0), 'unit': 'Hz'}`
     - 
   * - project
     - :code:`''`
     - 
   * - starttime
     - :code:`''`
     - 
   * - stoptime
     - :code:`''`
     - 
   * - applytsys
     - :code:`True`
     - 
   * - autocorr
     - :code:`False`
     - 
   * - antnamescheme
     - :code:`'new'`
     - 
   * - keepblanks
     - :code:`False`
     - 
   * - evlabands
     - :code:`False`
     - 


Parameter Explanations
=======================================



archivefiles
---------------------------------------

:code:`numpy.array( [  ] )`

Name of input VLA archive file(s)


vis
---------------------------------------

:code:`''`

Name of output visibility file


bandname
---------------------------------------

:code:`''`

VLA frequency band name:\'\'=>obtain all bands in the archive file


frequencytol
---------------------------------------

:code:`{'value': float(150000.0), 'unit': 'Hz'}`

Frequency shift to define a unique spectra window (Hz)


project
---------------------------------------

:code:`''`

Project name: \'\' => all projects in files


starttime
---------------------------------------

:code:`''`

start time to search for data


stoptime
---------------------------------------

:code:`''`

end time to search for data


applytsys
---------------------------------------

:code:`True`

apply nominal sensistivity scaling to data and weights


autocorr
---------------------------------------

:code:`False`

import autocorrelations to ms, if set to True


antnamescheme
---------------------------------------

:code:`'new'`

\'old\' or \'new\'; \'VA04\' or \'04\' for VLA ant 4


keepblanks
---------------------------------------

:code:`False`

Fill scans with blank (empty) source names (e.g. tipping scans)


evlabands
---------------------------------------

:code:`False`

Use updated eVLA frequencies and bandwidths for bands and wavelengths




