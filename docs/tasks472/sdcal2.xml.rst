sdcal2 -- ASAP SD calibration task -- single dish task
=======================================

Description
---------------------------------------

Task sdcal2 is an implementation of a calibration scheme like as 
interferometry, i.e., generate caltables and apply them. Available 
calibration modes are 'ps', 'otf', 'otfraster', and 'tsys'. Those 
modes generates caltables for sky or Tsys calibration. Those 
caltables can be applied to the data by using calmode 'apply'.

The above three calibration modes, 'ps', 'otf', and 'otfraster',
generate sky calibration tables. The user should choose appropriate 
calibration mode depending on the data. Use case for each mode is 
as follows:

    'ps': position switch (including OTF) with explicit
          reference (OFF) spectra
    'otf': non-raster OTF scan without explicit OFFs
           (e.g. Lissajous, double circle, etc.)
           intends to calibrate fast scan data
    'otfraster': raster OTF scan without explicit OFFs

So, if the data contains explicit reference spectra, 'ps' should
be used. Otherwise, 'otfraster' and 'otf' are appropriate for raster 
OTF and non-raster OTF, respectively. In 'otf' and 'otfraster' modes, 
the task first try to find several integrations near edge as OFF 
spectra, then the data are calibrated using those OFFs. If the 
observing pattern is raster, you should use the 'otfraster' mode to 
calibrate data. Otherwise, the 'otf' mode should be used. For detail 
about edge marking, see inline help of sd.edgemarker module and its 
methods. Those modes are designed for OTF observations without 
explicit OFF spectra. However, these modes should work even if 
explicit reference spectra exist. In this case, these spectra will 
be ignored and spectra near edges detected by edge marker will be 
used as reference.

Except for how to choose OFFs, the procedure to derive calibrated
spectra is common for the above three modes. Selected (or preset) 
OFF integrations are separated by its continuity in time domain, 
averaged in each segment, then interpolated to timestamps for ON 
integrations. Effectively, it means that OFF integrations are 
averaged by each OFF spectrum for 'ps' mode, averaged by either ends 
of each raster row for 'otfraster' mode, averaged by each temporal 
segments of detected edges for 'otf' mode. The formula for calibrated 
spectrum is

    Tsys * (ON - OFF) / OFF. 

  


Parameters
---------------------------------------

.. list-table:: Title
   :widths: 25 25 50 
   :header-rows: 1
   
   * - Parameter
     - Default
     - Description
   * - infile
     - :code:`''`
     - 
   * - calmode
     - :code:`'ps'`
     - SD calibration mode [\'ps\',\'otf\',\'otfraster\',\'tsys\',\'apply\', and their possible combinations]
   * - fraction
     - :code:`'10%'`
     - 
   * - noff
     - :code:`int(-1)`
     - 
   * - width
     - :code:`float(0.5)`
     - 
   * - elongated
     - :code:`False`
     - 
   * - tsysavg
     - :code:`False`
     - 
   * - tsysspw
     - :code:`''`
     - 
   * - applytable
     - :code:`''`
     - 
   * - interp
     - :code:`''`
     - 
   * - spwmap
     - :code:`*UNKNOWN*`
     - 
   * - field
     - :code:`''`
     - 
   * - spw
     - :code:`''`
     - 
   * - scan
     - :code:`''`
     - 
   * - pol
     - :code:`''`
     - 
   * - outfile
     - :code:`''`
     - 
   * - overwrite
     - :code:`False`
     - overwrite the output file if already exists [True, False]


Parameter Explanations
=======================================



infile
---------------------------------------

:code:`''`

name of input SD dataset (must be in scantable format)


calmode
---------------------------------------

:code:`'ps'`

SD calibration mode


fraction
---------------------------------------

:code:`'10%'`

fraction of the OFF data to mark


noff
---------------------------------------

:code:`int(-1)`

number of the OFF data to mark


width
---------------------------------------

:code:`float(0.5)`

width of the pixel for edge detection


elongated
---------------------------------------

:code:`False`

whether observed area is elongated in one direction or not


tsysavg
---------------------------------------

:code:`False`

Whether Tsys is averaged in spectral axis or not


tsysspw
---------------------------------------

:code:`''`

list of IF IDs (spectral windows) and their channel ranges of averaging for Tsys calibration.


applytable
---------------------------------------

:code:`''`

(List of) sky and/or tsys tables


interp
---------------------------------------

:code:`''`

Interpolation type in time[,freq]. Valid options are "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").


spwmap
---------------------------------------

:code:`*UNKNOWN*`

A dictionary indicating IFNO combinations to apply Tsys calibration to target. The key should be IFNO for Tsys calibration and its associated value must be a list of science IFNOs to be applied.


field
---------------------------------------

:code:`''`

select data by field IDs and names, e.g. \'3C2*\' (\'\' = all)


spw
---------------------------------------

:code:`''`

select data by IF IDs (spectral windows), e.g., \'3,5,7\' (\'\' = all)


scan
---------------------------------------

:code:`''`

select data by scan numbers, e.g. \'21~23\' (\'\'=all)


pol
---------------------------------------

:code:`''`

select data by polarization IDs, e.g, \'0,1\' (\'\' = all)


outfile
---------------------------------------

:code:`''`

name of output file (See a WARNING in help)


overwrite
---------------------------------------

:code:`False`

overwrite the output file if already exists




