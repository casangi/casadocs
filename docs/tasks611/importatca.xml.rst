importatca -- Import ATCA RPFITS file(s) to a measurement set -- import/export task
=======================================

Description
---------------------------------------

Imports an arbitrary number of ATCA RPFITS format data sets into a
casa measurement set.  If more than one band is present, they will be
put in the same measurement set but in a separate spectral window.
The task will handle both old ATCA and new CABB (after April 2009)
archive data.



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
     - Name of input ATCA RPFits file(s)
   * - vis
     - :code:`''`
     - Name of output MeasurementSet
   * - options
     - :code:`''`
     - Processing options: birdie, reweight, noxycorr, fastmosaic, hires, noac (comma separated list)
   * - spw
     - :code:`numpy.array( [  ] )`
     - Select spectral window/channels
   * - nscans
     - :code:`numpy.array( [  ] )`
     - Number of scans to skip followed by number of scans to read
   * - lowfreq
     - :code:`{'value': float(0.1), 'unit': 'GHz'}`
     - Lowest reference frequency to select
   * - highfreq
     - :code:`{'value': float(999), 'unit': 'GHz'}`
     - Highest reference frequency to select
   * - fields
     - :code:`numpy.array( [  ] )`
     - List of field names to select
   * - edge
     - :code:`float(8)`
     - Percentage of edge channels to flag. For combined zooms, this specifies the percentage for a single zoom window


Parameter Explanations
=======================================



files
---------------------------------------

:code:`numpy.array( [  ] )`

Name of input ATCA RPFits file(s)


vis
---------------------------------------

:code:`''`

Name of output MeasurementSet
                     Default: none

                        Example: vis='mydata.ms'



options
---------------------------------------

:code:`''`

Processing options
                     Default: none
                     Options: birdie, reweight, noxycorr, fastmosaic,
                     hires, noac (comma separated list)

                     * birdie: (pre-CABB data only) discard edge
                       channels and channels affected by internal RFI
                     * reweight: (pre-CABB data only) suppress ringing
                       of RFI spikes by reweighting of the lag
                       spectrum 
                     * noxycorr: do not apply the xy phase correction
                       as derived from the switched noise calibration,
                       by default this is applied during loading of
                       the data
                     * fastmosaic: use this option if you are loading
                       mosaic data with many pointings and only one or
                       two integrations per pointing; this option
                       changes the tiling of the data to avoid
                       excessive I/O
                     * hires: use this option if you have data in time
                       binning mode (as used for pulsars) but you want
                       to make it look like data with very short
                       integration time (no bins)
                     * noac: discard the auto-correlation data



spw
---------------------------------------

:code:`numpy.array( [  ] )`

Select spectral window/channels
                     Default: '' (all spectral windows and channels)
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.



nscans
---------------------------------------

:code:`numpy.array( [  ] )`

Number of scans to skip followed by number of scans to
read
                     Default: [0, 0]



lowfreq
---------------------------------------

:code:`{'value': float(0.1), 'unit': 'GHz'}`

Lowest reference frequency to select
                     Default: 0.1GHz



highfreq
---------------------------------------

:code:`{'value': float(999), 'unit': 'GHz'}`

Highest reference frequency to select
                     Default: 999GHz



fields
---------------------------------------

:code:`numpy.array( [  ] )`

List of field names to select



edge
---------------------------------------

:code:`float(8)`

The edge parameter specifies how many edge channels to
discard as a percentage of the number of channels in each band.
                     Default: 8 (e.g., discard 82 channels from the
                     top and bottom of a 2048 channel spectrum)

                     For combined zooms, this specifies the percentage
                     for a single zoom window





