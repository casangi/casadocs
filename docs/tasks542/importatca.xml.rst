importatca -- Import ATCA RPFITS file(s) to a measurement set -- import/export task
=======================================

Description
---------------------------------------

      Imports an arbitrary number of ATCA RPFITS format data sets into
      a casa measurement set.  If more than one band is present, they
      will be put in the same measurement set but in a separate spectral
      window.  The task will handle both old ATCA and new CABB (after
      April 2009) archive data.
   


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - files
     - :code:`numpy.array( [  ] )`
     - 
   * - vis
     - :code:`''`
     - 
   * - options
     - :code:`''`
     - 
   * - spw
     - :code:`numpy.array( [  ] )`
     - 
   * - nscans
     - :code:`numpy.array( [  ] )`
     - 
   * - lowfreq
     - :code:`{'value': float(0.1), 'unit': 'GHz'}`
     - 
   * - highfreq
     - :code:`{'value': float(999), 'unit': 'GHz'}`
     - 
   * - fields
     - :code:`numpy.array( [  ] )`
     - 
   * - edge
     - :code:`float(8)`
     - 


Parameter Explanations
=======================================



files
---------------------------------------

:code:`numpy.array( [  ] )`

Name of input ATCA RPFits file(s)


vis
---------------------------------------

:code:`''`

Name of output visibility file (MeasurementSet)


options
---------------------------------------

:code:`''`

Processing options: birdie, reweight, noxycorr, fastmosaic, hires, noac (comma separated list)


spw
---------------------------------------

:code:`numpy.array( [  ] )`

Specify the spectral windows to use, default=all


nscans
---------------------------------------

:code:`numpy.array( [  ] )`

Number of scans to skip followed by number of scans to read


lowfreq
---------------------------------------

:code:`{'value': float(0.1), 'unit': 'GHz'}`

Lowest reference frequency to select


highfreq
---------------------------------------

:code:`{'value': float(999), 'unit': 'GHz'}`

Highest reference frequency to select


fields
---------------------------------------

:code:`numpy.array( [  ] )`

List of field names to select


edge
---------------------------------------

:code:`float(8)`

Percentage of edge channels to flag. For combined zooms, this specifies the percentage for a single zoom window




